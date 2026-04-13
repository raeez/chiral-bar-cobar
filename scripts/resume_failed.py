#!/usr/bin/env python3
"""
Universal Resume Script — picks up where any campaign left off.
Scans ALL campaign output directories, identifies empty/missing/timed-out agents,
and relaunches only what's needed. Safe to run multiple times — idempotent.

Usage:
    python3 scripts/resume_failed.py [--batch-size 5] [--timeout 1800] [--delay 45]
"""

import subprocess, os, sys, time, argparse, importlib.util, glob
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"resume_{TS}"

# All campaign scripts and their output directories
CAMPAIGNS = {
    "adversarial_campaign": ("scripts/adversarial_campaign.py", "audit_campaign_20260412_231034"),
    "adversarial_wave2": ("scripts/adversarial_wave2.py", "wave2_audit_20260413_001942"),
    "rectification_campaign": ("scripts/rectification_campaign.py", "rectification_20260412_233715"),
    "fix_campaign_A": ("scripts/fix_campaign_100.py", "fix_wave_A_*"),
    "healing_fortification": ("scripts/healing_fortification_40.py", "healing_*"),
    "elite_rescue": ("scripts/elite_rescue_40.py", "elite_rescue_*"),
    "mega_rescue": ("scripts/mega_rescue_100.py", "mega_rescue_*"),
}


def find_failures():
    """Scan all campaign directories for empty/missing results."""
    failures = []

    for campaign_name, (script_path, out_pattern) in CAMPAIGNS.items():
        script = Path(VOL1) / script_path
        if not script.exists():
            continue

        # Find output directories
        out_dirs = sorted(glob.glob(str(Path(VOL1) / out_pattern)))
        if not out_dirs:
            # Campaign never ran or output dir doesn't exist
            print(f"[{campaign_name}] No output directory found — entire campaign needs launch")
            failures.append({"campaign": campaign_name, "script": str(script), "type": "full"})
            continue

        out_dir = Path(out_dirs[-1])  # Use the latest

        # Load agent definitions from script
        try:
            spec = importlib.util.spec_from_file_location(campaign_name, str(script))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, 'AGENTS') and isinstance(mod.AGENTS, list):
                all_agents = mod.AGENTS
            elif hasattr(mod, 'AGENTS') and isinstance(mod.AGENTS, dict):
                all_agents = []
                for wave_agents in mod.AGENTS.values():
                    all_agents.extend(wave_agents)
            else:
                continue
        except Exception as e:
            print(f"[{campaign_name}] Could not load script: {e}")
            continue

        # Check each agent
        for agent in all_agents:
            aid = agent["id"]
            result_file = out_dir / f"{aid}.md"

            if not result_file.exists():
                failures.append({"campaign": campaign_name, "agent": agent, "type": "missing"})
            elif result_file.stat().st_size < 200:
                failures.append({"campaign": campaign_name, "agent": agent, "type": "empty"})
            elif "TIMEOUT" in result_file.read_text()[:100]:
                failures.append({"campaign": campaign_name, "agent": agent, "type": "timeout"})

    return failures


def run_agent(a, timeout=1800):
    """Execute a single Codex agent."""
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-", "-m", "gpt-5.4", "-C", a.get("cwd", VOL1), "--full-auto"],
            input=a["prompt"], capture_output=True, text=True, timeout=timeout,
        )
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} ({dt:.0f}s)\n\n{r.stdout}\n\n---\nSTDERR:\n{r.stderr}")
        return a["id"], r.returncode == 0, dt
    except subprocess.TimeoutExpired:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — TIMEOUT ({dt:.0f}s)\n")
        return a["id"], False, dt
    except Exception as e:
        dt = time.time() - t0
        out_file.write_text(f"# {a['id']} — ERROR: {e}\n")
        return a["id"], False, dt


def main():
    parser = argparse.ArgumentParser(description="Resume failed/missing agents from all campaigns")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=45)
    parser.add_argument("--dry-run", action="store_true", help="List failures without relaunching")
    parser.add_argument("--campaign", type=str, default=None, help="Filter to specific campaign")
    args = parser.parse_args()

    print(f"Scanning all campaign directories for failures...")
    failures = find_failures()

    if args.campaign:
        failures = [f for f in failures if f["campaign"] == args.campaign]

    # Separate full-campaign failures from individual agent failures
    full_campaigns = [f for f in failures if f["type"] == "full"]
    agent_failures = [f for f in failures if f["type"] != "full"]

    print(f"\nFound:")
    print(f"  {len(full_campaigns)} campaigns that never ran")
    print(f"  {len(agent_failures)} individual agent failures")
    for f in agent_failures[:20]:
        print(f"    [{f['type']}] {f['campaign']}/{f['agent']['id']}")
    if len(agent_failures) > 20:
        print(f"    ... and {len(agent_failures)-20} more")

    if args.dry_run:
        print("\n--dry-run: not launching anything")
        return

    if not agent_failures and not full_campaigns:
        print("\nNo failures found. All campaigns complete.")
        return

    # Relaunch individual agent failures
    if agent_failures:
        OUT.mkdir(parents=True, exist_ok=True)
        agents_to_run = [f["agent"] for f in agent_failures]
        print(f"\nRelaunching {len(agents_to_run)} agents -> {OUT}")
        print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s, Delay: {args.delay}s\n")

        ok, fail = 0, 0
        results = []
        for i in range(0, len(agents_to_run), args.batch_size):
            batch = agents_to_run[i:i + args.batch_size]
            bn = i // args.batch_size + 1
            tb = (len(agents_to_run) + args.batch_size - 1) // args.batch_size
            print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")
            with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
                futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
                for f in as_completed(futs):
                    aid, success, dt = f.result()
                    ok += success; fail += (not success)
                    results.append({"id": aid, "ok": success, "time": dt})
                    print(f"  [{ok+fail}/{len(agents_to_run)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")
            if i + args.batch_size < len(agents_to_run):
                print(f"  (cooldown {args.delay}s)")
                time.sleep(args.delay)

        summary = [f"# Resume Summary — {TS}\n",
                   f"Total: {len(agents_to_run)} | OK: {ok} | Failed: {fail}\n"]
        for r in sorted(results, key=lambda x: x["id"]):
            summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
        (OUT / "SUMMARY.md").write_text("\n".join(summary))
        print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")

    # Report full campaigns that need launching
    if full_campaigns:
        print(f"\nFull campaigns that never ran (launch manually):")
        for f in full_campaigns:
            print(f"  python3 {f['script']} --batch-size 5 --timeout 1800 --delay 45")


if __name__ == "__main__":
    main()
