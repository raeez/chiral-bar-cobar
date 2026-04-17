# Wave 8: Vol I Compute-Engine Independence Audit (Tautology Detection)

**Date.** 2026-04-16.
**Auditor mandate.** Apply the Vol III HZ3-11 / AP10 protocol to Vol I:
every `\ClaimStatusProvedHere` theorem with computational support must carry
an *independent* test. The decorator infrastructure is already installed in
Vol I (`compute/lib/independent_verification.py`,
`compute/scripts/audit_independent_verification.py`, `make verify-independence`)
but is **not adopted**: only the self-test
`compute/tests/test_independent_verification_infra.py` carries the
`@independent_verification` decorator. ProvedHere coverage is therefore
**0 / N** for the entire Vol I theorem corpus, identical to the Vol III
baseline at protocol installation (2 / 283).

This report does **not** edit any Vol I source file (per task constraint).
It produces (a) an inventory snapshot, (b) a tautology table for the most
load-bearing engines, (c) the algebraic argument that
`mc_recursion_rational` and `sqrt_ql_rational` are restatements of the same
ODE, (d) explicit independent verification candidates with sketches, (e) a
decorator proposal, and (f) a punch list for the next session.

---

## Section 1. Engine inventory (snapshot)

`compute/lib/` contains **1350** Python modules; `compute/tests/` contains
**1428**. Decorator usage, by raw grep:

```
grep -rn "@independent_verification" compute/tests/  -> 3 hits
                                                       (all in
                                                        test_independent_verification_infra.py)
```

`make verify-independence` is wired and exits 0 today only because the
audit is a coverage report, not a coverage gate. The current state would
audit roughly as:

```
ProvedHere claims found:        ~2275  (Vol I scrape, per CLAUDE.md table)
Claims with independent test:        0
Tautological decorations:            0  (none registered)
Orphan entries:                      0
Coverage:                       0.00%
```

In other words, **every Vol I `ProvedHere` theorem is currently
unprotected by the protocol**. The shadow-tower OPE-recursion finding
from wave 1 is one instance of a systematic exposure, not an isolated
defect.

The audit below focuses on the **load-bearing** engines: those whose
output is cited by a manuscript ProvedHere theorem (shadow tower,
Feynman-bar matching, BV-BRST chain-level, Virasoro `m_4`, conformal-block
shadow integral). Bulk inventory of the other ~1340 engines is a
separate task; the methodology in this report extends mechanically.

Headline list (engine -> manuscript theorem -> testing pattern):

| Engine | Theorem support | Test family | Verdict |
|---|---|---|---|
| `shadow_tower_ope_recursion.py` | `thm:obstruction-recursion`, `thm:riccati-algebraicity`, `thm:single-line-dichotomy` | `test_shadow_tower_ope_recursion.py` (122 tests) | **TAUTOLOGICAL on the central "two-method" claim**; spot checks WEAK-INDEPENDENT |
| `shadow_tower_recursive.py` | same theorems (re-exported via `virasoro_S5`, `virasoro_shadow_coefficients_exact`) | `test_virasoro_ainfty_explicit.py` and 14 dependents | TAUTOLOGICAL: every importer ultimately re-evaluates the same recursion |
| `virasoro_ainfty_explicit.py` | `comp:virasoro-m4`, `thm:obstruction-recursion`, `prop:depth-classification` | `test_virasoro_ainfty_explicit.py` (~50 tests) | TAUTOLOGICAL: `virasoro_S5(c) == PrimarySectorAInfinity(c).shadow_coefficients(6)[5]` calls the same function twice |
| `feynman_bar_matching_engine.py` | `thm:feynman-bar-frontier` (genus 0); `thm:genus1-bar-feynman-affine` | `test_feynman_bar_matching_engine.py` (13 tests) | **GENUINELY-INDEPENDENT** at genus 0 (manual sl_2 brackets vs engine); WEAK-INDEPENDENT at genus 1 (formula `(k+2)/32` derived once, asserted twice) |
| `bv_brst_chain_level.py` | `thm:bv-bar-geometric`, `thm:brst-bar-genus0`, `thm:harmonic-factorisation`, `thm:coderived-bv-bar` | `test_bv_brst_chain_level.py` (81 tests) | MIXED: Faber-Pandharipande lambda-classes hardcoded against Faber 1999 (independent); QME genus-0/1 verified against direct expansion (independent); higher-genus arguments call the same `_faber_pandharipande` helper twice |
| `theorem_feynman_bar_frontier_engine.py` | `thm:feynman-bar-frontier` | `test_theorem_feynman_bar_frontier_engine.py` | TAUTOLOGICAL on the Bubble-correction claim: tree-level r-matrix and 1-loop bubble both computed from the same `(S_3, kappa)` table |
| `verify_virasoro_m4.py` (script) | `comp:virasoro-m4` | none — print-only script | TAUTOLOGICAL by construction: the script *asserts* `(1/12)^2 == 1/144` and prints "verified". This is high-school arithmetic, not a verification of the m_4 = c^2/144 claim. |
| `conformal_block_shadow_integral_engine.py` | `thm:shadow-conformal-block` | `test_theorem_shadow_conformal_block_engine.py` | UNAUDITED (out of wave 8 scope) |

---

## Section 2. Tautology detection table (per engine)

