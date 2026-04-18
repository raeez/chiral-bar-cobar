# Wave-2 attack-and-heal: Vol III mock modular K3 (d=2) + κ_BKM(Φ_N) universality

**Date:** 2026-04-18
**Channel:** Beilinson adversarial (Etingof / Polyakov / Kazhdan / Gelfand /
Nekrasov / Kapranov / Bezrukavnikov / Costello / Gaiotto / Witten).
**Targets:**

- `rem:mock-modular-k3` at `chapters/examples/k3e_cy3_programme.tex:509-549`.
- `thm:kappa-hodge-supertrace-identification` at `cy_d_kappa_stratification.tex:177`.
- `thm:borcherds-weight-kappa-BKM-universal` at `cy_d_kappa_stratification.tex:1152`.
- `thm:kappa-stratification-by-d` at `cy_d_kappa_stratification.tex:402`.
- `compute/lib/kappa_bkm_universal.py` + `compute/tests/test_kappa_bkm_universal.py`.

---

## 1. Attack ledger

### A1 (Zwegers decomposition scope, rem:mock-modular-k3)

The "machine-precision $\sim 5.7 \times 10^{-16}$" verification at line 545 is
nominally of equation~\eqref{eq:mock-modular-decomposition}
$Z_{K3}(\tau,z) = (h(\tau) - 24\mu(\tau,z)) \cdot \vartheta_1^2/\eta^3$.
The prose claim that "the polar term
$h|_{q^{-1/8}} = -2 = -\kappa_{\mathrm{ch}}(\cA_{K3})$" appears via
Appell--Lerch cancellation is a LOW-ORDER reading: the remark verifies the
decomposition as a formal identity of holomorphic-plus-mock forms, but the
mock-modularity content (shadow $S(\tau) = 24\,\eta(\tau)^3$) is not itself
checked. AP245 three-level agreement: the decorator path consistent with
manuscript prose would be (statement) Zwegers μ-decomposition → (engine)
Fourier coefficient extraction of $h(\tau)$ on ≥5 coefficients against
Eguchi--Ooguri--Tachikawa 2010 Table / Gannon 2016 proof → (cross-check)
shadow $S(\tau) = 24\eta^3$ verified weight-3/2. No engine currently runs
the mock-modular shadow equation independently; the polar-coefficient match
$A_0^{\mathrm{full}} = -2$ is the only numerical bridge. **Not a falsification,
but a SCOPE restriction**: the Zwegers identification at this inscription
level is correct at the polar coefficient and on the single displayed
identity, not at the full shadow level.

### A2 (`thm:kappa-hodge-supertrace-identification`, proof Step 1)

The proof cites `thm:hkr-cy` for the HKR decomposition and
`prop:serre-duality-cy` for the Mukai pairing as inputs. Neither inscription
is load-bearing with a local proof body: both are cited, not inscribed, in
this file. **HZ-11 adjacency**: if `thm:hkr-cy` resolves to an inscribed
Vol III theorem, ProvedHere is permissible; if it resolves cross-volume
(Vol I or folklore), the present theorem inherits cross-volume scope and
must downgrade clause to `\ClaimStatusConditional` or inscribe HKR locally.
The argument at Step 2 "the $r$-matrix on $\cA_X$ is the Mukai pairing"
is asserted, not derived. For compact CY$_d$ at $d = 2$ the Mukai pairing
is standard; for $d \geq 3$ the chiral-algebra $r$-matrix on $\cA_X$
is itself an output of $\Phi_d$, which is conjectural at $d \geq 3$
(CY-A$_3$ conjecture). So the theorem is PROVED at $d = 2$, CONDITIONAL
on CY-A$_d$ for $d \geq 3$. The text "unconditional identity at generic
parameters of $\Phi$" understates this scope.

### A3 (κ_BKM universality, `thm:borcherds-weight-kappa-BKM-universal`)

