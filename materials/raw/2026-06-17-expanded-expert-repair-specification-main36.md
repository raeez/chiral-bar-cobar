# Expanded Expert Repair Specification for `main(36).pdf`

## Purpose

This memo is an ambition-preserving repair plan. It does **not** shrink the manuscript. It adds the proof-contract layer, type discipline, geometry, physics interfaces, and convention controls needed for a reader at the level of Etingof, Kontsevich, Gelfand, Polyakov, Gaiotto, Costello, and Witten.

## A. Global structural repairs

### A1. Install a theorem-status firewall before the first theorem-bearing chapter

Every result must be labeled as one of:

1. **Theorem**: fully proved from stated hypotheses in the current volume.
2. **Comparison theorem**: fully proved once a named external comparison package is assumed.
3. **Conditional theorem**: proved only under a named package of hypotheses.
4. **Conjecture**: no complete proof in the manuscript.
5. **Numerical evidence**: finite-window computation only.
6. **Physical derivation**: physically motivated derivation, not an algebraic proof.
7. **Dictionary/atlas entry**: a typed comparison or reconstruction surface, not a theorem.

This prevents the manuscript from using physical or computational rhetoric as hidden proof.

### A2. Move ambient hypotheses before theorem statements

Theorem A and its descendants must be stated only after the Francis--Gaitsgory/Ran factorization ambient, exact base change, conilpotent-complete coalgebra side, and properadic-envelope hypotheses are introduced.

### A3. Enforce four-object separation

The manuscript must never conflate:

- \(B_X^{\mathrm{ord}}(A)\): ordered bar coalgebra,
- \(B_X^\Sigma(A)\): symmetric averaged bar coalgebra,
- \(A^i = H^\bullet B(A)\): bar-dual coalgebra/cohomology object,
- \(A^! = (A^i)^\vee\): strict Koszul dual algebra,
- \(Z_{\mathrm{ch}}^{\mathrm{der}}(A)\): derived chiral center.

A repair pass should grep all occurrences of “bar cohomology”, “chiral Hochschild”, “center”, “bulk”, “Koszul dual”, and “inverse” and type them.

### A4. Replace global \(d\log(z_i-z_j)\) rhetoric by local representatives plus global transition data

Use:

\[
\eta_{ij}=d\log(z_i-z_j)
\]

only on an affine chart, formal disk, or tangent collision screen. Globally on \(X\), define the logarithmic normal form along \(D_{ij}\) as a section of the log de Rham complex with transition cocycle governed by coordinate change. On genus \(g\ge1\), replace the genus-zero form by prime-form/KZB representatives and period data.

### A5. Rewrite \(d_B=KZ^*(\nabla_{\mathrm{Arnold}})\) as a typed superconnection statement

Correct target statement:

\[
D_{A,n}=d_{\mathrm{dR}}+d_A-\sum_{i<j}\rho_A(t_{ij})\eta_{ij}
\]

is a flat superconnection on the coefficient bundle over the ordered configuration space, and the chain differential on the ordered bar complex is the total residue/de Rham/internal differential induced by this superconnection. The literal equality between a chain differential and a connection is shorthand only after applying the residue realization functor.

### A6. Replace “Arnold proves \(d^2=0\)” by “Arnold + Borcherds prove \(d^2=0\)”

Nilpotence requires:

- internal differential squares to zero;
- de Rham differential squares to zero;
- residue/de Rham compatibility by Stokes;
- internal/residue compatibility by the chiral derivation property;
- disjoint residues supercommute by transverse normal-crossing orientation;
- repeated same divisor residue vanishes because the first residue removes the unique logarithmic normal factor;
- triple-collision residue terms vanish by **Arnold on forms** plus **Borcherds on OPE coefficients**.

### A7. Repair positive-genus curvature language

Use curved \(A_\infty\)/CDG language:

\[
m_1^2(a)=m_2(m_0,a)-(-1)^{|a|}m_2(a,m_0)=[m_0,a].
\]

The scalar statement \(d_{\mathrm{fib}}^2=\kappa(A)\lambda_g\) is a shadow statement only after passing to the scalar diagonal/uniform-weight projection. The total period-corrected modular differential \(D_g\) is the square-zero object.

### A8. Formalize ordered-to-symmetric averaging

State a theorem:

\[
B_X^\Sigma(A)\simeq \left(B_X^{\mathrm{ord}}(A)\right)_{\Sigma_n,L_R}
\]

under:
- QYBE for \(R\),
- unitarity \(R_{21}(-z)R_{12}(z)=1\),
- regular-singular FM extension,
- compatible local system \(L_R\),
- conilpotent completion.

Define the kernel as the “ordered information-loss conductor”, not as metaphor.

## B. Expert-specific gates

### B1. Etingof gate

Etingof will require exact control of quantum groups, \(R\)-matrices, completions, and PBW hypotheses.

Add:

- a single \(q\)-convention theorem:
  \[
  q_{\mathrm{KL}}=\exp(\pi i\hbar),\qquad q_{\mathrm{DK}}=\exp(2\pi i\hbar),\qquad q_{\mathrm{DK}}=q_{\mathrm{KL}}^2;
  \]
- explicit trace-form versus KZ-form \(r\)-matrix conversion:
  \[
  r_{\mathrm{tr}}=\frac{k\Omega_{\mathrm{tr}}}{z},
  \qquad
  r_{\mathrm{KZ}}=\frac{\Omega}{(k+h^\vee)z},
  \qquad
  \Omega=2h^\vee\Omega_{\mathrm{tr}};
  \]
- a finite-window versus completed-category distinction for Yangian/RTT statements;
- statement of PBW hypotheses before every Yangian, shifted-Yangian, Hall, or EK quantization claim;
- no “Etingof--Kazhdan quantization” unless the exact Lie bialgebra, topology, associator, and equivalence target are specified.

### B2. Kontsevich gate

Kontsevich will require geometric precision.

Add:

- local/global distinction for \(d\log\);
- exact choice of FM compactification: algebraic FM, real oriented blowup, logarithmic FM, or ordered FM;
- orientation and determinant-line conventions on every residue map;
- graph complex orientation conventions;
- precise formality torsor and associator dependence;
- separation of the graph-integral theorem from chiral deformation quantization analogies;
- statement of whether \(GRT_1\) acts, is trivialized, or is merely conjecturally recognized.

### B3. Gelfand gate

Gelfand will require object separation and cohomological discipline.

Add:

- a D-module definition of chiral algebra and chiral operation;
- a typed comparison among chiral Hochschild, algebraic Hochschild, topological Hochschild, Lie algebra cohomology, and Gelfand--Fuchs cohomology;
- exact continuity/topology hypotheses for mode Lie algebras;
- no identification of critical center, derived center, Drinfeld center, and bar cohomology without a named theorem.

### B4. Polyakov gate

Polyakov will require anomaly accounting.

Add:

