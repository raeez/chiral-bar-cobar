# Wave 5 Adversarial Attack + Heal: genus-2 DDYBE face-model cluster

Target: `chapters/theory/genus_2_ddybe_platonic.tex` (687 lines) + engine
`compute/lib/face_model_ddybe_engine.py` + tests
`compute/tests/test_face_model_ddybe_engine.py`.

Author: Raeez Lorgat. No AI attribution.

Date: 2026-04-17.

## PHASE 1 ATTACK: verdicts

### (i) Tolerance ladder justification — PARTIAL PASS, strengthened

The ladder T1(1e-12) / T2(1e-10) / T3(1e-6) / T4(1e-4) is an
**engineering roundoff + truncation budget**, NOT a theoretical
error term of the form $O(\hbar^2)$. The chapter states this
correctly ("$10^{-4}$ ceiling reflects the $N=8$ truncation of
the genus-$2$ theta series, not a failure of the DDYBE");
reading the engine confirms: `verify_face_ddybe_g2` hardcodes
`relative < 1e-4` (line 795), `verify_g2_to_g1_degeneration`
hardcodes `relative < 1e-6` (line 830). At $N=12$ the residual
empirically drops to $10^{-6}$ per the chapter's claim (not
directly verified in-engine; plausibly correct given Gaussian
decay of the theta series at $|\mathrm{Im}(\Omega)|\sim 1$).

**Heal installed**: explicit remark distinguishing
*engineering budget* from *theoretical error term*; explicit
scaling law $\varepsilon(N) \lesssim e^{-\pi N^2 \min(\mathrm{Im}(\Omega))/2}$
for the truncation budget; statement that absence of a residual
theoretical error term is what makes T4 *numerical evidence*
rather than *proof*.

### (ii) 5 tests at T4 is weak numerical evidence — UPHELD

The generic-$\Omega$ sweep covers two spectral pairs, two
$\boldsymbol\lambda$ values, and three $\eta$ values across
five test instances. This is **insufficient** for a generic-locus
claim over a three-complex-dimensional moduli $\HHH_2$.

**Heal installed**: chapter already states "numerical evidence,
not a proof"; reinforcement added that five instances sweep a
codim-0 subset of a 3-complex-dimensional moduli, so the claim
is pointwise, not uniform; residue bounds $<10^{-4}$ do NOT
constitute asymptotic continuity verification across $\HHH_2$.

### (iii) Diagonal-$\Omega$ factorisation "exact via two genus-1 DYBE copies" — PARTIAL UPHOLD, HEAL

The engine test `test_ddybe_diagonal_omega` uses
`lam = np.array([0.7 + 0.2j, 0.0])` — so $\lambda_2 = 0$, and
the "two independent Felder copies" is actually
**one Felder copy + a trivial factor**, not two nontrivial
copies. The 4x4 $R^{\mathrm{face}}$ at diagonal $\Omega$ does
not tensor-factorise into two 4x4 Felder matrices; the chapter
statement

\[
  R^{\mathrm{face}}\bigl(z,(\lambda_1,\lambda_2),
  \mathrm{diag}(\tau_1,\tau_2)\bigr)
  =
  R^{\mathrm{Felder}}(z,\lambda_1,\tau_1)\otimes
  R^{\mathrm{Felder}}(z,\lambda_2,\tau_2)\big|_{\mathrm{shift}}
\]

is overstated: the engine treats
`Theta_odd(x e_1 | diag(tau_1,tau_2)) = theta_1(x|tau_1) * theta_3(0|tau_2)`,
so the $\tau_2$-factor is a **constant** in $x$, NOT a
$R^{\mathrm{Felder}}(z,\lambda_2,\tau_2)$ matrix. The correct
statement is: the face $R$-matrix REDUCES to
$R^{\mathrm{Felder}}(z,\lambda_1,\tau_1)$ (up to the overall
$\theta_3$ normalisation), and the "second copy" is trivial.

**Heal installed**: theorem (i) rewritten to state "reduces to
a single genus-1 Felder $R$-matrix (the $\tau_2$-sector entering
only through the $\theta_3(0|\tau_2)$ normalisation that cancels
in every Boltzmann-weight ratio), so the DDYBE reduces to one
genus-1 DYBE". The prior "tensor product of two Felder" form is
retracted. The "doubly dynamical" claim at diagonal
$\Omega$ is vacuous.

### (iv) "Separating degeneration AP157-empty" — UPHELD

Pattern-225-equivalent: a specialisation that factorises to
independent lower-genus copies cannot carry genuinely $g=2$
content, so any identity verified there is tautological relative
to the $g=1$ theorem. The chapter correctly marks this regime
as "empty" and explicitly notes the genuinely $g=2$ content
lives at generic $\Omega$ with $\Omega_{12} \ne 0$.

