# Adversarial attack-and-heal: genus-2 doubly-dynamical Yang-Baxter
# Date: 2026-04-18
# Author: Raeez Lorgat
# Target: conj:g2-ddybe + thm:g2-face-model-bypass-scope-restricted + thm:fay-trisecant-genus-2-specific
# AP block: AP641-AP660 (attack-discovered), cache #228-#231.

## 0. Epistemic frame

Per CONSTITUTIONAL TRUST WARNING 2026-04-17 and Beilinson epistemic
hierarchy: the attack proceeds at levels (1) direct source computation,
(2) .tex body reading, (4) Felder 1994 / Etingof-Varchenko 1998 / Fay 1973
as primary literature. The sandbox does not have numpy; an empirical
re-run of the engine at N=12 vs N=8 is NOT performed here. This is
acknowledged: the findings below rest on source-level inspection of the
engine code and the manuscript, NOT on a fresh numerical verification.
The recommended patch includes an engine-level self-consistency upgrade
that the next session with numpy should execute and the result
inscribed; this report converts the latent claim-structure attack into
a committed heal with a DEFERRED numerical audit slot.

## 1. Attack findings (before heal)

### F1. T4 tolerance 1e-4 is below the residual-to-noise floor of a single-entry check (AP641)

CLAUDE.md line 625 records: "Generic-Ω DDYBE: 4 tests at T4 (10^{-4}
relative); plus 1 diagonal-Ω tier-(T3) consistency check". Reading the
engine at `compute/lib/face_model_ddybe_engine.py:795`:
```python
'passed': relative < 1e-4,
```
and the four generic-Ω tests at
`compute/tests/test_face_model_ddybe_engine.py:370-401`
(test_ddybe_generic_omega, test_ddybe_different_spectral,
test_ddybe_different_eta, test_ddybe_strong_coupling) all call
`verify_face_ddybe_g2` with `N=8`. The engine returns a SINGLE
`relative` scalar defined as `diff / scale` with `diff = np.max(...)`
and `scale = max(...)`. Parallel to the AP315 finding in the elliptic
swarm (engine tolerance 1e-6 accepting CYBE residuals 0.8-5.8 at
one-site values), the DDYBE 1e-4 bound at N=8 is at the BOUNDARY of the
theta-series truncation-noise floor.

The manuscript (genus_2_ddybe_platonic.tex:492-494) documents this
honestly: "at $N=12$ the residual empirically drops to $10^{-6}$, and
the $10^{-12}$ figure advertised in the prior CLAUDE.md row is not
attained without a higher-precision arithmetic backend."

**Attack resolution.** The T4 claim is SELF-CONSISTENT with an
engineering budget bound, NOT a theoretical error term.  But the T4
tolerance 1e-4 is within a factor ~100 of the truncation noise at N=8.
This is different from the AP315 elliptic-engine pattern where the
accepted residuals (0.8-5.8) were NOT passing CYBE at any reasonable
threshold. At N=8, the genus-2 theta truncation error bound is
$\epsilon(N) \lesssim e^{-\pi N^2 \min(\mathrm{Im}(\Omega))/2}
\approx e^{-\pi \cdot 64 \cdot 1.0 / 2} \approx e^{-100}$, which is
FAR below 1e-4: N=8 is not genuinely at the truncation-noise floor
for $\min(\mathrm{Im}(\Omega))=1.0$. The 1e-4 ceiling is set by the
CUMULATIVE error across 3 matrix multiplications of 8×8 matrices with
entries of scale O(1), i.e. the float-64 accumulated rounding error
plus the finite-$\hbar$ DDYBE residual. The dominant contribution at
N=8 is finite-$\hbar$ residual, not truncation.

**The honest interpretation**: the 1e-4 tolerance is a conservative
engineering budget chosen to be ~100x above the float-64 noise floor
($\approx 10^{-15}$) for an 8x8 matrix product cascade; the measured
residual is evidence that the DDYBE holds, but the bound is not
sensitive to a 1e-6 scale obstruction that would appear as
finite-$\hbar$ correction of the form $O(\hbar^k)$ with $k$ moderate.

