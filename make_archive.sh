#!/usr/bin/env bash
# Create Vol1Archive.zip from the repository, excluding dotfiles, archive/, and bibliography/
set -euo pipefail
cd "$(dirname "$0")"
rm -f Vol1Archive.zip
zip -r Vol1Archive.zip . \
  -x '.*' \
  -x '*/.*' \
  -x 'archive/*' \
  -x 'bibliography/*' \
  -x 'references/*' \
  -x 'Vol1Archive.zip' \
  -x 'make_archive.sh'
echo "Created Vol1Archive.zip ($(du -h Vol1Archive.zip | cut -f1))"
