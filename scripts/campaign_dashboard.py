#!/usr/bin/env python3
"""Quick dashboard of all campaign status."""
import glob, os
from pathlib import Path

VOL1 = "/Users/raeez/chiral-bar-cobar"
campaigns = [
    ("Wave 1 Audit", "audit_campaign_20260412_231034"),
    ("Rectification", "rectification_20260412_233715"),
    ("Wave 2 Deep", "wave2_audit_20260413_001942"),
    ("Wave A Fixes", "fix_wave_A_*"),
    ("Relaunch", "relaunch_*"),
    ("Platonic", "platonic_rectification_*"),
    ("Healing", "healing_*"),
    ("Elite Rescue", "elite_rescue_*"),
    ("Mega Rescue", "mega_rescue_*"),
    ("Resume", "resume_*"),
    ("Wave2 Empties", "relaunch_wave2_empties"),
]

print(f"{'Campaign':<20} {'Files':>6} {'Empty':>6} {'Timeout':>8} {'Summary':>8}")
print("=" * 60)
for name, pattern in campaigns:
    dirs = sorted(glob.glob(str(Path(VOL1) / pattern)))
    if not dirs:
        print(f"{name:<20} {'—':>6} {'—':>6} {'—':>8} {'no dir':>8}")
        continue
    d = Path(dirs[-1])
    files = list(d.glob("*.md"))
    files = [f for f in files if f.name != "SUMMARY.md"]
    empty = sum(1 for f in files if f.stat().st_size < 200)
    timeout = sum(1 for f in files if "TIMEOUT" in f.read_text()[:100])
    has_summary = (d / "SUMMARY.md").exists()
    print(f"{name:<20} {len(files):>6} {empty:>6} {timeout:>8} {'YES' if has_summary else 'running':>8}")

import subprocess
procs = subprocess.run(["pgrep", "-c", "-f", "codex exec"], capture_output=True, text=True)
print(f"\nActive codex procs: {procs.stdout.strip()}")