**Heal**: (a) inscribe an explicit FALSIFICATION LADDER test: at
$N \in \{8, 12, 16\}$, if the claim is exact the residual should be
bounded by float-64 accumulated roundoff $\sim 10^{-15} \cdot
(\text{matrix-size}) = O(10^{-14})$. Anything above this is evidence
of either finite-$\hbar$ residual or truncation. If the residual
plateaus at $N \gtrsim 12$, the plateau value IS the DDYBE residual
and the claim should be downgraded by that amount. (b) Move the T4
tolerance down to $10^{-6}$ at $N=12$ and record the residuals at
$N=8,12,16$ explicitly in a registry. (c) The manuscript at
genus_2_ddybe_platonic.tex:492-494 already states the $N=12 \to 10^{-6}$
empirical drop; this report formalizes it as a mandatory engine-level
ladder.

### F2. "Szegő extends to g=2" is TRUE AS STATED; stronger statement (Szegő universal all g) is also TRUE (AP642)

Fay 1973 Cor. 2.5 is the three-term Szegő kernel identity proved
universally at all $g \geq 0$ via the Riemann addition formula on
$\mathrm{Jac}(X)$. The statement "Szegő universal at all $g \geq 0$" IS
the content of Fay's 1973 theorem: not an extension from $g=1$.
The manuscript (thm:fay-trisecant-genus-2-specific) states this
correctly: the theorem covers $g \geq 0$ with uniform proof via theta
addition. Rem:fay-name-disambiguation correctly separates:
 - (a) Three-term Szegő form (Cor. 2.5): universal at all $g$;
 - (b) Four-theta-nulls quartic identity (Cor. 4.8): holds ONLY on the
   theta divisor, a codim-1 subvariety of $\HHH_g$.
The "Fay trisecant extends to genus 2" language in the prior CLAUDE.md
row was misleading because it suggested an extension argument; Fay's
original paper is already universal. The manuscript reconciliation is
correct as written.

**Heal**: no chapter edit required; this confirms the existing
`rem:fay-name-disambiguation`. Add a sharper diagnostic test:
verify numerically the three-term Szegő identity
$S_{12}S_{23} + S_{23}S_{31} + S_{31}S_{12} = 0$ at genus-2 (currently
the engine tests the distinct Boltzmann-unitarity identity
$\alpha\beta - \gamma\delta = \Theta(z-\eta)/\Theta(z+\eta)$ via
`verify_unitarity_g2`, which is a RELATED but not identical theta
relation, per `rem:fay-versus-boltzmann-unitarity`). The missing test
is currently a gap: "Fay trisecant" in the status is asserted at
citation level for Fay 1973, not tested numerically at genus-2 in the
programme's own engine. Inscribing a direct `verify_szego_three_term_g2`
would provide a genuine independent path (vs the theta-addition
derivation).

### F3. Diagonal-Ω factorization is ALGEBRAIC on the R-matrix, not only numerical (AP643; strengthening of theorem (i))

The manuscript
`thm:g2-face-model-bypass-scope-restricted(i)` claims algebraic
exactness at diagonal Ω. Reading the engine at
`face_model_ddybe_engine.py:607-610`:

```
At diagonal Omega = diag(tau_1, tau_2), the genus-2 theta with
characteristic [1/2, 0; 1/2, 0] factorizes as
    Theta_odd(x*e_1|diag(tau_1,tau_2)) = theta_1(x|tau_1) * theta_3(0|tau_2)
and the second factor cancels in all ratios, recovering the genus-1
face model at tau = tau_1.
```

The factorization of the GENUS-2 ODD THETA at diagonal Ω along
direction $e_1$ IS an algebraic identity, NOT a numerical one:
substituting $\Omega = \mathrm{diag}(\tau_1, \tau_2)$ into the
genus-2 theta series
$\sum_{(n_1,n_2) \in \ZZ^2+\delta_1}
e^{\pi i (n_1^2\tau_1 + n_2^2\tau_2) + 2\pi i (n_1 z_1+n_2 z_2 + n\cdot\delta_2)}$
separates the $n_1$-sum from the $n_2$-sum. Each Boltzmann ratio in
(eq:g2-boltzmann) has numerator and denominator with the SAME argument
in the second component (all of $\lambda e_1, (\lambda \pm \eta) e_1,
z e_1$, etc., have zero second component), so the $n_2$-sum produces
a fixed constant $\theta_3(0|\tau_2)$ in numerator and denominator and
EXACTLY CANCELS. No numerical approximation: the cancellation is at
the level of the theta series BEFORE truncation.

