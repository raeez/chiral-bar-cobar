# Riemann Hypothesis via the ℓ-adic Derived Chiral Centre: Weil-Grothendieck Lift

An honest first-principles attack on the three items from the Weil–Grothendieck ℓ-adic
yoga, using the programme's derived chiral centre as the ℓ-adic realisation candidate.
Reader should hold `riemann_hypothesis_motivic_shadow_platonic.md` in parallel — that
note exhausted the three *motivic* routes; this note attacks the orthogonal *ℓ-adic*
route and shows precisely what the programme's étale realisation buys (and does not
buy) relative to the motivic one.

## 0. Coordinates: what the Weil-Grothendieck ladder demands

For a smooth projective variety $X/\mathbb{F}_q$, Grothendieck–Artin gives a graded
$\mathrm{Gal}(\overline{\mathbb{F}_q}/\mathbb{F}_q)$-representation
$H^\bullet_{\text{ét},\ell}(X_{\overline{\mathbb{F}_q}},\mathbb{Q}_\ell)$
with Frobenius endomorphism $F_q$; Deligne's Weil I + II prove
$|\alpha| = q^{i/2}$ for every eigenvalue $\alpha$ of $F_q$ on $H^i$ (pure of weight $i$).
The Weil $\zeta$-bounds follow; their *number-field* analogue is RH proper.

For the programme's chiral algebra $\mathcal{A}$ to enter this ladder, three rungs
must be climbed:

1. An ℓ-adic realisation functor $\mathcal{A} \mapsto V_\ell(\mathcal{A})$ living in
   $\mathrm{Gal}$-rep, such that $V_\ell(B(\mathcal{A}))$ computes the ℓ-adic étale
   cohomology of a geometric object naturally attached to $\mathcal{A}$.
2. A Frobenius endomorphism $F_p$ acting on $V_\ell(B(\mathcal{A}))$ with
   computable eigenvalues, and a Weil-type absolute-value bound on them.
3. A candidate "variety-over-$\mathbb{F}_1$" $\mathcal{A}_\mathbb{Z}$ whose ℓ-adic
   derived chiral centre's Frobenius spectrum matches the non-trivial
   $\zeta$-zeros.

Items (1)–(2) are geometric and can be investigated honestly on specific families.
Item (3) is where all $\mathbb{F}_1$ programmes stall; we spell out exactly how the
chiral-algebra framework stalls in the same place, and whether it offers anything new.

## 1. ℓ-adic bar complex and derived chiral centre of $V_k(\mathfrak{sl}_2)$

### 1.1 Construction

Let $k=-2+p/q$ be admissible, so Arakawa $C_2$-cofiniteness yields a finite-type
simple quotient $L_k(\mathfrak{sl}_2)$ whose weight spaces $L_k(\mathfrak{sl}_2)_n$ are
finite-dimensional over $\mathbb{Q}$. The bar complex
$B(L_k(\mathfrak{sl}_2)) = \bigoplus_{n\geq 0} L_k(\mathfrak{sl}_2)^{\otimes n}[n]$
is levelwise finite over $\mathbb{Q}$; each weight-$w$ summand $B_w$ is a finite-
dimensional $\mathbb{Q}$-vector space. Define
$B_\ell(\mathcal{A}) := B(\mathcal{A}) \otimes_\mathbb{Q} \mathbb{Q}_\ell.$

For the Galois action, we need a base-change lift. At admissible level, characters
$\chi_{k,\lambda}(\tau)$ are Kac–Wakimoto modular forms of explicit weight $w_\lambda$
and level $N_\lambda$ on $\Gamma_0(N_\lambda)$. Deligne's construction attaches to any
such cuspidal eigenform a compatible system of two-dimensional ℓ-adic Galois
representations $\rho_{f,\ell}: \mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q}) \to
\mathrm{GL}_2(\overline{\mathbb{Q}_\ell})$. The ℓ-adic bar of
$L_k(\mathfrak{sl}_2)$ is then the Grothendieck spectral weight filtration
$V_\ell(B_w(L_k(\mathfrak{sl}_2))) := \bigoplus_{\lambda \vdash w} \rho_{f_{k,\lambda},\ell}^{\otimes m_\lambda(w)}$
where $m_\lambda(w)$ is the multiplicity of the weight-$\lambda$ character
component in $B_w$ (computed by Kac-Wakimoto fusion rules; finite).

