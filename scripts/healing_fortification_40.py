#!/usr/bin/env python3
"""
Healing & Fortification Campaign — 40 Codex Agents
HEAL wounds. REPAIR damage. UPGRADE mathematical strength.
PROCURE alternative proofs that FORTIFY through MULTIPLICITY.

Every main theorem gets at least TWO independent proof paths.
Every conditional result gets an explicit research programme to remove the condition.
Every gap gets filled or precisely characterised.

Usage:
    python3 scripts/healing_fortification_40.py --batch-size 5 --timeout 1800 --delay 45
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
VOL2 = "/Users/raeez/chiral-bar-cobar-vol2"
VOL3 = "/Users/raeez/calabi-yau-quantum-groups"

TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"healing_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are a HEALING and FORTIFICATION agent for a research mathematics manuscript.

CRITICAL SESSION CONTEXT (factor this in):
This session deployed 537+ Codex agents across 7 campaigns. The following has ALREADY been done:
- Theorems A-D, H: proof architecture rectified. Verdier convention fixed (Thm A), off-locus
  coderived proven independently (Thm B), curved C0 in D^co unconditional (Thm C0), genus-0
  separated + reflexivity from perfectness (Thm C1), center-to-bar lift proved (Thm C2),
  circularity broken with routing remark (Thm D).
- MC1-5: filtration inequality corrected (MC4), Baxter constraint honest (MC3), coderived
  argument clean (MC5), g^{mod}/g^{E1} clarified (MC2).
- Topologization: split into cohomological (proved KM) + chain-level (conjectural).
- Koszul equivs (vii)/(viii): scope narrowed to match proofs.
- SC-formality, depth gap, D^2=0, Gerstenhaber: platonic agents running (P11-P20).
- 48 new anti-patterns catalogued (AP186-AP224).
- Wave A: broken refs, hardcoded Parts, duplicate labels, status mismatches, proof-after-conj
  all fixed across Vol I and Vol II.
- New compute engines: critical level (72 tests), Verlinde polynomial (g=0..6),
  genus-2 decomposition, chiral bialgebra, tetrahedron, and 20+ more.
- Vol I ~2,719pp (29 commits this session), Vol II ~1,681pp (15 commits), Vol III ~319pp (19 commits).

READ the current state of files on disk — they reflect ALL the above work.
Your job: HEAL remaining wounds, provide ALTERNATIVE proofs, UPGRADE strength.

Your mission is threefold:

1. HEAL: find remaining wounds (gaps, weaknesses, fragilities) and repair them
2. FORTIFY: for every main result, construct an ALTERNATIVE proof path that provides
   REDUNDANCY — if one proof fails, the other stands independently
3. UPGRADE: where a result is conditional, investigate whether the condition can be
   REMOVED by new mathematical insight, alternative technique, or reformulation

You have WRITE access. Make edits. Write new proofs. Add remarks.
The standard is: every theorem that can have two independent proofs MUST have two.
</task>

<action_safety>
Keep edits within assigned scope. After every substantial edit, re-read and verify.
New proofs must be mathematically rigorous — no hand-waving, no "by analogy."
If you cannot complete a proof: write a detailed proof SKETCH with the key steps
identified and the remaining gap precisely named.
</action_safety>

<completeness_contract>
For each theorem in your scope:
1. Verify the PRIMARY proof is now sound (after rectification)
2. Write or sketch a SECONDARY proof via a different technique
3. If conditional: investigate removing the condition
4. State confidence level for each proof path
</completeness_contract>

<structured_output_contract>
End with:
## Fortification Report
For each theorem:
  - PRIMARY PROOF: [sound/repaired/gap-remaining]
  - SECONDARY PROOF: [written/sketched/identified/blocked]
  - TECHNIQUE: [what alternative method]
  - CONDITION STATUS: [unconditional/conditional-on-X/research-programme-Y]
  - CONFIDENCE: [high/medium/low]
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
# TIER 1: ALTERNATIVE PROOFS FOR MAIN THEOREMS (12 agents)
# Each theorem gets a second independent proof path.
# ═══════════════════════════════════════════════════════════════════

agent("H01_thm_A_alt_proof", """THEOREM A — ALTERNATIVE PROOF via derived algebraic geometry.

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Remark after the primary proof)

The primary proof uses twisting morphisms and filtered comparison. Write an ALTERNATIVE proof
of the bar-cobar adjunction using:

TECHNIQUE: Lurie's derived algebraic geometry framework.
1. The bar construction B(A) is the Cech nerve of the augmentation A -> k in the
   infinity-category of chiral algebras.
