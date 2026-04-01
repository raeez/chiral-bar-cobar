# Level 2 to Level 3: Sewing as (Generalized) Poisson Summation

## Summary

The bar complex sewing operation is Poisson summation for abelian algebras (Heisenberg, lattice VOAs) and fails to be Poisson summation in any classical sense for non-lattice algebras (Virasoro at generic c, W-algebras). The obstruction is precise: Poisson summation requires a lattice (or at minimum an abelian group structure on the state space), and the sewing of non-abelian chiral algebras sums over a basis of states that carries no such structure. The manuscript already identifies the correct generalization: the bar construction is a non-abelian Fourier transform (Chapter "The Fourier seed," fourier_seed.tex), and the Weyl group character formula replaces the dual-lattice sum (rem:weyl-nonabelian-fourier in free_fields.tex). Whether this constitutes a "generalized Poisson summation" is a question of definition, not of mathematics.

## 1. Heisenberg: sewing IS Poisson summation

### The mechanism

The Heisenberg algebra H_k at level k has genus-1 partition function

    Z_1(H_k; tau) = Tr_{H_k} q^{L_0 - c/24} = 1/eta(tau) = q^{-1/24} prod_{n>=1} 1/(1 - q^n)

for a single boson (c = 1, kappa = k). For rank r, the partition function is eta(tau)^{-r}.

The Dedekind eta function satisfies

    eta(-1/tau) = sqrt(-i*tau) * eta(tau).

This IS Poisson summation. The standard proof: write 1/eta(tau) via the Euler product, take logarithm to get -sum_{n>=1} log(1 - q^n) = sum_{n>=1} sum_{m>=1} q^{nm}/m, interchange summation order, and recognize the result as a sum over the lattice Z which transforms under tau -> -1/tau by Poisson summation on Z.

More precisely, the Jacobi triple product gives

    eta(tau)^{-1} = q^{-1/24} sum_{n in Z} (-1)^n q^{n(3n-1)/2}  (pentagonal numbers)

but this is not quite the right way to see it. The cleaner route: the genus-1 sewing of the Heisenberg is a Fredholm determinant (thm:heisenberg-sewing, clause (iv)):

    Z_1 = det(1 - K_q)^{-1}

where K_q is the one-particle Bergman sewing operator. On the one-particle space (weight-1 states), K_q has eigenvalues {q^n : n >= 1}, each with multiplicity 1. The Fredholm determinant factors as

    det(1 - K_q) = prod_{n >= 1} (1 - q^n) = q^{1/24} eta(tau).

The modular transformation eta(-1/tau) = sqrt(-i*tau) * eta(tau) is proved by Poisson summation on the lattice Z: the theta function theta_3(tau) = sum_{n in Z} q^{n^2/2} satisfies theta_3(-1/tau) = sqrt(-i*tau) * theta_3(tau), and the Dedekind eta is obtained from theta_3 by the Jacobi triple product.

### What makes this work

The Heisenberg OPE is purely quadratic: J(z)J(w) ~ k/(z-w)^2, no simple pole. Consequently:

1. The bar differential decomposes pairwise (prop:abelian-bar-factorization): d_bar = sum_{i<j} d_{ij} with [d_{ij}, d_{kl}] = 0 for disjoint pairs.

2. The state space has a Z-grading by L_0-eigenvalue with multiplicity p(n) (number of partitions) at weight n, and the sewing operator respects this grading.

3. The one-particle reduction (thm:heisenberg-one-particle-sewing) collapses the full Fock-space sewing to a determinant on a SINGLE particle Hilbert space, where K_q is diagonal with eigenvalues q^n.

4. The modular transformation acts on the period tau of the torus. On the Z-graded state space, the S-transformation tau -> -1/tau acts as Fourier transform on Z (the lattice of L_0-eigenvalues), and Poisson summation on Z gives the modular transformation of eta.

The key structural point: the abelian factorization of the bar differential ensures that sewing decomposes into independent one-particle channels, each summing over the integer lattice Z. Poisson summation acts channel by channel.

### At higher genus

For genus g, the Heisenberg partition function is (thm:lattice-sewing, eq:lattice-sewing-factorization for the trivial lattice):

    Z_g(H_k; Omega) = (det Im(Omega))^{-1/2} * det'_zeta(Delta_{Sigma_g})^{-1/2}

