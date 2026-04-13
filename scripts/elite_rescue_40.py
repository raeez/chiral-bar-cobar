#!/usr/bin/env python3
"""
Elite Rescue Campaign — 40 Codex Agents
Focused on the latest 50-100 commits across all three volumes.
HEAL, REPAIR, UPGRADE, ALTERNATIVE PROOFS, CROSS-CONSISTENCY, LITERATURE DERIVATIONS.

Usage:
    python3 scripts/elite_rescue_40.py --batch-size 5 --timeout 1800 --delay 45
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"elite_rescue_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are an ELITE RESCUE agent. Your focus: the latest 50-100 commits across a 3-volume,
4,700-page mathematical manuscript. This session deployed 592 Codex agents producing
63+ commits across: adversarial audit (105+250), rectification (25+20), platonic upgrade (20),
healing (40), plus relaunches. Every main theorem (A-D, H, MC1-5) was attacked, repaired,
and upgraded. You now operate on the CURRENT state — all those fixes are on disk.

Your mission:
1. HEAL remaining wounds from the session
2. PROVIDE alternative proof routes for REDUNDANCY (multiplicity of proof)
3. CROSS-CHECK against published literature (BD, FG, CG, Lurie, PTVV, CFG, Costello-Li)
4. DERIVE key results via INDEPENDENT methodology to confirm correctness
5. UPGRADE mathematical strength wherever possible
6. VERIFY cross-domain and cross-approach consistency

Run `git log --oneline -50` in the assigned repo to see recent work.
Read AGENTS.md and CLAUDE.md for the constitutional framework.
Read the actual .tex files — they reflect ALL session work.
</task>

<grounding_rules>
Ground every claim in file contents or tool outputs. Label hypotheses.
When citing literature: give paper, theorem number, and convention check.
</grounding_rules>

<completeness_contract>
For each result in your scope: state PRIMARY proof status, ALTERNATIVE proof (written/sketched/identified),
LITERATURE cross-check (confirmed/discrepant/not-checked), and CONFIDENCE (high/medium/low).
</completeness_contract>

<verification_loop>
After edits: re-read modified sections, grep for AP126/AP132/AP29/AP165 violations.
Run relevant tests if in compute scope.
</verification_loop>
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
# TIER 1: LITERATURE CROSS-CHECK (10 agents)
# Derive key results from published sources, verify consistency.
# ═══════════════════════════════════════════════════════════════════

agent("L01_BD_comparison", """LITERATURE CROSS-CHECK: Beilinson-Drinfeld [BD04].

Read chapters/theory/chiral_koszul_pairs.tex and chapters/theory/bar_construction.tex.
Cross-check against BD's chiral algebra framework:
1. Does our bar construction B(A) agree with BD's factorization coalgebra on Ran(X)?
2. Is the chiral Koszul duality consistent with BD's chiral homology?
3. BD Chapter 4 "commutative" = pole-free = strict subclass of E_inf. Verify our E_inf
   treatment is consistent (V2-AP5: "commutative" ≠ E_inf).
4. The Arnold relation on FM_n(C): does our treatment match BD's?
Write a Remark[BD comparison] in the relevant file with explicit convention bridge.""")

agent("L02_FG_comparison", """LITERATURE CROSS-CHECK: Frenkel-Gaitsgory [FG04/FG06].

Read chapters/theory/higher_genus_modular_koszul.tex (shadow tower, Theorem D).
Cross-check against FG's local geometric Langlands:
1. Does our Koszul duality at critical level k=-h^v match FG's local Langlands?
2. The center at critical level (Feigin-Frenkel): does our kappa→0 specialization agree?
3. FG's Wakimoto modules: are they consistent with our bar-cobar at critical level?
Write a Remark[FG comparison] with explicit convention bridge.""")

agent("L03_CG_comparison", """LITERATURE CROSS-CHECK: Costello-Gwilliam [CG17/CG21].

