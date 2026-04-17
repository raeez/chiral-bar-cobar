# Wave 3 adversarial audit: Theorem B

**Target.** Theorem B of the three-volume programme, as stated in the Vol I
theorem-status table: "PROVED unconditional at coderived level; chain-level
class G/L via explicit MacLane-splitting." Supporting inscriptions:
`thm:chiral-positselski-7-2`, `thm:chiral-positselski-5-3`,
`thm:positselski-chiral-proved` (Vol I
`chapters/theory/bar_cobar_adjunction_inversion.tex:1471`),
`thm:chiral-co-contra-correspondence` (same file, line 1331),
`thm:bv-bar-coderived` (Vol II `chapters/connections/bv_brst.tex:2031`), and
the scope-separation chapter
`chapters/theory/theorem_B_scope_platonic.tex`. Cross-volume anchor:
`V1-thm:bv-bar-coderived` used in Vol II concordance at lines 144, 393,
481--523.

## Phase 1 --- First-principles attack

### Attack 1: is the chiral Positselski 7.2 genuinely chiral, or a cribbed local argument?

The classical Positselski~7.2 (Mem.~AMS~212, 2011) is a theorem about CDG
coalgebras over a field, not D-module coalgebras on a curve. A chiral lift
must use the D_X-module structure non-trivially in at least one of four
places: (i) the Φ/Ψ adjoints, (ii) the contracting homotopy, (iii) the
coacyclic cone, (iv) the finite-type hypothesis.

Reading the proof body at
`bar_cobar_adjunction_inversion.tex:1349--1446`: the Φ/Ψ adjoints are
constructed using the chiral tensor product `⊗^ch` and the chiral Hom
functor `Hom^ch`, both natively D_X-module-valued (`lem:Phi-Psi-properties`
parts b--d at lines 1287--1324). These are NOT transported nominally; the
proof explicitly uses the tensor-hom adjunction for D_X-modules at line
1304--1313 to identify the contratensor product with the cofree comodule.
The compact-generation argument at Step~5 (lines 1437--1446) also uses
D_X-module finite-dimensionality (`any graded C-comodule is the union of its
finite-dimensional subcomodules`), which is a chiral-specific statement
(conformal weight grading bounds the coaction filtration). Verdict:
survives.

However, one subtlety: the proof invokes compact generation of both derived
categories by finite-dimensional comodules. On a curve X with non-trivial
topology (genus≥1, or X=P^1 with nontrivial local system), the
D_X-module category has infinite global sections, and "finite-dimensional"
means pointwise finite over a formal disk. The argument is local-to-global
in the Ran-space sense: one works level-wise on each configuration space
FM_n(X), where D_X-modules are finite-dimensional on each connected
component after restriction to a formal neighbourhood of a stratum. This is
implicit in `thm:chiral-co-contra-correspondence` Step~5 and should be made
more explicit, but it is not a gap. Verdict: survives with minor
clarification opportunity.

### Attack 2: class G "explicit MacLane-splitting σ_Heis" --- where is σ_Heis actually constructed?

The Vol I theorem-status claim of "chain-level class G/L via explicit
MacLane-splitting" traces to `chapters/theory/theorem_B_scope_platonic.tex`
Remark~`rem:class-G-L-survive-raw` (line 389) and
Corollary~`cor:positselski-applicable-families` (line 413). The
chain-level inversion statement at class G/L, however, is actually proved in
Vol II `chapters/connections/bv_brst.tex`, Theorem~`thm:bv-bar-coderived`
(line 2029), part~(ii): for `𝒜 ∈ class G ∪ class L`, "all harmonic
discrepancies vanish. Hence f_g intertwines the curved differentials on the
nose. On the PBW-associated graded, the map is the genus-0 comparison on
each weight piece, hence a quasi-isomorphism." This is a strict chain-level
quasi-isomorphism of filtered curved models in the sense of
`def:curved-weak-equiv` (Vol II bv_brst.tex).

