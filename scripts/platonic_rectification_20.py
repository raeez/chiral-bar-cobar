#!/usr/bin/env python3
"""
Platonic Ideal Rectification Swarm — 20 Codex Agents
REFUSE to downgrade. UPGRADE to the strongest version.
If a theorem needs new mathematics to reach its platonic form: do the research.

Usage:
    python3 scripts/platonic_rectification_20.py --batch-size 5 --timeout 1800
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"platonic_rectification_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are a PLATONIC IDEAL rectification agent for a 4,500-page research mathematics manuscript.
Your mission: take each theorem to its STRONGEST possible form. REFUSE TO DOWNGRADE.

Hierarchy of action:
1. STRENGTHEN the proof to match the original claim (best outcome)
2. If the proof has a genuine gap: FILL IT with new mathematics
3. If the gap requires substantial new research: SKETCH the research programme needed, then
   state the strongest INTERMEDIATE result that IS proved, and mark the full claim as
   conditional on the identified research programme
4. NEVER silently narrow. If narrowing is needed, prove the narrow version is OPTIMAL
   by exhibiting a counterexample at the boundary of the narrow claim.

You have WRITE access. Make the edits. Verify after each edit.
</task>

<action_safety>
Only edit files in your assigned scope. After every edit, re-read the modified section.
Run grep for forbidden patterns (AP126 bare Omega, AP132 augmentation, AP29 slop).
</action_safety>

<completeness_contract>
Address every finding in your scope. For each: STRENGTHENED / FILLED / INTERMEDIATE+PROGRAMME / BLOCKED.
Do not stop until every finding is resolved or precisely blocked.
</completeness_contract>

<verification_loop>
After all edits: re-read the full modified region. Verify mathematical correctness.
Check that no new AP violations were introduced. State the final theorem in its strongest form.
</verification_loop>

<structured_output_contract>
End with:
## Platonic Rectification Report
For each theorem touched:
  - BEFORE: [original statement + status]
  - ISSUE: [what was wrong]
  - ACTION: [STRENGTHENED / FILLED / INTERMEDIATE / BLOCKED]
  - AFTER: [new statement + status]
  - CONFIDENCE: [high/medium/low]
  - REMAINING GAP: [if any]
</structured_output_contract>
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
# 20 PLATONIC RECTIFICATION AGENTS
# Each targets one foundational theorem or structural issue.
# REFUSE TO DOWNGRADE. UPGRADE OR FILL THE GAP.
# ═══════════════════════════════════════════════════════════════════

agent("P01_thm_A_verdier_upgrade", """THEOREM A: Bar-cobar adjunction + Verdier intertwining.

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES (from 105-agent audit):
1. Verdier half flips algebra/coalgebra in the proof
2. Missing "bar-degree analogue of Lemma filtered-comparison"
3. The family statement over M-bar_{g,n} uses genus-0 Verdier theorem for modular claim

YOUR MISSION: Do NOT narrow Theorem A. Instead:
1. Fix the algebra/coalgebra convention (state at algebra level post-D_Ran throughout)
2. WRITE the missing lemma (bar-degree filtered comparison) — derive it from the existing
   filtered-comparison lemma by adapting the filtration to bar degree
3. For the family statement: either prove the modular-family version properly (using the
   correct base-change for holonomic D-modules on Ran(X)), or identify the PRECISE
   obstruction and state the strongest intermediate result.

Search for 'thm:bar-cobar-adjunction' and 'Verdier'. Focus on lines 3600-3700 and 400-430.
WRITE the missing lemma near the existing filtered-comparison lemma.""")

agent("P02_thm_B_offlocus_upgrade", """THEOREM B: Bar-cobar inversion (Omega(B(A)) -> A qi on Koszul locus).

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex + chapters/theory/coderived_models.tex

KNOWN ISSUES:
1. Off-locus proof circular (coderived_models cites thm:higher-genus-inversion)
2. d^2=0 spectral sequence used in curved setting

YOUR MISSION: Do NOT restrict to on-locus only. Instead:
1. Prove coderived-adequacy INDEPENDENTLY using the intrinsic characterisation of D^co
   (Verdier quotient by coacyclic objects). The key: show the bar-cobar unit is a
   coacyclic-equivalence, not just a quasi-isomorphism.
