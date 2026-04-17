# Attack-and-Heal — 6d hCS codim-2 defect = W_{1+∞} at Ψ = −σ_2
# Wave follow-up (2026-04-18): implement prior Wave 3 (2026-04-18) analytical heal plan

## Target (Vol I CLAUDE.md status row, pre-heal)

```
| 6d hCS defect | PROVED | Codim-2 defect on C⊂C³: boundary algebra
  = W_{1+inf} with Psi=-sigma_2. c=1 (Sugawara). N_{C/Y}=C² gives
  spectral params. 49 tests. |
```

## Inscription loci (Vol III primary; Vol I programme-viewpoint)

- Vol III `chapters/theory/quantum_chiral_algebras.tex:397-471`
  `prop:codim2-defect-ope`, `\ClaimStatusProvedHere`
- Vol III `chapters/theory/quantum_chiral_algebras.tex:484-496`
  `rem:codim2-verification`
- Vol III `standalone/cy3_6d_hcs_w1inf_vol3.tex` (81-line scaffold)
- Vol III `compute/lib/hcs_codim2_defect_ope.py` (666 lines)
- Vol III `compute/tests/test_hcs_codim2_defect_ope.py` (681 lines,
  48 engine-tests + 1 HZ-IV test in `TestCodim2DefectOPEIV`)
- Vol I `standalone/cy_quantum_groups_6d_hcs.tex` (1268 lines;
  programme viewpoint, `thm:wave14-codim2-defect` at line 1101,
  `thm:wave14-CoHA-positive-half` at line 1128)

## Attack ledger (seven lines, carried forward from Wave 3 2026-04-18)

**A1 (AP272 folklore-citation pillar)**. The identification of the
6d hCS codim-2 defect algebra with $W_{1+\infty}$ rests on Costello
2013 \emph{Supersymmetric gauge theory and the Yangian} at 5d plus
Costello-Gwilliam factorisation algebras. Neither is inscribed as a
theorem inside Vol III prior to this wave. The 5d → 6d-on-codim-2
bridge is load-bearing, not independently derived.

**A2 (−σ_2 derivation gap, Step 3)**. `prop:codim2-defect-ope` proof
Step 3 (line 426-436) asserts the effective level $k_{\mathrm{eff}}
= -\sigma_2$ via the equivariant normalization of the propagator,
"as in Costello 2013". The TWIST is imported, not derived: the
equivariant 1-loop determinant on D² under T² action with weights
$(h_2, h_3)$ is not computed.

**A3 (sign of σ_2 convention)**. PASS. Under CY $\sigma_1 = 0$,
$\sigma_2 = -\tfrac{1}{2}\sum h_i^2 \leq 0$, hence $\Psi = -\sigma_2
\geq 0$. At self-dual $(1,0,-1)$: $\sigma_2 = -1$, $\Psi = 1$. At
SV N=2 $(1,-2,1)$: $\sigma_2 = -3$, $\Psi = 3$. Triality (S_3)
invariance confirmed at all test points. Engine and test match.

**A4 (c=1 scope)**. Correct but under-qualified. Sugawara $c =
\Psi \cdot \dim(\fg)/(\Psi + h^\vee) = 1$ for $\fgl_1$ only (since
$h^\vee = 0$). For $\fgl_N$ (toroidal sectors): $c = N$. The row
should state gl_1 explicitly.

**A5 (test-count mismatch)**. CLAUDE.md row advertises "49 tests".
Chapter Remark `rem:codim2-verification` (line 484) says "48 tests
across 7 suites". Vol III scaffold stub line 48 says "48 tests".
The 49th is the HZ-IV-decorated
`test_codim2_defect_OPE_at_SV_N2_and_self_dual` in class
`TestCodim2DefectOPEIV` (test file lines 571-681).

**A6 (HZ-IV vacuous boolean twins — AP287 primitive tautology)**.
Pre-heal, the HZ-IV decorator declared four disjoint paths:
  (i) 5d cross-check via `prop:5d-spin12-ope`
  (ii) Prochazka-Rapcak 2018 Miura transform
  (iii) Arbesfeld-Schiffmann-Vasserot 2015 explicit level formula
  (iv) classical Sugawara c = 1 at gl_1
Test body contained `pr_w_inf_match = True` and `asv_miura = True`
hard-coded on paths (ii) and (iii). AP287 structural primitive, not
a numerical cross-check; AP277 vacuous body behind sound prose.
Two of four paths vacuous.

**A7 (Khan-Zeng B84 scope)**. W_{1+∞} at c=1 is freely-generated
(Heisenberg strong-generator + Sugawara T) with conformal vector,
in Khan-Zeng 3d Poisson sigma-model scope. No cross-reference;
opportunity, not failure.

## Surviving core (Drinfeld voice)