Read chapters/theory/en_koszul_duality.tex and chapters/connections/bv_brst.tex.
Cross-check against CG's factorization algebra framework:
1. Does our BV/bar comparison (MC5) agree with CG's BV quantization?
2. The E_n structure: does our topologization match CG's factorization homology E_n?
3. CG's Koszul duality for En operads: consistent with our chiral Koszul pairs?
4. Does CFG arXiv:2602.12412 E_3 from BV-quantized CS agree with our topologization?
Write a Remark[CG comparison].""")

agent("L04_Lurie_comparison", """LITERATURE CROSS-CHECK: Lurie [HA, DAG].

Read chapters/theory/bar_construction.tex and chapters/theory/cobar_construction.tex.
Cross-check:
1. Our bar construction as Cech nerve of augmentation: consistent with Lurie HA Ch 5?
2. Our bar-cobar adjunction: matches Lurie's Koszul duality for E_n algebras?
3. Ran space formalism: consistent with Gaitsgory-Rozenblyum DAG Vol II?
4. Coderived category: consistent with Lurie's stable infinity-categories?
Write a Remark[Lurie comparison].""")

agent("L05_PTVV_comparison", """LITERATURE CROSS-CHECK: Pantev-Toen-Vaquie-Vezzosi [PTVV13].

Read chapters/theory/higher_genus_complementarity.tex (Theorem C, shifted symplectic).
Cross-check:
1. Our (-1)-shifted symplectic structure on bar-cobar moduli: consistent with PTVV?
2. Complementarity kappa+kappa'=K as volume of shifted symplectic form: derivable from PTVV?
3. Lagrangian decomposition (C1): consistent with PTVV Lagrangian intersections?
4. Calaque-Scheimbauer integration: consistent with our fiber integration?
Write a Remark[PTVV comparison].""")

agent("L06_EF_comparison", """LITERATURE CROSS-CHECK: Etingof-Frenkel-Kazhdan [EFK98], Etingof-Varchenko.

Read chapters/examples/kac_moody.tex and chapters/theory/ordered_associative_chiral_kd.tex.
Cross-check:
1. Our R-matrix r^KM(z) = k*Omega/z: consistent with EF's KZ connection?
2. Our Yangian construction: consistent with Drinfeld's original Y(g)?
3. Etingof-Varchenko elliptic R-matrices: consistent with our elliptic claims?
4. KZB connection at genus 1: consistent with Bernard [Ber88], Felder [Fel94]?
Write a Remark[EF comparison] with explicit convention bridges.""")

agent("L07_KS_comparison", """LITERATURE CROSS-CHECK: Kontsevich-Soibelman [KS08/KS14].

Read chapters/theory/higher_genus_modular_koszul.tex (MC2, Theta_A, shadow tower).
Cross-check:
1. Our MC element Theta_A: consistent with KS wall-crossing/scattering diagrams?
2. Shadow tower growth bound alpha_g: derivable from KS stability conditions?
3. Our G/L/C/M classification: interpretable in terms of KS BPS structures?
4. Does the scattering-diagram alternative construction of Theta_A (from P06) match KS?
Write a Remark[KS comparison].""")

agent("L08_Livernet_comparison", """LITERATURE CROSS-CHECK: Livernet [Liv06], Loday-Vallette [LV12].

Read chapters/theory/chiral_koszul_pairs.tex (SC^{ch,top} Koszulity, SC^! structure).
Cross-check:
1. SC^{ch,top} Koszulity: matches Livernet's proof?
2. SC^! = (Lie, Ass, shuffle-mixed): consistent with LV's colored operad theory?
3. Our claim SC is NOT self-dual: verify against LV's dimension formulas.
4. Homotopy transfer for SC: consistent with LV's operadic transfer?
Write a Remark[Livernet-LV comparison].""")

agent("L09_CFG_E3_comparison", """LITERATURE CROSS-CHECK: Costello-Francis-Gwilliam [CFG arXiv:2602.12412].

Read chapters/theory/en_koszul_duality.tex (topologization, E_3).
Cross-check:
1. CFG construct filtered E_3 from BV-quantized CS. Does their E_3 match ours?
2. Their factorization homology trace = RT invariant. Consistent with our shadow tower?
3. CFG's E_3 is perturbative at genus 0. Does our E_3 (cohomological) agree at genus 0?
4. The chain-level gap: does CFG face the same obstruction as us?
Write a Remark[CFG comparison].""")

agent("L10_GR_comparison", """LITERATURE CROSS-CHECK: Gaiotto-Rapcak [GR17], Gaiotto-Rapcak-Zhou [GRZ23].

