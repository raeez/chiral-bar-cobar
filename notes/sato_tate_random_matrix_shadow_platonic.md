# Sato-Tate via Shadow Tower and Symmetric-Power R-Matrices: First-Principles Audit

An honest first-principles attack on Sato-Tate for elliptic curves over $\mathbb{Q}$
(Taylor-Barnet-Lamb-Geraghty-Harris 2008; Clozel-Harris-Taylor 2008; Barnet-Lamb-Geraghty-Harris-Taylor 2011)
using the programme's symmetric-power chiral-algebra + shadow-tower machinery. Complementary
to `bsd_conjecture_cy_a2_elliptic_platonic.md` (which audited the $L(E,s)$ side of the same
$\Phi(E) = V_{L_E}$ construction) and to `riemann_hypothesis_random_matrix_rz_platonic.md`
(which audited GUE statistics of $R(z)$ eigenvalues). The Sato-Tate question sits at the
intersection: equidistribution of normalised Frobenius traces $a_p(E)/(2\sqrt{p}) \in [-1,1]$
against the Sato-Tate measure $(2/\pi)\sqrt{1-x^2}\,dx$ (equivalently $(2/\pi)\sin^2\theta\,d\theta$
under $x = \cos\theta$).

The Sato-Tate theorem for non-CM $E/\mathbb{Q}$ is proved via symmetric-power automorphy:
$\mathrm{Sym}^n \rho_{E,\ell}$ is automorphic for all $n \geq 1$ by Newton-Thorne 2021 extending
Clozel-Harris-Taylor; equidistribution then follows by a Weyl-type theorem from non-vanishing
of $L(s, \mathrm{Sym}^n f_E)$ on $\mathrm{Re}(s) = 1$.

## 0. Coordinates

For $E/\mathbb{Q}$ non-CM, $a_p = p + 1 - \#E(\mathbb{F}_p)$ satisfies $|a_p| \leq 2\sqrt{p}$
(Hasse). Write $a_p = 2\sqrt{p}\cos\theta_p$, $\theta_p \in [0,\pi]$. Sato-Tate: as
$p \to \infty$ through primes, $\theta_p$ is equidistributed according to
$\mu_{\mathrm{ST}} := (2/\pi)\sin^2\theta\,d\theta$. The programme's derived chiral centre
$Z^{\mathrm{der}}_{\mathrm{ch}}(\Phi(E))$ and shadow tower $\{S_r(\Phi(E))\}_{r\geq 2}$ are
already related to symmetric powers via
`prop:shadow-symmetric-power` (`arithmetic_shadows.tex:7637`):
$$
S_r \;\propto\; \sum_p p^{-rs}\,\mathrm{tr}\!\bigl(\mathrm{Sym}^{r-1}\mathrm{diag}(\alpha_p,\beta_p)\bigr)
\;=\; \sum_p p^{-rs}\,\sum_{j=0}^{r-1} \alpha_p^j\beta_p^{r-1-j}
$$
— the Dirichlet coefficients of $(\log L(s, \mathrm{Sym}^{r-1}f))'$.

## 1. Symmetric-power chiral algebra: Hilbert series of $\mathrm{Sym}^n V_k(\mathfrak{sl}_2)$

### 1.1 Construction
At admissible level $k = -2 + p/q$, the simple quotient $L_k(\mathfrak{sl}_2)$ is $C_2$-cofinite
(Arakawa) with finitely many simple modules $\{L_k(\lambda_i)\}$. The n-th fusion symmetric
power $\mathrm{Sym}^n_{\mathrm{fus}} L_k(\mathfrak{sl}_2)$ is the $S_n$-invariant subspace of
the $n$-fold fusion tensor product, equipped with the naive (bosonic) $S_n$-grading on
weight spaces.

**Hilbert series.** Writing $\chi_{k}(q,z) := \mathrm{ch}\,L_k(\mathfrak{sl}_2) = \sum_{\lambda} c_\lambda(q)\,z^\lambda$,
the symmetric-power character is
$$
\chi_{\mathrm{Sym}^n L_k}(q,z) \;=\; \mathrm{PE}_n[\chi_k(q,z)] \;=\; \bigl[\exp\bigl(\textstyle\sum_{m\geq 1}\tfrac{1}{m}\chi_k(q^m, z^m)\bigr)\bigr]_{\deg = n}
$$
(plethystic exponential truncated at total degree $n$). At admissible level the inner
sum is a finite Kac-Wakimoto combination; the generating function
$H_k(q,z,t) := \sum_{n \geq 0} t^n \chi_{\mathrm{Sym}^n L_k}(q,z)$
satisfies $H_k = \prod_{\lambda,\,m\geq 0}(1 - t\, q^{\lambda+m} z^\lambda)^{-d_\lambda(q)}$
where $d_\lambda(q) = [z^\lambda]\chi_k(q,z)$ — a product of Heisenberg-Fock factors twisted
by Kac-Wakimoto module weights.

