# 6D Holomorphic Chern-Simons and the CFG 2026 \(E_3\) Algebra: Adversarial Derivation

Context: Vol I cross-volume audit note. Scope: first-principles derivation, correction, and cross-consistency audit for the proposed six-dimensional holomorphic Chern-Simons avatar of the Costello-Francis-Gwilliam 2026 \(E_3\) algebra. Date: 2026-04-24.

## Findings First

1. **CFG 2026 is not a 6D hCS source.** The paper verified as Costello-Francis-Gwilliam 2026 is *Chern-Simons factorization algebras and knot polynomials*, arXiv:2602.12412. Its Theorem 1.1 concerns ordinary three-dimensional Chern-Simons theory, a filtered \(E_3\)-algebra \(A_\lambda\), perfect modules, and Reshetikhin-Turaev link invariants. It does not contain six-dimensional holomorphic Chern-Simons on Calabi-Yau threefolds, Bochner-Martinelli propagators, quintic anomaly coefficients, CoHA\((\mathbb C^3)\), or wave-function renormalisation.
2. **The requested "line-by-line CFG 2026 6D hCS match" is therefore not source-verifiable.** The correct object is an *avatar*: compare the \(E_3\)-algebraic role of CFG 2026 with the Dolbeault-reduced factorization algebra of 6D hCS. This comparison is conditional until a theorem constructs the functor or deformation equivalence.
3. **The prompt's one-loop anomaly formula is false as a primary hCS statement.** Costello-Li compute the one-loop gauge anomaly of holomorphic Chern-Simons in complex dimension three from a four-vertex one-loop diagram and a quartic invariant, schematically
   \[
   \int_X \operatorname{Tr}_{\mathrm{ad}}\bigl(A(F_A)^3\bigr),
   \]
   not a theta graph and not a cubic \(d^{abc}\)-term. In complex dimension \(d\), the local holomorphic gauge anomaly is controlled by an invariant polynomial of degree \(d+1\); for \(d=3\) this is degree \(4\).
4. **The prompt's wave-function counterterm is not source-supported.** Williams' holomorphic renormalisation theorem gives one-loop finiteness and no counterterms for holomorphic theories on \(\mathbb C^d\). Thus the displayed logarithmic flat-space wave-function counterterm must be treated as UNVERIFIED and, in the holomorphic scheme, false.
5. **The Bochner-Martinelli coefficient \(2/(2\pi i)^3\) is verified.** Gwilliam-Williams' algebraic Bochner-Martinelli kernel has coefficient \((d-1)!/(2\pi i)^d\), so for \(d=3\) it is \(2/(2\pi i)^3\), up to the chosen orientation convention.
6. **The quintic Euler number is verified.** From
   \[
   c(TX_5)=\frac{(1+h)^5}{1+5h}=1+10h^2-40h^3,
   \qquad \int_{X_5}h^3=5,
   \]
   one obtains \(\chi_{\mathrm{top}}(X_5)=\int_{X_5}c_3(TX_5)=-200\). Any anomaly coefficient proportional to \(\chi_{\mathrm{top}}\) therefore receives a factor \(-200\), but the prompt's scalar denominator is not primary-verified.

## Conventions Used Throughout

Let \(X\) be a Calabi-Yau threefold with a fixed holomorphic volume form
\[
\Omega_X\in H^0(X,K_X),\qquad K_X\simeq \mathcal O_X.
\]
Let \(\mathfrak g\) be a finite-dimensional Lie algebra with invariant symmetric pairing \(\kappa_{\mathfrak g}(-,-)\). On noncompact \(X=\mathbb C^3\), all pairings and observables are compactly supported, distributional, or placed in a renormalised factorization-algebra setting; bare integrals over all of \(\mathbb C^3\) are not used.

The BV field convention is:
\[
\mathcal E_X=\Omega^{0,*}(X,\mathfrak g)[1],
\]
with ghost number assigned by
\[
|\alpha_{0,q}|=1-q.
\]
Thus
\[
\mathcal A=c+A_{0,1}+A^+_{0,2}+c^+_{0,3},
\]
where \(c\) has ghost number \(+1\), \(A_{0,1}\) ghost number \(0\), \(A^+_{0,2}\) ghost number \(-1\), and \(c^+_{0,3}\) ghost number \(-2\). If a cited source uses the opposite cohomological shift convention, the same formulas are shifted by the corresponding suspension sign. This note fixes the above convention and does not silently switch.

The invariant pairing is extended by wedge product:
\[
(\alpha,\beta)_X=\int_X \Omega_X\wedge \kappa_{\mathfrak g}(\alpha\wedge \beta).
\]
The integral is nonzero only when the Dolbeault form degrees sum to \(3\). Since
\[
|\alpha_{0,q}|+|\beta_{0,3-q}|=(1-q)+(1-(3-q))=-1,
\]
the pairing has cohomological degree \(-1\). This is the odd BV symplectic pairing.

The classical holomorphic Chern-Simons action is normalised as in Costello-Li:
\[
S_{\mathrm{cl}}(\mathcal A)
=\int_X \Omega_X\wedge
\left(
\frac12\kappa_{\mathfrak g}(\mathcal A,\bar\partial\mathcal A)
+\frac16\kappa_{\mathfrak g}(\mathcal A,[\mathcal A,\mathcal A])
\right).
\]
The prompt's expression
\[
\int_X\Omega_X\wedge \langle A,\bar\partial A+\tfrac13[A,A]\rangle
\]
is equivalent only if the external \(\langle-,-\rangle\) already contains the quadratic factor \(1/2\) and the cubic cyclic symmetrisation. The unambiguous convention is \(1/2,1/6\).

For a finite-dimensional odd symplectic model with Darboux coordinates \(x_i,x_i^+\), the BV Laplacian is fixed by
\[
\Delta(fg)=\Delta(f)g+(-1)^{|f|}f\Delta(g)+(-1)^{|f|}\{f,g\},
\]
so that the quantum master equation is
\[
(Q+\hbar \Delta)e^{I/\hbar}=0
\quad\Longleftrightarrow\quad
QI+\frac12\{I,I\}+\hbar\Delta I=0.
\]
The prompt's expression \((S+\hbar\Delta)e^{S/\hbar}=0\) is not dimensionally or operadically correct: the differential is \(Q+\hbar\Delta\), not multiplication by \(S\).

## (A) Set-Up

### Claim

**CFG 2026 literal claim.** CFG 2026, Theorem 1.1, constructs from three-dimensional Chern-Simons theory a filtered \(E_3\)-algebra \(A_\lambda\) and identifies traces of perfect modules with Reshetikhin-Turaev link invariants. No six-dimensional hCS claim is stated there.

**6D hCS avatar claim.** For a Calabi-Yau threefold \(X\) and a metric Lie algebra \(\mathfrak g\), the BV field theory with fields
\[
\Omega^{0,*}(X,\mathfrak g)[1]
\]
and action \(S_{\mathrm{cl}}\) above is the classical holomorphic Chern-Simons theory. On \(X=\mathbb C^3\), translation invariance and Dolbeault reduction produce an \(E_3\)-type algebraic shadow of the factorization algebra of observables.

The shift-law table to be held separate from hCS is:

| CY dimension \(d\) | shifted symplectic degree in the repo convention | chiral shadow |
|---:|---:|---|
| \(2\) | \(-2\) | \(E_2\) |
| \(3\) | \(-1\) | \(E_1\) |
| \(4\) | \(0\) | \(E_0\) |
| \(5\) | \(+1\) | \(E_5\)-Poisson |

This table is verified against the local source `chapters/theory/cy_to_chiral.tex`, not directly against Costello-Gwilliam Vol II in this session. It remains a repository theorem-surface claim unless the exact Costello-Gwilliam Vol II page is checked.

### Derivation

Start with the Dolbeault dg Lie algebra
\[
L_X=\Omega^{0,*}(X,\mathfrak g),
\qquad
d_L=\bar\partial,
\qquad
[\alpha\otimes x,\beta\otimes y]
=(-1)^{|\beta||x|}(\alpha\wedge\beta)\otimes[x,y].
\]
Since \(\mathfrak g\) is concentrated in degree \(0\), the sign reduces to the Dolbeault/Koszul sign for the forms. The Jacobi identity follows from the Jacobi identity in \(\mathfrak g\) and associativity of wedge product. The differential is a derivation because \(\bar\partial\) is.