where Omega is the g x g period matrix and Delta is the Laplacian on Sigma_g. The sewing operator on the one-particle Bergman space A^2(Sigma_g) has eigenvalues determined by the period matrix, and the modular transformation Omega -> -Omega^{-1} acts by Poisson summation on the lattice Z^g (the lattice of harmonic forms on Sigma_g).

## 2. Lattice VOAs: sewing IS Poisson summation on L

### The mechanism

For a lattice VOA V_Lambda of rank r with even positive-definite lattice Lambda, the genus-1 partition function is (eq:lattice-sewing-factorization):

    Z_1(V_Lambda; tau) = Theta_Lambda(tau) / eta(tau)^r

where Theta_Lambda(tau) = sum_{lambda in Lambda} q^{|lambda|^2/2} is the lattice theta function.

By Poisson summation on the lattice Lambda (lattice_foundations.tex, line 1467):

    Theta_Lambda(-1/tau) = (tau/i)^{r/2} |Lambda*/Lambda|^{1/2} Theta_{Lambda*}(tau)

For unimodular Lambda = Lambda*, this gives S-invariance of Z_1.

### At genus g

    Z_g(V_Lambda; Omega) = Z_g(H_r; Omega) * Theta_Lambda^{(g)}(Omega)

where Theta_Lambda^{(g)}(Omega) = sum_{lambda in Lambda^g} exp(i*pi*lambda^T*Omega*lambda) is the Siegel theta series. The modular transformation Omega -> -Omega^{-1} acts by Poisson summation on the lattice Lambda^g in R^{rg}, and Theta_Lambda^{(g)} transforms as a Siegel modular form of weight r/2 for Sp(2g, Z).

### What makes this work

The lattice VOA state space decomposes by charge sector:

    V_Lambda = bigoplus_{gamma in Lambda} F_gamma

where F_gamma is the Fock module with momentum gamma. The sewing operation sums over the full lattice Lambda^g of momenta flowing through the g handles of the surface. This sum IS a lattice sum, and its modular transformation IS Poisson summation on the lattice.

The Dirichlet sewing lift (rem:lattice-completion-kinematics) is:

    S_{V_Lambda}(u) = sum r_Lambda(n) n^{-u}

where r_Lambda(n) = #{v in Lambda : |v|^2/2 = n}. The completed Epstein zeta function E_Lambda*(s) = (2*pi)^{-s} Gamma(s) E_Lambda(s) satisfies the functional equation E_Lambda*(s) = E_Lambda*(r/2 - s) by Poisson summation (arithmetic_shadows.tex, line 510).

The L-function factorization (thm:shadow-spectral-correspondence, Step 3) decomposes the Epstein zeta into products of Hecke L-functions:

    E_Lambda(s) = c_E * zeta(s) * zeta(s - r/2 + 1) + sum_j c_j * L(s, f_j)

where the f_j are Hecke eigenforms. This is the spectral decomposition of Poisson summation into Hecke eigenspaces.

## 3. Non-lattice algebras: sewing is NOT Poisson summation

### The Virasoro case

The Virasoro algebra Vir_c at central charge c has genus-1 character

    chi_0(tau) = q^{-c/24} prod_{n>=2} 1/(1 - q^n)

(the product starts at n = 2 because the vacuum module has L_{-1}|0> = 0). For generic c, this is NOT a modular form. More precisely:

- The FULL Virasoro character (including all Virasoro modules in a modular-invariant partition function) may be modular, but the VACUUM character alone is not.

- The genus-1 propagator involves E_2*(tau) (the quasi-modular Eisenstein series), which transforms as:

      E_2*(-1/tau) = tau^2 * E_2*(tau) - 6*tau/(pi*i)

  The additive anomaly -6*tau/(pi*i) means E_2* is QUASI-modular, not modular. Products of E_2* generate the ring of quasi-modular forms Q[E_2*, E_4, E_6], which is LARGER than the ring of modular forms C[E_4, E_6].

- AP15 (from CLAUDE.md): "E_2*(tau) is quasi-modular (transforms with additive anomaly 3*tau/(pi*i)), NOT a holomorphic modular form for SL(2,Z). The shadow multiplicativity theorem falsely claimed graph amplitudes are 'polynomials in E_4, E_6' -- but the genus-1 propagator IS E_2*."

### Why Poisson summation fails

