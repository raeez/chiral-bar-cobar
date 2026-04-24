# F5 Drinfeld Double Audit

Audit date: 2026-04-24.

Volumes:
- Vol I: `/Users/raeez/chiral-bar-cobar`
- Vol II: `/Users/raeez/chiral-bar-cobar-vol2`
- Vol III: `/Users/raeez/calabi-yau-quantum-groups`

## Verdict First

F5 is not close to a theorem in its advertised global form. The strongest
live, well-scoped manuscript statement is a conjectural, fixed-curve,
bar-level existence problem for a meromorphic quasi-triangular chiral
Hopf-like object `U(A)=A \bowtie A^!`, whose binary semiclassical part is
the already-inscribed collision residue `r(z)`. The global family version
over `\overline{M}_{g,n}`, especially at `g >= 1`, is a separate and much
harder problem.

Three independent manuscript paths agree on the non-theorem status.

1. The canonical memory table identifies F5 as the universal Drinfeld double
   over `\overline{M}_{g,n}`, with local formal-disk coproduct plus antipode
   and global lift `conj:F5-local-global`, explicitly "OPEN at g >= 1"
   (`/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/platonic_ideal_reconstituted_2026_04_17.md:120`).
2. Vol II's operative Drinfeld programme says the core remarks name
   `U=A \bowtie A^!` "without constructing it" and that "Everything in this
   section is conjectural. No step is claimed as a theorem"
   (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6042`,
   `:6055`).
3. Vol III says the global quantum group obtained by Drinfeld doubling is
   obstructed by non-commutation of doubles with homotopy colimits, and is
   not produced in general
   (`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:63`,
   `:4482`, `:4483`).

There is also serious status drift. Vol I's holographic datum chapter marks
some `U_A` and Drinfeld-centre statements as `ProvedHere`
(`/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:1887`,
`:2251`, `:2391`), while Vol II's Drinfeld programme says the Hopf object,
antipode, center comparison, and hemisphere pairing are open or conjectural
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:972`,
`:981`, `:984`, `:987`, `:991`). The charitable reading is that Vol I proves
a modular-Koszul/pro-completed, categorical `U_A` shadow on named lanes, not
the global chiral Hopf Drinfeld double over families. The uncharitable
reading is overclaim.

## Recon Register

The grep sweep located the following active surfaces.

| Surface | Status found | Evidence |
|---|---|---|
| Seven faces, local `r(z)` | theorem for local collision-residue presentations, not a global double | Vol I master seven-face theorem: `/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex:35`; F5 there is Yangian `r`-matrix, not `D(A,A^!)`: `:65` |
| F5 local/global architectural row | conjectural/open at `g >= 1` | memory row: `/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/platonic_ideal_reconstituted_2026_04_17.md:120` |
| `U(A)=A \bowtie A^!` construction | conjecture, no unconditional structure maps | Vol II `conj:drinfeld-double-e1-construction`: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6076`, status at `:6114` |
| Bowtie in Vol I | `ProvedHere` on modular Koszul/pro-completed lane, but conflicts with Vol II open programme if read as Hopf double | Vol I universal property: `/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:1887`; strict off-locus still open: `:2354` |
| Antipode | definition/conjecture; bar reversal proved, double-level Hopf axiom doubly conjectural | Vol II definition: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2752`; conjecture: `:2833`; status: `:3026` |
| `Z(U_A)=Zder_ch(A)` | conjecture in Vol I preface and Vol II Hochschild; LHS tentative | Vol I conjecture: `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:4525`; Vol II conjecture: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5035`; tentative LHS: `:5011` |
| Hemisphere = cyclic pairing | conjecture; genus zero; Heisenberg hemisphere only heuristic | Vol II part (d): `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1554`; Heisenberg heuristic: `:1624`; scope: `:1771` |
| Dimofte `D|T|N` slab | bimodule, not SC disk; mostly translation/prose plus scoped boundary-linear theorem surface | Vol II slab correction: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:57`; remark: `:247` |
| KZB F5 boundary status | inconsistent: one conjecture says boundary regularity open, one theorem says boundary regularity proved | open conjecture: `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex:1100`; theorem says boundary points: `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/curved_dunn_higher_genus.tex:1454` |
| Vol III double obstruction | Drinfeld double/global quantum group not constructed in general | `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:1360`, `:2795`, `:2799` |

## (a) E_1-Chiral `D(A,A^!)` At Operadic Level

### 1. Definition Status

