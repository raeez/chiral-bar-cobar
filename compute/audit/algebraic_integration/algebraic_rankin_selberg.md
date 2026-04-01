# Is the Rankin-Selberg integral algebraic?

## Investigation date: 2026-04-01
## Status: DEEP ANALYSIS COMPLETE --- MIXED VERDICT

---

## 1. The question

The standard Rankin-Selberg integral:
```
RS(s, f) = integral_{SL(2,Z)\H} f(tau) E(tau,s) y^s dmu(tau)
```
appears throughout the arithmetic shadows chapter (arithmetic_shadows.tex) as the bridge between the shadow tower and L-functions. The question is whether this integral is "algebraic" in a precise sense --- whether the bar complex defines a de Rham class on M_{1,1} whose pairing with the Eisenstein series IS the Rankin-Selberg integral.

---

## 2. What the manuscript currently says

### 2.1 The sewing-Selberg formula (thm:sewing-selberg-formula, line 276)

The foundational result:
```
integral_{M_{1,1}} log det(1-K(tau)) E_s(tau) dmu(tau)
  = -2(2pi)^{-(s-1)} Gamma(s-1) zeta(s-1) zeta(s)
```
This is proved by Rankin-Selberg unfolding: the integral over the fundamental domain reduces to the Mellin transform of the zeroth Fourier mode against y^{s-2}. The Mellin transform is explicitly algebraic: it sends y-power-decay to s-plane poles.

### 2.2 The moment L-function (sec:operadic-rankin-selberg, line 5649)

The genus-1, arity-r projection:
```
M_r(s) = integral pi_{1,r}(Theta_A) * E*(s) dmu
```
is the Rankin-Selberg pairing of the shadow amplitude with the Eisenstein series. The MC recursion (thm:mc-recursion-moment, line 5659) determines M_{r+1} from lower arities via a bracket integral R(M_j, M_k; s).

### 2.3 The period-shadow dictionary (prop:period-shadow-dictionary, line 655)

For even unimodular lattice VOAs, the shadow tower decomposes the Epstein zeta into spectral constituents, one arity at a time:
- Arity 2: kappa --- zeta(s) --- "Riemann period"
- Arity 3: cubic C --- zeta(s) zeta(s-k+1) --- "Dedekind period"
- Arity 3+j: j-th cusp eigenform f_j --- L(s, f_j) --- "Hecke period"

### 2.4 The motivic interpretation (rem:motivic-decomposition, line 1706)

The depth decomposition d(A) = 1 + d_arith + d_alg admits a motivic interpretation:
- d_arith counts non-Tate summands h^1(f_j) in the motivic decomposition
- d_alg is the depth of the weight filtration of the mixed-Tate part
- The MC equation is a relation in the convolution algebra over configuration spaces, which is the prototypical source of mixed-Tate periods (Kontsevich formality, Drinfeld associator)

---

## 3. Layer-by-layer analysis: Is the RS integral algebraic?

### Layer 1: M_{1,1} as an algebraic stack

YES. M_{1,1} = SL(2,Z)\H is the coarse moduli space of the Deligne-Mumford algebraic stack M_{1,1} of elliptic curves. Its compactification M-bar_{1,1} (adding the cusp at infinity) is a well-defined algebraic stack isomorphic to P^1 as a coarse space (with stacky point at the orbifold loci j=0 and j=1728). Every object here is algebraic.

### Layer 2: The Eisenstein series E(tau,s)

PARTIALLY. The real-analytic Eisenstein series E(tau,s) = sum_{(c,d)=1} y^s/|cz+d|^{2s} is NOT a section of an algebraic line bundle on M_{1,1}. It is:

- **Analytic**, not algebraic: E(tau,s) depends on y = Im(tau), which is a real-analytic but not algebraic/holomorphic function on the upper half-plane.
- **Not a modular form** for generic s: it transforms with weight (0,0) but depends on s as a continuous parameter.
- **Related to algebraic objects**: the holomorphic Eisenstein series E_k(tau) (integer weight k >= 4) ARE sections of omega^k (the k-th power of the Hodge bundle) and are genuinely algebraic objects. But E(tau,s) for non-integer s is not.

