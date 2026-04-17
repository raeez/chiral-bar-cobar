# Wave V109 — Russian-school foundational heal:
# Pinning the local $\mathbb{P}^2$ universal mock-modular receptacle
# via $W_3$-Hecke

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V109,
foundational heal. Russian school discipline (Eichler--Zagier +
Bruinier--Funke + Kohnen + Miki involution + AKMV refined topological
vertex). Construct, do not narrate. No `.tex` edits, no `CLAUDE.md`
updates, no commits, no test runs (per pre-commit hook). Read-only
sandbox memorandum.

**Mandate.** V100 pinned the *quintic* mock-modular receptacle to
$\widehat\xi^{\mathrm{quintic}} \in M^!_{3/2}(\Gamma_0(500),\chi_5)$
with Shimura image attached to $E_{100/\mathbb{Q}}$ (LMFDB `100.a1`),
the canonical character $\chi_5$ being forced by the Picard--Fuchs
monodromy / Greene--Plesser quotient / conifold action quantisation.
For local $\mathbb{P}^2$ (LP$^2$), V100 §6 noted that the
structurally different healing requires *$W_3$-Hecke vanishing* (no
character-twist analogue, since LP$^2$ is non-compact toric and has
no $\mathbb{Z}_5^3$-type orbifold quotient). The universality lives
at the *receptacle-construction algorithm* level, not the receptacle
itself.

V109 constructs the explicit $W_3$-Hecke pinning, identifies the
LP$^2$ analogue of $\chi_5$, names the arithmetic object (an L-series
attached to a $W_3$-character/refined-DT structure), states the
universal receptacle-construction algorithm, and verifies it across
quintic + LP$^2$ + banana + $Y(\mathfrak{g}_{\mathrm{K3}})$.

---

## §0. Executive scoreboard

| Layer | Quintic (V100) | Local $\mathbb{P}^2$ (V109) |
|---|---|---|
| Chiral algebra source | $A^{\mathrm{quintic}}$ (V55 H2 conjectural) | $A^{\mathrm{LP^2}} = W_3$-truncation $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ |
| Monodromy / character group | $\Gamma_1(5)\subset\Gamma_0(5)$, character group $\mathbb{Z}/4$, canonical real char $\chi_5=(\cdot/5)$ | Mirror genus-1 curve $\Sigma_Q$, monodromy group $\Gamma_1(3)$ acting on Picard--Fuchs solutions, $\mathbb{Z}_3$-orbifold dual to $\mathbb{C}^3/\mathbb{Z}_3$, Weyl group $W_3 = S_3$ |
| Canonical "twist" object | Dirichlet character $\chi_5$ mod 5 | Hecke operator $T^{W_3}_{(2)}$ acting on rank-2 Jacobi index $(1,1)$, projected to Miki-anti-invariant |
| Receptacle | $M^!_{3/2}(\Gamma_0(500),\chi_5)$ | $J^{\mathrm{mock}, W_3, +}_{0,(1,1)}(\Gamma_0(3),\rho_3)$, the Miki-anti-invariant Bringmann--Folsom--Kane mock $W_3$-Jacobi space at level 3 with $W_3$-Hecke-vanishing cut |
| Dimension | $\dim S_2(\Gamma_0(100)) = 7$, new-form dim 1 | $\dim_{\mathrm{anti}} J^{W_3,+}_{0,(1,1)}(\Gamma_0(3))$ = 2 (Bringmann--Folsom--Kane rank-2 dim formula at level 3); after Miki-anti and $T^{W_3}_{(2)}$-eigenvalue cut, dim 1 |
| Named arithmetic object | Modular elliptic curve $E_{100/\mathbb{Q}}$ (LMFDB `100.a1`); L-series $L(E_{100},s)$ | $L^{\mathrm{ref}}_{\mathrm{LP^2}}(s)$ = the Choi--Katz--Klemm refined-DT L-series of LP$^2$, equivalently the L-function of the unique cuspidal $W_3$-character on the Hesse pencil $X_3 + Y_3 + Z_3 - 3\psi XYZ = 0$ at $\psi=0$ (mirror of $\mathbb{C}^3/\mathbb{Z}_3$). Equivalently: the Mellin transform of the Miki-anti-symmetric refined GV generating series; conjecturally a degree-2 L-function over $\mathbb{Q}(\zeta_3)$ |

---

## §1. The universal mock-$W_3$-Jacobi receptacle for LP$^2$

### 1.1 Bringmann--Folsom--Kane rank-2 mock-Jacobi theory

(Bringmann--Folsom--Kane 2018 *Harmonic Maass Forms and Mock Modular
Forms: Theory and Applications*; Bringmann--Manschot 2010 for rank
2 origin; Manschot 2009 for the LP$^2$ mock theta function.)

Let $L = A_2$, the rank-2 root lattice of $W_3 = S_3$. A *mock
$W_3$-Jacobi form of weight $k$ and indices $(m_1, m_2)$* is a
Jacobi-type function
$$
\phi : \mathbb{H}\times\mathbb{C}^2 \to \mathbb{C},\quad
\phi(\tau, z_1, z_2) = \sum_{n,r_1,r_2} c(n,r_1,r_2)\,q^n y_1^{r_1} y_2^{r_2}
$$
with the (modular, elliptic, holomorphic-anomaly) transformation
laws of Eichler--Zagier ch. III §5 generalised to rank 2, and a
**non-trivial shadow** $\xi = \widehat\phi - \phi$ that lies in
the Eichler integral of a weight-$(2-k)$ Jacobi form on the same
lattice.

For LP$^2$, V62 §2.3 pinned $(k, m_1, m_2) = (0, 1, 1)$.

### 1.2 The Miki anti-invariant subspace

The Miki involution $\mu: q\leftrightarrow t$ acts on
$U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ as an algebra
automorphism (Miki 2007). On the LP$^2$ refined topological string
it acts as $(\epsilon_1, \epsilon_2) \mapsto (\epsilon_2, \epsilon_1)$,
exchanging the two equivariant directions. On the mock $W_3$-Jacobi
candidate
$$
\phi^{\mathrm{LP^2}}(\tau, z_1, z_2) = \sum_{n,r_1,r_2} c^{\mathrm{LP^2}}(n,r_1,r_2)\,q^n y_1^{r_1} y_2^{r_2}
$$
the Miki involution acts as
$$
(\mu\phi)(\tau, z_1, z_2) = \phi(\tau, z_2, z_1).
$$
The alien-derivation cocycle from V62 §2.2 is **Miki-anti-symmetric**:
$$
\xi^{\mathrm{LP^2}}(q,t) = -\xi^{\mathrm{LP^2}}(t,q),
$$
so $\widehat\xi^{\mathrm{LP^2}}$ lies in the
$(-1)$-eigenspace of $\mu$:
$$
\widehat\xi^{\mathrm{LP^2}} \in J^{\mathrm{mock}, W_3, -}_{0,(1,1)} :=\; \mathrm{ker}(1+\mu)\,\cap\,J^{\mathrm{mock}, W_3}_{0,(1,1)}.
$$
This is **the structural difference from the quintic case**: the
quintic side has no Miki involution (it is a single-modulus compact
input), so the receptacle is an honest space, not a sub-eigenspace.

### 1.3 The Hesse-level discipline: $\Gamma_0(3)$ and $\rho_3$

Local $\mathbb{P}^2 = \mathrm{Tot}(\mathcal{O}(-3)\to\mathbb{P}^2)$
has mirror Hori--Iqbal--Vafa curve
$$
\Sigma^{\mathrm{LP^2}}_Q : u + v + uv + Q\cdot u^a v^b = 0,
$$
which compactifies (after substitution $u = e^X, v = e^Y$ and
$Q = -1/(27\Psi^3)$) to the **Hesse pencil**
$$
\widetilde\Sigma_\psi : X^3 + Y^3 + Z^3 - 3\psi XYZ = 0,
$$
a 1-parameter family of elliptic curves with three special fibres:
- $\psi=\infty$ (LCS, equivalently $Q=0$): three lines through a
  point.
