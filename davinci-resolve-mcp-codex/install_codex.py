#!/usr/bin/env python3
"""
DaVinci Resolve MCP Server — Codex Installer

Configures Codex Desktop via ~/.codex/config.toml.

Default behavior:
  - macOS: use authenticated streamable-http + launchd
  - Windows/Linux: use stdio

Examples:
  python install_codex.py
  python install_codex.py --transport stdio
  python install_codex.py --transport streamable-http --port 8766
  python install_codex.py --dry-run
"""

from __future__ import annotations

import argparse
import os
import platform
import re
import secrets
import shutil
import subprocess
import sys
import textwrap
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from install import (
    VERSION,
    SYSTEM,
    bold,
    build_server_env,
    check_resolve_running,
    create_venv,
    cyan,
    find_resolve_paths,
    get_venv_python,
    green,
    install_dependencies,
    is_mac,
    platform_name,
    verify_resolve_connection,
    yellow,
)


DEFAULT_SERVER_NAME = "davinci_resolve"
DEFAULT_HTTP_PORT = 8766
DEFAULT_HTTP_HOST = "127.0.0.1"
DEFAULT_HTTP_PATH = "/mcp"
DEFAULT_TRANSPORT = "streamable-http"
LAUNCH_AGENT_LABEL = "com.con11.davinci-resolve-mcp-http"


def home() -> Path:
    return Path.home()


def codex_config_path() -> Path:
    return home() / ".codex" / "config.toml"


def codex_backup_path() -> Path:
    return home() / ".codex" / "config.toml.bak.davinci-resolve-codex"


def launch_agent_path() -> Path:
    return home() / "Library" / "LaunchAgents" / f"{LAUNCH_AGENT_LABEL}.plist"


def print_banner() -> None:
    title = f"DaVinci Resolve MCP — Codex Installer v{VERSION}"
    print()
    print(bold("  ╔══════════════════════════════════════════════════════╗"))
    print(bold(f"  ║{title:^54}║"))
    print(bold("  ╚══════════════════════════════════════════════════════╝"))
    print()


def resolve_transport(requested: str | None) -> str:
    if requested == "http":
        return "streamable-http"
    if requested:
        return requested
    return DEFAULT_TRANSPORT if is_mac() else "stdio"


def generate_token() -> str:
    return secrets.token_urlsafe(24)


def toml_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def build_stdio_block(
    server_name: str,
    python_path: Path,
    server_path: Path,
    api_path: str | None,
    lib_path: str | None,
) -> str:
    env = build_server_env(python_path, api_path, lib_path, system=SYSTEM)
    lines = [
        f"[mcp_servers.{server_name}]",
        'type = "stdio"',
        f'command = "{toml_escape(str(python_path))}"',
        f'args = ["{toml_escape(str(server_path))}"]',
        "startup_timeout_sec = 120",
        "",
        f"[mcp_servers.{server_name}.env]",
    ]
    for key in ("RESOLVE_SCRIPT_API", "RESOLVE_SCRIPT_LIB", "PYTHONPATH", "PYTHONHOME"):
        value = env.get(key)
        if value:
            lines.append(f'{key} = "{toml_escape(value)}"')
    return "\n".join(lines) + "\n"


def build_http_block(server_name: str, host: str, port: int, token: str) -> str:
    return "\n".join(
        [
            f"[mcp_servers.{server_name}]",
            f'url = "http://{host}:{port}{DEFAULT_HTTP_PATH}"',
            'http_headers = { Authorization = "Bearer ' + toml_escape(token) + '" }',
            "startup_timeout_sec = 120",
            "",
        ]
    )


def replace_or_append_server_block(text: str, server_name: str, new_block: str) -> str:
    pattern = re.compile(
        rf"(?ms)^\[mcp_servers\.{re.escape(server_name)}\]\n.*?(?=^\[(?!mcp_servers\.{re.escape(server_name)}(?:\.|]))|\Z)"
    )
    if pattern.search(text):
        return pattern.sub(new_block, text).rstrip() + "\n"
    return text.rstrip() + "\n\n" + new_block


def update_codex_config(config_path: Path, server_name: str, block: str, dry_run: bool) -> None:
    config_path.parent.mkdir(parents=True, exist_ok=True)
    existing = config_path.read_text() if config_path.exists() else ""
    updated = replace_or_append_server_block(existing, server_name, block)

    if dry_run:
        print(f"\n  {cyan('Config preview')} → {config_path}")
        print()
        for line in block.strip().splitlines():
            print(f"    {line}")
        print()
        return

    if config_path.exists():
        shutil.copy2(config_path, codex_backup_path())
    config_path.write_text(updated)