Part (a) is defined only as a conjectural sketch. Vol II states the setup:
`B^{ord}(A)=T^c(s^{-1}\bar A)` with deconcatenation, and
`A^!=(\bar B(A))^\vee` as Verdier-dual boundary algebra
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6063`,
`:6067`, `:6068`, `:6071`). It then conjectures an `E_1`-chiral Hopf
object `U(A)=A \bowtie A^!` (`:6076`, `:6080`, `:6082`).

The bowtie product is not a completed precise construction. Same-sector
products are declared to be the OPEs of `A` and `A^!`
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6089`).
The mixed sector is a meromorphic section on `C x C \ Delta`, not a
pointwise multiplication map (`:6093`, `:6098`, `:6101`, `:6102`). The
twisting datum is the universal twisting morphism, with the binary part
reducing to `r(z)` (`:6103`, `:6106`). The manuscript immediately says that
none of the structure maps is constructed unconditionally (`:6114`, `:6116`).

The coproduct is only a sketch. Vol II says `Delta_U` "should be" a map
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6196`),
should restrict to the bar deconcatenation structure (`:6203`, `:6206`), and
must satisfy quasi-triangular compatibility with a universal `R(z)` (`:6216`,
`:6220`, `:6224`). The relation to `r(z)` is that
`R(z)=1+tau_(2)+tau_(3)+...` and `r(z)=tau_(2)` at binary level (`:6240`,
`:6249`). That is an infinitesimal/classical shadow, not a constructed
quantum `R`-matrix.

The core chapter is even clearer: the full Drinfeld double whose module
category should be the line-operator category is "not yet constructed at the
bar-complex level" (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1395`,
`:1397`).

### 2. Proof Status

No proof of the full construction exists in Vol II. Part (a) explicitly says
the entire section is conjectural and no step is a theorem
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6054`,
`:6055`).

There are base-case checks. Heisenberg is described as tautological on class
G because the mixed product has no higher corrections, the coproduct is
primitive, and descent is naive (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6330`,
`:6349`, `:6355`, `:6361`). The affine `sl_2` level-one case is explicitly
not closed: the putative double "should be" an affine Yangian or variant,
but the precise identification is open (`:6378`, `:6382`, `:6384`).

Vol I's `holographic_datum_master` does contain `ProvedHere` statements for
`U_A=A \bowtie A^!_infty` representing Koszul pairs and being
quasitriangular with `R` equal to collision residue
(`/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:1887`,
`:1894`, `:1912`, `:1913`). It also marks an `E_2` Drinfeld infinity-centre
identification as `ProvedHere` on/off locus after pro-completion
(`/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2251`,
`:2268`, `:2282`, `:2286`). This does not supply the missing Vol II Hopf
maps. It should be read as a categorical/pro-completed modular-Koszul lane,
not as a chain-level construction of the global Drinfeld double over
families. Otherwise it directly contradicts Vol II's open status.

### 3. Weakest Precise Conjectural Form Currently Supported

For a strongly admissible `E_1`-chiral algebra `A` on a fixed smooth curve
`C`, after choosing a meromorphic braided line-operator category and a
Drinfeld/KZ associator, there should exist a quasi-triangular chiral
Hopf-like object `U(A)` whose underlying graded object is a completion of
`A \oplus A^!` or `A \otimes^tau A^!`, whose mixed product is a meromorphic
section on ordered two-point configurations, and whose binary semiclassical
part is the collision residue `r(z)`. The coproduct and antipode should
satisfy Hopf identities only up to the full higher MC tower.

That form is much weaker than "global Drinfeld double over
`\overline{M}_{g,n}`". It is also weaker than "an `E_1`-chiral Hopf algebra"
in the ordinary algebraic sense.

### 4. Gap To Theorem

The manuscript itself lists the gaps: mixed product as sheaf section rather
than bilinear map; missing `E_1` chiral factorization formalism with poles;
infinite higher MC tower; transcendental KZ associator; and `Sigma_n`
descent compatibility
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6260`,
`:6270`, `:6277`, `:6282`, `:6297`, `:6311`). The core double-bosonization
remark says the missing piece is the definition of a braided Hopf algebra in
a meromorphic `z`-dependent tensor category and that no part is proved
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1427`,
`:1435`, `:1436`, `:1437`).

### 5. Counterexamples, Type Errors, Conflations

**Critical type risk: `E_1` versus `E_2`.** A Drinfeld double is naturally
quasi-triangular/braided, hence lives in braided monoidal or `E_2` data.
Vol I itself distinguishes the Drinfeld centre as an `E_1`-category to
`E_2`-category construction
(`/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:4346` through
`:4388`) and warns that the chiral derived centre is not the same object as
the Drinfeld centre (`/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:12089`,
`:12095`, `:12098`). Vol III says a CoHA is ordered `E_1`; the missing swap
is precisely the `R`-matrix, which requires the Drinfeld double
(`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:3334`),
and that the `R`-matrix lives in two halves of the double, not in the
positive half alone (`:3353`, `:3354`).

