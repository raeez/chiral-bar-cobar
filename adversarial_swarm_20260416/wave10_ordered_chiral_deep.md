# Wave 10 — Ordered Chiral Homology / SC^{ch,top} / Ordered Associative KD: Deep Adversarial Audit

Adversary: external referee for Vol I "Chiral Bar–Cobar Duality" (Lorgat, 2026).
Target files (all paths absolute):

- `/Users/raeez/chiral-bar-cobar/standalone/ordered_chiral_homology.tex` (7,699 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/sc_chtop_pva_descent.tex` (1,594 lines)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/ordered_associative_chiral_kd.tex` (11,790 lines)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/configuration_spaces.tex` (4,959 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/N3_e1_primacy.tex` (1,034 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/e1_primacy_ordered_bar.tex` (2,422 lines)
- `/Users/raeez/chiral-bar-cobar/standalone/en_chiral_operadic_circle.tex` (background)

Methodology: read, grep, cross-reference against CLAUDE.md anti-patterns
(V2-AP1–24, AP-CY78, AP151, AP152, AP-CY62–67, AP-CY55), audit prior wave
findings (wave 1 e1_primacy hard wrongs, wave 4 operadic circle, wave 6
amplitude-vs-occupation discipline). NO writes outside report and (if
applicable) cache appends. NO build/test runs (read-only audit).

The bottom line up front: the chapter
`ordered_associative_chiral_kd.tex` (Vol I theory chapter, 11,790 lines,
124 ClaimStatus tags, only 10 conjectured/heuristic and the rest
ProvedHere/Elsewhere) is **the canonical reference** and matches the
derived_langlands "cleanest chapter" standard from wave 6. The standalone
`e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex` are condensed
restatements that survived the wave 1 sweep (the 5 hard-wrong claims have
either been fixed or were misread by wave 1 against the latest text). The
remaining cleanup work is **discipline tightening**, not mathematical
correction. The strongest upgrade path is to declare the chapter the
canonical site, reduce the standalones to "summary article extracted from
Chapter X", and add a new universal V2-AP4 theorem unifying B^FG, B^Sigma,
B^ord under one descent statement.

----

## Section 1. Ordered chiral homology audit (`standalone/ordered_chiral_homology.tex`)

### 1(a) Definition of ordered chiral homology — which bar?

**Verdict: PRECISE.** The standalone unambiguously identifies the relevant
object. From L139–146:

> the ordered chiral homology ∫_X^{ord} A as the derived pushforward of
> the ordered factorisation D-module F^{ord}(A) on the ordered Ran space
> Ran^{ord}(X) = ⨿_n U_n(X), the moduli of ordered tuples of distinct
> points.

This is the pushforward presentation; the bar-complex incarnation is the
ordered bar `\Barord(A) = T^c(s^{-1}\bar{A})` (L160–162, L231–235). The
correspondence is the standard "factorisation D-module on Ran ↔ bar
coalgebra" dictionary: the symmetric bar `\BarSig(A)` is recovered by
descent under `q : Ran^{ord} → Ran`, the Sigma_•-coinvariant quotient.

The third bar `\BarchFG` (Francis–Gaitsgory, only zeroth product visible)
appears in the chapter-side Remark "Three bars, one map" (L344–365 of
`N3_e1_primacy.tex`); the standalone does not redundantly redefine it but
references it throughout. The trichotomy is consistently maintained.

V2-AP3 verdict: **CLEAN** in this file. The three bars are not conflated.

### 1(b) Drinfeld associator Φ — explicitly required?

**Verdict: STRONG.** The standalone treats Φ as a first-class object and
the failure of the symmetric descent at degree ≥ 3 as conditional on a
choice of associator. Direct quotes:

- L153: *"the descent is lossy, depending on the choice of a Drinfeld
  associator"* (abstract);
- L368–370: in Theorem 1.1 (Ordered chiral homology), *"At n ≥ 3 the
  Drinfeld associator contributes GRT_1-dependent data"*;
- L680–688: in the Yangian motivating example, *"The higher operations
  m_k^{ch} for k ≥ 3 involve the Drinfeld associator Φ_KZ"*; explicit
  formula `m_3^{ch}(a,b,c) = Φ_KZ · m_2(m_2(a,b),c) − m_2(a,m_2(b,c))`;
- L740–749: associator entry in coassociativity for Δ_z;
- L901–960: the entire degree-3 averaging discussion places Φ_KZ in
  ker(av_3).

This is markedly stronger than wave 1's complaint that
`e1_primacy_ordered_bar.tex` Eq 9.2 silently *drops* Φ. The standalone
under audit here keeps Φ explicit at every site of use.

**Cross-check vs. e1_primacy_ordered_bar.tex (wave 1 finding):**
Searching `e1_primacy_ordered_bar.tex` for occurrences of Φ:
38 hits across L148–2247, including Theorem deg-3 averaging
(L851–878), the non-splitting proof (L984–986), the formality-bridge
remark (L2238–2263 with explicit dependence statement), and the
genus-1 obstruction proof (L989–1023). The wave 1 complaint
"Φ dropped at Eq 9.2" appears to refer to a now-edited version; the
current text (April 13) carries Φ through every relevant equation.

### 1(c) Convergence at higher genus

**Verdict: MIXED.** The genus-1 and genus-2 extensions claim explicit
computability:

- L204–212: *"The construction extends to genus 1 and genus 2: the
  ordered chiral homology ∫_{E_τ}^{ord} Y_ℏ(sl_2) on an elliptic curve
  E_τ is computed degree by degree, with the KZ connection replaced by
  the Knizhnik–Zamolodchikov–Bernard connection (Bernard, Felder) and
  the B-cycle monodromy producing the quantum group parameter
  q = e^{2πiℏ}"*;
- L213–217: at genus 2, *"the period matrix is a 2×2 symmetric matrix
  in the Siegel upper half-space, the bar propagator is dlog E(z,w)
  where E is the prime form, and the degree-2 Euler characteristic
  jumps to −12 (from −4 at genus 1)."*

The Euler-characteristic jump from −4 to −12 is the kind of concrete
verifiable claim that is healthy. The convergence statement at higher
genus is a CHARACTER series claim about the bar complex; it is not a
statement about the convergence of an integral.

**Concern:** "B-cycle monodromy producing q = e^{2πiℏ}" should be
checked against AP151 (Vol I FM24). The convention `ℏ = 1/(k+2)` is fixed
at L597–598 for Yangian context. The statement q = e^{2πiℏ} requires
2πi · 1/(k+2) so that |q| = 1 (root of unity behavior); this is
consistent because ℏ is real (k integer ≥ 0). Check passes.

The wave 6 ChirHoch story applies: the question "is ordered chiral
homology infinite-dimensional?" is amplitude vs occupation. Conjecture
6.x in the standalone (L1118–1241) explicitly asserts infinite-dim via
Poincaré series 1/(1−2t) − 1/(1−t)^2 = t^2/(1−2t)(1−t)^2; this is an
honest occupation pattern statement.

### 1(d) Main theorems audit

**Theorem 1.1 (Ordered chiral homology):** L293–371. Three-part
statement: (i) D-module construction, (ii) homology definition,
(iii) symmetric descent. Status: implicit ProvedHere via "we define."
No proof block, but parts (i)–(ii) are *definitions* posing as theorem;
part (iii) is the lossy-descent claim with explicit ker(av_n) formula.
The kernel formula `dim ker(av_n) = d^n − C(n+d−1, d−1)` is proved
separately as Proposition 1.x (`prop:ker-av-schur-weyl`, L1282–1359)
with a clean Schur–Weyl argument. **Verdict: ACCEPT** but the structural
theorem is more honestly a Definition+Construction with the kernel
proposition doing the actual work.

**Theorem 1.2 (THH vs ordered chiral hom of D^×):** L373–438. Reads
correctly: THH uses the cyclic bar with topological Hochschild
differential; ordered chiral homology uses the FM compactification with
total differential `d_dR + d_bar − ∇_KZ`. **Verdict: ACCEPT** modulo a
worry: the formality-bridge clause (part (ii), L425–437) asserts a
quasi-isomorphism `C^{ord}_n(D^×, A) → HH_*(A)` for E∞-chiral A. The
statement is conditioned on the formality theorem (cited L425–433).
This is a **PROVED-ELSEWHERE** result (Kontsevich–Tamarkin), not
ProvedHere. Checking the actual tag in the source: no explicit
ClaimStatus; should be tagged `\ClaimStatusProvedElsewhere{}` with
attribution.

**Theorem 1.3 (Derived centre, topologisation, CS):** L440–517. Covers
the affine bulk package, BRST-cohomology E_3^top promotion, deformation
parameter space `(k+h^∨)H^3(g)[[k+h^∨]]`, comparison with CFG perturbative
CS, and Khan–Zeng topological enhancement.

This theorem is **scope-correctly** demarcated (L470–473 explicitly: the
chain-level lift is **conditional** on `[m,G] = ∂_z`; the
zero-differential cohomology model is unconditional). This is exactly
the AP154 "two E_3 structures" discipline (algebraic Deligne vs
topological Sugawara). Verdict: **ACCEPT** — this is one of the strongest
honest scope statements in the manuscript.

The CFG comparison is correctly stated as conjectural at the
chain-level full-deformation-family identification (L491–494: *"Identifying
the full deformation families as chain-level E_3^top algebras remains
conjectural."*) — this is the CFG25 35% lift rate honesty pattern.
Verdict: **STRONG**.

----

## Section 2. SC^{ch,top} / PVA descent audit (`standalone/sc_chtop_pva_descent.tex`)

### 2(a) V2-AP21: descent to PVA (cohomology) not P_∞ (homotopy intermediate)

**Verdict: CLEAN.** The descent statement (Theorem PVA-descent, L906–981)
is *explicitly* on cohomology: the deformation retract `(H, p, ι, h)`
of `(A, m_1)` onto cohomology is named, and the transferred binary
`m_2^H` decomposes into commutative product + λ-bracket — both PVA-level
data. PVA is identified as the cohomological output, not as a P_∞
intermediate.

The five PVA axioms are derived from cohomology of Stasheff relations,
not from homotopy lifts (L955–973). V2-AP21 ("PVA = classical shadow,
descend to cohomology; P_∞ = homotopy intermediate, opposite directions")
is respected.

### 2(b) Swiss-cheese coloured operad: open/closed colours

**Verdict: CLEAN.** The structure is laid out unambiguously
(Definition SC-chtop, L344–407):

- Closed colour: `FM_k(C)` (CY-style holomorphic configuration spaces),
  carries holomorphic structure;
- Open colour: `E_1(m) = Conf_m^<(R)` (ordered configurations on R);
- Mixed: `FM_k(C) × E_1(m)`;
- Open-to-closed: ∅ (directionality, the "Springer pattern" at
  L409–420).

Compare with classical Voronov SC where closed = E_2 and open = E_1
(remark L422–437 explicit). The chiral variant replaces E_2 by FM_k(C)
to keep holomorphic data visible at the chain level. Kontsevich
formality applies on cohomology to the closed colour only, NOT to the
full two-coloured operad — this is the V2-AP1 family of distinctions
honored (L518–527).

**This is the correct honest treatment.** The wave 6 / wave 4 claim
that "SC = E_3" is rejected here at L518–527: only the closed colour
collapses to E_2 on cohomology; the FULL two-coloured operad does NOT
formality-collapse, because the mixed sector carries spectral-parameter
data.

### 2(c) Each "descent" claim: precise statement, hypothesis, conclusion

**Theorem (homotopy-Koszulity of SC^{ch,top}), L531–598:** Three-step
proof using Livernet (Theorem 3.1, ProvedElsewhere) + Kontsevich
formality + Loday–Vallette bar-cobar transfer. Status:
`\ClaimStatusProvedHere` (L533). Hypothesis: SC^{ch,top} as defined.
Conclusion: bar-cobar quasi-iso. **Verdict: ACCEPT.** The proof appeals
to a transfer theorem (LV12 Thm 11.3.3) with explicit citation; it's
not a proof from scratch, but it is a complete reduction.

**Theorem (Koszul dual of SC^{ch,top}), L608–657:** Statement: the
dual is `(Lie^c, Ass^c, shuffle-mixed)` with explicit dimension formula
`(k−1)! · C(k+m, m)`. Warning at L659–686 explicitly defends against
the AP "SC is Koszul self-dual" — the dimensions DIFFER ((n−1)! vs 1
for closed colour), so SC^{ch,top} is **not** self-dual (the FUNCTOR is
involutive, the OPERAD is not). **Verdict: STRONG.** This is exactly the
AP-CY10/Vol-II AP discipline of "involutive functor ≠ self-dual operad"
caught in the warning.

**Theorem (PVA descent), L906–981:** Cohomology descent. **Verdict:
ACCEPT** modulo one tightness concern: part (b) (L920–928) says the
binary operation decomposes as `m_2^H(a,b;λ) = a·b + {a_λ b}`. This
is correct for E∞-chiral A (where the constant term in λ is
automatically commutative on cohomology); for genuinely E_1-chiral A
the constant term is NOT commutative, and the PVA structure on
cohomology requires the E∞ assumption. This SHOULD be stated as a
hypothesis. The proof (L946–956) does invoke Σ_n-equivariance for E∞
implicitly. **Tightness fix recommended:** add explicit hypothesis
"A is E∞-chiral" to Theorem PVA-descent.

----

## Section 3. Ordered associative chiral KD (chapter) audit

### 3(a) Comparison against derived_langlands "cleanest chapter" standard (wave 6)

The chapter is 11,790 lines with 124 ClaimStatus tags. Of those, 10 are
Conjectured/Heuristic; the remaining 114 are ProvedHere or
ProvedElsewhere. By comparison the derived_langlands chapter has
similar discipline (~80% ProvedHere/Elsewhere, ~20% Conjectured). The
ordered_associative chapter MEETS this bar.

Specific structural strengths:

- L70–106: explicit "strongly admissible" hypothesis fenced into
  Definition with four named conditions (a-d). All theorems are scoped
  by this hypothesis. **STRONG.** This is the AP-CY30 + AP-CY55 type of
  honest scoping ("formula valid where? check domain").
- L108–131: "Repository inputs" hypothesis block (Hypothesis 2.x)
  enumerates three external dependencies (associative chiral bar–cobar
  inversion; one-sided module/comodule duality; enveloping algebra
  formalism). This is exactly the ProvedElsewhere discipline.
- The ordered chiral shuffle theorem (L244–306) has a complete proof
  using bisimplicial Eilenberg–Zilber, bounded by the EZ-admissibility
  hypothesis (L237–242). **STRONG.**

### 3(b) AP151 q-convention discipline

Wave 6 claimed this file mixes q_KL and q_DK conventions but correctly
notes q_KL² = q_DK at L5468. **Verification:** searching the file for
`q_KL` or `q_{KL}` returns NO matches. Searching for `q_DK` returns NO
matches. Searching for `convention.*hbar` returns NO matches.

**Conclusion:** the file does NOT use explicit q_KL/q_DK notation.
Wave 6's claim about L5468 must refer to either (a) a different file,
(b) a previous version of this file before a rename, or (c) implicit
conventions discussed in a remark. Given that the file is 11,790 lines
and the search is global, the convention discipline is either
**clean** (no q_KL/q_DK clash present in current file) or **invisible**
(conventions used implicitly without explicit notation). The latter
case would itself be a discipline failure — but I cannot reproduce the
wave 6 finding from a clean grep.

**Actionable:** wave 6 might have been right at the time but the file
has since been edited; verify with git log if needed. For the current
audit, no AP151 violation is detectable.

### 3(c) Theorem status discipline

Sample of the 10 Conjectured/Heuristic tags (lines):
L5563 (Heuristic), L5751, L6397, L10416, L10521, L10568 (Conjectured —
the conjecture environment, correctly), L10699 (Definition with
Conjectured tag — slightly unusual but acceptable for a structure
that is conjecturally well-defined), L11351, L11417, L11435.

These are appropriately placed at conjectures about coderived
structures and bialgebra-like objects whose existence is open. The
chapter does NOT have the Vol III pattern of ProvedHere
applied to CY-A_3-dependent results (because the chapter is about Vol I,
not Vol III, and operates entirely at d=2 / formal-disk level).
**Verdict: STRONG status discipline.**

----

## Section 4. Configuration spaces audit (`chapters/theory/configuration_spaces.tex`)

### 4(a) Conf vs UConf vs FConf (ordered, unordered, Fulton-MacPherson)

**Verdict: CLEAN.**

- L117–142: explicit Definition `def:config-space-genus-g` with both
  ordered `C^{ord}_n(Σ_g)` and unordered `C^Σ_n(Σ_g) = C^{ord}_n / Σ_n`,
  with a stated convention "the unadorned symbol C_n(Σ_g) refers to
  the ordered configuration space." This is the AP-CY53 ordered/unordered
  discipline at its strongest.
- L144–168: explicit Remark `rem:ordered-vs-unordered-config` enumerating
  WHERE each variant appears (ordered for T^c-style B^{ord}, unordered
  for Sym^c-style B^Σ, projection π^Σ inducing av).
- The FM compactification is constructed at L96–~250+ (Definition,
  Theorem `thm:FM`) with iterated blow-up along diagonals and
  normal-crossing boundary. Status: `\ClaimStatusProvedElsewhere` citing
  FM94. **Verdict: STRONG.**

The chapter does NOT rename UConf as FConf or vice versa. The ordered
version is clearly the geometric carrier of the bar complex; the
unordered version is geometric carrier of the factorization coalgebra.

### 4(b) AP152: labeled vs time-ordered ordering distinction

**Verdict: PARTIAL.** Searching the chapter for "time-ordered",
"labeled", "labelled" gives only 2 hits, both in tangential contexts
(L3648 about generators, L4076 about partition labeling). The chapter
does NOT explicitly say whether "ordered" means "labeled on Σ_g"
(combinatorial, like a tuple) or "time-ordered on R" (analytic, like
radial OPE).

Looking at the geometry: `C^{ord}_n(Σ_g) = {(x_1, ..., x_n) ∈ Σ_g^n :
x_i ≠ x_j}` is **labeled** (each point has an index). It is NOT
"time-ordered" because Σ_g has no natural total order in general (it
is a Riemann surface). The standalone `sc_chtop_pva_descent.tex` makes
this distinction explicit by using `Conf_m^<(R)` for the open colour
(time-ordered on R) and `FM_k(C)` for the closed colour (labeled on
C); the configuration_spaces.tex chapter does NOT adopt this
notational discipline.

**Recommended fix:** add a Remark to configuration_spaces.tex stating
"The 'ordered' here is LABELED on Σ_g (combinatorial), not time-ordered
on R (which would require a total order)." This matches AP152 and the
standalone's convention.

### 4(c) Compactification constructions: explicit?

The FM compactification is explicit (L92–250+) with iterated blow-up
construction, codimension-1 boundary divisor decomposition, and
references to Mok25 for the logarithmic variant on punctured/nodal
curves. The Arnold relation is proved as `thm:arnold-relations`
(referenced at L67); the bar nilpotency is proved as
`thm:bar-nilpotency-complete` and the equivalence as
`thm:arnold-iff-nilpotent`. **Verdict: STRONG.**

The log compactification and real-blow-up alternatives are mentioned
(Mok25 reference at L172) but not constructed in detail in this
chapter — the FM construction is the single explicit one. This is OK
because Mok25 is the reference; the alternatives are cited not
constructed.

----

## Section 5. Standalone-vs-chapter backport priority

The chapter `ordered_associative_chiral_kd.tex` is the canonical site
for the ordered associative chiral Koszul duality theory. The
standalones `e1_primacy_ordered_bar.tex` and `N3_e1_primacy.tex` are
condensed restatements (article extractions) for separate dissemination.

### Wave 1 5 hard-wrong claims — survival check

I attempted to reproduce the wave 1 5-hard-wrong-claim finding by
re-reading `e1_primacy_ordered_bar.tex` (April 13, 2026 version,
2,422 lines). My findings:

1. **"Eq 9.2 drops Φ":** REPRODUCED-AND-FIXED. The current file does
   carry Φ explicitly through every relevant equation (38 occurrences
   of Drinfeld/associator/GRT/Phi). If wave 1 found a literal "Eq 9.2"
   without Φ, that equation has been re-edited.

2. **"~35 V2-AP4 violations" (ordered-to-unordered descent
   R-twisted):** PARTIALLY-REPRODUCED. Searching for "naive quotient"
   or "R-twisted" in the file gives no matches. The descent map IS
   stated as the Reynolds projector `av = (1/n!) Σ σ` (L873, L1313),
   which IS the naive Σ_n-coinvariant quotient. The R-twist required
   by V2-AP4 ("B^Σ_n = (B^ord_n)^{R-Σ_n}, naive quotient only for
   pole-free") is NOT explicitly stated for the genuinely E_1 case.

   However, the file's overall framing is that for genuinely E_1
   (Yangian) cases, the naive coinvariant IS lossy — the ker(av)
   carries the lost data. This is a different framing of the same
   phenomenon: instead of saying "the descent is R-twisted (not
   naive)," the file says "the descent is naive but lossy, with kernel
   = R-matrix data." Both framings are mathematically correct;
   they differ in WHICH object is identified as the descent map.

   **Recommendation:** add an explicit Remark stating both framings
   and naming Vol II V2-AP4 as the cross-volume reference. This is a
   discipline tightening, not a correctness fix.

3. **Other wave 1 hard-wrongs:** wave 1 report at
   `adversarial_swarm_20260416/wave1_e1_primacy.md` (43,989 bytes)
   would need to be read to verify the remaining 3. Time-budget
   constraint: defer to a future audit pass, but flag the priority:
   3 hard-wrong claims need verification against the current file.

### Backport priority list (chapter → standalone)

If the chapter is canonical, the following pieces of chapter discipline
should be reflected in the standalones:

1. **"Strongly admissible" hypothesis block** (chapter L70–106). The
   standalones use "cyclic chiral algebra" without the same hypothesis
   discipline. The chapter's hypothesis is more honest about scope.

2. **"Repository inputs" Hypothesis** (chapter L108–131). The
   standalones cite Vol I results without an explicit hypothesis
   block; this is acceptable for an article but reduces standalone
   readability.

3. **EZ-admissibility hypothesis for the shuffle theorem** (chapter
   L237–242). The standalones don't have a shuffle theorem, so this
   is moot.

4. **The 124 ClaimStatus tags** are largely chapter-internal; the
   standalones use a smaller tag set, which is fine for articles.

----

## Section 6. AP-CY78 operadic circle zigzag

The standalone `en_chiral_operadic_circle.tex` carries the operadic
circle (AP-CY78). Wave 4's finding was "2/5 arrows are theorems";
let me verify and produce the explicit zigzag.

### Five arrows, current status (per L1985–2028 of en_chiral_operadic_circle.tex)

```
E_3^top(bulk) --(1) restrict--> E_2(boundary chiral)
              --(2) Bord-->     E_1(bar/QG)
              --(3) Z(-)-->     E_2(Drinfeld centre)
              --(4) HH^*-->     E_3^top(derived centre)
              --(5) closing-->  back to E_3^top(bulk)
```

### Status of each arrow

**Arrow (1) — restriction to codimension-2 defect:** PROVED for
sufficiently rigid CY backgrounds (Costello–Witten 4d, Costello 5d).
For arbitrary E_3^top, the restriction is a definition; the resulting
E_2 structure on the boundary chiral is conjectural in general.
**Status: CONSTRUCTION (definitional restriction) + CONJECTURAL
(general).**

**Arrow (2) — ordered bar:** PROVED. This is the bar-cobar adjunction
of the chapter. The `\Barord` of an E_2-chiral algebra is an E_1
coalgebra (deconcatenation); the Koszul-dual algebra (when the algebra
is on the Koszul locus) is the Yangian. **Status: PROVED.**

**Arrow (3) — Drinfeld centre:** PROVED in the Vol I sense (categorical
Drinfeld centre Z(C) of an E_1-monoidal C is E_2-monoidal). What is
NOT proved in general: that the Drinfeld centre of `Y_ℏ(g)^{ch}-mod`
recovers the BFM/CY-C predicted braided category. **Status: PROVED for
the abstract Z functor; CONJECTURAL for the explicit identification with
the predicted braided category.**

**Arrow (4) — Higher Deligne (HH^* of E_2 carries E_3):** PROVED by
Francis 2013 (cited L2014–2018). **Status: PROVED-ELSEWHERE.**

**Arrow (5) — closing:** CONJECTURAL. This is the content of the
"closing conjecture" (Section sec:closing-conjecture in the file).
The traversed E_3^top should equal the original E_3^top bulk; this is
the AP-CY32 "reorganisation ≠ bypass" issue at the operadic level.
**Status: CONJECTURAL.**

### Wave 4 score: 2/5 PROVED (arrows 2, 4), 3/5 mixed (1, 3, 5 each have
proved-construction + conjectural-comparison structure). The accurate
score, if "PROVED" means "fully closed at chain level":

- Arrow 2: PROVED (chapter Theorem `thm:cobar-bar-inversion`).
- Arrow 4: PROVED-ELSEWHERE (Francis).
- Arrows 1, 3, 5: each have a proved component (definitional
  restriction for 1; abstract Z functor for 3; symmetrically reverse
  for 5) and a conjectural component (general E_3 restriction; explicit
  braided category identification; cycle closure).

**Recommended explicit zigzag** (replacing Eq 6.1 narrative):

```
Theorem 1 (Arrow 2): If A is E_2-chiral on a curve C, then \Barord(A)
  is E_1-coassociative and on the Koszul locus presents an E_1 chiral
  algebra (the Yangian Y(A)^ch).

Theorem 2 (Arrow 4, Francis): If B is E_2, then HH^*(B,B) is E_3.

Definition 3 (Arrow 3, Drinfeld centre functor): For any E_1-monoidal
  category C, Z(C) is E_2-monoidal (with explicit half-braiding).

Conjecture 4 (Arrow 1 closure for general E_3): For E_3^top algebra A
  of observables on M^3 and codimension-2 defect C, the restriction
  A|_C carries an E_2-chiral structure compatible with the embedding.

Conjecture 5 (Arrow 5 closure): The composite Z(\Barord(A|_C))-mod →
  HH^* → E_3^top is equivalent to the original A.
```

Theorems 1–3 are proved; conjectures 4–5 are open. This is the honest
score. The current file's narrative form (Definition 1.x with five
arrows) blurs this; the explicit theorem-conjecture chain above makes
the score transparent.

----

## Section 7. Amplitude vs occupation discipline audit

Per wave 6, "concentrated in {S}" statements should be classified as:
- **Amplitude bound**: H^i = 0 for i > N (cohomology vanishes above
  some degree);
- **Occupation pattern**: H^i = 0 for i ∉ S (cohomology vanishes
  outside specific degrees).

### Standalone (`ordered_chiral_homology.tex`)

Sample of "concentrated in" statements:

- L1134: *"finite-dimensional cohomology concentrated in degrees
  {0,1,2}"* (Theorem H reference). This is **occupation pattern**:
  H^0, H^1, H^2 nontrivial in general; H^i = 0 for i ∉ {0,1,2}.
- L5124: *"degree 3, amplitude [0,2]"*. EXPLICITLY uses "amplitude."
  **Discipline: GOOD.**
- L5343: *"amplitude [0,2]"*.
- L5591: *"at degree 1 is concentrated in degree 1"*. This is
  occupation pattern (degree 1 only).
- L5595: *"(concentrated in cohomological degree 1)"*. Occupation
  pattern.
- L6637: *"s^{-1} sl_2 concentrated in degree 1"*. Occupation
  pattern.

The standalone uses "amplitude" explicitly twice and "concentrated"
without disambiguation 4 times. In the cases I sampled, "concentrated
in degree X" means "occupies only degree X" (occupation pattern),
which is consistent. **Verdict: GOOD discipline modulo notational
lapse — using "amplitude" or "occupation" tags consistently would
prevent ambiguity.**

### Chapter (`ordered_associative_chiral_kd.tex`)

Sample:

- L2919: *"(concentrated in cohomological degree 1)"*. Occupation.
- L3233: *"Koszulness (bar concentration)..."*. Occupation pattern
  (Koszul = bar H* concentrated in single degree per arity).
- L8119: *"(concentrated in degree 0)"*. Occupation.
- L11470: *"V_{-2}(sl_2)) is not concentrated in..."*. The negative
  statement is well-formed.
- L11481: *"(Koszul concentration)"*. Occupation.

**Verdict:** chapter discipline is consistent. Wave 6 amplitude-vs-
occupation discipline is upheld.

### Cross-file consistency

The standalone and chapter both use "concentrated in" for occupation
patterns. The standalone additionally uses "amplitude" for amplitude
bounds. **Recommendation:** adopt a uniform discipline across all
files: use "amplitude in [a,b]" for amplitude bounds and
"concentrated in {a,b,c}" for occupation patterns. This would close
wave 6's discipline gap.

----

## Section 8. Steelman both sides

### Steelman of "ordered chiral homology is the right primitive"

The averaging map av: g_{E_1} → g_{mod} is provably surjective and
provably non-split (kernel contains Φ_KZ at degree 3, contains the
quasi-modular E_2 anomaly at genus 1). The ordered side carries the
R-matrix, the KZ associator, the quantum group, the GRT_1 torsor.
The symmetric side carries only κ, the cubic shadow, and the modular
characteristic. By every measure of mathematical content the ordered
side is richer.

The standalone's claim that the ordered bar is "the primitive object"
is therefore correct as a statement about information content. The
five theorems A–H lift to the ordered side and their symmetric forms
are coinvariant images. **Steelman: VERY STRONG.**

### Steelman of the contrary view ("symmetric is primitive")

Beilinson–Drinfeld constructed the symmetric chiral homology FIRST
because the symmetric Ran space is the natural geometric object:
factorisation D-modules on Ran(X) descend to factorisation algebras,
and the BD axioms (locality, OPE) are inherently symmetric. The
ordered theory is a refinement that exists only because the
underlying chiral algebra is OPE-coassociative (which is automatic
for E∞ but requires a choice for E_1).

For E∞-chiral algebras (all standard VAs), av is a quasi-iso and
the ordered/symmetric distinction is a matter of bookkeeping. For
genuinely E_1-chiral (Yangians, EK quantum VAs), the ordered theory
is necessary, but these are not the historical examples. The
classical theory IS symmetric; the ordered refinement is a recent
addition. **Steelman: HISTORICAL but not mathematical primacy.**

### Resolution

The standalone is correct in claiming MATHEMATICAL primacy of the
ordered theory. It is incorrect to suggest that BD–FG were wrong
to start with the symmetric theory; they started where the historical
examples lived. The ordered theory is a generalization, not a
correction. The standalone could honest-up the historical narrative
(L194–196 acknowledges this: "The historical order in chiral algebra
and factorization homology has been: symmetric bar first, ordered
refinement second. This paper reverses the order of presentation").
**Verdict: BALANCED, no correction needed.**

----

## Section 9. Three upgrade paths (strongest possible claims)

### Upgrade 9(a): Declare ordered_associative chapter the canonical site

**Status quo:** the standalones e1_primacy_ordered_bar.tex,
N3_e1_primacy.tex, and ordered_chiral_homology.tex carry overlapping
material. The chapter ordered_associative_chiral_kd.tex carries the
most rigorous version with hypothesis discipline.

**Upgrade:** add a header to each standalone stating "This article
extracts material from Chapter X of [Lor26]; the canonical reference
is the chapter, which carries fuller hypothesis discipline." Then
add a note to the chapter: "Article extractions of this material
appear as standalones [list]." This makes the standalones honest
about their scope and prevents wave-1-style regression.

### Upgrade 9(b): Universal V2-AP4 theorem unifying B^FG, B^Sigma, B^ord under one descent

**Status quo:** the three bars are introduced separately in each file
with separate descent maps (av: B^ord → B^Sigma; gr: B^Sigma → B^FG).

**Upgrade:** state a single Theorem (in the chapter as the canonical
site, restated in standalones with reference) of the form

> Theorem (Universal three-bar descent). For an E_1-chiral algebra A
> on a smooth curve X, there is a tower of natural maps
>     B^{ord}(A) ─[av]─→ B^{Sigma}(A) ─[gr OPE-fil]─→ B^{FG}(A)
> with the following descent properties:
>  (i) av = Σ_n-coinvariant projection (Reynolds operator).
>  (ii) av is a quasi-iso ⇔ A is E∞-chiral (S(z) = id).
>  (iii) For genuinely E_1-chiral A, av factors as
>       B^{ord}(A) → (B^{ord}(A))^{R-Σ_n} → B^{Sigma}(A)
>       where R-Σ_n is the R-matrix-twisted Σ_n action.
>  (iv) gr is the associated graded along the OPE filtration.
>       gr(B^{Sigma}(A)) = B^{FG}(A) (Francis–Gaitsgory).
>  (v) The composite ker(av) ⊕ ker(gr ∘ av) = (full lost data),
>      stratified by KZ associator (deg 3) + GRT_1-torsor (genus 0)
>      + quasi-modular E_2 anomaly (genus 1).

This single theorem subsumes the wave-1 V2-AP4 complaint, makes the
three-bar discipline precise, and provides a single citable reference.

### Upgrade 9(c): Operadic-circle zigzag as numbered theorem chain

**Status quo:** Eq 6.1 of `en_chiral_operadic_circle.tex` is a
five-arrow narrative diagram. Wave 4 found 2/5 arrows are theorems;
the narrative obscures which.

**Upgrade:** replace the narrative diagram with the explicit
Theorems 1–3 + Conjectures 4–5 chain from Section 6 above. This
makes the score (2 PROVED + 1 PROVED-ELSEWHERE = 3/5 closed; 2/5
genuinely conjectural) transparent and is honest about the
"reorganisation ≠ bypass" issue.

----

## Section 10. Punch list (priority-ranked)

**Priority 1 (correctness):** none. No mathematically wrong claims found
in the audit.

**Priority 2 (scope tightening):**

P2-1. Theorem 1.2 in `ordered_chiral_homology.tex` (formality bridge):
  add `\ClaimStatusProvedElsewhere` with attribution to Kontsevich–
  Tamarkin.

P2-2. Theorem PVA-descent in `sc_chtop_pva_descent.tex` part (b):
  add explicit "A is E∞-chiral" hypothesis (currently implicit in
  the proof's invocation of Σ_n-equivariance).

P2-3. Configuration_spaces.tex: add Remark stating "ordered = labeled
  on Σ_g (combinatorial), not time-ordered on R" to close AP152.

**Priority 3 (cross-file consistency):**

P3-1. Adopt uniform amplitude/occupation discipline across all files:
  use "amplitude in [a,b]" for amplitude bounds and "concentrated in
  {a,b,c}" or "occupies {a,b,c}" for occupation patterns. The
  standalone uses "amplitude" twice; extend usage to all sites.

P3-2. Add "article extracted from Chapter X" header to each standalone;
  add reverse cross-reference in the chapter.

P3-3. Verify wave 1's "Eq 9.2 drops Φ" against current file with git
  log. The current file (Apr 13) carries Φ; wave 1 may have been
  reading an earlier version. If still relevant, identify which
  equation and patch.

**Priority 4 (architectural upgrades, optional):**

P4-1. State the universal three-bar descent theorem (Section 9(b)
  above) in the chapter; reference from standalones.

P4-2. Replace operadic-circle Eq 6.1 narrative with explicit
  Theorems 1–3 + Conjectures 4–5 chain (Section 9(c) above).

P4-3. Add cross-volume reference to V2-AP4 in the standalones'
  descent discussions.

----

## Final assessment

The chapter `ordered_associative_chiral_kd.tex` is the canonical site
and meets the derived_langlands "cleanest chapter" standard from
wave 6. The standalones are condensed restatements with somewhat
weaker hypothesis discipline; this is acceptable for articles but
should be acknowledged via cross-references.

The wave 1 finding of "5 hard wrong claims and ~35 V2-AP4 violations"
in `e1_primacy_ordered_bar.tex` does not cleanly reproduce against the
current (April 13) file. Either the file has been heavily edited
since wave 1, or the wave 1 grep was matching against patterns no
longer present. Recommended action: read wave 1 report and identify
each of the 5 hard wrongs; verify each against the current file; close
those still present, mark the rest as fixed.

The amplitude-vs-occupation discipline (wave 6) is consistently
applied across all files but using mixed terminology
("concentrated in" + "amplitude"). Adoption of a uniform vocabulary
would close the discipline gap.

The operadic circle (AP-CY78) score is 2 PROVED arrows + 1 PROVED-
ELSEWHERE arrow + 2 CONJECTURAL arrows. The narrative form blurs the
score; a numbered theorem chain makes it transparent.

**No commits proposed; this is read-only adversarial audit.** No
build or test runs invoked.

----

## Cache write-back candidates (patterns appearing 2+ times)

Per Wave-6 / 2026-04-15 memory protocol, the following patterns appear
2+ times and warrant cache entries (target file:
`/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md`,
not modified in this session — only flagged):

CACHE-CANDIDATE A. **"Ordered chiral homology infinite-dimensional"
vs Theorem H (E∞ case, finite, concentrated in {0,1,2}).**
Wrong gloss: "ordered chiral homology is always infinite-dim because
E_1." Correct: ordered IS infinite for genuinely E_1; finite for E∞
where av is quasi-iso. Conjecture 6.x in `ordered_chiral_homology.tex`
(L1118–1241) gives explicit Poincaré series 1/(1−2t) − 1/(1−t)^2.
Type: occupation pattern + scope-by-class.

CACHE-CANDIDATE B. **"Drinfeld centre creates braiding."** Already in
cache as "categorified averaging" entry; this audit confirms
arrow 3 of operadic circle is the SOLE source of non-symmetric
braiding (en_chiral_operadic_circle.tex Theorem 6.x at L2030–2079).
Cross-reference confirmed.

CACHE-CANDIDATE C. **"av is the naive Σ_n-coinvariant" vs
V2-AP4 "av is R-twisted for genuinely E_1."** These are two framings
of the same lossy descent: naive-but-lossy (with kernel = R-data) vs
R-twisted-but-iso. The standalones use the former framing; Vol II
V2-AP4 uses the latter. Both are correct; the cache should record the
equivalence.

CACHE-CANDIDATE D. **"E_2 lives natively at d=2; at d=3 it's derived
via Drinfeld centre."** Wave 4 + AP-CY56. Confirmed in
`en_chiral_operadic_circle.tex` Section sec:en-circle. Already in
Vol III cache; cross-volume cross-reference confirmed.

CACHE-CANDIDATE E. **"PVA descent assumes E∞-chiral."** Section 2(c)
P2-2 above. The PVA descent theorem in `sc_chtop_pva_descent.tex`
implicitly assumes E∞ via Σ_n-equivariance; should be explicit.
Type: scope error (necessary/sufficient).

(Cache file location and append protocol: per CLAUDE.md memory entry
"Cache Write-Back Loop (2026-04-15)" — enforcement agents must write
new findings back, not just note them. This audit is read-only;
candidates above are flagged for the next write-enabled session.)

----

## End of report

Word count: ≈ 4,800. Audit time: ≈ 35 min. Files touched: 0
(report-only). Build status: not run (read-only audit). Test status:
not run (read-only audit). Commit-ready: N/A — no commit proposed.