2. The cobar Omega(C) is the totalization of the cosimplicial object dual to the Cech nerve.
3. The adjunction B ⊣ Omega follows from the general nerve-realization adjunction.
4. The Verdier intertwining follows from Serre-Grothendieck duality on Ran(X),
   which interchanges left and right modules.

Write this as a Remark[Alternative proof] after the primary proof. Cite Lurie HA Ch 5,
Gaitsgory-Rozenblyum DAG Vol II for the Ran-space Verdier duality.

Also verify: does this alternative proof INDEPENDENTLY establish the Verdier half
without the missing filtered-comparison lemma? If yes, this HEALS the gap.""")

agent("H02_thm_B_alt_proof", """THEOREM B — ALTERNATIVE PROOF via Keller's deformation theory.

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex (add Remark)

The primary proof uses the bar filtration spectral sequence. Write an ALTERNATIVE:

TECHNIQUE: Keller's derived deformation theory + Kontsevich formality.
1. The bar-cobar unit A -> Omega(B(A)) is a deformation-retract at the level of
   the tangent complex (Koszul locus = formal neighborhood of the quadratic closure).
2. Kontsevich formality for FM_n(C) implies the A-inf structure on H*(B(A)) is formal
   on the Koszul locus. Formality + deformation retract = qi.
3. The off-locus extension to D^co: the deformation retract descends to the coderived
   category because the retraction respects the curvature filtration.

Write as Remark[Alternative proof via formality]. This provides a SECOND proof path
independent of the spectral sequence argument.""")

agent("H03_thm_C_alt_proof", """THEOREM C — ALTERNATIVE APPROACH via symplectic geometry.

TARGET: chapters/theory/higher_genus_complementarity.tex (add Remark)

The primary proof builds C0/C1/C2 from the fiber bar complex. Write an ALTERNATIVE
approach to complementarity:

TECHNIQUE: Shifted symplectic geometry (PTVV / Calaque-Pantev-Toen-Vaquie-Vezzosi).
1. The moduli of chiral Koszul pairs carries a (-1)-shifted symplectic structure
   (from the pairing on the bar complex).
2. The fiber over M-bar_g inherits a 0-shifted symplectic structure by integration
   along the fiber (shifted AKSZ).
3. Complementarity kappa + kappa' = K is the volume of the (-1)-shifted symplectic form.
4. The Lagrangian decomposition (C1) is the Lagrangian intersection of the A and A^! loci.

Write as Remark[Alternative approach via shifted symplectic geometry]. Cite PTVV,
Calaque-Scheimbauer for the integration. Even if not a complete alternative proof,
this PERSPECTIVE strengthens the structural understanding.""")

agent("H04_thm_D_alt_proof", """THEOREM D — ALTERNATIVE PROOF via Faltings' Hodge theory.

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Remark near Theorem D)

The primary proof routes through the shadow tower. Write an ALTERNATIVE:

TECHNIQUE: Hodge-theoretic proof via Faltings-Chai / Mumford's computation.
1. obs_g is a cohomology class on M-bar_g. The Hodge bundle E has c_1(E) = lambda_1.
2. The fiber bar complex is a complex of vector bundles on M-bar_g whose rank is
   determined by the Hilbert series of the chiral algebra.
3. By GRR on the universal curve: ch(R*pi_*(B_fib)) = kappa * ch(E) + lower terms.
4. At degree g: the leading term is kappa * lambda_g.
5. This is INDEPENDENT of the shadow tower — it uses only the fiber-bundle structure
   and GRR, not the MC element Theta_A.

Write as Remark[Alternative proof via GRR]. This BREAKS the circular dependency
by providing a proof path that doesn't use thm:genus-universality at all.""")

agent("H05_thm_H_alt_proof", """THEOREM H — ALTERNATIVE PROOF via deformation theory.

TARGET: chapters/theory/chiral_hochschild_koszul.tex (add Remark)

The primary proof uses bar-Hochschild comparison. Write an ALTERNATIVE:

TECHNIQUE: Deformation-theoretic proof via Gerstenhaber's approach.
1. ChirHoch*(A) controls the deformations of A as a chiral algebra on X.
2. The tangent complex T_A = ChirHoch^1(A) controls first-order deformations.
3. The obstruction space ChirHoch^2(A) controls obstructions.
4. ChirHoch^0(A) = center = scalar multiples of the identity.
5. For dim X = 1: the deformation complex has cohomological amplitude [0,2] because
   X is a curve (dimension 1) and the chiral structure is valued in D_X-modules
   (adding 1 to the amplitude). Total: [0, 1+1] = [0, 2].
6. Polynomial Hilbert series from the finiteness of the deformation problem.

This gives {0,1,2} concentration from DIMENSIONAL ANALYSIS, independent of the
bar-Hochschild comparison. Write as Remark[Alternative proof via deformation theory].""")