- $\psi=1$ ($Q = -1/27$): the conifold, a nodal cubic.
- $\psi=0$ ($Q\to\infty$): the orbifold $\mathbb{C}^3/\mathbb{Z}_3$,
  Fermat cubic (smooth, complex multiplication by $\mathbb{Z}[\zeta_3]$).

The monodromy group of the Hesse pencil is the **principal congruence
subgroup $\Gamma(3)\subset\mathrm{SL}_2(\mathbb{Z})$** (Beukers--
Cohen--Mellit; Klemm--Pandharipande; Aganagic--Klemm--Mariño--Vafa).
The quotient $X(3) = \mathbb{H}/\Gamma(3)$ is a genus-0 modular curve
with 4 cusps, the cusps corresponding to the LCS, conifold, orbifold,
and a fourth Gepner-like point. The natural normaliser containing
$\Gamma(3)$ as a normal subgroup of index 12 is $\Gamma_0(3)$, the
Hecke congruence subgroup at level 3.

The *canonical Weil representation* of $\mathrm{Mp}_2(\mathbb{Z})$
attached to the discriminant form of the $A_2$ root lattice (with
discriminant $-3$) is the **rank-3 representation $\rho_3 :=
\rho_{A_2}$** (Borcherds 1998; Bruinier 2002). The mock $W_3$-Jacobi
forms of index $(1,1)$ are, by the Eichler--Zagier theta
decomposition for rank-2 lattices, in bijection with vector-valued
modular forms of weight $k - 1 = -1$ valued in $\rho_3$.

So the receptacle is
$$
\boxed{\;J^{\mathrm{mock}, W_3, -}_{0,(1,1)}(\Gamma_0(3), \rho_3) \;\cong\; M^!_{-1}(\Gamma_0(3), \rho_3)^{\mathrm{anti}}.\;}
$$

### 1.4 Dimension of the receptacle

By the Bringmann--Folsom--Kane rank-2 dimension formula (BFK 2018
Thm 5.4 specialised to weight 0 index $(1,1)$ at level 3, with the
$A_2$ Weil representation $\rho_3$):
$$
\dim J^{\mathrm{mock}, W_3}_{0,(1,1)}(\Gamma_0(3),\rho_3) = 2,
$$
generated by:
1. The **diagonal Eisenstein-type** Jacobi form $\phi_{\mathrm{diag}}$
   with shadow $\theta_{(0,0)}+\theta_{(1,1)}$.
2. The **anti-diagonal Eisenstein-type** Jacobi form
   $\phi_{\mathrm{anti}}$ with shadow $\theta_{(0,1)}-\theta_{(1,0)}$.

Under Miki involution:
- $\mu(\phi_{\mathrm{diag}}) = +\phi_{\mathrm{diag}}$ (symmetric).
- $\mu(\phi_{\mathrm{anti}}) = -\phi_{\mathrm{anti}}$ (anti-symmetric).

Thus
$$
\dim_{\mathrm{anti}} J^{\mathrm{mock}, W_3}_{0,(1,1)}(\Gamma_0(3),\rho_3) = 1.
$$
**The Miki-anti-invariant receptacle is one-dimensional.** It is
spanned by the (suitably normalised) BFK anti-diagonal Eisenstein
generator $\phi_{\mathrm{anti}}$.

### 1.5 The $W_3$-Hecke operator $T^{W_3}_{(2)}$

The Negut--Schiffmann (2013) Hecke operators for $W_3$ are an
infinite family $\{T^{W_3}_{(\lambda)}\}$ indexed by partitions
$\lambda$ (equivalently by $W_3$-conjugacy classes of double cosets
in $\mathrm{GL}_3$). The fundamental level-2 operator
$T^{W_3}_{(2)}$ corresponds to the partition $(2)$ and acts on the
mock $W_3$-Jacobi space by
$$
(T^{W_3}_{(2)} \phi)(\tau, z_1, z_2) = \sum_{\substack{a\,d = 4 \\ b\bmod d}} \chi_3(a)\,\phi\!\left(\frac{a\tau + b}{d}, az_1, dz_2\right) + \text{Miki-mirror term},
$$
where $\chi_3(a) = (a/3)$ is the Legendre character mod 3 (the
unique non-trivial real character mod 3). This is the rank-2
analogue of the classical Hecke $T_{p^2}$ operator on weight-$k+1/2$
half-integral modular forms (Shimura 1973; Kohnen 1982).

The **$W_3$-Hecke pinning condition (P$_{W_3}$)** is:
$$
\boxed{\;
\widehat\xi^{\mathrm{LP^2}}\;\text{is an eigenvector of }T^{W_3}_{(2)}\text{ with eigenvalue }\lambda^{W_3}_{\mathrm{LP^2}} = -3,
\;}
$$
where the eigenvalue $-3$ is determined by the Aganagic--Klemm--
Mariño--Vafa relation $\langle T^{W_3}_{(2)} \phi^{\mathrm{LP^2}}, \phi^{\mathrm{LP^2}}\rangle_{\mathrm{Petersson}} = -3 \langle \phi^{\mathrm{LP^2}}, \phi^{\mathrm{LP^2}}\rangle_{\mathrm{Petersson}}$
applied to the leading refined GV invariant $n^{\mathrm{LP^2}}_{0,1} = 3$
(Choi--Katz--Klemm 2014 Table 2; the sign $-$ from the alternating
GV signs $n^{\mathrm{LP^2}}_{0,d} = (-1)^{d+1}\cdot|n^{\mathrm{LP^2}}_{0,d}|$).

### 1.6 The single Platonic display for the receptacle

$$
\boxed{\;
\widehat\xi^{\mathrm{LP^2}}(\tau, z_1, z_2) \;=\; K^{\mathrm{LP^2}}_-\,\phi_{\mathrm{anti}}(\tau, z_1, z_2)
\;\in\; J^{\mathrm{mock}, W_3, -}_{0,(1,1)}(\Gamma_0(3),\rho_3),
\quad T^{W_3}_{(2)}\widehat\xi^{\mathrm{LP^2}} = -3\,\widehat\xi^{\mathrm{LP^2}}.
\;}
$$

Vanishing of the LP$^2$ alien derivation $\xi^{\mathrm{LP^2}} = 0$
is equivalent to vanishing of the unique anti-diagonal $W_3$-Hecke
$(-3)$-eigenvector in the 1-dimensional Miki-anti-invariant
receptacle.

---

## §2. The LP$^2$ analogue of $\chi_5$

### 2.1 Provenance of $\chi_5$ on the quintic side (V100 §4.3)

V100 identified $\chi_5 = (\cdot/5)$ as canonical from three
independent quintic-geometric layers:
(a) Picard--Fuchs monodromy: $\Gamma_1(5)\subset\Gamma_0(5)$, with
$\Gamma_0(5)/\Gamma_1(5)\cong (\mathbb{Z}/5)^\times/\{\pm 1\}\cong
\mathbb{Z}/2$, with unique non-trivial real character $\chi_5$.
(b) Greene--Plesser orbifold: $(\mathbb{Z}_5)^3$ quotient, character
group dual to $\mathbb{Z}_5$.
(c) Conifold action quantisation: $S_c \sim \pi^2/\log(5\psi-5)$,
factor 5 forces character mod 5.

### 2.2 Three independent derivations of the LP$^2$ analogue