The shifted field space is \(L_X[1]\). The pairing
\[
\omega_X(\alpha,\beta)=\int_X\Omega_X\wedge\kappa_{\mathfrak g}(\alpha\wedge\beta)
\]
pairs \(\Omega^{0,q}\) with \(\Omega^{0,3-q}\). Under the ghost convention \(|\alpha_{0,q}|=1-q\), the total ghost degree is \(-1\). Thus \(\omega_X\) is a \((-1)\)-shifted symplectic form.

Vary the action:
\[
\delta S_{\mathrm{cl}}
=\int_X\Omega_X\wedge
\left(
\frac12\kappa(\delta A,\bar\partial A)
+\frac12\kappa(A,\bar\partial\delta A)
+\frac16\kappa(\delta A,[A,A])
+\frac16\kappa(A,[\delta A,A])
+\frac16\kappa(A,[A,\delta A])
\right).
\]
Using Stokes' theorem, \(\bar\partial\Omega_X=0\), compact support or no-boundary conditions, and invariance/cyclicity of \(\kappa\), the two quadratic terms combine and the three cubic terms combine:
\[
\delta S_{\mathrm{cl}}
=\int_X\Omega_X\wedge
\kappa\left(\delta A,\bar\partial A+\frac12[A,A]\right).
\]
Hence the Euler-Lagrange equation is the Maurer-Cartan equation
\[
\bar\partial A+\frac12[A,A]=0.
\]

On \(\mathbb C^3\), the full locally constant real translation structure would be \(E_6\) if the theory were topological in all six real directions. Holomorphic translation invariance plus \(\bar\partial\)-cohomological reduction removes the anti-holomorphic directions and leaves the holomorphic three-disk/Dolbeault-reduced \(E_3\)-type operation. Therefore the correct sentence is:

\[
\text{geometric factorization on }\mathbb R^6
\quad\rightsquigarrow\quad
E_6\text{ before Dolbeault reduction,}
\quad E_3\text{ after holomorphic reduction.}
\]

### Attack

1. The prompt attributes a 6D hCS \(E_3\) statement to CFG 2026. That attribution is false.
2. The action coefficient \(1/3\) is ambiguous unless the pairing includes the missing \(1/2\). The primary hCS convention uses \(1/2\) and \(1/6\).
3. The expansion \(c+A_{0,1}+A^+_{0,2}+c^+_{0,3}\) fixes a ghost-number convention. Without stating it, the phrase \([1]\) is ambiguous.
4. On noncompact \(\mathbb C^3\), the Serre pairing requires compact support, rapid decay, or distributional/renormalised interpretation.
5. The shift-law table belongs to the CY-to-chiral/PTVV lane. It must not be used as a direct Costello-Gwilliam Vol II quote unless the exact theorem/page is verified.
6. The \(E_3\) label is a reduced holomorphic label, not the raw real-dimensional factorization label.

### Heal

Use \(S_{\mathrm{cl}}\) with coefficients \(1/2,1/6\). Fix the ghost convention \(|\Omega^{0,q}[1]|=1-q\). Insert compact-support/renormalised hypotheses for \(\mathbb C^3\). State \(E_6\) before Dolbeault reduction and \(E_3\) after it. Mark the shift-law table as locally verified but externally pending until the precise Costello-Gwilliam Vol II citation is checked.

### Cross-check

Costello-Li, arXiv:1905.09269, Introduction and Section 2, state the hCS action on a Calabi-Yau threefold with the \(1/2,1/6\) convention and equation \(\bar\partial A+\frac12[A,A]=0\). The local Vol III source `chapters/theory/cy_to_chiral.tex` gives the displayed shift-law table. CFG 2026, arXiv:2602.12412, Theorem 1.1, gives a filtered \(E_3\)-algebra from ordinary 3D Chern-Simons, not this 6D construction.

## (B) BV Formalism

### Claim

**CFG 2026 literal claim.** CFG 2026 uses BV quantization of ordinary Chern-Simons to produce the filtered \(E_3\)-algebra \(A_\lambda\). It does not state the hCS BV master equation on a Calabi-Yau threefold.

**6D hCS claim.** The odd symplectic form above makes \(S_{\mathrm{cl}}\) solve the classical master equation
\[
\{S_{\mathrm{cl}},S_{\mathrm{cl}}\}=0.
\]
A quantum lift is a renormalised interaction \(I[L]\) satisfying
\[
(Q+\hbar\Delta_L)e^{I[L]/\hbar}=0,
\]
equivalently
\[
QI[L]+\frac12\{I[L],I[L]\}_L+\hbar\Delta_L I[L]=0.
\]

### Derivation

The Hamiltonian vector field of \(S_{\mathrm{cl}}\) is
\[
Q_{\mathrm{BV}}A=\bar\partial A+\frac12[A,A].
\]
The classical master equation is equivalent to \(Q_{\mathrm{BV}}^2=0\). Compute:
\[
Q_{\mathrm{BV}}^2A
=\bar\partial\left(\bar\partial A+\frac12[A,A]\right)
+\left[A,\bar\partial A+\frac12[A,A]\right].
\]
Since \(\bar\partial^2=0\) and \(\bar\partial\) is a derivation,
\[
\bar\partial[A,A]=[\bar\partial A,A]+(-1)^{|A|}[A,\bar\partial A].
\]
With \(A\) the suspended total odd field and the graded Lie convention fixed above, these terms cancel the \([A,\bar\partial A]\) contribution. The remaining term is
\[
\frac12[A,[A,A]],
\]
which vanishes by the graded Jacobi identity. Hence \(Q_{\mathrm{BV}}^2=0\), so
\[
\{S_{\mathrm{cl}},S_{\mathrm{cl}}\}=0.
\]

At the quantum level, \(\Delta\) is not a literal infinite-dimensional second-order differential operator. Costello's renormalisation replaces it by a scale-dependent BV Laplacian \(\Delta_L\) and bracket \(\{-,-\}_L\), built from a regulated kernel. The QME is then imposed at each scale:
\[
QI[L]+\frac12\{I[L],I[L]\}_L+\hbar\Delta_L I[L]=0.
\]
The obstruction at order \(\hbar\) is the cohomology class of
\[
\Delta_L I_{\mathrm{cl}}
\]
after taking the small-scale limit and projecting to local functionals.

### Attack

1. The prompt writes \((S+\hbar\Delta)e^{S/\hbar}=0\). This is incorrect: \(S\) is an action functional, not the cohomological differential.
2. The sign of \(\Delta\) depends on Darboux-coordinate conventions. Without a product rule, the bracket sign is not fixed.
3. The infinite-dimensional BV Laplacian is divergent before regularisation.
4. The CME proof uses compact support/no-boundary hypotheses. Boundary terms on noncompact \(\mathbb C^3\) are otherwise uncontrolled.
5. The hCS QME and CFG's ordinary CS QME are structurally parallel but not the same theorem.

### Heal

Replace the prompt's QME by
\[
(Q+\hbar\Delta_L)e^{I[L]/\hbar}=0.
\]
Fix the BV Laplacian by the second-order product identity. Treat \(\Delta_L\) as a renormalised scale-\(L\) operator. State all noncompact integrals with compact support or renormalisation data.

### Cross-check

Costello-Gwilliam Vol I and Vol II are the standard BV/factorization-algebra references for scale-dependent observables and QME conventions; exact pages were not rechecked in this session. Costello-Li, arXiv:1905.09269, uses the BV hCS master field \(A\in\Omega^{0,*}\otimes\mathfrak g[1]\) and computes the one-loop anomaly by the BV obstruction method. CFG 2026, Theorem 1.1, is the parallel ordinary CS \(E_3\) construction.

## (C) Flat \(\mathbb C^3\), Heat Kernels, and the Bochner-Martinelli Propagator

### Claim

**CFG 2026 literal claim.** CFG 2026 uses perturbative Chern-Simons/factorization-algebra techniques, but not the 6D Bochner-Martinelli kernel.

**6D hCS claim.** On \(\mathbb C^3\), the singular part of the hCS propagator is the Bochner-Martinelli kernel. In the algebraic normalisation of Gwilliam-Williams,
\[
\omega_{\mathrm{BM}}^{\mathrm{alg}}(z,z^*)
=\frac{(d-1)!}{(2\pi i)^d}
\sum_{i=1}^d(-1)^{i-1}
\frac{z_i^*\, dz_1^*\wedge\cdots\wedge\widehat{dz_i^*}\wedge\cdots\wedge dz_d^*}
{(zz^*)^d}.
\]
For \(d=3\), this gives coefficient \(2/(2\pi i)^3\).