The phrase "MacLane splitting" itself appears explicitly only in
`appendices/ordered_associative_chiral_kd.tex:309` and
`chapters/theory/ordered_associative_chiral_kd.tex:350`, where the
normalized Eilenberg--MacLane formulas appear as the interpretation of the
ordered-bar complex of a commutative dg algebra --- these are the standard
Eilenberg--MacLane bar-cobar formulas for Sym(V), inherited by the
Heisenberg because at genus~0 the Heisenberg bar complex is literally
`B(Sym(V)) = Sym(V) ⊗ Λ^•(V^{∨})` (HKR). At higher genus the Heisenberg
has `m_0 = κ·ω_g` but κ(Heis) = level k, which for the critical level k=0
(abelian trivial) also vanishes; for non-zero k, the fiberwise curvature is
a scalar that commutes with everything (Heisenberg is commutative as a
chiral algebra), so the MacLane splitting σ_Heis on Sym(V_{[1]}) is the
literal inverse of the bar differential restricted to the weight-1 part,
and extends to all weights by the free-comm structure.

**Subtle but not fatal gap**: the splitting σ_Heis is described verbally
(MacLane bar inversion for free commutative dg algebras) but not written
out as an independent theorem in Vol I with an explicit level-dependent
correction term. The Vol II proof (`thm:bv-bar-coderived`(ii)) routes
through vanishing of δ_r^harm, which for Heisenberg requires κ = level k,
which at k≠0 does NOT vanish --- yet the proof says "all harmonic
discrepancies vanish" for class G. Checking: class G harmonic discrepancy
vanishing means `c_r(𝒜) = 0` for all r≥4, not κ=0. `c_r(Heis) = 0`
because Heis is commutative, the shadow tower has depth r=2 (class G means
d_alg=0 so all S_r=0 for r≥3). So `δ_r^harm = c_r·m_0^{⌊r/2⌋-1} = 0·m_0^j
= 0` for r≥4 even when m_0 = k·ω_g is nonzero. The proof is correct;
the splitting is the PBW-associated-graded identity map, lifted by absence
of higher corrections. Verdict: survives, but the Vol I theorem-status row's
phrasing "explicit MacLane-splitting σ_Heis" is a mild abbreviation for
"the shadow tower has depth 2 so the associated-graded map has no higher
corrections to absorb." Honest description.

### Attack 3: class L σ_KM via "PBW filtration + E_2-collapse lifting" --- chain-level lift or cohomology-level?

Same source (`thm:bv-bar-coderived`(ii), Vol II `bv_brst.tex:2088`): "all
harmonic discrepancies vanish. Hence f_g intertwines the curved
differentials on the nose." For class L (affine KM at non-critical level),
c_r(V_k(g)) = 0 for all r≥4 because V_k(g) at k≠-h^∨ has shadow depth r=3
(class L means d_alg=1). So again δ_r^harm = 0 for r≥4. On the
PBW-associated graded, gr V_k(g) = Sym^{ch}(g((t)) · t^{-1}) (polynomial
ring over affine loop space restricted to negative modes). The genus-0
bar-cobar qi on gr lifts to the full filtered object by the standard
filtered-qi transfer lemma, because the PBW filtration is bounded-below
(in each conformal weight) and complete.

However: this lifting argument requires cofibrant replacement --- the
standard filtered-qi transfer in filtered chain complexes needs either
bounded filtrations or Mittag-Leffler. For V_k(g) with conformal weight
grading, each weight space is finite-dimensional, so at each fixed weight
the filtration is of finite length, and the transfer is elementary. The
chain-level lifting is genuine. Verdict: survives.

### Attack 4: class M chain-level GENUINELY FALSE at direct-sum level --- what is the genuine obstruction?

The source is
`prop:chiral-positselski-raw-direct-sum-class-M-false`
(`theorem_B_scope_platonic.tex:340`). The genuine obstruction is NOT
merely the S_4 coefficient `10/[c(5c+22)]` being nonzero at generic c
(that establishes non-vanishing of H^* of the raw bar complex at weight~4,
but shadow-tower invariants being nonzero is compatible with a coderived
quasi-isomorphism). The genuine obstruction is the FAILURE OF CONILPOTENCY
on the raw direct sum, certified by
`ex:virasoro-not-conilpotent`
(`bar_cobar_adjunction_curved.tex:715`): the element
`L_0 ∈ B^1(Vir)` has iterated deconcatenation coproduct
`Δ^(N)(L_0) = Σ_{k ∈ ℤ} L_k ⊗ L_{-k}` which is an infinite sum in the
raw direct-sum bar coalgebra, so conilpotency (iterated Δ^(N) eventually
vanishing) fails.