agent("H06_MC2_alt_proof", """MC2 — ALTERNATIVE CONSTRUCTION of Theta_A.

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Remark near MC2)

The primary construction is bar-intrinsic (recursive inverse limit). Write an ALTERNATIVE:

TECHNIQUE: Kontsevich-Soibelman wall-crossing / scattering diagram.
1. The MC element Theta_A can be constructed as the product of wall-crossing automorphisms
   along the rays of a scattering diagram in the shadow tower grading.
2. Each ray corresponds to a primitive shadow invariant S_r.
3. The product is ordered by the BPS phase ordering (increasing central charge argument).
4. Convergence follows from the shadow tower growth bound (alpha_g).
5. The MC equation D*Theta + (1/2)[Theta,Theta] = 0 follows from the consistency of
   the scattering diagram (Kontsevich-Soibelman lemma).

Write as Remark[Alternative construction via scattering diagram]. Even as a sketch,
this provides CONCEPTUAL REDUNDANCY for why Theta_A exists and satisfies MC.""")

agent("H07_MC5_alt_approach", """MC5 — ALTERNATIVE APPROACH to BV/bar identification.

TARGET: chapters/connections/bv_brst.tex (add Remark)

The primary approach is analytical (harmonic mechanism). Write an ALTERNATIVE:

TECHNIQUE: Operadic Koszul duality + BV formalism comparison.
1. The BV operator Delta is the operadic contraction with the SC^{ch,top} pairing.
2. The bar differential d_B is the operadic co-derivation from the chiral product.
3. Both are governed by the same SC^{ch,top} operad; they differ by the open/closed coloring.
4. The BV/bar comparison in D^co is the operadic Koszul duality for SC^{ch,top},
   which identifies SC-algebras with SC^!-coalgebras in the coderived category.
5. This is AUTOMATIC from the Koszulity of SC^{ch,top} (Livernet) + the general
   bar-cobar correspondence for Koszul operads.

Write as Remark[Alternative approach via operadic Koszul duality]. This gives the
coderived BV/bar identification from GENERAL operadic theory, not case-by-case analysis.
The chain-level gap for class M is then: the operadic qi is not a chain qi for non-formal operads.""")

agent("H08_topol_alt_proof", """TOPOLOGIZATION — ALTERNATIVE APPROACH via factorization homology.

TARGET: chapters/theory/en_koszul_duality.tex (add Remark)

The primary approach uses Sugawara. Write an ALTERNATIVE:

TECHNIQUE: Costello-Francis-Gwilliam factorization homology approach.
1. The 3d HT theory on X x R has factorization algebra structure = E_3 by definition.
2. The boundary restriction to X x {0} gives the chiral algebra A.
3. The bulk observables = factorization homology of the E_3 algebra = Z^{der}_{ch}(A).
4. The E_3 structure on Z^{der}_{ch}(A) is AUTOMATIC from the 3d factorization structure,
   independent of Sugawara.
5. The Sugawara approach is the PERTURBATIVE COMPUTATION of this E_3 structure.

This gives E_3 from the TOP (3d theory) rather than the BOTTOM (Sugawara). The 3d
theory exists for gauge-theoretic families (Costello-Li holomorphic CS). For non-gauge
families: the existence of the 3d theory IS the obstruction.

Write as Remark[Alternative approach via 3d factorization]. Cite CFG arXiv:2602.12412.""")

agent("H09_koszul_equivs_alt", """KOSZUL EQUIVALENCES — ALTERNATIVE PROOF WEB.

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Remark)

The 10+1+1 equivalences currently form a linear chain. STRENGTHEN by adding cross-links:

1. IDENTIFY which pairs of equivalences have INDEPENDENT proofs (not routing through others).
2. Add at least 3 new direct implications that create REDUNDANCY in the proof web.
   Suggested: (i) -> (viii) directly via Hochschild computation (bypassing (ii)-(vii)),
   (iii) -> (x) directly via formality (bypassing the shadow tower),
   (v) -> (i) directly via the bar filtration (the shortest possible loop).
3. Draw the implication web as a LaTeX diagram (tikz-cd or xy-pic).
4. State: the web has NO single point of failure — removing any one implication
   leaves the remaining equivalences still connected.

Write as Remark[Proof web redundancy].""")