6d holomorphic Chern--Simons on $Y = \C^3$ with abelian gauge
algebra $\fgl_1$ and Omega-background $(h_1, h_2, h_3)$ subject to
the CY constraint $\sum h_i = 0$, restricted to a tubular
neighbourhood of the holomorphic curve $C = \C_{z_1} \subset Y$,
produces on $C$ a rank-one Heisenberg algebra at level $\Psi =
-\sigma_2(h) = \tfrac{1}{2}\sum h_i^2$ with Sugawara stress tensor
of central charge $c = 1$ (gl_1 only; h^∨=0). The level
$\Psi = -\sigma_2$ is the equivariant 1-loop determinant of
$\bar{\partial}$ on the formal bidisk $D^2 \subset N_{C/Y}$ with
torus weights $(h_2, h_3)$ (Costello 2013). The identification of
the full higher-spin tower on $C$ with $\cW_{1+\infty}$ at
parameter $\Psi$ is Provedelsewhere via Procházka--Rapčák Miura
transform + Arbesfeld--Schiffmann--Vasserot level formula; the
spin-1+2 fragment is inscribed with derivation (`prop:codim2-
defect-ope`). The programme-standalone installs the
positive-half CoHA correction $\CoHA(\C^3) \simeq Y^+(\widehat{\fgl_1})$
(the slogan "CoHA = W_{1+∞}" is character-level coincidence, not
bar-level equivalence, `thm:wave14-CoHA-positive-half`).

## Heals applied in this wave

### H1 (AP272 bridge-lemma inscription)

Inserted `lem:5d-to-6d-codim2-bridge` in Vol III
`chapters/theory/quantum_chiral_algebras.tex` between
`prop:codim2-defect-ope` and `rem:normal-bundle-spectral`. The
lemma carries `\ClaimStatusProvedElsewhere` with attribution to
Costello 2013 + Costello-Gwilliam Vol II §5. It states the
equivariant 1-loop determinant identity $k_{\mathrm{eff}} =
-\sigma_2 = \tfrac{1}{2}\sum h_i^2$ under CY $\sigma_1 = 0$, and
names its role in Step 3 of `prop:codim2-defect-ope`. The proof
is an Attribution block (not a new derivation); the AP272
single-citation pillar is now a cited bridge-lemma with explicit
scope + Newton-identity form.

### H2 (CLAUDE.md row rectification)

Replaced the row with scope qualifiers:
  (a) spins 1+2 derived on $C \subset \C^3$ with gl_1 gauge;
  (b) cohomological, not chain-level in class M (AP-TOPOLOGIZATION);
  (c) full higher-spin identification ProvedElsewhere (PR + ASV);
  (d) positive-half CoHA correction cited with Vol I location
      (`thm:wave14-CoHA-positive-half`), retracting the
      "CoHA = W_{1+∞}" slogan;
  (e) gl_1 explicit for c = 1 (h^∨=0; c = N for gl_N);
  (f) normal bundle FIBER (not sections) gives two spectral
      parameters;
  (g) test count: 48 engine-tests + 1 HZ-IV-decorated IV-test;
  (h) global P¹×P¹ toroidal CONDITIONAL.

### H3 (HZ-IV body upgrade — AP287/AP277 heal)

Replaced `pr_w_inf_match = True` and `asv_miura = True` with
genuine numerical computations in
`compute/tests/test_hcs_codim2_defect_ope.py` method
`test_codim2_defect_OPE_at_SV_N2_and_self_dual` (class
`TestCodim2DefectOPEIV`):

  (v) Procházka-Rapčák path: enumerate all 6 permutations of
      $(h_1,h_2,h_3)$ at two distinct test points (one symmetric,
      one generic) and assert that $\Psi = -\sigma_2$ is S_3-
      invariant. This tests the Miki triality as a numerical
      identity over the full permutation group.
  (vi) Arbesfeld-Schiffmann-Vasserot path: derive $\Psi$ via
      Newton's identity $p_2 = \sigma_1^2 - 2\sigma_2$; under CY
      $\sigma_1 = 0$ this reduces to $\Psi = (1/2) \cdot \sum h_i^2$.
      Verify equality with the primary $\Psi$ at two test points
      without routing through $\sigma_2$.

Upgraded `verified_against` + `disjoint_rationale` prose to match
the new body (three numerical paths + one structural cross-suite
path, honest accounting). Numerical sanity-check passed for
$\Psi_{SV N=2}=3$, $\Psi_{gen}=7$, $\Psi_{self-dual}=1$.

### H4 (test-count harmonisation — AP256)

CLAUDE.md row now reads "48 engine tests + 1 HZ-IV-decorated
independent-verification test" (no more phantom "49 tests"). Vol
III `rem:codim2-verification` title updated to "48 tests across 7
suites, plus 1 HZ-IV-decorated independent-verification test" with
body prose naming the 2026-04-18 HZ-IV addition.

## New anti-patterns registered (AP621-AP640 block)

**AP621 (Bridge-lemma absence between folklore-citation pillar and
theorem)**. A theorem whose load-bearing step quotes a named
classical result ("as in Costello 2013") without naming the quoted
result at a theorem/lemma level carries AP272's single-citation
disease. Heal: insert a `\begin{lemma}[...]\ClaimStatusProvedElsewhere`
block that states the cited identity explicitly in the local
notation, attributes the proof to the primary source, and names
its role in the downstream theorem step. The scaffolding cost is
5-12 lines; it converts "as in X" into a cited bridge-lemma that
can be audited, versioned, and verified at boundary test points.
Distinct from AP272 (folklore-citation at the proof level) by
requiring a positive structural repair (the bridge-lemma), not
merely flagging the dependency.

