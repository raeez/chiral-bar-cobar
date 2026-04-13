#!/usr/bin/env python3
"""
Final Gaps Campaign — 30 Codex Agents
Target: every remaining unresolved gap from the 832-agent session.

Usage:
    python3 scripts/final_gaps_campaign.py --batch-size 5 --timeout 1800 --delay 30
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"final_gaps_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are a FINAL GAPS agent. This is the LAST PASS. Every remaining gap must be closed.
832 agents have already run. You fix what they couldn't finish.
Read files on disk — they reflect ALL prior work. Be surgical. Be complete.
</task>
<action_safety>Keep changes scoped. After edits, re-read and verify. Grep for AP violations.</action_safety>
<completeness_contract>Fix EVERY issue in your scope. Report: FIXED or BLOCKED (with reason).</completeness_contract>
<verification_loop>After all edits, verify no new violations introduced.</verification_loop>
"""


def agent(aid, prompt, cwd=VOL1):
    AGENTS.append({"id": aid, "prompt": PREAMBLE + "\n\n" + prompt, "cwd": cwd, "model": "gpt-5.4"})


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


# ═══════════════════════════════════════════════════════════════════
# GAP 1: AP225 — Theorem D universality (THE deepest gap)
# ═══════════════════════════════════════════════════════════════════

agent("G01_thm_D_universality_fix", """THE MOST CRITICAL REMAINING GAP: AP225.

TARGET: chapters/theory/higher_genus_modular_koszul.tex + chapters/theory/higher_genus_foundations.tex

The all-genera obs_g = kappa*lambda_g rests on thm:genus-universality whose proof
has a substantive gap: scalar saturation doesn't uniquely force lambda_g.

YOUR MISSION: Fix this by ONE of:
(a) PROVE clutching-uniqueness: show that a class on M-bar_g that restricts to
    kappa*lambda_{g1}*lambda_{g2} on every boundary stratum must equal kappa*lambda_g.
    This follows from Faber's conjectures / Pixton's theorem on the tautological ring.
(b) PROVE via GRR directly: the fiber bar complex is a complex of vector bundles;
    GRR on the universal curve gives ch(R*pi_*(B_fib)) involving lambda classes;
    the leading term at each genus is kappa*lambda_g by the Mumford computation.
(c) If NEITHER can be proved: split Theorem D into (a) genus-1 unconditional
    (b) all-genera conditional on clutching-uniqueness, and INSCRIBE this split
    in the theorem statement, concordance, and introduction.

Option (a) or (b) is STRONGLY PREFERRED. Do NOT downgrade if you can upgrade.

Search for thm:genus-universality and thm:family-index. Read the proofs. Fix them.""")

agent("G02_thm_D_concordance_propagate", """After G01 fixes the universality gap, propagate to ALL downstream surfaces.

TARGETS: chapters/connections/concordance.tex, chapters/theory/introduction.tex,
chapters/frame/preface.tex, standalone/*.tex

Search for: 'obs_g', 'Theorem D', 'genus-universality', 'family-index', 'all genera'.
For each: update to match the new Theorem D status (either fully proved via
clutching-uniqueness/GRR, or split genus-1/all-genera).

Also fix: cor:kappa-additivity to route through genus-1 only (AP230).
Also fix: thm:universal-generating-function status to match.
Also fix: anomaly-Koszul dependency direction (AP228).""")


# ═══════════════════════════════════════════════════════════════════
# GAP 2: Cross-volume formula sweeps (C06, C12, C14 timeouts)
# ═══════════════════════════════════════════════════════════════════

agent("G03_averaging_sugawara_xvol", """Fix av(r(z)) Sugawara shift across ALL volumes (timed-out C06).

NARROW SCOPE: only fix instances where av(r(z))=kappa is stated for non-abelian KM
WITHOUT the Sugawara shift dim(g)/2. Don't rewrite whole files.

grep -rn 'av.*r.*kappa\\|averaging.*kappa' chapters/ standalone/ | head -30
Do the same in Vol II and Vol III.
For each: add "for abelian" qualifier or add "+ dim(g)/2 Sugawara shift for non-abelian KM."
""")

agent("G04_desuspension_xvol", """Fix desuspension direction across ALL volumes (timed-out C12).

NARROW SCOPE: find |s^{-1}v| = |v|+1 (WRONG) and fix to |v|-1.
grep -rn 's.*{-1}.*|v|.*+.*1' chapters/ | head -20
Same for Vol II and Vol III. Fix each instance.""")

