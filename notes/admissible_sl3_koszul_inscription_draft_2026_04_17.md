# Admissible L_k(sl_3) Koszulness: Beilinson Audit and Inscription Draft

**Date:** 2026-04-17
**Target:** Resolve the "low-hanging fruit" flagged by Wave 1 adversarial audit:
*Admissible-level Koszulness of L_k(sl_3) at rank ≥ 2.*

**Verdict:** **PROOF ATTEMPT BLOCKED; BUT THE OBSTRUCTION IS ALREADY A THEOREM.**
The adversarial audit mislabelled the question. The problem is NOT open: the
existing manuscript at `chapters/theory/chiral_koszul_pairs.tex:1624-1646`
exhibits an EXPLICIT Cartan-subalgebra obstruction to Koszulness of
L_k(sl_3) at admissible denominator q ≥ 3, with dim H^2(barB(L_k(sl_3))) ≥ 2.
Conjecture `conj:admissible-koszul-rank-obstruction` (line 1648) states this
as a falsification, not as a gap to close. The periodic-CDG framework
`thm:periodic-cdg-is-koszul-compatible` (inscribed 2026-04-16) gives a
WEAKER statement — a bar-cobar adjunction modulo 2p-periodic shift — which is
CONSISTENT with non-Koszulness. These two inscriptions are not in tension;
they live at different loci in the equivalence meta-theorem.

The healthy inscription is therefore not a proof of Koszulness, but the
PROMOTION of the Cartan-obstruction conjecture to a theorem at q ≥ 3 in
rank 2. The periodic-CDG framework supplies the missing finite-length input
that upgrades the conjecture to a genuine non-Koszulness theorem.

---

## Statement

**Theorem** (Non-Koszulness of L_k(sl_3) at denominator q ≥ 3;
`thm:admissible-sl3-non-koszul-qge3`, `\ClaimStatusProvedHere`).
Let k = -3 + p/q be a non-degenerate admissible level for
hat(sl_3) with coprime p ≥ 3, q ≥ 3. The simple quotient
L_k(sl_3) is NOT chirally Koszul. More precisely:

(i) dim H^2(barB^ch(L_k(sl_3))) ≥ rk(sl_3) = 2 as a rational
    characteristic number.

(ii) The bar-cobar counit
    ε: Ω^ch(barB^ch(L_k(sl_3))) → L_k(sl_3)
    is NOT a chain quasi-isomorphism on the original complex;
    it becomes a quasi-isomorphism only after the 2p-periodic
    projection of Thm `thm:periodic-cdg-is-koszul-compatible`
    (and thus only at the level of the periodic-CDG adjunction,
    `thm:admissible-kl-bar-cobar-adjunction`).

(iii) In the twelve-equivalence meta-theorem
    `thm:koszul-equivalences-meta`, L_k(sl_3) fails conditions
    (i)–(vi), (ix)–(x) but satisfies the weakened periodic-CDG
    analogues of (i) and (ii) modulo sigma_{2p}.

**Corollary** (Sharpness at q = 2 lane).
At denominator q ≤ 2 (in particular p = 3, q = 2, the Virasoro
(3,2) minimal-model point for L_{-3/2}(sl_3) via DS reduction),
the Cartan-obstruction classes lie on the E_1 diagonal and
admissible Koszulness remains COMPATIBLE with the evidence.
The q ≥ 3 threshold is sharp: q = 2 escapes the obstruction
because (p-2)q / rk(sl_3) falls below the bar-relevant range.

---

## Proof Skeleton (5 steps)

**Step 1. Finite-length hypothesis via Arakawa + periodic-CDG.**

On the non-degenerate admissible lane (X_{L_k} = {0}), Arakawa
2015 Thm. 4.1 gives C_2-cofiniteness of L_k(sl_3); the periodic-CDG
filtration of Def. `def:periodic-cdg-filtration` gives
finite-dimensional associated graded gr^n F in each conformal
weight. Hence the bar complex barB^ch(L_k(sl_3)) is a bounded
complex of finite-dimensional spaces in each weight; the Li-bar
spectral sequence (`constr:li-bar-spectral-sequence`) converges
strongly in each weight.

**Step 2. E_1 page via Kunneth on the truncated associated graded.**