### 1.2 Does $n \to \infty$ give Sato-Tate?
**No, and the obstruction is explicit.** The measure one extracts from
$\chi_{\mathrm{Sym}^n L_k}$ in the $n \to \infty$ limit is the $\mathrm{SU}(2)$ Haar measure
on characters of the highest-weight representation — which IS the Sato-Tate measure
$(2/\pi)\sin^2\theta\,d\theta$ under the identification $z = e^{i\theta}$. Explicitly:
the Weyl integration formula on $\mathrm{SU}(2)$ gives
$$
\lim_{n \to \infty} \frac{1}{n+1}\sum_{j=0}^n \delta(\theta - \tfrac{\pi j}{n+1}) \;=\; \frac{2}{\pi}\sin^2\theta\,d\theta
$$
(density of Young-diagram spectra inside $\mathrm{SU}(2)$, standard Peter-Weyl fact).

However, this is NOT Sato-Tate for an elliptic curve. It is Sato-Tate for $\mathrm{SU}(2)$-Haar,
which is the statement "$\mathrm{SU}(2)$ eigenangles equidistribute by Haar measure" —
a tautological consequence of the group structure, independent of any arithmetic.
The non-trivial content of Sato-Tate is that $\theta_p(E)$ — a sequence of arithmetic
points indexed by primes — equidistributes by $\mu_{\mathrm{ST}}$. The programme's
$\mathrm{Sym}^n L_k(\mathfrak{sl}_2)$ gives the MEASURE $\mu_{\mathrm{ST}}$ as a Haar
calculation, but does NOT supply the input sequence $\{\theta_p(E)\}$: the VOA has no
prime-indexed family, only a level-indexed family $\{L_k\}_{k \in \mathrm{Adm}}$.

**Verdict on item (1).** The $\mathrm{Sym}^n$ chiral-algebra limit produces the Sato-Tate
measure as a Haar measure on $\mathrm{SU}(2)$; this is structural knowledge independent of
the programme, stated at VOA level cleanly, without new content.

## 2. Programme-internal Sato-Tate reformulation

### 2.1 The shadow-tower equivalence
For $\Phi(E) = V_{L_E}$ with $L_E = H^1(E,\mathbb{Z})$ cup-product lattice (per BSD note §1.1),
the weight-$r$ bar component $V_\ell(B_r(\Phi(E)))$ carries a $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$-action
inherited from $\rho_{E,\ell}$. At each good prime $p \nmid N$, Frobenius $\mathrm{Frob}_p$ acts
on the rank-$(r+1)$ symmetric-power component $\mathrm{Sym}^{r-1}(T_\ell E)$ inside $B_r$ with
eigenvalues $\{\alpha_p^j \beta_p^{r-1-j}\}_{j=0}^{r-1}$.

By `prop:shadow-symmetric-power`, the shadow coefficient $S_r(\Phi(E))$ — a rational
number intrinsically attached to the bar complex of $\Phi(E)$ — is the $r$-th power
sum $p_r(\alpha_p,\beta_p)$ summed over primes, weighted as a Dirichlet series
$\sum_p p^{-rs}\cdot p_r(\alpha_p,\beta_p)$.

### 2.2 Reformulation
**Claim.** Equidistribution of $\theta_p(E)$ according to $\mu_{\mathrm{ST}}$ is equivalent to:
for each $r \geq 1$, the Dirichlet series
$$
L(s,\mathrm{Sym}^r f_E) \;=\; \exp\!\Bigl(\sum_{p,\,m\geq 1} \tfrac{1}{m}\,p^{-ms}\,\mathrm{tr}(\mathrm{Sym}^r \mathrm{Frob}_p^m)\Bigr)
$$
is holomorphic and non-vanishing on $\mathrm{Re}(s) = 1$. This is the Serre reduction
(`rem:serre-reduction`, `arithmetic_shadows.tex:7677`): non-vanishing + analytic continuation
of $L(s, \mathrm{Sym}^r f_E)$ for all $r \geq 1$ implies $|\alpha_p| = |\beta_p| = p^{1/2}$
(Hasse, already known) AND equidistribution of $\theta_p$ by $\mu_{\mathrm{ST}}$ (Sato-Tate)
via a standard Weyl-type theorem (see Serre, *Abelian* $\ell$-*adic representations* 1968,
I-25 for this reduction).