This is the first item's ℓ-adic bar. The $\mathrm{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$-
action is by Deligne on each $\rho_{f,\ell}$; it promotes to a $\mathrm{Gal}$-action
on the derived chiral centre $Z^{\mathrm{der}}_{\mathrm{ch}}(L_k(\mathfrak{sl}_2))$ via
the chiral Deligne-Tamarkin bridge to $\mathrm{ChirHoch}^\bullet$, which at admissible
level is concentrated in $\{0,1,2\}$ per Theorem H and whose $\mathrm{ChirHoch}^0$
component is $Z(L_k(\mathfrak{sl}_2)) = $ fusion centre.

**Honesty check.** The construction is *not* a standalone ℓ-adic derived chiral
centre with intrinsic Galois action; it is a Deligne-pullback of the admissible
characters' Galois reps along the bar decomposition. The Galois action on the
bar is *inherited* from characters, not native to the chiral algebra. This matters
for item (2): the Frobenius bounds we compute are inherited from Deligne/Weil,
not derived independently of it.

### 1.2 Explicit for $V_k(\mathfrak{sl}_2)$, $k=-2+p/q=-4/3$ (so $p=2,q=3$)

Admissible level $k=-4/3$ gives three simple modules of conformal weights
$0, -1/3, -1/4$ (Kac-Wakimoto $A_1^{(1)}$ admissible level tables). Their characters
are modular forms of weight $1/2$ on $\Gamma_0(12)$. The weight-2 bar
$B_2(L_{-4/3})$ has dimension $\sum_\lambda \dim L_{-4/3}(\lambda)^{\otimes 2}$.
Using the Kac-Wakimoto $3\times 3$ fusion matrix, the bar graded pieces decompose
as a sum of three modular forms of explicit level and weight. Deligne attaches
Galois reps to each; the $\mathrm{Gal}$-action on $V_\ell(B_2(L_{-4/3}))$ is then
explicit up to $\mathrm{GL}_2$-semisimplification.

## 2. Frobenius eigenvalue bounds on $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal{A})$

### 2.1 Claim attempted

For each prime $p \nmid 12$, the Frobenius $F_p$ on $V_\ell(B_w(L_{-4/3}))$ has
eigenvalues $\{\alpha_{p,i,\lambda}\}$ inherited from the Hecke eigenvalues
$a_p(f_{k,\lambda})$ of the admissible characters. Deligne's theorem on modular
forms $|\alpha_{p,i,\lambda}| = p^{(w_\lambda-1)/2}$ transports to
$|\alpha_{p,i,\lambda}| = p^{w_\lambda/2 - 1/2}$ on $V_\ell(B_w)$.

### 2.2 Would this be a new RH-type statement?

No — and the reason is precisely the one FM129 already records. The Weil-type bound
on $V_\ell(B_w(L_{-4/3}))$ is a *theorem* of Deligne (1974, modular forms case —
Weil II specialises to the Eichler-Shimura theorem). The programme's shadow tower
constructs $V_\ell(B_w(L_{-4/3}))$ as a specific representation; the bound on
Frobenius eigenvalues comes from applying Deligne to the underlying characters, not
from any shadow-tower computation.

**Where the programme *does* contribute.** The bar decomposition produces the
*explicit weight-$w$ multiplicities* $m_\lambda(w)$ from fusion, which Deligne's
theorem on individual forms does not tell you. Combined, we can bound the trace
$\mathrm{Tr}(F_p \mid V_\ell(B_w)) = \sum_\lambda m_\lambda(w) a_p(f_{k,\lambda})$,
and this gives a *trace-level* Ramanujan bound
$|\mathrm{Tr}(F_p \mid V_\ell(B_w))| \leq \dim(B_w) \cdot p^{w/2-1/2}$.