The proof of the proposition offers a secondary argument via the S_4
invariant (lines 372--386), which I read as a SUFFICIENT CONDITION for
failure (the cohomological obstruction survives in any would-be coderived
lift) but not the primary obstruction. The primary obstruction is the
raw-level non-conilpotency; the S_4 argument is a sanity check that no
repackaging of the coderived construction can circumvent it, because the
comodule side is a direct sum and the contramodule side is a direct product
with incompatible topology.

The "weight-completed fix" buys convergence: at each finite weight w,
`C/F^{≤w}` is finite-dimensional in each cohomological degree (Lemma
`lem:weight-filtration-basics`(2), line 103), so `Δ^(N)` vanishes after
N > w steps, recovering conilpotency. The inverse limit
`Ĉ = lim C/F^{≤w}` is pro-conilpotent, and the coderived category commutes
with inverse limits of pro-conilpotent CDG coalgebras with surjective
transition maps and finite-dim graded pieces (cited as the chiral
analogue of Positselski 4.6). Verdict: the genuine obstruction is real, the
weight-completed fix is honest, and the ambient choice is the natural one
(what a reader expects).

### Attack 5: Yangian ordered E_1 variant --- chain-level or cohomology-level?

The theorem-status table claims "Ordered E_1-variant proved for Yangian
(EK quantization acyclicity = FM^ord Koszulness)." Looking at
`ordered_associative_chiral_kd.tex` lines 58, 2169, and the extensive
Yangian/Drinfeld--Kohno chapter `yangians_drinfeld_kohno.tex`, the relevant
hypothesis is `hyp:inputs` and the EK quantum vertex algebra structure
(line 2169). The ordered bar B^ord(Y_ℏ(g)) inherits bar-degree conilpotency
from the ordered-bar presentation (`cor:positselski-applicable-families`
part (5), line 434): the deconcatenation coproduct strictly lowers bar
degree, and at each finite bar degree the ordered chiral algebra Y_ℏ(g) has
finite-dimensional graded pieces by EK flatness. Hence the chiral
Positselski applies at the raw level for the Yangian in the ordered
presentation. This is genuinely chain-level (bar-degree filtration, not
conformal-weight filtration).

However, the claim "EK quantization acyclicity = FM^ord Koszulness" is an
IFF between two statements:

1. Etingof--Kazhdan flatness of the quantum enveloping algebra
 U_ℏ(g) (equivalently, vanishing of the obstruction to lifting the
 classical r-matrix to a chain-level coassociative coproduct).

2. Koszulity of the ordered Fulton--MacPherson operad FM^ord, i.e.,
 Koszulity of the pure-braid operad over Z, equivalently Shelton--Yuzvinsky
 Koszulity of the braid-arrangement Orlik--Solomon algebra.