### (v) Non-separating degeneration NOT tested — CRITICAL FINDING

The chapter Remark~\ref{rem:ap157-g2} distinguishes two
boundary divisors; only separating is tested numerically
(diagonal $\Omega$). The genuinely $g=2$ degeneration —
non-separating, $\Omega_{22} \to i\infty$, $\Omega_{12}$ FIXED
NONZERO, $\Omega_{11}$ fixed — is absent from the engine suite.

**Heal installed**: explicit frontier remark
`rem:g2-nonseparating-untested`; conjecture
`conj:g2-ddybe-nonseparating-limit` registering as a separate
falsification target that at the non-separating boundary, the
DDYBE reduces to a genus-$1$ *twisted* DYBE with Stokes data
encoding the surviving $\Omega_{12}$ periodic direction. This
is the genuine open content and is NOT currently in the engine
suite.

### (vi) Fay vs Szegő three-term identity — UPHELD with NUANCE

Chapter claim: the programme uses Fay 1973 Cor. 2.5 (Szegő
three-term), NOT the four-theta-nulls quartic identity on the
theta divisor. The engine tests a DIFFERENT Fay-class identity:
`verify_unitarity_g2` checks the scalar *product* identity

\[
  \alpha\beta - \gamma\delta = \Theta((z-\eta)e_1)/\Theta((z+\eta)e_1),
\]

which is the unitarity-type Boltzmann-weight Riemann addition
formula, NOT the three-term cyclic Szegő identity
$S_{12}S_{23} + S_{23}S_{31} + S_{31}S_{12} = 0$ stated in
\eqref{eq:fay-three-term}. The three-term trisecant
(Fay 1973 Cor. 2.5) is INVOKED in the bar complex Stokes
analysis (Remark~\ref{rem:why-a-not-b}), but is NOT the
identity verified numerically by
`verify_unitarity_g2`/`test_fay_identity_g2_generic`.

**Heal installed**: explicit distinction between
(1) *Szegő three-term trisecant* $S_{12}S_{23}+S_{23}S_{31}+S_{31}S_{12}=0$
[Fay 1973 Cor. 2.5, used in the bar-complex Stokes analysis,
not numerically tested here] and
(2) *Boltzmann-weight unitarity* $\alpha\beta-\gamma\delta$
[tested numerically in `verify_unitarity_g2`, a Riemann-addition
corollary]; (1) and (2) are DISTINCT theta-function identities
both due to Fay; the engine tests (2). Chapter prose and test
docstrings now agree on the naming.

### (vii) Vertex-IRF at $g=2$ not established — UPHELD

Correct: vertex-face correspondence at $g=1$ is Baxter 1973,
but $g=2$ vertex-IRF is open. The programme bypasses by
constructing Boltzmann weights directly from genus-2 theta
functions. Chapter statement accurate.

### (viii) 29 face-model tests enumeration — FAILS INVENTORY

Counting from `test_face_model_ddybe_engine.py`:

| Class | Method | T-tier |
|-------|--------|--------|
| `TestThetaFunctions` | 4 methods | T1 |
| `TestBoltzmannWeightsG1` | 6 methods | T2 |
| `TestFaceDYBEG1` | 4 methods | T2 |
| `TestClassicalLimit` | 3 methods | T1-T2 |
| `TestGenus2Theta` | 3 methods | T3 |
| `TestBoltzmannWeightsG2` | 4 methods | T3 |
| `TestFaceDDYBEG2` | 5 methods | **T4** (1 diagonal, 4 generic) |
| `TestFullSuite` | 1 integration | mixed |

Total: **30** (not 29). The claim "29 face-model tests" in
CLAUDE.md is off-by-one. The T4-level generic-Ω is
**4 tests** (diagonal-Ω is at T3, not T4 — the test is in class
`TestFaceDDYBEG2` but its physics is T3). If we count by
physics-tier, T4 has 4 tests; if we count by class, the diagonal
test is in the T4 class.

**Heal installed**: accurate enumeration in chapter
`rem:tolerance-ladder`; "5 generic-$\Omega$ compute tests"
(the 4 non-diagonal + the 1 that passes at diagonal, which
is simultaneously a T3 check and a T4 sanity) revised to
"$4$ genuinely generic-$\Omega$ DDYBE tests at T4 +
$1$ diagonal-$\Omega$ DDYBE sanity check at T3"; total
"$30$ face-model tests".

### (ix) Cache entries #220-227 — INACCURATE CITATION

`first_principles_cache_comprehensive.md` Patterns 220-227
are: 220 (theorem-preamble throat-clearing), 221
(blacklist-slug leakage), 222 ($\overline{\cM}_{0,n}$
off-by-one), 223 (iterated-residue ordering), 224
(Sym-r-matrix normalisation), 225 (wave/campaign
identifier leakage), 226 (Mukai signature), 227
(Taylor expansion degree). These are **unrelated to DDYBE**
— they arise in different Wave 2026-04-17 audits
(bar_construction, configuration_spaces, Mukai/Yangian).