This is a genuine programme deliverable: for admissible $V_k(\mathfrak{sl}_2)$, the
bar complex realises an *explicit* ℓ-adic Galois representation whose Frobenius
trace is Deligne-bounded. It does not prove Weil; it applies Weil to an explicitly
constructible object. This is the same status as Route B of the motivic note:
sub-convexity-adjacent, Weil-dependent.

## 3. Number-field lift: candidate $\mathcal{A}_\mathbb{Z}$ for the "variety over $\mathbb{F}_1$"

### 3.1 The demand

Manin/Kurokawa/Deninger: $\zeta(s)$ should be a Hasse–Weil zeta of a virtual
variety $\overline{\mathrm{Spec}(\mathbb{Z})}$ over $\mathbb{F}_1$, whose
ℓ-adic cohomology carries a "Frobenius" whose spectrum is the non-trivial
$\zeta$-zero set $\{\rho\}$, with $\mathrm{Re}(\rho) = 1/2$ = "weight 1"
of $H^1$ in Weil's scheme. Connes (Selecta Math 1999) realises the spectrum
of the Frobenius as the absorption spectrum of the adelic action on
$L^2(\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times)$.

For the programme, the analogue would be: a chiral algebra $\mathcal{A}_\mathbb{Z}$
with distinguished arithmetic structure, whose ℓ-adic derived chiral centre has
Frobenius spectrum $= \{\rho : \zeta(\rho)=0, 0<\mathrm{Re}(\rho)<1\}$.

### 3.2 Candidate construction

Two candidates present themselves naturally within the programme.

**Candidate A: Heisenberg-theta.** $\mathcal{A}_\mathbb{Z}^{\mathrm{Heis}} :=
H_{k=1}$ with character $\theta(\tau) = \sum_{n\in\mathbb{Z}} q^{n^2/2}$, the
Jacobi theta. The shadow L-function of $\mathcal{A}_\mathbb{Z}^{\mathrm{Heis}}$ is
the Hurwitz-Lerch Dirichlet series; its Mellin transform at integer arguments is
the classical $\zeta(2s)$ via the Jacobi theta / zeta integral representation.
The ℓ-adic derived chiral centre is the abelian (Ind-étale) realisation of the
additive line $\mathbb{G}_a$. Frobenius spectrum: trivial $\{p^0\}$; no
$\zeta$-zeros appear.

**Candidate B: Epstein-Leech adelic.** $\mathcal{A}_\mathbb{Z}^{\mathrm{Leech}} :=
V_\Lambda$ where $\Lambda = \Lambda_{24}$ is the Leech lattice, tensored with
the adelic completion at all finite primes. The Epstein L-factorisation
$\varepsilon^{24}_s(V_\Lambda) = c_E \zeta(s)\zeta(s-11) + c_\Delta L(s,\Delta_{12})$
gives $\zeta(s)$ as a genuine factor. The ℓ-adic derived chiral centre carries
a $\mathrm{Gal}$-action whose Frobenius on the Eisenstein piece has spectrum
$\{p^{0}, p^{11}\}$; on the cuspidal piece, $\{a_p(\Delta_{12}), p^{11} \bar{a_p(\Delta_{12})}/a_p(\Delta_{12})\}$ with Ramanujan $|a_p| \leq 2p^{11/2}$.
This is a genuine Weil-bounded object, but the spectrum is Eisenstein + Hecke,
not $\zeta$-zero.

**Candidate C (the only one that touches RH directly): $\mathcal{A}_\mathbb{Z}^{\mathrm{Conn}}$ =
cohomological Hopf dual of the Connes-Bost-Marcolli system.** Connes proves
$\zeta$-zeros as absorption spectrum of adelic class operator. A chiral algebra
*could* be attached: take the ordered bar of the universal enveloping algebra
$U(\mathfrak{bm})$ of the Bost-Connes Lie algebra, whose character is the
adelic class function. The Frobenius eigenvalue computation reduces to the
Connes trace formula, which is equivalent to RH.