There are three nested obstructions:

**Obstruction 1: No lattice.** Poisson summation requires a lattice (discrete cocompact subgroup of R^n) or more generally a locally compact abelian group. The Virasoro state space V = bigoplus_n V_n is Z_{>=0}-graded by conformal weight, but there is no dual lattice: the states at weight n are L_{-lambda}|0> indexed by partitions lambda of n, and there is no natural group structure on the set of partitions.

**Obstruction 2: Non-abelian bar differential.** The Virasoro OPE has a simple pole: T(z)T(w) ~ (c/2)/(z-w)^4 + 2T(w)/(z-w)^2 + (dT(w))/(z-w). The simple pole means the bar differential does NOT factor pairwise (prop:nonabelian-kernel-nonfactorization). The non-factorization means the sewing cannot be reduced to independent one-particle channels. The "non-abelian Fourier kernel" is d_bar = sum d_{ij} with [d_{ij}, d_{jk}] != 0.

**Obstruction 3: Infinite shadow depth.** The Virasoro has shadow depth r_max = infinity (class M). The full sewing involves an infinite tower of higher-arity shadow components (S_3, S_4, S_5, ...) that contribute to the genus-g amplitude beyond the scalar kappa. The sewing is not determined by a single lattice sum but by an infinite sequence of graph integrals over M-bar_{g,n} with n-point insertions.

### The sewing operator for Virasoro

The Fredholm sewing engine (fredholm_sewing_engine.py) implements the genus-1 sewing as:

    Z_1(Vir_c; tau) = det(1 - K_q)^{-1}

where K_q acts on the weight-n subspace V_n (dimension p(n)) as a NON-TRIVIAL matrix S_n encoding the interaction structure. For Heisenberg, S_n = Id (all eigenvalues 1); for Virasoro, S_n has a nontrivial spectrum depending on c.

The crucial difference: for Heisenberg, det(1 - S_n * q^n) = (1 - q^n)^{dim V_n}, which is an eta-function. For Virasoro, det(1 - S_n * q^n) has NO product formula and NO lattice interpretation. The eigenvalues of S_n are determined by the Shapovalov (Gram) matrix of the Virasoro representation, which depends on c in an algebraic but non-periodic way.

## 4. Generalized Poisson summation: what the bar complex provides

### The manuscript's framework

The Fourier seed chapter (fourier_seed.tex) frames the entire bar construction as a non-abelian Fourier transform:

> "The bar construction is a non-abelian Fourier transform. The kernel is the logarithmic propagator eta_{ij} = d*log(z_i - z_j), the source is the operator product expansion of a chiral algebra A, and the integration contour is the boundary divisor of the Fulton-MacPherson compactification C-bar_n(X)."

The dictionary (free_fields.tex, lines 3150-3178) maps:

| Classical Fourier        | Chiral bar-cobar                               | Abelian specialization     |
|--------------------------|-------------------------------------------------|----------------------------|
| Dual group G-hat         | Koszul dual A!                                 | H_k^! = Sym^ch(V*)        |
| Kernel e^{i<x,xi>}      | eta_{ij} = d*log(z_i - z_j)                   | genus 0: dz/(z-w)         |
| Fourier inversion        | D_Ran B(A) ~ A!_infty                         | Omega -> -Omega^{-1}      |
| Poisson summation        | theta function identity                        | Siegel modular involution  |
| Plancherel measure       | spectral discriminant Delta_A(x)               | Delta_H = 1 (flat)        |

### The Weyl group as non-abelian Poisson summation

For affine Kac-Moody algebras, rem:weyl-nonabelian-fourier (free_fields.tex, line 3442) identifies:

> "The Weyl-Kac character formula replaces the dual-lattice sum in classical Poisson summation with an alternating sum over W_aff = W x| Q^v."

This is the closest the manuscript comes to a "non-abelian Poisson summation." The mechanism: the bar spectral sequence at E_1 is indexed by Verma modules M(w . lambda) for w in W_aff, and the collapse at generic level gives the Weyl-Kac character formula as a signed sum over the affine Weyl group. The affine Weyl group IS an infinite discrete group (a lattice semidirect product W x| Q^v), so the sum over it IS structurally analogous to Poisson summation -- but it is a SIGNED (alternating) sum, not a positive sum. The signs come from the Weyl denominator, which is itself a product of theta functions.

