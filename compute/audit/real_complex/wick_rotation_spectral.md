# Wick Rotation as a Real-to-Complex Bridge in Spectral Theory

## Date: 2026-04-01
## Status: Deep investigation, falsification-first (Beilinson Principle)
## Sources: arithmetic_shadows.tex, scattering_resonance.py, roelcke_selberg_decomposition.py, mc_spectral_measure.md, working_notes.tex (Vol II archive), shadow_radius.py, shadow_singularity_map.py, spectral_continuation.py

---

## 0. Executive Summary

The bar complex sees real algebraic data (OPE coefficients, shadow tower, MC equation). The zeta zeros live at complex spectral parameters. Five distinct "Wick rotation" mechanisms are investigated as potential bridges. The conclusion: each mechanism is mathematically precise but none crosses the structural obstruction (rem:structural-obstruction). The obstruction is a theorem, not a gap to be closed.

**Decisive findings:**

1. Wick-rotating c to the complex plane gives access to new analytic structure in the shadow metric Q_L (the branch points move), but the shadow tower remains determined by three invariants (kappa, alpha, S_4) regardless of whether c is real or complex. Three invariants cannot constrain infinitely many zeros.

2. The zeta zeros enter the Benjamin-Chang construction through the functional equation factor F_c(s) = Gamma(...) zeta(2s) / [... zeta(2s-1)], not through the spectral decomposition itself. The RS integral I(s) is holomorphic at all scattering poles (prop:scattering-residue, PROVED). The poles are artifacts of the functional equation, not of the integral.

3. The Selberg zeta function Z_Gamma(s) is the closest complete spectral-geometric bridge, but its construction requires input (the Selberg trace formula) not supplied by the sewing/bar formalism. The real-to-complex transition in the Selberg setting IS a resonance phenomenon for non-compact surfaces, but the bar complex does not see geodesic data.

4. The Polyakov complexification (constr:liouville-complexified) is the most promising framework for accessing complex spectral parameters, but it has a no-go at genus 1 (prop:genus-one-saddle-triviality) and requires genus >= 2 geometry where the Liouville action is nonlinear. This is genuinely beyond the current bar formalism.

5. The "spectral Wick rotation" s -> s + i*theta in the spectral variable is mathematically well-defined (the Eisenstein series E(tau, s) continues meromorphically) but does not provide new constraints: the MC equation fixes c(t) for real t, and the Eisenstein continuation is a CONSEQUENCE of the Eisenstein functional equation, which is external to the bar construction.

---

## 1. Investigation 1: Shadow Tower at Complex Central Charge

### 1.1 The shadow metric Q_L at real c

For the Virasoro algebra at real c > 0, the shadow metric on a one-dimensional primary slice is (thm:riccati-algebraicity):

    Q_L(t) = 4*kappa^2 + 12*kappa*alpha*t + (9*alpha^2 + 16*kappa*S_4)*t^2

where kappa = c/2, alpha = -5c/(5c+22) * kappa (from cubic OPE), S_4 = Q^contact = 10/[c(5c+22)].

The critical discriminant is:

    Delta = 8*kappa*S_4 = 80*kappa / [c*(5c+22)] = 40 / (5c+22)

For real c > 0 (and c != -22/5): Delta > 0, so the discriminant of Q_L is:

    disc(Q_L) = -32*kappa^2 * Delta < 0

The branch points of sqrt(Q_L(t)) are a complex conjugate pair.

### 1.2 What happens at complex c

Analytically continuing c to C:

**(a) kappa(c) = c/2**: continues holomorphically, with kappa = 0 at c = 0.

**(b) alpha(c) = -5c*kappa / (5c+22) = -5c^2 / [2(5c+22)]**: continues holomorphically, with a simple pole at c = -22/5.

**(c) S_4(c) = 10/[c(5c+22)]**: continues meromorphically, with simple poles at c = 0 and c = -22/5.

**(d) Delta(c) = 40/(5c+22)**: continues holomorphically away from c = -22/5.

**(e) The branch points t_pm(c)**: are solutions to Q_L(t) = 0, hence algebraic functions of c. At real c > 0 they form a complex conjugate pair. At complex c they are generically two distinct complex numbers, no longer conjugate.

### 1.3 New analytic structure at complex c

**The branch cut rotates.** At real c, the branch cut of sqrt(Q_L) connects two conjugate points in the complex t-plane. At complex c, the branch cut connects two non-conjugate points. The monodromy remains -1 (Koszul sign, thm:shadow-connection), since the monodromy group is topological and does not change under continuous deformation of c.