Read chapters/theory/ordered_associative_chiral_kd.tex and Vol III cy_to_chiral.tex.
Cross-check:
1. GRZ chiral coproduct for type A: consistent with our Drinfeld coproduct via bar-cobar?
2. GR vertex algebras from M2-M5 brane intersections: consistent with our E_1 chiral algebras?
3. Jindal-Kaubrys-Latyntsev [JKL25] ADE CoHA vertex coproducts: consistent with our framework?
Write a Remark[GRZ comparison].""")


# ═══════════════════════════════════════════════════════════════════
# TIER 2: ALTERNATIVE PROOF ROUTES (10 agents)
# Independent derivations for redundancy.
# ═══════════════════════════════════════════════════════════════════

agent("R01_kappa_independent", """INDEPENDENT DERIVATION: kappa(A) via three methods.

For Heisenberg, KM, Virasoro: derive kappa via THREE independent methods:
1. Shadow tower: kappa = av(r(z)) (+ Sugawara for non-abelian)
2. Anomaly: kappa from the 1-loop partition function Z_1 = eta(tau)^{-2*kappa}
3. Hilbert series: kappa from the growth rate of the bar complex Hilbert series

Verify all three agree for each family. Write the comparison as a Proposition
with three independent proofs. Add to chapters/theory/higher_genus_modular_koszul.tex.""")

agent("R02_complementarity_independent", """INDEPENDENT DERIVATION: complementarity K(A) = kappa + kappa' via two methods.

1. Koszul duality: K from the Euler characteristic of the total bar complex
2. Index theory: K as the index of the bar-cobar operator on the Koszul pair

Verify for Vir (K=13), KM (K=0), BP (K=196). Add as a Remark[Independent derivation]
in chapters/theory/higher_genus_complementarity.tex.""")

agent("R03_obs_g_genus1_independent", """INDEPENDENT DERIVATION: obs_1 = kappa*lambda_1 = kappa/24 via modular forms.

1. Direct: compute F_1 from the genus-1 shadow tower
2. Modular: F_1 = -log eta(tau)^{2*kappa} evaluated at the Eisenstein point
3. Topological: F_1 from the Euler characteristic of the Hodge bundle

All three must give kappa/24. Verify for Heisenberg, KM, Virasoro.
Add as a worked example in chapters/theory/higher_genus_modular_koszul.tex.""")

agent("R04_bar_cohom_sl2_independent", """INDEPENDENT VERIFICATION: sl_2 bar H^2 = 5.

Compute dim H^2(B(sl_2)) by THREE independent methods:
1. Direct: enumerate the bar complex at degree 2, compute the differential
2. Lie algebra: use the Chevalley-Eilenberg comparison (with the CE-chiral correction)
3. Compute engine: run compute/lib/sl2_chiral_bar_dims.py and verify

All three must give 5 (NOT 6). Document the triple verification.""")

agent("R05_depth_gap_independent", """INDEPENDENT VERIFICATION: d_alg in {0,1,2,inf}, gap at 3.

1. Algebraic: the MC relation at degree 4 forces S_4 = f(kappa, S_3); show non-cancellation
2. Representation-theoretic: shadow Lie algebra Jacobi identity (from P10 alternative)
3. Computational: verify d_alg for Heis (0), sl_2 KM (1), betagamma (2), Vir (inf)
   using compute engines. Run all four tests.

Document the triple verification.""")

agent("R06_SC_koszulity_independent", """INDEPENDENT VERIFICATION: SC^{ch,top} is Koszul.

1. Livernet's proof [Liv06]: verify the citation is correct and hypotheses match
2. Operadic: verify via the PBW criterion for colored operads
3. Computational: verify dim SC(n,m) vs dim SC^!(n,m) for small n,m

Also verify SC^! = (Lie, Ass, shuffle-mixed) by direct computation at low degrees.
Add verification remark in chapters/theory/en_koszul_duality.tex.""")

agent("R07_Verlinde_shadow", """INDEPENDENT DERIVATION: Verlinde formula from the shadow tower.

