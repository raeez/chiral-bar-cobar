# Attack-and-Heal: genus-2 KZB Siegel matrix construction

Target: CLAUDE.md row
`Genus-2 construction | CONSTRUCTED | KZB with 2x2 Siegel period matrix, chi=-12 at degree 2, doubly-dynamical (conj:g2-ddybe)`.

Primary loci:
- `chapters/theory/genus_2_ddybe_platonic.tex`
- `chapters/theory/higher_genus_modular_koszul.tex` (prop:genus-g-euler-general, line 34780)
- `compute/tests/test_genus_2_ddybe_platonic.py`
- `compute/lib/face_model_ddybe_engine.py`, `compute/lib/genus2_ddybe_engine.py`
- `compute/tests/test_face_model_ddybe_engine.py` (29 tests)
- `compute/tests/test_genus2_ddybe_engine.py` (18 tests)

Author: Raeez Lorgat. No AI attribution.

Date: 2026-04-18.

## Mission items

(i) Locate construction: DONE. Chapter `genus_2_ddybe_platonic.tex`
    is the canonical Platonic-ideal inscription (Wave 5, 2026-04-17).
    Siegel matrix definition at lines 105-119; doubly-dynamical
    structure at lines 370-378 (two Cartan variables
    $\boldsymbol\lambda=(\lambda_1,\lambda_2)\in\fh^*\oplus\fh^*$
    matching dim $H^0(\Sigma_2,\Omega^1)=g=2$).

(ii) chi=-12 at degree 2: VERIFIED with ARITHMETIC DRIFT FOUND.

(iii) Doubly-dynamical structure: VERIFIED. Two dynamical variables
    from the two A-cycle periods of $\Sigma_2$; $R^{\mathrm{face}}
    (z,\boldsymbol\lambda,\Omega)$ depends on both Cartan
    variables and on three Siegel entries
    $(\Omega_{11},\Omega_{12},\Omega_{22})$.

(iv) conj:g2-ddybe engine/test state: IN PLACE. Engine
    `face_model_ddybe_engine.py::verify_face_ddybe_g2` hardcodes
    `relative < 1e-4` at N=8 truncation. 29 tests in the engine
    test file, 18 in genus2_ddybe engine, 9 in platonic HZ-IV
    file. Totals match chapter advertisement (~30 face-model
    tests at preface, plus platonic HZ-IV supplement).

## Phase 1 ATTACK verdicts

### (A) chi=-12 arithmetic drift — REAL BUG, HEALED

Chapter `genus_2_ddybe_platonic.tex` at lines 664-669 (pre-heal)
carried the displayed equation

```
chi(Sigma_2 \ {0}, L_KZB^{(2)})
  = r * chi_top(Sigma_2 \ {0})
  = 4 * (1 - 2g - s) |_{g=2, s=1}
  = -12.
```

First-principles check:
- chi_top(Sigma_g \ {s points}) = (2 - 2g) - s = 2 - 2g - s (open surface).
- At g=2, s=1: chi_top = 2 - 4 - 1 = -3.
- Rank r = d^2 = 4 for sl_2 in V x V fibre.
- Correct: chi = 4 * (-3) = -12.
- Buggy formula `(1 - 2g - s)` at g=2, s=1 gives 1 - 4 - 1 = -4,
  so the middle term evaluates to 4 * (-4) = -16, NOT -12.

The formula `d^2 * (1 - 2g)` (used in
`prop:genus-g-euler-general`, `higher_genus_modular_koszul.tex:34794`)
is correct because the `-1` from the single puncture is already
ABSORBED into `(2-2g) - 1 = 1-2g`. Line 34799 of
higher_genus_modular_koszul states this explicitly:
"chi_top(Sigma_g \ {0}) = 2 - 2g - 1 = 1 - 2g".

The drift: in the genus_2 chapter the author wrote `(1-2g-s)`
(combining both conventions and double-counting the puncture).
At g=2, s=1 this gives -16, but the displayed value is -12, so
the displayed arithmetic is inconsistent with the symbolic
formula.