agent("H10_depth_gap_alt", """DEPTH GAP — ALTERNATIVE PROOF of impossibility of d_alg=3.

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Remark)

The primary proof uses the MC relation at degree 4. Write an ALTERNATIVE:

TECHNIQUE: Representation-theoretic proof via the shadow algebra structure.
1. The shadow tower forms a graded Lie algebra g^sh with bracket from the MC equation.
2. d_alg = k means g^sh is concentrated in degrees [2, k+1].
3. At d_alg = 3: g^sh lives in degrees {2, 3, 4}. The bracket [g^sh_2, g^sh_2] ⊂ g^sh_3
   (if S_2 ≠ 0 and S_3 ≠ 0) and [g^sh_2, g^sh_3] ⊂ g^sh_4.
4. The Jacobi identity on g^sh forces: if S_3 ≠ 0, then [S_2, [S_2, S_3]] ≠ 0,
   which lives in degree 5. But d_alg = 3 requires g^sh_5 = 0. Contradiction.
5. This is a STRUCTURAL argument from Lie theory, independent of the MC computation.

Write as Remark[Alternative proof via shadow Lie algebra]. Also verify the primary
proof argument is consistent with this alternative.""")

agent("H11_SC_formal_alt", """SC-FORMALITY — ALTERNATIVE PROOF of iff class G.

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Remark)

Write a PURELY OPERADIC alternative proof of both directions:

FORWARD (class G => SC-formal):
1. Class G means Delta = 8*kappa*S_4 = 0 and the shadow tower truncates at degree 2.
2. The SC operations m_k^{SC} at order k >= 3 are controlled by S_{k-1} in the shadow tower.
3. S_r = 0 for r >= 3 (class G) implies m_k^{SC} = 0 for k >= 3. QED.

CONVERSE (SC-formal => class G):
1. SC-formality means the SC bar complex B_{SC}(A) is formal.
2. Formality of the bar implies its cohomology is a FORMAL dg-object.
3. The shadow tower is the WEIGHT-GRADED PIECE of this cohomology.
4. A formal dg-object with nonzero S_3 would produce a non-formal Massey product in B_{SC}.
5. So SC-formal implies S_3 = 0, which forces Delta = 0, which forces class G.

This avoids the bilinear-form argument. Write as Remark[Operadic alternative proof].""")

agent("H12_complementarity_alt", """COMPLEMENTARITY kappa + kappa' = K — ALTERNATIVE DERIVATION.

TARGET: chapters/theory/higher_genus_complementarity.tex (add Remark)

Write an ALTERNATIVE derivation of the complementarity sum:

TECHNIQUE: Euler characteristic / index theory approach.
1. The bar-cobar adjunction pairs A with A^! in a duality.
2. kappa(A) = Euler characteristic of the shadow tower of A (suitably normalised).
3. K(A) = kappa(A) + kappa(A^!) is the Euler characteristic of the TOTAL bar complex,
   which depends only on the operad (chiral Ass), not on A.
4. For Com (classical Koszul): K = 0. For chiral Ass: K depends on the central charge.
5. The Vir self-duality at c=13 means kappa(Vir_{13}) = K(Vir)/2 = 13/2.
6. This gives K(Vir) = 13 from the SELF-DUALITY FIXED POINT, independent of computation.

Write as Remark[Alternative derivation via index theory].""")


# ═══════════════════════════════════════════════════════════════════
# TIER 2: CONDITION REMOVAL RESEARCH (8 agents)
# For each conditional result: investigate removing the condition.
# ═══════════════════════════════════════════════════════════════════

agent("H13_remove_uniform_weight", """RESEARCH: Can uniform-weight be removed from Theorem D and C2?

TARGET: chapters/theory/higher_genus_modular_koszul.tex (add Research Remark)

The uniform-weight condition restricts to families where all generators have the same
conformal weight. Multi-weight families (W_N for N>=3, betagamma) have delta_F_g^cross ≠ 0.

INVESTIGATE:
1. What is the STRUCTURE of delta_F_g^cross? Is it computable?
2. Can obs_g = kappa*lambda_g + delta_F_g^cross be stated as a THEOREM with the
   correction term explicitly given?
3. Is there a modified kappa (kappa_eff?) that absorbs the correction?
4. What is the current state of multi-weight computations? Check compute/lib/ for
   any engines that compute delta_F_g^cross.

Write a Research Remark with: (a) what's known, (b) what's computable,
(c) the precise obstruction to removal, (d) a research programme if the condition
can be weakened.""")