AP165 makes the same problem sharper. The bar complex is only an `E_1`
coassociative coalgebra and explicitly does not carry
`SC^{ch,top}` structure
(`/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/feedback_sc_primary_use.md:9`,
`:11`, `:16`). Vol I has the same principle inscribed: the bar complex is
`E_1` coassociative, not SC, and SC emerges on the derived chiral centre
(`/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1352`,
`:1357`, `:1364`, `:1367`, `:1388`). If `D(A,A^!)` is claimed as an
ordinary `E_1`-chiral Hopf object directly on `B(A)`, the `R`-matrix and
Drinfeld-double axioms are not typed. The only coherent target currently
visible is an `E_1` algebra object inside a meromorphic braided/line-operator
category, or an `E_2` Drinfeld-centre object after passing to the derived
centre pair. The manuscript does not yet define that target fully.

## (b) Antipode From Orientation Reversal

### 1. Definition Status

There is a conjectural definition, not a theorem. Vol II defines the chiral
Drinfeld antipode for the conjectural Hopf object `U_A=A \bowtie A^!`
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2752`,
`:2754`). It has a bar-coalgebra stage using order reversal and Verdier
intertwining (`:2763`, `:2767`) and a double stage exchanging the two
tensorands via the pairing (`:2769`, `:2771`). For Heisenberg it gives the
generator-level formula `S(J(z))=-J(-z)` (`:2775`, `:2780`).

### 2. Proof Status

Only the ingredients are proved. Order reversal on the ordered bar coalgebra
is proved; orientation reversal equals Verdier duality is proved elsewhere;
the double-level antipode is conjectural and verified only on class G
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:3026`,
`:3029`, `:3031`, `:3034`, `:3037`). The actual Hopf antipode axioms are
conjectural (`:2833`) and the status remark says the antipode axiom involving
the coproduct is "doubly conjectural" (`:2876`, `:2878`).

### 3. Weakest Precise Conjectural Form Currently Supported

On class G/primitive examples, order reversal of the ordered bar coalgebra
extends to the expected generator-level antipode. Beyond class G, if the
part (a) coproduct exists and if the homotopy anti-homomorphism tower is
constructed, then orientation reversal should extend to a Hopf antipode on
`U_A`.

### 4. Gap To Theorem

The manuscript names the gaps: higher `A_infty` operations require coherent
homotopies `S_k`; the antipode axiom cannot be checked until the coproduct
is constructed; and the squaring element is unknown for class M
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2966`,
`:2972`, `:2974`, `:2981`, `:2985`). The proposed relation
`u_A=Phi(K_A)` is only a hoped-for formula (`:2992`, `:3003`).

### 5. Counterexamples, Type Errors, Conflations

The slogan "orientation reversal gives the antipode" is under-typed unless
the relevant orientation reversal is specified as a monoidal
anti-equivalence compatible with multiplication and coproduct. Vol II
mentions complex conjugation/local `z -> -z` and Verdier duality
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:2740`,
`:2744`, `:2747`, `:2749`), but this does not prove
`S(ab)=S(b)S(a)` or `(id tensor S)Delta=eta epsilon`. Those are separate
Hopf axioms and are stated only conjecturally (`:2842`, `:2847`).

There is no theorem that orientation reversal on `\bar M_{g,n}` itself
matches the Hopf antipode axiom. Complex conjugation, real structures, and
Hodge involutions are not interchangeable in the manuscript. A global
all-pairs antipode is therefore ABSENT. The actual verified scope is class G
plus bar-level order reversal.

## (c) `Z(U_A)=Z^{der}_{ch}(A)`

### 1. Definition Status

The right-hand side is defined: the chiral derived centre is chiral
Hochschild cochains/cohomology
(`/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:7179`,
`:7181`) and the universal bulk in the open/closed theorem (`:7186`,
`:7191`). Vol II main likewise defines
`Zder_ch(A)=RHom_{A tensor A^op}(A,A)` as chiral Hochschild cochains
(`/Users/raeez/chiral-bar-cobar-vol2/main.tex:1181`, `:1183`).