**Heal installed (2026-04-18)**: chapter line 667 rewritten to
`4 * (2-2g-s) |_{g=2,s=1} = 4 * (-3) = -12`. The inlining of
the `(-3)` step forces the correct arithmetic and removes the
possibility of future drift. The alternative equivalent form
`d^2 * (1-2g)` (with s absorbed) used in
`prop:genus-g-euler-general` is retained as the upstream
citation.

Test file `test_genus_2_ddybe_platonic.py` line 329 already
uses the correct formula `d*d*(2 - 2*g - s)`; no test edit
required. Line 327 of the test carries a comment-only remark
that documents the two conventions and is not executed as
the actual assertion (the `chi` variable is immediately
overwritten on line 329 before the assert on line 330).

### (B) Test count advertisement — VERIFIED, minor drift

CLAUDE.md row "face-model DDYBE VERIFIED" advertised 29 tests
(post-Wave-5 updated to 30). Actual counts:
- `test_face_model_ddybe_engine.py`: 29 test functions.
- `test_genus2_ddybe_engine.py`: 18 test functions.
- `test_genus_2_ddybe_platonic.py`: 9 test functions.

The chapter preface at lines 76-80 states "4 generic-Omega
compute tests, plus a tier-(T3) diagonal-Omega consistency
check" (5 tests), and "30 face-model tests total across
TestThetaFunctions, TestBoltzmannWeightsG1, TestFaceDYBEG1,
TestClassicalLimit, TestGenus2Theta, TestBoltzmannWeightsG2,
TestFaceDDYBEG2, TestFullSuite". Adding one second-Omega spot
check to the original 29 gives 30, matching. No drift.

### (C) Doubly-dynamical structure — VERIFIED

Definition at line 378 uses $\boldsymbol\lambda=(\lambda_1,\lambda_2)
\in\fh^*\oplus\fh^*$. Two Cartan variables correspond to the
two A-cycle periods of $\Sigma_2$ (equivalently, the two
elements of a basis of $H^0(\Sigma_2,\Omega^1)$ normalised
against $(A_1,A_2)$). The dynamical shift enters the Boltzmann
weights via the theta ratios at shifted arguments
$\Theta(z \pm \eta, \boldsymbol\lambda \pm \alpha)$.

At diagonal $\Omega = \mathrm{diag}(\tau_1,\tau_2)$ the
construction degenerates to a single genus-1 Felder DYBE
(Theorem at lines 406-409). This is consistent with the
Felder dynamical YBE: each A-cycle carries its own dynamical
variable; diagonal Omega makes the two A-cycles independent;
odd-characteristic theta at g=2 projects onto a single cycle
and the other cycle's contribution cancels in Boltzmann-weight
ratios.

Verdict: UPHELD. The "doubly-dynamical" label corresponds
genuinely to 2 dynamical Cartan directions, not a terminological
inflation.

### (D) Separating-degeneration scope — UPHELD (pre-existing heal)