def build_launch_agent_plist(
    python_path: Path,
    server_path: Path,
    project_dir: Path,
    api_path: str | None,
    lib_path: str | None,
    host: str,
    port: int,
    token: str,
) -> str:
    env = build_server_env(python_path, api_path, lib_path, system=SYSTEM)
    env["DAVINCI_MCP_HOST"] = host
    env["DAVINCI_MCP_PORT"] = str(port)
    env["DAVINCI_MCP_TOKEN"] = token

    env_lines = []
    for key in (
        "RESOLVE_SCRIPT_API",
        "RESOLVE_SCRIPT_LIB",
        "PYTHONPATH",
        "PYTHONHOME",
        "DAVINCI_MCP_HOST",
        "DAVINCI_MCP_PORT",
        "DAVINCI_MCP_TOKEN",
    ):
        value = env.get(key)
        if value:
            env_lines.extend(
                [
                    f"    <key>{key}</key>",
                    f"    <string>{value}</string>",
                ]
            )

    logs_dir = project_dir / "logs"
    stdout_path = logs_dir / "launchd.stdout.log"
    stderr_path = logs_dir / "launchd.stderr.log"

    return textwrap.dedent(
        f"""\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
          <key>Label</key>
          <string>{LAUNCH_AGENT_LABEL}</string>

          <key>ProgramArguments</key>
          <array>
            <string>{python_path}</string>
            <string>{server_path}</string>
            <string>--transport</string>
            <string>streamable-http</string>
          </array>

          <key>RunAtLoad</key>
          <true/>

          <key>KeepAlive</key>
          <true/>

          <key>WorkingDirectory</key>
          <string>{project_dir}</string>

          <key>StandardOutPath</key>
          <string>{stdout_path}</string>

          <key>StandardErrorPath</key>
          <string>{stderr_path}</string>

          <key>EnvironmentVariables</key>
          <dict>
        {chr(10).join(env_lines)}
          </dict>
        </dict>
        </plist>
        """
    )


def install_launch_agent(
    python_path: Path,
    server_path: Path,
    project_dir: Path,
    api_path: str | None,
    lib_path: str | None,
    host: str,
    port: int,
    token: str,
    dry_run: bool,
) -> None:
    if not is_mac():
        return

    plist_path = launch_agent_path()
    plist_path.parent.mkdir(parents=True, exist_ok=True)
    (project_dir / "logs").mkdir(parents=True, exist_ok=True)
    plist_text = build_launch_agent_plist(
        python_path, server_path, project_dir, api_path, lib_path, host, port, token
    )

    if dry_run:
        print(f"\n  {cyan('LaunchAgent preview')} → {plist_path}")
        print(f"    label: {LAUNCH_AGENT_LABEL}")
        print(f"    command: {python_path} {server_path} --transport streamable-http")
        print(f"    token: {token}")
        return

    plist_path.write_text(plist_text)
    uid = os.getuid()
    subprocess.run(
        ["launchctl", "bootout", f"gui/{uid}", str(plist_path)],
        check=False,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["launchctl", "bootstrap", f"gui/{uid}", str(plist_path)],
        check=True,
    )
    subprocess.run(
        ["launchctl", "kickstart", "-k", f"gui/{uid}/{LAUNCH_AGENT_LABEL}"],
        check=True,
    )