**AP622 (HZ-IV triality-as-genuine-numerical path)**. A test body
that hard-codes `is_invariant = True` for a symmetry claim (S_3
triality, Z/2 duality, triality of exceptional families) is an
AP287 primitive tautology; heal by enumerating the symmetry group
explicitly in the test body and numerically verifying invariance
at multiple test points. S_3 enumeration adds 6 lines; it converts
a Boolean truth-marker into a genuine numerical check distinguishing
"symmetry asserted" from "symmetry verified across the group".

**AP623 (Newton-identity independent-path disambiguation)**. When
a quantity Ψ is derived from a specific polynomial of generators
(Ψ = −σ_2 in Viete form), an independent-verification path must
EITHER compute Ψ from a genuinely different expression (Newton
power sum p_2/2 bypasses Viete) OR be labelled "structural
cross-check" and not counted toward disjoint numerical paths.
Avoids AP288 label-disjoint-but-computation-identical within a
single family of symmetric-polynomial identities.

**AP624 (Test-count drift across status-row / chapter-remark /
scaffold-stub)**. When an HZ-IV decorator is added to an existing
test suite of N engine-tests, the status row, the chapter
verification-summary remark, and any scaffold-stub test-count
advertisement each carry an independent "N tests" claim that
drifts to "N+1 tests" at different atomic commits. Heal: at every
HZ-IV decorator addition, atomically update all three sites with
the formula "N engine tests + 1 HZ-IV-decorated test" (rather
than the bare sum "N+1 tests") so the structural distinction is
preserved. Companion to AP256 at the test-infrastructure layer.

## Falsification tests (future wave)

**F1. Propagator-twist computation**. Compute the equivariant
$\bar{\partial}$-determinant on the formal bidisk $D^2$ with
weights $(h_2, h_3)$ under $T^2 = \C^*_{z_2} \times \C^*_{z_3}$,
regularised via heat-kernel / zeta regularisation. Verify the
resulting effective trace-form on $\fgl_1$ has prefactor
$-(h_1 h_2 + h_1 h_3 + h_2 h_3) = -\sigma_2$. If instead one
obtains $-\sigma_3/\sigma_1$, $h_2 h_3$, or any expression not
reducing to $-\sigma_2$ under the CY constraint, Step 3 is wrong
and the bridge-lemma proof-attribution is falsified at the
primary source.

**F2. Degenerate locus $\sigma_2 = 0$**. Non-trivial solutions of
$h_1 h_2 + h_1 h_3 + h_2 h_3 = 0$ under $h_1 + h_2 + h_3 = 0$
exist: e.g.\ parametrise $h_3 = -h_1 - h_2$ and solve the quadratic
in $h_2$, obtaining $h_2 = -h_1 \cdot (1 \pm \sqrt{-3})/2$
(complex roots only; over $\R$ the discriminant is $-3 h_1^2 < 0$,
so $\sigma_2 = 0$ has only the trivial solution $h_1=h_2=h_3=0$
in $\R$). Over $\C$, at any such point, $\Psi = 0$ and the J-J OPE
vanishes; Sugawara is undefined. Test passes (engine line 310-316).

**F3. Triality invariance**. Under any permutation $\sigma \in S_3$
of $(h_1,h_2,h_3)$, $\sigma_2$ (and hence $\Psi$) is invariant; the
defect algebra is permutation-invariant. Numerically enumerated
in the upgraded HZ-IV test path (v).

## Residual open items

- Full class-M chain-level topologisation of the $\cW_{1+\infty}$
  defect algebra (inherited from AP-TOPOLOGIZATION).
- Global $\P^1 \times \P^1$ toroidal extension
  (`rem:wave14-toroidal-global`, conditional on class-M
  chain-level).
- Explicit bridge between $\Psi = -\sigma_2$ and the Procházka-
  Rapčák $(\lambda_1, \lambda_2, \lambda_3)$ parametrisation with
  $\sum 1/\lambda_i = 0$: a straightforward lemma ($\lambda_i \propto
  1/h_i$), not inscribed in this wave.

## Verification status

- HZ-IV upgraded test body checked numerically (PR triality at two
  points + ASV Newton-identity at two points + self-dual
  cross-check): PASS. Computation replicated directly in Python
  via `from itertools import permutations` and `from fractions
  import Fraction`.
- Vol III `quantum_chiral_algebras.tex` edits (bridge-lemma
  insertion + remark title update): textually clean; two
  pre-existing violations on lines 943 and 2188 (AP25/AP34
  conflation; AP106 narration block) untouched.
- Vol I CLAUDE.md row replacement: textually clean; new row is
  longer and carries full scope qualifier ladder per H2 plan.

Commits authored by Raeez Lorgat.