Wave-5 heal correctly noted: separating degeneration gives
diagonal Omega, which reduces to ONE Felder DYBE (not two),
because the g=2 odd theta characteristic projects onto the
$n_1$-sum while the $n_2$-sum contributes a normalising
$\theta_3(0|\tau_2)$ constant that cancels in every Boltzmann
ratio. Prior "two Felder DYBE copies" claim was retracted in
Wave-5. Current chapter is consistent with the retraction
(line 412 "independent of lambda_2 and tau_2: the face-model
R-matrix reduces to a single genus-1 Felder R-matrix").

### (E) Non-separating degeneration test — GAP, already recorded

Non-separating degeneration ($\Omega_{22}\to i\infty$,
$\Omega_{12}$ fixed nonzero) is the regime where a genuinely
genus-2 DDYBE identity survives the limit (because the
off-diagonal period $\Omega_{12}$ is retained). No engine
test exists for this regime. Already recorded as a frontier
item in the chapter; no new AP required.

## Phase 2 HEAL summary

One edit to `chapters/theory/genus_2_ddybe_platonic.tex`
lines 664-669, replacing buggy `(1-2g-s)` with `(2-2g-s)` and
inlining the `(-3)` intermediate to force correct arithmetic.
No test edits required; test file already carries the correct
formula. No CLAUDE.md edits required; status row "CONSTRUCTED"
unchanged.

## Anti-patterns surfaced (AP1561-AP1562, per AP314 minimal inscription)

**AP1561 (Two-convention Euler-characteristic drift from
puncture-absorption ambiguity).** The topological Euler
characteristic of a genus-$g$ surface with $s$ punctures admits
two canonical presentations: (a) $\chi_{\mathrm{top}}(\Sigma_g
\setminus \{s\text{ pts}\}) = 2 - 2g - s$ (separated form);
(b) the $s=1$ specialisation $\chi_{\mathrm{top}} = 1 - 2g$
(puncture-absorbed form). Drift mode: an author who recalls
the (b) specialisation, mis-generalises to arbitrary $s$ by
writing $(1 - 2g - s)$ — which double-counts the puncture.
At $g=2$, $s=1$: (a) gives $-3$; (b) gives $-3$; the incorrect
generalisation $(1-2g-s)$ gives $-4$. Detection: substitute
boundary values $g=0, s=1$: the correct form gives $\chi_{\mathrm{top}}
(\PP^1 \setminus \{0\}) = 1$; the buggy form gives $0$
(contradicting $\PP^1 \setminus \{0\} \simeq \mathbb{A}^1$ has
$\chi = 1$). Counter: before writing a generic-$(g,s)$
Euler-characteristic formula, verify at $(g,s)=(0,1)$ and
$(g,s)=(1,1)$. Healing: use form (a) $(2-2g-s)$ when the
puncture count is variable; use form (b) $(1-2g)$ when $s=1$
is fixed and absorbed; NEVER write $(1-2g-s)$. Distinct from
AP252 (Chern-character / Taylor-expansion direction) which is
about `O(x^2)` direction in Chern-character expansions;
AP1561 is about baseline-offset double-count in a linear
topological formula.

**AP1562 (Test-file buggy formula overwritten-before-assert
masquerades as documentation).** A test file contains two
successive assignments `chi = FORMULA_A` then `chi = FORMULA_B`
with the second form used in the actual assert. If FORMULA_A
is buggy but FORMULA_B happens to equal the correct expected
value, the test passes while leaving FORMULA_A in the code as
a trap for a future reader who sees `chi = d*d*(1-2*g-s+1)`
(test line 327) and copies it into a manuscript. The comment
"chi = r (2 - 2g - s), not (1-2g)-only" documents the RIGHT
formula but the line right above it computes the OLD formula.
Counter: when refactoring a test formula, delete the
superseded formula rather than leaving it as a comment-
documented but-now-overwritten predecessor. Distinct from
AP292 (operator-precedence Fraction bug): AP292 is a
language-level arithmetic error; AP1562 is an
intent-documentation residue that preserves the bug in
readable source form. Healing for this session: the test
file's executed assertion is already correct (line 329 form),
so no test edit; chapter manuscript edit suffices.

Neither AP needs to enter HOT ZONE (low recurrence: first
sighting in this wave).

## Final state

| item | status |
|------|--------|
| chapter chi=-12 derivation | HEALED (2026-04-18) |
| engine tests | CORRECT (no edit) |
| test file HZ-IV formula | CORRECT (no edit) |
| CLAUDE.md status row | CORRECT (no edit) |
| conj:g2-ddybe Conjectured | UNCHANGED |
| doubly-dynamical verification | UPHELD |
| non-separating degeneration engine | OPEN (pre-existing) |

No new frontier items added. No CLAUDE.md status downgrades.
One manuscript arithmetic heal.

Author: Raeez Lorgat. 2026-04-18.