The left-hand side is not a settled classical Drinfeld centre. Vol II says
the "ordered Drinfeld centre" required by the thesis is tentatively
identified with `HH^0` of the `E_1` module category of `U_A`, computed on
the ordered bar resolution
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:4982`,
`:4984`, `:4990`). It then explicitly says the classical Drinfeld centre is
an `E_2` invariant, while the ordered bar side is `E_1`, and that in the
absence of a fully worked chiral `E_1`-centre construction this is a
tentative identification (`:5011`, `:5013`, `:5017`, `:5018`).

Vol I preface states the equation as a conjecture under topologization
hypotheses (`/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:4525`,
`:4527`, `:4530`, `:4534`).

### 2. Proof Status

The equation is a conjecture in Vol II:
`conj:drinfeld-center-equals-bulk` (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5035`,
`:5045`, `:5050`). The proof section is only a proof strategy with three
steps (`:5073`, `:5075`). Vol II states bar-cobar/Verdier do not identify
the two sides and the Hochschild functor is a separate input (`:5057`,
`:5065`, `:5070`).

Vol I's `holographic_datum_master` claims a stronger `ProvedHere` Drinfeld
infinity-centre statement on the modular Koszul locus and after
pro-completion off locus
(`/Users/raeez/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex:2251`,
`:2267`, `:2282`). That is not synchronized with Vol II's conjectural
status. If it is intended to close part (c), Vol II is stale. If Vol II is
canonical for the Drinfeld programme, Vol I is overclaiming. The audit
cannot honestly collapse those into a theorem without resolving the drift.

The Heisenberg base case is explicitly heuristic: the computation compares
`Z(U_Hk)` to `k[[kappa]]` only after an illegitimate truncation and records
the inconsistency (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5197`,
`:5215`, `:5221`, `:5225`).

### 3. Weakest Precise Conjectural Form Currently Supported

Assuming:
- part (a) constructs `U_A`,
- `U_A` has a module category equivalent to the line-operator category,
- pointwise centres globalize as factorization algebras,
- the Verdier dual factorizes strictly enough, and
- chiral Hochschild cochains are compatible with the bar-cobar/Verdier
  construction,

then the ordered `E_1` centre of `U_A`, defined as the derived endomorphism
algebra of the `U_A` module category on the ordered bar resolution, should be
quasi-isomorphic to `ChirHoch(A)`.

### 4. Gap To Theorem

The manuscript lists the three exact obstructions: class M breaks
stalk-wise reduction because higher `A_infty` pieces are invisible at a
single stalk; Verdier dual factorization does not commute with stalk
restriction in general; and bar-cobar does not directly give the centre, so
a Hochschild/bar-cobar compatibility theorem is missing
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5116`,
`:5128`, `:5131`, `:5137`, `:5142`, `:5152`). Vol I preface identifies the
same three obstructions (`/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex:4541`,
`:4548`).

### 5. Counterexamples, Type Errors, Conflations

The equality is not even well-typed without a comparison functor. Vol I's
concordance explicitly says Drinfeld centre `Z(C)` is a braided monoidal
category of half-braidings and never a chain complex, while
`Zder_ch(A)` is a derived chain-level analogue
(`/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:12089`,
`:12092`, `:12095`, `:12097`). Vol II tries to repair this by redefining
the left side as an ordered Hochschild-type object, but that is tentative
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5017`,
`:5019`).

Class M is an immediate adversarial test: any proof that reduces the centre
to pointwise stalks loses the higher `A_infty` operations by the manuscript's
own obstruction statement (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:5120`,
`:5127`). Critical affine levels are another excluded zone because the
finite Theorem H window can fail, as Vol II notes while excluding
`k=-h^\vee` in the programme conditions (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6008`,
`:6012`).

## (d) Hemisphere = Cyclic Pairing

### 1. Definition Status

The hemisphere partition function is defined in Vol II as a scalar
`Z_{D^3}[T;B] in C`, computed by localization for a 3d `N=4`
holomorphic-topological theory with boundary condition
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1409`,
`:1418`, `:1423`, `:1425`). The slab pairing is gluing of two hemispheres
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1431`,
`:1438`, `:1440`).

The cyclic pairing on `B^{ord}(A)` is precisely defined for cyclic
`A_infty` chiral algebras and marked `ProvedElsewhere`
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1463`,
`:1479`, `:1485`, `:1492`, `:1500`).

The equality is conjectural: `conj:hemisphere-cyclic-pairing` assumes a 3d
theory with transverse boundary conditions `D,N`, `H_D=A`, `H_N=A^!`, and a
cyclic `A_infty` pairing, then asserts equality up to a scalar
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1554`,
`:1559`, `:1561`, `:1565`, `:1570`, `:1573`).

### 2. Proof Status

No theorem proves the equality. The section says every identification is
conjectural
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1401`,
`:1404`). The Heisenberg cyclic-bar side is `ProvedHere` (`:1516` and
`:1661`), but the Heisenberg hemisphere computation is `Heuristic` and
explicitly lacks a published primary source for the `D^3` abelian CS
hemisphere (`:1624`, `:1642`, `:1647`).