The shadow tower at genus g should recover the Verlinde formula for affine KM.
1. Compute the shadow tower obs_g for V_k(sl_2) at genus g=0,1,2
2. Compare with the Verlinde formula dim H^0(M_g, L^k) for sl_2 at level k
3. Verify they agree (possibly up to a normalization)

This connects the abstract shadow tower to a CONCRETE algebro-geometric quantity.
Document in chapters/examples/kac_moody.tex.""")

agent("R08_Borcherds_bar_Euler", """INDEPENDENT DERIVATION: bar Euler product = Borcherds denominator (Vol III).

For K3 x E:
1. Compute the bar complex Euler product from the shadow tower
2. Compare with the Borcherds-Kac-Moody denominator formula for Phi_10
3. Verify kappa_BKM = 5 = wt(Phi_10)/2

This is the Vol III bridge theorem. Document in
~/calabi-yau-quantum-groups/chapters/theory/bar_cobar_bridge.tex.""", cwd=VOL3)

agent("R09_E3_from_3d_CS", """INDEPENDENT DERIVATION: E_3 from 3d Chern-Simons.

For V_k(sl_2) at non-critical level:
1. The 3d holomorphic CS theory (Costello-Li) gives a factorization algebra on C x R
2. This factorization algebra is E_3 by Dunn additivity (E_2 on C x E_1 on R)
3. Restriction to the boundary C x {0} gives V_k(sl_2)
4. Bulk observables = derived center = E_3

This gives E_3 from the TOP (3d theory) rather than from Sugawara (BOTTOM).
Verify consistency with our topologization theorem.
Document in chapters/theory/en_koszul_duality.tex.""")

agent("R10_genus2_explicit", """INDEPENDENT COMPUTATION: genus-2 shadow tower.

Compute the genus-2 observable obs_2 for Heisenberg, sl_2 KM, and Virasoro:
1. Enumerate all 7 stable graphs at (g=2, n=0)
2. For each graph: compute the Feynman integral using the shadow tower propagator
3. Sum: obs_2 = sum over graphs = F_2 * kappa * lambda_2
4. Verify F_2 = 7/5760

This is the first non-trivial genus. The separating vs non-separating
degeneration channels must be distinguished (AP157).
Document in chapters/theory/higher_genus_modular_koszul.tex.""")


# ═══════════════════════════════════════════════════════════════════
# TIER 3: CROSS-VOLUME CONSISTENCY (10 agents)
# Verify the latest commits are consistent across volumes.
# ═══════════════════════════════════════════════════════════════════

agent("X01_thm_status_3vol", """CROSS-CONSISTENCY: theorem status across 3 volumes.

Run git log --oneline -50 in each volume. For each theorem status change in the latest commits:
1. Read the theorem in Vol I
2. Check how it's cited in Vol II
3. Check how it's cited in Vol III
Verify ALL three are consistent AFTER the session's rectification.

Focus on: Thm A Verdier scope, Thm B coderived, C0 D^co, C1 g>=1, Thm D non-circular,
MC3 Baxter, MC5 coderived, topologization split, Koszul (vii)/(viii).
Fix any remaining stale citations.""")

agent("X02_formula_3vol", """CROSS-CONSISTENCY: formulas across 3 volumes.

For each of these key formulas, verify IDENTICAL across all three repos:
kappa(KM), kappa(Vir), kappa(Heis), kappa(W_N), r^KM(z), r^Vir(z),
B(A) = T^c(s^{-1} A-bar), |s^{-1}v|=|v|-1, eta(tau)=q^{1/24}*prod,
Cauchy 1/(2*pi*i), K(Vir)=13, K(BP)=196.

Grep each formula across all three repos. Fix any discrepancy.""")

agent("X03_SC_3vol", """CROSS-CONSISTENCY: SC^{ch,top} across 3 volumes.

After the session's SC correction (AP165-AP175):
1. Vol I: SC on derived center pair? Check.
2. Vol II: SC on derived center pair? Check the Swiss-cheese chapter.
3. Vol III: SC references? Check.
4. SC^! = (Lie, Ass) everywhere? Check.
5. SC NOT self-dual everywhere? Check.
6. E_3-TOPOLOGICAL (not chiral) everywhere? Check.
Fix any remaining violations.""")

agent("X04_E1_Einf_3vol", """CROSS-CONSISTENCY: E_1/E_inf hierarchy across volumes.