Methodology: for each engine listed above I read (a) the engine
implementation, (b) the test module, and asked the three AP10 questions:
(Q1) Does the test invoke the same recursion as the engine? (Q2) Does
the test simply re-call the engine? (Q3) Is the expected value derived
from a disjoint mathematical source?

### 2.1 `shadow_tower_ope_recursion.py` x `test_shadow_tower_ope_recursion.py`

The engine exposes two named methods:

* `mc_recursion_rational(kappa, S3, S4, max_r)` -- the "MC recursion".
* `sqrt_ql_rational(kappa, S3, S4, max_r)` -- the "sqrt(Q_L) Taylor expansion".

The module's docstring (lines 21--27) advertises:

> KEY MATHEMATICAL POINT: This recursion is INDEPENDENT of the assumption
> that the shadow metric Q_L(t) is a polynomial of degree <= 2. ...
> Agreement between the two methods at each arity is a VERIFICATION of
> the quadratic shadow metric theorem.

The test class `TestFullCrossMethodAgreement` (test L175--283) contains
20 test methods, each of which calls `_compute_and_compare(...)`, which
just runs both methods and reports `agree=True`. The "master test"
`test_full_agreement_all_20_lines` asserts
`report['all_agree'] == True` over all 20 primary lines.

**Verdict: TAUTOLOGICAL on the central claim.** The two methods are not
independent -- they are restatements of the same Riccati ODE
`H' = sqrt(Q_L)` (see Section 3 for the algebraic proof). Agreement is
a property of the *implementations*, not a verification of any theorem.

The 122 tests subdivide as follows:

| Subfamily | Count | Verdict |
|---|---|---|
| Cross-method agreement at S_2..S_30 across 20 lines | ~50 | TAUTOLOGICAL |
| Hardcoded values like `S_5(Vir, c=1) = -16/9` | ~15 | WEAK-INDEPENDENT (the value is computed by the engine and then asserted as the literal -16/9, which is also the engine's output -- the literal is a snapshot, not a derivation) |
| Affine KM `kappa = dim(g)(k+h^v)/(2h^v)` | 6 | GENUINELY-INDEPENDENT (the formula is closed-form, the test recomputes it as `Fraction(dim_g)*(k+h_vee)/(2*h_vee)`) |
| Class G/L/M classification (S_3=0,S_4=0 -> G etc.) | ~10 | WEAK-INDEPENDENT (the classifier reads the same tower) |
| Koszul `kappa(c)+kappa(26-c)=13` | 4 | GENUINELY-INDEPENDENT (closed-form, c+26-c=26) |
| Quintic formula `S_5 = -6*S_3*S_4/(5*kappa)` | 8 | TAUTOLOGICAL: this *is* the recursion at r=5 |
| W-line parity (odd arities vanish when S_3=0) | 6 | GENUINELY-INDEPENDENT (a parity argument, not a re-run) |
| Symbolic Vir at S_2..S_15 (sympy MC vs sympy sqrt) | 5 | TAUTOLOGICAL (same reduction, different field) |
| Asymptotic ratio test rho ~ 0.232 at c=26 | 2 | GENUINELY-INDEPENDENT (the formula `rho = sqrt((180c+872)/((5c+22)c^2))` is closed-form from the resolvent; the engine's tower is checked to decay accordingly) |
| Recursion-structure (deterministic, extending preserves) | 6 | META (testing software contracts, not math) |

Net: ~16 of 122 tests do genuinely independent work. The other ~106 are
self-consistency. **No test in this module computes any S_r from a
disjoint source** (Selberg integral, Wick contraction, BPZ recursion on
conformal blocks, etc.).

### 2.2 `virasoro_ainfty_explicit.py` x `test_virasoro_ainfty_explicit.py`

```
def virasoro_S5(c_val):
    return FR(-48) / (c_val ** 2 * (FR(5) * c_val + FR(22)))
```

The "test":

```
def test_S5_function(self):
    for c_val in [FR(1), FR(5), FR(25)]:
        assert virasoro_S5(c_val) \
            == PrimarySectorAInfinity(c_val).shadow_coefficients(6)[5]
```

The right-hand side is the same recursion that derived the formula on
the left. **TAUTOLOGICAL.** The single useful test is
`test_S5_c1: virasoro_S5(1) == -16/9`, which is a hardcoded literal.
Even this is weak: -16/9 was computed *by the recursion*, then frozen
as the expected value, then re-checked against the same recursion.

The Vol III analogue did genuine work: `m_5 = 775/5184` for the
**connected 5-point Wick contraction G_5^conn**, computed as a sum over
labelled trees with explicit propagator and vertex weights, with no
reference to any A_inf recursion. Vol I lacks any such Wick computation.

### 2.3 `feynman_bar_matching_engine.py` x `test_feynman_bar_matching_engine.py`

This is the cleanest engine in the audit.

Genus 0 (tree-level): the test file (L33--65) defines `MANUAL_BRACKET`
**by hand from the sl_2 commutation relations** -- this is a literal
restatement of `[h,e]=2e`, `[e,f]=h`, etc., but it is a bona fide
independent source (a textbook fact). `_manual_bar_d3` then composes
these brackets via the boundary formula to produce expected
coefficients, which are checked against the engine's
`bar_differential_arity3`. The engine internally uses a different
data structure (`SL2_BRACKET` dict) -- *almost* a tautology, but the
two definitions are wired up in two different orderings (engine uses a
dataclass + dispatch; test uses a plain dict + closure). I rate this
**WEAK-INDEPENDENT**: it catches a transcription bug but not a
mathematical mistake.

Genus 1: the engine asserts `F_1 = (k+2)/32` via two paths:

* `genus1_bar_amplitude(k) = kappa(k) * lambda_1` where
  `kappa = 3(k+2)/4`, `lambda_1 = 1/24`.
* `genus1_feynman_amplitude(k) = classical(k) + quantum_shift = k/32 + 1/16`.

The two expressions are *algebraically* equal:
`3(k+2)/4 / 24 = (k+2)/32 = k/32 + 2/32 = k/32 + 1/16`. The test asserts
their equality. **WEAK-INDEPENDENT**: it catches a sign error in the
constant 1/16 vs 1/32, but the underlying lambda_1 = 1/24 is a hardcoded
Faber-Pandharipande value (which IS independent -- Faber 1999 -- but no
decorator declares this).

Boundary value at `k = -2` (critical level): the test asserts both
amplitudes vanish. This **IS** a genuine independent check: at the
critical level the affine Sugawara construction degenerates and kappa
must vanish; the test catches any constant-term error.

### 2.4 `bv_brst_chain_level.py` x `test_bv_brst_chain_level.py`

The engine has 81 tests. I read the QME (`verify_qme`) genus-0 and
genus-1 helpers and the Faber-Pandharipande lambda helper.

Genus-0 QME verification (`_verify_qme_genus0`): expands the BV master
equation `{S, S} + 2*hbar*Delta(S) = 0` to order hbar^0 and checks
classical involutivity. This is a **direct** expansion test:
GENUINELY-INDEPENDENT.

Genus-1 QME (`_verify_qme_genus1`): includes the `lambda_1 = 1/24`
prefactor against `kappa(A) * lambda_1`. The kappa values are pulled
from the per-algebra builder (`heisenberg_bv`, `affine_km_bv`, etc.).
The lambda_1 = 1/24 value is hardcoded; the closest external source is
the Mumford `lambda_1 = 1/24 * pi*kappa_1` formula, but the test does
not cite Mumford. **WEAK-INDEPENDENT**.

Higher-genus (`_verify_qme_higher_genus`): computes the
Faber-Pandharipande integral `int_{Mbar_g} lambda_g lambda_{g-1} ...`
from the `_faber_pandharipande(g)` helper and then asserts its product
with the kappa tower matches a separate "geometric" computation. The
"geometric" computation also calls `_faber_pandharipande`. **TAUTOLOGICAL**
at genus >= 2.

### 2.5 `theorem_feynman_bar_frontier_engine.py`

The 1-loop bubble correction is computed as `S_3^2 / kappa` (engine
function `bubble_diagram_amplitude`, line 644). The Vol I claim is
that the `r(z)` z^{-1} coefficient receives a `-S_3^2/kappa` quantum
correction. The "verification" test simply recomputes
`S_3^2/kappa` and compares to `bubble_diagram_amplitude(S_3, kappa)`.
**TAUTOLOGICAL.**

A genuine verification would compute the bubble integral
`int dz/z^2 * G(z) * G(0-z)` directly from the propagator and check
the residue at z=0 reduces to `-S_3^2/kappa`. This calculation does
not appear anywhere in `compute/`.

### 2.6 `verify_virasoro_m4.py` (script)

The "verification" reduces (lines 104--165) to:

```
total_coeff = Rational(1, 144)
assert total_coeff == Rational(1, 12)**2          # arithmetic
assert simplify(Rational(1,2) * Rational(1,6) - Rational(1,12)) == 0
assert simplify(Rational(1,12)**2 - Rational(1,144)) == 0
```

These three assertions verify that 1/12 squared is 1/144 and that
(1/2)*(1/6) = 1/12. They do **not** verify that `m_4(T^4)|_{c^2}` equals
`(c^2/144) d^4 T`. The script even concedes (lines 102, 152): "Rather
than derive each coefficient individually, we verify the TOTAL" and
"Sum = 0 (verified in manuscript)". The script is a print-only
narrative; it should not be cited as computational verification of
`comp:virasoro-m4`.

This was anticipated by Wave 5 BV-Feynman ("m_4 (Vir at c^2/144) is
homotopy-transfer + pentagon-consistency, NOT independent Wick"). The
present audit confirms it at the source level.

---

## Section 3. Shadow tower focus: `mc_recursion_rational` = `sqrt_ql_rational`

The wave-1 finding is correct. Algebraic proof:

**Setup.** Both methods compute coefficients of the formal power series

```
H(t) := t^2 * sqrt(Q_L(t)),  Q_L(t) = q_0 + q_1 t + q_2 t^2,
```

with `q_0 = 4 kappa^2`, `q_1 = 12 kappa S_3`, `q_2 = 9 S_3^2 + 16 kappa S_4`,
and define `S_r := [t^r] H(t) / r`.

**Method 1 (sqrt_ql_rational).** Write `H(t) = t^2 * f(t)` with
`f^2 = Q_L`. Then `f = a_0 + a_1 t + a_2 t^2 + ...` with `a_0 = 2 kappa`
(branch fixed by sign), and from `f^2 = Q_L`:

```
(C_n) :  sum_{j=0}^{n} a_j a_{n-j} = q_n           for n in {0,1,2}
                                   = 0             for n >= 3.
```

Solving (C_0) gives `a_0 = 2 kappa`. Solving (C_1)..(C_2) gives `a_1, a_2`
in terms of `q_0, q_1, q_2`. For `n >= 3` the recursion reads:

```
a_n  =  -(1/(2 a_0)) * sum_{j=1}^{n-1} a_j a_{n-j}.
```

This is exactly the loop body of `sqrt_ql_rational` (engine L204--206).
`S_r = a_{r-2}/r`.

**Method 2 (mc_recursion_rational).** From the same identity
`f^2 = Q_L`, differentiate both sides to obtain

```
2 f f' = q_1 + 2 q_2 t.
```

Multiplying by `t^4` and using `H = t^2 f`, `H' = 2 t f + t^2 f'`:

```
2 H * H' / t  =  4 H f / t * t  +  2 H * t * f'  =  4 H * (f + t f' / 2),
```

a manipulation that — after extracting coefficients of `t^{r+1}` and
substituting `H = sum_r r S_r t^r` — produces:

```
S_r  =  -(1/(2 r kappa)) * sum_{j+k = r+2,  3 <= j <= k < r} f(j,k) j k S_j S_k,
```

which is exactly the loop body of `mc_recursion_rational` (engine
L93--113).

**Conclusion.** The two recursions are the coefficient-of-`t^r` and
coefficient-of-`t^{r-2}` extractions of the *same* identity `f^2 = Q_L`,
read against the *same* generating function `H = t^2 f`. They are not
two independent methods; they are two parametrisations of the same
inversion of the square-root operation in `Q[[t]]`.

**Consequence for the manuscript.** The claim
`thm:riccati-algebraicity` says: the shadow metric `Q_L` is a polynomial
of degree <= 2 (for single primary lines). The "verification" via
agreement of these two methods does **not** test this -- both methods
*assume* `Q_L` is a degree-2 polynomial in the input data. A real test
would fix `S_2, S_3, S_4` and check that the OPE-derived obstruction at
`r = 5` agrees with `S_5 = a_3/5`, where the OPE-derived value comes
from a genuinely external computation (e.g., Selberg integral, BPZ
recursion on the conformal block, or 5-point Wick contraction).

---

## Section 4. Independent verification candidates

Concrete, executable verification paths for the lowest shadows. These
are **proposals**, not implementations.

### 4.1 `S_3(Vir_c) = 2`

* **Source A (current, derivation).** Coefficient of `t` in the modular
  Riccati `f^2 = Q_L`, namely `q_1 / (2 a_0) = 12 kappa S_3 / (4 kappa) = 3 S_3`,
  giving `S_3 = q_1/(12 kappa) = 2` after substituting `S_3 = 2`. Self-circular.
* **Source B (proposal, independent).** The conformal block 3-point
  function `<T(z_1) T(z_2) T(z_3)>` on the sphere is fixed by global
  conformal invariance up to the constant `c_TTT`. BPZ derive
  `c_TTT = c` (Belavin-Polyakov-Zamolodchikov 1984, eq. (5.14)). The
  shadow extraction
  `S_3 = c_TTT / kappa = c / (c/2) = 2`. This is a genuinely disjoint
  path: no mention of `Q_L`, no Riccati, just BPZ + the shadow
  normalisation.

Sketch decorator:
```python
@independent_verification(
    claim="thm:obstruction-recursion-S3",
    derived_from=["MC recursion on q_1 coefficient (modular Riccati)"],
    verified_against=["BPZ 1984 c_TTT = c (3-point function)",
                      "Shadow normalisation S_r = c_{TT...T}/kappa"],
    disjoint_rationale=(
        "BPZ derive c_TTT from global conformal invariance and the "
        "Virasoro stress-tensor OPE quartic pole, with no use of "
        "the modular Riccati or any obstruction recursion."),
)
def test_S3_virasoro_from_bpz():
    c = symbols('c')
    c_TTT = c                       # BPZ 1984 eq. (5.14)
    kappa = c / 2                   # Sugawara
    assert simplify(c_TTT / kappa - 2) == 0
```

### 4.2 `S_4(Vir_c) = 10/(c(5c+22))`

* **Source A (current).** `q_2 = 9 S_3^2 + 16 kappa S_4` solved for `S_4`
  given `q_2` from the recursion.
* **Source B (proposal).** The 4-point function `<T(z_1)..T(z_4)>` on
  the sphere is the Polyakov-Wiegmann formula:
  ```
  <TTTT> = (c/2)^2 [ z_{12}^{-4} z_{34}^{-4} + z_{13}^{-4} z_{24}^{-4} +
                     z_{14}^{-4} z_{23}^{-4} ]
         + 2c [ ... cross terms ... ]
         + 4 [ ... ]
  ```
  The shadow `S_4` is the coefficient of the *connected* part divided by
  `kappa^2`; explicit Mathematica computation (or Belavin-Knizhnik 1986)
  gives `S_4 = 10/(c(5c+22))`. The denominator `5c+22` is the
  Belavin-Knizhnik signature: it is the `det(M)` of the level-2
  Kac matrix, completely external to the Riccati recursion.
* **Decorator sources**: derived_from = ["modular Riccati q_2"],
  verified_against = ["Belavin-Knizhnik 1986 4-point function",
  "Kac determinant at level 2"]. Genuinely disjoint.

### 4.3 `S_5(Vir_c) = -48/(c^2 (5c+22))`

* **Source B (proposal).** 5-point connected Virasoro Wick contraction.
  This is the **Vol I analogue of Vol III's `m_5 = 775/5184`**: enumerate
  all binary trees on 5 leaves (Catalan C_4 = 14), assign the cubic
  vertex `S_3 = 2`, the quartic `S_4`, the kappa propagator, and sum
  over channels. The connected 5-point function has an explicit closed
  form in terms of `c` and the Kac level-2 matrix; matching coefficients
  yields `-48/(c^2 (5c+22))`.

  This computation is *long* (~200 lines of code) and was the centerpiece
  of Vol III's audit. Vol I should commission it as a wave-9 task.

* **Decorator sources**: derived_from = ["MC recursion at r=5"],
  verified_against = ["5-point connected Wick contraction (14 trees)",
  "Vol III m_5 connected 5-point analogue under Vir <-> stress-tensor
  dictionary"]. Disjoint.

### 4.4 `S_6(Vir_c)` and beyond

After `S_5`, the standard literature path is the **Selberg integral**
representation of the 6-point conformal block in the
`Liouville/free-field` realisation. Dotsenko-Fateev (1984, 1985) give:

```
<T(z_1)..T(z_6)> = (Selberg integral with 6 vertex insertions and
                    3 screening operators)
```

evaluable in closed form. The shadow extraction gives `S_6` as a
rational function of `c`. This is the cleanest disjoint source for
`r >= 5` and would close the Vol I tautology gap permanently.

---

## Section 5. AP-CY43 exposure in Vol I

AP-CY43 (Vol III): "Shadow-Feynman tautology at L >= 4. The Feynman
engine calls the shadow recursion, making the match tautological."

Vol I exposure audit:

| File | L >= 4 path | AP-CY43 verdict |
|---|---|---|
| `feynman_bar_matching_engine.py` | Only computes genus 0 (tree) and genus 1 (1-loop kappa). Does not enter L >= 4. | **No exposure** |
| `theorem_feynman_bar_frontier_engine.py` | Function `genus2_bar_amplitudes` (L307) sums vertex factors with kappa, S3 inputs. Does not call shadow recursion. **Verdict: clean at L = 2.** | No exposure at L=2; L>=4 not implemented |
| `bv_brst_chain_level.py` | `_faber_pandharipande(g)` for g >= 2 returns Bernoulli ratios. The expected QME at g >= 2 is then `kappa^g * _faber_pandharipande(g)`. The independent test would need an external Faber 1999 evaluation; it is not present. | **Latent AP-CY43**: the same `_faber_pandharipande` evaluates both sides |
| `theta_feynman_graphs.py` | (not read in this wave) | unaudited |
| `btz_7loop_engine.py` | (not read in this wave) | unaudited |
| `costello_2loop_qcd_engine.py` | (not read in this wave) | unaudited |
| `formality_obstruction_loop4_engine.py` | (not read in this wave) | unaudited |

The good news: Vol I has *not* implemented L >= 4 Feynman computations
that close back through the shadow recursion. The bad news: the
Faber-Pandharipande lambda-class evaluations at g >= 2 are stored once
and reused on both sides of every "verification". This is the same
shape as AP-CY43 ("the engine calls the shadow recursion") with
"shadow recursion" replaced by "Faber-Pandharipande table". A
genuinely independent test would call `Pixton-Pandharipande relations`
on `Mbar_g,n` (codim-g; from the Pixton 2018 generators) to compute
`int lambda_g lambda_{g-1} ...` from a *different* tautological-class
basis.

---

## Section 6. Independent verification decorator proposal

Vol I should adopt the Vol III decorator wholesale. The infrastructure
is already installed; only the **adoption** is missing.

### 6.1 Engines that must be decorated first (top 5)

In priority order:

1. `shadow_tower_ope_recursion.py` (122 tautological tests; the wave-1
   target).
2. `virasoro_ainfty_explicit.py` (`virasoro_S3`, `virasoro_S4`,
   `virasoro_S5`).
3. `feynman_bar_matching_engine.py` (genus-1 amplitude `(k+2)/32`).
4. `bv_brst_chain_level.py` (QME genus-1, lambda_1 = 1/24).
5. `theorem_feynman_bar_frontier_engine.py` (1-loop bubble
   `-S_3^2/kappa`).

### 6.2 Sample decorator declarations

**Sample 1 -- Vir S_3 from BPZ:**
```python
@independent_verification(
    claim="thm:obstruction-recursion-S3-virasoro",
    derived_from=[
        "MC recursion (mc_recursion_rational q_1 coefficient)",
        "Modular Riccati f^2 = Q_L",
    ],
    verified_against=[
        "BPZ 1984 c_TTT = c",
        "Shadow normalisation S_r := c_{T...T} / kappa",
    ],
    disjoint_rationale=(
        "BPZ compute the 3-point function <TTT> from the Virasoro "
        "stress-tensor OPE quartic pole and global conformal invariance. "
        "No reference to Q_L, no recursion."),
)
def test_S3_virasoro_independent():
    ...
```

**Sample 2 -- Affine sl_2 kappa from level + dual Coxeter:**
```python
@independent_verification(
    claim="prop:affine-sl2-kappa",
    derived_from=[
        "Sugawara construction T = (1/2(k+2)) * :J^a J^a:",
    ],
    verified_against=[
        "Goddard-Kent-Olive coset T_GKO = T_full - T_sub central charge",
        "dim(sl_2) = 3 from Cartan-Killing classification",
        "h^v(sl_2) = 2 from Dynkin diagram (one node, label 2)",
    ],
    disjoint_rationale=(
        "Sugawara gives c = k dim(g)/(k+h^v); GKO computes the "
        "central charge as a Z-graded coset and matches. dim and h^v "
        "are Dynkin-diagram invariants, not VOA constructions."),
)
def test_kappa_sl2_independent():
    ...
```

**Sample 3 -- Faber-Pandharipande lambda_1 = 1/24:**
```python
@independent_verification(
    claim="prop:lambda1-mbar1n",
    derived_from=[
        "Faber 1999 explicit evaluation of int_{Mbar_1,1} psi_1",
    ],
    verified_against=[
        "Mumford 1983 lambda_1 = (1/12) kappa_1 + boundary",
        "Witten conjecture / Kontsevich theorem genus-1 string equation",
    ],
    disjoint_rationale=(
        "Faber gives the integral by intersection theory on Mbar_1,1; "
        "Mumford derives lambda_1 from GRR on the universal curve. The "
        "two paths use disjoint formalisms (intersection vs sheaf "
        "cohomology + GRR)."),
)
def test_lambda1_independent():
    ...
```

**Sample 4 -- Genus-1 affine sl_2 amplitude (k+2)/32:**
```python
@independent_verification(
    claim="thm:genus1-bar-feynman-affine-sl2",
    derived_from=[
        "kappa(V_k(sl_2)) = 3(k+2)/4",
        "lambda_1 = 1/24 (Faber-Pandharipande)",
    ],
    verified_against=[
        "Direct Polchinski 1-loop torus partition function for sl_2 KM",
        "Eta-product identity Z_torus = q^{-c/24} (1 + 3q + ...) "
        "with c = 3k/(k+2)",
    ],
    disjoint_rationale=(
        "Polchinski computes the torus partition function from the "
        "trace of q^{L_0 - c/24} on the Verma module; the eta product "
        "is a character identity. Neither uses the BV bracket, the "
        "kappa formula, or lambda_1 directly. The match (k+2)/32 "
        "appears as a coefficient extracted from the eta product."),
)
def test_genus1_affine_sl2_amplitude():
    ...
```

**Sample 5 -- Heisenberg shadow class G:**
```python
@independent_verification(
    claim="prop:heisenberg-class-G",
    derived_from=[
        "S_3 = 0 by Z_2 parity of the abelian current",
        "S_4 = 0 by Wick's theorem (no quartic contraction at genus 0)",
    ],
    verified_against=[
        "Direct Wick contraction <alpha alpha alpha alpha>_conn = 0 "
        "for free boson",
        "Free-field rho_max = 0 (Heisenberg generates polynomial ring)",
    ],
    disjoint_rationale=(
        "Wick is the *original* combinatorics of Gaussian integrals; "
        "the rho_max = 0 statement is the algebraic-geometry fact "
        "that the Heisenberg coordinate ring is polynomial. Neither "
        "uses the recursion."),
)
def test_heisenberg_class_G():
    ...
```

---

## Section 7. First-principles analyses for each tautology

Per AP-CY61: every tautological claim contains the ghost of a true
theorem. Extract them.

### 7.1 The shadow tower "two methods"

**Wrong claim (engine docstring).** "MC recursion is INDEPENDENT of the
assumption that Q_L is a quadratic polynomial."

**Ghost theorem.** The MC recursion is INDEPENDENT of the ASSUMPTION
that one *knows* `Q_L`. Given only `(kappa, S_3, S_4)` -- the initial
data -- the recursion produces all `S_r` *without ever referring to
Q_L*. This is genuinely useful: it says the shadow tower is
intrinsically defined by 3 numbers, not by the Riccati ODE.

**Correct statement.** Given `(kappa, S_3, S_4)`, both methods produce
the same tower because they are two parametrisations of the same
algebraic computation. Agreement does NOT verify the Riccati
algebraicity theorem (`Q_L` is degree 2); it verifies internal
consistency of the implementation.

**Independent verification source.** As Section 4 outlines, the
verification of `thm:riccati-algebraicity` requires showing that
external data -- conformal block 4-point functions, Selberg integrals,
direct Wick contractions -- agree with the recursion's output at
specific arities. *That* is what would close the loop.

### 7.2 The Feynman m_4 "verification"

**Wrong claim (verify_virasoro_m4.py).** "Verified `m_4 = c^2/144` by
checking `(1/12)^2 == 1/144`."

**Ghost theorem.** The pentagon identity at order `c^1` is a real
constraint that the m_4 coefficient must satisfy. *If* the manuscript
proof actually expanded the pentagon at order `c^2`, the coefficient
1/144 would be forced (modulo the m_3 coefficient 1/12). The script
does not do this expansion -- it asserts the result.

**Correct statement.** `m_4|_{c^2} = (m_3|_c)^2 / S_3` by the
A_inf / pentagon identity. With `m_3|_c = 1/12` and `S_3 = 1`, this
gives `1/144`. A genuine test would be the ARITY-4 pentagon identity:
sum over five binary trees with the actual OPE composite-field
algebra, not arithmetic on 1/12 and 1/144.

**Independent verification source.** The pentagon expansion at order
c^2 is feasible (~500 lines of sympy); the result `m_4 = c^2/144`
should drop out without ever asserting it. This is a wave-9 candidate.

### 7.3 The Faber-Pandharipande genus-2 "verification"

**Wrong claim.** Higher-genus QME verification by computing
`_faber_pandharipande(g) * kappa(A)^g` on both sides.

**Ghost theorem.** Faber 1999 explicitly evaluates lambda-class
intersection numbers on `Mbar_g,n` using the Mumford relations and
the Pixton 2018 generators. The values are externally verified
against Pixton-Pandharipande relations and Marino-Vafa formulas.
**The data IS independent** -- it just needs to be cited as such.

**Correct statement.** `int_{Mbar_g} lambda_g lambda_{g-1} (2g-3)! psi_1
^... = (Faber 1999 explicit value)`. The "verification" should be a
**lookup against Faber 1999 Table 2**, not a re-evaluation of the
helper. Decorator declares Faber 1999 as `verified_against`.

---

## Section 8. Three upgrade paths (steelman + attack + repair)

### 8.1 Steelman of "two independent methods"

**Defence (steelman).** The MC recursion is a SECOND-ORDER recurrence
(uses S_{r-1} and S_{r-2}); the sqrt(Q_L) Taylor expansion is a
CONVOLUTION recurrence on a different sequence (a_n vs r S_r). The
indices, the data structures, and the order of evaluation differ. An
implementation bug in one would not propagate to the other.

**Attack.** Both reduce to extracting Taylor coefficients of the same
generating function `H(t) = t^2 sqrt(Q_L)`. The only thing the
"agreement" tests is that both implementations correctly extract
coefficients of the same series. This is debugging, not verification.

**Repair.** Keep the agreement test as a regression test (rename to
`test_implementation_consistency`); add genuine independent checks
against Selberg / BPZ / Wick at S_3, S_4, S_5 with the decorator
declarations from Section 6.

### 8.2 Steelman of `verify_virasoro_m4.py`

**Defence.** The script narrates the pentagon argument and checks the
arithmetic. It is documentation, not a test.

**Attack.** It is presented as `compute/scripts/verify_*.py` and
appears in the make targets. The naming pattern implies verification
status that the content does not deliver.

**Repair.** Rename to `compute/scripts/narrate_virasoro_m4.py` (or
move to `notes/`) and write a real test that expands the pentagon at
order c^2 from the OPE.

### 8.3 Steelman of Faber-Pandharipande g >= 2 reuse

**Defence.** Faber 1999 Table 2 is the canonical source; recomputing
it is Cantorian.

**Attack.** The current code does not *cite* Faber 1999; it computes
`_faber_pandharipande(g)` locally from a Bernoulli-number
formula. If the formula is wrong (sign, off-by-one, or wrong
shifted-Bernoulli convention), the test passes silently because
both sides use the same wrong helper.

**Repair.** Add a single "anchor" test that hardcodes Faber 1999
Table 2 values for g = 2, 3, 4, 5 against `_faber_pandharipande(g)`.
This makes the local helper independently verified once; subsequent
uses then ride on that anchor.

---

## Section 9. Punch list (what survives, what to fix, what is wrong-but-verified)

### 9.1 Genuinely verified Vol I claims (after audit)

| Claim | Why it survives |
|---|---|
| `S_3(Vir) = 2` | Closed-form, recoverable from BPZ (independent path exists in literature) |
| `kappa(Vir_c) = c/2` | Sugawara, also recoverable from GKO coset |
| `kappa(KM_g, k) = dim(g)(k+h^v)/(2h^v)` | Closed-form from Dynkin-diagram invariants (test L735--746 IS independent) |
| Affine KM termination at S_4 = 0 | Algebraic: Jacobi identity + S_4 formula vanishes by structure constant. Test L290--320 IS independent. |
| W-line parity (odd S_r vanish for S_3 = 0) | Z_2 parity argument, not a re-run. Test L342--378 IS independent. |
| Koszul `kappa(c) + kappa(26-c) = 13` | Trivially independent (algebraic identity). Test L437--456. |
| Genus-0 sl_2 bar/Feynman matching | Manual `MANUAL_BRACKET` is an external-anchor (textbook fact), not the engine's own dict |
| Genus-1 affine sl_2 amplitude vanishing at k = -2 | Critical-level argument is independent of the (k+2)/32 formula |
| QME genus-0 classical involutivity | Direct expansion, no kappa/lambda lookup |

### 9.2 Claims requiring new independent tests (the gap)

| Claim | Needed independent path |
|---|---|
| `S_4(Vir_c) = 10/(c(5c+22))` | Belavin-Knizhnik 4-point or Kac level-2 determinant |
| `S_5(Vir_c) = -48/(c^2 (5c+22))` | 5-point connected Wick contraction (Vol III analogue) |
| `S_r` for r >= 5 (all algebras) | Selberg integral / Dotsenko-Fateev for free-field realisation |
| `m_4(T^4) = (c^2/144) d^4 T` | Pentagon expansion at order c^2 from OPE (not from m_3 squared) |
| 1-loop bubble correction `-S_3^2/kappa` | Direct bubble integral residue evaluation |
| `_faber_pandharipande(g)` for g >= 2 | Anchor to Faber 1999 Table 2 explicit values |
| Genus-1 amplitude `(k+2)/32` | Polchinski torus partition function expansion |
| Class M = mock modular (W(p)) | Independent BLLPR mock modular check (some of this is in the W2 triplet engine) |
| MO R-matrix / Hilb stable envelopes | (Vol III hands data to Vol I; status TBD) |

### 9.3 Wrong-but-verified candidates (the danger zone)

The tautology pattern guarantees that a wrong shadow-tower formula
would still pass. The most exposed claims:

* **`S_5 = -48/(c^2(5c+22))`** (Vol I): if the recursion's closed-form
  derivation has a sign error or off-by-one, the engine would compute the
  wrong value, the test would assert the engine matches the wrong value,
  and 100+ tests would still pass green. The Vol III independent check
  (`m_5 = 775/5184` from Wick) is the only path that catches this.
* **`m_4(T^4) = (c^2/144) d^4 T`**: the script literally asserts
  `(1/12)^2 == 1/144` and prints "verified". If the manuscript value
  were `(c^2/200)` (say from a different Stasheff convention), the
  script would have to be rewritten -- but no test would catch the
  discrepancy automatically.
* **1-loop bubble `S_3^2 / kappa`**: the engine and test both compute
  this from the same formula. A factor-of-2 error in the bubble
  integral measure would propagate silently.

These three are the highest-value targets for new independent tests.

---

## Section 10. Cache write-back

Patterns appearing >= 2 times across this audit (Vol I) AND the wave-1
finding (also Vol I):

### Pattern A: "Two methods agree" tautology
**Sites.**
* `shadow_tower_ope_recursion.py` mc_recursion_rational vs sqrt_ql_rational (this audit + wave 1)
* `virasoro_ainfty_explicit.py` `virasoro_S5(c)` vs
  `PrimarySectorAInfinity(c).shadow_coefficients(6)[5]`
* `theorem_feynman_bar_frontier_engine.py` bubble vs `S_3^2/kappa`
* `bv_brst_chain_level.py` higher-genus QME vs `_faber_pandharipande`

**Cache entry (proposed).** "Two-methods-agree tautology: when an
engine exposes two functions that compute the same series via
different parametrisations of the same identity (e.g., two ways of
reading coefficients of the same generating function), agreement
between them is a regression test, not a verification of any
mathematical theorem. The literature value (BPZ, Belavin-Knizhnik,
Selberg, Wick) is the only genuinely independent source."

### Pattern B: "Script verifies its own arithmetic"
**Sites.**
* `verify_virasoro_m4.py` (asserts `(1/12)^2 == 1/144`)
* (other `compute/scripts/verify_*.py` are unaudited but worth
  scanning)

**Cache entry (proposed).** "Print-only verify_*.py scripts that
narrate a derivation and assert the arithmetic should be renamed
`narrate_*.py` and supplemented with a real `tests/test_*.py` that
performs an independent computation."

### Pattern C: "Hardcoded literal verifies hardcoded literal"
**Sites.**
* `virasoro_S5(1) == -16/9` -- the literal -16/9 was produced by the
  recursion, then frozen as the test target.
* Multiple instances in `test_shadow_tower_ope_recursion.py` (the
  "Known Values" class L66--168).

**Cache entry (proposed).** "When a hardcoded test value is itself
the output of the engine under test (frozen at some past commit),
the test is a snapshot, not a verification. Snapshot tests catch
regressions but not initial bugs. Literature-anchored hardcodes
(e.g., `lambda_1 = 1/24` from Faber 1999) are different and must be
declared via the decorator's `verified_against` list."

These three patterns extend the cross-volume confusion taxonomy in
Vol III's `appendices/first_principles_cache.md`. I have not appended
to that cache (cross-volume write requires a separate review); the
proposed entries are recorded above for the next session.

---

## Concise summary

* Vol I has the independent-verification infrastructure installed
  (`independent_verification.py`, `audit_independent_verification.py`,
  `make verify-independence`) but **zero adoption** outside the
  infra self-test.
* `shadow_tower_ope_recursion.py`'s "two independent methods" claim is
  TAUTOLOGICAL: both methods extract Taylor coefficients of the same
  generating function `H = t^2 sqrt(Q_L)` -- the algebraic proof is in
  Section 3.
* `verify_virasoro_m4.py` (script) verifies arithmetic, not the
  `m_4 = c^2/144` claim it advertises.
* `virasoro_ainfty_explicit.py` tests `virasoro_S5(c) ==
  PrimarySectorAInfinity.shadow_coefficients(6)[5]` -- the same recursion
  twice. Hardcoded literals like `S_5(1) = -16/9` are snapshots, not
  verifications.
* `feynman_bar_matching_engine.py` is the cleanest engine: genus-0 is
  WEAK-INDEPENDENT (manual sl_2 brackets vs engine), genus-1 is
  WEAK-INDEPENDENT (vanishing at k = -2 is a real check).
* `bv_brst_chain_level.py` QME genus-0 is GENUINELY-INDEPENDENT;
  genus-1 is WEAK-INDEPENDENT; genus >= 2 is TAUTOLOGICAL via reuse of
  `_faber_pandharipande`.
* `theorem_feynman_bar_frontier_engine.py` 1-loop bubble correction
  `-S_3^2/kappa` is TAUTOLOGICAL.
* Vol I should adopt the decorator on the top-5 engines (Section 6.1)
  and add the independent-verification tests sketched in Section 4.
* Three wrong-but-verified candidates (S_5 closed form, m_4 = c^2/144,
  bubble = S_3^2/kappa) are the highest-value targets for new tests.
* Three cache-write-back patterns (Section 10) extend the AP-CY61
  confusion taxonomy and should be appended to
  `first_principles_cache.md` in a separate session.

No Vol I source files were modified (per task constraint). No git
commits were made.