Claim in statement: $N \in \{1, 2, 3, 4, 6\}$ (FIVE Borcherds families).
Engine `diagonal_siegel_cy_orbifolds.py` `FRAME_SHAPE_DATA` carries EIGHT
orbifolds $N \in \{1, \ldots, 8\}$. The theorem statement restricts to
five, the engine covers eight; the proof body at line 1213 states
"$c_2(0) = 8$, $c_3(0) = 6$, $c_4(0) = 4$, $c_6(0) = 2$" — four values, not
the five the statement advertises. The statement's
"$N \in \{1, 2, 3, 4, 6\}$" is correct (these five $N$ admit Siegel
paramodular forms with weight $c_N(0)/2 \in \Z$); $N \in \{5, 7, 8\}$
give weight $c_N(0)/2 \in \{2, 1, 1\}$ and appear in the engine but
correspond to Igusa / non-diagonal Sp(4,Z) quotients where the
"Borcherds family of orbifolds of $\mathrm{K3} \times E$" phrasing in
the statement is restrictive by convention. **AP270 multi-object row**:
CLAUDE.md Vol III κ_BKM claim advertises universal across $N \in \{1,2,3,4,6\}$
while the engine covers eight values. Neither claim is wrong; the
statement's five-family scope matches the Gritsenko--Nikulin paramodular
lineage, the engine's eight-family scope is the Frame-shape lineage.
They are complementary, not contradictory. Honest reading:
the theorem is PROVED at its stated five Siegel-paramodular families
via Borcherds Invent. Math. 1995 Thm. 10.1; the engine verifies the
formula $c_N(0)/2 = \mathrm{wt}(\Phi_N)$ on the extended eight-family
Frame-shape tabulation, consistent with the theorem.

### A4 (AP250 per-type uniformity)

The universality claim $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is
proved via Borcherds 1995/1998, which is universal for any
vector-valued theta lift satisfying the convergence hypothesis. At
$N = 1$ the cited primary source is Gritsenko 1999 $\Delta_5$ weight-5
paramodular of level 1. At $N \in \{2, 3, 4, 6\}$ the cited sources
are Gritsenko 1994 / Allcock 2000 / Gritsenko--Hulek--Sankaran 2008
(proof body line 1217). **Per-type verification is CITATION-complete**
for these four $N$ but not inscribed: the theorem's universality is
a uniform Borcherds-theorem application, not a case-by-case
inscription; the citations are the per-type anchors. AP250 is
satisfied at citation level.

### A5 (AP289 Künneth audit)

Single residual hit: `cy_d_kappa_stratification.tex:164` in the Wave-12
remark explicitly names the additive rule
$\Xi(X \times Y) = \Xi(X) + \Xi(Y)$ as FALSE (naive, coincides on
product entries with one factor $\Xi = 0$, diverges elsewhere; K3×K3
the multiplicative and additive values happen to coincide at $2 \cdot 2 =
4$ and $2 + 2 = 4$, K3×K3$^{[2]}$ diverges). This is a correct
inoculation, not a drift. Programme-wide grep on `.tex` shows no other
additive claim; CLAUDE.md entry is registry-only (permitted).

### A6 (AP239 K3 naming)

The K3 abelian Yangian / K3 chiral algebra naming is anchored in
rank-24 signature-(4, 20) even unimodular lattice + CY$_2$ constraint.
The "Mathieu moonshine" structure used in the mock-modular remark DOES
use K3-specific content: the $M_{24}$ representation theory of
$A_n^{\mathrm{full}} = 2\,a_n$ attached to K3 massive multiplicities is
K3-specific beyond lattice invariants (Eguchi--Ooguri--Tachikawa 2010,
Gannon 2016). The remark's internal claim
"bar complex does NOT detect $M_{24}$ directly: it detects
$\kappa_{\mathrm{ch}} = 2$ at degree 2" is an honest AP239 inoculation:
bar-complex visibility is through scalars (lattice + signature),
$M_{24}$-structure is an orthogonal internal symmetry.

### A7 (HZ-IV N=1 decorator disjointness, test file line 772-872)

The `TestIndependentVerificationN1` class verifies $c_0 = 10$ via two
paths: (DERIVATION) `FRAME_SHAPE_DATA[1].c_disc_0 = 10` (GHV 2010 Frame
shape); (VERIFICATION) `phi01_by_discriminant(D=0) = 10` from exact
theta-ratio (Eichler--Zagier 1985). **Disjointness check**: the GHV 2010
Frame-shape computation uses $M_{24}$ conjugacy-class character theory
applied to the untwisted sector; the Eichler--Zagier theta-ratio formula
computes the Fourier expansion of $\phi_{0, 1}$ independent of
$M_{24}$. Both yield $c(0) = 10$. No hidden shared lemma (Borcherds'
weight theorem itself is used only in Step 4 of the bridge, which is
post-verification). **HZ-IV PASS** for N=1. AP288 risk: the test body
does perform a genuine numerical cross-check (assert
$c_{\mathrm{theta}} = c_{\mathrm{frame}} = 10$), not a tautological
`assert True`. AP277 / AP287 PASS.

