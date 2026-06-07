# Codex Notes

## Overview

DaVinci Resolve MCP Server exposes the DaVinci Resolve Scripting API over MCP.

There are two entry modes:

- `src/server.py`
  Default compound server with 27 tools.
- `src/resolve_mcp_server.py`
  Full granular server with 354 tools.

For Codex Desktop on macOS, prefer running the server over local HTTP instead of direct stdio. Codex's sandbox can block Resolve IPC even when Resolve itself is configured correctly.

## Codex Install Path

Recommended Codex setup:

1. Create or reuse a local venv.
2. Run the server outside Codex's sandbox.
3. Point `~/.codex/config.toml` at a local HTTP MCP endpoint.

The repo includes a Codex-specific installer:

```bash
python install_codex.py
```

Useful variants:

```bash
python install_codex.py --dry-run
python install_codex.py --transport stdio
python install_codex.py --transport http --port 8766
```

## Recommended Runtime

- Python `3.10` to `3.12` is preferred.
- Python `3.13+` may import `DaVinciResolveScript` successfully but still fail at `scriptapp("Resolve")`.
- DaVinci Resolve must be `Studio`.
- Resolve setting must be:
  `Preferences > General > External scripting using > Local`

## Codex Verification

When checking whether Codex-compatible setup really works, verify in this order:

1. Resolve scripting works outside Codex sandbox.
2. HTTP bridge is alive on `127.0.0.1`.
3. MCP handshake succeeds.
4. Codex config points at the bridge.

Expected HTTP health behavior:

- `curl http://127.0.0.1:8766/` should return `406 Not Acceptable`
- This is normal for a live MCP HTTP server without MCP headers

Good protocol-level verification is:

- MCP `initialize`
- MCP `list_tools`

If those succeed, Codex should be able to connect after reload.

## Code Structure

- `src/server.py`
  Compound server entrypoint and grouped tools.
- `src/resolve_mcp_server.py`
  Full granular tool entrypoint.
- `src/granular/`
  Per-object granular tool implementations.
- `src/utils/`
  Shared helpers for platform detection, stdio transport, Resolve connection, and safety helpers.
- `install.py`
  Generic multi-client installer.
- `install_codex.py`
  Codex-specific installer.

## Editing Rules

- Keep the compound server and granular server behavior aligned when changing shared Resolve semantics.
- Helper functions should stay internal with `_` prefixes when not part of MCP tool surface.
- Any path that Resolve itself writes to must stay compatible with `_resolve_safe_dir()`.
- Do not assume Codex can use stdio safely on macOS. Preserve HTTP transport support.
- Keep log directory writes under the project directory writable by the launching user.

## Transport Notes

`src/server.py` supports:

- `stdio`
- `streamable-http` via `--transport http`

For Codex packaging, HTTP support is not optional on macOS. Treat it as first-class.

## Release Notes

When bumping the version, update all matching version references:

- `src/server.py`
- `src/resolve_mcp_server.py`
- `README.md` version badge
- `README.md` changelog section

If transport behavior, tool count, or coverage changes, update related README claims too.

## Practical Debugging

If Resolve access fails in Codex:

1. Test `fuscript` or plain Python outside Codex sandbox.
2. If outside-sandbox access works but Codex stdio fails, use HTTP bridge.
3. Check `logs/server.log`
4. On macOS HTTP mode, check `launchd` logs and `~/.codex/config.toml`

Symptoms and likely causes:

- `scriptapp("Resolve")` returns `None` only inside Codex
  Likely sandboxed stdio IPC failure.
- `import DaVinciResolveScript` works but Resolve handle is null everywhere
  Usually free edition, wrong scripting setting, or incompatible Python.
- HTTP endpoint returns `406`
  Usually healthy.
- HTTP endpoint refuses connection
  Bridge process is not running or failed to bind.
