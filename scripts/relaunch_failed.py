#!/usr/bin/env python3
"""
Relaunch failed agents from all campaigns.
Small batch size (5) with 30s inter-batch delay to avoid 429 rate limits.
"""
import subprocess, sys, time, importlib.util
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"relaunch_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

BATCH_SIZE = 5
INTER_BATCH_DELAY = 30  # seconds between batches to avoid 429

# Failed agent IDs to relaunch
WAVE1_FAILS = {
    "AP21_topologization_scope", "AP22_S2_c12", "AP23_pi3_BU",
    "AP24_undefined_macros", "AP25_slop_v2_v3", "CE01_shadow_engines",
    "XV03_bar_def_xvol", "XV05_topologization_xvol", "XV06_hochschild_xvol",
    "XV07_yangian_xvol", "XV08_thm_status_xvol", "XV10_convention_bridge",
}

WAVE2_FAILS = {
    "D05_rmatrix_level", "D06_desuspension_direction", "F03_definitions_shadow",
    "F10_prerequisites_MC1_5", "F13_hidden_imports_curved", "F15_hidden_imports_hg_comp",
    "F16_undefined_macros_v1", "F17_dangling_refs_v1", "F18_dangling_refs_v2",
    "S14_standalone_to_main", "S15_appendices_to_body", "S16_v1_to_v2_bridge",
    "S19_compute_to_manuscript", "U07_forward_refs_v1", "U15_build_warnings",
}

RECT_FAILS = {
    "R01_chiral_koszul_pairs", "R04_higher_genus_modular_koszul",
    "R11_thqg_symplectic_polarization", "R13_introduction", "R14_concordance",
    "R15_toroidal_elliptic_v1", "R17_free_fields", "R18_cobar_construction",
    "R19_coderived_models", "R20_configuration_spaces",
}

ALL_FAILS = WAVE1_FAILS | WAVE2_FAILS | RECT_FAILS


def load_agents_from(script_path):
    """Import a campaign script and return its AGENTS list."""
    spec = importlib.util.spec_from_file_location("campaign", script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.AGENTS


def run_agent(a, timeout=1500):
    """Execute a single Codex agent."""
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-", "-m", "gpt-5.4", "-C", a["cwd"], "--full-auto"],
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
    scripts = [
        f"{VOL1}/scripts/adversarial_campaign.py",
        f"{VOL1}/scripts/adversarial_wave2.py",
        f"{VOL1}/scripts/rectification_campaign.py",
    ]

    all_agents = []
    for s in scripts:
        try:
            agents = load_agents_from(s)
            all_agents.extend(agents)
        except Exception as e:
            print(f"Warning: could not load {s}: {e}")

    # Filter to only failed agents
    to_relaunch = [a for a in all_agents if a["id"] in ALL_FAILS]

    # Deduplicate (same ID might appear in multiple scripts)
    seen = set()
    unique = []
    for a in to_relaunch:
        if a["id"] not in seen:
            seen.add(a["id"])
            unique.append(a)
    to_relaunch = unique

    print(f"Relaunch: {len(to_relaunch)} agents → {OUT}")
    print(f"Batch size: {BATCH_SIZE}, Inter-batch delay: {INTER_BATCH_DELAY}s")
    print(f"Missing from scripts: {ALL_FAILS - seen}")
    print()

    ok, fail = 0, 0
    results = []
    for i in range(0, len(to_relaunch), BATCH_SIZE):
        batch = to_relaunch[i:i + BATCH_SIZE]
        bn = i // BATCH_SIZE + 1
        tb = (len(to_relaunch) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")

        with ThreadPoolExecutor(max_workers=BATCH_SIZE) as ex:
            futs = {ex.submit(run_agent, a): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(to_relaunch)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")

        # Rate limit avoidance
        if i + BATCH_SIZE < len(to_relaunch):
            print(f"  (waiting {INTER_BATCH_DELAY}s for rate limit cooldown)")
            time.sleep(INTER_BATCH_DELAY)

    summary = [f"# Relaunch Summary — {TS}\n", f"Total: {len(to_relaunch)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