The shadow tower $\{S_r(\Phi(E))\}_{r\geq 2}$ generates — via Proposition 7637
($S_r \propto$ Dirichlet coefficient of $(\log L(s,\mathrm{Sym}^{r-1}f_E))'$) — the algebraic
(Dirichlet-coefficient-level) data of $\{L(s,\mathrm{Sym}^r f_E)\}_{r \geq 1}$.

**Therefore.** Sato-Tate for $E$ is equivalent to the chain
$$
\{S_r(\Phi(E))\}_{r\geq 2} \;\xrightarrow{\text{analytic cont.}}\; \{L(s,\mathrm{Sym}^r f_E)\}_{r\geq 1}
\;\xrightarrow{\text{non-vanish on Re}(s)=1}\; \mu_{\mathrm{ST}}.
$$
The first arrow is Newton-Thorne 2021 (automorphy of $\mathrm{Sym}^n$ for holomorphic
cuspidal eigenforms of regular algebraic weight, all $n$); the second is classical from
automorphy. **The shadow tower encodes all $\mathrm{Sym}^r$ Dirichlet coefficients
algebraically; Newton-Thorne supplies analytic continuation; Sato-Tate follows.**

### 2.3 Does the programme prove Sato-Tate independently?
**No.** Newton-Thorne is the load-bearing analytic input and sits OUTSIDE the programme.
`rem:escalation-circularity` (`arithmetic_shadows.tex:6476`) explicitly records that the
programme's algebraic shadow tower reaches $\mathrm{Sym}^{r-1}$ Dirichlet coefficients but
"the gap is the middle arrow: MC constraints give polynomial relations on symmetric power
traces (Newton's identities), but polynomial relations on Dirichlet coefficients do not
imply analytic continuation of the Dirichlet series." The programme bundles Hasse +
Newton-Thorne + Serre into a clean shadow-tower reformulation; it does not replace any link.

**Verdict on item (2).** Sato-Tate is EQUIVALENT to a shadow-tower-level statement
(algebraic part) + Newton-Thorne automorphy (analytic part). The programme contributes the
algebraic reformulation; the analytic closure is inherited. Reformulation, not solution.

## 3. Higher rank: K3/$\mathbb{Q}$ and Sato-Tate for $H^2$

### 3.1 Setup
Let $X/\mathbb{Q}$ be a K3 surface with Picard rank $\rho$. The transcendental lattice
$T(X) \subset H^2(X_{\overline{\mathbb{Q}}},\mathbb{Z}_\ell)$ has rank $22 - \rho$ and carries
a Galois action $\rho_{X,\ell}: \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to \mathrm{O}(T(X))$
landing in an orthogonal group. For a K3 with $\rho = 20$ (singular K3), $T(X)$ has rank 2
and $\rho_{X,\ell}$ factors through the Galois group of a CM number field (Shimura, Shioda-Inose).
For generic $\rho = 1$, $T(X)$ has rank 21 and $\rho_{X,\ell}$ is "big" (image Zariski-dense
in $\mathrm{O}(21)$); conjecturally semisimple, Hodge-style.

**Programme construction.** The CY-A functor at $d = 2$ gives $\Phi(X) = V_{H_{\mathrm{Muk}}}$,
a lattice VOA on the Mukai lattice $H_{\mathrm{Muk}}(X,\mathbb{Z}) = H^0 \oplus H^2 \oplus H^4$
of rank 24, signature $(4, 20)$ (`arithmetic_shadows.tex` and Vol III CY-A Theorem).
$\kappa_{\mathrm{ch}}(\Phi(X)) = \chi(\mathcal{O}_X) = 2$ for K3 (AP-CY34 specialized at $d=2$,
$h^{1,0}=0$).

### 3.2 Sato-Tate for K3
**Equidistribution prediction.** Normalised Frobenius eigenvalues on $T(X)$: for generic
K3/$\mathbb{Q}$ with $\rho = 1$, the 21-dimensional $\mathrm{Frob}_p$ acts on $T(X) \otimes \mathbb{Q}_\ell$
with eigenvalues on a circle of radius $p$ (Deligne's Weil II bound, $|\alpha| = p^{1}$
since $H^2$ is pure of weight 2). Normalised eigenvalues $\alpha_p/p \in S^1$. Generalised
Sato-Tate for orthogonal Galois reps (Katz-Sarnak 1999) predicts equidistribution according
to the Haar measure on the image Lie group; for generic K3, this is
$\mu_{\mathrm{Haar}}^{\mathrm{SO}(21)}$.

**Programme-internal reformulation.** By analogy with §2.2, equidistribution of normalised
eigenvalues of $\mathrm{Frob}_p$ on $T(X)$ according to $\mu_{\mathrm{Haar}}^{\mathrm{SO}(21)}$
is equivalent to non-vanishing + analytic continuation of $L(s, \mathrm{Sym}^r \rho_{X,\ell})$
for all $r \geq 1$, where $\mathrm{Sym}^r$ now lives in representations of $\mathrm{SO}(21)$.

The shadow tower of $\Phi(X) = V_{H_{\mathrm{Muk}}(X)}$ is computed in
`arithmetic_shadows.tex:3158` for general lattice VOAs: Hecke eigenvalues of the lattice
theta series of $H_{\mathrm{Muk}}(X)$ enter at each prime, and via
`prop:shadow-symmetric-power` these map to $\mathrm{Sym}^r$-power Dirichlet coefficients
for the attached Galois representation.

**The obstruction at $d = 2$.** Newton-Thorne 2021 is stated for $\mathrm{GL}_2$ (holomorphic
modular forms, i.e. 2-dimensional Galois reps). For a 21-dimensional (or 22-$\rho$)
orthogonal Galois rep attached to K3, the analogous $\mathrm{Sym}^r$-automorphy is the
generalised Langlands functoriality conjecture $\mathrm{SO}(21) \to \mathrm{GL}(\binom{21+r}{r})$
— UNKNOWN even at $r = 2$ for generic K3. For singular K3 (CM K3), the Galois rep factors
through an abelian Galois group; $\mathrm{Sym}^r$-automorphy follows from Hecke character theory
(class field theory). Sato-Tate for CM K3 is consequently a theorem (CM version of Sato-Tate,
following same proof template); Sato-Tate for generic K3 is conjectural. The programme
inherits this status exactly: reformulates, does not close.

### 3.3 The K3 case matches the BSD case as pattern
For the two $d \leq 2$ cases (elliptic, K3), the programme provides:
- Explicit chiral algebra $\Phi(X) = V_{L_X}$ with Galois-equivariant structure.
- Identification of shadow coefficients $S_r$ with $\mathrm{Sym}^{r-1}$-Dirichlet data.
- Clean reduction of Sato-Tate to symmetric-power automorphy + non-vanishing.

The programme does NOT provide:
- Analytic continuation of $L(s, \mathrm{Sym}^r \rho_{X,\ell})$ for $r$ large (Newton-Thorne
  stops at $\mathrm{GL}_2$; higher-rank cases are Langlands functoriality opens).
- Non-vanishing on $\mathrm{Re}(s) = 1$ independent of automorphy.

## 4. Verdict

**Programme-internal statement (proved):** Sato-Tate for $E/\mathbb{Q}$ non-CM is equivalent
to the conjunction of:
(a) the shadow-tower-level statement $\{S_r(\Phi(E))\}_{r \geq 2}$ generating
    $\{$Dirichlet coefficients of $L(s,\mathrm{Sym}^{r-1} f_E)\}_{r\geq 2}$ for all $r$
    (provided by `prop:shadow-symmetric-power` + lattice VOA theta decomposition);
(b) Newton-Thorne symmetric-power automorphy (external input, 2021);
(c) classical non-vanishing on $\mathrm{Re}(s) = 1$ for automorphic $L$-functions (Jacquet-Shalika).

**Programme-internal statement (conjectural, K3):** Sato-Tate for generic K3/$\mathbb{Q}$ is
equivalent to the conjunction of:
(a') shadow tower of $\Phi(X) = V_{H_{\mathrm{Muk}}(X)}$ generating
     $\{\mathrm{Sym}^r \rho_{X,\ell}$-Dirichlet coefficients$\}_{r \geq 1}$;
(b') Langlands functoriality $\mathrm{SO}(22-\rho) \to \mathrm{GL}_N$ (UNKNOWN for generic K3);
(c') non-vanishing for the resulting higher-rank $L$-functions.

**Honest position.** The programme is a reformulation-not-solution:
- Elliptic curves: Taylor et al. 2008 + Newton-Thorne 2021 close Sato-Tate; the programme's
  shadow-tower reformulation is a cleanup that packages Serre's reduction inside bar-cobar language.
- K3/$\mathbb{Q}$: programme gives the analogous reformulation as far as the structure of
  shadow coefficients allows; the analytic input is an UNPROVEN case of Langlands
  functoriality, so the programme shifts the difficulty from "prove Sato-Tate for K3" to
  "prove $\mathrm{Sym}^r$-automorphy for the Galois rep attached to $T(X)$."

**What the programme genuinely contributes:**
1. A clean statement that every Sato-Tate-type equidistribution at CY dimension $d$ is
   controlled by the shadow tower $\{S_r(\Phi(X))\}$ of the lattice VOA $\Phi(X) = V_{L_X}$.
2. A functorial organising principle: symmetric-power Galois reps are the bar-spectral
   weight-$r$ pieces of $B(\Phi(X))$ (not a new identification, but a systematic one).
3. A precise articulation of the obstruction: the algebraic shadow tower ALWAYS exists
   and is computable (by Kac-Wakimoto fusion, Borcherds theta, etc.); the analytic closure
   ALWAYS depends on Langlands functoriality at the relevant rank.

**What the programme does not contribute:**
- No independent proof of $\mathrm{Sym}^r$-automorphy at any rank.
- No new tool for non-vanishing on $\mathrm{Re}(s) = 1$.
- No random-matrix statistical content: as shown in `riemann_hypothesis_random_matrix_rz_platonic.md`,
  $R(z)$ eigenvalues are algebraic and do not produce Wigner-Dyson statistics; the
  Sato-Tate measure here arises via Peter-Weyl Haar, not any statistical limit of $R(z)$.

Bottom line: Sato-Tate is reformulation-not-solution through the programme. The elliptic
case is a theorem (TBLGHNT + NT), and the programme's contribution there is a structural
restatement. The K3 and higher-rank cases reduce to $\mathrm{Sym}^r$-automorphy for
higher-dimensional Galois reps — a Langlands-functoriality open. The three obstructions
from the BSD and RH notes — (a) inherited analytic content, (b) Galois-twisted vs
Galois-invariant mismatch, (c) topological vs arithmetic gap — all reappear here in the
expected shape.

## Literature anchors
- Taylor R. 2008 "Automorphy for some $\ell$-adic lifts of automorphic mod $\ell$ Galois representations II."
- Clozel-Harris-Taylor 2008 *Pub. Math. IHES* (companion to Taylor 2008).
- Barnet-Lamb, Geraghty, Harris, Taylor 2011 *Publ. RIMS* "A family of Calabi-Yau varieties
  and potential automorphy II" (Sato-Tate for non-CM elliptic curves over totally real fields).
- Newton-Thorne 2021 "Symmetric power functoriality for holomorphic modular forms" I/II,
  *Pub. Math. IHES* 134.
- Serre J.-P. 1968 *Abelian $\ell$-adic representations and elliptic curves*, I-25 (reduction
  of equidistribution to non-vanishing of all $\mathrm{Sym}^n L$-functions).
- Katz-Sarnak 1999 *Random Matrices, Frobenius Eigenvalues, and Monodromy* AMS.
- Harris-Shepherd-Barron-Taylor 2010 "A family of Calabi-Yau varieties and potential automorphy."
- Tate 1966 "Endomorphisms of abelian varieties over finite fields" *Invent. Math.*

## Cross-references
- `prop:shadow-symmetric-power` (`arithmetic_shadows.tex:7637`): $S_r \propto \mathrm{tr}(\mathrm{Sym}^{r-1}\cdot)$
  Dirichlet sums over primes.
- `rem:serre-reduction` (`arithmetic_shadows.tex:7677`): explicit chain MC $\Rightarrow$
  $\mathrm{Sym}^r$-data $\Rightarrow$ Ramanujan/Sato-Tate; middle arrow is the open one.
- `rem:escalation-circularity` (`arithmetic_shadows.tex:6476`): Newton-Thorne closes the
  circularity for holomorphic forms; Maass case (Kim-Sarnak $\theta \leq 7/64$) remains.
- `notes/bsd_conjecture_cy_a2_elliptic_platonic.md`: $\Phi(E) = V_{L_E}$ construction at $d=1$.
- `notes/riemann_hypothesis_random_matrix_rz_platonic.md`: $R(z)$ is algebraic, not GUE;
  reinforces that Sato-Tate measure here is Haar-from-group-structure, not RMT-from-statistics.
- Vol III AP-CY34/AP-CY44: $\kappa_{\mathrm{ch}}(X) = \chi(\mathcal{O}_X)$ for CY$_2$ with
  $h^{1,0}=0$; fixes $\kappa_{\mathrm{ch}}(K3) = 2$.
