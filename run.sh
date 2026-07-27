#!/usr/bin/env bash
# Launch the D&D Character Builder from source
set -e
cd "$(dirname "$0")"
exec python3 main.py "$@"