In analytic coordinates \(u=z-w\), with \(u_i^*=\overline u_i\), the corresponding singular kernel is
\[
P_{\mathrm{BM}}(z,w)
=\frac{2}{(2\pi i)^3}
\sum_{k=1}^3(-1)^{k-1}
\frac{\overline{z_k-w_k}}
{\|z-w\|^6}
\widehat{d\overline{(z_k-w_k)}}\wedge d^3w,
\]
where
\[
\widehat{d\overline{(z_k-w_k)}}
=d\overline{(z_1-w_1)}\wedge\cdots
\wedge\widehat{d\overline{(z_k-w_k)}}\wedge\cdots
\wedge d\overline{(z_3-w_3)}.
\]
The final sign changes if the \(d^3w\) factor is moved past the anti-holomorphic forms.

### Derivation

The Bochner-Martinelli kernel is the Dolbeault homotopy kernel for \(\mathbb C^d\setminus\{0\}\). It is characterised by:

1. \(\bar\partial\omega_{\mathrm{BM}}=0\) away from \(0\).
2. \(\bar\partial\omega_{\mathrm{BM}}=\delta_0\) as a current after wedging with the holomorphic volume form.
3. The residue normalisation is \(1\):
   \[
   \int_{S^{2d-1}}\omega_{\mathrm{BM}}=1.
   \]

The algebraic formula has coefficient \((d-1)!/(2\pi i)^d\). Specialising to \(d=3\) gives
\[
\frac{(3-1)!}{(2\pi i)^3}=\frac2{(2\pi i)^3}.
\]
The denominator is \((zz^*)^3=\|z\|^6\), so the prompt's power \(\|z-w\|^{-6}\) is correct for the singular kernel.

Heat-kernel regularisation supplies a smooth scale-\(\epsilon\) propagator \(P_\epsilon\), and the renormalised propagator between scales \(\epsilon<L\) is
\[
P_{\epsilon<L}=\int_\epsilon^L Q^{\mathrm{GF}}K_t\,dt.
\]
The small-scale singular limit of \(P_{\epsilon<L}\) is the Bochner-Martinelli kernel. The exact Gaussian coefficient depends on the convention for the Dolbeault Laplacian:
\[
\Delta_{\bar\partial}
=\bar\partial\bar\partial^*+\bar\partial^*\bar\partial
\quad\text{versus}\quad
2\Delta_{\mathrm{real}},
\]
so the invariant source-checked datum is the BM residue coefficient, not a standalone heat-kernel prefactor.

Feynman amplitudes are integrals of wedge products of regulated propagators and interaction vertices over configuration spaces. On compact manifolds these are treated through compactified configuration spaces. On \(\mathbb C^3\), one must either impose compact support/IR cutoff or work locally near the small diagonal; otherwise \(\overline{\operatorname{Conf}}_n(\mathbb C^3)\) is noncompact and the integral is not a number without extra data.

### Attack

1. The prompt's BM coefficient is correct, but only after fixing whether the source uses \(z_i^*=\bar z_i\), \(d\bar z_i\), or independent algebraic conjugates.
2. The sign \((-1)^{k-1}\) is tied to the position of the omitted anti-holomorphic differential. Moving \(d^3w\) changes signs by a Koszul permutation.
3. A Gaussian-regulated heat kernel needs a Laplacian convention. The prompt gives no convention, so its heat-kernel coefficient cannot be verified.
4. Configuration-space integrals over all of \(\mathbb C^3\) have IR divergences unless compact supports, local functionals, or renormalisation are specified.
5. CFG 2026 does not verify this hCS kernel.

### Heal

Use the Gwilliam-Williams algebraic BM normalisation as the primary fixed point:
\[
(d-1)!/(2\pi i)^d.
\]
For \(d=3\), record \(2/(2\pi i)^3\). Treat heat kernels as regulators whose convention-dependent coefficients are subordinate to the BM residue normalisation. Always specify compact support/locality on \(\mathbb C^3\).

### Cross-check

Gwilliam-Williams, arXiv:1810.06534, Proposition 2.2, gives the algebraic Bochner-Martinelli kernel and residue normalisation. The same paper later uses a propagator \(P\) satisfying
\[
d^dz\,\bar\partial P=\delta_{\mathrm{Diag}}\operatorname{id}.
\]
Costello-Paquette, arXiv:2001.02177, Section 6.3, uses hCS on \(\mathbb C\times\mathbb C^2\) and its holomorphic operator calculus, but the exact BM coefficient used here is verified from Gwilliam-Williams.

## (D) Observable Algebra

### Claim

**CFG 2026 literal claim.** CFG 2026 constructs a filtered \(E_3\)-algebra \(A_\lambda\) from ordinary Chern-Simons factorization algebras. It does not identify that algebra with 6D hCS observables.

**6D hCS avatar claim.** For an open set \(U\subset X\), classical hCS observables are Chevalley-Eilenberg cochains of the local dg Lie algebra:
\[
\operatorname{Obs}_{\mathrm{cl}}(U)
=C^*_{\mathrm{Lie}}\bigl(\Omega_c^{0,*}(U,\mathfrak g),\mathbb C\bigr)
\]
with differential induced by \(\bar\partial\) and the Lie bracket. Quantum observables are a deformation
\[
\operatorname{Obs}_{\mathrm q}(U)
=\left(\widehat{\operatorname{Sym}}(\mathcal E_c(U)^\vee[-1])[[\hbar]],\,
Q+\hbar\Delta+\{I,-\}\right),
\]
where the displayed suspension is fixed by the convention that functions on \(\mathcal E\) are completed symmetric functions on \(\mathcal E^\vee\). Other sources write \(\mathcal E^\vee[1]\); the formula is equivalent only after stating the shift convention.

On \(U=\mathbb C^3\), holomorphic translation invariance and Dolbeault reduction give an \(E_3\)-type algebra of local observables. The unreduced real factorization algebra is not literally \(E_3\); it is holomorphic factorization in complex dimension \(3\).

### Derivation

For a dg Lie algebra \(L\), the formal moduli problem of Maurer-Cartan solutions has functions
\[
C^*_{\mathrm{Lie}}(L)
=\widehat{\operatorname{Sym}}(L^\vee[-1])
\]
with CE differential
\[
d_{\mathrm{CE}}=d_L^\vee+d_{\mathrm{br}}^\vee.
\]
Here \(L=\Omega_c^{0,*}(U,\mathfrak g)\). The term \(d_L^\vee\) is dual to \(\bar\partial\), and \(d_{\mathrm{br}}^\vee\) is dual to
\[
\Omega_c^{0,*}(U,\mathfrak g)^{\otimes 2}\to\Omega_c^{0,*}(U,\mathfrak g).
\]

The BV quantisation deforms the commutative factorization algebra of classical observables by adding the scale-dependent BV Laplacian and the interaction:
\[
d_{\mathrm q}=Q+\{I[L],-\}_L+\hbar\Delta_L.
\]
The product of observables on disjoint open sets gives the factorization product. If \(U_1,\dots,U_n\subset V\) are disjoint polydisks, the structure map is multiplication followed by extension to \(V\), with Koszul sign
\[
a_{\sigma(1)}\cdots a_{\sigma(n)}
=\epsilon(\sigma;a_1,\dots,a_n)\,a_1\cdots a_n,
\]
where \(\epsilon(\sigma;-)\) is determined by
\[
a_i a_j=(-1)^{|a_i||a_j|}a_j a_i.
\]
This is the "sum-over-shuffles with Koszul signs"; no extra sign is present beyond the standard symmetric monoidal sign once the suspensions are fixed.

The phrase
\[
\operatorname{Obs}_{\mathrm{hCS}}(\mathbb C^3)
\simeq CE^\bullet_{\bar\partial,\mathrm{chir}}
(\mathcal E_{\mathrm{hCS}},\mathcal O_{\mathbb C^3})
\]
is acceptable as repository shorthand only if \(CE^\bullet_{\bar\partial,\mathrm{chir}}\) is defined as the Dolbeault-reduced chiral CE construction. It is not a primary-source theorem as written.

### Attack

1. The shift in \(\operatorname{Sym}(\mathcal E^\vee[1])\) versus \(\operatorname{Sym}(\mathcal E^\vee[-1])\) is convention-sensitive. The prompt does not define it.
2. \(Q=\bar\partial+\operatorname{ad}_A+\) gauge BRST mixes background-dependent and formal-BV descriptions. At \(A=0\), the linear differential is \(\bar\partial\); the bracket enters CE/BV nonlinearly.
3. The BV Laplacian is scale-dependent and renormalised; a bare \(\Delta\) is not an operator on all polynomial functionals.
4. \(E_3\) is not the unreduced real factorization structure on \(\mathbb C^3\).
5. The CFG 2026 \(A_\lambda\) and hCS observables are not identified by any checked primary theorem.

### Heal