**The shadow growth rate rho(c) = sqrt(9*alpha^2 + 2*Delta) / (2|kappa|)** (thm:shadow-radius) continues to complex c. The critical cubic 5c^3 + 22c^2 - 180c - 872 = 0 (convergence/divergence threshold) has three roots in C:

- c* approx 6.125 (real, the physical threshold)
- Two complex conjugate roots

At complex c beyond these roots, the shadow tower may have different convergence properties.

### 1.4 Falsification: does complex c help?

**NO.** The fundamental obstruction persists:

**(i) Finite determination.** The shadow tower at ANY c (real or complex) is determined by three invariants (kappa(c), alpha(c), S_4(c)). These are three holomorphic functions of c. Three functions of one variable cannot constrain the infinitely many zeros of epsilon^c_s(A).

**(ii) The primary spectrum {Delta_i} is independent of the shadow tower.** For Virasoro at generic c (irrational), the primary spectrum is a discrete set {h_{r,s}} determined by the central charge via the Kac determinant formula, not by the OPE data that enters the shadow tower. The shadow tower sees the vacuum OPE; the primary spectrum sees the representation theory.

**(iii) Analytic continuation in c does not generate new constraints.** The MC equation at complex c is the SAME algebraic equation as at real c, with c treated as a parameter. The algebraic constraints from the MC equation are satisfied for ALL c simultaneously (they are polynomial identities in the OPE data). Specializing to complex c does not produce additional equations.

**(iv) The discriminant field changes but remains quadratic.** At real c, the shadow generating function lives over Q(c)(sqrt(Delta)). At complex c, it lives over Q(c)(sqrt(Delta(c))). The quadratic extension changes character (the field norm is no longer positive definite), but the algebraic degree remains 2. The tower is still determined by a quadratic algebraic function.

**VERDICT: Wick-rotating c yields interesting complex geometry (the branch cut rotates, the monodromy representation acquires new structure) but does NOT cross the structural obstruction. The shadow tower at complex c carries the same finite amount of information (three invariants) as at real c.**

---

## 2. Investigation 2: Where the Zeta Zeros Enter

### 2.1 The spectral decomposition on M_{1,1}

The Roelcke-Selberg decomposition (roelcke_selberg.md, roelcke_selberg_decomposition.py) decomposes Z-hat^c(tau) into:

    Z-hat^c = c_res * (3/pi)                                [residual]
            + (1/4pi) int c_E(t) E(1/2 + it, tau) dt       [Eisenstein/continuous]
            + sum_j c_j u_j(tau)                             [Maass/discrete]

