#!/usr/bin/env python3
"""
Residual Sweep — 15 Codex Agents
TOTAL AND EXHAUSTIVE cleanup of every remaining moderate item.
No corners cut. Every instance fixed.

Usage:
    python3 scripts/residual_sweep.py --batch-size 5 --timeout 1800 --delay 30
"""
import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"residual_sweep_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

P = """\
<task>
TOTAL AND EXHAUSTIVE residual sweep. Fix EVERY instance. Cut NO corners.
This is the FINAL pass. After this, the issue must be COMPLETELY resolved.
</task>
<action_safety>Only edit assigned files. Re-read after each edit.</action_safety>
<completeness_contract>Fix ALL instances, not just the first N. Report exact count fixed.</completeness_contract>
<verification_loop>After all edits, grep to verify ZERO remaining violations in scope.</verification_loop>
"""

def agent(aid, prompt, cwd=VOL1):
    AGENTS.append({"id": aid, "prompt": P + "\n\n" + prompt, "cwd": cwd, "model": "gpt-5.4"})

def run_agent(a, timeout=1800):
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


# ═══════════════════════════════════════════════════════════════
# 1. SC-FORMALITY PROPAGATION + CONCORDANCE (3 agents)
# ═══════════════════════════════════════════════════════════════

agent("RS01_concordance_final", """FINAL concordance sync. Read chapters/connections/concordance.tex.
Update EVERY theorem entry to match current state after the full session:

- Theorem D: ALL-GENERA PROVED via GRR + Arakelov-Faltings + BGS determinant-of-cohomology
- Topologization: cohomological (all families), chain-level class G/L (gauge), class M conjectural
- SC-formality: operadic both directions, no bilinear form, class G ONLY
- Koszul (viii): concentration + polynomial + E2-formality PROVED; freeness DISPROVED
- MC5: harmonic mechanism PROVED (prop:harmonic-factorization); coderived clean
- Gerstenhaber: complete brace proof
- Depth gap: two independent proofs (MC recursion + shadow Lie)
- MC3: conditional on Baxter + Mittag-Leffler completion
- Thm A: relative Ran analysis written (smooth unconditional, nodal conditional)
- Thm H: FM-tower spectral sequence collapse proved

Search for each theorem name. Verify and fix EVERY entry.""")

agent("RS02_sc_formal_xvol", """Fix SC-formality claims across ALL three volumes.

SC-formal iff class G ONLY (not G/L, not G/L/C). The operadic proof uses no bilinear form.

Vol I: grep -rn 'SC.*formal\\|sc.*formal' chapters/ standalone/ | head -40
Vol II: grep -rn 'SC.*formal\\|sc.*formal' ~/chiral-bar-cobar-vol2/chapters/ | head -20
Vol III: grep -rn 'SC.*formal\\|sc.*formal' ~/calabi-yau-quantum-groups/chapters/ ~/calabi-yau-quantum-groups/compute/ | head -20

For EVERY instance: verify it says "class G" not "class G/L" or "class G, L, C".
Fix ALL violations. Also check for bilinear-form language in SC-formality proofs.""")

agent("RS03_topol_scope_xvol", """Fix topologization scope across ALL volumes. CRITICAL: Vol II 3d_gravity.tex.

Topologization is:
(a) Cohomological E_3: PROVED for all families with conformal vector at non-critical level
(b) Chain-level E_3 on original complex: PROVED for class G/L (gauge rectification)
(c) Chain-level E_3 for class M: CONJECTURAL
(d) General (non-KM): CONJECTURAL

Search ALL volumes:
grep -rn 'topologi[sz]ation.*unconditional\\|topologi[sz]ation.*proved.*general\\|topologi[sz]ation.*all' chapters/ | head -20
Same for Vol II and Vol III.

CRITICAL FIX: ~/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex near line 6516
says "topologization mechanism is unconditional" — MUST be fixed to scope properly.

Fix ALL instances across ALL three volumes.""")


# ═══════════════════════════════════════════════════════════════
# 2. CROSS-VOLUME THEOREM STATUS (3 agents)
# ═══════════════════════════════════════════════════════════════

agent("RS04_vol2_status_sync", """Sync ALL Vol I theorem citations in Vol II to current state.

grep -rn 'Theorem.*[A-H]\\|MC[1-5]\\|topologi\\|Koszul.*equiv\\|SC.*formal\\|depth.*gap' chapters/ | head -60

For each citation verify it matches Vol I's CURRENT status. Key updates:
- Thm D: ALL-GENERA PROVED (not conditional)
- Topol: three-level (not "unconditional")
- Koszul (viii): freeness DISPROVED
- MC3: Baxter conditional
- MC5: harmonic proved, coderived clean
- SC-formal: class G ONLY, operadic

Fix ALL stale citations.""", cwd=VOL2)

agent("RS05_vol3_status_sync", """Sync ALL Vol I theorem citations in Vol III.

grep -rn 'Theorem.*[A-H]\\|Volume.*I\\|Vol.*I\\|MC[1-5]\\|topologi' chapters/ | head -40

Verify each matches current Vol I. Also:
- kappa subscripts (AP113): grep for bare \\kappa, fix any remaining
- CY-A d=2 scope: verify stated clearly
- pi_3(BU)=0: verify no remaining errors

Fix ALL stale citations.""", cwd=VOL3)

agent("RS06_vol2_vol3_dirty", """Commit and push any dirty state in Vol II and Vol III.

cd ~/chiral-bar-cobar-vol2 && git status --short
If dirty: git add -A && git commit with descriptive message && git push

cd ~/calabi-yau-quantum-groups && git status --short
If dirty: git add -A && git commit with descriptive message && git push

Do NOT credit any LLM. Author: Raeez Lorgat only.""")