### 3. Weakest Precise Conjectural Form Currently Supported

For a genus-zero spherical slab, on a locus where a 3d HT bulk theory exists
with transverse boundary conditions realizing `A` and `A^!`, and where `A`
is cyclic `A_infty`, the hemisphere pairing should equal the cyclic ordered
bar pairing after multiplying by a nonzero normalization scalar.

### 4. Gap To Theorem

Vol II lists four obstructions: availability of the bulk 3d theory,
Omega-background gluing for the slab-to-hemisphere step, existence of a
cyclic `A_infty` structure, and regularity of the normalization
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1717`,
`:1723`, `:1732`, `:1740`, `:1754`). The genus-g generalization is
explicitly conjectural on both sides at `g >= 1` (`:1771`, `:1776`,
`:1780`, `:1781`).

### 5. Counterexamples, Type Errors, Conflations

The statement is false as an all-landscape assertion unless modified:
class C `beta gamma` is not cyclic in the strict sense because a weight-zero
generator prevents a non-degenerate invariant pairing
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1744`,
`:1748`). The left side is undefined for a general chiral algebra unless a
3d bulk theory with the right boundary algebra has been constructed
(`:1723`, `:1731`). The Dimofte step is a single physics-level slab fiber
functor input, not an inscribed chain-level theorem (`:1595`, `:1602`).

## (e) Genus 0 Status

### 1. Definition Status

The genus-zero binary collision residue is strongly represented. Vol I's
master seven-face theorem says the seven presentations determine the same
collision residue, with F5 listed as the Yangian `r`-matrix and
`R(z;hbar)=1+hbar r(z)+O(hbar^2)` satisfying QYBE by Drinfeld
(`/Users/raeez/chiral-bar-cobar/chapters/connections/master_concordance.tex:35`,
`:42`, `:65`, `:68`). This is a theorem about `r(z)` and its
presentations, not a construction of `D(A,A^!)`.

The canonical memory file says F5 local presentation includes coproduct plus
antipode on `A \bowtie A^!` on the formal disk, but marks the global lift
conjectural/open at `g >= 1`
(`/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/platonic_ideal_reconstituted_2026_04_17.md:120`). In live Vol II, even the
fixed-curve construction is conjectural (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6076`,
`:6116`).

### 2. Proof Status

Formal disk/P1/`\bar M_{0,n}` full Drinfeld double status:
- formal disk: binary `r(z)` theorem, full double ABSENT except class G
  tautological/primitive checks.
- fixed `C=P^1`: no full `D(A,A^!)` Hopf construction located; only
  genus-zero KZ/Yangian/r-matrix surfaces.
- `\bar M_{0,n}`: no full family Drinfeld double located; KZ associator and
  seven-face localizations are not the same as a Hopf double.

The Heisenberg local case is the closest extractable theorem: `U(H_k)` is
described as `H_k \bowtie H_-k`, mixed product prescribed by `r(z)=k/z`,
with all obstructions vacuous and construction tautological on class G
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6330`,
`:6337`, `:6349`, `:6355`, `:6361`). The affine `sl_2` next case is open
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6378`,
`:6384`).

### 3. Weakest Precise Conjectural Form Currently Supported

At genus zero, the honest theorem is:

> The binary collision residue `r(z)` has the listed seven presentations in
> the standard landscape, with F5 interpreted as the classical Yangian
> `r`-matrix presentation.

The honest F5 double conjecture at genus zero is:

> On the formal disk, for class G and possibly finite-depth class L/C after
> choosing associator data, `A \bowtie A^!` should admit a quasi-triangular
> meromorphic Hopf-like structure whose binary piece is the proven `r(z)`.

### 4. Gap To Theorem

The gap from genus-zero `r(z)` to genus-zero Drinfeld double is the entire
quantization/associator/coproduct package. The seven-face theorem proves the
shadow, not the object casting it. Vol II's part (a) makes this explicit by
saying `r(z)` determines degree two but not higher degrees
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6282`,
`:6295`).

### 5. Counterexamples, Type Errors, Conflations