The spectral parameters are:
- Residual: s = 1 (eigenvalue 0)
- Continuous: s = 1/2 + it for t in R (eigenvalue 1/4 + t^2)
- Discrete: s_j = 1/2 + it_j with t_j^2 > 0 real (Selberg's theorem for SL(2,Z)\H)

ALL spectral parameters on the REAL t-axis (for the compact case SL(2,Z)\H).

### 2.2 The functional equation and the scattering matrix

The Eisenstein series E(tau, s) satisfies:

    E(tau, s) = phi(s) E(tau, 1-s)

where phi(s) = Lambda(1-s)/Lambda(s) is the scattering matrix, and Lambda(s) = pi^{-s} Gamma(s) zeta(2s).

The scattering matrix has:
- Poles at s = rho/2 where zeta(2s) = zeta(rho) = 0 (the nontrivial zeros, from Lambda(s) = 0)
- Zeros at s = (1-rho_bar)/2 where Lambda(1-s) = 0

These poles are at COMPLEX values of s (Re(rho) between 0 and 1, so Re(s) between 0 and 1/2, generically NOT on Re(s) = 1/2).

### 2.3 The Benjamin-Chang construction: how zeta zeros enter

The constrained Epstein series epsilon^c_s satisfies a functional equation (Benjamin-Chang, arXiv:2208.02259):

    epsilon^c_{c/2 - s} = F_c(s) * epsilon^c_{c/2 + s - 1}

The factor F_c(s) = Gamma(s) Gamma(s + c/2 - 1) zeta(2s) / [pi^{2s-1/2} Gamma(c/2-s) Gamma(s-1/2) zeta(2s-1)] introduces poles from zeta(2s-1) = 0 at s = (1+rho_n)/2.

**The zeta zeros enter through the FUNCTIONAL EQUATION FACTOR F_c(s), not through the spectral decomposition.**

### 2.4 The RS integral is holomorphic at scattering poles (PROVED)

Proposition prop:scattering-residue (arithmetic_shadows.tex line 7093):

The Rankin-Selberg integral I(s) = int Z-hat^c * E_s d mu continues meromorphically and is HOLOMORPHIC at all s = rho/2. The proof: RS unfolding replaces the integral by the Mellin transform of a_0(y), whose poles are determined EXCLUSIVELY by the asymptotic behavior of a_0 at y = 0 and y = infinity. The scattering matrix phi(s) is erased by the unfolding.

**The RS unfolding is the mathematical Wick rotation:** it replaces a real-analytic integral over the modular surface (which sees both chiralities and the scattering matrix) by a Mellin transform of the zeroth Fourier mode (which sees only one chirality and has poles only from the asymptotic expansion). The unfolding "rotates" away the scattering data.

### 2.5 The inverse Wick rotation problem

To access the scattering poles, one would need to REVERSE the unfolding: go from the Mellin integral I(s) = int a_0(y) y^{s-2} dy back to the geometric integral int Z-hat^c * E_s d mu, and then continue E_s OFF the critical line Re(s) = 1/2.

But this is exactly the problem of analytic continuation of the Eisenstein series to complex s, which is EXTERNAL to the bar construction. The bar complex provides a_0(y) (through the sewing determinant and the shadow tower). The Eisenstein series E(tau, s) and its scattering matrix are properties of the HYPERBOLIC SURFACE, not of the chiral algebra.

**VERDICT: The zeta zeros enter through the functional equation of the Eisenstein series, which is a property of the modular surface SL(2,Z)\H. The bar complex does not see the modular surface; it sees the chiral algebra and its sewing. The RS unfolding erases the scattering matrix. No mechanism within the bar formalism can restore it.**

---

## 3. Investigation 3: The Spectral Wick Rotation s -> is

### 3.1 Formal definition

The Eisenstein series E(tau, s) for Re(s) > 1 is:

    E(tau, s) = (1/2) sum_{(c,d)=1} y^s / |c*tau + d|^{2s}

This extends meromorphically to all s in C. The "spectral Wick rotation" s -> s + i*theta rotates the spectral parameter off the critical line.

### 3.2 The Riemann zeta on the critical line

The Riemann zeta zeta(s) on the critical line s = 1/2 + it satisfies |zeta(1/2+it)| in R. The Hardy Z-function Z(t) = exp(i*theta(t)) * zeta(1/2+it) is real-valued for real t, where theta(t) is the Riemann-Siegel theta function.

The RS integral at s = 1/2 + it is:

    I(1/2 + it) = int Z-hat^c(tau) * E(tau, 1/2 + it) d mu(tau)

For real t, E(tau, 1/2+it) is real-valued on SL(2,Z)\H (since E(tau, s) = overline{E(tau, s_bar)} and s_bar = 1/2 - it = 1 - s on the critical line, and E(tau, 1-s) = phi(s) E(tau, s) with |phi(1/2+it)| = 1). So I(1/2+it) is real up to the phase of phi.

### 3.3 Wick rotation s -> s + i*theta: what it sees

Continuing E(tau, s) off the critical line to s = 1/2 + i*t + delta (real delta > 0):

    E(tau, 1/2 + delta + it)

This is a regular Eisenstein series for delta > 0. As delta increases, the series converges better (the terms decay faster). The spectral content changes: we are now probing the non-L^2 part of the spectral decomposition.

**The poles of E(tau, s) in s are at s = 0 and s = 1 (from the Epstein-zeta functional equation), NOT at the zeta zeros.** The Eisenstein series does not see the zeta zeros in its pole structure. The zeta zeros appear only in the scattering matrix phi(s) = Lambda(1-s)/Lambda(s), which mediates between E(tau, s) and E(tau, 1-s).

### 3.4 Could the MC equation constrain I(s) at complex s?

The MC equation constrains the shadow tower coefficients S_r, which determine a_0(y) (through the sewing intertwining theorem). The Mellin transform I(s) = int a_0(y) y^{s-2} dy is then determined by a_0(y) for ALL s (by analytic continuation of the Mellin transform).

So in principle, the MC equation DOES constrain I(s) at complex s. But:

**(i) The constraint is vacuous.** The MC equation determines three numbers (kappa, alpha, S_4). The Mellin transform I(s) is an entire function of s (with finitely many poles from the asymptotic expansion of a_0). Three numbers cannot determine an entire function.

**(ii) The shadow tower determines a_0(y) only through the sewing intertwining.** The sewing intertwining theorem gives:

    F_1^conn(q; A) = sum_{r>=2} Sh_r^{(1)}(A) * G_r(q)

This is a formal series in the shadow amplitudes. The individual geometric kernels G_r(q) are functions of the elliptic curve. Their Mellin transforms against E(tau, s) involve higher RS integrals, not just the constrained Epstein zeta. The full chain:

    shadow tower -> F_1^conn(q) -> a_0(y) -> I(s) -> analytic continuation to complex s

requires computing the RS integral of each geometric kernel G_r against E_s, which is a separate computation for each r.

**(iii) For Heisenberg, the chain terminates and gives complete control.** The sewing-Selberg formula (thm:sewing-selberg-formula) computes:

    int log det(1-K) * E_s d mu = -2*(2pi)^{-(s-1)} * Gamma(s-1) * zeta(s-1) * zeta(s)

This is a PRODUCT of zeta functions, whose analytic continuation to complex s is completely explicit. The zeros of this product are the zeros of zeta(s-1) and zeta(s), which are the standard zeta zeros shifted by 0 and 1.

But this is NOT new information: the zeros of zeta are INPUTS to the Gamma/zeta product formula, not OUTPUTS of the shadow tower. The shadow tower for Heisenberg gives kappa = 1/2; the Mellin integral gives zeta(s-1)*zeta(s); the zeros of zeta are inherited from the standard zeta function, not derived from kappa.

**VERDICT: The spectral Wick rotation s -> s + i*theta is mathematically well-defined. The MC equation does constrain I(s) at complex s, but the constraint is too weak (three invariants vs an entire function) and the zeros of the continued integral are inherited from the zeta function, not derived from the shadow tower.**

---

## 4. Investigation 4: The Selberg Zeta Function and Resonances

### 4.1 The Selberg zeta function

For a Fuchsian group Gamma acting on H, the Selberg zeta function is:

    Z_Gamma(s) = prod_{gamma primitive} prod_{n>=0} (1 - N(gamma)^{-(s+n)})

where N(gamma) = exp(ell(gamma)) is the norm of the primitive geodesic gamma with length ell(gamma).

**Key properties (Selberg trace formula):**
- Z_Gamma(s) is entire (for co-compact Gamma) or meromorphic (for co-finite Gamma)
- The zeros on Re(s) = 1/2 are the spectral parameters s_j = 1/2 + it_j of the Laplacian eigenvalues lambda_j = 1/4 + t_j^2
- For co-compact Gamma: all spectral parameters are REAL, all zeros of Z_Gamma are on Re(s) = 1/2 or at non-positive integers (trivial zeros)
- For non-compact Gamma (e.g., SL(2,Z)): resonances appear. The scattering poles at s = rho/2 are related to the zeros of Z_Gamma through the determinantal identity:

    Z_Gamma(s) = phi(s) * Z_Gamma(1-s) * (explicit Gamma factors)

### 4.2 The real-to-complex transition IS a resonance phenomenon

For COMPACT hyperbolic surfaces: all Laplacian eigenvalues are real (self-adjoint operator on L^2). The spectral parameters s_j are real, and Z_Gamma(s) has all its nontrivial zeros on Re(s) = 1/2.

For NON-COMPACT surfaces (e.g., SL(2,Z)\H): the Laplacian is still self-adjoint on L^2, so eigenvalues are real. But the CONTINUOUS SPECTRUM introduces the scattering matrix phi(s), which has poles at complex spectral parameters. These are RESONANCES: they are NOT eigenvalues (they do not correspond to L^2 eigenfunctions) but they appear as poles of the resolvent (Delta - s(1-s))^{-1} when continued beyond L^2.

The real-to-complex transition is therefore:
- **L^2 spectrum** (eigenvalues) -> REAL spectral parameters (Selberg's theorem)
- **Resolvent continuation** (resonances) -> COMPLEX spectral parameters (scattering poles)

### 4.3 The sewing determinant as an analogue of Z_Gamma

The sewing Fredholm determinant det(1-K(tau)) = prod_{n>=1}(1-q^n) is an infinite product, structurally analogous to Z_Gamma(s) = prod_gamma prod_n (1 - N(gamma)^{-(s+n)}).

**The analogy (rem:selberg-trace-arithmetic, arithmetic_shadows.tex line 7384):**

| Selberg | Sewing |
|---------|--------|
| Geodesic lengths ell(gamma) | Sewing eigenvalues q^n = e^{2pi*i*n*tau} |
| Convergence for Re(s) > 1 | Convergence for |q| < 1 (Im(tau) > 0) |
| Continuation via trace formula | Continuation via modular transformation tau -> -1/tau |
| Zeros on Re(s) = 1/2 = Laplacian spectrum | Zeros of eta(tau) = cusps and CM points |
| Scattering poles at s = rho/2 | Poles of 1/eta(tau) = NONE (eta is entire and nonvanishing on H) |

### 4.4 The critical difference: eta has no zeros on H

The Dedekind eta function eta(tau) = q^{1/24} prod(1-q^n) is NONVANISHING on the upper half-plane H. It has zeros only at the cusps (tau -> i*infinity in any cusp). The function 1/eta(tau) = q^{-1/24} / prod(1-q^n) is holomorphic and nonvanishing on H.

Consequence: the sewing determinant det(1-K(tau)) = e^{-pi*i*tau/12} eta(tau) has NO ZEROS on H. Unlike the Selberg zeta function, which has zeros on the critical line corresponding to Laplacian eigenvalues, the sewing determinant has NO analogue of the spectral zeros.

**This is the root cause of the structural obstruction.** The Selberg zeta function encodes spectral data (eigenvalues as zeros). The sewing determinant encodes modular data (eta function, which is nonvanishing on H). The passage from spectral to modular replaces zeros with nonvanishing, and the spectral information (Laplacian eigenvalues, and hence their analytic continuation to resonances) is lost.

### 4.5 Could the resolvent approach help?

The resolvent (Delta - lambda)^{-1} of the Laplacian on SL(2,Z)\H continues meromorphically to lambda in C. Its poles at lambda = s_j(1-s_j) are the eigenvalues (real, discrete) and the resonances (complex, from the continuous spectrum).

The question: does the bar complex provide data that constrains the resolvent?

**Answer: NO.** The bar complex provides the sewing determinant det(1-K(tau)), which equals eta(tau) (up to normalization). The Kronecker limit formula connects log|eta|^2 to E_s(tau) at s = 1. The sewing-Selberg formula connects int log|eta|^2 * E_s d mu to zeta(s-1)*zeta(s). But these are all INTEGRAL identities: they relate the sewing determinant to AVERAGED spectral data (the RS integral), not to the resolvent at specific spectral parameters.

The resolvent at a specific lambda = s_0(1-s_0) requires POINTWISE information about the Green's function G(z, w; s_0) on SL(2,Z)\H. The bar complex provides GLOBAL information (the partition function, the sewing determinant). The passage from global to pointwise is the spectral decomposition, which requires the full Roelcke-Selberg theory (external to the bar construction).

**VERDICT: The real-to-complex transition IS a resonance phenomenon in spectral theory (compact -> non-compact, eigenvalues -> scattering poles). But the bar complex does not see the resolvent. It sees the sewing determinant, which is eta(tau), which is nonvanishing on H. The spectral zeros that would encode Laplacian eigenvalues are absent from the sewing determinant. The Selberg zeta function is a structurally richer object than the sewing determinant, and the Selberg trace formula provides input (closed geodesics) that the sewing formalism does not supply.**

---

## 5. Investigation 5: The Polyakov Complexification

### 5.1 The programme (constr:liouville-complexified)

The Polyakov-Alvarez formula represents the spectral determinant det'(-Delta_g) for g = e^{2sigma} g_0 as:

    log det'(-Delta_g) = log det'(-Delta_{g_0}) - S_L[sigma]/(6pi) + log(A_g/A_{g_0})

where S_L[sigma] = int (|nabla sigma|^2 + R_{g_0} sigma) dA is the Liouville action. The complexified Liouville integral (eq:complexified-liouville-integral):

    Z_L^C(tau) = int_C e^{-S_L[sigma]/(6pi)} D sigma

where C is a contour in the space of complex-valued conformal factors.

### 5.2 The genus-1 no-go (PROVED)

Proposition prop:genus-one-saddle-triviality (arithmetic_shadows.tex line 7326): For the flat torus E_tau with R_{g_0} = 0, the Liouville action S_L[sigma] = int |nabla sigma|^2 dA is a positive-definite quadratic functional. The Euler-Lagrange equation Delta sigma = 0 has sigma = const as its only periodic solution, for sigma real- or complex-valued. The complexified Liouville integral at genus 1 has no nontrivial complex saddle points.

**This is a theorem.** At genus 1, the "Wick rotation" of the Liouville field phi -> i*phi does not produce new saddle points. The partition function on the flat torus is entirely controlled by the Gaussian integral around sigma = const.

### 5.3 The genus >= 2 possibility (OPEN, HEURISTIC)

At genus g >= 2, the constant-curvature metric has R_{g_0} = -1 (hyperbolic). The Liouville action S_L[sigma] = int (|nabla sigma|^2 - sigma) dA is NO LONGER positive-definite: the linear term -sigma makes the functional unbounded below. The critical points of S_L are solutions to Delta sigma + 1 = 0, which has a unique solution sigma_0 (giving the hyperbolic metric) for REAL sigma, but may have additional solutions for COMPLEX sigma.

Conjecture conj:complex-saddle-scattering (arithmetic_shadows.tex line 7354, ClaimStatusHeuristic): At higher genus, complex saddles of the Liouville action contribute non-perturbative corrections e^{-S_L[sigma_*]/(6pi)} that are sensitive to the scattering poles. The real saddle reproduces I(s) (holomorphic at rho/2); the complex saddles contribute non-perturbative corrections that may have poles at rho/2.

### 5.4 Assessment of the Polyakov programme

**What is proved:**
- The sewing-spectral bridge (prop:sewing-spectral-bridge): det(1-K) and det'(-Delta) encode the same data (eta function)
- The RS meromorphic continuation (prop:rs-analytic-continuation): I(s) continues to all s in C
- Holomorphy at scattering poles (prop:scattering-residue): I(s) is holomorphic at s = rho/2
- Genus-1 saddle triviality (prop:genus-one-saddle-triviality): no complex saddles at genus 1

**What is heuristic/conjectural:**
- Complex saddle access to scattering poles (conj:complex-saddle-scattering): at genus >= 2, complex saddles may detect arithmetic
- The Selberg zeta bridge (rem:selberg-trace-arithmetic): structural analogy between sewing and Selberg, but the trace formula input is not supplied

**The structural assessment:** The Polyakov complexification is the RIGHT framework if one wants to access complex spectral parameters from the partition function. But it requires:

(a) Working at genus >= 2 (genus 1 is trivially Gaussian)
(b) Classifying the complex saddle points of the Liouville action on Sigma_g
(c) Computing the contribution of each complex saddle to the partition function
(d) Showing that these contributions have poles at s = rho/2

Each of these steps is genuinely hard and goes beyond the current bar formalism. Step (b) is a problem in complex geometric analysis (existence and classification of complex solutions to Delta sigma + R = 0 on compact Riemann surfaces). Step (d) would require a new mechanism connecting the action of complex saddles to the scattering matrix.

**VERDICT: The Polyakov complexification is the most conceptually promising approach. But it requires input (genus >= 2 complex saddle classification, non-perturbative partition function contributions) that is genuinely beyond the current algebraic machinery. The bar complex at genus >= 2 provides the modular MC element Theta_A, but the passage from Theta_A to complex saddle-point contributions has not been established.**

---

## 6. Synthesis: The Five Mechanisms Compared

| Mechanism | Math Status | Crosses Obstruction? | Why Not? |
|-----------|-------------|---------------------|----------|
| Complex c | Well-defined | NO | Still 3 invariants. Same finite determination. |
| Spectral s -> is | Well-defined | NO | MC constrains I(s) but too weakly (3 vs infinity). |
| Functional equation poles | PROVED (prop:scattering-residue) | N/A (they show WHERE zeros are, not HOW to find them from bar data) | RS unfolding erases scattering matrix. |
| Selberg zeta/resonances | Structural analogy only | NO | Sewing det = eta (nonvanishing on H). Selberg trace formula not supplied by bar. |
| Polyakov complexification | Genus 1: NO-GO proved. Genus >= 2: OPEN/HEURISTIC. | UNKNOWN | Requires complex saddle classification and non-perturbative contributions. |

### 6.1 The hierarchy of obstructions

**Level 0 (trivial):** The shadow tower is determined by three invariants. Three invariants cannot determine infinitely many zeros. This kills Mechanisms 1 and 2.

**Level 1 (structural):** The RS unfolding erases the scattering matrix. Algebraic constraints on the real spectral line cannot reach complex spectral parameters. This is rem:structural-obstruction (PROVED). This kills Mechanisms 3 and 4 in their naive form.

**Level 2 (geometric):** The Selberg zeta function has a richer zero structure than the sewing determinant (eta function), because it encodes geodesic data. The bar complex does not see geodesic data. This is the content of rem:selberg-trace-arithmetic.

**Level 3 (non-perturbative):** Complex saddle points of the Liouville action at genus >= 2 could potentially access the scattering poles. But this requires genuinely new input: the bar complex in its current form produces the PERTURBATIVE partition function (the sewing expansion), not the non-perturbative completion. The Polyakov complexification is a framework for the non-perturbative completion, but constructing it is an open problem.

### 6.2 The Wick rotation is NOT a bridge

In QFT, the Wick rotation tau_E = i*tau_M converts between Euclidean and Minkowski signatures. It succeeds because:
(a) The rotation is a 90-degree rotation in a single complex plane (time)
(b) The OS axioms (Osterwalder-Schrader) guarantee that the rotation preserves the physical content
(c) The rotation acts on the SPACETIME coordinates, which enter the path integral through the action

In the spectral theory setting, the analogous rotation would be:
(a) s -> is (spectral variable) or c -> ic (central charge) or tau -> i*tau (modular parameter)
(b) No OS-type axiom guarantees that the rotation preserves the arithmetic content
(c) The rotation acts on SPECTRAL parameters, which do NOT enter the path integral through the action

**The fundamental difference:** In QFT, Wick rotation connects two FORMULATIONS of the same theory (Euclidean and Minkowski). In spectral theory, "Wick rotation" would need to connect two DIFFERENT OBJECTS (the RS spectral coefficients c(t) on the real line and the scattering matrix phi(s) in the complex plane). These are not two formulations of the same thing; they are two different mathematical objects that are related by the Eisenstein functional equation, which is external to the bar construction.

### 6.3 What would work

A mechanism that WOULD cross the structural obstruction would need to provide:

**(a) Infinitely many independent constraints** from the MC equation (not just three invariants). This would require the MC equation to constrain the FULL primary spectrum, not just the shadow tower on a single primary line.

**(b) Constraints at COMPLEX spectral parameters.** This would require the RS integral (or some analogue) to retain the scattering matrix, i.e., to NOT unfold. A "non-unfolded" RS integral is the geometric integral int Z-hat^c * E_s d mu at complex s, which requires the Eisenstein series at complex s, which is the scattering problem itself.

**(c) A positivity mechanism.** Even with constraints at complex spectral parameters, one would need a POSITIVITY argument (like the Li criterion) to force zeros onto the critical line. The sewing-lift Li coefficients are eventually negative (prop:li-criterion-failure, verified computationally at n = 7 for Heisenberg).

No current mechanism provides any of (a), (b), or (c). The honest assessment from working_notes.tex (lines 3290-3310) is correct:

> "The programme does not produce a critical-line theorem. The structural obstruction is that the shadow spectral measure and the automorphic spectral measure are different objects, and the map between them (the Rankin-Selberg integral) is not sign-preserving. No mechanism for positivity has been identified."

---

## 7. Detailed Assessment of Each Investigation Point

### Point 1: Shadow tower S_r(c) as rational function of c

S_r(c) is a rational function of c for each r >= 2. At real c > 0: the shadow metric Q_L has discriminant -32*kappa^2*Delta with Delta = 40/(5c+22) > 0, giving complex conjugate branch points. At complex c: Q_L has branch points in C^2 (no longer paired by complex conjugation unless c is real).

**New analytic structure at complex c?** YES, formally: the branch cut of sqrt(Q_L) is an arc in the complex t-plane whose position depends on c, and as c varies in C, this arc moves. The monodromy representation of the fundamental group pi_1(C - branch_locus) changes: at real c, the monodromy is Z/2 (the Koszul sign); at complex c, it remains Z/2 (topological invariance under continuous deformation). The PERIOD MATRIX of the algebraic curve y^2 = Q_L(t) (a genus-0 curve with 2 branch points) is trivial in all cases (genus 0 has no periods). So the new analytic structure is confined to the POSITION of the branch points, not to any modular/period data.

**Does this help?** NO. The position of the branch points determines the convergence radius rho and the shadow growth rate, but these are continuous functions of c and carry no number-theoretic information. The discriminant field Q(c)(sqrt(Delta)) at irrational complex c is isomorphic to Q(c) itself (since sqrt(Delta) in C is just a complex number), so the arithmetic content (which requires Delta to be in a specific number field) is absent at generic complex c.

### Point 2: Where complex spectral parameters enter

ANSWERED IN FULL in Section 2 above. They enter through the functional equation factor F_c(s), specifically through zeta(2s-1) = 0 at s = (1+rho_n)/2. The RS integral I(s) is holomorphic at these points (PROVED). The poles are in the functional equation, not in the integral.

### Point 3: The functional equation factor

ANSWERED IN FULL. The functional equation of epsilon^c_s inherits poles from zeta(2s-1) = 0. These poles are UNIVERSAL (same for every CFT at every c). Their residues are CFT-specific. The bar complex constrains neither.

### Point 4: The spectral Wick rotation s -> s + i*theta

ANSWERED IN FULL in Section 3. Mathematically well-defined but provides no new constraints: the MC equation determines three invariants, which cannot control the analytic continuation of I(s) (an entire function of s with finitely many poles).

### Point 5: The Selberg zeta and resonances

ANSWERED IN FULL in Section 4. The real-to-complex transition IS a resonance phenomenon for non-compact surfaces. The Laplacian eigenvalues (L^2 spectrum) are real; the scattering resonances (resolvent poles) are complex. The bar complex does not see the resolvent: it sees the sewing determinant (eta), which has no zeros on H. The Selberg zeta function is a richer object than the sewing determinant because it encodes geodesic data, which is not supplied by the bar construction.

---

## 8. Three Honest Positive Results

Despite the negative results above, the investigation clarifies three genuine mathematical structures:

### 8.1 The sewing-spectral bridge is a proved theorem

The identity det'(-Delta_{E_tau}) = 4pi^2 y |eta|^4 (prop:sewing-spectral-bridge) connects the algebraic sewing determinant to the spectral zeta determinant. This is a genuine bridge between the bar complex (which produces eta through the sewing expansion) and the spectral theory of the Laplacian (which produces det'(-Delta) through the eigenvalue zeta function). The bridge is EXACT and PROVED.

### 8.2 The Kronecker-Selberg hierarchy extends the bridge

The sewing-Selberg formula extends the Kronecker limit formula to all spectral parameters s:

    int log det(1-K) * E_s d mu = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)