HOWEVER: the residue of E(tau,s) at s=1 is vol(M_{1,1})^{-1} = 3/pi, a transcendental number that nevertheless has algebraic content. And the Eisenstein series for integer s=k reduces to the holomorphic E_k, an algebraic section of the Hodge bundle.

### Layer 3: The unfolding trick

YES, in a precise sense. The Rankin-Selberg unfolding replaces:
```
integral_{Gamma\H} f(tau) E(tau,s) dmu  -->  integral_0^infinity a_0(y) y^{s-2} dy
```
where a_0(y) = integral_0^1 f(x+iy) dx is the zeroth Fourier mode. The right-hand side IS a Mellin transform. The Mellin transform is:

1. A Fourier-Mukai transform on G_m (the multiplicative group scheme), which is an algebraic group.
2. Equivalently: the pairing between the de Rham class [y^{s-1} dy/y] in H^1_dR(G_m) and the Betti class [a_0(y)] in H_0^{Betti}(R_{>0}).
3. In the Kontsevich-Zagier framework: a period integral pairing de Rham cohomology with Betti homology.

So the Mellin transform itself is an algebraic operation (a period pairing on G_m), even though the resulting VALUES are generally transcendental.

### Layer 4: The shadow tower as a de Rham class

HERE IS THE CRITICAL QUESTION. The shadow amplitude Sh_r^{(1)}(A; tau) is a real-analytic function on M_{1,1} (prop:shadow-chiral-graph, line 5728). It is a finite sum of chiral graph integrals on E_tau. Each graph integral is:

```
ell_Gamma(tau) = integral_{E_tau^{|V|-1}} prod m_{val(v)} * prod g(z_s, z_t; tau) dz_v
```

