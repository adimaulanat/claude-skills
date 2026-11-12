#!/usr/bin/env bash
# bash render-images.sh <page.html> <out-dir> <id:filename> [<id:filename> ...]
# Renders each #id of a 1080x1350 HTML page to a PNG with headless Chrome (one slide per :target).
# Example: bash render-images.sh threads.html ../threads post-02:post-02-naskah.png post-07:post-07-score.png
set -euo pipefail
CH="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
[ -x "$CH" ] || { echo "Chrome not found; set CHROME=/path/to/chrome" >&2; exit 1; }
PAGE="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"; OUT="$2"; shift 2
mkdir -p "$OUT"; OUT="$(cd "$OUT" && pwd)"
for pair in "$@"; do
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1080,1350 \
    --screenshot="$OUT/${pair#*:}" "file://$PAGE#${pair%%:*}" >/dev/null 2>&1
done
ls -la "$OUT"