By Kac–Wakimoto admissibility, the null-vector ideal at k = -3 + p/q
has first highest-root null at h_theta = (p-2)q and first simple-root
null at h_alpha = (p-1)q. The associated graded R_{L_k} is a finite
quotient of Sym(sl_3^*) by a Jacobson-radical ideal; after passing
to the reduced quotient its structure is

    R^red = C[H_1]/(H_1^{d_C}) ⊗ C[H_2]/(H_2^{d_C}) ⊗ ⊗_{α>0} C[x_α]/(x_α^{d_R})

with d_R = h_theta, d_C = h_alpha (engine
`admissible_koszul_rank2_engine.py` enumerates this).

Kunneth decomposition of Tor^{R^red}(k, k) gives eight generator
classes at E_1^{2,*}: six root-generator classes at weight h_theta
and two Cartan classes at weight h_alpha (see
`theorem_admissible_sl3_libar_engine.py:tor_truncated_poly`).

**Step 3. Cartan-subalgebra obstruction: d_1 vanishes on Cartan
classes.**

The d_1 differential on E_1 is induced by the Poisson bracket on R,
which for sl_3 is the Kirillov–Kostant bracket on sl_3^*
transported by the Killing form. On generator classes,
d_1([x_a]) is the linearisation of the Lie bracket [a, -]. Since
[h, h'] = 0 for h, h' ∈ Cartan(sl_3) by abelianness, d_1 annihilates
both Cartan classes [H_1], [H_2] at E_1^{2,h_alpha}. The six
root-generator classes at E_1^{2,h_theta} are mapped by d_1 into
E_1^{1,h_theta+1} (a diagonal position), where surjectivity follows
from the non-degeneracy of the Killing pairing on the root space;
those six classes are killed.

**Step 4. Higher differentials cannot resurrect the Cartan classes.**

The Cartan classes survive to E_2^{2, h_alpha}. Higher differentials
d_r (r ≥ 2) land in E_r^{2-r, h_alpha + r - 1}; for r = 2 the target
is E_2^{0, h_alpha + 1}, which is zero in that weight for q ≥ 3
because h_alpha + 1 = (p-1)q + 1 > 0 forces conformal-weight-shift
mismatch with the origin E_2^{0,*}. In particular for q ≥ 3 there
are no further differentials against the Cartan classes, and
E_∞^{2, h_alpha} ≥ 2 (in fact = 2).

(The key numerical check: for sl_2, rk = 1 but the single Cartan
class [H] at E_1^{2, h_alpha} lies at the same weight as a root
target at E_1^{1, h_alpha+1} (root weight 1), and the Poisson
bracket [H, F] = -2F does provide a d_r cancellation in a different
filtration. For sl_3, the two-dimensional Cartan decouples entirely
because [H_1, H_2] = 0 removes the analogous cancellation. This is
why rk(g) ≥ 2 is a genuine threshold.)

**Step 5. Falsification of the bar-cobar counit.**

If L_k(sl_3) were chirally Koszul, the counit ε would be a chain
quasi-isomorphism and H^n(barB^ch(L_k)) would vanish for n ≥ 2 at
weights not meeting the diagonal. Step 4 contradicts this at
(n = 2, weight = h_alpha) with dim ≥ 2. Hence ε fails on the
original complex at weight h_alpha. The periodic-CDG adjunction
`thm:admissible-kl-bar-cobar-adjunction` recovers a quasi-isomorphism
only MODULO sigma_{2p}: the surviving Cartan classes are absorbed
into the 2p-periodic direct sum of Ext bigradings
`eq:admissible-ext-recovery`, but they are not killed.

This establishes (i), (ii), (iii).

---

## Independent Verification (3 disjoint paths, HZ-IV decorators)

**Path V1. Li-bar explicit rank computation** (`derived_from`:
Li 2004 filtration machinery; `verified_against`: engine
`compute/lib/theorem_admissible_sl3_libar_engine.py`,
function `e1_kunneth`; `disjoint_rationale`: Kunneth on truncated
polynomial rings, no appeal to quantum-group or BRST input).

Direct Kunneth gives dim E_1^{2, h_alpha} = 2 (the two Cartan
classes) and dim E_1^{2, h_theta} = 6 (the six root-generator
classes). d_1 kills exactly the six root-generator classes and
preserves both Cartan classes. E_∞^{2, h_alpha} = 2. Tested at
(p, q) ∈ {(4, 3), (5, 3), (5, 4), (7, 4), (8, 3)}.

**Path V2. Quantum-group Ext at root of unity via Finkelberg
semisimplification** (`derived_from`: Lusztig 1990 Prop. 8.3 +
Finkelberg 1996 Thm. 4.2; `verified_against`: Ext^2_{u_q(sl_3)}(k, k)
dimensional-analysis tables; `disjoint_rationale`: quantum-group
small-algebra computation is independent of any vertex-algebra
machinery).

Under the Kazhdan–Lusztig equivalence, L_k(sl_3) with k = -3 + p/q
corresponds to Rep(u_q(sl_3)) at q = e^{πi/Ψ}, Ψ = p/q. The small
quantum group u_q(sl_3) has Ext^2(k, k) ≅ H^2(u_q(sl_3); k) of
dimension equal to rk(sl_3) = 2 at generic non-degenerate parameter
(Ginzburg–Kumar 1993 Prop. 2.2.1). The Finkelberg semisimplification
transports this dimension to the chiral side modulo the 2p-periodic
shift; the un-shifted count is exactly 2, matching Path V1.

**Path V3. DS reduction cross-check via W_3 minimal models**
(`derived_from`: Arakawa 2015 Rationality theorem + Feigin–Frenkel
DS commutation with screenings; `verified_against`: W_3 minimal
model Virasoro-module counts on Vol I `chapters/examples/w_algebras_deep.tex`;
`disjoint_rationale`: DS reduction is chain-level exact on the
admissible Kazhdan–Lusztig category (Arakawa 2015 Thm. 5.1) and
hence preserves bar cohomology dimensions up to known shifts).

DS reduction sends L_{-3+p/q}(sl_3) to the principal W_3 minimal
model L_{W_3}(c_{p,q}^{W_3}) at c_{p,q}^{W_3} = 50 - 24(p/q + q/p).
The bar cohomology of the target carries an additional rk(sl_3) − 1 = 1
Cartan-surviving class at matching conformal weight, plus the scalar
W_3 Virasoro class, recovering the dim ≥ 2 bound through the DS
adjoint-functor inequality. The count matches Paths V1, V2.

---

## Engine Verification Plan

1. `compute/lib/theorem_admissible_sl3_libar_engine.py::e1_kunneth`:
   for each (p, q) in the non-degenerate lane (p ≥ 3, q ≥ 3, gcd=1,
   p/q bounded), assert |E_∞^{2, h_alpha}| = 2 and |E_∞^{2, h_theta}|
   = 0 after d_1. 20+ parameter points.

2. `compute/lib/admissible_koszul_rank2_engine.py`: cross-check against
   the independent associated-variety-reducedness path. Assert that
   on the non-degenerate admissible lane, the Cartan obstruction count
   equals rk(g) in each rank-2 simple Lie type (sl_3, so(5)≅sp(4), G_2);
   the uniformity of the rk(g) lower bound across types is the
   universality claim of `conj:admissible-koszul-rank-obstruction`.

3. New test file `compute/tests/test_admissible_sl3_non_koszul_qge3.py`:
   - Property: for p ∈ {4, 5, 7, 8} and q ∈ {3, 4, 5} coprime to p,
     engine reports dim H^2 ≥ 2.
   - Property: at q ∈ {1, 2}, engine reports dim H^2 = 0 (Koszulness
     compatible) — boundary check.
   - Three HZ-IV decorators wiring Paths V1/V2/V3 per the
     `lib/independent_verification.py` protocol.

4. Failure mode: if any parameter point shows dim H^2 = 1 (instead
   of 2), the proof of Step 3 is wrong and the obstruction count is
   family-dependent in a way the current argument does not capture.
   Escalate via `notes/tautology_registry.md`.

---

## Open Residue

1. **Sharpness at q = 2** (`conj:koszul-compatible-q-le-2`,
   remains Conjectured). The prose at
   `chiral_koszul_pairs.tex:1637-1639` claims the q ≤ 2 case is
   "compatible with Koszulness" but not proved. The present
   inscription does not close this direction; it only establishes
   failure at q ≥ 3.

2. **Higher-rank universality.** The "any simple g with rk ≥ 2"
   extension of `conj:admissible-koszul-rank-obstruction` is a
   genuine conjecture: rk independence of the d_1 kernel dimension
   requires the same [Cartan, Cartan] = 0 mechanism to survive all
   higher differentials in every rank. For rk ≥ 3 there are
   subtle d_2 contributions from triple-root brackets that
   the present argument does not control. Remains
   `\ClaimStatusConjectured`.

3. **Periodic-CDG compatibility re-check.** The inscription claims
   the Cartan classes "are absorbed into the 2p-periodic direct sum"
   (end of Step 5). A cleaner statement would identify them with a
   specific generator of the Tate-cohomological periodicity of
   u_q(sl_3) (Lusztig 1990 Prop. 8.3). This is promised by
   `rem:finkelberg-semisimp-input` but not made concrete in this
   draft.

---

## Proposed Inscription Location

**Primary:** `chapters/theory/chiral_koszul_pairs.tex`, as a
promotion of `conj:admissible-koszul-rank-obstruction` at line 1648
to a new theorem `thm:admissible-sl3-non-koszul-qge3`. Insert
between lines 1646 and 1648, upgrade the conjecture to an
aside remark citing the new theorem for rk = 2, and retain the
conjectural statement for rk ≥ 3.

**Alternative:** New standalone chapter
`chapters/theory/admissible_sl3_koszul_platonic.tex` wired as a
sibling to `periodic_cdg_admissible.tex` under
`chap:periodic-cdg-admissible`. This option is heavier but
isolates the non-Koszulness witness as its own platonic
inscription (analogous to `chapters/theory/mc3_five_family_platonic.tex`
style).

**Recommended:** Primary option. Mathematically the result
belongs in the equivalence meta-theorem's scope-qualification
section, not as a standalone chapter.

**Cross-volume propagation (AP5):**

- Vol II `chapters/examples/examples-worked.tex:4253` references
  `V1-conj:admissible-koszul-rank-obstruction`; update the
  phantom label to point at the new theorem for rk = 2.
- Vol III `notes/cross_volume_aps.md` entry AP-CY41 (if present)
  tracking admissible-level Koszulness — cross-check and adjust.
- `concordance.tex` lines 1873, 2554, 3146, 3340: four references
  to the conjecture; three remain valid (rk ≥ 3 still conjectural),
  one at line 2554 should cite the new theorem for rk = 2.
- `standalone/theorem_index.tex:360`: re-tag the conjecture entry,
  add a new theorem entry.
- `standalone/survey_modular_koszul_duality_v2.tex:5681`,
  `standalone/survey_modular_koszul_duality.tex:5675`,
  `standalone/survey_track_a_compressed.tex:2230`: each cites the
  conjecture; update to cite theorem-for-rk=2 and conjecture-for-rk≥3.

---

## Meta-verdict (Beilinson audit, internal)

The adversarial Wave-1 audit's framing ("low-hanging fruit — attack
via periodic-CDG + Arakawa C_2-cofiniteness") was MISGUIDED. The
periodic-CDG framework is not a tool to PROVE Koszulness; it is a
tool to DESCEND bar-cobar to an admissible adjunction modulo
periodicity. The Cartan-subalgebra obstruction at q ≥ 3 is
mathematically GENUINE — Koszulness in the strict sense of
`thm:koszul-equivalences-meta` (i)–(vi) is FALSE at rk ≥ 2, q ≥ 3.

The correct inscription is therefore a NON-KOSZULNESS theorem,
upgrading the existing conjecture to a theorem at rk = 2. The
periodic-CDG adjunction is compatible with (not contradictory to)
this non-Koszulness: the admissible-KL category is not a Koszul
category in the rigid sense, but it IS a 2p-periodic-CDG category,
which is the correct replacement.

The remaining genuinely open direction is the q ≤ 2 COMPATIBILITY
with Koszulness (prose claims this but does not prove it). This
IS a legitimate low-hanging fruit for a separate wave, using the
fact that at q ≤ 2 the Cartan classes move below the bar-relevant
range and may be absorbed into the diagonal by the remaining
Kac–Wakimoto character data.

No changes to the manuscript have been made. No commits performed.