def ensure_python_env(
    project_dir: Path,
    no_venv: bool,
    python_override: str | None,
    dry_run: bool,
) -> Path:
    if python_override:
        return Path(python_override).expanduser().resolve()

    if no_venv:
        return Path(sys.executable).resolve()

    venv_path = project_dir / "venv"
    venv_python = get_venv_python(venv_path)

    if dry_run:
        return venv_python if venv_python.exists() else Path(sys.executable).resolve()

    if not venv_python.exists():
        create_venv(venv_path)

    try:
        result = subprocess.run(
            [str(venv_python), "-c", "import mcp; print('ok')"],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.stdout.strip() != "ok":
            install_dependencies(venv_path, project_dir)
    except Exception:
        install_dependencies(venv_path, project_dir)

    return venv_python


def verify_http_endpoint(host: str, port: int, token: str) -> tuple[bool, str]:
    url = f"http://{host}:{port}{DEFAULT_HTTP_PATH}"
    last_error = "unknown error"
    for attempt in range(10):
        req = Request(url, headers={"Authorization": f"Bearer {token}"})
        try:
            with urlopen(req, timeout=5) as response:
                return True, f"HTTP bridge responded with {response.status}"
        except HTTPError as exc:
            if exc.code == 401:
                return False, "HTTP bridge rejected the bearer token"
            if 200 <= exc.code < 500:
                return True, f"HTTP bridge responded with {exc.code}"
            last_error = f"HTTP bridge returned {exc.code}"
        except URLError as exc:
            last_error = str(exc.reason)
        except Exception as exc:
            last_error = str(exc)
        if attempt < 9:
            time.sleep(0.5)
    return False, last_error


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Install DaVinci Resolve MCP for Codex Desktop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--transport",
        choices=("stdio", "streamable-http", "http"),
        default=None,
        help="Codex transport to configure. Defaults to streamable-http on macOS, stdio elsewhere.",
    )
    parser.add_argument(
        "--host",
        default=DEFAULT_HTTP_HOST,
        help="HTTP bind host for the local bridge.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=DEFAULT_HTTP_PORT,
        help="HTTP bind port for the local bridge.",
    )
    parser.add_argument(
        "--server-name",
        default=DEFAULT_SERVER_NAME,
        help="MCP server name inside ~/.codex/config.toml",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Pinned bearer token for streamable-http. Defaults to a generated token.",
    )
    parser.add_argument(
        "--python",
        default=None,
        help="Python executable to use instead of creating/reusing ./venv",
    )
    parser.add_argument(
        "--no-venv",
        action="store_true",
        help="Use the current Python instead of creating ./venv",
    )
    parser.add_argument(
        "--server",
        default=None,
        help="Path to src/server.py",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without writing files or starting launchd",
    )
    args = parser.parse_args()

    print_banner()

    project_dir = Path(__file__).resolve().parent
    transport = resolve_transport(args.transport)
    server_path = Path(args.server).expanduser().resolve() if args.server else project_dir / "src" / "server.py"
    python_path = ensure_python_env(project_dir, args.no_venv, args.python, args.dry_run)
    api_path, lib_path = find_resolve_paths()
    resolve_running = check_resolve_running()
    token = args.token or generate_token()

    print(f"  Platform:  {bold(platform_name())}")
    print(f"  Transport: {bold(transport)}")
    print(f"  Python:    {python_path}")
    print(f"  Server:    {server_path}")
    print(f"  API Path:  {green(api_path) if api_path else yellow('Not found')}")
    print(f"  Library:   {green(lib_path) if lib_path else yellow('Not found')}")
    print(f"  Resolve:   {green('Running') if resolve_running else yellow('Not running')}")
    if transport == "streamable-http":
        print(f"  URL:       http://{args.host}:{args.port}{DEFAULT_HTTP_PATH}")

    if not server_path.exists():
        print(f"\n  {yellow('Error:')} server script not found: {server_path}")
        sys.exit(1)

    if transport == "streamable-http":
        block = build_http_block(args.server_name, args.host, args.port, token)
    else:
        block = build_stdio_block(args.server_name, python_path, server_path, api_path, lib_path)

    update_codex_config(codex_config_path(), args.server_name, block, args.dry_run)

    if transport == "streamable-http":
        install_launch_agent(
            python_path,
            server_path,
            project_dir,
            api_path,
            lib_path,
            args.host,
            args.port,
            token,
            args.dry_run,
        )

    print()
    print(f"  {green('Codex config updated') if not args.dry_run else cyan('Dry run complete')}")
    print(f"  Config:    {codex_config_path()}")
    if transport == "streamable-http" and is_mac():
        print(f"  Launchd:   {launch_agent_path()}")

    if args.dry_run:
        print()
        return

    if transport == "streamable-http":
        ok, message = verify_http_endpoint(args.host, args.port, token)
        print(f"  Verify:    {green(message) if ok else yellow(message)}")
    elif api_path:
        ok, message = verify_resolve_connection(python_path, api_path, lib_path)
        print(f"  Verify:    {green(message) if ok else yellow(message)}")

    print()
    print(bold("  Next steps"))
    if transport == "streamable-http":
        print("    1. Restart Codex Desktop so it reloads ~/.codex/config.toml")
        print("    2. Keep DaVinci Resolve Studio running with External scripting set to Local")
        print("    3. Ask Codex to list Resolve tools or read the current project name")
    else:
        print("    1. Restart Codex Desktop so it reloads ~/.codex/config.toml")
        print("    2. If Codex cannot connect but Terminal can, rerun with --transport streamable-http")
        print("    3. Ask Codex to list Resolve tools or read the current project name")
    print()


if __name__ == "__main__":
    main()