The test `test_theta_g2_odd_factorization_diagonal` at
`test_face_model_ddybe_engine.py:274-295` verifies this factorization
to tolerance $< 10^{-6}$ with $N=10$ (truncation error); the UNDERLYING
identity is algebraically exact. The `test_ddybe_diagonal_omega`
residual is therefore upper-bounded by the float-64 + theta-truncation
accumulated error on a cascade of 8x8 matrix products, i.e. the
diagonal-Ω DDYBE is IMPLIED on the nose by Felder 1994 Thm 3.1
applied to the resulting genus-1 Felder R-matrix.

**Heal**: upgrade theorem (i) from "exact at diagonal Ω" (which is
already the inscribed statement) to include an explicit algebraic
proof WITHIN the chapter, not just a proof sketch. The current proof
at genus_2_ddybe_platonic.tex:447-468 is adequate; strengthen the
statement to: "at diagonal Ω the face R-matrix is ALGEBRAICALLY
equal to a single Felder R-matrix at $\tau_1$ after the $\theta_3(0|\tau_2)$
factor cancellation, and thus satisfies DDYBE as an algebraic identity
pulled back from Felder 1994 Thm 3.1". This is essentially what the
chapter already says; the upgrade is in the numerical diagnostic: add
an assertion in the test file that checks the R-matrix element-wise
equality (not just the DDYBE residual) between `face_rmatrix_g2` at
diagonal Ω and `face_rmatrix_g1` at $\tau_1$, at tolerance 1e-6 (this
IS the content of `verify_g2_to_g1_degeneration` at engine:803-831,
which is already tested at `test_degeneration_to_g1` and
`test_degeneration_different_params` — GOOD, the algebraic exactness
is registered as a regression gate).

Conclusion for F3: the diagonal-Ω claim IS exact algebraically, the
proof is adequately inscribed, and a regression test exists. No
further chapter edit required, but a CROSS-REFERENCE from the theorem
proof to the regression test function names would harden the HZ-IV
discipline. See heal H3 below.

### F4. Four T4 tests: independence audit (AP644)

The four generic-Ω tests at test_face_model_ddybe_engine.py are:
 - test_ddybe_generic_omega:     z=0.2+0.05j, w=0.15+0.1j, lam=(0.7+0.2j, 0.3+0.1j), eta=0.25, Omega generic.
 - test_ddybe_different_spectral: z=0.1+0.1j,  w=0.05+0.2j, lam=(0.5+0.1j, 0.2+0.15j), eta=0.25, Omega generic.
 - test_ddybe_different_eta:      z=0.15+0.08j,w=0.12+0.06j, lam=(0.6+0.15j,0.25+0.1j), eta=0.2,  Omega generic.
 - test_ddybe_strong_coupling:    z=0.1+0.05j, w=0.08+0.12j, lam=(0.8+0.1j, 0.4+0.2j),  eta=0.4,  Omega generic.

All four share the SAME `generic_omega` fixture
$\Omega = \begin{pmatrix} 1.1i & 0.15+0.05i \\ 0.15+0.05i & 1.3i \end{pmatrix}$.
Three of the four share $\eta=0.25$. All four are in the same region of
$\HHH_2$ (single $\Omega$ up to spectral/dynamical variation).

The FIRST and SECOND tests vary only $(z,w,\lambda)$ at fixed
$(\eta,\Omega)$. The THIRD varies $\eta$. The FOURTH varies $\eta$
more strongly (0.4, strong coupling). NONE of the four tests varies
$\Omega$.

The tests are genuinely distinct as spot-checks of a 3-parameter family
$(z,w,\lambda,\eta)$ at fixed $\Omega$. But the $\Omega$ degree of
freedom — the genuinely genus-2 content — is sampled at ONE point in
$\HHH_2$ across all four tests. This is a WEAKNESS, not a falsification,
but it should be disclosed: "four instances at a SINGLE $\Omega$
parameter choice".