- determinant-line formulation of the partition function;
- separation of \(c\), \(\kappa\), ghost central charge, and BRST anomaly;
- explicit \(bc\) ghost complex, BRST current, nilpotence condition, and anomaly cancellation equation;
- Polyakov measure and Liouville/Weyl anomaly dictionary;
- stress-tensor OPE and Schwarzian/projective-connection transformation law;
- statement of when \(c+c'=26\) or \(100\) is algebraic complementarity and when it is physical string criticality.

### B5. Gaiotto gate

Gaiotto will require boundary/line/bulk category precision.

Add:

- boundary algebra \(A\), line category \(\mathcal L_A\), derived center \(Z_{\mathrm{ch}}^{\mathrm{der}}(A)\), and physical bulk \(\mathcal O_{\mathrm{bulk}}\) as separate slots;
- precise open/closed functor \(OCA\) and its hypotheses;
- no class-S, corner VOA, or \(Y\)-algebra claim without Ω-background parameters and boundary conditions;
- DS reduction as a functor on primitive triples, not an equality of all structures;
- exact scope of \(Y_{L,M,N}[\Psi]\), affine Yangian, and shifted Yangian comparisons.

### B6. Costello gate

Costello will require BV/factorization/renormalization discipline.

Add:

- local-to-global factorization algebra definitions;
- QME versus CME distinction;
- renormalization group data: scale parameter, propagator, counterterms, local functional space;
- analytic SDR hypotheses before any all-loop QME or \(E_3\)-lift statement;
- distinction between locally constant topological \(E_n\) and holomorphic-topological/chiral structures;
- pro-completion and Mittag--Leffler hypotheses in every infinite bar/cobar statement.

### B7. Witten gate

Witten will require physical state-space and anomaly correctness.

Add:

- Chern--Simons/WZW boundary condition data;
- framing anomaly and modular functor normalization;
- Hilbert spaces/conformal blocks as actual spaces or derived complexes;
- Wilson-line/line-operator category and braiding;
- ghost sector and BRST cohomology for string claims;
- separation of “central-charge complementarity” from “physical critical string theorem”;
- exact statement of what is mathematical theorem, what is physical derivation, and what remains conjectural.

## C. Critical local repairs

### C1. Same-pair residue

Replace “same pair vanishes for degree reasons” by:

\[
\operatorname{Res}_{D_{ij}}\circ\operatorname{Res}_{D_{ij}}=0
\]

because after the first residue the logarithmic normal factor \(d\log u_{ij}\) has been removed. This is a residue exact-sequence/normal-crossing statement, not a degree-count slogan.

### C2. \(\beta\gamma\) residue

The raw OPE contraction

\[
\beta(z)\gamma(w)\sim \frac{1}{z-w}
\]

is nonzero. In the manuscript’s \(r_{\mathrm{coll}}\) convention, the \(d\log\)-bar kernel absorbs the simple pole completely, so the **pole-valued collision \(r\)-matrix** is zero. The regular contact operator \(\Theta_{\beta\gamma}=\beta\otimes\gamma-\gamma\otimes\beta\) remains nonzero and must be tracked separately.

### C3. Feigin--Frenkel language

Rename \(k\mapsto -k-2h^\vee\) as the “critical-level reflection” or “Feigin--Frenkel level reflection on the non-critical Verdier/Koszul lane,” not as the whole Feigin--Frenkel duality theorem. The critical center, the Koszul dual, the bar-cobar inverse, and the derived center remain distinct.

### C4. DDYBE

State:

- exact diagonal/separating degeneration to genus-one Felder DYBE: theorem;
- generic-\(\Omega\) DDYBE finite-window tests: numerical evidence;
- full genus-two DDYBE: conjecture;
- non-separating degeneration with \(\Omega_{12}\neq0\): frontier target.

### C5. K3/BKM/Hall

Keep the ambition but label the structure as conditional until the Hall/CoHA source, BKM Lie bialgebra, super-EK quantization, PBW theorem, and denominator/trace comparison are supplied.

## D. Replacement theorem skeleton

### D1. Typed Arnold--KZ theorem

Let \(X\) be a smooth genus-zero curve, \(A\) an augmented finite-weight \(E_1\)-chiral algebra with quasi-free BRST resolution and OPE residue representation
\[
\rho_A:\mathfrak t_n\to \operatorname{End}(B_{X,n}^{\mathrm{ord}}(A)).
\]
Then the superconnection
\[
D_{A,n}=d_{\mathrm{dR}}+d_A-\sum_{i<j}\rho_A(t_{ij})\eta_{ij}
\]
is flat if and only if the Arnold relations and Borcherds identities hold. The induced total differential on the residue-realized ordered bar complex is \(d_B\). This is the precise content of the slogan \(d_B=KZ^*(\nabla_{\mathrm{Arnold}})\).

### D2. Typed Theorem A

In the Francis--Gaitsgory factorization ambient \(Fact(X)\), assuming exact star-monoidal base change, conilpotent completeness, Mittag--Leffler convergence, and properadic transfer, the chiral bar and cobar functors form an adjunction:
\[
\Omega_X^{\mathrm{ch}}\dashv \bar B_X^{\mathrm{ch}}.
\]
On the Koszul locus:
\[
\Omega_X^{\mathrm{ch}}\bar B_X^{\mathrm{ch}}(A)\simeq A.
\]
Off the strict locus the statement belongs to the weight-completed coderived/contraderived Positselski surface. Verdier-dualized Koszul duality is a separate functor:
\[
\Omega_X^{\mathrm{cont}}\mathbb D_{\mathrm{Ran}}\bar B_X^{\mathrm{ch}}(A)\simeq A_\infty^!.
\]

### D3. Typed Theorem C

Define
\[
C^\bullet_{\mathrm{ch}}(A,A)=R\operatorname{Hom}_{A_{\mathrm{ch}}^e}(A,A),
\qquad
Z_{\mathrm{ch}}^{\mathrm{der}}(A)=C^\bullet_{\mathrm{ch}}(A,A)
\]
with its \(E_2/E_3\) structure only after the appropriate Deligne/Swiss-cheese hypotheses. Conductor identities are lane-specific:
\[
K_E,\quad K_c,\quad K_\kappa,\quad K_{\mathrm{ghost}}^{\mathrm{leg}}
\]
are distinct until a theorem identifies them.

### D4. Typed Theorem D

The genus tower is:
\[
F_g(A)=\kappa(A)\lambda_g^{\mathrm{FP}}+\delta F_g^{\mathrm{cross}}(A),
\]
where the first term is the scalar diagonal/uniform-weight projection and \(\delta F_g^{\mathrm{cross}}\) records the ordered multi-channel information lost by averaging. At chain level the curved fiberwise differential satisfies \(m_1^2=[m_0,-]\), and the total modular differential is square-zero only after period correction.

### D5. Typed Theorem H

On the proved Koszul/generic surface:
\[
CH_{\mathrm{ch}}^n(A)=0\qquad n\notin\{0,1,2\}.
\]
At critical level, logarithmic admissible quotients, nonsemisimple module categories, and non-Koszul \(W\)-families, this is not a theorem unless the relevant spectral sequence degeneracy and completion hypotheses are supplied.

## E. Rewrite policy

Do not remove ambition. Convert unsupported ambition into correctly typed theorem, conditional theorem, conjecture, evidence proposition, or comparison surface. Every major claim must answer:

1. What is the object?
2. In which ambient category?
3. With which topology/completion?
4. Under which hypotheses?
5. Which functor proves it?
6. Which equality is literal and which is a shadow/projection?
7. What is the physical interpretation, if any?
8. What remains open?
