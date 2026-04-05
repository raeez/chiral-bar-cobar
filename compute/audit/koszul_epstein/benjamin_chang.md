# Benjamin-Chang L-functions for Vertex Algebras vs. the Koszul-Epstein Construction

## Date: 2026-04-01
## Status: Research audit
## Sources: arXiv:2208.02259 (Benjamin-Chang 2022), rn96/rn101/rn102/rn105/rn106/rn111/rn112, arithmetic_shadows.tex

---

## 1. What Benjamin-Chang Construct

**Paper**: N. Benjamin and C.-H. Chang, *Scalar modular bootstrap and zeros of the Riemann zeta function*, arXiv:2208.02259 (2022). Cited as `\bibitem{BenjaminChang22}` in `bibliography/references.tex`.

**2025 extension**: Benjamin-Chang-Fitzpatrick-Ramella extended the analysis to scalar primaries of arbitrary 2d CFTs (not just Narain/U(1)^c). This later paper is NOT currently in references.tex.

### The construction (answer to Question 1: option (a), the constrained Epstein zeta from the primary spectrum)

Benjamin-Chang define the **constrained Epstein series**:

$$
\varepsilon^c_s(\mu) = E^c_s(\mu) := \sum_{\Delta \in S} (2\Delta)^{-s}
$$

where $S$ is the multiset of non-vacuum **scalar primary dimensions** of a 2d CFT at central charge $c$, with multiplicity.

This is *not* a Rankin-Selberg L-function from VOA characters (option (b)). It is a Dirichlet series built directly from the scalar primary spectrum. The construction is:

1. Start with the partition function $Z(\tau, \bar\tau)$ of a modular-invariant 2d CFT.
2. Form the primary-counting function $\hat{Z}^c(\tau) = y^{c/2} |\eta(\tau)|^{2c} Z(\tau, \bar\tau)$.
3. Decompose $\hat{Z}^c$ spectrally on $\mathrm{SL}(2,\mathbb{Z}) \backslash \mathbb{H}$ via Roelcke-Selberg:

$$
\hat{Z}^c = E_{c/2} + (\text{const}) \cdot \varepsilon^c_{c/2-1} + \frac{1}{4\pi i} \int_{1/2 - i\infty}^{1/2 + i\infty} \pi^{s-c/2} \Gamma(c/2 - s) \, \varepsilon^c_{c/2-s} \, E_s(\tau) \, ds + (\text{Maass})
$$

4. The Eisenstein spectral coefficient of $\hat{Z}^c$ IS the constrained Epstein series $\varepsilon^c_s$.

### The functional equation

Benjamin-Chang prove that $\varepsilon^c_s$ satisfies:

$$
\varepsilon^c_{c/2 - s} = F_c(s) \cdot \varepsilon^c_{c/2 + s - 1}
$$

where

$$
F_c(s) = \frac{\Gamma(s) \, \Gamma(s + c/2 - 1) \, \zeta(2s)}{\pi^{2s-1/2} \, \Gamma(c/2 - s) \, \Gamma(s - 1/2) \, \zeta(2s - 1)}
$$

The factor $\zeta(2s)/\zeta(2s-1)$ is the decisive feature: contour deformation picks up residues at $s = (1 + \rho_n)/2$ where $\rho_n$ are the nontrivial zeros of $\zeta(s)$ (from $\zeta(2s-1) = 0$).

### The pole structure (contour-shift poles)

Three families of poles appear:

1. **$s = c/2$** -- from $\Gamma(c/2 - s)$ in the denominator
2. **$s = (1 + \rho_n)/2$** -- from $\zeta(2s - 1) = 0$ in the denominator (nontrivial zeta zeros)
3. **$s = (1 + \bar{\rho}_n)/2$** -- conjugate zeros

The coefficients $\epsilon_c(\mu)$ and $\delta_{k,c}(\mu)$ at these poles are integrals over the modular fundamental domain against residues of Eisenstein series. The pole LOCATIONS are universal (same for every CFT); the AMPLITUDES are CFT-specific.

---

## 2. The Shadow Tower's Epstein Zeta: Two Distinct Objects

The monograph defines TWO different "Epstein-type" zeta functions. They are **different objects** with different inputs, different analytic properties, and different arithmetic content.

### Object A: The constrained Epstein zeta $\varepsilon^c_s(A)$ (Benjamin-Chang)

- **Input**: The scalar primary spectrum $\{(\Delta_i, m_i)\}$ of the CFT.
- **Definition**: $\varepsilon^c_s = \sum_{\Delta \in S} (2\Delta)^{-s}$.
- **Source of functional equation**: Modular invariance of the partition function on $\mathcal{M}_{1,1}$.
- **Pole structure**: Poles at $s = c/2$ and at $(1 + \rho_n)/2$.
- **Lattice case**: For lattice VOA $V_\Lambda$ of rank $r$ with $\Theta_\Lambda = c_E E_{r/2} + \sum_j c_j f_j$:

$$
\varepsilon^r_s(V_\Lambda) = 2^{-s} \bigl( c_E \cdot C_E(s) \cdot \zeta(s) \cdot \zeta(s - r/2 + 1) + \sum_j c_j \cdot C_j(s) \cdot L(s, f_j) \bigr)
$$

- **Manuscript location**: `arithmetic_shadows.tex`, eq:constrained-epstein-fe (line ~3041), thm:narain-universality, thm:shadow-spectral-correspondence.

### Object B: The shadow-metric Epstein zeta $\varepsilon_{Q_L}(s)$ (Koszul-Epstein)

- **Input**: The shadow metric $Q_L(m,n) = 4\kappa^2 m^2 + 12\kappa\alpha \, mn + (9\alpha^2 + 2\Delta) n^2$, a binary quadratic form built from THREE OPE invariants $(\kappa, \alpha, S_4)$.
- **Definition**: $\varepsilon_{Q_L}(s) = \sum'_{(m,n) \in \mathbb{Z}^2} Q_L(m,n)^{-s}$ (classical Epstein zeta of a quadratic form).
- **Source of functional equation**: Poisson summation (Epstein 1903): $\Lambda_{Q_L}(s) = \Lambda_{Q_L}(1-s)$ where $\Lambda_{Q_L}(s) = (|D|/4)^{s/2} \pi^{-s} \Gamma(s) \varepsilon_{Q_L}(s)$.
- **Pole structure**: Single simple pole at $s = 1$.
- **Arithmetic content**: When disc$(Q_L) = -32\kappa^2 \Delta$ is a fundamental discriminant, the Epstein zeta factors through the Dedekind zeta of the shadow field $K_L = \mathbb{Q}(\sqrt{\text{disc}(Q_L)})$, and then through Dirichlet L-functions via $\zeta_{K_L}(s) = \zeta(s) \cdot L(s, \chi_d)$.
- **Manuscript location**: `arithmetic_shadows.tex`, constr:shadow-l-function (line ~2699), `compute/lib/shadow_epstein_zeta.py`.

### Object C: The shadow Epstein zeta $Z_{\mathrm{sh}}(s, c)$

- **Input**: The shadow obstruction tower coefficients $S_r(c)$.
- **Definition**: $Z_{\mathrm{sh}}(s, c) = \sum_{r \geq 2} |S_r(c)|^2 r^{-s}$.
- **Source**: A Dirichlet series in the shadow coefficients themselves (not the primary spectrum).
- **Properties**: At $c = 13$ (self-dual point), has trivial functional equation under $c \to 26 - c$.
- **Manuscript location**: `arithmetic_shadows.tex`, constr:shadow-epstein-eisenstein (line ~1884).

### Summary of relationships

| Property | $\varepsilon^c_s$ (Benjamin-Chang) | $\varepsilon_{Q_L}$ (shadow metric) | $Z_{\mathrm{sh}}$ (shadow obstruction tower) |
|---|---|---|---|
| Input | Primary spectrum $\{\Delta_i\}$ | OPE invariants $(\kappa, \alpha, S_4)$ | Shadow coefficients $S_r$ |
| Summation variable | Primary dimensions | Lattice points in $\mathbb{Z}^2$ | Arity index $r$ |
| Functional equation center | $s = c/4$ (roughly) | $s = 1/2$ | (under $c \to 26-c$ at $c=13$) |
| Pole at | $s = c/2$, $(1+\rho_n)/2$ | $s = 1$ | (convergence domain) |
| Arithmetic content | Full L-function package | Dirichlet L-functions via $K_L$ | Shadow growth rate |

**These are NOT the same object.** They live at different levels:

- $\varepsilon^c_s$ is the analytic/spectral object: it encodes the full primary spectrum and couples to the scattering resonances of $\mathcal{M}_{1,1}$.
- $\varepsilon_{Q_L}$ is the algebraic/deformation-theoretic object: it encodes three OPE invariants (the scalar shadow $\kappa$, the cubic shadow $\alpha$, and the quartic contact $S_4$) packaged into a binary quadratic form.
- $Z_{\mathrm{sh}}$ is the combinatorial object: it encodes the full shadow obstruction tower.

The relationship is through a CHAIN OF PROJECTIONS:

$$
\text{Full CFT data} \xrightarrow{\text{primary spectrum}} \varepsilon^c_s \xrightarrow{\text{low moments}} \varepsilon_{Q_L} \xrightarrow{\text{Taylor coefficients}} Z_{\mathrm{sh}}
$$