V2-AP1 through V2-AP24 define the hierarchy. Verify:
1. Vol I: all standard VAs listed as E_inf? Check.
2. Vol II: no "VAs are not E_inf"? Check.
3. Vol III: E_1 vs E_2 correctly distinguished? Check.
4. "E_inf means no OPE poles" NEVER appears? Check.
5. Three-tier picture (pole-free < VA-with-poles < genuinely-E_1) consistent? Check.
Fix any violations.""")

agent("X05_modular_operad_3vol", """CROSS-CONSISTENCY: modular operad breakthroughs.

Recent Vol II commits include "Modular operad breakthroughs: composition, equivariance, unitality proved."
1. Read the modular operad content in Vol II
2. Verify it's consistent with Vol I's modular bar theory
3. Verify it's consistent with Vol III's CY modular structure
4. Are the proofs sound? Cross-check the composition, equivariance, unitality claims.
Fix any inconsistencies.""", cwd=VOL2)

agent("X06_chiral_coproduct_3vol", """CROSS-CONSISTENCY: chiral coproduct across volumes.

Vol III created several coproduct engines (spin-2, spin-3, general, bialgebra).
1. Is the chiral coproduct in Vol III consistent with Vol I's bar-cobar Drinfeld coproduct?
2. Is it consistent with Vol II's ordered KD coproduct?
3. Are the compute engines consistent with each other?
4. Does the bialgebra compatibility hold?
Run the relevant tests. Fix any discrepancies.""", cwd=VOL3)

agent("X07_critical_level_3vol", """CROSS-CONSISTENCY: critical level k=-h^v across volumes.

Recent commits include "Critical level center jump (prop, 72 tests)."
1. At k=-h^v: kappa→0, center jumps (Feigin-Frenkel), Sugawara undefined
2. Vol I: is this correctly stated in the KM chapter?
3. Vol II: is the 3d gravity treatment correct at critical level?
4. Vol III: is CY-to-chiral correct at critical level?
5. Are the 72 tests consistent with the manuscript claims?
Fix any inconsistencies.""")

agent("X08_Verlinde_3vol", """CROSS-CONSISTENCY: Verlinde formula connections.

Recent commits include "Verlinde polynomial family" and "Verlinde-shadow numerical comparison."
1. Read the Verlinde content in Vol I
2. Is it consistent with the shadow tower theory?
3. Is the numerical comparison verified by compute engines?
4. Does the Verlinde-shadow bridge extend to Vol II (3d gravity) and Vol III (BKM)?
Fix any inconsistencies.""")

agent("X09_standalone_sync", """CROSS-CONSISTENCY: standalone papers vs main manuscript.

The platonic agent P20 (standalone sync) timed out. Do its job:
1. Read each standalone paper in standalone/*.tex
2. Compare theorem statements with the CURRENT main manuscript (after all rectification)
3. Fix any scope inflation, stale status, convention drift
4. Verify macros defined via providecommand
Focus on the most important standalones: N3_e1_primacy, ordered_chiral_homology.""")

agent("X10_compute_manuscript_sync", """CROSS-CONSISTENCY: compute engines vs manuscript claims.

For the 10 most important compute engines:
1. Read the engine's computed values
2. Read the manuscript's stated values
3. Verify they match
4. Run the tests

Focus on: shadow_tower, koszul_conductor, bar_cohomology_sl2, r_matrix_km,
central_charge_bc_bg, complementarity, depth_classification, genus_2_graphs,
verlinde_polynomial, critical_level_center.
Fix any discrepancies.""")


# ═══════════════════════════════════════════════════════════════════
# TIER 4: HEALING THE LATEST WORK (10 agents)
# Focus on commits from THIS session that need hardening.
# ═══════════════════════════════════════════════════════════════════

agent("H01_heal_platonic_P01_P05", """HEAL the Platonic agent outputs P01-P05 (Theorems A-C2).

Read platonic_rectification_*/P01*.md through P05*.md.
Then read the ACTUAL .tex files these agents modified.
Verify: did the agents make CORRECT edits? Any errors introduced?
Cross-check each claim against the actual file content on disk.
Fix any issues the platonic agents introduced.""")

agent("H02_heal_platonic_P06_P10", """HEAL the Platonic agent outputs P06-P10 (Thm D, H, MC1, MC3, MC5).