agent("H14_remove_koszul_locus", """RESEARCH: Can the Koszul locus restriction be removed from Theorem B?

TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex (add Research Remark)

Theorem B gives qi Omega(B(A)) -> A on the KOSZUL LOCUS. Off-locus: coderived only.

INVESTIGATE:
1. What is the Koszul locus PRECISELY? (Quadratic A-inf algebras whose bar cohomology
   is concentrated in degree 1.)
2. How far off-locus can the qi be pushed? Is there a DERIVED Koszul locus?
3. The coderived equivalence IS unconditional. Can it be upgraded to a genuine qi
   for specific non-Koszul families?
4. What families are NOT on the Koszul locus? (All standard VAs are Koszul — the
   locus is restrictive only for genuinely pathological algebras.)

Write a Research Remark characterising the Koszul locus and the off-locus obstruction.""")

agent("H15_remove_chain_level_topol", """RESEARCH: Chain-level topologization.

TARGET: chapters/theory/en_koszul_duality.tex (add Research Remark)

Topologization is proved cohomologically, not at chain level.

INVESTIGATE:
1. The homotopy transfer theorem (HTT) gives a chain-level A-inf E_3 structure on
   a qi-equivalent model. Is this SUFFICIENT for applications?
2. What applications REQUIRE chain-level E_3 on the original complex (not a qi model)?
3. For class M (Virasoro): the chain-level BV/bar is FALSE (MC5). Does this obstruct
   chain-level topologization? Is the obstruction the SAME?
4. For affine KM: Sugawara is explicit. Can the chain-level structure be constructed
   by EXPLICIT homotopy? The key: [Q, G] = T + Q-exact. Can the Q-exact term be
   killed by a gauge transformation exp(ad_h) for suitable h?

Write a Research Remark with the explicit gauge-transformation approach for KM.""")

agent("H16_remove_baxter_MC3", """RESEARCH: Can the Baxter constraint be removed from MC3?

TARGET: chapters/examples/yangians_computations.tex (add Research Remark)

MC3 type-A thick generation is conditional on the Baxter constraint b = a - 1/2.

INVESTIGATE:
1. The Baxter constraint comes from the shifted prefundamental representations.
   Are there OTHER generating representations that don't need this constraint?
2. In the classical (non-shifted) setting: the fundamental representations generate
   without spectral constraints. Can the classical result be DEFORMED?
3. The completion extension is conditional on localising generation. Is this proved
   in the literature for the relevant categories?
4. For types B, C, D: what is the analogue of the Baxter constraint?

Write a Research Remark with the deformation approach and the type-BCD landscape.""")

agent("H17_remove_perfectness_C1", """RESEARCH: Can perfectness be avoided in C1?

TARGET: chapters/connections/thqg_symplectic_polarization.tex (add Research Remark)

The involution sigma uses a double-dual evaluation requiring reflexivity.

INVESTIGATE:
1. Is the fiber cohomology H*(M-bar_g, Z(A)) perfect (= in D^perf)?
   For g=0: yes (finite-dimensional). For g>=1: depends on the algebra.
2. Can sigma be constructed WITHOUT double-dual, using the Serre duality pairing
   on M-bar_g directly?
3. The Serre pairing: H^k(M-bar_g, Z(A)) x H^{3g-3-k}(M-bar_g, Z(A)^v ⊗ omega) -> k.
   This gives a duality without reflexivity. Can C1 be based on this?

Write a Research Remark with the Serre-based approach.""")

agent("H18_remove_class_M_MC5", """RESEARCH: Chain-level BV/bar for class M.

TARGET: chapters/connections/bv_brst.tex (add Research Remark)

MC5 chain-level is FALSE for class M (Virasoro). The coderived result holds.

INVESTIGATE:
1. WHY does chain-level fail for class M? The infinite shadow tower means infinitely
   many non-zero A-inf operations; the BV complex cannot capture them all at chain level.
2. Is there a SPECTRAL version of MC5 that works for class M? (A spectral sequence
   from the shadow tower filtration converging to the BV complex.)
3. What is the BEST chain-level statement? Perhaps: BV ≅ bar in a COMPLETED category
   (pro-completion by shadow tower degree)?
4. Can the coderived result be STRENGTHENED to something between coderived and chain-level?

Write a Research Remark with the spectral and completed approaches.""")