Define observables as CE cochains of the local dg Lie algebra and quantum observables as the renormalised BV deformation. State the suspension convention explicitly. Use "Dolbeault-reduced \(E_3\)" rather than bare "\(E_3\)" for hCS on \(\mathbb C^3\). Treat the CFG comparison as an open avatar theorem, not a proved identification.

### Cross-check

Costello-Gwilliam Vol I/II provide the factorization algebra of classical and quantum observables; exact page numbers were not rechecked. Gwilliam-Williams, arXiv:1810.06534, uses local Lie algebra CE cochains for higher Kac-Moody observables. CFG 2026, Theorem 1.1, supplies the ordinary-CS filtered \(E_3\)-algebra analogue.

## (E) One-Loop Anomaly

### Claim

**Prompt claim to test.** The prompt asserts a one-loop theta-graph anomaly
\[
\int_{\mathbb C^3}
\frac{\Omega\wedge \operatorname{Tr}(d^{abc}A_aA_bA_c)}
{|z-w|^6|w-u|^6|z-u|^6}
\]
and a global coefficient
\[
\kappa_{\mathrm{anom}}(X,\mathfrak g)
=\frac{\hbar A(\mathfrak g)\chi_{\mathrm{top}}(X)}
{2(4\pi)^3}\|\Omega_X\|^2.
\]

**Primary-source verdict.** This is not the Costello-Li hCS anomaly. In complex dimension \(3\), the local gauge anomaly is controlled by a degree-\(4\) invariant polynomial and a one-loop diagram with four interaction vertices. Schematically, Costello-Li obtain
\[
\int_X\operatorname{Tr}_{\mathrm{ad}}\bigl(A(F_A)^3\bigr),
\]
and, after restricting to the ghost \(c\),
\[
\int_X\operatorname{Tr}_{\mathrm{ad}}\bigl(c(F_A)^3\bigr).
\]
Thus the theta/cubic formula must be rejected for pure hCS.

### Derivation

The first-principles local cohomology reason is dimension-counting plus descent.

For holomorphic gauge theory in complex dimension \(d\), the local gauge anomaly is a ghost-number-one local functional. Its universal source is the Chern-Weil invariant polynomial of degree \(d+1\):
\[
P\in \operatorname{Sym}^{d+1}(\mathfrak g^\vee)^{\mathfrak g}.
\]
The descent of \(P(F^{d+1})\) produces a ghost-number-one \(2d\)-real-dimensional local functional. For \(d=3\), this requires
\[
P\in \operatorname{Sym}^4(\mathfrak g^\vee)^{\mathfrak g}.
\]
Therefore a cubic invariant \(d^{abc}\in\operatorname{Sym}^3(\mathfrak g^\vee)^{\mathfrak g}\) has the wrong invariant degree for the universal six-real-dimensional holomorphic gauge anomaly.

In perturbation theory, hCS has a cubic interaction. A one-loop local anomaly in complex dimension \(3\) is the wheel/rectangle contribution with four vertices; its Lie factor is a trace of four adjoint generators. The theta graph with three edges connecting two trivalent vertices is not the one-loop hCS gauge anomaly described by Costello-Li. It is a different graph type and cannot be used as the source of the primary hCS anomaly.

The flat-space and compact-space statements must be separated:

1. **Local pure hCS anomaly on \(\mathbb C^3\).** The local obstruction class is determined by the quartic invariant. It does not vanish merely because \(\mathbb C^3\) has trivial tangent characteristic classes.
2. **Global characteristic-number expressions.** A formula proportional to \(\chi_{\mathrm{top}}(X)\) would be a separate index-theoretic/global anomaly statement. That exact formula, including \(2(4\pi)^3\), was not verified in the primary hCS sources checked here.

For the quintic \(X_5\subset\mathbb P^4\), the Euler characteristic is:
\[
c(TX_5)=\frac{c(T\mathbb P^4)}{c(\mathcal O(5))}\bigg|_{X_5}
=\frac{(1+h)^5}{1+5h}
=1+10h^2-40h^3,
\]
so
\[
\chi_{\mathrm{top}}(X_5)
=\int_{X_5}c_3(TX_5)
=-40\int_{X_5}h^3
=-40\cdot 5
=-200.
\]
The independent Hodge-number check is
\[
\chi_{\mathrm{top}}(X_5)=2(h^{1,1}-h^{2,1})=2(1-101)=-200.
\]

For \(K3\times E\),
\[
\chi_{\mathrm{top}}(K3\times E)=\chi(K3)\chi(E)=24\cdot 0=0.
\]
Thus any *global* anomaly coefficient proportional to \(\chi_{\mathrm{top}}\) vanishes on \(K3\times E\), but this does not prove the vanishing of the local pure hCS obstruction class.

For \(SU(3)\):

1. The prompt's cubic tensor \(d^{abc}\) is not zero in the fundamental normalisation of \(\mathfrak{su}_3\). Thus the statement "SU(3) anomaly zero because \(d^{abc}=0\)" is false.
2. The adjoint representation of \(\mathfrak{su}_3\) is self-dual, so odd adjoint traces vanish, but the hCS anomaly is quartic, not cubic.
3. Under the rejected global formula, flat \(\mathbb C^3\) gives \(0\) only because the relevant compactly supported/global characteristic number is zero or undefined. That is not the Costello-Li local anomaly computation.
4. On the quintic, any corrected global coefficient proportional to \(\chi_{\mathrm{top}}\) is multiplied by \(-200\). The scalar coefficient in the prompt is UNVERIFIED.

### Attack

1. **Graph error:** theta graph is not the primary one-loop hCS gauge anomaly graph in complex dimension \(3\).
2. **Invariant-degree error:** cubic \(d^{abc}\) has degree \(3\), while the six-dimensional holomorphic gauge anomaly uses degree \(4\).
3. **Group-vanishing error:** the prompt lists groups by cubic-invariant vanishing. That criterion is irrelevant to the quartic hCS anomaly.
4. **Flat-space error:** local anomalies on \(\mathbb C^3\) are not computed by \(\chi_{\mathrm{top}}(\mathbb C^3)\).
5. **Quintic error:** \(\chi=-200\) is correct, but inserting it into the prompt's scalar formula imports an unverified denominator and wrong Lie polynomial.
6. **CHSW error:** the CHSW standard embedding \(F=R\) is a heterotic anomaly-cancellation mechanism. It is not, by itself, a theorem that pure hCS on a quintic has its BV anomaly trivialised.

### Heal

Replace the anomaly claim by:

> In complex dimension \(3\), the pure hCS one-loop gauge anomaly is controlled by the quartic adjoint invariant, represented by the Costello-Li local functional \(\int_X\operatorname{Tr}_{\mathrm{ad}}(A(F_A)^3)\) or its ghost descent. Any cubic theta expression is not the primary hCS anomaly.

If a global \(\chi_{\mathrm{top}}\)-coefficient is needed, prove it separately from an index theorem and write it as
\[
\kappa_{\mathrm{global}}(X,\mathfrak g)
=\hbar\,C_{\mathrm{scheme}}(\mathfrak g)\,\chi_{\mathrm{top}}(X),
\]
until the denominator, \(\Omega_X\)-normalisation, and trace convention are derived. For the quintic, this becomes
\[
-200\,\hbar\,C_{\mathrm{scheme}}(\mathfrak g).
\]

### Cross-check

Costello-Li, arXiv:1905.09269, compute the hCS gauge anomaly in complex dimension three from a four-vertex one-loop diagram and express it through \(\operatorname{Tr}_{\mathrm{ad}}A(F_A)^3\). Williams, arXiv:1809.02661, supports the holomorphic renormalisation setting but does not supply the prompt's cubic anomaly coefficient. CHSW 1985 supplies the standard embedding context for heterotic compactifications; the exact page was not reverified here, and its use for pure hCS must be marked CONDITIONAL.

## (F) Wave-Function Renormalisation

### Claim

**Prompt claim to test.** The prompt asserts a flat-space one-loop bubble counterterm
\[
S^{(1)}_{\mathrm{ct}}
=-\hbar C_2(\mathfrak g)(4\pi)^{-3}\log(L/\epsilon)
\int\Omega\wedge\operatorname{Tr}(A\bar\partial A),
\]
and
\[
Z_A^{(1)}
=1-\hbar C_2(\mathfrak g)(4\pi)^{-3}\log(L/\epsilon),
\]
with \(SU(N)\) coefficient \(N/(32\pi^3)\).

