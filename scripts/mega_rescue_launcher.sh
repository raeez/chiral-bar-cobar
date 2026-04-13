#!/bin/bash
echo "Waiting for current campaigns to settle (< 5 codex procs)..."
while true; do
    COUNT=$(ps aux | grep -c "[c]odex exec")
    echo "$(date +%H:%M:%S) — codex: $COUNT procs"
    if [ "$COUNT" -lt 5 ]; then
        echo "Settled. Launching 100-agent mega rescue..."
        break
    fi
    sleep 60
done
cd /Users/raeez/chiral-bar-cobar
python3 scripts/mega_rescue_100.py --batch-size 5 --timeout 1800 --delay 45
