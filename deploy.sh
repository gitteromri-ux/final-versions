#!/usr/bin/env bash
# Idempotent: rebuild site, commit everything, push (rebase on reject). Safe to re-run any time.
set -euo pipefail
cd "$(dirname "$0")"
python3 build_site.py
big=$(find videos -name '*.mp4' -size +95M | head -5 || true)
[ -n "$big" ] && echo "WARNING: >95MB files (GitHub rejects >100MB): $big"
G="git -c user.name=gitteromri-ux -c user.email=gitteromri-ux@users.noreply.github.com"
$G add -A
if $G diff --cached --quiet; then echo "nothing to commit"; else
  $G commit -q -m "deploy $(date -u +%Y-%m-%dT%H:%MZ): $(ls videos/*.mp4 2>/dev/null | wc -l) videos"
fi
for i in 1 2 3; do
  if $G push -q origin HEAD:main; then break; fi
  echo "push rejected, rebasing ($i)"; $G pull --rebase -q origin main || { $G rebase --abort || true; sleep 3; }
done
echo "HEAD $(git rev-parse --short HEAD) -> https://gitteromri-ux.github.io/final-versions/"