2. For the curved setting: replace the d^2=0 spectral sequence with the CODERIVED spectral
   sequence (filtration on bar degree, d^2=kappa*omega_g absorbed into the E_1 page).
3. State the strongest result: on-locus qi (unconditional) + off-locus coderived equivalence
   (unconditional) + off-locus chain-level qi (conditional on kappa=0 or class G/L).

Search for 'thm:bar-cobar-inversion' and 'coderived-adequacy'.""")

agent("P03_thm_C0_curved_upgrade", """THEOREM C0: Fiber-center identification.

TARGET: chapters/theory/higher_genus_foundations.tex

KNOWN ISSUE: Proof applies ordinary cohomology to curved fiber bar (d_fib^2 = kappa*omega_g).

YOUR MISSION: Do NOT restrict to kappa=0. Instead:
1. Use the CODERIVED fiber bar complex, where the curvature is part of the structure.
   The coderived cohomology IS well-defined for curved complexes.
2. Alternatively: use the FLAT piece d_g (convolution differential, d_g^2=0) and prove
   the fiber-center identification via the flat differential, then lift to the curved
   setting via a comparison theorem (flat -> curved in D^co).
3. State the strongest result: C0 holds unconditionally in the coderived category;
   the ordinary-cohomology version holds when kappa=0 or under perfectness.

Search for 'thm:fiber-center' or 'C0' near 'higher_genus'. Focus on lines 230-400.""")

agent("P04_thm_C1_genus0_upgrade", """THEOREM C1: Lagrangian eigenspace decomposition.

TARGET: chapters/connections/thqg_symplectic_polarization.tex

KNOWN ISSUES:
1. Q_g(A) ≅ Q_g(A^!)^v claimed for all g>=0, but Q_0(A^!)=0 at g=0
2. Involution sigma uses vv without reflexivity hypothesis

YOUR MISSION: Do NOT just add g>=1. Instead:
1. UNDERSTAND why Q_0(A^!)=0. Is this correct? At g=0, the complementarity map should
   degenerate in a controlled way. The center Z(A) at g=0 is the chiral center;
   Z(A^!) should be the Koszul-dual center. Investigate: is Q_0(A^!) genuinely 0,
   or is the g=0 identification wrong?
2. If Q_0(A^!)=0 is correct: prove it's the OPTIMAL boundary — exhibit why no duality
   can hold at g=0 (the Koszul-dual center is trivial because...).
3. For reflexivity: prove it using the perfectness criterion that's already in the manuscript.
   The fiber cohomology IS perfect by the existing prop:perfectness-criterion.

Search for 'Q_0' and 'sigma' and 'involution'. Focus on lines 150-700.""")

agent("P05_thm_C2_nondegen_upgrade", """THEOREM C2: Scalar BV pairing (conditional on uniform-weight).

TARGET: chapters/theory/higher_genus_complementarity.tex

KNOWN ISSUES:
1. Proof switches from D(bar B(A)) to Omega(A^!) mid-argument
2. Lagrangian eigenspace lift from center-side to bar-side missing

YOUR MISSION: STRENGTHEN by:
1. Fix the object identity: D_Ran(bar B(A)) = (A)^!_inf consistently throughout.
   The nondegeneracy argument uses the Verdier-bar-cobar theorem; cite it correctly.
2. PROVE the center-to-bar lift: the Lagrangian decomposition on H*(M-bar_g, Z(A))
   lifts to the bar complex via the bar-center comparison (Theorem C0). Write this
   explicitly as a lemma.
3. Investigate: can uniform-weight be weakened? What is the MINIMAL condition?
   At multi-weight, delta_F_g^cross appears. Can C2 hold with a modified pairing
   that accounts for delta_F_g^cross? Sketch the research direction.

Search for 'thm:shifted-symplectic' and 'nondegeneracy'. Focus on lines 1900-2000.""")

agent("P06_thm_D_circularity_upgrade", """THEOREM D: obs_g = kappa * lambda_g (uniform-weight).

TARGET: chapters/theory/higher_genus_modular_koszul.tex + higher_genus_foundations.tex

KNOWN ISSUE: Circular dependency thm:genus-universality <-> thm:family-index.

YOUR MISSION: BREAK the circularity by providing an INDEPENDENT proof of thm:family-index.