The most dangerous conflation is "same `r(z)`" implies "same Drinfeld
double." It does not. The manuscript itself treats `r(z)` as the binary
classical part `tau_(2)` of a tower (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6240`,
`:6249`). In class M the tower is infinite (`:6292`, `:6295`), so the
binary theorem is radically weaker than a double theorem.

## (f) Genus 1 Breakdown

### 1. Definition Status

Vol I constructs a genus-one F5 face as an elliptic `r`-matrix for affine
Kac-Moody at noncritical level. The theorem says the genus-one collision
residue equals the Belavin elliptic `r`-matrix up to level normalization
(`/Users/raeez/chiral-bar-cobar/chapters/connections/genus1_seven_faces.tex:467`,
`:474`, `:475`, `:478`). It also states the elliptic CYBE (`:502`,
`:508`) and proves the identification by regularizing the channels to
Weierstrass/theta functions (`:512`, `:519`, `:528`, `:542`).

That is not a genus-one Drinfeld double. It is a genus-one `r`-matrix face.

### 2. Proof Status

There is a serious KZB status inconsistency. The programme climax states F5
as a conjecture: smooth-locus Jimbo-Miwa KZB is closed, but boundary-stratum
regularity at `\overline{M}_{g,n}` for `g >= 1` remains open
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/programme_climax_platonic.tex:1100`,
`:1107`, `:1110`, `:1115`). The modular PVA frontier repeats the same
scope: smooth-locus closed, boundary extension open
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/modular_pva_quantization_frontier.tex:1802`,
`:1808`, `:1813`, `:1815`).

But Vol II's curved-Dunn chapter states a `ProvedHere` theorem claiming KZB
regularity at every boundary point of every stable-graph stratum and coherent
modular operad composition at every boundary point
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/curved_dunn_higher_genus.tex:1454`,
`:1458`, `:1476`, `:1484`). This is a live inconsistency. Even if the
curved-Dunn theorem is accepted as an upgrade of the KZB analytic piece, it
does not construct the Drinfeld double, antipode, center comparison, or slab
pairing.

### 3. Weakest Precise Conjectural Form Currently Supported

At genus one, the supported theorem is the elliptic `r`-matrix/collision
residue identification for affine KM. The supported conjecture for F5 is
that this elliptic/dynamical `r`-matrix can be integrated into a
quasi-Hopf/meromorphic braided line-operator category and then into a
Drinfeld double compatible with KZB isomonodromy in the modular parameter
`tau`.

### 4. Gap To Theorem

The missing genus-one step is not just regular singular versus irregular
singular KZB. It is compatibility of elliptic/dynamical `R`-matrices with
the double axioms under modular covariance in `tau`. Vol III records the
elliptic stratum as quasi-Hopf with a Felder-Jimbo-Konno dynamical
associator, not a strict Hopf object
(`/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:1060`,
`:1062`). Vol II's antipode frontier also points beyond elliptic to
Siegel-elliptic dynamical `R`-matrices as a frontier, with anomaly data at
genus 2 (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding-frontier.tex:3055`,
`:3057`).

### 5. Counterexamples, Type Errors, Conflations

An elliptic `r_ell(z,tau)` satisfying CYBE is not automatically compatible
with a Drinfeld double coproduct. The manuscript has no proof that modular
transport in `tau` preserves `Delta^op=R Delta R^{-1}` for the conjectural
`Delta_U`; indeed `Delta_U` itself is not constructed
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_frontier.tex:6196`,
`:6216`, `:6224`). Any statement that genus-one F5 is solved because the
elliptic `r`-matrix is known is therefore a type error: it confuses the
classical infinitesimal face with the quantum Hopf object.

## (g) Dimofte `D|T|N` Slab Interpretation

### 1. Definition Status

The current manuscripts correctly treat the slab as a bimodule geometry, not
as an SC disk. Vol II says the slab has two boundary components, with `A` on
one wall and `A^!` on the other, and is "a bimodule geometry, not a
Swiss-cheese disk"
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:57`,
`:61`, `:64`, `:68`). The same correction appears in the preface
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/frame/preface.tex:941`,
`:945`), consistent with AP165.

The manuscript defines a slab fiber functor by
`F(ell)=Hom_T(D,ell,N)` and says `U=End(F)` reconstructs the line category
as the Drinfeld double
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:70`,
`:73`, `:79`, `:83`). It lists the five geometric components: factors,
hemisphere Hopf pairing, antipode from interval reversal, coproduct from
cutting, and `R`-matrix from meromorphic braiding (`:85`, `:99`).

### 2. Proof Status

The slab statements are mostly explanatory/translation remarks, not a
chain-level or `(infty,1)`-categorical theorem identifying a concrete
bimodule `A-M-A^!`. The core line says the slab fiber functor "realises" the
double as universal algebra of line operators and records the translation to
the algebraic framework
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:247`,
`:250`, `:254`). The theorem surface nearby is weaker: for any logarithmic
`SC^{ch,top}` algebra, bulk identifies with chiral Hochschild cochains of
the boundary; line-side module models and derived-center identifications
require the chirally Koszul, compact-generation, and derived-center
hypotheses (`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_bulk_boundary_line_core.tex:113`,
`:126`, `:138`, `:142`).

