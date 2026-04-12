#!/usr/bin/env python3
"""
Beilinson Rectification Campaign — 25 Codex Agents
Systematic first-principles fix of all CRITICAL findings from the adversarial audit.
Each agent targets a specific file (non-overlapping) with exact findings to address.

The strongest technical choice for each finding:
1. Strengthen the proof if possible
2. Narrow the claim to match what's proved if proof cannot be strengthened
3. Add missing lemma/proof if the gap is fillable
4. Mark as conditional/conjectural with explicit scope if the gap is real

Usage:
    python3 scripts/rectification_campaign.py [--batch-size 10] [--timeout 1200]
"""

import subprocess, os, time, argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

VOL1 = "/Users/raeez/chiral-bar-cobar"
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
OUT = Path(VOL1) / f"rectification_{TS}"
OUT.mkdir(parents=True, exist_ok=True)

AGENTS = []

PREAMBLE = """\
<task>
You are a RECTIFICATION agent for a research mathematics manuscript on operadic Koszul duality.
Your mission: fix the specific findings below with the STRONGEST technical choice.
Hierarchy: (1) strengthen proof > (2) add missing lemma > (3) narrow claim to match proof > (4) mark conditional.
NEVER weaken when you can strengthen. NEVER leave a gap unfixed.
</task>

<action_safety>
Only edit the specific file(s) assigned. Do not touch other files.
Make the MINIMUM truthful edit that resolves each finding.
After each edit, re-read surrounding context to verify coherence.
</action_safety>

<verification_loop>
After all edits, re-read the modified sections and verify:
1. Each finding is resolved
2. No new inconsistencies introduced
3. Theorem status tags match the actual proof status
4. All \\ref and \\label are valid
</verification_loop>

<completeness_contract>
Address EVERY finding listed. Do not stop at the first fix.
For each finding, state: FIXED (how) or CANNOT_FIX (why, what narrower claim survives).
</completeness_contract>

<structured_output_contract>
End with:
## Rectification Summary
- [FIXED] finding — what was done
- [NARROWED] finding — claim narrowed to X
- [CONDITIONAL] finding — marked conditional on Y
- [BLOCKED] finding — cannot fix because Z
</structured_output_contract>
"""


def agent(aid, prompt, cwd=VOL1):
    AGENTS.append({"id": aid, "prompt": PREAMBLE + "\n\n" + prompt, "cwd": cwd, "model": "gpt-5.4"})