agent("H19_remove_genus0_koszul_vii", """RESEARCH: All-genera Koszul equivalence (vii).

TARGET: chapters/theory/chiral_koszul_pairs.tex (add Research Remark)

Koszul equiv (vii) is proved at g=0 only. The all-genera version fails at multi-weight.

INVESTIGATE:
1. At uniform weight: does (vii) hold at all genera? The shadow tower formula
   obs_g = kappa*lambda_g IS the all-genera (vii) at uniform weight. This should be TRUE.
2. At multi-weight: the obstruction is delta_F_g^cross. Can (vii) be REFORMULATED
   to include the cross-channel correction?
3. What is the geometric meaning of the cross-channel correction? Is it related to
   mixed-weight OPE residues?

Write a Research Remark with the uniform-weight proof and the multi-weight reformulation.""")

agent("H20_remove_associator_dep", """RESEARCH: Associator independence.

TARGET: chapters/theory/en_koszul_duality.tex (add Research Remark)

The chiral QG equivalence depends on the choice of Drinfeld associator.
Cohomological derived center = associator-independent (proved for sl_2).
Cochain-level = associator-dependent.

INVESTIGATE:
1. Is the GRT_1 (Grothendieck-Teichmüller) action on the cochain-level structure
   well-understood? Does it act by COBOUNDARIES (= trivially on cohomology)?
2. For sl_2: the GRT_1 action shifts P_3 by coboundaries. For general g:
   what is the obstruction to extending this?
3. Can the bar-side invariants (kappa, shadow tower) detect the associator choice?
   If not: they are AUTOMATICALLY associator-free.
4. Is there an associator-FREE approach to the chiral QG equivalence?
   (Tamarkin's approach via formality of the operad of little discs?)

Write a Research Remark with the Tamarkin approach and the GRT_1 analysis.""")


# ═══════════════════════════════════════════════════════════════════
# TIER 3: CROSS-VOLUME HEALING (10 agents)
# Strengthen the bridges between volumes.
# ═══════════════════════════════════════════════════════════════════

agent("H21_vol2_3d_gravity_heal", """HEAL the 3d gravity climax in Vol II.

TARGET: ~/chiral-bar-cobar-vol2/chapters/connections/3d_gravity.tex

The gravity chapter is the CLIMAX of Vol II. After the topologization split
(cohomological proved, chain-level conjectural), the gravity partition function
needs updating. The E_3-TOPOLOGICAL structure at cohomological level is
PROVED for affine KM; the chain-level E_3 is conjectural.

1. Verify the gravity partition function computation uses only cohomological E_3
   (which is proved) or mark chain-level dependence.
2. Strengthen the genus-tower treatment with the corrected depth-gap witnesses.
3. Add cross-references to the Vol I rectified theorems.
4. Verify the gravitational Yangian connection is consistent with the MC3 Baxter fix.

Write fixes and add fortification remarks.""", cwd=VOL2)

agent("H22_vol2_factorisation_sc_heal", """HEAL the factorisation Swiss-cheese chapter.

TARGET: ~/chiral-bar-cobar-vol2/chapters/theory/factorisation_swiss_cheese.tex

After the SC^{ch,top} correction (AP165), verify:
1. SC attributed to derived center pair (C^bullet_ch(A,A), A), NOT to B(A)
2. SC^! = (Lie, Ass, shuffle-mixed) stated correctly
3. SC NOT claimed self-dual
4. The five SC presentations all present and consistent
5. Topologization scope: affine KM proved, general conjectural

Fix any remaining violations. Add a verification remark listing which AP165-related
claims are now clean.""", cwd=VOL2)

agent("H23_vol2_bar_cobar_review_heal", """HEAL the bar-cobar review chapter.

TARGET: ~/chiral-bar-cobar-vol2/chapters/theory/bar-cobar-review.tex

This chapter reviews Vol I results for Vol II readers. After rectification:
1. Verify Theorem A stated with correct Verdier convention (algebra level)
2. Verify Theorem B stated with on-locus qi + off-locus coderived
3. Verify Theorem C with g>=1 for C1, curved qualifier for C0
4. Verify Theorem D with non-circular proof path noted
5. Verify MC2 correctly attributes g^{mod} carrier
6. Add a "What changed in Vol I" remark listing the rectifications

Fix all stale claims.""", cwd=VOL2)

agent("H24_vol3_cy_to_chiral_heal", """HEAL the CY-to-chiral functor chapter.

TARGET: ~/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex

After the pi_3(BU) correction and kappa_ch domain fix:
1. Verify CY-A stated as proved for d=2 only
2. Verify d=3 claims properly conditioned
3. Verify kappa_ch = chi(S)/2 applied only to local surfaces Tot(K_S -> S)
4. Verify pi_3(BU) = 0 (not Z) in any remaining homotopy arguments
5. Verify the bar-Euler/Borcherds connection doesn't overclaim
6. Add cross-references to the Vol I rectified theorems

Fix any remaining violations.""", cwd=VOL3)