### What would a genuine generalization require?

A "generalized Poisson summation" for non-lattice sewing would need to satisfy:

1. **Summation formula**: The sewing sum sum_{states s} <s|K_q|s> would need to be rewritten as a sum over a "dual" basis with a known transformation law.

2. **Duality involution**: There must be an involution (analogous to tau -> -1/tau) that exchanges the original sum and the dual sum.

3. **Functional equation**: The sewing amplitude Z_g(A; Omega) must satisfy a functional equation relating Z_g at Omega to Z_g at some transform of Omega.

For the bar complex, the natural candidate for the duality involution is Verdier duality (Theorem A): D_Ran(B(A)) ~ B(A!). This exchanges A and A!. At genus 1, this gives:

    Z_1(A; tau) <-> Z_1(A!; tau')

for some transformation tau -> tau'. For Heisenberg: A! = H_{-k}, and the transformation is k -> -k (level negation), which is NOT the modular S-transformation tau -> -1/tau. The S-transformation sends k -> 1/k (free_fields.tex, line 2831). These are DIFFERENT operations:

- Koszul duality: k -> -k (Verdier duality, algebraic)
- S-transformation: k -> 1/k (Poisson summation, analytic)

For lattice VOAs: Koszul duality maps V_Lambda to V_{Lambda'} where Lambda' depends on the lattice dual. The S-transformation maps Theta_Lambda to Theta_{Lambda*} by Poisson summation.

The relationship: Koszul duality is the ALGEBRAIC shadow of Poisson summation. They coincide for self-dual lattices (Lambda = Lambda*), diverge for non-self-dual lattices, and have no direct analogue for non-lattice algebras.

## 5. The Level 2 to Level 3 descent: precise obstruction

### The descent chain context

- **Level 2** (categorical/algebraic): The bar-cobar adjunction (Theorem A), bar-cobar inversion (Theorem B), Verdier intertwining -- all categorical operations on factorization algebras/coalgebras on Ran(X).

- **Level 3** (analytic/arithmetic): Modular forms, L-functions, Poisson summation, Hecke eigenvalue decomposition, functional equations.

### For lattice algebras: the descent CLOSES

The twelve-station proof (twelve_station_verification.py, arithmetic_shadows.tex) demonstrates the full chain:

    Station 1: Poisson summation -> Theta_Lambda in M_{r/2}(SL(2,Z))
    Station 2-3: Hecke decomposition, L-function factorization
    Station 4-6: MC equation, intertwining, HS-sewing (algebraic, Level 2)
    Station 7-12: Spectral correspondence, prime locality, Rankin-Selberg

The bridge from Level 2 to Level 3 is the lattice theta function: the sewing operation (Level 2) produces Theta_Lambda (a lattice sum), and Poisson summation (Level 3) gives the functional equation. The Epstein zeta function is the Mellin transform of the theta function, and its functional equation is Poisson summation in Mellin space.

### For non-lattice algebras: the descent is OPEN

The obstruction is not a single missing theorem but a structural mismatch:

**The sewing operation for non-lattice algebras produces a function Z_1(A; tau) that is NOT a theta function, NOT a modular form (in general), and has NO lattice to apply Poisson summation to.**

More precisely, at genus 1:

1. For Virasoro at generic c: the vacuum character chi_0(tau) is NOT modular. A modular-invariant partition function requires summing over ALL Virasoro representations (Verma modules, degenerate modules), not just the vacuum. The sewing of the VACUUM MODULE alone gives a non-modular function.

2. The genus-1 bar complex for Virasoro involves the quasi-modular form E_2*(tau), so the resulting amplitudes lie in Q[E_2*, E_4, E_6] (the ring of quasi-modular forms), not in C[E_4, E_6] (modular forms). Quasi-modular forms do NOT have a classical Poisson summation origin.

3. The "non-abelian Fourier transform" (the bar construction) replaces the exponential kernel e^{i<x,xi>} with the logarithmic propagator d*log(z-w). For Poisson summation to work, the kernel must satisfy the orthogonality relation <e_n, e_m> = delta_{nm} on the lattice. The logarithmic propagator satisfies the Arnold relation eta_{12} ^ eta_{23} + cyc = 0 at genus 0, but this is a cocycle condition, not an orthogonality relation.

4. At genus >= 1, the Arnold relation FAILS (eq:fourier-arnold-failure): sum_cyc eta^{(1)}_{12} ^ eta^{(1)}_{23} = omega_1, the Arakelov (1,1)-form. This failure is measured by kappa(A) (the modular characteristic). The curvature omega_1 is the genus-1 anomaly, and it prevents the bar differential from factoring pairwise. No pairwise factorization means no reduction to independent lattice sums, means no Poisson summation.

### The three candidate generalizations

**Candidate A: Trace formula as generalized Poisson summation.** The Selberg trace formula for the hyperbolic Laplacian on Sigma_g gives

    sum_n h(r_n) = (area) * integral h(r) tanh(pi*r) r dr + sum_{gamma} l(gamma)/(2 sinh(l(gamma)/2)) * g(l(gamma))

where the left side sums over eigenvalues and the right side sums over closed geodesics. This IS a generalization of Poisson summation (eigenvalues <-> closed orbits). For the sewing of the bar complex: the left side is the spectral decomposition of Z_g, and the right side involves the length spectrum of Sigma_g. Whether the bar complex sewing can be identified with either side of the Selberg trace formula is an OPEN QUESTION. The difficulty: the Selberg trace formula involves the LAPLACIAN on Sigma_g, while the bar complex sewing involves the BERGMAN KERNEL (the holomorphic projection of the Green's function). These are related but not identical.

**Candidate B: Langlands duality as non-abelian Poisson summation.** The Langlands program replaces Poisson summation on abelian groups with automorphic forms on reductive groups. The theta correspondence (Howe duality, Weil representation) is the non-abelian analogue of Poisson summation. For the bar complex: the Koszul duality A <-> A! is an algebraic version of Langlands duality (dual group <-> group). Whether this can be made precise is the content of the arithmetic shadow programme (arithmetic_shadows.tex), specifically the arithmetic comparison conjecture (conj:arithmetic-comparison): Theta_A canonically determines the arithmetic packet connection nabla^arith_A. This conjecture is OPEN.

**Candidate C: The bar construction itself as the generalization.** The fourier_seed chapter proposes that the chiral bar construction IS the correct generalization of the Fourier transform to the non-abelian setting. If one accepts this, then the "generalized Poisson summation" is simply the genus-1 sewing of the bar complex:

    Z_1(A; tau) = Tr_{B^{(1)}(A)} q^{L_0 - c/24} = "sum over bar states"

and the "functional equation" is Koszul duality:

    D_Ran(B(A)) ~ B(A!)  =>  Z_1(A; tau) <-> Z_1(A!; tau')

This is aesthetically appealing but mathematically empty unless one specifies the transformation tau -> tau'. For lattice algebras, tau' = -1/tau. For non-lattice algebras, there is no known tau'.

## 6. Assessment and precise status

### What is PROVED

1. For Heisenberg: sewing = Poisson summation on Z (via eta function). The one-particle Bergman reduction (thm:heisenberg-one-particle-sewing) makes this explicit: the Fredholm determinant det(1 - K_q) = prod(1 - q^n) = eta function, and the modular transformation is Poisson summation.

2. For lattice VOAs: sewing = Poisson summation on Lambda (via Siegel theta function). The lattice sewing theorem (thm:lattice-sewing) gives Z_g = Z_g(H_r) * Theta_Lambda^{(g)}, and Poisson summation on Lambda gives the functional equation.

3. The bar construction is a non-abelian Fourier transform with kernel d*log(z-w) (fourier_seed.tex). The four properties (Theorem thm:fourier-four-properties) correspond to intertwining, inversion, Plancherel (complementarity), and characteristic function (modular characteristic kappa).

4. The Weyl-Kac character formula replaces the dual-lattice sum with an alternating sum over the affine Weyl group W_aff = W x| Q^v (rem:weyl-nonabelian-fourier). This is the "non-abelian Poisson summation" for affine KM algebras.

### What is OPEN

1. For non-lattice algebras (Virasoro at generic c, W_N): no Poisson summation formula for the sewing. The genus-1 partition function is not a modular form, the sewing does not factor into independent lattice channels, and there is no dual lattice.

2. Whether the Selberg trace formula can serve as a bridge between bar sewing and Poisson summation (Candidate A).

3. Whether the arithmetic comparison conjecture (conj:arithmetic-comparison) can close the Level 2 to Level 3 descent for non-lattice algebras (Candidate B).

4. Whether the quasi-modular forms arising from non-lattice sewing have a Poisson-summation-type origin. The quasi-modular Eisenstein series E_2* does satisfy a "almost-modular" transformation law, but the additive anomaly prevents a clean functional equation.

### The honest answer

The descent chain Level 2 (categorical sewing) to Level 3 (analytic Poisson summation) **closes for lattice algebras and is genuinely open for non-lattice algebras**. The obstruction is not technical but structural: Poisson summation requires an abelian group structure (lattice), and non-lattice chiral algebras have state spaces with no such structure.

The bar complex provides a candidate generalization: the non-abelian Fourier transform. But calling the sewing operation "generalized Poisson summation" without specifying the dual sum and the functional equation is terminological inflation, not mathematics (AP7, AP28). The correct statement is:

> For lattice algebras, genus-g sewing decomposes as oscillator contribution times lattice theta sum, and Poisson summation on the lattice gives the modular transformation. For non-lattice algebras, the sewing is a Fredholm determinant on the interacting state space, and whether it satisfies any generalization of Poisson summation is open (controlled by the arithmetic comparison conjecture and the quasi-modular structure of the genus-1 amplitudes).

## 7. Connection to the manuscript's existing framework

### The twelve-station proof (arithmetic_shadows.tex)

Stations 1-3 of the twelve-station proof for lattice algebras are precisely the Poisson summation -> Hecke decomposition -> L-function factorization chain. For non-lattice algebras (Section on "twelve stations for non-lattice families"), the proof replaces Poisson summation with "the modular transformation law of F and the vector-valued Hecke spectral theorem" (arithmetic_shadows.tex, line 5597). This replacement is the non-lattice analogue, but it requires F to be modular or quasi-modular, which is a HYPOTHESIS, not a theorem, for generic non-lattice algebras.

### The arithmetic packet connection (def:arithmetic-packet-connection)

The arithmetic packet connection nabla^arith_A encodes the arithmetic data (L-packets, scattering) of the chiral algebra. The principle "arithmetic is semisimple; homotopy defect is unipotent" (arithmetic_shadows.tex) suggests that the Poisson summation content of the sewing is captured by the semisimple part of nabla^arith, while the non-abelian corrections (shadow tower, Swiss-cheese non-formality) are captured by the unipotent part. This is a precise and testable structural prediction, but it remains CONJECTURAL.

### The shadow Postnikov tower

The shadow tower Theta_A^{<=r} provides a filtration of the sewing operation:

- Arity 2 (kappa): the scalar part, which IS controlled by the Hodge class lambda_g and hence by Poisson-summation-type identities (Mumford isomorphism).
- Arity 3 (cubic shadow C): tree-level non-abelian correction, involving the simple-pole structure constant f^{ab}_c. No Poisson summation.
- Arity >= 4 (quartic Q, quintic, ...): higher-loop corrections, involving graph sums over M-bar_{g,n}. No Poisson summation.

The scalar shadow kappa * lambda_g is the part of the sewing that "remembers" Poisson summation (through the Mumford isomorphism and the Hodge bundle). The higher-arity shadows are the genuinely non-abelian contributions that have no Poisson summation analogue.

## References within the monograph

- fourier_seed.tex: Chapter "The Fourier seed" -- bar as non-abelian Fourier transform
- free_fields.tex, lines 2820-3060: Heisenberg genus-g bar complex, Poisson summation, Koszul-Fourier dictionary
- free_fields.tex, lines 3150-3180: Classical Fourier / chiral bar-cobar dictionary table
- free_fields.tex, rem:weyl-nonabelian-fourier (line 3442): Weyl group as non-abelian Poisson summation
- lattice_foundations.tex, lines 1460-1490: Poisson summation for lattice theta functions
- arithmetic_shadows.tex, lines 500-530: Epstein zeta functional equation via Poisson summation
- arithmetic_shadows.tex, lines 5592-5600: twelve stations for non-lattice families
- heisenberg_eisenstein.tex, thm:heisenberg-sewing: Heisenberg sewing theorem
- higher_genus_modular_koszul.tex, prop:saddle-point-mc: MC element as saddle point, Fredholm determinant
- fredholm_sewing_engine.py: compute implementation of sewing operators
- twelve_station_verification.py, station_1_poisson_summation: numerical verification