Strategy: The family-index theorem should follow from:
1. The shadow tower gives obs_g as a specific cohomology class on M-bar_g
2. The Mumford-type computation identifies this class with kappa*lambda_g
3. This identification uses the Grothendieck-Riemann-Roch theorem applied to the
   universal curve, NOT thm:genus-universality

Write the independent proof. The key computation: the fiber bar complex is a complex
of vector bundles on M-bar_g; its Euler class in K-theory is computed by GRR; the
result is kappa * ch_1(E) = kappa * lambda_1 at genus 1, extending to lambda_g by
the shadow tower recursive structure.

Search for 'thm:family-index' and 'thm:genus-universality'. Focus on the proof of
thm:family-index and provide the independent computation.""")

agent("P07_thm_H_upgrade", """THEOREM H: ChirHoch*(A) polynomial Hilbert series, concentrated in {0,1,2}.

TARGET: chapters/theory/chiral_hochschild_koszul.tex

KNOWN ISSUES:
1. Bar-coalgebra/Koszul-dual conflation (bar B^v ≠ A^!)
2. Configuration-space collapse not justified

YOUR MISSION: STRENGTHEN by:
1. Fix the identification chain: bar B(A) -> H*(bar B(A)) = A^i -> (A^i)^v = A^!
   with Verdier duality replacing linear dual. Write the correct comparison.
2. PROVE the configuration-space collapse: construct a spectral sequence from the FM tower
   filtration (FM_{p+2}(X) has a filtration by p-collision strata) whose E_2 page
   is D_X-Ext on the base curve. The collapse follows from the formality of
   FM_n(C) (Kontsevich) or from the weight filtration on mixed Hodge structure.
3. With both fixes: verify concentration in {0,1,2} follows from the curve dimension
   (dim X = 1, so D_X-Ext has cohomological amplitude [0,2]).

Search for 'thm:main-koszul-hoch' and 'thm:hochschild-polynomial-growth'.""")

agent("P08_MC1_PBW_whitehead_upgrade", """MC1: PBW theorem.

TARGET: chapters/theory/higher_genus_modular_koszul.tex

KNOWN ISSUE: Whitehead lemma applied to truncated current algebra without justification.

YOUR MISSION: PROVE the Whitehead reduction properly:
1. The truncated current algebra g[t]/t^N has a weight decomposition where g acts
   on each weight piece. The enrichment classes live in H*(g, M_h) for weight-h modules M_h.
2. Whitehead: H^1(g, M) = 0 for semisimple g and any finite-dimensional M. This kills
   the enrichment at genus 0 -> genus 1.
3. The mixed maps (genus-0/genus-1) factor through the g-action on the weight pieces.
   WRITE this factorisation explicitly as a lemma.
4. State the PBW theorem in its STRONGEST form: the spectral sequence from bar degree
   to modular degree collapses at E_1 for ALL families where the underlying Lie algebra
   is semisimple. For non-semisimple families: characterise the obstruction.

Search for 'PBW' and 'Whitehead' near lines 990-1100 and 1290-1300.""")

agent("P09_MC3_baxter_upgrade", """MC3: Thick generation.

TARGET: chapters/examples/yangians_computations.tex

KNOWN ISSUES:
1. lambda=0 Baxter constraint is NOT vacuous (b = a - 1/2)
2. Finite-dim to completed extension not proved

YOUR MISSION: Do NOT restrict MC3 to avoid the Baxter constraint. Instead:
1. PROVE thick generation SUBJECT TO the Baxter constraint. The constraint b = a - 1/2
   defines a codimension-1 locus; show that the shifted prefundamental representations
   on this locus still generate the relevant category.
2. For the completion extension: use localising generation theory (Neeman/Bondal-Van den Bergh).
   The key: if {P_i} generate D^b(O), they also generate D^b(O-hat) under suitable
   completeness conditions. Cite the relevant theorem from derived algebraic geometry.
3. State MC3 in its STRONGEST form: thick generation on the Baxter locus for type A
   (unconditional), with the completion extension (conditional on localising generation
   in the completed category).

Search for 'thm:shifted-prefundamental' and 'Baxter'. Focus on lines 3050-3230.""")

agent("P10_MC5_coderived_upgrade", """MC5: BV/bar identification.

TARGET: chapters/connections/bv_brst.tex

KNOWN ISSUES:
1. Class-M harmonic mechanism unproved
2. Coderived category misuse