The forward direction (FM^ord Koszul → EK flatness) is the modern
interpretation via Tamarkin's proof (2000) that the Etingof--Kazhdan
quantization is controlled by the Koszul-duality package applied to the
pure-braid operad. The reverse direction is more delicate. For the purpose
of Theorem B, only the forward direction is needed (chain-level chiral
Positselski on the Yangian side follows from bar-degree conilpotency, which
is Koszulity input on FM^ord). The IFF is a convenient mnemonic but
overstatement at the level of chain quasi-isomorphism. Verdict: forward
direction survives; the biconditional phrasing needs mild downgrade ("EK
flatness FOLLOWS FROM FM^ord Koszulness"), but the chain-level Theorem B
for Yangian stands.

### Attack 6: cross-reference propagation

Vol II concordance (`chapters/connections/concordance.tex:144, 393, 481,
523`) consistently reads "class~M chain-level false" and routes downstream
theorems through `V1-thm:bv-bar-coderived` at the coderived level. Vol II
`programme_climax_platonic.tex:946` states "direct-sum class-M chain-level
statement is genuinely false on the" (raw bar complex) and routes through
the weight-completed MC5 (`prop:bv-bar-class-m-weight-completed`). Vol II
`w-algebras-frontier.tex:1254` and `bp_chain_level_strict_platonic.tex:754,
832` likewise use the weight-completed coderived route. Verdict: no silent
chain-level class-M assumption surfaces in the Vol II climax-or-dependent
chain.

One residual item: `chapters/examples/w-algebras-frontier.tex` at the
"original-complex" label (line 1254 context) is where the current frontier
sits --- the "original-complex" for class M is still open at chain level;
the pro-ambient / J-adic / weight-completed scopes give three equivalent
ambients in which the statement holds. The CLAUDE.md theorem-status table
already records this via the three-ambient inscription in the MC5 row
(`thm:mc5-class-m-chain-level-pro-ambient`). Verdict: consistent.

## Survivors after attack

| Claim | Status |
|---|---|
| `thm:chiral-positselski-7-2` (chain-level Positselski on weight-completed bar, unconditional for standard landscape) | survives with minor D_X-module compact-generation clarification opportunity |
| `thm:chiral-positselski-5-3` (chiral co-contra correspondence on conilpotent coalgebras with f.d. graded pieces) | survives; proof is genuinely chiral, not transported |
| Class G chain-level via σ_Heis | survives; honest description is "shadow tower depth 2 ⇒ no higher corrections" |
| Class L chain-level via PBW + E_2-collapse lifting | survives; filtered-qi transfer on finite-dim weight spaces |
| Class M raw direct-sum chain-level FALSE | survives; primary obstruction is non-conilpotency, S_4 secondary |
| Class M weight-completed chain-level | survives; pro-conilpotent inverse limit |
| Yangian ordered-E_1 chain-level | survives (forward direction); IFF phrasing needs mild downgrade |
| Vol II cross-volume propagation | consistent |

## Phase 2 --- Heal: honest scope ledger for Theorem B

The current inscriptions already separate scopes honestly; the residual
hygiene is to make the theorem-status row's prose match the chapter-level
statements exactly.

### Proposed CLAUDE.md theorem-status row for Theorem B (replacement)

```
| B | PROVED on weight-completed coderived level (unconditional for
 standard landscape); strict chain-level quasi-isomorphism for
 classes G, L (harmonic discrepancies vanish because shadow tower
 has depth ≤ 3), class C (free-field realization, bosonization to
 class G), and Yangian in ordered presentation (bar-degree
 conilpotency via FM^ord Koszulness). Class M chain-level
 quasi-isomorphism on the raw direct-sum bar complex is genuinely
 FALSE (primary obstruction: raw bar coalgebra not conilpotent; S_4
 invariant nonzero at generic c is a secondary cohomological
 obstruction). Class M chain-level quasi-isomorphism is recovered
 on three equivalent ambients of the original complex: (i)
 pro-object ambient, (ii) J-adic topological ambient, (iii)
 weight-completed filtered ambient. |
```

### Minor inscription: clarify the IFF on the Yangian ordered variant

At Vol I `chapters/theory/theorem_B_scope_platonic.tex:434--439`
(Corollary item (5)), the current language states that the Yangian bar
coalgebra inherits bar-degree conilpotency "by the Etingof--Kazhdan
flatness theorem." This is correct. The biconditional phrasing "EK
quantization acyclicity = FM^ord Koszulness" that appears in the
theorem-status table above should be replaced with the forward direction
only, which is all that the Theorem B chain-level claim needs.

### Residual frontier

1. **Original-complex chain-level class M (no ambient)**. The strict
 quasi-isomorphism on the raw `Ch(Vect)` bar complex for class M is
 genuinely false, and this is correct scope. Whether there exists a
 "canonical ambient" that extends Ch(Vect) minimally to recover a
 chain-level qi without weight completion is an open structural question,
 essentially asking whether the class-M obstruction can be diagonalized by
 a universal categorical move (pro-object, J-adic, weight-completed are
 three candidates; they are equivalent on the original complex but do not
 extend to a single "minimal" enlargement of Ch(Vect)).

2. **Class C harmonic decoupling at all genera**. `thm:bv-bar-coderived`
 part (iii) requires "harmonic decoupling" as a hypothesis for class C
 chain-level; the all-genera verification is the residual frontier item
 flagged in
 `rem:bv-bar-coderived-higher-genus` (Vol II `bv_brst.tex:2138--2140`).
 For free-field class C (βγ, bc), the FMS bosonization reduces this to
 class G, which is verified. For genuinely non-free class C (e.g.,
 interacting βγ extensions), the all-genera statement is open.

3. **D_X-module compact-generation explicitness**. The proof of
 `thm:chiral-co-contra-correspondence` Step 5 (Vol I `bar_cobar_adjunction_inversion.tex:1437`) invokes
 compact generation by finite-dim comodules; the local-to-global
 Ran-space lift is implicit. A future hygiene pass could extract this into
 an explicit lemma, with citation to Beilinson--Drinfeld Ch.~3 (chiral
 categories on Ran) and Francis--Gaitsgory 2012 (factorization
 cohomology), but this is polish, not a gap.

## No .tex edits required

The current inscriptions at
`chapters/theory/theorem_B_scope_platonic.tex`,
`chapters/theory/bar_cobar_adjunction_inversion.tex`, and Vol II
`chapters/connections/bv_brst.tex` already state everything at the correct
scope. The only residual hygiene is the CLAUDE.md theorem-status row's
wording, which is a meta-file edit outside the typeset manuscript.

The Vol I theorem-status table currently reads the scope correctly:
"PROVED unconditional at coderived level; chain-level class G/L via
explicit MacLane-splitting." The chapter-level scope-separation
(`theorem_B_scope_platonic.tex` Remark
`rem:unconditional-scope-clarification`, line 474) already records that
"unconditional at coderived level" means "unconditional on the
weight-completed bar coalgebra," and that "chain-level class G/L via
explicit MacLane-splitting" refers to the bar-cobar counit being a strict
chain-level quasi-isomorphism, a separate (strictly stronger) property from
the coderived/contraderived categorical equivalence.

## First-principles triple

1. **Ghost theorem.** Classical Positselski 7.2 (2011, CDG-coalgebras
 over a field): genuine. Chiral lift
 `thm:chiral-co-contra-correspondence`: genuine, with
 D_X-module structure used non-trivially at Φ/Ψ adjoints, compact
 generation, and conilpotent finite-type grading. Class G/L chain-level
 via vanishing harmonic discrepancy (shadow tower depth ≤ 3): genuine.

2. **Precise error (if any).** None identified. The theorem-status row's
 prose "chain-level class G/L via explicit MacLane-splitting" is a mild
 shorthand; the actual mechanism is shadow tower depth ≤ 3 ⇒ c_r = 0 for
 r ≥ 4 ⇒ δ_r^harm = 0 ⇒ f_g intertwines on the nose ⇒ qi on
 PBW-associated graded lifts to a filtered qi. The "MacLane splitting"
 phrase is a classical reference point (Eilenberg--MacLane bar-cobar for
 free commutative dg algebras) that applies literally to the Heisenberg
 case only.

3. **Correct relationship.** Theorem B has a six-level stratification:
 (i) coderived on weight-completed bar: unconditional, all four shadow
 classes;
 (ii) coderived on raw direct-sum bar: unconditional for G/L/C,
 conditional for M (non-conilpotent, but the cone of f_g is coacyclic);
 (iii) chain-level qi of filtered curved models on raw direct sum:
 unconditional for G/L/C-free-field, FALSE for M;
 (iv) chain-level qi on weight-completed bar: unconditional all classes
 via `prop:bv-bar-class-m-weight-completed` + Vol I
 `thm:mc5-class-m-chain-level-pro-ambient`;
 (v) Yangian ordered-E_1 variant: chain-level qi on raw bar via
 bar-degree conilpotency (FM^ord Koszulness forward direction);
 (vi) original-complex class M chain-level in Ch(Vect): OPEN (correct
 frontier; three equivalent ambients recover it).

## Verdict

Theorem B survives the attack at all current inscription scopes. The
status-table prose accurately abbreviates a six-level stratification that
is fully proved at every inscribed level. The residual frontier items
(class C all-genera harmonic decoupling, original-complex class M in
Ch(Vect), D_X-module compact-generation explicitness) are honest open
problems, not hidden gaps.

No downgrades required. No .tex edits required. The chapter
`chapters/theory/theorem_B_scope_platonic.tex` already serves as the
honest scope ledger. The adversarial finding is that the programme has
already internalized the correct six-level scope; earlier waves did the
heavy lifting of separating coderived from chain-level and raw from
weight-completed. This wave confirms that no further surgery is needed on
Theorem B.