The CLAUDE.md HOT ZONE statement "Cache entries #220-227
register this" (for g=2 DDYBE) is **factually wrong**.

**Heal installed**: CLAUDE.md annotation pointer retracted
internally (via this wave note); no DDYBE-specific cache
patterns currently registered. A new cache pattern #228
(*numerical tolerance ladder conflation with theoretical
error term*) is the correct refactor; this is inscribed in
the cache file as a Wave 5 deliverable outside this chapter.

## PHASE 2 HEAL: surgical edits to `genus_2_ddybe_platonic.tex`

1. Remark `rem:ap157-g2`: fix empty `\textup{(...)} states:`
   fragment at line 148 (missing antecedent, orphaned
   `\textup{(...)}`). Supplied correct clause "Anti-pattern
   157 states: a degeneration-dependent identity is NOT a
   genus-$2$ invariant, because the separating locus carries
   no genuinely $g=2$ content". No manuscript-metadata-hygiene
   violation: use the semantic descriptor, not the AP label.

2. Remark `rem:g2p-g1-limit` line 244: orphaned `\textup{(-empty)}`
   fragment fix; replace with "factorised-limit regime".

3. Theorem `thm:g2-face-model-bypass-scope-restricted`(i):
   revise from "tensor product of two independent Felder
   DYBEs" to the correct reduction to a SINGLE Felder DYBE
   in $(z,\lambda_1,\tau_1)$ with a trivial $\theta_3(0|\tau_2)$
   normalisation. The engine confirms this: `lam_g2 = [lam_scalar, 0]`
   at the test, and only the first coordinate enters the
   weights. The "doubly-dynamical" character is vacuous at
   diagonal $\Omega$.

4. Theorem (iii): rename "separating-degeneration regime
   (-empty)" to "separating-degeneration regime
   (factorised-limit, no genuinely $g=2$ content)".

5. Remark `rem:tolerance-ladder`: add explicit engineering
   vs theoretical budget distinction; cite the
   $\varepsilon(N) \lesssim e^{-\pi N^2 \min(\mathrm{Im}(\Omega))/2}$
   scaling.

6. New remark `rem:fay-versus-boltzmann-unitarity`: distinguish
   the Szegő three-term trisecant (Fay 1973 Cor. 2.5, used in
   bar complex Stokes) from the Boltzmann-weight unitarity
   identity $\alpha\beta-\gamma\delta = \Theta(z-\eta)/\Theta(z+\eta)$
   (tested numerically).

7. New remark `rem:g2-nonseparating-untested`: register the
   non-separating degeneration as untested; document it as
   the genuine frontier for `conj:g2-ddybe`.

8. Summary-of-status table row corrections: "$5$ generic-$\Omega$"
   -> "$4$ generic-$\Omega$ + $1$ diagonal-$\Omega$ sanity";
   "$29$ tests" -> "$30$ tests".

9. Corrigenda `rem:g2-corrigenda` item (d) corrected: from
   "$29$ face-model tests, of which $5$ are generic-$\Omega$"
   to "$30$ face-model tests, of which $4$ are genuinely
   generic-$\Omega$ DDYBE".

10. Remove the "Fay trisecant extends to genus 2" residual
    language from `rem:g2-corrigenda` item (c): the correct
    statement is that Fay 1973 Cor. 2.5 (Szegő three-term)
    holds at all $g \ge 0$, including $g = 2$, by direct
    application; no "extension" is needed.

## Residual (conjectural) content of `conj:g2-ddybe`

After this heal, the residual conjectural content is:

(A) Finite-$\hbar$ commutativity of doubly-dynamical Casimirs
    at GENERIC $\Omega \in \HHH_2$ with $\Omega_{12} \ne 0$
    (infinitesimal/classical limit proved via heat-equation
    symmetry; finite $\hbar$ is numerical evidence only).

(B) Non-separating degeneration limit: at
    $\Omega_{22} \to i\infty$ with $\Omega_{12}$ FIXED nonzero,
    the DDYBE reduces to a genus-$1$ *twisted* DYBE. This is
    untested.

(C) Stokes-data consistency across the entire non-separating
    boundary stratum, with $\Omega_{12}$ serving as the
    surviving modular parameter.

## Constitutional hygiene

All AP/HZ/cache labels in this heal note are in the working
notebook (this file), NOT in the manuscript. The .tex edits
use mathematical substance only. No manuscript-AP-label
leakage. No AI attribution anywhere. All mathematics
attributed to Raeez Lorgat.