YOUR MISSION: PROVE the harmonic mechanism:
1. The harmonic decomposition delta_r^harm = c_r(A)*m_0^{floor(r/2)-1} should follow from:
   (a) the Hodge decomposition on the fiber bar complex (bar differential d_B + curvature m_0),
   (b) the harmonic projection P_harm commuting with powers of m_0 (by degree counting),
   (c) the fact that delta_r restricted to harmonics factors through m_0^{floor(r/2)-1}
   because the only degree-compatible insertion is through the curvature.
2. Fix the coderived argument: use the correct characterisation (coacyclic quotient).
   The key: the bar-BV comparison map sends the curvature d^2 = m_0 to the BV operator
   delta. In D^co, this is an equivalence because m_0-torsion objects are coacyclic
   (they are totalizations of the m_0-Koszul complex, which is exact).
3. State MC5 in its STRONGEST form: coderived BV/bar equivalence for ALL shadow classes
   (unconditional), with the chain-level equivalence for class G/L (unconditional) and
   class C (conditional on harmonic decoupling).

Search for 'thm:bv-bar-coderived' and 'delta_r'. Focus on lines 1920-1960.""")

agent("P11_topologization_chainlevel", """TOPOLOGIZATION: SC^{ch,top} + Sugawara = E_3.

TARGET: chapters/theory/en_koszul_duality.tex

KNOWN ISSUE: Chain-level E_3 not proved; only cohomological.

YOUR MISSION: Push the chain-level result as far as possible:
1. The cohomological E_3 IS proved for affine KM. State this cleanly.
2. For chain-level: the obstruction is that [Q,G] = T_Sug + Q-exact correction, where
   the correction is not strictly zero. INVESTIGATE: can the correction be removed by
   a gauge transformation? The homotopy transfer theorem gives a chain-level structure
   UNIQUE UP TO A-inf quasi-isomorphism. This means there EXISTS a chain-level E_3
   structure on a qi-equivalent model. State this.
3. The obstruction to chain-level E_3 on the ORIGINAL cochain complex (not a qi model)
   is an A-inf coherence condition. Characterise it precisely.
4. State the STRONGEST result: (a) cohomological E_3 unconditional for affine KM,
   (b) chain-level E_3 on a qi-equivalent model unconditional for affine KM,
   (c) chain-level E_3 on the original complex conditional on A-inf coherence,
   (d) general (non-KM) conjectural.

Search for 'thm:topologization' and 'Sugawara'. Focus on lines 2940-3200.""")

agent("P12_koszul_vii_viii_upgrade", """KOSZUL EQUIVALENCES (vii) and (viii).

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES:
1. (vii) proved only at g=0, listed as unconditional
2. (viii) claims free polynomial ChirHoch, only duality+concentration proved

YOUR MISSION:
1. For (vii): PROVE the all-genera version. The obstruction is delta_F_g^cross at g>=2
   for multi-weight. Strategy: show that on the UNIFORM-WEIGHT locus, (vii) extends
   to all genera. The shadow tower obs_g = kappa*lambda_g at uniform weight IS the
   all-genera (vii). Write this proof explicitly.
2. For (viii): INVESTIGATE freeness. The polynomial Hilbert series is proved. Does
   concentration in {0,1,2} + polynomial Hilbert series IMPLY freeness for graded-commutative
   algebras? If the algebra is in degrees {0,1,2} with a 1-dimensional degree-0 piece,
   the algebra is generated in degree 1 and 2 with relations in degree 2 and 3.
   This is free iff there are no relations in degree 2 (= no Massey products).
   PROVE vanishing of Massey products from the formality of FM_n(C).
3. State the STRONGEST versions of (vii) and (viii).

Search for 'equiv' near 'vii' and 'viii' in the file.""")

agent("P13_SC_formality_upgrade", """SC-FORMALITY: A is SC-formal iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex

KNOWN ISSUES:
1. Converse proof uses bilinear form that doesn't exist for betagamma
2. Forward proof only verified for Heisenberg, not full class G

YOUR MISSION:
1. For the FORWARD direction (class G => SC-formal): prove it for ALL class-G families
   (Heisenberg, lattice VOAs, free fermions). The key: class G means S_4 = 0 and
   Delta = 0 (shadow tower finite at degree 2). SC-formality means m_k^{SC} = 0 for k>=3.
   Prove: Delta=0 implies the SC mixed-sector operations vanish at order 3+.
   This should follow from the shadow tower controlling the SC operations via the
   averaging map.