This gives complete control of the RS integral for Heisenberg (where F_1 = kappa * G_2 and the tower terminates). For interacting theories, the sewing intertwining theorem provides an infinite series of corrections, each involving a different geometric kernel G_r and a different RS integral.

### 8.3 The depth decomposition is proved and structurally illuminating

The depth decomposition d(A) = 1 + d_arith(A) + d_alg(A) separates arithmetic content (L-functions, critical lines) from homotopy-theoretic content (A-infinity non-formality, Maass projections). This is a genuine structural theorem that classifies the different types of spectral data carried by the bar complex.

---

## 9. Falsification Notes

### 9.1 False claim tested and rejected: "Wick-rotating c accesses zeta zeros"

The investigation shows this is false at Level 0 (finite determination). The shadow tower at complex c carries the same three invariants as at real c.

### 9.2 False claim tested and rejected: "The RS integral can be continued to scattering poles"

The RS integral CAN be continued to complex s (prop:rs-analytic-continuation, PROVED). But it is HOLOMORPHIC at the scattering poles (prop:scattering-residue, PROVED). Continuation to complex s does not produce singularities at the zeta zeros.

### 9.3 False claim tested and rejected: "The Selberg zeta provides a model for the sewing determinant"

The Selberg zeta and the sewing determinant are structurally analogous but mathematically different. The Selberg zeta has zeros on Re(s) = 1/2 (Laplacian eigenvalues); the sewing determinant (eta function) has NO zeros on H. The trace formula input that gives the Selberg zeta its rich zero structure is absent from the sewing formalism.