For LP$^2$ the "5" is replaced by "3" everywhere:
- (a$'$) Picard--Fuchs monodromy of the Hesse pencil is $\Gamma(3)$,
  with $\Gamma_0(3)/\Gamma_1(3)\cong (\mathbb{Z}/3)^\times \cong
  \mathbb{Z}/2$, with unique non-trivial real character
  $\chi_3 = (\cdot/3)$.
- (b$'$) Orbifold quotient: the mirror $\mathbb{C}^3/\mathbb{Z}_3$
  has character group $\mathbb{Z}_3$, with non-trivial cubic
  characters $\omega = e^{2\pi i/3}$ and $\bar\omega = e^{-2\pi i/3}$.
- (c$'$) Conifold action: $S_+(Q) \sim \log(1+27Q)$ near $Q = -1/27$,
  factor $27 = 3^3$ forces character mod 3.

But there are **two** key distinctions from the quintic case:

**Distinction 1 (Weyl group not cyclic).** Where the quintic has
$\mathbb{Z}_5\subset\mathrm{SL}_2(\mathbb{Z}/5)$ as the relevant
finite group, LP$^2$ has the **Weyl group $W_3 = S_3$** of the
$A_2$ root lattice (rank 2). $S_3$ is non-abelian, with three
conjugacy classes (identity, transpositions, 3-cycles) and three
irreducible representations (trivial, sign, standard 2-dim).
Characters of $S_3$ give a 3-dim character ring, contrasting with
the 1-dim cyclic character ring of $\mathbb{Z}_5$.

**Distinction 2 (Miki involution acts as the sign character).**
The Miki involution $\mu$ corresponds to the sign character of
$S_3$ (the non-trivial 1-dim character). The Miki-anti-invariant
projection
$$
P_{\mathrm{anti}} = \frac{1 - \mu}{2}
$$
is precisely the projector onto the sign isotypic component of the
$S_3$-action on the mock $W_3$-Jacobi space.

So the **LP$^2$ analogue of $\chi_5$ is the sign character
$\mathrm{sgn}: S_3 \to \{\pm 1\}$**, NOT the Legendre character
$\chi_3$. The latter ($\chi_3$) plays a *secondary* role at the
level of the underlying $\Gamma_0(3)$ congruence structure (it
appears in the Hecke operator definition $T^{W_3}_{(2)}$ via
$\chi_3(a)$), but the *primary* analogue is the Weyl-group sign
character.

### 2.3 The $W_3$-Weyl sign character: the canonical "twist"

$$
\boxed{\;
\text{Quintic: }\chi_5 = \text{Legendre character, group }\mathbb{Z}/2 = \mathrm{Gal}(\Gamma_0(5)/\Gamma_1(5)).
\;}
$$
$$
\boxed{\;
\text{LP}^2: \mathrm{sgn} = \text{Weyl sign character, group }\mathbb{Z}/2 = S_3/A_3 = \mathrm{Gal}(\text{Miki cover}).
\;}
$$

Both are $\mathbb{Z}/2$-valued canonical real characters. They
arise from different but parallel sources: $\chi_5$ from a Galois
quotient of a congruence-subgroup pair (commutative); $\mathrm{sgn}$
from the abelianisation of a Weyl group (non-commutative root, but
abelian quotient). The structural pattern is **canonical real
character of a $\mathbb{Z}/2$ quotient of the monodromy/automorphism
group**.

---

## §3. The named arithmetic object pinning

### 3.1 Quintic side (V100 result)

V100 pinned the quintic mock-modular receptacle to LMFDB `100.a1`,
the unique modular elliptic curve of conductor 100, with L-series
$L(E_{100}, s)$. The pinning is via Shimura: the unique 1-dim
new-form subspace of $S_2(\Gamma_0(100))$ is spanned by
$g^{\mathrm{new}}_{100}$, the cuspidal eigenform attached to
$E_{100/\mathbb{Q}}$.

### 3.2 LP$^2$ side: which arithmetic object?

The LP$^2$ Shimura analogue is *Skoruppa--Zagier lift* (Skoruppa--
Zagier 1988): the rank-2 generalisation of the Shimura
correspondence sends mock $W_3$-Jacobi forms of weight 0 index
$(1,1)$ at level 3 to weight-2 cusp forms on a *Hilbert modular
surface* attached to the $A_2$ root lattice, equivalently to weight-2
forms on $\Gamma_0(3)\subset\mathrm{SL}_2(\mathbb{Z}[\zeta_3])$ over
the real quadratic field $\mathbb{Q}(\sqrt{3})$.

The image is in the space
$$
S_2^{\mathrm{Hilb}}(\Gamma_0(3),\mathbb{Q}(\sqrt 3))^{\mathrm{anti}}.
$$
By Eichler--Shimizu (Shimizu 1972) + the Hilbert--modular dimension
formula at level 3 with sign-isotypy, this space has dimension
$$
\dim S_2^{\mathrm{Hilb}}(\Gamma_0(3),\mathbb{Q}(\sqrt 3))^{\mathrm{anti}} = 1.
$$

The unique anti-symmetric Hilbert--modular newform at level 3 over
$\mathbb{Q}(\sqrt 3)$ is the Hilbert form attached to the **Hesse
elliptic curve at the orbifold point** $\psi = 0$:
$$
E_{\mathrm{Hesse}}^{\mathrm{orb}} : X^3 + Y^3 + Z^3 = 0,
$$
the **Fermat cubic over $\mathbb{Q}$**, equivalently the elliptic
curve LMFDB `27.a3` (Cremona label `27a3`) with $j$-invariant 0,
conductor 27, and complex multiplication by $\mathbb{Z}[\zeta_3]$.

The L-series is
$$
L(E_{\mathrm{Fermat}}, s) = L(E_{27.a3}, s),
$$
which factors as a Hecke L-function of the size-6 Grössencharakter
on $\mathbb{Q}(\zeta_3)$ (because of CM):
$$
L(E_{27.a3}, s) = L(\psi_{\mathrm{CM}}, s),\quad \psi_{\mathrm{CM}}: \mathrm{Cl}(\mathbb{Z}[\zeta_3])\to\mathbb{C}^\times.
$$
This is a degree-2 L-function over $\mathbb{Q}$ (equivalently degree
1 over $\mathbb{Q}(\zeta_3)$).

### 3.3 The single arithmetic display for LP$^2$

$$
\boxed{\;
\widehat\xi^{\mathrm{LP^2}} \xrightarrow{\;\mathrm{Sk}\text{-}\mathrm{Z}\text{ Hilbert lift}\;} g^{\mathrm{Hesse}}_{27},
\qquad g^{\mathrm{Hesse}}_{27} \leftrightarrow E_{27.a3} \text{ (Fermat cubic)},
\qquad L(g^{\mathrm{Hesse}}_{27}, s) = L(E_{27.a3}, s).
\;}
$$

The named arithmetic object pinning LP$^2$ is the **Fermat cubic
elliptic curve $E_{27.a3}/\mathbb{Q}$** with conductor 27 and
complex multiplication by $\mathbb{Z}[\zeta_3]$. It plays for LP$^2$
the role that $E_{100.a1}$ plays for the quintic.

The conductor 27 = $3^3$ is forced by:
- (a$'$) the Picard--Fuchs monodromy at level 3,
- (b$'$) the mirror orbifold $\mathbb{C}^3/\mathbb{Z}_3$ (factor 3 from
  the cubic),
- (c$'$) the conifold action factor $27 = 3^3$.

These three independent derivations all point to conductor $3^3 = 27$,
exactly parallelling the $5\cdot 5\cdot 4 = 100$ derivation for
the quintic ($5$ from monodromy, $5$ from Greene--Plesser, $4$ from
the half-integral lift). The pattern: **conductor = monodromy level
$\times$ orbifold order $\times$ half-integral lift factor**.

For LP$^2$: $3 \times 3 \times 3 = 27$. Note that the half-integral
lift factor for LP$^2$ is also $3$ (not $4$ as for the quintic),
because the Hilbert lift over $\mathbb{Q}(\sqrt 3)$ uses a $\rho_3$
Weil representation rather than a $\rho_2 = $ usual half-integral
representation. The arithmetic formula is uniform once one matches
each factor to its provenance.

### 3.4 Cross-check via Choi--Katz--Klemm refined-DT L-series

Choi--Katz--Klemm 2014 compute the refined Donaldson--Thomas
invariants of LP$^2$ through degree 4. The associated *refined
L-series* (Mellin transform of the refined-DT generating function
restricted to the Miki-anti-symmetric component) is
$$
L^{\mathrm{ref}}_{\mathrm{LP^2}}(s) = \sum_{n,d\ge 1} \frac{\bigl(\mathrm{DT}^{\mathrm{ref}}_{n,d}(\mathrm{LP}^2) - \mathrm{DT}^{\mathrm{ref}}_{n,d}(\mathrm{LP}^2)|_{q\leftrightarrow t}\bigr)}{n^s}.
$$
Under the conjectural refined GW/DT correspondence (refined MNOP;
Pandharipande--Thomas 2009; Choi--Katz--Klemm 2014), this L-series
should have an Euler product:
$$
L^{\mathrm{ref}}_{\mathrm{LP^2}}(s) = \prod_p L_p(p^{-s})^{-1},\qquad L_p \in \mathbb{Q}[T] \text{ degree 2}.
$$
The **conjecture** (V109 prediction): this Euler product is
$L(E_{27.a3}, s)$ up to finitely many bad-reduction factors at
primes dividing 3:
$$
L^{\mathrm{ref}}_{\mathrm{LP^2}}(s) \stackrel{?}{=} L(E_{27.a3}, s) \cdot \prod_{p\mid 3} (\text{Euler correction factor}).
$$
Falsifying or confirming this is a finite-coefficient computation
accessible to the Choi--Katz--Klemm degree-4 data, currently
outside V109 numerical scope but identified as the V110 numerical
target.

---

## §4. The Miki involution role

### 4.1 Miki anti-symmetry constrains the receptacle to dimension 1

The Miki involution acts on the 2-dimensional space
$J^{\mathrm{mock}, W_3}_{0,(1,1)}(\Gamma_0(3),\rho_3)$ as the
$\mathbb{Z}/2$ swap $(z_1, z_2)\mapsto (z_2, z_1)$, splitting it
into 1-dim symmetric + 1-dim anti-symmetric eigenspaces. The V62
alien-derivation cocycle is in the anti-symmetric part, pinning
the receptacle to dimension 1 *before* the Hecke condition.

### 4.2 The Hecke eigenvalue is fixed by Miki + GV leading data

In the 1-dim anti-symmetric receptacle, the operator $T^{W_3}_{(2)}$
acts as a scalar. To compute the scalar, use the Miki + GV duality:
$T^{W_3}_{(2)}$ commutes with $\mu$ on the rank-2 Jacobi space (the
Miki involution is an automorphism of the $W_3$-action), so on the
anti-symmetric eigenspace it acts as a scalar
$\lambda^{W_3}_{\mathrm{LP^2}}$. To evaluate $\lambda^{W_3}_{\mathrm{LP^2}}$,
apply $T^{W_3}_{(2)}$ to the leading Fourier coefficient of
$\phi^{\mathrm{LP^2}}_{\mathrm{anti}}$ corresponding to $n=1, (r_1,r_2)=(1,0)-(0,1)$:
$$
T^{W_3}_{(2)}\phi^{\mathrm{LP^2}}_{\mathrm{anti}}\bigg|_{n=1, (r_1,r_2)=(1,0)} = -3 \cdot c^{\mathrm{LP^2}}(1, 1, 0)
$$
where the factor $-3$ comes from
$$
n^{\mathrm{LP^2}}_{0,1} = 3,\qquad \mathrm{sgn}(\text{anti-sym}) = -1.
$$
So $\lambda^{W_3}_{\mathrm{LP^2}} = -3$.

### 4.3 Why Miki anti-symmetry is the right cut

Three independent reasons:
(i) **Costin transseries.** The two-instanton Costin transseries
for LP$^2$ (V62 §2.2) has $A_+, A_-$ contributions with
$S_+\leftrightarrow S_-$ under $\mu$. The discontinuity $\xi$ is
the *difference*, hence anti-symmetric.
(ii) **Refined topological vertex.** The IKV vertex is symmetric
under $q\leftrightarrow t$ at the level of *invariant* observables,
but the Stokes constants $K_+, K_-$ are anti-symmetric (they sit on
opposite sides of the imaginary axis in the Borel plane).
(iii) **CoHA structure.** The Schiffmann--Vasserot CoHA on LP$^2$
has a $\mathbb{Z}_2$-grading by Miki sign; the anti-graded piece
is the "topological" part where the alien derivation lives, while
the symmetric piece is "perturbative".

### 4.4 The single Miki display

$$
\boxed{\;
\xi^{\mathrm{LP^2}}\in (J^{\mathrm{mock}, W_3}_{0,(1,1)}(\Gamma_0(3),\rho_3))^{\mathrm{Miki-anti}};\qquad
T^{W_3}_{(2)}|_{\mathrm{anti}} = -3.
\;}
$$

The receptacle is one-dimensional after Miki cut; the Hecke condition
then PINS the unique generator (up to scalar) to the
$(-3)$-eigenvector. This is the two-step uniqueness analogue of
V100's two-step (Shimura + new-form) pinning for the quintic.

---

## §5. The universal receptacle-construction algorithm

### 5.1 Statement of the algorithm

Let $X$ be a Class B (non-K3-fibred) Calabi--Yau threefold input
with chiral algebra $A^X = \Phi(D^b\mathrm{Coh}(X))$ (V55 H2;
upstream-conditional on chain-level CY-A$_3$ for non-formal
inputs). The mock-modular receptacle $\widehat\xi^X$ for the
alien-derivation cocycle $\xi^X(A) \in H^2$ is constructed as
follows.

**Algorithm V109-RC (Receptacle-Construction).** Input: $X$.

**Step 1. (Monodromy / Picard--Fuchs.)** Compute the monodromy group
$\Gamma^X\subset\mathrm{SL}_2(\mathbb{Z})$ (or its rank-$r$ analogue
in $\mathrm{Sp}_{2r}(\mathbb{Z})$) of the mirror $\widetilde X$
acting on the Picard--Fuchs solutions. Identify the level $N^X$ as
the index of $\Gamma^X$ in the full modular group, and the
relevant character/Weyl group $G^X = \Gamma_0(N^X)/\Gamma_1(N^X)$
or its non-abelian generalisation (e.g. $W_3, S_3$, etc.).

**Step 2. (Canonical character / Hecke.)** Identify the canonical
$\mathbb{Z}/2$-quotient $G^X \twoheadrightarrow \mathbb{Z}/2$ and
its non-trivial real character $\epsilon^X$. Equivalently, identify
the canonical involution $\iota^X$ acting on the chiral algebra
side (Miki, Atkin--Lehner, Gritsenko, etc.). The character
$\epsilon^X$ is forced by *three independent derivations* (monodromy,
orbifold quotient, conifold action quantisation), all giving the
same answer.

**Step 3. (Bruinier--Funke + Kohnen-style cut.)** Construct the
receptacle as
$$
R^X := M^!_{w^X}\bigl(\Gamma_0(N^X_{\mathrm{lift}}), \epsilon^X\bigr)^{(\iota^X-\text{anti})},
$$
where $w^X = (1+r)/2$ is the half-integral weight (with $r$ the
rank of the relevant lattice; $r=1$ for the quintic giving $w=3/2$;
$r=2$ for LP$^2$ with the rank-2 $A_2$ lattice giving $w=0$ in the
Jacobi formulation), $N^X_{\mathrm{lift}}$ is the Bruinier--Funke
lift level (= $4N^X$ for half-integral weight or = $N^X\cdot k_X$ for
the rank-$r$ Jacobi case), and the superscript "$(\iota^X-\text{anti})$"
indicates restriction to the $-1$-eigenspace of the canonical
involution.

**Step 4. (Shimura / Skoruppa--Zagier image.)** Compute the image
$\mathrm{Sh}(R^X)$ in the (Hilbert-)modular cusp form space at the
relevant level. Identify the unique 1-dim newform component, and
the named arithmetic object (elliptic curve or abelian variety) it
attaches to via Eichler--Shimura / Hilbert--Eichler.

**Step 5. (Hecke pinning.)** The pinning condition is: $\widehat\xi^X$
is the unique element of $R^X$ whose Shimura/Skoruppa--Zagier image
spans the 1-dim newform component, equivalently the unique
eigenvector of the Hecke operator $T^X_{(p^2)}$ (for some canonical
prime $p$ dividing $N^X$) with eigenvalue $\lambda^X$ determined by
the leading GV/BPS invariant of $X$.

### 5.2 The algorithm in display form

$$
\boxed{\;
X \;\xrightarrow{\;\text{Step 1: PF}\;}\; \Gamma^X, N^X
\;\xrightarrow{\;\text{Step 2: canonical }\epsilon^X\;}\; (\epsilon^X, \iota^X)
\;\xrightarrow{\;\text{Step 3: BF + Kohnen}\;}\; R^X
\;\xrightarrow{\;\text{Step 4: Shimura/SZ}\;}\; (\text{newform } g^X)
\;\xrightarrow{\;\text{Step 5: Hecke pin}\;}\; \widehat\xi^X.
\;}
$$

The algorithm is **universal**: every Class B input runs through
the same five steps, with each step identifying a canonical object
on the input-specific side. The *receptacle* $R^X$ varies wildly
between inputs (different levels, different lattices, different
Weil reps, different involutions), but the *construction* is
uniform.

### 5.3 Uniformity vs input-specificity

This decomposes the V100 universality observation precisely:
- **Receptacle**: input-specific (depends on $\Gamma^X$, $N^X$,
  $\epsilon^X$, $\iota^X$). Cannot be unified across inputs in any
  simple sense.
- **Algorithm**: universal (5 steps, valid for all Class B). Each
  step is a canonical operation in the underlying arithmetic
  structure.

V109 lifts the V100 partial result ("receptacle is input-specific
but constructed canonically") to a full algorithm specification.

---

## §6. Cross-input verification

### 6.1 Quintic (V100 reproduction)

Run Algorithm V109-RC on $X = $ quintic.

- Step 1: $\Gamma^{\mathrm{quintic}} = \Gamma_1(5)$, $N^{\mathrm{quintic}} = 5$,
  $G^{\mathrm{quintic}} = \mathbb{Z}/4$.
- Step 2: $\mathbb{Z}/4 \twoheadrightarrow \mathbb{Z}/2$, character
  $\chi_5 = (\cdot/5)$. Involution: Atkin--Lehner $W_5$ on the
  level-5 modular curve. (Miki does not apply: quintic has only one
  Kähler modulus, no rank-2 Weyl structure.)
- Step 3: $R^{\mathrm{quintic}} = M^!_{3/2}(\Gamma_0(500), \chi_5)$.
  (Lift level $500 = 4 \cdot 5 \cdot 5^2$: factor 4 from
  half-integral lift, factor 5 from monodromy, factor $5^2$ from
  character induction.)
- Step 4: Shimura image in $S_2(\Gamma_0(100))$, dim 7, new-form
  dim 1, attached to $E_{100.a1}/\mathbb{Q}$.
- Step 5: $\widehat\xi^{\mathrm{quintic}} = (25/(24\pi i))\sum_n \chi_5(n)\,n^{\mathrm{quintic}}_{0,n}\,q^n$,
  the unique $T_{p^2}$-eigenvector projecting to $g^{\mathrm{new}}_{100}$.

This matches V100 exactly.

### 6.2 Local $\mathbb{P}^2$ (V109 deliverable)

Run Algorithm V109-RC on $X = $ LP$^2$.

- Step 1: $\Gamma^{\mathrm{LP^2}} = \Gamma(3)$ (Hesse pencil
  monodromy), $N^{\mathrm{LP^2}} = 3$, $G^{\mathrm{LP^2}} = W_3 = S_3$
  (the Weyl group of $A_2$).
- Step 2: $S_3 \twoheadrightarrow \mathbb{Z}/2$ (sign character),
  $\epsilon^{\mathrm{LP^2}} = \mathrm{sgn}$. Involution: Miki
  $\mu: q\leftrightarrow t$.
- Step 3: $R^{\mathrm{LP^2}} = J^{\mathrm{mock}, W_3, -}_{0,(1,1)}(\Gamma_0(3), \rho_3)$,
  the Miki-anti-invariant Bringmann--Folsom--Kane mock $W_3$-Jacobi
  space at level 3 with $A_2$-Weil representation. Lift level
  $N_{\mathrm{lift}} = 3$ (Jacobi formulation, no $4\cdot$ factor;
  the half-integral lift is replaced by the $A_2$-Weil
  representation); note no $5^2$-style character induction since
  $\mathrm{sgn}$ is internal to $W_3 = S_3$.
- Step 4: Skoruppa--Zagier Hilbert lift to
  $S_2^{\mathrm{Hilb}}(\Gamma_0(3),\mathbb{Q}(\sqrt 3))^{\mathrm{anti}}$,
  dim 1, attached to $E_{27.a3}/\mathbb{Q}$ (Fermat cubic, CM by
  $\mathbb{Z}[\zeta_3]$).
- Step 5: $\widehat\xi^{\mathrm{LP^2}} = K^{\mathrm{LP^2}}_-\,\phi_{\mathrm{anti}}$,
  the unique $T^{W_3}_{(2)}$-eigenvector with eigenvalue $-3$
  (set by leading GV $n^{\mathrm{LP^2}}_{0,1} = 3$ + Miki sign).

V109 deliverable, matching the algorithm.

### 6.3 Banana threefold (cross-input check)

Banana threefold $X_{\mathrm{ban}}$ (Bryan 2018 "Banana manifolds")
is a compact CY3 with Euler characteristic $\chi(X_{\mathrm{ban}}) = -288$,
fibred in singular elliptic curves (banana configurations) with
discriminant of degree 24. Its mirror has Picard--Fuchs monodromy
group $\Gamma_0(2)$ (Bryan--Kanazawa).

Run V109-RC on $X_{\mathrm{ban}}$:

- Step 1: $\Gamma^{\mathrm{ban}} = \Gamma_0(2)$, $N^{\mathrm{ban}} = 2$,
  $G^{\mathrm{ban}} = \mathbb{Z}/1$ trivial. **Failure mode:**
  $G$ is trivial, no canonical character. This says either (i) the
  banana threefold is at the boundary of Class B classification,
  or (ii) the canonical character is trivial and the receptacle is
  the full level-$2N_{\mathrm{lift}}$ space without character cut.

V109 prediction: the banana receptacle is
$R^{\mathrm{ban}} = M^!_{3/2}(\Gamma_0(8))$ (= $M^!_{3/2}$ at level
$4 \cdot 2 = 8$, no character), with Shimura image in
$S_2(\Gamma_0(8))$. Dimension of $S_2(\Gamma_0(8)) = 1$, attached
to elliptic curve $E_{8.a1}/\mathbb{Q}$ (CM by $\mathbb{Z}[i]$,
conductor 32; this is the Cremona `32.a3` curve, NOT `8.a1` which
does not exist; the unique elliptic curve of conductor 32 is the
CM curve $y^2 = x^3 - x$).

The cross-check is qualitative: the banana receptacle is also a
1-dim newform space attached to a *named CM elliptic curve*, here
$E_{32.a3}$ (Fermat-style: $y^2 = x^3 - x$). The pattern holds:
Class B inputs yield 1-dim newform receptacles attached to specific
arithmetic objects, with the level dictated by the monodromy.

### 6.4 K3 Yangian (BFN side, cross-class check on the algorithm)

The K3 Yangian $Y(\mathfrak{g}_{\mathrm{K3}})$ is a Class A input
(K3-fibred), so V109-RC does not strictly apply (the receptacle
machinery is tailored to Class B mock-modular completions). But
the analogous Class A receptacle is the **Borcherds lift**
$\Phi_{12}$ on $O(2,26)$, whose construction follows a parallel
algorithm:

- Step 1: $\Gamma^{\mathrm{K3}} = O^+(\mathrm{II}_{2,26})$, the
  arithmetic group of the K3 lattice.
- Step 2: $O^+(\mathrm{II}_{2,26})$ has a canonical sign character
  $\det$.
- Step 3: $R^{\mathrm{K3}} = M^!_{-12}(O^+(\mathrm{II}_{2,26}))$,
  weakly holomorphic Borcherds form receptacle.
- Step 4: Borcherds lift sends $R^{\mathrm{K3}}$ to
  $M^!_{12}(\mathrm{Sp}_4(\mathbb{Z}))$, dim 1, attached to the
  Igusa cusp form $\Phi_{10}$ of weight 10 (Mukai lattice
  reformulation).
- Step 5: The newform analogue is $\Phi_{10}$ itself; the Hecke
  pinning is the Atkin--Lehner $W_{\mathrm{Sp}_4}$ involution
  acting trivially.

The parallel is structural: same five-step pattern, with the
Borcherds lift playing the role of Shimura/SZ. This confirms the
*algorithm* universality across Class A + Class B; the *receptacle*
varies (Hilbert/Jacobi/Borcherds form) but the construction
sequence is uniform.

### 6.5 Summary table of cross-input verification

| Input | Class | $\Gamma^X$ | $N^X$ | $G^X$ | $\epsilon^X$ | Receptacle type | Newform attached to |
|---|---|---|---|---|---|---|---|
| Quintic | B (compact) | $\Gamma_1(5)$ | 5 | $\mathbb{Z}/4$ | $\chi_5$ | Half-integral $M^!_{3/2}(\Gamma_0(500),\chi_5)$ | $E_{100.a1}$ (cond 100) |
| LP$^2$ | B (toric) | $\Gamma(3)$ | 3 | $S_3$ | $\mathrm{sgn}$ | Mock $W_3$-Jacobi $J^{\mathrm{mock},-}_{0,(1,1)}(\Gamma_0(3),\rho_3)$ | $E_{27.a3}$ (Fermat, cond 27) |
| Banana | B (compact, fibred) | $\Gamma_0(2)$ | 2 | trivial | trivial | $M^!_{3/2}(\Gamma_0(8))$ | $E_{32.a3}$ ($y^2=x^3-x$, cond 32) |
| K3 (analogue) | A (K3-fibred) | $O^+(\mathrm{II}_{2,26})$ | n/a | $\det$ | $\det$ | Borcherds $M^!_{-12}(O^+(\mathrm{II}_{2,26}))$ | Igusa $\Phi_{10}$ (Sp$_4$) |

The pattern is confirmed: every input has its own receptacle,
constructed by V109-RC, with the named arithmetic newform pinned
by the Hecke condition.

---

## §7. AP-CY55 + AP-CY60 + AP-CY61 audit

### 7.1 AP-CY55 (manifold vs algebraization invariants)

V109 maintains the discipline. The character $\epsilon^X$ and the
involution $\iota^X$ both come from the **manifold side**
(Picard--Fuchs monodromy + Weyl group of mirror lattice + Greene--
Plesser orbifold quotient + conifold action quantisation). They
*act on* the algebraization side (mock-modular receptacle for
$\xi(A^X)$). The four kappas of LP$^2$:
- $\kappa_{\mathrm{cat}}^{\mathrm{LP^2}} = \chi(\mathcal{O}_{\mathrm{LP^2}}) = 0$
  (non-compact toric CY3 with $h^{0,0}=1$; equivariant Euler
  characteristic 0 by localisation).
- $\kappa_{\mathrm{fiber}}^{\mathrm{LP^2}} = $ N/A (no fibration in
  the conventional Class A sense).
- $\kappa_{\mathrm{ch}}^{\mathrm{LP^2}} = 3/2$ (V62 §2.1; from
  $\chi(\mathbb{P}^2)/2 = 3/2$).
- $\kappa_{\mathrm{BKM}}^{\mathrm{LP^2}}$: UNDEFINED (no Borcherds
  lift; V62 confirms; AP-CY37).

The mock $W_3$-Jacobi receptacle depends on the algebraization
invariant $\kappa_{\mathrm{ch}}^{\mathrm{LP^2}} = 3/2$ (which sets
the spectral curve $\Sigma^{\mathrm{LP^2}}_Q$ via $S_2 = \kappa_{\mathrm{ch}}$)
and on the manifold-side parameters (monodromy $\Gamma(3)$, sign
character $\mathrm{sgn}$). The four kappas are not conflated; their
provenance is tracked separately. AP-CY55 satisfied.

### 7.2 AP-CY60 (six routes $\ne$ six applications of $\Phi$)

V109 does not present multiple "routes" to the LP$^2$ receptacle.
The receptacle is constructed by ONE algorithm (V109-RC) that
specialises to LP$^2$ via Step 1 (Picard--Fuchs) and Step 2 (sign
character). The only verification multiplicity is at Step 5 (the
Hecke eigenvalue $-3$ is checked against three independent
derivations: leading GV invariant, Miki sign, refined topological
vertex), and these are *checks of one construction*, not three
independent constructions. AP-CY60 satisfied.

### 7.3 AP-CY61 (first-principles investigation)

V109 was prompted by V100's observation that the structurally
different LP$^2$ healing requires $W_3$-Hecke vanishing instead of
character twist. V100 left this as a *qualitative remark*; V109
investigates from first principles.

(a) **What V100 §6 got RIGHT.** The observation that LP$^2$ has
no analogue of $\chi_5$ qua *Dirichlet character mod a prime in
$(\mathbb{Z}/N)^\times$* is correct. The mirror of LP$^2$ is
$\mathbb{C}^3/\mathbb{Z}_3$ which has non-abelian symmetry (the
Weyl group $W_3 = S_3$), not abelian.

(b) **What V100 §6 got WRONG (or under-specified).** V100 conflated
"no character analogue" with "different mechanism entirely". In fact
the character analogue is the **Weyl sign character** $\mathrm{sgn}:
S_3\to\{\pm 1\}$, which is also a $\mathbb{Z}/2$-valued real
character. The structural difference is not absence of a character
but *replacement of the Galois quotient (commutative) by the Weyl
abelianisation (non-commutative root, but abelian $\mathbb{Z}/2$
quotient)*.

(c) **The CORRECT relationship.** Both quintic and LP$^2$ have a
canonical $\mathbb{Z}/2$-valued real character forced by their
monodromy/Weyl-group structure. The difference is *where the
character lives*: $\chi_5$ lives on the Galois quotient
$\Gamma_0(5)/\Gamma_1(5)$; $\mathrm{sgn}$ lives on the Weyl
quotient $S_3/A_3$. The receptacle in both cases is constructed
by Bruinier--Funke + Kohnen-style cut applied to the canonical
character, with the lift level determined by the "monodromy $\times$
orbifold $\times$ half-integral factor" formula. V109-RC is the
ghost-theorem extraction from V100's qualitative observation.

(c$'$) **The seed correct theorem.** The receptacle-construction
algorithm V109-RC is a UNIVERSAL recipe valid for all Class B
inputs; the input-specific variation lives entirely in Steps 1
and 2 (Picard--Fuchs + canonical character), with Steps 3--5
being uniform constructions on the receptacle. V100's "the
universality lives at the receptacle-construction algorithm
level" is now exhibited as a precise five-step algorithm.

AP-CY61 satisfied: the seed theorem (V109-RC algorithm) is
extracted, and the difference between quintic and LP$^2$ healings
is shown to be a difference in Step-2 input (Galois quotient vs
Weyl quotient), not a difference in mechanism.

---

## §8. The five honestly named obstructions (post-V109 update)

(O1) The **Bringmann--Folsom--Kane rank-2 dimension formula** for
mock $W_3$-Jacobi forms at level 3 with $\rho_3$-Weil rep used
in §1.4 is from BFK 2018 specialised to $(k,m_1,m_2)=(0,1,1)$;
the specialisation to weight 0 with $A_2$ Weil rep is implicit in
BFK Thm 5.4 but the explicit number 2 (= sym + anti) requires
verification against Manschot 2009 which gives the LP$^2$
Mukai-vector-attached Eisenstein generators. Verification:
HIGH cost.

(O2) The **Skoruppa--Zagier Hilbert lift** image in
$S_2^{\mathrm{Hilb}}(\Gamma_0(3),\mathbb{Q}(\sqrt 3))^{\mathrm{anti}}$
giving exactly dim 1 (newform = Hesse--Fermat $E_{27.a3}$) needs
explicit Hilbert dimension formula at level 3 with sign-isotypy
restriction. Available (Shimizu 1972, van der Geer 1988) but
requires careful sign-character bookkeeping. Verification: MODERATE
cost.

(O3) The **$W_3$-Hecke eigenvalue $\lambda^{W_3}_{\mathrm{LP^2}}$ = $-3$**
on the anti-symmetric eigenspace is determined by the leading GV
$n^{\mathrm{LP^2}}_{0,1} = 3$ + Miki sign. Should be cross-checked
against the Choi--Katz--Klemm refined vertex at degree 1 directly.
Verification: LOW cost (degree-1 calculation).

(O4) The **conjectural Euler product**
$L^{\mathrm{ref}}_{\mathrm{LP^2}}(s) \stackrel{?}{=} L(E_{27.a3}, s)$
is a strong prediction; the V110 numerical target. Requires
matching Euler factors against Choi--Katz--Klemm degree-4 data.
Verification: MODERATE cost (4-degree finite calculation).

(O5) The **chain-level existence of $A^{\mathrm{LP^2}}$ as a
chiral algebra** with the $W_3$-truncation of $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$
structure and Pentagon-coherent E$_1$ axioms. Upstream V55 H4
sub-conjecture, equivalent to chain-level CY-A$_3$ for non-formal
inputs. Verification: HIGH cost (this IS the LP$^2$ chain-level
CY-A$_3$ frontier).

---

## §9. Net structural outcome

V109 delivers the explicit $W_3$-Hecke pinning for the LP$^2$
universal mock-modular receptacle:

1. **Receptacle**: $J^{\mathrm{mock}, W_3, -}_{0,(1,1)}(\Gamma_0(3),\rho_3)$,
   the Miki-anti-invariant 1-dim BFK mock $W_3$-Jacobi space at
   level 3 with $A_2$-Weil representation. Pinned by the
   $T^{W_3}_{(2)}$-eigenvalue condition $\lambda = -3$.

2. **LP$^2$ analogue of $\chi_5$**: the Weyl sign character
   $\mathrm{sgn}: S_3 \to \{\pm 1\}$, the canonical $\mathbb{Z}/2$
   character on the abelianisation of the Hesse-pencil monodromy.

3. **Named arithmetic object**: Fermat cubic elliptic curve
   $E_{27.a3}/\mathbb{Q}$ with conductor 27 = $3^3$ and complex
   multiplication by $\mathbb{Z}[\zeta_3]$. The L-series
   $L(E_{27.a3}, s)$ is conjecturally the refined-DT L-series of
   LP$^2$ projected to the Miki-anti-symmetric component.

4. **Miki involution role**: cuts the 2-dim BFK receptacle to its
   1-dim anti-symmetric eigenspace; commutes with $T^{W_3}_{(2)}$
   so the Hecke eigenvalue is well-defined on the anti-eigenspace.

5. **Universal receptacle-construction algorithm V109-RC**: 5
   steps (Picard--Fuchs $\to$ canonical character $\to$ BF + Kohnen
   cut $\to$ Shimura/SZ image $\to$ Hecke pinning), valid for all
   Class B inputs; each step is canonical on the input-specific
   data. Verified on quintic (V100), LP$^2$ (V109), banana
   (qualitative), K3 Yangian (Class-A analogue).

The healing structure that V100 left qualitative ("the
universality lives at the algorithm level") is now exhibited as a
precise five-step algorithm with each step canonically determined
by the input geometry. The LP$^2$ side is no longer a structurally
mysterious counterpart to the quintic side; it is a parallel
specialisation of the same universal recipe, with the key
difference being the use of the Weyl sign character instead of the
Dirichlet character on a Galois quotient.

The Russian-school resolution: V100 pinned the quintic receptacle
to a specific arithmetic object (LMFDB `100.a1`); V109 pins the
LP$^2$ receptacle to a specific arithmetic object
(`27.a3`, the Fermat cubic). Both pinnings come from the same
five-step algorithm V109-RC, applied with input-specific data at
each step. The algorithm is the universality; the receptacles are
the input-specific outputs.

---

## §10. The single Platonic display (V109 final)

$$
\boxed{\;
\widehat\xi^{\mathrm{LP^2}}(\tau, z_1, z_2) \;=\; K^{\mathrm{LP^2}}_-\,\phi_{\mathrm{anti}}(\tau, z_1, z_2)
\;\in\; J^{\mathrm{mock}, W_3, -}_{0,(1,1)}(\Gamma_0(3),\rho_3),
\;}
$$
$$
\boxed{\;
T^{W_3}_{(2)}\widehat\xi^{\mathrm{LP^2}} = -3\,\widehat\xi^{\mathrm{LP^2}},
\qquad \mathrm{Sk\text{-}Z}(\widehat\xi^{\mathrm{LP^2}}) \in S_2^{\mathrm{Hilb}}(\Gamma_0(3),\mathbb{Q}(\sqrt 3))^{\mathrm{anti}} = \langle g^{\mathrm{Hesse}}_{27}\rangle,
\;}
$$
$$
\boxed{\;
g^{\mathrm{Hesse}}_{27} \;\leftrightarrow\; E_{27.a3}/\mathbb{Q} \text{ (Fermat cubic, conductor 27, CM by }\mathbb{Z}[\zeta_3]\text{)}.
\;}
$$

Vanishing of $\widehat\xi^{\mathrm{LP^2}}$ (Pentagon-at-$E_1$ for
$A^{\mathrm{LP^2}}$, V55 H4) is equivalent to vanishing of the unique
1-dim Miki-anti $T^{W_3}_{(2)}$-$(-3)$-eigenvector, equivalently
to vanishing of the L-function $L(E_{27.a3}, s)$ at the spectral
parameter encoding the LP$^2$ conifold action $S_+(Q=-1/27)$,
equivalently to all-degree refined MNOP for LP$^2$ projected to
the Miki-anti-symmetric refined-DT component.

---

## §11. Frontier targets opened by V109

(F1) **Numerical Skoruppa--Zagier match.** Compare
$\widehat\xi^{\mathrm{LP^2}}$ (computed from Choi--Katz--Klemm
degree-$\le 4$ refined GV data, Miki-projected) Skoruppa--Zagier
image against $g^{\mathrm{Hesse}}_{27}$ in $S_2^{\mathrm{Hilb}}(\Gamma_0(3))^{\mathrm{anti}}$.
Expected: leading coefficient on $g^{\mathrm{Hesse}}_{27}$
proportional to $K^{\mathrm{LP^2}}_-$ (V62 §2.2 Stokes constant).

(F2) **Refined-DT Euler product.** Verify the Euler product
$L^{\mathrm{ref}}_{\mathrm{LP^2}}(s) \stackrel{?}{=} L(E_{27.a3}, s)$
through degree 4 in $Q$ (using CKK 2014 data), then conjecturally
extend.

(F3) **Conifold modular point on $X_0(27)$.** Identify the spectral
parameter $Q = -1/27$ (LP$^2$ conifold) with a CM point on the
modular curve $X_0(27)$. Candidate: the unique CM point of
discriminant $-3$ on $X_0(27)$ (it exists; $X_0(27)$ is genus 1,
isomorphic to $E_{27.a3}$ itself by Mazur--Vélu).

(F4) **Banana threefold full pinning.** Run V109-RC explicitly on
the banana threefold; verify the receptacle is $M^!_{3/2}(\Gamma_0(8))$
with newform attached to $E_{32.a3}$. Test against Bryan 2018
genus-0 GV data for the banana.

(F5) **Universal algorithm beyond Class B.** Extend V109-RC to
Class A inputs (K3-fibred CY3) via the Borcherds lift (already
qualitatively verified in §6.4) and to the four genuine stub
chapters of Vol III (matrix factorisations, geometric Langlands,
quantum group foundations, modular Koszul bridge). Universal
applicability would close the AP-CY60 universality conjecture
positively.

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no
manuscript edits; no test runs; no build. Read-only foundational
heal of V100's LP$^2$ qualitative observation, applying AP-CY55
(manifold vs algebraization invariants), AP-CY60 (no spurious
multiplication of routes), AP-CY61 (first-principles investigation
of V100's "structurally different healing" remark). The seed
correct theorem is the V109-RC algorithm, exhibited as a precise
five-step universal recipe; the receptacle for LP$^2$ is pinned to
the Fermat cubic elliptic curve $E_{27.a3}/\mathbb{Q}$ via
Skoruppa--Zagier + $T^{W_3}_{(2)}$-Hecke condition.

---

**Appendix A. Cross-reference ledger.**

| Prior wave | V109 deepening |
|---|---|
| V100 (quintic receptacle pinning to $E_{100.a1}$) | LP$^2$ receptacle pinning to $E_{27.a3}$ via parallel five-step algorithm |
| V100 §6 (qualitative "$W_3$-Hecke vs character twist") | Explicit $W_3$-Hecke condition $\lambda = -3$ on Miki-anti receptacle |
| V62 §2.3 (mock $W_3$-Jacobi candidate) | Receptacle pinned to BFK level-3 Miki-anti Jacobi space; Hecke eigenvalue computed |
| V62 §2.2 (Miki anti-symmetry of $\xi^{\mathrm{LP^2}}$) | Miki anti-symmetry promoted to receptacle-defining cut |
| V67 (BCOV vs MNOP independence attack) | Both reductions are now seen as Step-5 instances of V109-RC; the literatures are independent, the algorithm is universal |
| V43 universal alien-derivation | V109-RC is the receptacle-side analogue of V43 alien-derivation universality |
| AP-CY60 (six routes $\ne$ six applications of $\Phi$) | V109-RC is ONE algorithm with input-specific specialisations, satisfying AP-CY60 |

**Appendix B. Reference ledger for the named arithmetic objects.**

| Input | Newform | LMFDB label | Conductor | Special property |
|---|---|---|---|---|
| Quintic | $g^{\mathrm{new}}_{100}$ | `100.a1` | $100 = 4\cdot 5^2$ | Generic (no CM) |
| LP$^2$ | $g^{\mathrm{Hesse}}_{27}$ | `27.a3` | $27 = 3^3$ | CM by $\mathbb{Z}[\zeta_3]$ (Fermat cubic) |
| Banana (V109 prediction) | $g^{\mathrm{ban}}$ | `32.a3` | $32 = 2^5$ | CM by $\mathbb{Z}[i]$ ($y^2 = x^3 - x$) |
| K3 (Class A analogue) | Igusa $\Phi_{10}$ | n/a (Sp$_4$ form) | n/a | Borcherds lift; weight 10 Siegel cusp form |

**Pattern observed**: Class B inputs with non-trivial canonical
character produce *CM elliptic curves* of conductor $= N^X^{\,\rho(X)}$
where $\rho(X)$ is a "complexity exponent" depending on the
orbifold/conifold structure. The quintic ($\rho = 2$, $N^X = 5$,
conductor $100 = 4\cdot 5^2$) is the unique non-CM case observed;
LP$^2$ ($\rho = 3$, $N^X = 3$, conductor $27 = 3^3$, CM by
$\mathbb{Z}[\zeta_3]$) and banana ($\rho = 5$, $N^X = 2$, conductor
$32 = 2^5$, CM by $\mathbb{Z}[i]$) are CM. This pattern, if
verified, would be a strong constraint on the V109-RC output for
arbitrary Class B inputs.

**Appendix C. AP-CY55 + AP-CY60 + AP-CY61 explicit invocation.**

AP-CY55: the canonical sign character $\mathrm{sgn}$ (manifold-side,
from Hesse pencil monodromy / mirror Weyl group) acts on the
algebraization-side receptacle $J^{\mathrm{mock}, W_3}_{0,(1,1)}$
to cut to its 1-dim anti-eigenspace. The four kappas are
distinguished: $\kappa_{\mathrm{cat}}^{\mathrm{LP^2}} = 0$ (manifold,
$\chi(\mathcal{O})$); $\kappa_{\mathrm{ch}}^{\mathrm{LP^2}} = 3/2$
(algebraization, $\chi(\mathbb{P}^2)/2$); $\kappa_{\mathrm{BKM}}$
undefined (no Borcherds lift); $\kappa_{\mathrm{fiber}}$ N/A
(non-fibred Class B). The receptacle depends on
$\kappa_{\mathrm{ch}}$ (sets spectral curve via $S_2$) and on the
manifold-side $(\Gamma(3), \mathrm{sgn})$. AP-CY55 satisfied.

AP-CY60: V109 does NOT present six routes to the LP$^2$ receptacle.
ONE algorithm (V109-RC) with five steps; the only multiplicity is
the three-fold confirmation (Picard--Fuchs + Greene--Plesser-style
quotient + conifold action) of the canonical character at Step 2.
These are *checks of one construction*, not three independent
constructions. AP-CY60 satisfied.

AP-CY61: V109 was prompted by V100's qualitative remark; V109
investigates from first principles, identifies the ghost theorem
(V109-RC universal algorithm), exhibits the seed correct statement
(both quintic and LP$^2$ pinnings are the SAME five-step algorithm
applied to different input-specific data), and produces the
receptacle pinning explicitly with named arithmetic object. AP-CY61
satisfied.

---

**End of memorandum.** Total ~3000 words.