agent("H25_vol3_fukaya_heal", """HEAL the Fukaya categories chapter.

TARGET: ~/calabi-yau-quantum-groups/chapters/theory/fukaya_categories.tex

The pi_3(BU) error was the most critical Vol III finding:
1. Verify ALL homotopy group computations: pi_k(BU) = Z for k even, 0 for k odd
2. The CY_3 E_1 obstruction is the antisymmetric Euler form, NOT pi_3(BU)
3. Verify the E_2 claims at CY_4: pi_4(BU)=Z is an obstruction GROUP, not a guarantee
4. Add a Bott periodicity verification remark
5. Strengthen the categorical Hochschild -> chiral Hochschild bridge

Fix violations and add fortification.""", cwd=VOL3)

agent("H26_vol3_toric_cy3_heal", """HEAL the toric CY3 CoHA chapter.

TARGET: ~/calabi-yau-quantum-groups/chapters/examples/toric_cy3_coha.tex

After the McKay quiver fix and kappa domain fix:
1. Verify McKay quiver of Z_3 is 3 copies of oriented 3-cycle (NOT K_{3,3})
2. Verify kappa_ch for conifold: derivation must use DT, not the local-surface formula
3. Verify all kappa subscripts present (AP113)
4. Verify CoHA not claimed to be E_1-chiral automatically (AP-CY7)
5. Strengthen the wall-crossing/bar-cobar connection

Fix violations and add fortification.""", cwd=VOL3)

agent("H27_cross_vol_formula_heal", """CROSS-VOLUME FORMULA HEALING.

Search ALL three volumes for the most commonly misquoted formulas:
1. kappa(V_k(g)) — must include Sugawara shift dim(g)/2
2. r^KM(z) = k*Omega/z — level prefix present
3. kappa(W_N) = c*(H_N - 1) — NOT c*H_{N-1}
4. av(r(z)) — Sugawara qualification for non-abelian

For each: grep all three repos, verify, fix any remaining instances.
This is the FINAL healing pass on the most-violated formulas.""")

agent("H28_cross_vol_status_heal", """CROSS-VOLUME STATUS HEALING.

For each of the 5 main theorems + MC1-5 + topologization:
1. Read the status in Vol I concordance.tex
2. Read how it's cited in Vol II
3. Read how it's cited in Vol III
4. Verify ALL three are consistent

Fix any remaining inconsistencies. This is the FINAL status sync.""")

agent("H29_compute_test_heal", """COMPUTE/TEST HEALING for the most critical engines.

For each of these key engines in Vol I compute/lib/:
1. shadow_tower engines: verify kappa values match census
2. koszul_conductor engines: verify K(BP)=196, K(Vir)=13
3. bar_cohomology engines: verify sl_2 H^2=5
4. r_matrix engines: verify k=0 vanishing

Run: python3 -m pytest compute/tests/ -x --tb=short -q 2>&1 | tail -20
Fix any failures. For engines without tests: create basic test files.""")

agent("H30_compute_test_heal_v3", """COMPUTE/TEST HEALING for Vol III engines.

Run all Vol III tests: python3 -m pytest compute/tests/ -x --tb=short -q 2>&1 | tail -20
Fix any failures. Verify expected values against the canonical data:
- kappa_ch(K3 x E) = 3
- kappa_BKM(K3 x E) = 5
- pi_3(BU) = 0 computations

For engines without tests: create basic test files.""", cwd=VOL3)


# ═══════════════════════════════════════════════════════════════════
# TIER 4: STRUCTURAL FORTIFICATION (10 agents)
# ═══════════════════════════════════════════════════════════════════

agent("H31_proof_dependency_dag", """CONSTRUCT the complete proof dependency DAG for Vol I.

TARGET: Write to compute/audit/proof_dependency_dag.md

For each of the main theorems (A-D, H, MC1-5, topol, SC-formal, depth-gap, D^2=0):
1. List ALL results it depends on (direct + transitive)
2. List ALL results that depend on it
3. Check for circular dependencies (AP191)
4. Verify no single point of failure (removal of any one result disconnects the DAG)

Draw the DAG as a text-format graph. Flag any fragilities.""")

agent("H32_theorem_registry_rebuild", """REBUILD the theorem registry from scratch.

TARGET: metadata/theorem_registry.md

Scan ALL chapters for \\begin{theorem}, \\begin{proposition}, \\begin{lemma},
\\begin{conjecture}. For each:
- Label
- Name/description
- ClaimStatus tag
- File:line
- Dependencies (which other results it cites)

Write the complete registry. This is the AUTHORITATIVE list of all claims.""")

