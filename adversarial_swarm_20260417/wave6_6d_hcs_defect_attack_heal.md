# Wave 6 — 6d hCS codim-2 defect attack / heal (2026-04-17)

## Target

Status-table claim in Vol I CLAUDE.md:

> "6d hCS defect PROVED: Codim-2 defect on $C \subset \mathbb{C}^3$:
> boundary algebra = $W_{1+\infty}$ with $\Psi = -\sigma_2$. $c = 1$
> (Sugawara). $N_{C/Y} = \mathbb{C}^2$ gives spectral params.
> 48 tests."

Primary files:

- `/Users/raeez/chiral-bar-cobar/standalone/cy_quantum_groups_6d_hcs.tex` (1268 lines) — the programme standalone. `prop:v3-qg-c3-defect` (line 405), `thm:wave14-codim2-defect` (line 1078), remark `rem:v3-qg-level-r-matrix` (line 443).
- `/Users/raeez/calabi-yau-quantum-groups/standalone/cy3_6d_hcs_w1inf_vol3.tex` (81 lines) — scaffold stub only; no proofs.
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/hcs_codim2_defect_ope.py` (666 lines) — engine.
- `/Users/raeez/calabi-yau-quantum-groups/compute/tests/test_hcs_codim2_defect_ope.py` (680 lines, **49** `def test_`).

## Phase 1 findings (first-principles attack)

### F1. Test count is stale

Status claim "48 tests"; actual count is **49** `def test_` in
`test_hcs_codim2_defect_ope.py`. One test was added post-metadata.
Not a correctness failure — a metadata-hygiene violation (manuscript
hygiene does not pressure test counts, but the theorem-status table
becomes false after every new test without census regen).

### F2. Zero HZ-IV decorators

The test file has **0** occurrences of
`derived_from / verified_against / disjoint_rationale /
@independently_verified / @verified_against`. Every
`ClaimStatusProvedHere` test must carry such a decorator per the
Independent Verification Protocol installed 2026-04-16 (Vol III
CLAUDE.md §HZ3-11, cross-linked in Vol I). Coverage snapshot at
installation: Vol III 2/283, Vol I 0/2275 — this claim sits in the
Vol I working queue and is NOT yet protected by honest
independent-verification decoration. Heal path: either (a) honest
HZ-IV decorators citing Costello 2017 + Prochazka-Rapcak
arXiv:1910.07997 + the $c_3\_lie\_conformal$ cross-engine; or (b)
downgrade the table entry to `ClaimStatusProvedHere (no HZ-IV)`
pending decoration; or (c) restrict scope to "OPE verified" only
(the Sugawara c=1 step and the J-J level coincide with engine
ground truth, so option (a) is the honest path).

### F3. Load-bearing convention bug: level $k=1$ vs. $\Psi$

`prop:v3-qg-c3-defect` proof (line 438-440) wrote:

> "the central charge is computed from the Sugawara construction for
> the $\fgl_1$ current at level $k=1$: $c=1$."

`rem:v3-qg-level-r-matrix` (line 443-457) then wrote:

> "$r^{\mathrm{Heis}}(z) = k/z = 1/z$ at level $k = 1$."

This is inconsistent with the engine. `hcs_codim2_defect_ope.py:188`
fixes `r(z) = \Psi/z` with $\Psi = -\sigma_2(h_1, h_2, h_3)$, not
$k = 1$. The Heisenberg OPE derived from 6d is
$J(z)J(w) \sim \Psi/(z-w)^2$ (engine line 82, 239-244); the Sugawara
$T = (1/(2\Psi)):J^2:$ gives $c = 1$ for **every** nonzero $\Psi$,
not specifically $\Psi = 1$. Writing "level $k=1$" conflates the
rank-of-the-boson ($N=1$) with the 6d-derived level
($\Psi \ne 1$ generically, e.g. at SV N=2 point $(1,-2,1)$ we have
$\Psi = 3$ — see test line 21).

This is a genuine PE-1/AP126 load-bearing formula error: the
r-matrix level prefix was being asserted as `k=1`, making the
$k = 0$ check trivially meaningless (the 6d r-matrix only vanishes
at $\sigma_2 = 0$, a different locus from $k = 0$).

### F4. Ψ convention not anchored to Prochazka-Rapcak

Prochazka-Rapcak (arXiv:1910.07997, 1807.11304) parametrise
$\cW_{1+\infty}$ by three complex parameters
$(\lambda_1, \lambda_2, \lambda_3)$ with constraint
$\sum_i 1/\lambda_i = 0$; the projective "coupling" they use is a
ratio (variants: $\Psi_{PR} = -\lambda_2/\lambda_1$, or the
triality-covariant combination). The claim $\Psi = -\sigma_2$ is
INTERNALLY consistent (engine verifies at test points
$(1,0,-1) \to \Psi = 1$, $(1,-2,1) \to \Psi = 3$) but the reader is
not told how $-\sigma_2$ relates to $\lambda_i$ of Prochazka-Rapcak.
Heal: explicit bridge statement $\lambda_i^{-1} \propto h_i$ and
note that $\Psi = -\sigma_2$ fixes a normalisation consistent with
Costello's 6d action.

### F5. c = 1 is N-dependent, scope was implicit

Engine line 202-210: $c = N$ in general, not $c = 1$. The 6d theory
with $\fgl_1$ gauge gives $N = 1$, hence $c = 1$. The original
manuscript proof stated "$c=1$" without making $N=1$ explicit.
Heal: state `N=1` explicitly.

### F6. Cohomological vs chain-level scope (AP-TOPOLOGIZATION)

`thm:wave14-codim2-defect` (line 1078) already carries the
qualifier "cohomological, not chain-level, in class M" (line 1103),
consistent with AP-TOPOLOGIZATION. The earlier
`prop:v3-qg-c3-defect` proof sketch (line 420) does NOT state this
scope. Status-table claim "PROVED" is therefore
cohomological-scope; the Wave-14 addendum makes this explicit; the
main proposition did not. Not load-bearing once Wave-14 is read,
but a scope-inflation risk at the table line.

### F7. Toroidal global scope (AP-CY claim)

`rem:wave14-toroidal-global` (line 1152) is explicit: global
$\mathbb{P}^1 \times \mathbb{P}^1$ extension is CONDITIONAL on
class-M chain-level topologisation. Status-table phrasing "toroidal
chiral QG" in the wider Vol III theorem status table should
distinguish formal-disc (PROVED) from global (CONDITIONAL). Vol III
CLAUDE.md theorem-status table already does: "Toroidal chiral QG:
PROVED formal-disk via DIM + SV CoHA; global P¹×P¹ conditional on
class-M chain-level". Consistent.

### F8. $N_{C/Y} = \mathbb{C}^2$ gives TWO spectral parameters

Claimed: normal bundle of rank 2 produces two spectral parameters.
First-principles check: for $C = \mathbb{C} \subset \mathbb{C}^3$,
$N_{C/Y} = \mathcal{O} \oplus \mathcal{O}$ is trivial rank-2;
$H^0(C, N_{C/Y}) = \mathbb{C}[z]^{\oplus 2}$ is infinite-dimensional.
The TWO spectral parameters come from the FIBER of $N_{C/Y}$
(a rank-2 $\mathbb{C}$-vector space) via the
$\Omega$-background eigenvalues $(h_1, h_2)$ on the two normal
coordinates — NOT from $H^0$. This is what the text says (line 386
"the normal bundle supplies two spectral parameters from the two
fiber coordinates") — correct. The attack asking "why not
infinitely many" conflates normal bundle sections with normal
bundle fibers; the text is careful here.

### F9. Primary literature chain

Costello 2017 (ref [5] in standalone); Costello-Witten-Yamazaki
(ref [6]); Prochazka-Rapcak arXiv:1910.07997; Schiffmann-Vasserot
(ref [7]); Rapcak-Soibelman-Yang-Zhao (ref [8]). All cited. The
Wave-14 addendum (line 1106-1121) correctly installs the
Prochazka-Rapcak positive-half correction
$\CoHA(\mathbb{C}^3) \simeq Y^+(\widehat{\fgl_1})$ rather than the
earlier folklore $\CoHA = \cW_{1+\infty}$ (which is a character
coincidence).

### F10. Cross-volume placement

Vol I programme-level standalone is the substantive document
(1268 lines, all proofs). Vol III standalone is an 81-line scaffold.
Per AAP2, the substantive Vol I standalone is the canonical source;
Vol III scaffold correctly points to it (line 69-71 of Vol III
stub). Vol II has no duplicate 6d hCS theorem; celestial/UCH
mentions 6d hCS only as motivation.

## Phase 2 heals applied

### H1 (in file): fix `prop:v3-qg-c3-defect` proof and
`rem:v3-qg-level-r-matrix`

Load-bearing edit to
`/Users/raeez/chiral-bar-cobar/standalone/cy_quantum_groups_6d_hcs.tex`
lines 435-457:

- Proof: stated Sugawara as
  $T = (1/(2\Psi)):J^2:$ applied to level-$\Psi$ Heisenberg, yielding
  $c = 1$ for every nonzero $\Psi$; stated explicitly that $N = 1$
  (rank-1 boson), with $c = N$ in general; removed the false "level
  $k = 1$" phrasing.
- Remark: replaced $r^{\mathrm{Heis}}(z) = k/z = 1/z$ with
  $r^{\mathrm{Heis}}(z) = \Psi/z = -\sigma_2/z$; added the
  $\Psi = 0$ degenerate-locus diagnostic in place of the
  meaningless "$k = 0$ vanishing" (the 6d r-matrix vanishes at
  $\sigma_2 = 0$, not at $k = 0$); added Prochazka-Rapcak
  $\lambda_i$ bridge.
- Commented-out AP tags removed from the in-text `%` comment block
  per manuscript-metadata hygiene.

### H2 (not applied in this wave): test-count + HZ-IV

- Metadata refresh required: status table says "48", reality is
  "49". Do not silently sync; trigger census regeneration in a
  dedicated pass.
- HZ-IV decorator installation for the 49 tests (Vol I working-queue
  advancement). Candidate disjoint sources:
  - Costello 2017 preprint (6d hCS level formula) vs
    `c3_lie_conformal.py` SN-bracket computation.
  - Prochazka-Rapcak Miura factorisation (independent of bar).
  - FMS / Feigin-Frenkel free-field realization of
    $\cW_{1+\infty}$ (independent of 6d derivation).

### H3 (table diagnostic, not in file): cohomological scope

Theorem-status table entry for "6d hCS defect" should read
"PROVED cohomological; chain-level in class M conditional
(AP-TOPOLOGIZATION)". Currently the table entry reads "PROVED" with
the scope qualifier only in the file (line 1101-1103). Decoration
debt.

## Residual open items (frontier)

- HZ-IV decoration for the 49 tests (Vol I working queue).
- Chain-level class M topologisation of the $\cW_{1+\infty}$ defect
  algebra (inherited from general AP-TOPOLOGIZATION).
- Bridge theorem $\Psi = -\sigma_2 \leftrightarrow$ Prochazka-Rapcak
  $(\lambda_1, \lambda_2, \lambda_3)$ to make the conversion
  quotient-of-homogeneous-coordinates explicit (scope: a lemma, not
  a theorem).

## Verdict

The theorem is **substantially correct** at the cohomological level
as inscribed in the Wave-14 addendum. The earlier
`prop:v3-qg-c3-defect` body carried a convention bug (level $k=1$
vs $\Psi = -\sigma_2$) now healed. Test-count drift (48 → 49) and
zero-HZ-IV-coverage are verification-protocol debt, not
mathematical debt. The "PROVED" status is appropriate at
cohomological scope with the Wave-14 positive-half correction to
$\CoHA(\mathbb{C}^3) = Y^+$ (not the full $\cW_{1+\infty}$).

Do not commit in this session.
