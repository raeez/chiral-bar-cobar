#!/bin/bash
echo "Waiting for all codex campaigns to settle (< 3 procs)..."
while true; do
    COUNT=$(ps aux | grep -c "[c]odex exec")
    echo "$(date +%H:%M:%S) — codex: $COUNT procs"
    if [ "$COUNT" -lt 3 ]; then
        echo "Settled. Launching 40-agent healing campaign..."
        break
    fi
    sleep 60
done
cd /Users/raeez/chiral-bar-cobar
python3 scripts/healing_fortification_40.py --batch-size 5 --timeout 1800 --delay 45