**Primary-source verdict.** This coefficient is not verified and conflicts with the holomorphic one-loop finiteness theorem of Williams for holomorphic theories on \(\mathbb C^d\), which states that one-loop quantisation can be achieved with no counterterms. Therefore the displayed logarithmic wave-function counterterm must be rejected in the holomorphic renormalisation scheme unless a different regulator and observable are explicitly specified.

### Derivation

The kinetic term is
\[
S_{\mathrm{kin}}(A)=\frac12\int\Omega\wedge\kappa(A,\bar\partial A).
\]
A wave-function counterterm would be a local functional proportional to the same expression:
\[
\int\Omega\wedge\kappa(A,\bar\partial A).
\]
Dimensional analysis alone permits such a term, but holomorphic renormalisation imposes a stronger constraint. Williams proves that one-loop weights in holomorphic theories on \(\mathbb C^d\) admit a naive \(\epsilon\to0\) limit and require no counterterms. Therefore, in the Costello-Williams holomorphic scheme,
\[
S^{(1)}_{\mathrm{ct}}=0
\]
for the holomorphic UV divergence problem.

This does not say that wave-function renormalisation is the same as anomaly. It says:

1. A wave-function counterterm would have ghost number \(0\) and kinetic form.
2. The gauge anomaly has ghost number \(1\) and is represented by the local obstruction class.
3. They live in different cohomological degrees.
4. In the holomorphic scheme checked here, the asserted wave-function logarithm is not present.

### Attack

1. The bubble integral and logarithm are not derived from a cited primary hCS source.
2. The coefficient \((4\pi)^{-3}\) depends on a real six-dimensional heat-kernel normalisation, not the holomorphic BM residue normalisation.
3. The claimed \(SU(N)\) value \(N/(32\pi^3)\) follows only after choosing \(C_2(\mathfrak{su}_N)=N\) and rewriting \((4\pi)^{-3}=1/(64\pi^3)\); it still does not produce \(N/(32\pi^3)\) without an extra factor \(2\).
4. Williams' theorem gives no-counterterm one-loop holomorphic renormalisation, contradicting the asserted log divergence.
5. AP113 is correct only as a distinction: wave-function renormalisation is not anomaly. It does not validate the displayed coefficient.

### Heal

State:

> In holomorphic renormalisation on \(\mathbb C^3\), no source-verified logarithmic one-loop wave-function counterterm occurs. Any such term is regulator-dependent and must be rederived in that regulator. It must not be confused with the ghost-number-one BV anomaly.

If a non-holomorphic regulator is introduced later, the required computation is:

1. Fix the Laplacian and heat kernel.
2. Compute the two-point one-loop amplitude.
3. Project onto the local kinetic functional.
4. Compare with Williams' holomorphic scheme by a finite local counterterm.

Until then, the prompt's coefficient is UNVERIFIED.

### Cross-check

Williams, arXiv:1809.02661, Theorems 3.1 and 3.4, establish one-loop finiteness/no-counterterm statements for holomorphic theories on \(\mathbb C^d\). Costello-Li's hCS anomaly computation concerns a ghost-number-one obstruction, not a wave-function counterterm. No checked primary source in this session supports the displayed \(N/(32\pi^3)\) coefficient.

## (G) Minimal \(L_\infty\) Model

### Claim

**Prompt claim.** Via Kontsevich-Soibelman homotopy transfer, on flat \(\mathbb C^3\) the harmonic subspace is
\[
H=\mathbb C[z_1,z_2,z_3]\otimes\mathfrak g,
\]
the propagator kills \(H\), and \(l_n^{\min}=0\) for \(n\ge3\). On compact CY\(_3\), the Atiyah class obstructs formality. On \(K3\times E\), \(At(TE)=0\), and a claimed Kuranishi cubic involving \(H^3(K3,\Omega^3_{K3})\) vanishes.

**Corrected claim.** The flat Dolbeault dg Lie algebra admits a contraction onto holomorphic functions, and the transferred \(L_\infty\) structure is the strict dg Lie bracket on holomorphic functions tensored with \(\mathfrak g\), with no higher brackets, provided the contraction is chosen compatibly. Compact CY\(_3\) formality is controlled by global Atiyah/HKR data. On \(K3\times E\), \(TE\) is trivial, but \(TK3\) is not; the vanishing of \(\Omega^3_{K3}\) is true but does not by itself annihilate all \(K3\times E\) cubic/Yukawa data.

### Derivation

On \(\mathbb C^3\), the Dolbeault complex
\[
(\Omega^{0,*}(\mathbb C^3),\bar\partial)
\]
is homotopy equivalent, on polynomial/entire functions with the chosen growth condition, to its \(\bar\partial\)-cohomology
\[
H^0_{\bar\partial}(\mathbb C^3,\mathcal O)=\mathcal O(\mathbb C^3),
\qquad
H^q_{\bar\partial}=0\quad(q>0).
\]
For the polynomial model this is
\[
\mathbb C[z_1,z_2,z_3].
\]
Tensoring with \(\mathfrak g\) gives
\[
H=\mathbb C[z_1,z_2,z_3]\otimes\mathfrak g.
\]

Let
\[
p:\Omega^{0,*}\to H,\qquad i:H\hookrightarrow\Omega^{0,*},\qquad h:\Omega^{0,*}\to\Omega^{0,*-1}
\]
satisfy
\[
\bar\partial h+h\bar\partial=\operatorname{id}-ip,
\qquad
ph=0,\quad hi=0,\quad h^2=0.
\]
The homotopy-transfer formula for higher brackets is a sum over trees with internal edges labelled by \(h\) and vertices labelled by the original binary bracket. If \(h\) annihilates the holomorphic image and the bracket of holomorphic functions is holomorphic, then every tree with an internal \(h\)-edge applied after a holomorphic bracket vanishes. Hence
\[
l_2(f\otimes x,g\otimes y)=fg\otimes[x,y],
\qquad
l_n=0\quad(n\ge3).
\]
This is a classical flat statement; it is not a quantum anomaly statement.

For compact CY\(_3\), the Dolbeault complex has nontrivial higher cohomology. Global HKR/formality for sheaves is obstructed by the Atiyah class
\[
At(TX)\in H^1(X,\Omega_X^1\otimes\operatorname{End}(TX)).
\]
The Atiyah class records the obstruction to a global holomorphic connection and enters the correction terms in global formality/HKR identifications.

For \(K3\times E\):
\[
T(K3\times E)\cong p_1^*TK3\oplus p_2^*TE.
\]
Since \(E\) is a complex Lie group, \(TE\) is holomorphically trivial, so
\[
At(TE)=0.
\]
But \(At(TK3)\) is generally nonzero. Also \(\Omega^3_{K3}=0\) because \(\dim_\mathbb C K3=2\), so
\[
H^3(K3,\Omega^3_{K3})=0
\]
is a true but weak statement. It does not imply that all cubic terms on \(K3\times E\) vanish; the product has complex dimension \(3\), and mixed \(K3\)-\(E\) classes may survive.

### Attack

1. "Harmonic subspace \(H=\mathbb C[z]\otimes\mathfrak g\)" is false for all smooth functions unless a polynomial/entire/growth condition is fixed.
2. \(l_n=0\) for \(n\ge3\) requires a compatible contraction. It is not automatic for an arbitrary propagator.
3. The nonabelian binary bracket \(l_2\) does not vanish.
4. The compact CY\(_3\) Atiyah-class statement is a formality/HKR statement, not a direct statement about the local flat minimal model.
5. \(At(TE)=0\) does not imply \(At(T(K3\times E))=0\).
6. \(H^3(K3,\Omega^3_{K3})=0\) is dimensionally true but not the relevant full Kuranishi/Yukawa computation for \(K3\times E\).

### Heal

State the flat minimal model as:
\[
\left(\mathbb C[z_1,z_2,z_3]\otimes\mathfrak g,\ l_2,\ l_n=0\ (n\ge3)\right)
\]
under the polynomial Dolbeault contraction. For compact CY\(_3\), replace broad "Atiyah obstruction" language by the precise global formality/HKR obstruction role of \(At(TX)\). For \(K3\times E\), keep \(At(TE)=0\) but retain \(At(TK3)\) and mixed product classes.

### Cross-check

The flat Dolbeault contraction is the standard Dolbeault-Poincare lemma in polynomial/Stein settings. The Atiyah-class role is part of the Kontsevich-Soibelman/HKR formality framework; exact primary page not reverified. The local treatise `CoHA_to_W_infty_treatise.tex` itself later states that \(K3\times E\) can have a one-dimensional cubic/Yukawa datum even when \(\chi(K3\times E)=0\), so the stronger vanishing claim must be narrowed.

## (H) First-Order Deformation Moduli

### Claim