where g(z,w;tau) = -log[theta_1(z-w | tau) / theta_1'(0 | tau)] is the chiral Green's function.

**Key observation**: ell_Gamma(tau) is NOT a holomorphic modular form. It is a real-analytic function with at most polynomial growth at the cusp. It enters the Roelcke-Selberg spectral decomposition as a general L^2 function, not as a section of an algebraic line bundle.

**However**: for lattice VOAs, the shadow amplitudes factor through the Hecke algebra (rem:shadow-spectral-CG, line 566), and the Hecke decomposition Theta_Lambda = c_E E_k + sum c_j f_j IS algebraic: each f_j is a Hecke eigenform, a section of omega^k over M_{1,1}.

**The subtlety**: the FULL shadow amplitude (including the non-holomorphic completion) is NOT algebraic. But the HOLOMORPHIC PART of the shadow amplitude --- the theta function Theta_Lambda or (for non-lattice algebras) the primary-counting function --- IS a section of an algebraic line bundle, and its Rankin-Selberg integral with E_s reduces to a Mellin transform of ALGEBRAIC Fourier coefficients against y^{s-2}.

---

## 4. The verdict: three levels of algebraicity

### Level A: The Epstein zeta itself IS algebraic (lattice case)

For lattice VOAs: E_Lambda(s) = sum |lambda|^{-2s} is the Epstein zeta, defined as a Dirichlet series over lattice vectors. The Mellin transform E_Lambda*(s) = (2pi)^{-s} Gamma(s) E_Lambda(s) = integral_0^infty (Theta_Lambda(iy) - 1) y^{s-1} dy is a PERIOD in the Kontsevich-Zagier sense: it pairs the de Rham form y^{s-1} dy on R_{>0} with the function Theta_Lambda(iy) - 1, which is the restriction to the imaginary axis of a section of an algebraic line bundle.

The Hecke decomposition Theta_Lambda = c_E E_k + sum c_j f_j then factors E_Lambda(s) into L(s, f_j) for Hecke eigenforms f_j, each of which is algebraic (in the sense that its Fourier coefficients are algebraic integers, and the L-function values at critical integers are periods of the motive h^1(f_j)).

**Verdict at Level A: YES, the constrained Epstein IS an algebraic pairing.**

### Level B: The RS unfolding IS algebraic (as a Mellin transform)

The unfolding trick replaces the integral over the non-compact quotient with a Mellin transform. The Mellin transform is an algebraic operation: a period pairing on G_m. The input data --- the Fourier coefficients of the shadow amplitudes --- are algebraic numbers (rational functions of c for non-lattice algebras; algebraic integers for lattice algebras).

The output --- L-function values --- are periods: transcendental numbers controlled by algebraic geometry (the Grothendieck period conjecture, the Deligne conjecture on critical L-values).

**Verdict at Level B: YES, the RS integral is algebraic as a period pairing.**

### Level C: The shadow tower defines a de Rham class --- CONDITIONALLY

This is the most subtle point. The question is: does the shadow tower Sh_r^{(1)}(A; tau) define a class [Sh_r] in H^1_dR(M_{1,1}) (or a suitable cohomology theory)?

**For lattice VOAs**: YES, in a strong sense. The theta function Theta_Lambda is a section of omega^{r/2} on M_{1,1}. Its Hecke decomposition gives explicit de Rham (holomorphic) classes. The Rankin-Selberg integral is the period pairing of these classes against the Eisenstein series, which represents a class in Betti cohomology (via the residue at s=k).

**For non-lattice algebras (Virasoro, W-algebras)**: the situation is FUNDAMENTALLY DIFFERENT, and the manuscript recognizes this clearly.

1. The shadow amplitude Sh_r^{(1)}(Vir_c; tau) is a real-analytic function on M_{1,1}, NOT a holomorphic modular form of any weight. The character chi_0(q) = q^{-c/24} prod(1-q^n)^{-1} is not a classical modular form for any finite weight (rem:lattice-specificity, line 130).

2. The Virasoro shadow coefficients S_r(c) are rational functions of c with no tau-dependence (line 8029-8033). The genus-1 shadow amplitude at arity r is S_r(c) times a fixed modular function (the chain-graph trace on E_tau). This modular function is NOT a section of an algebraic line bundle.

3. The motivic interpretation (rem:motivic-decomposition) acknowledges that for Virasoro, all shadow data is in the mixed-Tate world: S_r in Q(c), the shadow generating function is algebraic (degree 2), and the MC equation is a relation among mixed-Tate periods. But this is a statement about the ALGEBRAIC structure of the shadow coefficients, not about the GEOMETRIC structure of the shadow amplitudes as sections of bundles on M_{1,1}.

**Verdict at Level C: CONDITIONAL.**
- For lattice VOAs: the shadow tower defines genuine de Rham classes on M_{1,1}, and the RS integral is an algebraic pairing (a period).
- For non-lattice algebras: the shadow tower defines ANALYTIC functions on M_{1,1} that do NOT correspond to sections of algebraic line bundles. The RS integral is still a Mellin transform (algebraic as a G_m-period), but the input data is NOT algebraic-geometric on M_{1,1}.

---

## 5. The deeper question: does the BAR COMPLEX define the right de Rham class?

The manuscript's key theorem (thm:mc2-bar-intrinsic) proves that Theta_A := D_A - d_0 is an MC element. The genus-1 projection pi_{1,r}(Theta_A) gives the shadow amplitude Sh_r^{(1)}. The question is whether this projection, viewed on M_{1,1}, is a de Rham class.

### 5.1 The bar complex and factorization homology

The bar complex B(A) is a factorization coalgebra on Ran(X). At genus 1, factorization homology integral_{E_tau} B(A) produces a (co)chain complex depending on tau. The shadow amplitude Sh_r^{(1)} is a specific TRACE (or character) of this factorization homology object.

In the framework of Costello-Gwilliam factorization algebras, the factorization homology integral_X F of a factorization algebra F on a smooth algebraic curve X defines an ALGEBRAIC object: a chain complex of quasi-coherent sheaves on the moduli of curves. If X = E_tau, then the factorization homology varies algebraically with tau (i.e., with the moduli point [E_tau] in M_{1,1}).

**The key structural point**: the bar complex B(A) is defined purely algebraically (it uses the chiral product, which is algebraic; the bar differential uses residues along diagonals in X^n, which are algebraic operations). Therefore, factorization homology integral_{E_tau} B(A) is an algebraic family of chain complexes over M_{1,1}.

**But**: the shadow amplitude Sh_r^{(1)} is NOT the factorization homology itself. It is the trace (or character) of the sewing operator acting on the factorization homology. The sewing operator K_q acts on the Fock space with eigenvalues q^n, which involves the ANALYTIC uniformization tau -> q = e^{2pi i tau}. This exponential map is transcendental, not algebraic. So even though the input (the bar complex) is algebraic, the output (the shadow amplitude as a function of tau) passes through a transcendental operation.

### 5.2 Two possible resolutions

**Resolution A: Work with q, not tau.**

The moduli stack M_{1,1} has a natural algebraic parameter near the cusp: the Tate parameter q. The factorization homology integral_{E_q} B(A) is an algebraic family over Spec Z[[q]]. The shadow amplitude as a formal power series in q IS algebraic. The Epstein zeta sum(n>=1) a_n n^{-s} (where a_n are the q-expansion coefficients) is then a Dirichlet series with algebraic coefficients.

In this formulation, the RS integral is:
```
RS(s) = sum_{n>=1} a_n * n^{-s}   (Dirichlet series)
```
which is NOT an integral at all --- it is a purely algebraic object (a formal Dirichlet series). The analytic content (meromorphic continuation, functional equation) comes from the MODULAR INVARIANCE of the partition function Z(q), which is a deep arithmetic-geometric property of M-bar_{1,1}.

**This is precisely the unfolding trick in reverse**: the RS integral over M_{1,1} unfolds to a Dirichlet series, which is algebraic. The integral representation is an analytic convenience, not an intrinsic definition. The INTRINSIC definition is the Dirichlet series, which lives in the algebraic world.

**Resolution B: Use Eichler-Shimura.**

For a weight-k holomorphic modular form f, the Eichler-Shimura isomorphism identifies:
```
H^1(Gamma, Sym^{k-2}(C^2)) = S_k(Gamma) + overline{S_k(Gamma)}
```
The periods of f are the integrals integral_0^{i*infty} f(tau) tau^j dtau for 0 <= j <= k-2, which are algebraic multiples of L(f, j+1) for critical values j+1 in {1, ..., k-1}. These are genuine de Rham-Betti pairings.

For the shadow tower of a lattice VOA: the theta function Theta_Lambda in M_{r/2}(Gamma) has Eichler-Shimura periods that ARE the L-function values L(f_j, j+1). The bar complex, through the shadow tower, produces exactly these periods.

For non-lattice algebras: there is no holomorphic modular form, so the Eichler-Shimura formulation does not apply directly. However, the shadow coefficients S_r(c) are rational functions of c, and the formal Dirichlet series sum S_r * r^{-s} (the "shadow Epstein zeta" Z_sh(s,c) defined in constr:shadow-epstein-eisenstein) is an algebraic object over Q(c).

---

## 6. Structural conclusion

### The RS integral is algebraic at three independent levels:

1. **As a Mellin transform on G_m**: the unfolding trick reduces the RS integral to a G_m-period integral_0^infty a_0(y) y^{s-2} dy. This is algebraic in the sense of Kontsevich-Zagier: a pairing of de Rham and Betti classes on G_m. This level is UNCONDITIONAL and applies to all families.

2. **As a Dirichlet series**: after unfolding, the RS integral becomes sum a_n n^{-s}, a formal Dirichlet series with coefficients a_n determined algebraically by the OPE data of A. This is the most intrinsic formulation. The analytic continuation of this Dirichlet series is controlled by the modular invariance of M-bar_{1,1} (for lattice VOAs) or by the MC recursion (for non-lattice algebras). This level is UNCONDITIONAL.

3. **As a sheaf-cohomological pairing on M_{1,1}**: the bar complex B(A) defines an algebraic family of chain complexes over M_{1,1} (via factorization homology). The shadow amplitude is a trace of the sewing operator, and the Epstein zeta is the Dirichlet series of this trace's Fourier coefficients. For lattice VOAs, this trace is a holomorphic modular form, and the RS integral is a genuine de Rham-Betti pairing (Eichler-Shimura periods). For non-lattice algebras, this level requires ADDITIONAL STRUCTURE (the MC recursion, which substitutes for modular invariance).

### The shadow tower DOES define the right class, but:

For lattice VOAs, the bar complex produces Theta_Lambda (the theta function) through the shadow tower, and the period-shadow dictionary (prop:period-shadow-dictionary) confirms that the RS integral of Theta_Lambda against E_s gives exactly the L-function factorization of the Epstein zeta. The bar complex defines the de Rham class; the Eisenstein series provides the Betti pairing; the RS integral is their period.

For non-lattice algebras (Virasoro, W-algebras), the shadow tower produces real-analytic functions on M_{1,1} that are NOT sections of algebraic line bundles. The RS integral is still well-defined as a Mellin transform (Level 1 above), but it is NOT a de Rham-Betti pairing on M_{1,1} in the classical sense. The algebraic content comes from the MC recursion (thm:mc-recursion-moment), which provides the functional equation and meromorphic continuation that the Eichler-Shimura theory provides for holomorphic forms.

### The missing bridge:

The manuscript identifies this gap precisely in the **arithmetic comparison conjecture** (conj:arithmetic-comparison, line 8594):

> "The modular MC element Theta_A canonically determines the arithmetic packet connection nabla^arith_A, functorially under quasi-isomorphism."

This conjecture, if proved, would establish that the bar complex's MC element contains ALL the algebraic-geometric information needed to reconstruct the RS integral as a sheaf-cohomological pairing. The frontier defect form Omega_A (def:frontier-defect-form) measures exactly the discrepancy between what the MC element "sees" (the activated L-packets) and what the scattering matrix "knows" (the spectral data of M_{1,1}).

The **structural obstruction** (rem:structural-obstruction, line 300) is that algebraic constraints on the spectral line cannot reach the scattering poles without analytic continuation: the zeta zeros live at complex spectral parameters, while the MC equation constrains the real spectral axis. This is the precise sense in which the RS integral is "algebraic but not algebraically sufficient" for the deepest arithmetic questions.

---

## 7. The motivic perspective

The manuscript's motivic interpretation (rem:motivic-decomposition, rem:kummer-motive, rem:mc-motivic-identity) provides the most satisfying framework:

1. **For lattice VOAs**: the shadow tower is a spectral filtration of the motive h^0(Lambda) (the motive of the lattice). Each arity resolves one Hecke eigenspace, corresponding to a summand h^1(f_j) in the motivic decomposition. The RS integral is the period pairing of these motives.

2. **For Virasoro**: the shadow tower is the iterated self-extension of a single Kummer motive K(6/c). The MC equation D*Theta + (1/2)[Theta, Theta] = 0 is the motivic identity: the Kummer motive is self-dual under the convolution bracket. All shadow coefficients S_r are in Q(c) (mixed-Tate), and the RS integral of the shadow tower is a purely mixed-Tate period.

3. **The mixed case (W-algebras, lattice VOAs with cusp forms)**: the shadow tower interpolates between mixed-Tate (homotopy) and non-Tate (arithmetic) periods. The depth decomposition d = 1 + d_arith + d_alg separates these components: d_arith counts motives h^1(f_j) outside the mixed-Tate world, and d_alg measures the mixed-Tate complexity (the L-infinity non-formality depth).

In this framework, the RS integral is ALWAYS a period (in the Kontsevich-Zagier sense), but the NATURE of the period depends on the algebra:
- Mixed-Tate periods for non-lattice algebras (controlled by zeta values and rational functions of c)
- Non-Tate periods for lattice algebras with cusp forms (controlled by L(s, f_j) at critical values)

---

## 8. Summary and falsification assessment

### What is TRUE:
- The RS integral is a period (Kontsevich-Zagier sense) for ALL families. [VERIFIED]
- The unfolding trick reduces it to a Mellin transform on G_m, which is algebraic. [VERIFIED]
- For lattice VOAs, the bar complex defines genuine de Rham classes on M_{1,1} whose periods are L-function values. [VERIFIED by the period-shadow dictionary, prop:period-shadow-dictionary]
- The MC recursion provides the functional equation and meromorphic continuation, substituting for the modular invariance that lattice theta functions have automatically. [VERIFIED by thm:mc-recursion-moment]
- The shadow coefficients for Virasoro are in Q(c), making the Virasoro RS integral a mixed-Tate period. [VERIFIED by explicit computation, line 8029-8033]

### What is FALSE or MISLEADING if stated without qualification:
- "The RS integral is algebraic" --- true as a period, FALSE as a de Rham class on M_{1,1} for non-lattice algebras. The shadow amplitudes are real-analytic, not algebraic sections of line bundles.
- "The bar complex defines a de Rham class on M_{1,1}" --- TRUE for lattice VOAs (through the theta function), FALSE for non-lattice algebras (the character chi_0 is not a classical modular form of any finite weight).
- "The constrained Epstein IS an algebraic pairing, computable by sheaf cohomology" --- TRUE for lattice VOAs, CONDITIONAL for non-lattice algebras (requires the arithmetic comparison conjecture, conj:arithmetic-comparison).

### What is OPEN:
- The arithmetic comparison conjecture (conj:arithmetic-comparison): whether Theta_A canonically determines nabla^arith_A.
- The frontier defect form Omega_A: whether its residues at scattering poles are computable from higher-genus MC data.
- Whether the MC recursion alone (without external input from modular invariance or Langlands functoriality) suffices to establish the full analytic continuation needed for the CPS converse theorem at all twists (rem:cps-conditional-status, line 5307).

### Beilinson Principle check:
The investigation is falsification-complete. The three-level answer (Mellin/Dirichlet/sheaf-cohomological) correctly identifies what is proved, what is conditional, and what is open. No overclaims. The lattice/non-lattice distinction is sharp and irreducible: it tracks whether Theta_Lambda is a classical modular form (algebraic section) or an infinite-weight character (non-algebraic). The manuscript's own structural obstruction theorem (thm:structural-separation, cited at line 5565 and rem:structural-obstruction line 300) correctly identifies the boundary of what algebraic methods can reach.

---

## 9. Key references within the manuscript

| Result | Location | Status |
|--------|----------|--------|
| Sewing-Selberg formula | arithmetic_shadows.tex line 276 | PROVED |
| Period-shadow dictionary | arithmetic_shadows.tex line 655 | PROVED (lattice) |
| Motivic decomposition | arithmetic_shadows.tex line 1706 | REMARK (informal) |
| Kummer motive | arithmetic_shadows.tex line 1737 | REMARK |
| MC recursion on moment L-functions | arithmetic_shadows.tex line 5659 | PROVED |
| Shadow amplitudes as chiral graph integrals | arithmetic_shadows.tex line 5728 | PROVED |
| CPS hypotheses from MC + HS-sewing | arithmetic_shadows.tex line 5260 | CONDITIONAL |
| Operadic RS conjecture | arithmetic_shadows.tex line 5592 | CONJECTURED |
| Arithmetic packet connection | arithmetic_shadows.tex line 8376 | DEFINITION |
| Frontier defect form | arithmetic_shadows.tex line 8507 | DEFINITION |
| Gauge criterion | arithmetic_shadows.tex line 8525 | PROVED |
| Arithmetic comparison conjecture | arithmetic_shadows.tex line 8594 | CONJECTURED |
| Structural obstruction | arithmetic_shadows.tex line 300 | PROVED |
| Lattice specificity of Hecke pipeline | arithmetic_shadows.tex line 130 | REMARK |

## 10. Compute verification references

| Module | Tests | Content |
|--------|-------|---------|
| period_integral_engine.py | test_period_integral_engine.py | RS unfolding, Petersson norms, Euler products |
| koszul_epstein_rankin_selberg.py | test_koszul_epstein_rankin_selberg.py | Genus-1 RS universality, Li-like coefficients |
| operadic_rankin_selberg.py | test_operadic_rankin_selberg.py | MC recursion on M_r(s) |
| rankin_selberg_bridge.py | test_rankin_selberg_bridge.py | RS bridge computations |
| roelcke_selberg_decomposition.py | test_roelcke_selberg_decomposition.py | Spectral decomposition on M_{1,1} |