The shadow-metric Epstein $\varepsilon_{Q_L}$ captures the QUADRATIC PART of the deformation-theoretic data (arity $\leq 4$). It is NOT the full spectral object. For lattice VOAs, the two objects are related by the shadow-spectral correspondence (thm:shadow-spectral-correspondence): the shadow depth counts the number of independent L-functions in $\varepsilon^c_s$. For non-lattice VOAs, the algebraic complexity (shadow depth) may EXCEED the spectral complexity (critical line count) -- see `compute/lib/betagamma_epstein.py` for the beta-gamma counterexample.

---

## 3. The Pole at $s = c/2$ and Its Connection to $\kappa$

### The claim to verify

From rn105: "the scalar crossing contour picks up poles at $s = c/2$". Is this pole at $s = c/2 = \kappa$ (the modular characteristic)?

### Analysis

For the Virasoro algebra at central charge $c$: $\kappa(\text{Vir}_c) = c/2$.

The constrained Epstein series $\varepsilon^c_s$ has a contour-shift pole at $s = c/2$. This comes from the $\Gamma(c/2 - s)$ factor in the denominator of $F_c(s)$: as $s \to c/2$, this gamma factor has a simple pole.

**Therefore: the first pole of the constrained Epstein functional equation IS at $s = \kappa$ for Virasoro.**

However, this identification requires careful qualification:

1. **For Virasoro**: $\kappa = c/2$, and the pole is at $s = c/2$. So $s_{\text{pole}} = \kappa$. This is an exact identification.

2. **For affine Kac-Moody** at level $k$: $\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee) / (2h^\vee)$, while $c = k \cdot \dim(\mathfrak{g}) / (k + h^\vee)$. The pole is at $s = c/2 = k \cdot \dim(\mathfrak{g}) / (2(k + h^\vee))$. Meanwhile $\kappa = \dim(\mathfrak{g}) \cdot (k + h^\vee) / (2h^\vee)$. These are NOT equal in general: $c/2 \neq \kappa$ for affine KM (they coincide only when $h^\vee = 1$, i.e., for abelian Lie algebras).

3. **The universal statement**: The constrained Epstein pole is at $s = c/2$ (half the central charge), NOT at $s = \kappa$ (the modular characteristic) in general. For Virasoro, $\kappa = c/2$ is an accidental coincidence. For affine KM, $\kappa \neq c/2$.

**Verdict**: The pole at $s = c/2$ connects to $\kappa$ ONLY for the Virasoro algebra, where $\kappa = c/2$ by definition. This is NOT a universal connection between modular characteristics and L-function poles. The pole is intrinsic to the Eisenstein spectral parameter (it comes from $\Gamma(c/2 - s)$, which depends on $c$, not $\kappa$). Making the identification $s = c/2 = \kappa$ for general algebras would be an AP1-type error (copying a formula between families without recomputation).

---

## 4. Comparison Theorem: $\varepsilon_{Q_L}(s)$ vs $E^c_s$ (Benjamin-Chang)

### Are they the same object?

**No.** They are fundamentally different objects at different levels of the theory.

### How they relate

The relationship is:

1. **$\varepsilon^c_s$** (Benjamin-Chang) is a Dirichlet series over the PRIMARY SPECTRUM of the CFT. It is an infinite series in the conformal dimensions $\Delta_i$ of scalar primaries.

2. **$\varepsilon_{Q_L}(s)$** (shadow metric) is a lattice sum over $\mathbb{Z}^2$, determined by exactly three OPE invariants $(\kappa, \alpha, S_4)$. It is a FINITE-PARAMETER object encoding the arity $\leq 4$ shadow data.

3. The shadow metric $Q_L$ is extracted from the MC equation's arity-4 projection. It captures the QUADRATIC APPROXIMATION to the deformation-theoretic content of the chiral algebra.

### Which is the "right" object?

**Both are "right" for different purposes.**

- For **spectral analysis and zeta-zero connections**: $\varepsilon^c_s$ (Benjamin-Chang) is the correct object. It is the Eisenstein spectral coefficient of the actual partition function, and its functional equation is where zeta zeros appear.

- For **algebraic/deformation-theoretic purposes**: $\varepsilon_{Q_L}$ (shadow metric) is the correct object. It captures the structure of the MC equation at finite arity and connects to the arithmetic of imaginary quadratic fields through the discriminant.

- For **the full Koszul-duality programme**: neither is the final object. The rn105 analysis (which survived the Beilinson pass) concludes that the right comparison requires a MIXED $(s,u)$-transform combining:
  - the $s$-variable from Rankin-Selberg/Eisenstein overlap ($\varepsilon^c_s$ side)
  - the $u$-variable from genus-one sewing/Dirichlet series ($\varepsilon_{Q_L}$ side)
  - the arity-4 shadow data (first nonlinear invariant)

### What has been proved

For **lattice VOAs**: the shadow-spectral correspondence (thm:shadow-spectral-correspondence) provides a precise comparison:

$$
\varepsilon^r_s(V_\Lambda) = 2^{-s} \bigl( c_E \, C_E(s) \, \zeta(s) \, \zeta(s - r/2 + 1) + \sum_j c_j \, C_j(s) \, L(s, f_j) \bigr)
$$

The shadow depth counts the number of independent L-functions: depth $d \to d-1$ critical lines. Verified for $V_{\mathbb{Z}}$ (1 line), $V_{E_8}$ (2 lines), $V_{\text{Leech}}$ (3 lines).

For **non-lattice theories**: the comparison is OPEN. The beta-gamma system provides a concrete warning: algebraic complexity (shadow depth 4) exceeds spectral complexity (1 critical line). The shadow-L correspondence requires a refined formulation for non-lattice algebras.

For **Virasoro at general $c$**: the genuine Virasoro constrained Epstein $\varepsilon^c_s(\text{Vir})$ requires the Virasoro primary spectrum at general $c$ (involving the representation theory of the Virasoro algebra at arbitrary central charge). This is a well-defined but INCOMPLETE computation.

### What has been dismissed (Beilinson pass, rn105)

Five false ideas were identified and dismissed:

1. **MC identities directly imply Li-type positivity.** FALSE: the theory-dependent coefficients are not sign-definite.
2. **Bar-cobar homotopy equivalence forces critical-line rigidity.** FALSE: bar-cobar gives deformation-theoretic transport, not arithmetic positivity.
3. **Narain variation gives zero-location leverage.** FALSE: varying $R$ changes only the positive character factor, not the zeta-zero locus.
4. **The $\zeta$-proxy is a decisive test.** FALSE: it excludes aggressively but does not preserve $\sigma = 1/2$ as a safe point.
5. **The quartic determinant is a single invariant.** FALSE: the potential-side Schur complement (quartic contact) and the Gram-side determinant (quartic resonance divisor) are distinct.

### The structural obstruction (rem:structural-obstruction in arithmetic_shadows.tex)

The shadow obstruction tower and MC equation constrain spectral coefficients $c(t)$ on the REAL spectral line ($s = 1/2 + it$, $t \in \mathbb{R}$). The zeta zeros live at COMPLEX spectral parameters. This separation is structural: algebraic constraints on the spectral line cannot reach the scattering poles without analytic continuation of the spectral data off the real axis. The completed scattering matrix $\varphi(s) = \Lambda(1-s)/\Lambda(s)$ has poles at $s = \rho/2$ (complex) and is regular for all real $t$.

---

## 5. Summary of Key Distinctions

| Aspect | Benjamin-Chang $\varepsilon^c_s$ | Shadow metric $\varepsilon_{Q_L}$ |
|---|---|---|
| **Nature** | Spectral/analytic | Algebraic/deformation-theoretic |
| **Input data** | Full primary spectrum (infinite) | Three OPE invariants (finite) |
| **Functional equation** | From modular invariance, involves $\zeta(2s)/\zeta(2s-1)$ | From Poisson summation, classical Epstein |
| **Zeta-zero connection** | Direct: poles at $(1+\rho_n)/2$ | Indirect: through discriminant and class field |
| **Koszul duality role** | Constrains amplitudes at poles (not pole locations) | Encodes deformation-theoretic data directly |
| **First pole** | $s = c/2$ (half central charge) | $s = 1$ (universal for binary forms) |
| **Arithmetic content** | Full L-function package of the partition function | Dirichlet L-functions of the shadow field $K_L$ |

The connection between the two is through the **shadow-spectral correspondence**: the shadow obstruction tower's arity-by-arity resolution of the partition function corresponds to the Hecke eigenform-by-eigenform decomposition of the constrained Epstein series. This is PROVED for lattice VOAs and CONJECTURAL in general.

---

## 6. Open Problems

1. **Non-lattice shadow-L correspondence**: Does shadow depth $\geq$ critical line count hold universally? Beta-gamma suggests inequality is strict.

2. **Genuine Virasoro Epstein**: Construct $\varepsilon^c_s(\text{Vir})$ from the Virasoro primary spectrum at general $c$, constrained by the MC shadow obstruction tower.

3. **Mixed $(s,u)$-transform**: Define the correct mixed transform combining spectral and sewing data at arity $\geq 4$.

4. **Analytic continuation off the spectral line**: Bridge the structural gap between real spectral constraints (from MC) and complex scattering poles (where zeta zeros live).

5. **Shadow principal class conjecture** (conj:shadow-principal-class): Does $Q_L$ always represent the principal ideal class in Cl($K_L$)? Already nontrivial at Ising ($c = 1/2$).

6. **Missing reference**: The 2025 Benjamin-Chang-Fitzpatrick-Ramella paper (extending to arbitrary 2d CFTs) is not in references.tex.