The Dimofte memory note also classifies WP1/WP2 as bimodule/global-triangle
conjectural beyond the Koszul locus and the double as conjectured universal
boundary-bulk algebra
(`/Users/raeez/.claude/projects/-Users-raeez-chiral-bar-cobar/memory/dimofte_six_workpackages.md:15`,
`:17`).

### 3. Weakest Precise Conjectural Form Currently Supported

The supported conjecture is: for a 3d HT theory with transverse boundary
conditions `D,N` whose boundary algebras are `A,A^!`, the slab fiber functor
on line operators should be represented by a universal algebra whose
algebraic avatar is the chiral Drinfeld double `A \bowtie A^!`; under
Koszul/compact-generation/derived-center hypotheses, the bulk is the derived
chiral centre of the boundary and the line category is modeled by
`A^!_line` modules.

### 4. Gap To Theorem

The missing theorem would need to build the actual bimodule category,
identify `F` as a monoidal fiber functor, prove Tannakian reconstruction
`End(F)=A \bowtie A^!`, and show that the resulting algebra has the
coproduct, antipode, `R`-matrix, and Hopf pairing listed in the prose. None
of that is inscribed as a proof.

The `K`-matrix is also not a full coproduct formula. Vol II gives the
operator
`K_A(z)=z^{alpha_0} exp(sum alpha_-n/-n z^n) exp(sum alpha_n/-n z^-n)`
and says it controls deviation from primitive coproduct
(`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1400`,
`:1405`, `:1408`). Vol I has a schematic formula
`Delta_K=K o Delta` and says the shadow tower generates `K` corrections
(`/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:18308`,
`:18314`, `:18323`). But there is no chain-level formula for the modified
coproduct on `U(A)` with coherence, associator, antipode, and factorization
compatibility. ABSENT.

### 5. Counterexamples, Type Errors, Conflations

The manuscripts have mostly repaired the AP165 slab/SC conflation: slab is
not an SC disk, and SC lives on `(Zder_ch(A),A)`, not on `B(A)`
(`/Users/raeez/chiral-bar-cobar-vol2/main.tex:1181`, `:1190`;
`/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1364`,
`:1390`). The remaining risk is using the slab prose to infer a mathematical
double before the fiber-functor reconstruction is proved. The slab
interpretation remains physics-level motivation plus scoped boundary-linear
theorems, not a rigorous construction of global `D(A,A^!)`.

## BRUTAL VERDICT

### How Far Short Is F5?

At `g=0`: halfway for `r(z)`, far short for `D(A,A^!)`. The binary
collision residue/seven-face theorem is real, and Heisenberg class G is
tautological. But the full Drinfeld double needs a meromorphic braided
Hopf-object formalism, full coproduct, associator, antipode, center
comparison, and slab pairing. None is proved beyond primitive/base lanes.

At `g=1`: the elliptic `r`-matrix face is proved for affine KM, but the
global double is not. The modular parameter `tau`, KZB/isomonodromy, and
dynamical/quasi-Hopf associator introduce structural issues. The KZB
boundary status is internally inconsistent across Vol II; even accepting the
stronger KZB theorem only closes an analytic connection piece, not the
Drinfeld double.

At `g>=2`: F5 is a frontier, not a theorem. Vol I's higher-genus raw F5
object is modular-sheaf-theoretic:
`R pi_*(j_*^{ord} B^{ch})`, with boundary extension classes controlling
obstructions
(`/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:39327`,
`:39335`, `:39349`). That is not a Hopf double. Vol III confirms the global
Drinfeld-double operation does not commute with hocolims and full quantum
groups are unconstructed in general
(`/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex:4482`,
`:4483`).

### Named Obstructions, Ranked

1. **Structural: target-category obstruction (`E_1` versus `E_2`).**
   Define the actual category in which a meromorphic `z`-dependent
   quasi-triangular Hopf object lives. Current `E_1` wording is not enough
   for a Drinfeld double with `R`-matrix.

2. **Structural: global-family descent/hocolim obstruction.**
   Prove Drinfeld doubles commute with, or can be reconstructed over,
   families of curves/moduli. Vol III explicitly says this fails or is
   obstructed for global quantum groups.

3. **Structural: coproduct and associator obstruction.**
   Construct `Delta_U` and a coherent KZ/elliptic/Siegel associator tower
   satisfying `Delta^op=R Delta R^{-1}` with meromorphic poles and modular
   covariance.