def run_agent(a, timeout=1200):
    out_file = OUT / f"{a['id']}.md"
    t0 = time.time()
    try:
        r = subprocess.run(
            ["codex", "exec", "-", "-m", a["model"], "-C", a["cwd"], "--full-auto"],
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


# ═══════════════════════════════════════════════════════════════════════════
# RECTIFICATION AGENTS (25 agents, non-overlapping files)
# ═══════════════════════════════════════════════════════════════════════════

agent("R01_chiral_koszul_pairs", """TARGET: chapters/theory/chiral_koszul_pairs.tex

FINDINGS TO FIX:

1. [CRITICAL T01] Line ~3616: Theorem A Verdier half flips between coalgebra and algebra.
   The setup defines A^!_inf as factorization ALGEBRA via D_Ran(bar B), but the theorem
   asserts bar COALGEBRA equivalences, and the proof concludes with "factorization algebra,
   not coalgebra." This violates four-functor discipline.
   FIX: Make the Verdier statement consistently about factorization ALGEBRAS (the D_Ran output).
   The bar B is a COALGEBRA; D_Ran(bar B) is an ALGEBRA. The theorem should state the
   equivalence at the algebra level after applying D_Ran. Check convention in bar_construction.tex:80-105.

2. [CRITICAL T01] Line ~584: Proof of part (2) imports Verdier compatibility as definition,
   not deriving it. The cited thm:verdier-bar-cobar identifies with factorization algebras
   in cobar_construction.tex:1347, not the coalgebra identification.
   FIX: Clarify that the Verdier identification is at the algebra (post-D_Ran) level.

3. [CRITICAL T01] Line ~416: Part (1) cites "bar-degree analogue of Lemma filtered-comparison"
   which does not exist anywhere in the repo.
   FIX: Either write this lemma or cite the correct existing result.

4. [CRITICAL T13] Line ~1998-2004: Koszul equiv (vii) is listed as unconditional but proof
   scopes it to g=0 only. All-genera version is strictly stronger.
   FIX: Move (vii) to the conditional equivalences, or add the all-genera proof.

5. [CRITICAL T13] Line ~2005-2008: Koszul equiv (viii) mis-stated. Cited Hochschild theorems
   prove duality and concentration, not free polynomial algebra. (viii)=>(v) uses unproved claim.
   FIX: Weaken (viii) to match what's actually proved, or prove the stronger statement.

6. [CRITICAL T15] Line ~2539: SC-formality converse proof uses bilinear form C(x,y,z)=kappa(x,[y,z])
   but kappa is scalar, not bilinear. Also not valid for betagamma (no metric).
   FIX: Restrict the proof to families with invariant bilinear form, or find a different proof.

7. [CRITICAL T15] Line ~2532: Forward implication only proved for Heisenberg, not full class G.
   Lattice VOA class assignment contradicts between tables.
   FIX: Resolve the class-G membership for lattice VOAs consistently and prove forward for all class G.

Read the file, verify each finding, make the strongest truthful fix for each.""")


agent("R02_higher_genus_complementarity", """TARGET: chapters/theory/higher_genus_complementarity.tex

FINDINGS TO FIX:

1. [CRITICAL T02] Line ~4123: Theorem B clause (b) — off-locus proof is circular.
   thm:higher-genus-inversion cited by coderived_models.tex:247-270 which itself cites
   thm:higher-genus-inversion. The off-locus argument uses d^2=0 spectral sequence for curved setting.
   FIX: Break the circularity. Either prove clause (b) independently or mark it conditional.
   The strongest choice: separate the off-locus argument from the on-locus, prove each independently.

2. [CRITICAL T04] Line ~455,1701: C1 genus-0 boundary case. Q_0(A)=Z(A) and Q_0(A^!)=0
   contradicts Q_g(A) ≅ Q_g(A^!)^v for all g>=0.
   FIX: Either add hypothesis g>=1, or fix the genus-0 identification. The strongest choice:
   check if Q_0 formula is correct and add the genus-0 exception if needed.

3. [CRITICAL T05] Line ~1940: C2 part (i) switches from D(bar B(A)) to Omega(A^!) mid-proof.
   These are different objects. Nondegeneracy not established.
   FIX: Use the correct object consistently. If the pairing is with bar B(A^!), use that.

4. [CRITICAL T05] Line ~1970: C2 part (iii) cites prop:lagrangian-eigenspaces about center-side
   V = H*(M-bar_g, Z(A)), but applies it to bar-side L_g = bar B^(g)(A)[1]. No lift is given.
   FIX: Either prove the lift from center-level to bar-side, or restructure to work at center level.

Read the file, verify each finding, make the strongest truthful fix.""")


agent("R03_higher_genus_foundations", """TARGET: chapters/theory/higher_genus_foundations.tex

FINDINGS TO FIX:

1. [CRITICAL T03] Line ~238: C0 uses ordinary cohomology (H^q, R^q pi_*, spectral sequence, EGA base change)
   on the fiber bar object with curved differential d_fib where d_fib^2 = kappa*omega_g.
   This is not well-typed: ordinary cohomology requires d^2=0.
   FIX STRATEGY: The strongest choice is to:
   (a) Use the FLAT piece d_g (the genus-g convolution differential) which IS d^2=0, OR
   (b) Add an explicit flat-side comparison lemma that relates the curved object to a flat resolution, OR
   (c) Restrict to kappa=0 (uncurved) case and mark the curved case as conditional.
   Read the file to determine which is mathematically correct.

2. [CRITICAL T03] Line ~411 (also in higher_genus_complementarity.tex): Step 3 jumps from
   "surviving bar cohomology/Koszul dual" to "center local system" without justification.
   cor:bar-cohomology-koszul-dual computes genus-0 data under PBW, but does not identify
   with the center local system Z_A.
   FIX: Either prove this identification or separate bar-cohomology from center.

3. [CRITICAL T06] Line ~5326: thm:family-index invoked by Theorem D proof, but thm:family-index
   itself starts from thm:genus-universality in concordance.tex:6010, creating a circular dependency.
   FIX: Break the circle. Identify the primitive non-circular anchor. The strongest choice:
   prove thm:family-index independently of thm:genus-universality, using only the genus-1 base case
   and the inductive structure of the shadow tower.

Read the file, verify each finding, make the strongest truthful fix.""")


agent("R04_higher_genus_modular_koszul", """TARGET: chapters/theory/higher_genus_modular_koszul.tex

This is the largest theory file. Multiple CRITICAL findings.

FINDINGS TO FIX:

1. [CRITICAL T06] Line ~2695: Theorem D circular dependency with thm:family-index.
   FIX: Add a routing remark (AP147) identifying the non-circular anchor.
   The proof chain should be: shadow tower construction (independent) → genus universality
   (from shadow tower) → family index identification (from universality). Make this explicit.

2. [CRITICAL T08] Lines ~994,1011: MC1 PBW — d_1^PBW maps enrichment classes to genus-0 sector
   without controlling mixed maps. Whitehead invoked for semisimple g but applied to truncated
   current algebra.
   FIX: Add the missing comparison between truncated current algebra and g. Whitehead applies
   to the finite-dimensional Lie algebra g acting on the weight graded pieces; make this precise.

3. [CRITICAL T09] Line ~3475: MC2 proved on g^mod only, not g^{E1}.
   Introduction.tex:368 wrongly attributes the E1 statement to thm:mc2-bar-intrinsic.
   FIX: Clarify that MC2 as stated here is on g^mod. The E1 version is in e1_modular_koszul.tex.
   Fix the introduction cross-reference.

4. [CRITICAL T09] Line ~3627: Theta_A placed in product of genuswise cyclic coderivations,
   then treated as element of Defcyc(A) ⊗ Gmod without identification.
   FIX: Add the explicit identification or restructure the proof to work in the genuswise product.

5. [CRITICAL T16] Line ~17115: Depth gap prop over-scoped. The kappa!=0 hypothesis excludes
   the d_alg=2 case (betagamma with kappa|_L=0).
   FIX: Split into kappa!=0 case ({0,1,inf}) and the kappa=0 boundary ({2}). Or remove the kappa!=0 hypothesis.

6. [CRITICAL T16] Line ~16414: Class-C witness contradicted. betagamma shadow tower vanishes
   on the weight-changing line. The claimed r_max=4 conflicts with proved mu_bg=0.
   FIX: Check which line/family actually realizes d_alg=2. If betagamma on the standard line,
   verify the shadow tower is nonzero there. Update the witness.

7. [CRITICAL T18] Lines ~30863,30882: D^2=0 proof uses wrong space. Log FM for fixed (X,D)
   has FM collisions and puncture collisions, not curve degenerations.
   FIX: The D^2=0 should work on the universal family over M-bar_{g,n}, not on log FM for fixed curve.
   Rewrite the space to be the correct one.

Read the file carefully (it's very large), verify each finding, fix in dependency order.""")


agent("R05_bar_cobar_adjunction_curved", """TARGET: chapters/theory/bar_cobar_adjunction_curved.tex

FINDINGS TO FIX:

1. [CRITICAL T11] Lines ~1116-1153: prop:standard-strong-filtration has wrong inequality.
   wt(J^a_{(n)}J^b) = h_a+h_b-n-1, but concludes wt(a*b) >= wt(a)+wt(b).
   For affine currents J^a_{(0)}J^b = [J^a,J^b] has weight 1, not in F^2.
   Also: bounded-below direct sum != inverse limit (product) unless weight-completed.
   FIX: Fix the inequality. The correct statement should use a DECREASING filtration
   by pole order, not an increasing filtration by conformal weight. Or restrict to
   weight-completed algebras. Make the strongest true statement.

2. The proof shifts from required mu_r on A to bar differential on bar B(A).
   FIX: Make the relationship between the filtration on A and on bar B explicit.

Read lines 1100-1200 carefully, verify the finding, make the fix.""")


agent("R06_nilpotent_completion", """TARGET: chapters/theory/nilpotent_completion.tex

FINDINGS TO FIX:

1. [CRITICAL T11] Lines ~1012-1168: MC4^0 / finite-resonance lane not proved.
   Step 2 studies transferred operations on H=H*(A,m_1), but Steps 3-4 conclude about
   original algebra A without comparison theorem. The filtration verification at 1121-1163
   actually proves the mixed differential DECREASES positive weight, then silently switches
   to a decreasing filtration. This is not a verification of the stated theorem.
   FIX: Either add the comparison theorem (H to A), or restructure to work on H throughout,
   or honestly mark the finite-resonance reduction as conditional. The strongest choice:
   add the comparison via homological transfer theorem.

Read the file, verify the finding, make the strongest truthful fix.""")


agent("R07_yangians_computations", """TARGET: chapters/examples/yangians_computations.tex

FINDINGS TO FIX:

1. [CRITICAL T10] Line ~3071: Step 2 of thm:shifted-prefundamental-generation claims lambda=0
   makes Baxter spectral constraint vacuous. But prop:baxter-yangian-equivariance at 2924-2941
   requires b=a-(lambda+1)/2, so at lambda=0: b=a-1/2 (NOT vacuous).
   Same false claim at 3222-3224.
   FIX: Correct the lambda=0 specialization. State the correct constraint b=a-1/2 and
   verify the short exact sequence holds under this constraint. If it does: fix the text.
   If it doesn't: the proof strategy needs revision.

2. [CRITICAL T10] Line ~3125: Step 4 jumps from finite-dimensional strata to compact objects
   of completed shifted category. But the file itself marks this extension as conjectural (2633-2649).
   FIX: Either prove the extension or mark the conclusion as conditional on the completion step.

Read the file, verify both findings, make fixes.""")


agent("R08_bv_brst", """TARGET: chapters/connections/bv_brst.tex

FINDINGS TO FIX:

1. [CRITICAL T12] Line ~1932: Core class-M mechanism delta_r^harm = c_r(A)*m_0^{floor(r/2)-1}
   is introduced without proof or citation. This is the main engine of thm:bv-bar-coderived.
   FIX: Either prove this factorization (derive from the harmonic projection properties)
   or cite the source. If genuinely unproved: mark the coderived result as conditional on this mechanism.

2. [CRITICAL T12] Line ~1945: Proof treats m_0*x = d^2(x) in Im(d) as sufficient to kill
   the obstruction in D^co. But coderived category is Verdier quotient by coacyclic objects,
   not "boundaries mod Im(d)." The manuscript itself says curved objects are NOT zero in D^co.
   FIX: This is a genuine logical failure. Either reprove using the correct coderived
   characterization (coacyclic = totalizations of short exact sequences), or honestly
   downgrade the coderived result.

Read the file, verify both findings, make the strongest truthful fix.""")


agent("R09_en_koszul_duality", """TARGET: chapters/theory/en_koszul_duality.tex

FINDINGS TO FIX:

1. [CRITICAL T14] Line ~2947: Topologization theorem stated as chain-level E_3, but proof
   only establishes [Q,G] = T_Sug + Q-exact on Q-cohomology (lines 3307-3311).
   The file itself concedes the chain-level gap at 3146-3176.
   FIX: The strongest truthful choice:
   (a) Restate the theorem as a Q-COHOMOLOGY level result (E_3 on H*(Z^der, Q)), OR
   (b) If a chain-level proof exists elsewhere, cite it, OR
   (c) Split into: "cohomological E_3" (ProvedHere) + "chain-level E_3" (Conjectured).
   Option (c) is probably the strongest honest choice. Update ClaimStatus accordingly.

Read lines 2900-3200 carefully, verify the finding, make the fix.
Also check if the chain-level concession at 3146-3176 is consistent with the final claim.""")


agent("R10_chiral_hochschild_koszul", """TARGET: chapters/theory/chiral_hochschild_koszul.tex

FINDINGS TO FIX:

1. [CRITICAL T07] Line ~618: Proof of thm:main-koszul-hoch conflates bar coalgebra bar B^ch(A)^v
   with Koszul dual algebra A^!. Then replaces Omega^ch(bar B^ch(A)) by Omega^ch(A^!).
   This makes the Hom computation invalid.
   FIX: The bar coalgebra and Koszul dual are distinct objects (AP25). Fix the identification
   chain: bar B → (bar B)^v = (A^i)^v would need Verdier, not linear dual. Make the correct
   identification explicit or restructure the proof.

2. [CRITICAL T07] Line ~740: Proof of thm:hochschild-polynomial-growth treats ChirHoch^n(A)
   as D_X-module morphisms on base curve, but the bigraded definition places cochains on
   varying configuration spaces FM_{p+2}(X) of dimension p+2. The collapse to curve-level
   Ext is not justified.
   FIX: Either prove the collapse (via a spectral sequence or filtration argument that
   reduces configuration spaces to the base curve), or acknowledge the gap.

3. [CRITICAL T20] Line ~4841: thm:gerstenhaber-structure tagged ProvedHere but has no proof.
   Construction only gives a single insertion-residue sum (not a Gerstenhaber bracket).
   FIX: Either write the proof (define the bracket properly with both insertions), or
   downgrade to Conjectured.

Read the file, verify all three findings, fix in order.""")


agent("R11_thqg_symplectic_polarization", """TARGET: chapters/connections/thqg_symplectic_polarization.tex

FINDINGS TO FIX:

1. [CRITICAL T04] Lines ~476,694: Q_g(A) ≅ Q_g(A^!)^v claimed for all g>=0, but
   Q_0(A)=Z(A) and Q_0(A^!)=0 proven in the same file. Contradiction at g=0.
   FIX: Add hypothesis g>=1, or fix the genus-0 identifications. Check if Q_0 should
   actually be nonzero for both A and A^!.

2. [CRITICAL T04] Lines ~197,220: The involution sigma uses ev: C_g(A)^{vv} -> C_g(A)
   without reflexivity hypothesis. The vv construction imports finite-dimensional fiber-cohomology.
   FIX: Add the reflexivity/perfectness hypothesis explicitly, or use a different construction.

Read the file, verify both findings, fix.""")


agent("R12_thqg_open_closed", """TARGET: chapters/connections/thqg_open_closed_realization.tex

FINDINGS TO FIX:

1. [CRITICAL T20] Line ~199: Proof of thm:thqg-brace-dg-algebra derives delta^2(f)=1/2[[m,m],f]
   from graded Jacobi with m at odd degree. But the manuscript later says this shortcut is
   invalid when ||m||=0 (AP138: degenerate at even degree).
   FIX: Check the actual suspended degree of m in this context. If ||m||=0 (even),
   use the brace expansion m{m}=0 instead of Jacobi. Fix the proof accordingly.

Read the file, verify the finding, fix.""")


agent("R13_introduction", """TARGET: chapters/theory/introduction.tex

FINDINGS TO FIX:

1. [CRITICAL T09] Line ~368: Incorrectly attributes the E1 ordered MC2 statement to
   thm:mc2-bar-intrinsic, which only proves the g^mod (symmetric/modular) version.
   The E1 version is in e1_modular_koszul.tex:290.
   FIX: Correct the cross-reference. Either cite the E1 theorem separately, or qualify
   that the introduction states the stronger E1 version which is proved in e1_modular_koszul.tex.

2. Lines ~2091-2092: Advertises MC4 application to V_k(g), Vir_c, W-algebras, lattices.
   But prop:standard-strong-filtration has the wrong inequality (T11 finding).
   FIX: Add qualification that the strong filtration requires weight-completion hypothesis.

Read the file, find these specific references, fix them.""")


agent("R14_concordance", """TARGET: chapters/connections/concordance.tex

This is the CONSTITUTION. All status changes from other fixes must be reflected here.

FINDINGS TO FIX:

1. [CRITICAL T06] Line ~6010: thm:family-index cites thm:genus-universality,
   creating circular dependency with Theorem D.
   FIX: Add a ROUTING REMARK (AP147) that breaks the circle by identifying the
   non-circular proof path. The anchor should be: shadow tower construction → universality → family index.

2. After ALL other agents complete, this file needs to be updated to reflect:
   - Any theorem status downgrades (ProvedHere → Conditional)
   - Any scope narrowings (all genera → g>=1, chain-level → cohomological)
   - Any missing-lemma additions

For now: fix the circular dependency routing. Leave a TODO for the status sync pass.

Read the file, find line 6010, add the routing remark.""")


agent("R15_toroidal_elliptic_v1", """TARGET: chapters/examples/toroidal_elliptic.tex (Vol I)

FINDINGS TO FIX:

1. [CRITICAL F08] Line ~2085: K3 CDR remark reverses bc/bg signs.
   States c_betagamma = -2 and c_bc = +2 per complex dimension.
   CANONICAL: c_bc(lambda=1) = 1-3(2*1-1)^2 = 1-3 = -2. c_bg(lambda=1) = 2(6-6+1) = +2.
   So c_bc = -2, c_bg = +2. The file has them SWAPPED.
   FIX: Swap the signs. c_bc = -2, c_betagamma = +2.

Read line ~2085, verify the finding, make the fix.""")


agent("R16_toroidal_elliptic_v3", """TARGET: chapters/examples/toroidal_elliptic.tex (Vol III at ~/calabi-yau-quantum-groups)

FINDINGS TO FIX:

1. [CRITICAL F08] Line ~2177: Same K3 CDR sign reversal as Vol I.
   c_betagamma = -2, c_bc = +2 stated. Should be c_bc = -2, c_bg = +2.
   FIX: Swap the signs.

Read line ~2177, verify the finding, make the fix.""",
cwd="/Users/raeez/calabi-yau-quantum-groups")


agent("R17_free_fields", """TARGET: chapters/examples/free_fields.tex

FINDINGS TO FIX:

1. [CRITICAL T16] Line ~1148-1166: A proved proposition says the entire betagamma shadow tower
   vanishes on some line. This contradicts the depth-gap theorem's claim that betagamma has
   d_alg=2 (realized r_max=4).
   FIX: Read the proposition carefully. Determine WHICH line the shadow tower vanishes on
   vs which line d_alg=2 is claimed on. They may be different lines (weight-changing vs standard).
   If they're the same line: the depth gap witness is wrong and needs replacement.
   If they're different: add clarification about which line realizes d_alg=2.

Also check line ~1171 for the betagamma global-depth theorem contradiction with T-line.

Read the file, verify, resolve the contradiction.""")


agent("R18_cobar_construction", """TARGET: chapters/theory/cobar_construction.tex

FINDINGS TO FIX:

1. [HIGH T01] Lines ~1347-1348: thm:verdier-bar-cobar identifies Omega^ch(A^!) ≅ D(bar B^ch(A))
   as factorization algebras. But Theorem A proof in chiral_koszul_pairs.tex uses this at
   the coalgebra level. Verify the convention is consistent: are we working with algebras
   (post-D_Ran) or coalgebras (pre-D_Ran)?
   FIX: Ensure the statement here is consistent with what Theorem A actually uses.

2. Lines ~2207-2219: Downstream propagation of Theorem A's wrong bar-target formula.
   FIX: After R01 fixes chiral_koszul_pairs.tex, verify this section is consistent.

Read the file, check conventions, fix if needed.""")


agent("R19_coderived_models", """TARGET: chapters/theory/coderived_models.tex

FINDINGS TO FIX:

1. [CRITICAL T12] Lines ~75, ~545: The coderived category is defined as Verdier quotient
   by coacyclic objects. But bv_brst.tex:1945 treats it as "boundaries mod Im(d)".
   FIX: Verify the definition here is correct and consistent. If it is, the bv_brst proof
   is using the wrong characterization.

2. [CRITICAL T02] Lines ~247-270: prop:coderived-adequacy(a) invokes thm:higher-genus-inversion,
   creating circular dependency.
   FIX: Break the circularity. Prove coderived-adequacy independently, or mark it conditional.

Read the file, verify both findings, fix.""")


agent("R20_configuration_spaces", """TARGET: chapters/theory/configuration_spaces.tex

FINDINGS TO FIX:

1. [CRITICAL T18] Lines ~1251, ~1278: Log FM definition for fixed pair (X,D) has FM collisions
   and puncture collisions only, NOT curve degenerations. But the D^2=0 proof in
   higher_genus_modular_koszul.tex:30863 claims curve-degeneration strata.
   FIX: Verify what strata the log FM space actually has. If no curve degenerations:
   the D^2=0 proof needs to use the universal family over M-bar_{g,n}, not fixed-curve log FM.
   Add clarification about which space has which strata.

Read the file, verify the finding.""")


agent("R21_standalone_e1_primacy", """TARGET: standalone/N3_e1_primacy.tex

FINDINGS TO FIX:

1. [CRITICAL F14] Line ~457: Theorem "Degree-2 averaging: av(r(z))=kappa" is false for
   affine KM. For non-abelian KM: av(r(z)) + dim(g)/2 = kappa (Sugawara shift, C13/FM11).
   FIX: Add the Sugawara shift qualification. State: av(r(z)) = kappa for abelian (Heisenberg).
   For non-abelian KM: av(r(z)) = kappa_dp = k*dim(g)/(2h^v), and full kappa includes
   Sugawara shift dim(g)/2.

Read the file, find the theorem, make the fix.""")


agent("R22_bar_construction", """TARGET: chapters/theory/bar_construction.tex

FINDINGS TO FIX:

1. [MEDIUM T01] Lines ~80-105: Convention that unqualified bar B means symmetric B^Sigma.
   This convention is load-bearing for Theorem A (which only works on symmetric bar).
   FIX: Verify this convention is clearly stated and consistent. Add a remark that
   Theorem A's Verdier statement requires the symmetric bar on unordered Ran(X),
   and that bar B^ord on the ordered surface does not support D_Ran.

Read the file, verify the convention, strengthen the clarity.""")


agent("R23_e1_modular_koszul", """TARGET: chapters/theory/e1_modular_koszul.tex

FINDINGS TO FIX:

1. [HIGH T09] Line ~290: This file has the E1 ordered MC2 theorem. Verify it is correctly
   stated on the ordered/E1 carrier g^{E1}, not g^{mod}.
   FIX: Verify the theorem statement and proof are on g^{E1}. If correct, ensure
   introduction.tex cites THIS theorem (not thm:mc2-bar-intrinsic) for the E1 claim.

Read the file, verify.""")


agent("R24_chiral_center_theorem", """TARGET: chapters/theory/chiral_center_theorem.tex

FINDINGS TO FIX:

1. [HIGH T20] Lines ~969-985: This file says the graded Jacobi shortcut is invalid at ||m||=0.
   Verify this warning is correctly stated and that it's consistent with how the Gerstenhaber
   bracket is defined elsewhere.
   FIX: If the warning is correct, ensure thqg_open_closed_realization.tex:199 doesn't
   use the shortcut at even degree.

Read the file, verify the warning, check consistency.""")


agent("R25_bar_cobar_adjunction_inversion", """TARGET: chapters/theory/bar_cobar_adjunction_inversion.tex

FINDINGS TO FIX:

1. [CRITICAL T02] Lines ~2789-2808, 3015-3041: Related to Theorem B off-locus argument.
   The strict spectral sequence at 2024-2077 is formulated for d^2=0 complexes.
   Used in the off-locus curved setting where d^2=kappa*omega_g.
   FIX: Either extend the spectral sequence to the curved/coderived setting, or restrict
   the off-locus claim to the coderived category (where the comparison IS proved).

Read the file, verify the finding, make the strongest truthful fix.""")


# ═══════════════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Beilinson Rectification Campaign")
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Concurrent agents per batch (lower than audit for write safety)")
    parser.add_argument("--timeout", type=int, default=1200,
                        help="Timeout per agent (longer for write work)")
    args = parser.parse_args()

    print(f"Rectification: {len(AGENTS)} agents → {OUT}")
    print(f"Batch size: {args.batch_size}, Timeout: {args.timeout}s")
    print()

    ok, fail = 0, 0
    results = []
    for i in range(0, len(AGENTS), args.batch_size):
        batch = AGENTS[i:i + args.batch_size]
        batch_num = i // args.batch_size + 1
        total_batches = (len(AGENTS) + args.batch_size - 1) // args.batch_size
        print(f"=== Batch {batch_num}/{total_batches} ({len(batch)} agents) ===")
        with ThreadPoolExecutor(max_workers=args.batch_size) as ex:
            futs = {ex.submit(run_agent, a, args.timeout): a for a in batch}
            for f in as_completed(futs):
                aid, success, dt = f.result()
                ok += success; fail += (not success)
                results.append({"id": aid, "ok": success, "time": dt})
                print(f"  [{ok+fail}/{len(AGENTS)}] {'OK' if success else 'FAIL'} {aid} ({dt:.0f}s)")

    summary = [f"# Rectification Summary — {TS}\n", f"Total: {len(AGENTS)} | OK: {ok} | Failed: {fail}\n"]
    for r in sorted(results, key=lambda x: x["id"]):
        summary.append(f"- [{'OK' if r['ok'] else 'FAIL'}] {r['id']} ({r['time']:.0f}s)")
    (OUT / "SUMMARY.md").write_text("\n".join(summary))
    print(f"\nDONE. OK={ok} Failed={fail}\nResults: {OUT}")


if __name__ == "__main__":
    main()