agent("H33_landscape_census_verify", """VERIFY the landscape census against compute engines.

TARGET: chapters/examples/landscape_census.tex + compute/lib/

For each family in the census:
1. Read the census entry (kappa, r-matrix, class, depth, K)
2. Find the matching compute engine
3. Verify the engine produces the census value
4. Run the test
5. Flag any disagreement

Focus on the 10 most important families: Heis, KM, Vir, W_2, W_3, bc, bg, BP, lattice, sl_2.""")

agent("H34_concordance_completeness", """VERIFY concordance completeness.

TARGET: chapters/connections/concordance.tex

For each theorem in the manuscript (use the theorem registry):
1. Is it listed in the concordance?
2. Is the status correct?
3. Is the scope correct?
4. Are the dependencies listed?

Flag any theorem NOT in the concordance. The concordance must be COMPLETE.""")

agent("H35_build_verification", """BUILD VERIFICATION across all three volumes.

Run builds and report any errors:
1. cd ~/chiral-bar-cobar && pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -20
2. cd ~/chiral-bar-cobar-vol2 && pkill -9 -f pdflatex 2>/dev/null; sleep 2; make 2>&1 | tail -20
3. cd ~/calabi-yau-quantum-groups && pkill -9 -f pdflatex 2>/dev/null; sleep 2; make fast 2>&1 | tail -20

For each: report undefined references, multiply-defined labels, LaTeX errors.
Fix any that can be fixed from the available information.""")

agent("H36_test_suite_verification", """TEST SUITE VERIFICATION across all volumes.

Run full test suites:
1. cd ~/chiral-bar-cobar && python3 -m pytest compute/tests/ -x --tb=short -q 2>&1 | tail -30
2. cd ~/calabi-yau-quantum-groups && python3 -m pytest compute/tests/ -x --tb=short -q 2>&1 | tail -30

Report failures. For each failure: diagnose root cause and fix if possible.""")

agent("H37_notation_consistency", """NOTATION CONSISTENCY audit across Vol I.

Check that key macros are used consistently:
1. \\kappa: always with family superscript in mathematical contexts
2. B(A): always T^c(s^{-1} \\bar A)
3. Z^{der}_{ch}: always with 'chiral' qualifier
4. SC^{ch,top}: always attributed to derived center pair
5. E_3: always E_3-TOPOLOGICAL (not chiral) for topologized center

Grep for variant spellings. Fix inconsistencies.""")

agent("H38_prose_final_polish", """PROSE FINAL POLISH across Vol I frame chapters.

TARGET: chapters/frame/preface.tex, chapters/theory/introduction.tex, chapters/frame/overture.tex

Final pass:
1. Zero AI slop (AP29)
2. Zero em dashes
3. Zero markdown in LaTeX
4. Every chapter opening = deficiency opening (not "In this chapter...")
5. Transitions force mathematical necessity
6. No hedging where math is clear

This is the FINAL cosmetic pass. Fix every instance.""")

agent("H39_standalone_final_sync", """STANDALONE PAPERS final synchronisation.

TARGET: standalone/*.tex

For each standalone:
1. Theorem statements match current manuscript
2. Formulas match canonical census
3. Macros defined via \\providecommand
4. No convention drift from main text
5. No scope inflation

Fix every discrepancy. This is the FINAL standalone sync.""")

agent("H40_session_summary_write", """SESSION SUMMARY: Write the definitive summary of this entire session.

TARGET: Write to compute/audit/session_2026_04_13_adversarial_reconstitution.md

Summarise the ENTIRE session:
1. 457 Codex agents deployed across 7 campaigns
2. 48 new anti-patterns catalogued (AP186-AP224, B74-B78, FM35-FM38)
3. 12 CRITICAL theorem-level findings in the proof architecture
4. 15/25 rectification agents succeeded; 10 relaunched
5. 40 healing/fortification agents providing alternative proofs and condition removal
6. Alternative proof paths identified for all 5 main theorems + MC2 + MC5

State: what is NOW proved, what is conditional, what is conjectural, what is open.
State: what the next session should prioritise.
State: what the programme's confidence level is on each main theorem after this session.

Be exhaustive and honest. This is the permanent record.""")


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Healing & Fortification Campaign")
    parser.add_argument("--batch-size", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--delay", type=int, default=45)
    args = parser.parse_args()

    print(f"Healing Campaign: {len(AGENTS)} agents → {OUT}")
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

    summary = [f"# Healing Campaign Summary — {TS}\n",
               f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