**Prompt claim.**
\[
\operatorname{Def}(\operatorname{Obs}_{\mathrm{hCS}})
=HH^*_{E_3}(\operatorname{Obs},\operatorname{Obs})[3],
\]
and on \(\mathbb C^3\) with simple \(\mathfrak g\),
\[
T_0\mathcal M
=H^{0,3}_{\bar\partial,c}(\mathbb C^3)
\otimes\operatorname{Sym}^2(\mathfrak g^\vee)^{\mathfrak g}
=\mathbb C\cdot\operatorname{Kil}.
\]
This should match the Yangian deformation \(Y_{\epsilon_1,\epsilon_2,\epsilon_3}\) on the Calabi-Yau slice \(\epsilon_1+\epsilon_2+\epsilon_3=0\).

**Corrected claim.** The deformation complex of an \(E_n\)-algebra is \(E_n\)-Hochschild cochains shifted by \(n\), so the displayed \(HH_{E_3}[3]\) form is structurally correct. The tangent computation on \(\mathbb C^3\) is correct only after replacing global compactly supported Dolbeault cohomology by a local residue/translation-invariant sector. The Yangian match is compatible with CoHA\((\mathbb C^3)\), but it is not a CFG 2026 theorem.

### Derivation

For an \(E_n\)-algebra \(A\), first-order deformations are governed by the deformation complex
\[
\operatorname{Def}_{E_n}(A)
\simeq HH^*_{E_n}(A,A)[n]
\]
in the convention where Maurer-Cartan elements of this shifted dg Lie algebra deform the \(E_n\)-multiplication.
For \(n=3\),
\[
\operatorname{Def}_{E_3}(A)\simeq HH^*_{E_3}(A,A)[3].
\]

For hCS, a first-order local deformation of the kinetic/coupling data preserving gauge invariance is built from:

1. a top Dolbeault residue/current on \(\mathbb C^3\), and
2. an invariant symmetric bilinear form on \(\mathfrak g\).

For simple \(\mathfrak g\),
\[
\operatorname{Sym}^2(\mathfrak g^\vee)^{\mathfrak g}
=\mathbb C\cdot\kappa_{\mathrm{Kil}}.
\]
The local Dolbeault residue sector has one generator, represented by the compactly supported top Dolbeault class dual to constants:
\[
H_c^{0,3}(\mathbb C^3)_{\mathrm{res}}\cong\mathbb C.
\]
Therefore the *local residue tangent* is
\[
T_0\mathcal M_{\mathrm{loc}}
\cong\mathbb C\cdot\kappa_{\mathrm{Kil}}.
\]

However, without the word "local" or "translation-invariant residue", ordinary compactly supported Dolbeault cohomology on \(\mathbb C^3\) is Serre dual to global holomorphic functions:
\[
H_c^{0,3}(\mathbb C^3)^\vee\simeq H^0(\mathbb C^3,\mathcal O),
\]
which is infinite-dimensional for entire functions and polynomially infinite for polynomial functions. Thus the one-dimensional answer needs a locality/translation-invariance restriction.

The CoHA/Yangian side is:
\[
\operatorname{CoHA}(\mathbb C^3)
\rightsquigarrow
Y^+(\widehat{\mathfrak{gl}}_1),
\]
with deformation parameters \((\epsilon_1,\epsilon_2,\epsilon_3)\) satisfying the Calabi-Yau slice
\[
\epsilon_1+\epsilon_2+\epsilon_3=0.
\]
This is compatible with a one-dimensional local deformation after quotienting by overall scaling and imposing the CY relation, but the exact equivalence to hCS observables is not proved by CFG 2026.

### Attack

1. The \(HH_{E_3}[3]\) convention needs a source; the exact Francis/Lurie theorem was not rechecked here.
2. \(H_c^{0,3}(\mathbb C^3)\cong\mathbb C\) is false unless a local residue/translation-invariant restriction is imposed.
3. The Yangian deformation parameters live in an equivariant/CoHA deformation theory, not directly in ordinary hCS BV deformation theory without a comparison theorem.
4. The CY slice \(\epsilon_1+\epsilon_2+\epsilon_3=0\) is a relation, not a distinguished numerical value.
5. CFG 2026 does not establish this hCS-Yangian match.

### Heal

Replace
\[
H^{0,3}_{\bar\partial,c}(\mathbb C^3)=\mathbb C
\]
by
\[
H^{0,3}_{\bar\partial,c}(\mathbb C^3)_{\mathrm{loc/res}}
\cong\mathbb C.
\]
State the Yangian comparison as a conjectural or separately proved CoHA-to-hCS bridge:
\[
\operatorname{Def}_{E_3}(\operatorname{Obs}_{\mathrm{hCS}})
\stackrel{?}{\longleftrightarrow}
\operatorname{Def}(Y_{\epsilon_1,\epsilon_2,\epsilon_3})
\quad
\text{on } \epsilon_1+\epsilon_2+\epsilon_3=0.
\]

### Cross-check

The local `CoHA_to_W_infty_treatise.tex` correctly treats \(\epsilon_1+\epsilon_2+\epsilon_3=0\) as the Calabi-Yau relation, not a chosen value. The simple-Lie-algebra invariant bilinear statement is standard and follows from simplicity. The exact \(E_n\)-Hochschild deformation theorem should be checked against Francis' deformation-complex theorem or Lurie HA before upgrading this section to a fully proved theorem.

## (I) Dualizability and \(E_3\)-Koszul

### Claim

**Prompt claim.** The \(E_3\)-trace is detected by
\[
S^5=\partial\overline{\operatorname{Conf}}_2(\mathbb C^3),
\]
nondegenerate on the abelian sector. Nonabelian 3-dualizability on \(\mathbb C^3\) fails because
\[
HH^0_{E_3}(\operatorname{Obs})
=\mathbb C[[\tau_1,\tau_2,\tau_3]]
\]
by Gwilliam-Williams 2021 Proposition 5.3.2. Compact CY\(_3\) recovers dualizability. Also
\[
D_3^!\simeq \operatorname{Lie}[2]
\]
by Fresse 2017, with strict/homotopy compatibility via Fresse and Positselski.

**Corrected claim.** The \(S^5\) boundary is the Bochner-Martinelli residue sphere for complex dimension \(3\). Calling it an \(E_3\)-trace requires the Dolbeault-reduced avatar; a literal \(E_3\) trace would more naturally involve the \(E_3\) operadic sphere dimension, not the real \(S^5\) of \(\mathbb C^3\). The infinite formal-power-series algebra \(\mathbb C[[\tau_1,\tau_2,\tau_3]]\) is source-supported by Gwilliam-Williams' formal CE computation, but the exact citation "Proposition 5.3.2" was not verified. The compact recovery statement is conditional on anomaly cancellation and finite-dimensional cohomology. Fresse supports \(E_n\)-Koszul duality, but the exact book theorem numbers in the prompt were not verified.

### Derivation

The configuration space of two distinct points in \(\mathbb C^3\) modulo translation has radial boundary
\[
\partial\overline{\operatorname{Conf}}_2(\mathbb C^3)
\simeq S^5.
\]
The BM residue pairing is integration over this \(S^5\):
\[
\int_{S^5}\omega_{\mathrm{BM}}=1.
\]
For the abelian hCS theory, observables are Gaussian/free, and this residue pairing gives a nondegenerate pairing between fields and antifields after restricting to the finite local residue sector.

For nonabelian hCS on \(\mathbb C^3\), the local observable algebra retains infinitely many holomorphic jets. The formal CE algebra of an abelian shifted \(\mathbb C^3\)-translation piece has the form
\[
\mathbb C[[\tau_1,\tau_2,\tau_3]],
\]
as in Gwilliam-Williams' computation for \(L=\mathbb C^n[-1]\). This infinite-dimensional Hochschild/center piece obstructs full finite 3-dualizability in the naive noncompact category. Compact CY\(_3\) replaces holomorphic polynomial/jets by finite-dimensional Dolbeault cohomology, but dualizability still requires:

1. a finite/perfect category of observables or modules,
2. nondegenerate trace pairing,
3. anomaly cancellation or a consistent quantum lift,
4. a completed category in which the trace exists.

For \(E_n\)-Koszul duality, Fresse constructs weak equivalences
\[
B^c(\Lambda^{-n}E_n^\vee)\longrightarrow E_n.
\]
This is the precise source-checked form from the accessible Fresse paper. Passing to homology recovers the familiar shifted Poisson/Gerstenhaber Koszul-duality pattern in which Lie brackets are shifted by \(n-1\). For \(n=3\), this is the source of the informal slogan
\[
E_3^!\sim E_3[-3],
\qquad
\text{and at homology level a Lie bracket shifted by }2.
\]
The stricter statement \(D_3^!\simeq\operatorname{Lie}[2]\) needs the exact operad \(D_3\) and convention specified before it is a theorem.

