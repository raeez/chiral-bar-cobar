#!/bin/bash
# Wait for current codex campaigns to finish, then launch wave 2
echo "Waiting for current campaigns to settle (< 5 codex procs)..."
while true; do
    COUNT=$(ps aux | grep -c "[c]odex exec")
    AUDIT=$(ls /Users/raeez/chiral-bar-cobar/audit_campaign_20260412_231034/*.md 2>/dev/null | wc -l)
    RECT=$(ls /Users/raeez/chiral-bar-cobar/rectification_20260412_233715/*.md 2>/dev/null | wc -l)
    echo "$(date +%H:%M:%S) — codex: $COUNT procs | audit: $AUDIT/105 | rect: $RECT/25"
    if [ "$COUNT" -lt 5 ]; then
        echo "Campaigns settled. Launching wave 2..."
        break
    fi
    sleep 60
done

cd /Users/raeez/chiral-bar-cobar
python3 scripts/adversarial_wave2.py --batch-size 12 --timeout 900