Same pattern: read the reports, read the .tex files, verify correctness.
Focus on: P06 Thm D routing remark, P07 Thm H FM-formality, P08 Whitehead,
P09 Baxter, P10 coderived. Fix any errors.""")

agent("H03_heal_platonic_P11_P16", """HEAL the Platonic agent outputs P11-P16 (topol, Koszul, SC, depth, D^2, Gerst).

Same: read reports, verify .tex files.
Focus on: P11 chain-level via homotopy transfer, P12 Massey vanishing,
P13 operadic SC-formality, P14 betagamma witness, P15 universal family,
P16 Gerstenhaber bracket. Fix any errors.""")

agent("H04_heal_wave_A", """HEAL the Wave A fix agent outputs A01-A20.

These agents fixed broken refs, hardcoded Parts, duplicate labels, status mismatches,
proof-after-conjecture. Read the ACTUAL files they modified.
Verify: are the refs now correct? Are the labels unique? Are status tags matching
environments? Are proof-after-conj → remark changes appropriate?
Fix any errors or incomplete fixes.""")

agent("H05_heal_new_engines_v1", """HEAL the new compute engines created this session in Vol I.

Run git log --oneline -50 and identify all new .py files.
For each new engine:
1. Read the code — is it mathematically correct?
2. Does it have a matching test file?
3. Run the tests — do they pass?
4. Are expected values independently verified (AP10/AP128)?
Fix any issues. Create missing test files for untested engines.""")

agent("H06_heal_new_engines_v3", """HEAL the new compute engines in Vol III.

Same: identify all new .py files from recent commits.
Run tests. Verify correctness. Create missing tests.
Focus on: chiral_coproduct engines, e1_koszul, e2_koszul, tetrahedron,
k3_double_current, categorical_s_matrix, zamolodchikov.""", cwd=VOL3)

agent("H07_heal_CLAUDE_AGENTS", """HEAL CLAUDE.md and AGENTS.md across all volumes.

After 63+ commits and 592 agents, verify:
1. CLAUDE.md theorem status table matches current concordance
2. AGENTS.md skill routing still correct
3. Anti-pattern catalog (AP1-AP224) referenced correctly
4. Formula census (C1-C31) still accurate after all rectification
5. No stale claims in either file
Fix any stale content.""")

agent("H08_heal_concordance_final", """FINAL concordance healing.

Read chapters/connections/concordance.tex in its CURRENT state.
For EVERY theorem listed:
1. Find the theorem in its source file
2. Verify status matches
3. Verify scope matches
4. Verify the proof is present (if ProvedHere)
This is the FINAL constitutional audit of this session.
Fix every discrepancy.""")

agent("H09_heal_introduction_preface", """HEAL the introduction and preface after all rectification.

The platonic agents P18 (introduction) and P19 (preface) upgraded these.
Now verify:
1. Every theorem advertised in the introduction matches its CURRENT form
2. The preface does not overclaim any result
3. The geometric escalation ladder is consistent with the E_n theory
4. No stale statuses from before the session
Fix any remaining scope inflation.""")

agent("H10_session_summary", """Write the DEFINITIVE session summary.

Write to compute/audit/session_2026_04_13_elite_rescue.md:
1. Total agents: 592+ across 8+ campaigns
2. Anti-patterns: AP186-AP224 (39 new), B74-B78 (5), FM35-FM38 (4)
3. Theorem status: what is NOW proved, conditional, conjectural, open
4. Alternative proofs: which theorems have redundant proof paths
5. Literature cross-checks: which are confirmed
6. Compute verification: test suite status
7. Cross-volume consistency: what was verified
8. Remaining gaps: honest list
9. What the next session should prioritize
Be exhaustive and honest.""")


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Elite Rescue Campaign")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=45)
    args = parser.parse_args()

    print(f"Elite Rescue: {len(AGENTS)} agents -> {OUT}")
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

    summary = [f"# Elite Rescue Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