2. For the CONVERSE (SC-formal => class G): replace the bilinear-form argument with
   a purely operadic one. SC-formality means the SC bar complex is formal. Formality
   of the SC bar implies the shadow tower truncates at degree 2 (by the tower-bar
   correspondence). Shadow tower truncation at degree 2 means Delta = 0, which means
   class G.

Search for 'SC-formal' and 'class G'. Focus on lines 2520-2560.""")

agent("P14_depth_gap_upgrade", """DEPTH GAP: d_alg in {0,1,2,inf}, gap at 3.

TARGET: chapters/theory/higher_genus_modular_koszul.tex

KNOWN ISSUES:
1. d_alg=2 witness (betagamma) on wrong parameter line
2. prop over-scoped with kappa!=0 excluding the d_alg=2 case

YOUR MISSION:
1. Fix the betagamma witness: identify the CORRECT parameter line where d_alg=2 is realized.
   The standard conformal-weight line (not the weight-changing line where tower vanishes).
   Compute S_2, S_3, S_4 on this line explicitly. Verify S_4 != 0 but S_r = 0 for r >= 5.
2. PROVE the impossibility of d_alg=3: the MC equation at degree 4 gives
   S_4 = f(kappa, S_2, S_3). At d_alg=3 we'd need S_3 != 0, S_4 = 0. But the MC
   relation at degree 4 constrains: if S_3 != 0 then S_4 = g(kappa, S_3) != 0
   (unless a specific cancellation occurs). PROVE this non-cancellation.
3. State in the STRONGEST form with correct witnesses for all four values.

Search for 'depth-gap' and 'trichotomy'. Focus on lines 17100-17200 and 16400-16430.""")

agent("P15_D2_zero_space_upgrade", """D^2=0 ON MODULI.

TARGET: chapters/theory/higher_genus_modular_koszul.tex

KNOWN ISSUE: Proof uses fixed-curve log FM (no curve degenerations) when it needs the
universal family over M-bar_{g,n} (which has curve degenerations).

YOUR MISSION:
1. REWRITE the D^2=0 proof to work on the universal family. The key spaces:
   - The universal curve pi: C_{g,n} -> M-bar_{g,n}
   - The relative FM compactification FM_k(C_{g,n}/M-bar_{g,n})
   - The boundary strata: FM collisions (fibers) + curve degenerations (base)
2. The D^2=0 argument: the bar differential d_B comes from FM collision strata;
   d_B^2 = 0 because the FM collision strata satisfy the Arnold relation.
   The curvature d_fib^2 = kappa*omega_g comes from the curve-degeneration strata
   (Hodge class). WRITE this cleanly with the correct spaces.
3. State: D^2_bar = 0 unconditionally (Arnold relation on FM); D^2_fib = kappa*omega_g
   from the Hodge class on the universal family.

Search for 'D^2' and 'moduli' and 'log FM'. Focus on lines 30850-30900.""")

agent("P16_gerstenhaber_upgrade", """GERSTENHABER BRACKET ON DERIVED CENTER.

TARGET: chapters/theory/chiral_hochschild_koszul.tex

KNOWN ISSUES:
1. Construction gives single insertion, not antisymmetrised bracket
2. thm:gerstenhaber-structure tagged ProvedHere but has no proof

YOUR MISSION: WRITE the proof:
1. Define the pre-Lie product f ∘ g via the chiral insertion-residue sum (the single
   insertion already in Construction 4855-4875).
2. Define the Gerstenhaber bracket {f,g} = f∘g - (-1)^{|f||g|} g∘f (antisymmetrisation).
3. PROVE the bracket satisfies graded Jacobi using the brace relations on the
   chiral endomorphism operad End^{ch}_A. The key: the brace relations follow from
   the associativity of the chiral product on FM_k(C), which gives the Jacobi identity
   via the Stasheff-type boundary relations on FM_3(C).
4. PROVE the bracket is a derivation of the cup product (Gerstenhaber compatibility)
   using the brace-cup compatibility from the SC^{ch,top} operadic structure.
5. State as ProvedHere with the complete proof.

Search for 'thm:gerstenhaber-structure' and 'const:gerstenhaber-bracket'.""")

agent("P17_concordance_sync", """CONCORDANCE CONSTITUTIONAL SYNC.