Furthermore, the NON-SEPARATING degeneration regime
($\Omega_{22} \to i\infty$ with $\Omega_{12}$ fixed nonzero) is NOT
tested at all. This is the boundary stratum that carries genuinely
genus-2 content BEYOND the interior generic-$\Omega$ data; it is where
the off-diagonal period survives the limit and encodes twisted modular
data invisible to both separating degeneration and
interior-generic-point sampling. The manuscript
(`rem:g2-nonseparating-untested` at genus_2_ddybe_platonic.tex:575-588)
correctly registers this as a frontier target; the status row should
make the sampling coarseness explicit.

**Heal**: (a) add at least one more generic-Ω test at a DIFFERENT
$\Omega \in \HHH_2$ (e.g. $\Omega_{11}=2i, \Omega_{22}=1.5i,
\Omega_{12}=0.3+0.1i$, genuinely distinct off-diagonal structure);
(b) record in the manuscript the $\Omega$-sampling coarseness explicitly
(the theorem currently says "four distinct generic-$\Omega$ parameter
choices"; this is accurate only in the sense that each test has a
distinct (z,w,lam,eta) parameter tuple, but the $\Omega$ coordinate
is shared; either rephrase as "four spectral-dynamical-$\eta$ choices
at a single $\Omega$" or add the second $\Omega$ sample.

### F5. Vertex-IRF bypass: DDYBE does not imply vertex YBE at g=2 (AP645, confirming existing scope)

The attack prompt asks: if face-model satisfies DDYBE to T4, does
vertex-IRF follow? Answer: NO, and the manuscript is correct to avoid
claiming this.

At genus 0/1, the face-vertex correspondence is the dressing
transform (Jimbo-Miwa-Okado 1988; Baxter 1982 Ch. 10) that conjugates
a face R-matrix by a gauge matrix built from reference states to
produce a vertex R-matrix satisfying the NON-dynamical YBE. At
genus 2 there is no published dressing transformation in the literature:
the face-vertex correspondence in the elliptic quantum group
setting (Felder 1994) uses the elliptic $R$-matrix with a single
dynamical variable $\lambda$; the doubly-dynamical setting with two
$\lambda$-variables and an off-diagonal period $\Omega_{12}$ has no
analogue of the reference-state dressing.

The manuscript (genus_2_ddybe_platonic.tex:337-345) is correct:
"At genus 2, the vertex-IRF transform is not established in the
literature, so the face model is constructed on its own from
genus-2 theta-Boltzmann weights; this is the operational meaning of
'bypass'."

The face-model DDYBE therefore does NOT imply a vertex-model DYBE
at $g=2$. The status row should not imply otherwise.

**Heal**: the status row already says "Face-model strategy bypasses
vertex-IRF (the latter not established at g=2)". This is accurate.
No heal beyond reinforcing the caveat in the chapter (remark ahead
of Sec 4 restating that face model is the PRIMARY object, not a
derived projection of vertex YBE).

## 2. Heals

### H1. Engine falsification ladder (AP641, deferred numerical execution)

Add `verify_face_ddybe_g2_ladder(z, w, lam, eta, Omega, N_values)`
that runs the verification at N in {8, 12, 16} (or user-specified) and
returns a dict with the residual at each N. A companion test
`test_ddybe_ladder_plateau` asserts that the residual plateau value at
$N \geq 12$ is strictly below $10^{-6}$ for at least two generic-$\Omega$
points. This is the AP315-analogous patch: exposure of the tolerance
ladder's truncation sensitivity.

### H2. Second generic-Ω sample (F4)

Add `test_ddybe_generic_omega_second_sample` at
$\Omega = \begin{pmatrix}2i & 0.3+0.1i \\ 0.3+0.1i & 1.5i\end{pmatrix}$,
$(z,w,\lambda,\eta) = (0.2, 0.15, (0.6, 0.4), 0.25)$ to widen the
$\Omega$-sampling beyond the single `generic_omega` fixture.

### H3. Cross-reference proof to regression test (F3)

Update `thm:g2-face-model-bypass-scope-restricted(i)` proof body
(genus_2_ddybe_platonic.tex:447-468) to include an explicit pointer
to the regression-gate function `verify_g2_to_g1_degeneration` and
the pass/fail test locations. HZ-IV discipline gain: the algebraic
factorization `Theta_odd(x e_1|diag(tau_1,tau_2)) = -theta_1(x|tau_1)
theta_3(0|tau_2)` is registered as a tested invariant.

### H4. Direct three-term Szegő test (F2)

Add `verify_szego_three_term_g2(z1, z2, z3, Omega, N)` computing
$S_{12} S_{23} + S_{23} S_{31} + S_{31} S_{12}$ at genus-2 and asserting
it vanishes to tolerance $10^{-6}$ at $N=10$. This gives an
independent verification path disjoint from both theta-addition and
Boltzmann unitarity.

### H5. Ω-sampling coarseness disclosure (F4)

Edit `thm:g2-face-model-bypass-scope-restricted(ii)` and
`rem:g2p-regime-ii-scope` to phrase: "four spectral-dynamical-$\eta$
parameter instances at a single $\Omega \in \HHH_2$, plus one
second-$\Omega$ spot check". Updates CLAUDE.md DDYBE-face-model status
row in the next master sync.

### H6. Status of `conj:g2-ddybe` stays Conjectured (NO upgrade)

The diagonal-Ω case is ProvedHere (pulled back from Felder).
The generic-Ω case remains numerical evidence at 5 (now 6 with H2)
parameter instances at N=8. The finite-$\hbar$ commutativity of
doubly-dynamical Casimirs is the residual conjecture (the manuscript
says so explicitly).

No upgrade to theorem; H1-H5 are SCOPE + DIAGNOSTIC sharpening, not
a proof extension.

## 3. AP registrations (AP641-AP645)

AP641: Tolerance-ladder-ceiling vs truncation-noise-floor disclosure.
Any numerical engine supporting a theorem-status "VERIFIED / NUMERICAL
EVIDENCE" row must expose a RESIDUAL-AT-VARYING-TRUNCATION ladder
test; a single tolerance bound at a single truncation depth is
insufficient to distinguish engineering budget from theoretical bound.

AP642: "Extends to genus X" language. When a classical result is
proved uniformly at all genera in the original paper (Fay 1973, Mumford
Tata I/II for theta identities, Bergman 1958 for prime form), the
programme must state the claim uniformly, not as an extension from a
lower-genus case; "extends to g=2" misleads on proof structure and
invites readers to expect an extension argument that does not exist.

AP643: Algebraic-exactness vs numerical-evidence in degeneration
claims. A degeneration along a stratum of moduli space (diagonal Ω,
separating boundary, non-separating boundary) is algebraically exact
iff the limit commutes with all defining operations (here: theta series
truncation → theta series + limit; matrix multiplication is preserved
trivially); numerical checks only VERIFY the algebraic identity, they
do not CONSTITUTE it.

AP644: Ω-sampling coarseness in genus-g claims. A numerical claim at
"generic Ω" on a $d$-dim moduli must state how many distinct Ω
parameters are sampled; sampling at a single Ω and varying only
ancillary parameters $(z, w, \lambda, \eta)$ does NOT witness the
Ω-dependence of the claim.

AP645: Face-model DDYBE does NOT imply vertex-model YBE at $g \geq 2$.
The Jimbo-Miwa-Okado / Baxter dressing transformation is established
for $g \leq 1$; for $g \geq 2$, the face-vertex correspondence is an
open problem, and face-model evidence cannot be propagated to vertex
claims.

## 4. Cache entries (#228-#231)

Cache #228 (AP641 operational): before declaring "VERIFIED at 10^{-k}",
run at 2 distinct truncation depths $N_1 < N_2$; if $r(N_1) \approx
r(N_2)$, the residual is the theoretical bound (finite-$\hbar$ or
finite-size); if $r(N_2) \ll r(N_1)$, the residual is still truncation
noise and the tolerance bound is a ceiling, not a theorem.

Cache #229 (AP642 operational): grep CLAUDE.md status rows for
"extends to genus $N$" / "extends to $g \geq k$"; for each hit, verify
that the extension is a proof, not a restatement of a uniform
classical theorem; rephrase to "uniform at all $g \geq 0$" or
"proved directly at genus $N$ via [specific argument]".

Cache #230 (AP643 operational): when a degeneration claim is
cross-referenced from the theorem body to a test function, the test
should assert ELEMENT-WISE EQUALITY of the degenerated object with
the target object (e.g. R_g2(x, lam, eta, diag(tau1,tau2)) == R_g1(x,
lam, eta, tau1) ± sign, element-wise to 10^{-6}), NOT only the
downstream DDYBE/DYBE residual. Algebraic exactness is registered
by element-wise match.

Cache #231 (AP644 operational): a numerical claim on moduli parameterized
by $d$ complex coordinates requires sampling at $\geq \min(d+1, 3)$
distinct moduli points to witness the full parameter dependence; sampling
at a single moduli point and varying ancillary data does not.

## 5. Files touched

Chapter body:
 - `chapters/theory/genus_2_ddybe_platonic.tex`:
   - (H3) proof of `thm:g2-face-model-bypass-scope-restricted(i)`:
     add cross-reference to `verify_g2_to_g1_degeneration` and its tests.
   - (H5) theorem statement (ii) and `rem:g2p-regime-ii-scope`:
     disclose single-Ω sampling coarseness.
   - (H5, post-H2) update numerical-instance count from 4 to 5.

CLAUDE.md (next master sync, not this session):
 - DDYBE face model row: add "single-$\Omega$ sample" caveat,
   advertise AP641-AP645 block.

Engine + tests (H1, H2, H4):
 - `compute/lib/face_model_ddybe_engine.py`:
   add `verify_face_ddybe_g2_ladder` (AP641); add
   `verify_szego_three_term_g2` (H4).
 - `compute/tests/test_face_model_ddybe_engine.py`:
   add `test_ddybe_ladder_plateau` (H1);
   add `test_ddybe_generic_omega_second_sample` (H2);
   add `test_szego_three_term_g2` (H4).

## 6. Deferred audit (numpy unavailable in sandbox)

The patch is WRITTEN but the ladder test has NOT been run in this
session (sandbox has no numpy). When numpy is available, run:
```
cd /Users/raeez/chiral-bar-cobar
python3 -m pytest compute/tests/test_face_model_ddybe_engine.py \
    -q -ra --no-header
```
and inscribe the ladder values at N=8,12,16 into
`rem:tolerance-ladder` of the chapter.

The deferred execution is registered as a pending verification item:
should the ladder show residual plateauing at $r \gg 10^{-6}$ for
$N \geq 12$, the status `conj:g2-ddybe` is STRENGTHENED to include an
explicit finite-$\hbar$ obstruction bound; should the plateau drop to
float-64 noise $\sim 10^{-14}$, the evidence ascends toward an
algebraic identity claim (still Conjectured at this programme, since
an algebraic proof of the DDYBE at generic $\Omega$ is not inscribed
anywhere in the programme).

## 7. Summary

| Attack | Finding | Heal |
|---|---|---|
| (i) T4 tolerance sensitivity | Engineering ceiling, not theoretical bound; 100x above float-64 noise at N=8 | H1 ladder test |
| (ii) Szegő at g=2 | Fay 1973 Cor. 2.5 universal at all $g$; manuscript already correct | H4 direct test, no chapter edit |
| (iii) Diagonal-Ω exactness | Algebraically exact via $\theta_3(0|\tau_2)$ cancellation; regression gate already exists | H3 cross-reference |
| (iv) 4 tests independence | Distinct (z,w,λ,η), single Ω | H2 second-Ω sample, H5 disclosure |
| (v) Vertex-IRF bypass | Face-model DDYBE does NOT imply vertex YBE at g=2; manuscript correct | AP645 register, no edit |

Final status of `conj:g2-ddybe`: `\ClaimStatusConjectured`. DOWNGRADE
not warranted (the numerical evidence, while coarse, is positive).
UPGRADE not warranted (no proof; only numerical evidence at 5 parameter
instances).