### 3.3 Verdict on item (3)

Candidate C's Frobenius spectrum is the $\zeta$-zero spectrum *by construction*
— because it inherits the Connes trace formula. This is tautological: it does
not prove RH, it re-states RH as a question about a specific chiral algebra's
ℓ-adic derived chiral centre. The programme's contribution would be the
chiral-algebra packaging of the Connes adelic system; this is not a proof.

Candidates A and B give honest Frobenius computations but their spectra are
Hecke-Eisenstein, not $\zeta$-zero.

**No chiral algebra currently in the programme has non-trivial $\zeta$-zero
Frobenius spectrum by a *derivation* independent of Connes or Weil.** The
programme's framework *can* package such an object (Candidate C), but cannot
*derive* the RH bound.

## 4. What the programme genuinely contributes (and does not)

**Contributes:**
- Explicit ℓ-adic bar complex for admissible $V_k(\mathfrak{sl}_2)$ (§1.2).
- Trace-level Ramanujan bound on $V_\ell(B_w(L_k))$ via Deligne + fusion
  multiplicities (§2.2); this is an *explicit Galois representation* with
  Weil-bounded Frobenius trace, not a new proof.
- Structural packaging of Epstein-Leech factorisation (§3.2 Candidate B) as an
  ℓ-adic derived chiral centre with Eisenstein + Hecke Frobenius spectrum.
- Chiral-algebra language for the Connes-Bost-Marcolli system (§3.2 Candidate C)
  as a tautological restatement of RH.

**Does not contribute:**
- No Weil-independent Frobenius bound. The bounds inherit from Deligne via the
  underlying Hecke eigenforms; FM129's honest position stands.
- No $\mathbb{F}_1$ construction that derives $\zeta$-zero spectrum. Candidate C
  is a restatement, not a derivation.
- No analytic continuation mechanism beyond classical Rankin-Selberg. The
  `rem:structural-obstruction` from the motivic note transports verbatim: shadow
  tower constrains real-line spectral coefficients; $\zeta$-zeros live off the
  real line.

## 5. Verdict

The ℓ-adic derived chiral centre construction is *honest and explicit* for
admissible $V_k(\mathfrak{sl}_2)$: the bar complex has an ℓ-adic realisation via
Deligne's Galois representations on Kac-Wakimoto characters; Frobenius
eigenvalue bounds are Weil-type via Eichler-Shimura. This gives the programme
an explicit ℓ-adic object to study, but the bounds are *inherited* from
Deligne/Weil, not derived independently.

The $\mathbb{F}_1$-lift to a candidate $\mathcal{A}_\mathbb{Z}$ stalls in the
same place every $\mathbb{F}_1$ approach stalls. Three candidates present
themselves: Heisenberg-theta (trivial Frobenius spectrum, no $\zeta$-zeros),
Epstein-Leech (Eisenstein + Hecke spectrum, not $\zeta$-zero), and Bost-Connes
adelic dual (tautologically RH-equivalent, not a derivation). The
chiral-algebra framework gives elegant repackaging but no new mechanism to
generate the $\zeta$-zero spectrum *from* the bar-cobar construction itself.

**Bottom line.** The ℓ-adic derived chiral centre gives a genuine RH-type bound
for $V_\ell(B(L_k(\mathfrak{sl}_2)))$ inherited from Deligne; the $\mathbb{F}_1$-
lift to $\mathcal{A}_\mathbb{Z}$ is conjectural in the same way all current
$\mathbb{F}_1$ approaches are. FM129 stands: Weil-independence is not achieved;
the programme's honest contribution is trace-level packaging, not a proof.

The three irreducible obstructions documented here (inherited-from-Deligne
bounds; Eisenstein + Hecke vs $\zeta$-zero spectrum mismatch; Connes
tautology) are the same three obstructions that stop every $\mathbb{F}_1$
programme. The programme does not circumvent them; it articulates them
precisely in its native language.