TARGET: chapters/connections/concordance.tex

YOUR MISSION: Synchronise the concordance (the constitution) with ALL changes from
the current rectification session. For each theorem:
1. Read the CURRENT theorem statement in its source file
2. Compare with the concordance entry
3. Update the concordance to match

Key updates needed:
- Theorem A: Verdier half at algebra level (post-D_Ran)
- Theorem B: on-locus qi (unconditional) + off-locus coderived (unconditional)
- Theorem C0: coderived version unconditional; ordinary-cohomology version conditional
- Theorem C1: g>=1 duality; genus-0 treated separately
- Theorem C2: object identity fixed; conditional on uniform-weight
- Theorem D: non-circular proof path; routing remark
- Theorem H: configuration-space collapse proved via FM formality
- MC2: g^{mod} carrier for main theorem; g^{E1} in e1_modular_koszul
- MC3: conditional on Baxter constraint
- MC4: filtration corrected; resonance lane conditional on transfer
- MC5: coderived unconditional; chain-level conditional for class M
- Topologization: cohomological proved (affine KM); chain-level via qi model; general conjectural
- Koszul (vii): uniform-weight all-genera; multi-weight g=0 only
- Koszul (viii): concentration + polynomial proved; freeness conditional on Massey vanishing

Also add routing remark for Theorem D non-circular path.""")

agent("P18_introduction_upgrade", """INTRODUCTION: Make the five theorems feel inevitable.

TARGET: chapters/theory/introduction.tex

YOUR MISSION: Rewrite the theorem announcements in the introduction to match the
STRONGEST versions from the current rectification. The introduction must:
1. State each theorem in its strongest proved form
2. Explicitly name what is conditional and on what
3. Not overclaim (AP215)
4. Make the theorems feel INEVITABLE (Gelfand) — each follows from the previous
   by mathematical necessity, not by choice
5. Fix the MC2 mis-attribution (cite e1_modular_koszul for E1 version)
6. Fix the MC4 application scope (weight-completion qualifier)

Use Chriss-Ginzburg structural moves: deficiency opening for each theorem
(what FAILS without this theorem), unique survivor (why THIS is the right statement),
instant computation (verify on Heisenberg or sl_2 immediately after stating).

Read the current introduction. Rewrite the theorem-announcement sections.""")

agent("P19_preface_upgrade", """PREFACE: Symphonic standard, all voices.

TARGET: chapters/frame/preface.tex

YOUR MISSION: Audit and upgrade the preface to reflect the CURRENT state of the programme
after the adversarial audit and rectification. The preface must:
1. Not overclaim any theorem (compare with concordance)
2. Present the strongest versions of all results
3. Explicitly name the open problems (chain-level topologization, MC5 chain-level class M,
   Koszul freeness, Baxter constraint, general topologization)
4. Use all 12 voices (Gelfand/Beilinson/Drinfeld/Kazhdan/Etingof/Polyakov/Nekrasov/
   Kapranov/Ginzburg/Costello/Gaiotto/Witten)
5. Achieve the geometric escalation: point -> R -> C -> H -> D -> annulus -> genus g ->
   E_2 -> E_3-TOPOLOGICAL (not E_3-chiral)

Focus on the theorem announcement sections. Verify each claim against the concordance.
Do NOT rewrite the whole preface — only the sections that advertise theorem status.""")

agent("P20_standalone_sync", """STANDALONE PAPERS: Sync with rectified theorems.

TARGET: standalone/ (all .tex files)

YOUR MISSION: For each standalone paper:
1. Read the theorem statements
2. Compare with the CURRENT versions in the main manuscript (after rectification)
3. Fix any scope inflation, stale status, or convention drift
4. Verify macros are defined via \\providecommand (FM6)
5. Verify formulas match the canonical census

Key fixes needed:
- N3_e1_primacy.tex: averaging identity Sugawara shift (already partially fixed)
- ordered_chiral_homology.tex: E1 ordered bar content
- All standalones: check theorem status matches current concordance

Be exhaustive. Fix every discrepancy.""")


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Platonic Ideal Rectification")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=30)
    args = parser.parse_args()

    print(f"Platonic Rectification: {len(AGENTS)} agents → {OUT}")
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

    summary = [f"# Platonic Rectification Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
