#!/bin/zsh
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
VENV_PYTHON="/Users/con11/Documents/Codex/davinci-resolve-mcp-2.3.0-venv/bin/python"
LOG_DIR="$ROOT_DIR/logs"
PORT="${DAVINCI_RESOLVE_MCP_PORT:-8766}"
HOST="${DAVINCI_RESOLVE_MCP_HOST:-127.0.0.1}"

mkdir -p "$LOG_DIR"

export RESOLVE_SCRIPT_API="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting"
export RESOLVE_SCRIPT_LIB="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/fusionscript.so"
export PYTHONPATH="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules"

cd "$ROOT_DIR"
exec "$VENV_PYTHON" "$ROOT_DIR/src/server.py" --transport http --host "$HOST" --port "$PORT" >>"$LOG_DIR/http-server.stdout.log" 2>>"$LOG_DIR/http-server.stderr.log"