### A8 (HZ-IV $N \geq 2$ coverage gap)

The `TestEightOrbifoldVerification` class (lines 100-154) tests the
$N = 2, \ldots, 8$ values but sources BOTH the formula value
($c_N(0)/2$) AND the literature value (`borcherds_weight`) from
`FRAME_SHAPE_DATA[N]`, which hardcodes both. This is AP277: the test
asserts the formula holds where the formula is implicit in the data
tabulation (`borcherds_weight = c_disc_0 / 2` is LITERAL in the GHV
tabulation). **HZ-IV FAIL at $N \geq 2$**: no disjoint source. Healing:
either (a) compute $c_N(0)$ independently at $N = 2, 3, 4, 6$ from the
eta-product formula of `diagonal_siegel_cy_orbifolds.py` twined
elliptic genus, OR (b) restrict HZ-IV decorator to $N = 1$ and flag
$N \geq 2$ as AP287-primitive-tautology (acceptable: Borcherds 1995
Thm 10.1 IS the universality theorem; independent verification at each
$N$ is not available without redoing the theta-lift calculation from
Eichler--Zagier basis).

### A9 (AP283 formula-in-CLAUDE.md)

CLAUDE.md κ_BKM row reads "$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$
universal across $N \in \{1, 2, 3, 4, 6\}$; at $N = 1$ this gives
$\kappa_{\mathrm{BKM}}(\Phi_1) = 10/2 = 5$ via Gritsenko's $\Delta_5$
weight-5 paramodular form of level 1 (Gritsenko 1999)". Verbatim-matches
manuscript theorem. AP283 PASS.

---

## 2. Surviving core

**PROVED**:
(i) `thm:borcherds-weight-kappa-BKM-universal` at the stated five-family
scope $N \in \{1, 2, 3, 4, 6\}$ via Borcherds 1995 Inv. Math. Thm 10.1
+ Gritsenko 1994/1999. $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$.
(ii) `thm:kappa-hodge-supertrace-identification` at $d = 2$ unconditional;
at $d \geq 3$ conditional on CY-A$_d$ (the $\Phi_d$ functor).
(iii) `rem:mock-modular-k3` Zwegers μ-decomposition at the polar
coefficient and at the displayed decomposition identity (Eguchi--Hikami
2008, Dabholkar--Murthy--Zagier 2012). Polar
coefficient $-2 = -\kappa_{\mathrm{ch}}(\cA_{K3})$ is a
PROVED identification; the shadow-tower connection to the bar-complex
shadow is prose parallel only (honest inoculation at line 524-528).
(iv) `thm:kappa-stratification-by-d` at $d \in \{1, 2, 3, 4, 5\}$ for
the standard families inscribed in Vol III.

**CONDITIONAL / SCOPE-QUALIFIED**:
(v) $d \geq 3$ Hodge-supertrace identification depends on CY-A$_d$.
(vi) HZ-IV independent-verification coverage for $\kappa_{\mathrm{BKM}} =
c_N(0)/2$ is PROVED disjoint at $N = 1$ only; at $N \geq 2$ the test
body tautologically reads the formula-value from the same table as the
literature-value (AP277). This is an ENGINE-LEVEL gap, not a
mathematics-level gap: the theorem at $N \geq 2$ is still PROVED via
Borcherds; the HZ-IV decorator should restrict scope or be honestly
flagged AP287-primitive-by-theorem.

**CONJECTURAL**:
(vii) `rem:cy-strat-open-frontier` — non-product, non-toric, non-local
compact CY$_3$ outside the four Borcherds-lift orbifolds. The
stratification theorem's prediction $\Xi(X) = 0$ (via Serre) is
conjecturally $\kappa_{\mathrm{ch}}(\cA_X) = 0$ for every compact CY$_3$
in this class; verification awaits concrete $\Phi_3(D^b(\Coh(X)))$
construction on the Pfaffian CY$_3$ and Gross--Popescu family.

---

## 3. Heal plan

**H1 (A7 secondary).** Extend `TestIndependentVerificationN1` to a
second decorated test verifying the polar coefficient
$c_1(-1) = 1$ (convention) / $c_{K3}(-1) = 2$ of $\phi_{0,1}$ via a
third disjoint path: direct computation from the Kac--Wakimoto
$\widehat{\mathfrak{sl}(1|1)}$ character formula for the elliptic
genus of K3 (independent of both GHV Frame-shape and Eichler--Zagier
theta-ratio). **PRIORITY: medium.** Would close the N=1 HZ-IV three-path
menu.