### 9.4 Verified claim: "The structural obstruction is a theorem"

The structural obstruction (rem:structural-obstruction) is correct and proved. The separation between real spectral parameters (MC constraints) and complex spectral parameters (zeta zeros) is structural and cannot be crossed by algebraic means within the bar formalism.

### 9.5 Status of conj:complex-saddle-scattering

The Polyakov complexification conjecture (conj:complex-saddle-scattering, ClaimStatusHeuristic) remains the only mechanism that COULD potentially cross the obstruction. It requires:
- Genus >= 2 (genus 1 is no-go, proved)
- Complex saddle classification for the Liouville action on compact Riemann surfaces
- Non-perturbative contributions from complex saddles
- A mechanism connecting these contributions to scattering poles

Each requirement is genuinely open. The conjecture is correctly tagged as heuristic.

---

## 10. Cross-References

### Manuscript source (Vol I, ~/chiral-bar-cobar):
- rem:structural-obstruction: arithmetic_shadows.tex line 300
- prop:scattering-residue: arithmetic_shadows.tex line 7093
- prop:sewing-spectral-bridge: arithmetic_shadows.tex line 6941
- prop:rs-analytic-continuation: arithmetic_shadows.tex line 7046
- prop:genus-one-saddle-triviality: arithmetic_shadows.tex line 7326
- conj:complex-saddle-scattering: arithmetic_shadows.tex line 7354
- rem:selberg-trace-arithmetic: arithmetic_shadows.tex line 7384
- thm:riccati-algebraicity: higher_genus_modular_koszul.tex line 14827
- thm:shadow-radius: higher_genus_modular_koszul.tex (via shadow_radius.py)

### Compute layer:
- scattering_resonance.py: scattering matrix, spectral zeta, Selberg trace formula
- roelcke_selberg_decomposition.py: RS decomposition of Ising model, Maass content verification
- spectral_continuation.py: Mellin continuation functor, shadow-Hecke identification
- shadow_singularity_map.py: branch point classification, resurgent structure
- shadow_radius.py: convergence radius, branch point positions

### Audit documents:
- mc_spectral_measure.md: definitive analysis of shadow-spectral relationship
- roelcke_selberg.md: precise spectral-theoretic content of epsilon^c_s
- level_2_3_functional_equation.md: functional equations of sewing-Dirichlet lift

### Vol II (~/chiral-bar-cobar-vol2/archive/source_tex):
- working_notes.tex lines 2550-2700: structural obstruction section
- working_notes.tex lines 3280-3460: spectrum and gravity, honest assessment
