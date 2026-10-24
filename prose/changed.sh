#!/bin/sh
# Lint the public texts changed since origin/main (README, notes, pages, llms.txt) before a push.
# Run from the root of any repository: sh /path/to/method/prose/changed.sh
DIR=$(cd "$(dirname "$0")" && pwd)
git fetch -q origin 2>/dev/null
FILES=$( (git diff --name-only origin/main...HEAD; git diff --name-only; git diff --name-only --cached) 2>/dev/null \
  | sort -u | grep -E '\.(md|txt|html)$' | while read -r f; do [ -f "$f" ] && echo "$f"; done)
[ -z "$FILES" ] && { echo "zero public text changed"; exit 0; }
python3 -I -X utf8 "$DIR/prose-lint.py" $FILES