# ═══════════════════════════════════════════════════════════════
# 3. REMAINING SYSTEMATIC SWEEPS (6 agents)
# ═══════════════════════════════════════════════════════════════

agent("RS07_provedhere_remaining", """Fix ALL remaining ProvedHere-without-proof in examples/ + connections/ + standalone/ + appendices/.

The theory/ chapters were done (36 fixes). Now do the REST:
grep -A50 'ClaimStatusProvedHere' chapters/examples/*.tex chapters/connections/*.tex standalone/*.tex appendices/*.tex 2>/dev/null | grep -B5 'end{theorem}\\|end{proposition}' | grep -v 'begin{proof}' | head -40

For each: change to ProvedElsewhere if proof is elsewhere, or Conjectured if no proof.
Fix ALL instances. Report exact count.""")

agent("RS08_hochschild_remaining", """Fix ALL remaining bare Hochschild in examples/ + connections/ + standalone/.

Theory/ was done (25 instances). Now the rest:
grep -rn 'Hochschild' chapters/examples/ chapters/connections/ standalone/ | grep -v 'chiral\\|topological\\|categorical\\|ChirHoch\\|%' | head -40

For each in mathematical context: add 'chiral' qualifier.
Also check Vol II: grep -rn 'Hochschild' ~/chiral-bar-cobar-vol2/chapters/ | grep -v 'chiral\\|topological\\|categorical' | head -20
Also Vol III: same pattern.
Fix ALL instances across ALL volumes.""")

agent("RS09_uniform_weight_remaining", """Fix ALL remaining uniform-weight tags in connections/ + standalone/.

Theory/ and examples/ were done (46 tags). Now the rest:
grep -rn 'obs_g\\|F_g\\|\\\\lambda_g' chapters/connections/ standalone/ | grep -v '%\\|UNIFORM\\|ALL-WEIGHT\\|unconditional' | head -40

For each in a theorem/claim context: add the appropriate tag.
Fix ALL instances.""")

agent("RS10_e3_chiral_ban", """Fix ALL remaining 'E_3-chiral' -> 'E_3-topological' across ALL volumes (AP168).

grep -rni 'E_3.*chiral\\|E_{3}.*chiral\\|E_3-chiral' chapters/ standalone/ | grep -v 'topological\\|NOT\\|not\\|!=\\|neq\\|%' | head -20
Same for Vol II and Vol III.

When referring to the topologized derived center: MUST be E_3-TOPOLOGICAL.
Fix ALL instances.""")

agent("RS11_bare_omega_final", """Fix ALL remaining bare Omega/z without level prefix across ALL volumes (AP126).

grep -rn '\\\\Omega' chapters/ standalone/ | grep -v 'k.*\\\\Omega\\|k+h\\|level\\|AP126\\|%\\|KZ\\|convention\\|Kazhdan\\|cobar\\|Omega_X\\|Omega_g\\|Omega_{ij}' | head -30
Same for Vol II and Vol III.

Every r-matrix Omega/z MUST have level prefix k. Fix ALL instances.""")

agent("RS12_arity_final", """Verify ZERO 'arity' remaining across ALL three volumes (AP176).

grep -rni '\\barity\\b' chapters/ appendices/ standalone/ compute/
Same for Vol II and Vol III.

Must return ZERO hits. If any found: replace with 'degree'. Fix 'an degree' -> 'a degree'.""")


# ═══════════════════════════════════════════════════════════════
# 4. FINAL VERIFICATION (3 agents)
# ═══════════════════════════════════════════════════════════════

agent("RS13_build_test", """Build and test Vol I.

pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -20
echo "==="
python3 -m pytest compute/tests/ -x --tb=short -q 2>&1 | tail -20

Report: build pass/fail, test pass/fail, any errors.""")

agent("RS14_readme_final", """Update ALL three READMEs with current accurate metrics.

Vol I: count pages (from build log or wc), count tests, verify theorem status summary.
Vol II: same.
Vol III: same.

No scope inflation. Every claim verifiable. Update and commit each README.""")

agent("RS15_claude_agents_final", """FINAL update to CLAUDE.md and AGENTS.md in Vol I.

Update the Theorem Status table to reflect:
- AP225 FULLY RESOLVED (determinant-of-cohomology, not just strategy)
- Theorem D: ALL-GENERA PROVED (remove "conditional" language)
- Remove the AP225 WARNING block (gap is closed)
- Add AP225 resolution to the Platonic Ideal Roadmap

Also verify AGENTS.md theorem table matches.

Update the anti-pattern count to 57 (AP186-AP233).
Update session totals: 1,040 agents, 15 results merged.
Verify recovery scripts documented.""")


def main():
    parser = argparse.ArgumentParser(description="Residual Sweep")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=30)
    args = parser.parse_args()

    print(f"Residual Sweep: {len(AGENTS)} agents -> {OUT}")
    print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s, Delay: {args.delay}s\n")

    ok, fail = 0, 0
    results = []
    for i in range(0, len(AGENTS), args.batch_size):
        batch = AGENTS[i:i+args.batch_size]
        bn = i // args.batch_size + 1
        tb = (len(AGENTS) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {bn}/{tb} ({len(batch)} agents) ===")
        with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
            futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(AGENTS)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")
        if i + args.batch_size < len(AGENTS):
            print(f"  (cooldown {args.delay}s)")
            time.sleep(args.delay)

    summary = [f"# Residual Sweep Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")

if __name__ == "__main__":
    main()