4. **Structural: center-comparison functor obstruction.**
   Build the functor identifying the ordered centre of `U_A` with the
   chiral Hochschild/derived centre of `A`. The two sides are not naturally
   the same kind of object.

5. **Structural: antipode homotopy obstruction.**
   Extend bar order reversal to the double and construct the coherent
   anti-homomorphism tower `S_k`, including the squaring element `u_A`.

6. **Technical-to-structural: KZB boundary/status obstruction.**
   Resolve the Vol II inconsistency: either `conj:f5-irregular-singular`
   remains open at boundaries, or `thm:irregular-singular-kzb-regularity`
   supersedes it. Then connect the analytic KZB theorem to the double
   axioms.

7. **Technical: `K`-matrix coproduct formula.**
   Upgrade `K_A(z)` and schematic `Delta_K=K o Delta` to a chain-level
   coproduct formula on `U(A)` with coherence and compatibility with
   antipode and `R`.

8. **Technical: cyclic/hemisphere normalization obstruction.**
   Prove the `D^3` hemisphere computation from a primary source, establish
   Omega-background gluing, and restrict or repair non-cyclic families such
   as class C.

### Extractable Honest Theorems Now

1. **Genus-zero binary seven-face theorem.**
   State only the `r(z)` identification, not the Drinfeld double. This is
   already in Vol I and is supported by the master seven-face theorem.

2. **Class G local primitive double.**
   For Heisenberg/free/lattice-type primitive lanes on the formal disk,
   `U(H_k)=H_k \bowtie H_-k` with primitive coproduct and generator-level
   antipode is an honest narrow theorem candidate. Do not attach the center
   equality unless the Tamarkin/Theorem H inconsistency is repaired.

3. **Affine KM `r`-matrix faces.**
   Rational genus-zero and elliptic genus-one `r`-matrix identifications can
   be stated as face theorems. They should not be called Drinfeld-double
   theorems.

4. **Boundary-linear bulk theorem.**
   The bulk as chiral Hochschild/derived centre of the boundary is already a
   theorem under its own hypotheses. It is not `Z(U_A)=Zder_ch(A)` unless
   the line/double reconstruction is added.

### Single Sharpest Adversarial Attack

The sharpest attack is the type attack:

> The programme asks for an `E_1`-chiral Drinfeld double on the ordered bar
> side, but a Drinfeld double with `R`-matrix, antipode, and center is
> naturally `E_2`/braided line-category data. AP165 says `B(A)` is only an
> `E_1` coassociative coalgebra and that `SC^{ch,top}` lives on the derived
> centre pair, not on `B(A)`. Therefore the claimed object is not well-typed
> unless it is reformulated as an algebra object in a meromorphic braided
> line-operator category or as an `E_2` Drinfeld-centre construction. Once
> reformulated that way, `Z(U_A)=Zder_ch(A)` is no longer a direct equality
> of two pre-existing chain complexes; it becomes a new comparison theorem
> that is currently missing.

This attack does not merely expose a missing lemma. It can force a major
reformulation of F5: from "global `E_1`-chiral Hopf double over families" to
"global meromorphic braided line-category reconstruction whose binary
classical shadow is the proven `r(z)`."

### Final Split

Proved core:
- binary collision residue and several `r(z)` faces at genus zero;
- genus-one elliptic `r`-matrix face for affine KM;
- bar order reversal and orientation/Verdier ingredients;
- boundary-derived-centre theorem under its own open/closed hypotheses;
- class G primitive sanity checks.

Computational or base-case evidence:
- Heisenberg `U(H_k)` primitive/tautological double behavior;
- Heisenberg cyclic bar pairing;
- affine `sl_2` binary mixed product heuristic;
- KZB analytic regularity depending on which Vol II status surface is
  accepted.

Conditional bridge:
- `U(A)=A \bowtie A^!` as universal reconstructor;
- antipode on the double;
- `Z(U_A)=Zder_ch(A)`;
- hemisphere equals cyclic pairing;
- Dimofte slab Tannakian reconstruction.

Conjectural extension:
- global Drinfeld double over `\overline{M}_{g,n}` for `g>=1`;
- class M infinite tower double;
- elliptic/Siegel dynamical quasi-Hopf global family compatibility;
- Vol III global quantum vertex group via Drinfeld double.

Heuristic picture:
- all seven faces as projections of one global `U_A`;
- Dimofte `D|T|N` slab as already giving the double;
- `K`-matrix as a complete coproduct correction;
- orientation reversal as automatically satisfying Hopf antipode axioms.