**H2 (A8).** Restrict the `TestEightOrbifoldVerification` class's
HZ-IV claim to $N = 1$ (the only disjoint-sourced case) and add a
module-level `# HZ-IV-W8-B FLAG: $N \geq 2$ verification is
tautological-by-theorem (Borcherds 1995 Thm 10.1); honest omission per
AP287 primitive-by-construction pattern` comment. This makes the
tautology honest rather than hidden. **PRIORITY: high.**

**H3 (A2).** Restate `thm:kappa-hodge-supertrace-identification` with
explicit scope split:
- clause (i): $d = 2$ with $h^{1, 0} = 0$ → unconditional at Koszul-generic
  parameters; reduces to $\chi(\cO_X)$.
- clause (ii): $d \geq 3$ compact CY$_d$ → conditional on CY-A$_d$
  and generic $\Phi$ parameters.
Downgrade clause (ii)'s prose "unconditional identity at generic
parameters of $\Phi$" to explicit `\ClaimStatusConditional` at the
clause level, or add a scope remark at line 237-238. **PRIORITY: medium.**

**H4 (A3 cosmetic).** Rewrite proof body lines 1213-1214 to enumerate
ALL FIVE paramodular families ($N = 1, 2, 3, 4, 6$) rather than four
($N = 2, 3, 4, 6$) + $N = 1$ in a separate paragraph, to match the
statement's five-family scope and eliminate the prose gap. **PRIORITY:
low.**

**H5 (A1 strengthening).** Add a second HZ-IV decorator to
`rem:mock-modular-k3`: independent verification of the Eguchi--Hikami
2008 decomposition via the $\mu$-function recursion (Zwegers 2002
thesis Ch 1, Prop 1.5) computing the first five Fourier coefficients of
$h(\tau)$ against $A_n^{\mathrm{full}} = 2 a_n$ from Gannon 2016 Table 1
($a_1 = 45, a_2 = 231, a_3 = 770, a_4 = 2277, a_5 = 5796$). Currently
only the polar coefficient is verified. **PRIORITY: medium.**

**H6 (A6 inoculation upgrade).** No change needed: the K3 naming
inoculation at `rem:factor-2-is-kappa:570-576` and `rem:mock-modular-k3`
line 524-528 already handles AP239 honestly. The K3-specific
$M_{24}$ structure is invisible to the bar complex (PROVED negative);
the bar-complex detects only the lattice scalar $\kappa_{\mathrm{ch}} = 2$.

---

## 4. Commit plan

**No commits this session** (per user directive).

Suggested future commits once H1-H5 are drafted:
- Commit 1: H2 + H4 (engine-side scope restriction + cosmetic proof
  rewrite, self-contained single-file).
- Commit 2: H3 (theorem scope split, propagate cross-file `\ref` if any).
- Commit 3: H1 + H5 (two new HZ-IV decorators, one each on N=1 polar
  coefficient and mock-modular Fourier coefficients).

**Beilinson dictum check**: every heal converts "larger false" (tautological
HZ-IV claim / unqualified "unconditional") into "smaller true" (scope-restricted
disjointness / explicit $d$-conditional). No healing inflates.

---

## 5. APs triggered (new entries for notes/first_principles_cache)

- **Cache #228 (A1)**: mock-modular decomposition verification at
  machine precision on the formal identity level does NOT automatically
  verify the shadow-equation content. State which level is checked.
- **Cache #229 (A2 Step 2)**: "r-matrix on $\cA_X$ is the Mukai
  pairing" is chain-level at $d = 2$, conditional on $\Phi_d$ at
  $d \geq 3$. Always scope.
- **Cache #230 (A8)**: HZ-IV decorator over a parameterized family
  where the parameter-indexed data tabulation (FRAME_SHAPE_DATA) literally
  carries the formula's LHS and RHS as paired columns is AP277 by
  construction; restrict to disjoint-verified indices or flag
  HZ-IV-W8-B per AP287 primitive-by-theorem.
- **Cache #231 (A3)**: when a theorem statement names a finite family
  by enumeration (five Siegel paramodular N's), the proof body must
  enumerate the same finite set, not a subset minus the singled-out
  anchor case.

---

## 6. Next action

None this session. Hand off H1-H5 to future waves. H2 is highest
priority (engine-level honest scope flag), H3 next (clause-split scope
restriction), H5 (mock-modular HZ-IV strengthening), H1/H4 cosmetic.