### Attack

1. \(S^5\) is correct for the BM kernel, but not automatically the literal trace sphere of an abstract \(E_3\)-algebra.
2. "GW 2021 Proposition 5.3.2" was not found in the checked arXiv text. The local result is supported by Gwilliam-Williams' Appendix A example/formal CE computation, not that exact proposition number.
3. Compact CY\(_3\) finite-dimensional cohomology does not by itself prove quantum 3-dualizability; the anomaly and trace must be handled.
4. The operad notation \(D_3^!\) is ambiguous. Little disks, chains on little disks, homology \(e_3\), and their suspensions have different Koszul-dual statements.
5. The Positselski coderived/contraderived transfer was not checked from a primary source in this session.

### Heal

State:

> The BM residue trace uses \(S^5\). After Dolbeault reduction this is part of the \(E_3\)-avatar trace data. Noncompact nonabelian \(\mathbb C^3\) is not fully 3-dualizable because the relevant center/Hochschild sector contains formal power series in three variables. Compact CY\(_3\) recovery is conditional on a finite, anomaly-free quantum model.

Replace the exact "GW Prop 5.3.2" citation by:

> Gwilliam-Williams, arXiv:1810.06534, Appendix A, Example A.4, computes \(C^*_{\mathrm{Lie}}(\mathbb C^n[-1])=\mathbb C[[t_1,\dots,t_n]]\). The exact final published proposition number remains to be verified.

Replace \(D_3^!\simeq\operatorname{Lie}[2]\) by the checked Fresse statement:
\[
B^c(\Lambda^{-3}E_3^\vee)\xrightarrow{\sim}E_3,
\]
plus the homology-level shifted Lie slogan with conventions stated.

### Cross-check

Gwilliam-Williams, arXiv:1810.06534, Proposition 2.2 verifies the \(S^5\)-normalised BM residue, and Appendix A, Example A.4 supports the formal \(\mathbb C[[\tau_1,\tau_2,\tau_3]]\) computation. Fresse's accessible paper *Koszul duality of \(E_n\)-operads* gives Theorems A/B constructing weak equivalences \(B^c(\Lambda^{-n}E_n^\vee)\to E_n\). The prompt's exact Fresse 2017 book theorem numbers were not verified.

## (J) Cross-Consistency Audit with `CoHA_to_W_infty_treatise.tex`

### J.1 CoHA\((\mathbb C^3)\) to \(Y^+(\widehat{\mathfrak{gl}}_1)\)

The treatise's core \(\mathbb C^3\) CoHA chain is compatible with the corrected hCS story when stated in two stages:
\[
\operatorname{Coh}(\mathbb C^3)
\xrightarrow{\ \Phi^{FA}_3\ }
\text{holomorphic factorization/\(E_3\)-avatar data}
\xrightarrow{\ Sp^{ch}_{\Sigma_2,\mathbb C}\ }
\text{chiral/Yangian shadow}.
\]
For the Jordan triple-loop quiver with potential
\[
W=\operatorname{tr}(X[Y,Z]),
\]
the Jacobi algebra is
\[
\mathbb C[X,Y,Z].
\]
The CoHA is realised as a Schiffmann-Vasserot shuffle algebra. Its positive half is
\[
Y^+(\widehat{\mathfrak{gl}}_1),
\]
and the full affine Yangian arises after Drinfeld double/central extension/completion. This is compatible with the hCS \(E_3\)-avatar only after the comparison theorem is supplied.

### J.2 Numerical and Convention Inconsistencies

1. **CFG source mismatch.** The treatise says the CFG \(E_3\)-deformation source was pending; the present prompt treats it as an available 6D hCS source. Heal: cite CFG only for ordinary 3D CS \(E_3\), and mark the 6D hCS comparison as a new theorem to prove.
2. **Action coefficient mismatch.** One treatise passage writes a cubic hCS coefficient equivalent to \(2/3\). Later it writes the standard \(1/2,1/6\). Heal: standardise to
   \[
   \int\Omega\wedge\left(\frac12\langle A,\bar\partial A\rangle+\frac16\langle A,[A,A]\rangle\right).
   \]
3. **\(E_3\) versus \(E_6\).** The treatise often says "holomorphic \(E_3\)" without warning. Heal: full real geometric factorization is \(E_6\)-like before Dolbeault reduction; the hCS avatar is \(E_3\) after \(\bar\partial\)-reduction.
4. **BM kernel.** The treatise's coefficient \(2/(2\pi i)^3\) is compatible with Gwilliam-Williams. Heal: add the orientation convention and the \((d-1)!/(2\pi i)^d\) source.
5. **Anomaly formula.** The treatise's cubic/\(\chi_{\mathrm{top}}\) anomaly formula conflicts with Costello-Li. Heal: replace by quartic adjoint invariant and four-vertex one-loop hCS anomaly; keep \(\chi_{\mathrm{top}}\) only as a separately proved global/index coefficient.
6. **Quintic coefficient.** The treatise's quintic insertion using \(-200\) has the right Euler number but the wrong/unverified Lie polynomial and denominator. Heal: write \(-200\,\hbar C_{\mathrm{scheme}}(\mathfrak g)\) until the index normalisation is proved.
7. **Wave-function coefficient.** The treatise/prompt logarithmic coefficient conflicts with Williams one-loop finiteness. Heal: mark absent in holomorphic renormalisation; regulator-dependent if introduced elsewhere.
8. **Gwilliam-Williams citation.** The local notes cite arXiv:2009.05037 and "Prop 5.3.2"; the checked source for higher Kac-Moody is arXiv:1810.06534, and the formal \(\mathbb C[[t_1,t_2,t_3]]\) computation is in Appendix A, Example A.4. Heal citation.
9. **\(K3\times E\) vanishing.** The treatise correctly notes \(\chi(K3\times E)=0\) but should not infer all cubic/Yukawa data vanish. Heal: separate global one-loop Euler coefficients from tree-level or Hodge-theoretic cubic data.
10. **CY parameter slice.** The treatise's corrected statement is right: \(\epsilon_1+\epsilon_2+\epsilon_3=0\) is a Calabi-Yau relation, not a special point such as \(\lambda=-1\). Preserve this.
11. **Stage-2 output.** The output is \(Y^+(\widehat{\mathfrak{gl}}_1)\) at the positive-half level. The full Yangian and \(W_{1+\infty}\) require double/central/module constructions. Heal: do not write direct equality between CoHA\((\mathbb C^3)\) and full \(W_{1+\infty}\).

### J.3 Healed Cross-Consistent Statement

The corrected cross-volume statement is:

> The \(\mathbb C^3\) CoHA of the Jordan triple-loop quiver is a shuffle algebra whose positive half is \(Y^+(\widehat{\mathfrak{gl}}_1)\). This is compatible with the Dolbeault-reduced \(E_3\)-avatar of 6D hCS observables on \(\mathbb C^3\), provided one proves the missing comparison theorem between hCS local observables and the CoHA factorization algebra. The BM kernel normalisation agrees. The cubic theta anomaly and logarithmic wave-function coefficient must be removed or marked conjectural; primary hCS anomaly data are quartic and Williams gives holomorphic one-loop finiteness.

## (K) Frontier Push: Next Theorems to Prove

### K.1 The Next Thing to Prove

The next theorem is not another numerical table. It is the missing comparison theorem:

**Theorem K.1 (CFG-to-hCS Avatar Comparison, target).**  
Let \(A_\lambda^{\mathrm{CFG}}\) be the filtered \(E_3\)-algebra produced by CFG 2026 from ordinary Chern-Simons theory. Let \(\operatorname{Obs}_{\mathrm{hCS}}^{\bar\partial}(\mathbb C^3,\mathfrak g)\) be the Dolbeault-reduced local quantum observable algebra of six-dimensional hCS, after anomaly cancellation or restriction to an anomaly-free sector. Construct a filtered \(E_3\)-functor or deformation comparison
\[
A_\lambda^{\mathrm{CFG}}
\longrightarrow
\operatorname{Obs}_{\mathrm{hCS}}^{\bar\partial}(\mathbb C^3,\mathfrak g)
\]
or prove no such functor can exist without adding CoHA/Yangian boundary data. The theorem must identify products, brackets, traces, filtrations, and deformation parameters.

Until Theorem K.1 is proved, "CFG 2026 6D hCS" is a slogan, not a theorem.

### K.2 Missing Lemmas and Computations