agent("G05_curved_flat_xvol", """Fix curved-vs-flat confusion across Vol I (timed-out C14).

NARROW SCOPE: find spectral sequences or H^* applied to objects with d^2=kappa*omega_g.
Search for 'spectral sequence' near 'dfib' or 'kappa.*omega' in chapters/theory/.
For each: verify d^2=0 for the complex being used. If d^2!=0, add coderived qualifier.
Focus on the FIRST 15 instances only.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 3: Uniform-weight tags (93 instances, D13 timeout)
# ═══════════════════════════════════════════════════════════════════

agent("G06_uniform_weight_theory", """Fix missing uniform-weight tags in chapters/theory/ (AP32).

Search: grep -rn 'obs_g\\|F_g\\|lambda_g' chapters/theory/ | head -40
For each in a theorem/proposition: add (UNIFORM-WEIGHT) tag if missing.
Focus on theory chapters only. Fix ALL instances.""")

agent("G07_uniform_weight_rest", """Fix missing uniform-weight tags in chapters/examples/ + chapters/connections/ (AP32).

Same pattern. Search and fix ALL untagged obs_g/F_g/lambda_g in theorem environments.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 4: Bare Hochschild (89 instances, D14 timeout)
# ═══════════════════════════════════════════════════════════════════

agent("G08_hochschild_theory", """Fix bare 'Hochschild' without qualifier in chapters/theory/ (AP197).

grep -rn 'Hochschild' chapters/theory/ | grep -v 'chiral\\|topological\\|categorical\\|ChirHoch' | head -30
For each in a mathematical context: add 'chiral' qualifier (since Vol I is about chiral Hochschild).
Theory chapters only.""")

agent("G09_hochschild_rest", """Fix bare 'Hochschild' in chapters/examples/ + chapters/connections/ + standalone/ (AP197).

Same pattern. Add qualifier. Also check Vol II and Vol III:
grep -rn 'Hochschild' ~/chiral-bar-cobar-vol2/chapters/ | grep -v 'chiral\\|topological\\|categorical' | head -20
grep -rn 'Hochschild' ~/calabi-yau-quantum-groups/chapters/ | grep -v 'chiral\\|topological\\|categorical' | head -20""")


# ═══════════════════════════════════════════════════════════════════
# GAP 5: ProvedHere without proof (99 instances, B10 timeout)
# ═══════════════════════════════════════════════════════════════════

agent("G10_provedhere_theory_1", """Fix ProvedHere-without-proof in chapters/theory/bar_*.tex + chapters/theory/chiral_*.tex (AP186).

For each file: find ClaimStatusProvedHere. Check if begin{proof} follows within 50 lines.
If no proof: either (a) add the proof if obvious, (b) change to ProvedElsewhere with citation,
or (c) change to Conjectured if no proof exists. Fix the FIRST 15 instances.""")

agent("G11_provedhere_theory_2", """Same for chapters/theory/higher_*.tex + chapters/theory/en_*.tex + chapters/theory/e1_*.tex.
Fix the first 15 ProvedHere-without-proof instances.""")

agent("G12_provedhere_rest", """Same for chapters/theory/nilpotent*.tex + chapters/theory/ordered*.tex +
chapters/theory/coderived*.tex + chapters/examples/*.tex + chapters/connections/*.tex.
Fix the first 15 instances.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 6: Cross-volume propagation (healing H21-H30 rate-limited)
# ═══════════════════════════════════════════════════════════════════

agent("G13_vol2_thm_status_propagate", """Propagate ALL Vol I rectification results to Vol II.

Read chapters/connections/concordance.tex in Vol I for current theorem statuses.
Then search Vol II for EVERY citation of Vol I theorems:
grep -rn 'Theorem.*A\\|Theorem.*B\\|Theorem.*C\\|Theorem.*D\\|Theorem.*H\\|MC[1-5]\\|topologi' chapters/ | head -40
For each: verify the cited scope matches Vol I's CURRENT status after rectification.

Key updates needed:
- Thm A: Verdier at algebra level
- Thm B: on-locus qi + off-locus coderived
- Thm D: genus-1 unconditional (all-genera AP225)
- MC3: conditional Baxter
- MC5: coderived clean, chain conjectural
- Topol: cohomological proved, chain-level conjectural
Fix all stale citations.""", cwd=VOL2)

agent("G14_vol3_thm_status_propagate", """Same for Vol III.

Search for Vol I theorem citations. Verify scope matches current status.
Also verify: kappa subscripts (AP113), CY-A d=2 only, pi_3(BU)=0.""", cwd=VOL3)

agent("G15_vol2_3d_gravity_topol_scope", """CRITICAL: Fix Vol II 3d_gravity.tex topologization scope inflation.

Line ~6516 says "topologization mechanism is unconditional." This is WRONG.
Topologization is proved ONLY for affine KM at non-critical level.

FIX: Change to "topologization mechanism is proved for affine Kac-Moody at non-critical
level (Theorem~\\ref{thm:topologization}); for general chiral algebras with conformal
vector, it is conjectural (Conjecture~\\ref{conj:topologization-general})."

Search for 'unconditional' near 'topologization' and fix ALL instances.""", cwd=VOL2)


# ═══════════════════════════════════════════════════════════════════
# GAP 7: SC-formality propagation (AP229)
# ═══════════════════════════════════════════════════════════════════

agent("G16_sc_formality_v3_compute", """Fix SC-formality propagation debt in Vol III compute (AP229).

The proof says SC-formal iff class G. But Vol III compute libraries may still
carry "class G/L SC-formal." Fix:

grep -rn 'SC.*formal\\|sc_formal\\|formality.*class' compute/ chapters/ | head -20
For each: verify it says "class G ONLY" not "class G/L."
Fix any stale claims.""", cwd=VOL3)


# ═══════════════════════════════════════════════════════════════════
# GAP 8: Large file rectification (R01/R04 always timeout)
# ═══════════════════════════════════════════════════════════════════

agent("G17_koszul_pairs_vii", """Fix Koszul equivalence (vii) in chiral_koszul_pairs.tex (AP216).

NARROW SCOPE — don't read the whole file. Search ONLY for 'equiv.*vii' or the
specific equivalence. It should say: uniform-weight all-genera (unconditional) /
multi-weight genus-0 only. If it still says "unconditional" without this qualifier,
fix it. Search lines 1990-2020.""")

agent("G18_koszul_pairs_viii", """Fix Koszul equivalence (viii) in chiral_koszul_pairs.tex (AP217).

NARROW SCOPE. Search for 'equiv.*viii' or 'free polynomial'. It should say:
concentration + polynomial Hilbert series (proved); freeness conditional on
Massey vanishing from FM formality. If it claims free polynomial unconditionally, fix.
Search lines 2000-2020.""")

agent("G19_hg_modular_PBW_whitehead", """Verify MC1 PBW Whitehead reduction in higher_genus_modular_koszul.tex (AP198).

NARROW SCOPE. Search for 'Whitehead' near lines 1011-1030 and 1290-1300.
Verify: the reduction from truncated current algebra to g is explicit.
If the platonic agent P08 wrote it, verify it's correct.
If not written yet: add a remark explaining the reduction.""")

agent("G20_hg_modular_depth_witness", """Verify depth gap betagamma witness in higher_genus_modular_koszul.tex (AP219).

NARROW SCOPE. Search for 'depth.*gap\\|beta.*gamma.*d_alg\\|class.*C.*witness' near lines 16400-16430 and 17100-17200.
Verify: the witness is on the STANDARD conformal-weight line (not weight-changing).
If the platonic agent P14 fixed it, verify the fix is correct.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 9: Remaining audit empties (8 from final resume)
# ═══════════════════════════════════════════════════════════════════

agent("G21_audit_empties_batch1", """Run the FIRST 4 empty audit agents that never completed.

1. CE01_shadow_engines: cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -k 'shadow' --tb=short -q 2>&1 | tail -20. Report pass/fail.
2. D05_rmatrix_level: grep ALL r-matrix formulas for level prefix across all 3 volumes. Report violations.
3. D06_desuspension_direction: grep ALL desuspension for direction errors. Report violations.
4. F03_definitions_shadow: check shadow tower definitions in higher_genus_modular_koszul.tex are complete.

Run all 4 checks. Report findings with file:line and fixes.""")

agent("G22_audit_empties_batch2", """Run the REMAINING 4 empty audit agents.

1. F10_prerequisites_MC1_5: trace the MC1-MC5 dependency DAG. Is each cited result proved?
2. F13_hidden_imports_curved: check bar_cobar_adjunction_curved.tex for hidden imports.
3. F15_hidden_imports_hg_comp: check higher_genus_complementarity.tex for hidden imports.
4. F16_undefined_macros_v1: grep standalone/*.tex for undefined macros.

Report findings with file:line and fixes.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 10: Literature cross-checks (elite L01-L10 rate-limited)
# ═══════════════════════════════════════════════════════════════════

agent("G23_literature_BD_CG", """Literature cross-check: BD + CG/CFG.

1. BD [BD04]: Does our bar construction agree with BD's factorization coalgebra?
   Read bar_construction.tex. Check: augmentation, Ran space, Arnold relation.
2. CG [CG17]: Does our BV/bar (MC5) agree with CG's BV quantization?
3. CFG [arXiv:2602.12412]: Does our E_3 topologization agree with CFG's E_3?

Write findings as Remarks in the relevant .tex files if discrepancies found.
If consistent: write Remark[Literature confirmation] noting the agreement.""")

agent("G24_literature_Lurie_PTVV", """Literature cross-check: Lurie + PTVV.

1. Lurie [HA]: Is our bar = Cech nerve of augmentation? Check bar_construction.tex.
2. PTVV [PTVV13]: Is our complementarity consistent with shifted symplectic?
   Check higher_genus_complementarity.tex.

Write findings as Remarks.""")

agent("G25_literature_EF_KS_LV", """Literature cross-check: EF + KS + LV.

1. Etingof-Frenkel: R-matrix r^KM(z) consistent with KZ connection?
2. Kontsevich-Soibelman: Theta_A consistent with scattering diagrams?
3. Loday-Vallette: SC Koszulity and SC^! consistent with colored operad theory?

Write findings as Remarks.""")


# ═══════════════════════════════════════════════════════════════════
# GAP 11: Independent derivations (elite R01-R10 rate-limited)
# ═══════════════════════════════════════════════════════════════════

agent("G26_kappa_3way_verification", """Triple-verify kappa for Heisenberg, KM, Virasoro via 3 methods each.

1. Shadow tower: kappa = av(r(z)) [+ Sugawara for non-abelian]
2. Anomaly: kappa from eta^{-2*kappa}
3. Hilbert series: kappa from bar complex growth

Write as Proposition[Three-path kappa verification] in higher_genus_modular_koszul.tex.
Verify Heis: k, k, k. KM: dim(g)(k+h^v)/(2h^v) all three. Vir: c/2 all three.""")

agent("G27_sl2_H2_3way", """Triple-verify sl_2 bar H^2 = 5.

1. Direct enumeration of bar complex at degree 2
2. CE comparison (with Orlik-Solomon correction for chiral)
3. Compute engine: run python3 -c "from compute.lib.sl2_chiral_bar_dims import *; print(sl2_chiral_bar_dims())"

All must give 5 (NOT 6). Write verification remark.""")

agent("G28_genus2_F2_verification", """Verify F_2 = 7/5760 via genus-2 stable graph sum.

Enumerate all 7 stable graphs at (g=2, n=0). For each: compute the Feynman weight.
Sum: should give F_2 = 7/5760. Verify against compute engine if one exists.
Check: are there really 7 graphs? (Not 6, AP123.)""")


# ═══════════════════════════════════════════════════════════════════
# GAP 12: Final concordance + README sync
# ═══════════════════════════════════════════════════════════════════

agent("G29_concordance_final_sync", """FINAL concordance sync.

Read concordance.tex. For EVERY theorem entry, verify against the current .tex source.
Focus on the entries most likely to be stale after this session:
- Theorem D (AP225 universality)
- Topologization (cohomological/chain-level split)
- MC3 (Baxter conditional)
- MC5 (coderived clean)
- Koszul (vii)/(viii) (scope narrowed)
- SC-formality (operadic both directions)
- Depth gap (witness corrected)

Fix every stale entry.""")

agent("G30_readme_final_sync", """FINAL README sync across all 3 volumes.

For each README: verify page counts, test counts, theorem status claims.
Run: wc -l chapters/**/*.tex for approximate page count.
Run: find compute/tests -name "*.py" | wc -l for test file count.
Verify theorem status matches concordance. Fix stale claims. No scope inflation.""")


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Final Gaps Campaign")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=30)
    args = parser.parse_args()

    print(f"Final Gaps: {len(AGENTS)} agents -> {OUT}")
    print(f"Batch: {args.batch_size}, Timeout: {args.timeout}s, Delay: {args.delay}s\n")

    ok, fail = 0, 0
    results = []
    for i in range(0, len(AGENTS), args.batch_size):
        batch = AGENTS[i:i + args.batch_size]
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

    summary = [f"# Final Gaps Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