1. **Source-map lemma.** Produce a table of exact theorem/page references: CFG 2026 for ordinary CS \(E_3\), Costello-Li for hCS anomaly, Williams for one-loop finiteness, Gwilliam-Williams for BM and higher Kac-Moody, Costello-Paquette for hCS Koszul-dual chiral operators, Fresse for \(E_n\)-Koszul.
2. **BV normalisation lemma.** Fix once and for all the shift convention, Serre-duality orientation, BV bracket sign, and \(1/2,1/6\) hCS action normalisation.
3. **BM kernel lemma.** Derive
   \[
   \omega_{\mathrm{BM}}^{(3)}
   =\frac2{(2\pi i)^3}\sum_i(-1)^{i-1}
   \frac{\bar z_i\,d\bar z_1\wedge\widehat{d\bar z_i}\wedge d\bar z_3}{\|z\|^6}
   \]
   with the exact orientation used in the factorization product.
4. **Local anomaly theorem.** Recompute the one-loop hCS obstruction on \(\mathbb C^3\) from the regulated four-vertex wheel and identify the quartic Lie polynomial. Separate pure hCS from open-closed Green-Schwarz cancellation.
5. **Global index theorem.** If a coefficient proportional to \(\chi_{\mathrm{top}}(X)\) is desired, derive it from Grothendieck-Riemann-Roch/family index methods and fix the denominator. For the quintic the topological factor is already proved to be \(-200\).
6. **Wave-function theorem.** Either prove Williams' no-counterterm theorem applies to the exact hCS setup used here, or define a non-holomorphic regulator and compute the finite scheme transformation producing any kinetic counterterm.
7. **Dolbeault-reduction theorem.** Prove the passage
   \[
   \text{holomorphic factorization on }\mathbb C^3
   \to
   E_3\text{-avatar}
   \]
   with explicit shuffle/Koszul signs.
8. **Deformation-complex theorem.** Verify
   \[
   \operatorname{Def}(\operatorname{Obs}_{\mathrm{hCS}})
   \simeq HH^*_{E_3}(\operatorname{Obs},\operatorname{Obs})[3]
   \]
   from Francis/Lurie/Gwilliam-Williams with exact conventions.
9. **CoHA comparison theorem.** Prove that the Stage-1 factorization algebra attached to \(\operatorname{CoHA}(\mathbb C^3)\) maps to hCS local observables, and that Stage 2 produces \(Y^+(\widehat{\mathfrak{gl}}_1)\). Then identify when the double gives the full affine Yangian and when the module category gives \(W_{1+\infty}\).
10. **Compact dualizability theorem.** Prove finite 3-dualizability for compact CY\(_3\) only under explicit finiteness, trace nondegeneracy, and anomaly-cancellation hypotheses.

### K.3 Status Split

**Proved or directly source-checked here.**

1. hCS classical BV action uses \(1/2,1/6\).
2. The BM coefficient in complex dimension \(3\) is \(2/(2\pi i)^3\).
3. The prompt's cubic theta anomaly is not the Costello-Li hCS one-loop anomaly.
4. Williams' holomorphic one-loop finiteness contradicts the asserted flat logarithmic counterterm.
5. \(\chi_{\mathrm{top}}\) of the quintic is \(-200\).
6. CoHA\((\mathbb C^3)\) positive half matches \(Y^+(\widehat{\mathfrak{gl}}_1)\) in the local treatise's shuffle-algebra surface, subject to standard CoHA references.

**Computationally verified here.**

1. \(c(TX_5)=(1+h)^5/(1+5h)=1+10h^2-40h^3\).
2. \(\int_{X_5}c_3=-40\cdot5=-200\).
3. \((3-1)!/(2\pi i)^3=2/(2\pi i)^3\).

**Conditional.**

1. Any \(\chi_{\mathrm{top}}\)-weighted hCS anomaly coefficient with a fixed denominator.
2. Compact CY\(_3\) recovery of full 3-dualizability.
3. CHSW standard embedding as an hCS BV anomaly trivialisation.
4. The exact CFG-to-hCS \(E_3\) avatar comparison.

**Rejected or unverified.**

1. "CFG 2026 proves 6D hCS \(E_3\)." Rejected.
2. Cubic theta graph as primary hCS one-loop anomaly. Rejected.
3. \(A(\mathfrak g)=d^{abc}\) vanishing list as hCS anomaly criterion. Rejected.
4. Flat hCS wave-function coefficient \(N/(32\pi^3)\). Unverified and incompatible with the holomorphic scheme.
5. "GW 2021 Prop 5.3.2 says \(HH^0=\mathbb C[[\tau_1,\tau_2,\tau_3]]\)." Exact citation unverified; corrected to Gwilliam-Williams arXiv:1810.06534, Appendix A, Example A.4 support.
6. Exact "Fresse 2017 Vol I Thm 14.1.A/12.3.A" citations. Unverified from the accessible paper; use the checked \(B^c(\Lambda^{-n}E_n^\vee)\to E_n\) theorem form.

## Appendix: Bibliography and Verified Citation Status

1. Kevin Costello, Owen Gwilliam, *Factorization Algebras in Quantum Field Theory*, Vol. I, 2017; Vol. II, 2021. Standard BV/factorization references. Exact pages for the shift-law table and QME conventions were not reverified in this session.
2. Kevin Costello, John Francis, Owen Gwilliam, *Chern-Simons factorization algebras and knot polynomials*, arXiv:2602.12412, 2026. Verified Theorem 1.1: ordinary 3D Chern-Simons gives a filtered \(E_3\)-algebra \(A_\lambda\) and perfect modules whose traces recover Reshetikhin-Turaev invariants. No 6D hCS theorem found.
3. Kevin Costello and Si Li, *Anomaly cancellation in the topological string*, arXiv:1905.09269. Verified hCS action normalisation \(1/2,1/6\), equation \(\bar\partial A+\frac12[A,A]=0\), and one-loop hCS gauge anomaly via a four-vertex diagram and \(\operatorname{Tr}_{\mathrm{ad}}A(F_A)^3\).
4. Brian R. Williams, *Renormalization for Holomorphic Field Theories*, arXiv:1809.02661. Verified Theorems 3.1 and 3.4: one-loop holomorphic theories on \(\mathbb C^d\) admit quantisation with no counterterms in the holomorphic scheme.
5. Owen Gwilliam and Brian R. Williams, *Higher Kac-Moody Algebras and Symmetries of Holomorphic Field Theories*, arXiv:1810.06534, published in ATMP 2021. Verified Proposition 2.2 for the algebraic Bochner-Martinelli kernel and Appendix A, Example A.4 for \(C^*_{\mathrm{Lie}}(\mathbb C^n[-1])=\mathbb C[[t_1,\dots,t_n]]\). The prompt's "Prop 5.3.2" citation was not verified.
6. Kevin Costello and Natalie Paquette, *Twisted Supergravity and Koszul Duality: A Case Study in AdS3*, arXiv:2001.02177. Verified Section 6.3 hCS setup on \(\mathbb C\times\mathbb C^2\), tree-level local operators, and the stated warning that hCS has a one-loop rectangle anomaly without Kodaira-Spencer coupling.
7. Benoit Fresse, *Koszul duality of \(E_n\)-operads*. Verified accessible paper Theorems A/B: weak equivalences \(B^c(\Lambda^{-n}E_n^\vee)\to E_n\). The exact book references "Vol I Thm 14.1.A" and "Thm 12.3.A" were not verified.
8. Candelas-Horowitz-Strominger-Witten, *Vacuum Configurations for Superstrings*, 1985. Used only for the standard-embedding context \(F=R\) in heterotic compactifications. Exact page not reverified; application to pure hCS BV anomaly cancellation is CONDITIONAL.
9. Local source: `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_waves_11_through_16.tex`, lines 75-185. Contains the 6D hCS synthesis audited here.
10. Local source: `/Users/raeez/calabi-yau-quantum-groups/notes/CoHA_to_W_infty_treatise.tex`, lines 1-250 and later hCS sections. Contains the \(\mathbb C^3\) CoHA-to-\(Y^+(\widehat{\mathfrak{gl}}_1)\) surface and several anomaly/action normalisation claims corrected above.
11. Local source: `/Users/raeez/chiral-bar-cobar/notes/6d_hCS_audit_2026_04_22_cross_volume_errors.md`. Contains prior cross-volume flags: cubic-vs-quartic anomaly, theta-vs-wheel graph, \(E_6\)-before-\(E_3\) reduction, and Stage-2 CoHA warnings. These flags agree with the primary-source corrections made here except where exact group-cancellation wording still requires a primary theorem.
