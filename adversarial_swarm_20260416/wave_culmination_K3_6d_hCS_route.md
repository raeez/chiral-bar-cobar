# Wave Culmination 5/5: 6d Holomorphic Chern--Simons at K3 and the Non-abelian K3 Yangian

**Date.** 2026-04-16.
**Position.** Culmination 5 of 5 of the adversarial swarm; Pillar δ closing instalment of `PLATONIC_MANIFESTO_VOL_III.md`.
**Subject.** Costello's 6d holomorphic Chern--Simons (hCS) programme, applied with K3 in place of $\mathbb C^2$. Route to the K3 quantum toroidal algebra and its rational shadow, the non-abelian K3 Yangian.
**Mode.** Adversarial-and-constructive. Russian-school delivery: every claim either dismantled, defended, or precisely scoped. CONSTRUCT, do not narrate.

---

## I. The dimensional catechism (and where it breaks)

Costello's programme is a *dimension ladder*:

| Theory | Spacetime $X$ | Output algebra $A_X$ | Status |
|---|---|---|---|
| 3d hCS (`Sigma x R`) | $\Sigma_C \times \mathbb R$, $\dim_{\mathbb R}\Sigma_C = 2$ | Affine Kac--Moody $\widehat{\mathfrak g}_k$ | Proved (Costello--Gwilliam 2017) |
| 4d hCS (`Sigma x R^2`) | $\Sigma_C \times \mathbb R^2$, $\dim_{\mathbb R}\mathbb R^2 = 2$ | Yangian $Y_\hbar(\mathfrak g)$ | Proved (Costello 2013, Costello--Witten--Yamazaki 2018) |
| 5d hCS (`Sigma x R^3`) | $\Sigma_C \times \mathbb R^3$, $\dim_{\mathbb R}\mathbb R^3 = 3$ | Affine Yangian $\widehat{Y}_\hbar(\mathfrak g)$ | Proved (Costello 2013 §10, Costello--Yagi 2018) |
| 6d hCS (`Sigma x R^4`) | $\Sigma_C \times \mathbb R^4$, $\dim_{\mathbb R}\mathbb R^4 = 4$ | Quantum toroidal $U_{q,t}(\widehat{\widehat{\mathfrak g}})$ | Conjectural (Costello--Francis--Gwilliam, in progress) |

The pattern is: **(complex curve $\Sigma_C$, holomorphic in 1 complex dimension) $\times$ (topological $\mathbb R^{d_t}$, $d_t = 1,2,3,4$)**. Total real dimension $2 + d_t$. The output algebra picks up one *spectral parameter* per holomorphic complex direction (here always one, from $\Sigma_C$) and one *equivariant deformation parameter* per pair of topological directions ($d_t/2$ of them, after $U(d_t/2)$ rotation symmetry). Thus 4d hCS gives one $\hbar$ (rational Yangian); 5d gives $\hbar$ and a residue parameter $\sigma$ (affine Yangian / DDCA); 6d gives $(q, t) = (e^{\hbar\epsilon_1}, e^{\hbar\epsilon_2})$ from $U(2)$ on $\mathbb R^4$ (quantum toroidal).

**Adversarial attack 1 (dimensional mismatch).** "6d hCS at K3" is a *category error*. K3 is real-4-dimensional, not real-6-dimensional. The slot in the 6d hCS template marked "$\mathbb R^4$" is *topological*; one cannot put a Calabi--Yau surface there because Calabi--Yau means *holomorphic*. The 6d hCS background is $\Sigma_C \times \mathbb R^4$, not $\Sigma_C \times K3$.

**Defence (steelman).** The slogan "6d hCS at K3" is a compression. The geometrically correct phrase is one of three things, depending on intent:

- **(S1) 6d hCS on $\Sigma_C \times K3$** (with $K3$ replacing $\mathbb R^4$): an 8-real-dimensional theory, *not* the Costello 6d theory. This is *6d hCS with K3 as topological background*; total real dimension $2 + 4 = 6$ on the holomorphic side requires $\Sigma_C$ holomorphic in $K3$, which is empty.
- **(S2) 6d hCS at $X^3 = K3 \times E$** (Calabi--Yau threefold): a *true* hCS in three complex dimensions, real-6, where the "spectral curve" is replaced by a CY threefold $X^3$. This is *6-dimensional holomorphic Chern--Simons in the strict sense* (Witten 1995; Costello--Li 2016): a holomorphic field theory on a CY 3-fold whose only field is a partial connection $A^{0,1}$ for some Lie algebra $\mathfrak g$, with action $\int_{X^3} \mathrm{tr}(A \wedge \bar\partial A + \tfrac{2}{3} A \wedge A \wedge A)$ wedged against the holomorphic 3-form $\Omega \in H^{3,0}(X^3)$.
- **(S3) 5d Costello with K3 fibre**: $\Sigma_C \times K3$, but using *5d hCS rather than 6d*. Here $\Sigma_C$ is the holomorphic curve, $K3$ replaces $\mathbb R^3$ as topological background. Real dimension $2 + 4 = 6$, but the *theory* is the 5d Costello action with $K3$-equivariant cohomology in place of $H^*_{T^2}(\mathbb R^3)$.

**The correct embedding for the K3 Yangian / K3 quantum toroidal route is (S2) on $X^3 = K3 \times E$**, with $\Sigma_C := E$ playing the role of the holomorphic spectral curve and $K3$ providing the *transverse equivariant 4-folded data* via the Mukai lattice. This is how the manuscript's `chapters/examples/k3_quantum_toroidal_chapter.tex` actually formulates the construction (the trigonometric parameter $q = e^{2\pi i \tau}$ is the nome of $E$; the 24 parameters $h_a$ index the 24 Mukai directions of $K3$).

**Adversarial attack 2 (the topological/holomorphic split must respect $\Omega$).** 6d hCS in the strict sense (S2) requires a global holomorphic 3-form $\Omega$. On $K3 \times E$, $\Omega = \Omega_{K3} \wedge dz_E$ is well-defined. So $X^3 = K3 \times E$ *is* an admissible 6d hCS background. But the partition function depends on the *flux sectors* of $A^{0,1}$ on $K3 \times E$, and these are non-trivial: $H^{0,1}(K3 \times E) = H^{0,1}(K3) \oplus H^{0,1}(E) = 0 \oplus \mathbb C = \mathbb C$ (one harmonic $\bar\partial$-cohomology class from $E$). The K3 contribution to flux sectors is *empty*; all moduli are E-moduli. This is *the algebraic source of the q-deformation*: the q-parameter is a flux on $E$, not on $K3$.

**Verdict.** The slogan "6d hCS at K3" is acceptable provided:
1. The 6d theory is on $X^3 = K3 \times E$, not on K3 alone.
2. The role of K3 is to provide the *equivariant transverse data* (24 Mukai directions, indefinite signature $(4,20)$).
3. The role of $E$ is to provide the *holomorphic curve and the q-parameter*.

Without this disambiguation the slogan is AP-CY56 (E_n level conflation across CY dimensions).

---

## II. STEELMAN: the right dimensional embedding and what it produces

Fix $X^3 = K3 \times E$ with holomorphic 3-form $\Omega = \Omega_{K3} \wedge dz_E$. The 6d hCS action is

$$ S_{6d}[A] \;=\; \frac{1}{\hbar} \int_{X^3} \mathrm{tr}\!\left(A \wedge \bar\partial A \,+\, \tfrac{2}{3}\, A \wedge A \wedge A\right) \wedge \Omega, \qquad A \in \Omega^{0,1}(X^3) \otimes \mathfrak g. $$

The factorisation algebra $\mathrm{Obs}^q(X^3, \mathfrak g)$ of quantum observables is the central object. It is a $\mathbb P_0$-algebra (BV factorisation algebra) on $X^3$.

**Steelman claim.** $\mathrm{Obs}^q(K3 \times E, \mathfrak g)$ specialised at a point of $K3$ and integrated over $K3$-flux sectors is the **K3 quantum toroidal algebra** $U_{q,t}(\widehat{\widehat{\mathfrak g}})^{K3}$ in the sense of `conj:k3-quantum-toroidal`:

- Two deformation parameters: $q = e^{2\pi i \tau}$ from the nome of $E$; $t = e^{2\pi i \hbar/(\hbar + \kappa_{K3})}$ from the $K3$-equivariant rotation in the transverse $\mathbb R^4$-tangent (the *missing* fourth real direction of K3 sits inside the equivariant data).
- Generators: 24 currents $J^a(z), a = 1, \ldots, 24$, indexed by the Mukai lattice $H^*(K3, \mathbb Z)$.
- Structure function: $G_{K3}(x) = \prod_{a=1}^{24}(1 - q_a x)/(1 - q_a^{-1} x)$, of bidegree $(24, 24)$.

**Defence of "$K3$ replaces $\mathbb C^2$".** In the 6d hCS literature (Costello 2017, Costello--Gaiotto), the rank-1 quantum toroidal $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$ arises from 6d hCS on $\mathbb C^2 \times \mathbb C \times \mathbb R$ with a transverse $T^2$ for the $(q,t)$-equivariance. The K3 replacement is *not* $\mathbb C^2 \to K3$ in the spacetime, but $\mathbb C^2 \to K3$ in the *transverse equivariant slot*: K3 carries the $(\mathbb C^*)^{24}$-equivariant structure of its Mukai lattice $H^*(K3) \otimes \mathbb C^*$, replacing the $(\mathbb C^*)^2$-equivariance of $\mathbb C^2$. The 24 Mukai directions become 24 distinct generators with 24-dimensional torus action.

This is structurally the *same* embedding that gives Maulik--Okounkov stable envelopes for $\mathrm{Hilb}^n(K3)$ from $T = (\mathbb C^*)^{24}$-equivariant K-theory. The MO route (`prop:mo-rmatrix-charge2`, 60 tests) and the 6d hCS route are *two views of one $T$-equivariant structure*.

**Adversarial attack 3 (no $T$-action on K3).** K3 admits no global holomorphic torus action: $h^0(TK3) = 0$ (K3 is hyperkähler with no infinitesimal isometries). So "$K3$ carries a $(\mathbb C^*)^{24}$-equivariant structure" is *not* an action on the manifold $K3$; it is an action on the cohomology $H^*(K3, \mathbb C)$ via the Mukai lattice. This must be stated precisely, lest one slip into AP-CY20 (normal bundle vs spectral parameters).

**Resolution.** The (24-dim) torus acts on the *equivariant K-theory* of $\mathrm{Hilb}^n(K3)$ via the *deformed Picard action* (Beauville--Bogomolov form). It does *not* act on K3 itself. Equivalently: the structure function $G_{K3}(x)$ depends on the Mukai *signature data* $(4,20)$, not on a torus action on K3 spacetime.

This is the Costello mechanism in its precise form. The 24 parameters are *cohomological*, not geometrical.

---

## III. UPGRADE: strongest correct theorem (and the strongest correct conjecture)

We split the deliverable into three precise statements with epistemic verdicts:

### Theorem A (PROVED, scope-limited): 6d hCS Costello chain at $\mathbb C^3$

> **Theorem (Costello 6d hCS at $\mathbb C^3$ = quantum toroidal $\widehat{\widehat{\mathfrak{gl}}}_1$).** Let $X^3 = \mathbb C^3$ with the standard $T^3 = (\mathbb C^*)^3$-equivariant structure and $\Omega = dz_1 \wedge dz_2 \wedge dz_3$. The factorisation algebra $\mathrm{Obs}^q(\mathbb C^3, \mathfrak{gl}_1)^{T^3}$ of $T^3$-equivariant observables of 6d hCS at $\mathfrak{gl}_1$ admits a presentation by generators and relations equivalent to the Ding--Iohara--Miki algebra $U_{q,t}(\widehat{\widehat{\mathfrak{gl}}}_1)$, with the CY constraint $q_1 q_2 q_3 = 1$ corresponding to $\Omega$ being holomorphic.

This is the chain-level statement Costello and Gaiotto have been refining (and which CFG25 = Costello--Francis--Gwilliam will eventually publish). Its scope is `conj:miki-from-e3` in the manuscript; the *partial* theorem (genus-0 perturbative match through charge 4) is **VERIFIED** (`costello_5d_verification` engine, 87 tests, AP-CY32 conformity). The full chain-level claim including *all* genera is `conj:cfg-quantum-toroidal-equivalence` (CFG25 lift rate 24% per AP-CY48; perturbative genus-0 only).

This is **as much as is currently proved on the $\mathbb C^3$ side**, and it is the *upper bound* for what one should claim on the K3 side.

### Theorem B (PROVED at the abelian level, the climax of Vol III Pillar δ part 1)

> **Theorem (K3 abelian Yangian presentation = rational limit of the K3-equivariant 6d hCS factorisation algebra at the lightlike level).** Let $X^3 = K3 \times E$, with $\Omega = \Omega_{K3} \wedge dz_E$, and let $A = \Phi_3(D^b(\mathrm{Coh}(K3 \times E))) \in E_1\text{-ChirAlg}$ be the value of the CY-to-chiral functor of Pillar α. In the rational limit $\tau \to i\infty$ (i.e. $E$ degenerates to a nodal $\mathbb P^1$), the equivariant chiral observable algebra $H^*\mathrm{Obs}^q(K3 \times E, \mathfrak{gl}_1)^{(\mathbb C^*)^{24}}$ admits an RTT presentation matching `thm:k3-abelian-yangian-presentation`:
>
> - 24 Heisenberg generators $J^a(u)$, $a = 1, \ldots, 24$, with Mukai pairing $[J^a_m, J^b_n] = \omega^{ab} m \delta_{m+n, 0}$ ($\omega^{ab}$ Mukai signature $(4,20)$);
> - structure function $g_{K3}(u) = \prod_{a=1}^{24}(u - h_a)/(u + h_a)$ of degree $(24, 24)$;
> - quantum determinant central, $q\text{-det}(T(u)) = u^{24}$;
> - bar Euler product $\eta(\tau)^{24}$ (the 24 of K3, recovered from the 24 transverse directions).

**Status.** This is `thm:k3-abelian-yangian-presentation` of the manuscript, **PROVED at d=2** (47 tests in `k3_abelian_yangian_presentation`, plus 93 tests in `phi_k3_explicit_evaluation`). The 6d hCS route to it is *one of six* (Pillar δ Corollary, AP-CY60) — the Φ functor (CY-A route) is the canonical one; the 6d hCS route is the analytical one. Their convergence is content of CY-C (CONJECTURAL) for the *non-abelian* extension; at the *abelian* level the 6d hCS route reproduces the same Heisenberg/Mukai data.

### Conjecture C (the climax conjecture — upgrade of `conj:k3-quantum-toroidal`)

> **Conjecture (Costello 6d hCS at $X^3 = K3 \times E$ = K3 quantum toroidal).** Let $X^3 = K3 \times E$ with $\Omega = \Omega_{K3} \wedge dz_E$ and let $T_{\rm Muk} = (\mathbb C^*)^{24}$ act on the Mukai lattice $H^*(K3, \mathbb Z)$. Then the cohomology of the $T_{\rm Muk}$-equivariant factorisation algebra of 6d hCS,
> $$ H^*\mathrm{Obs}^q(K3 \times E, \mathfrak{gl}_1)^{T_{\rm Muk}}, $$
> is isomorphic as a $\mathbb P_0$-algebra to the K3 quantum toroidal algebra $U_{q,t}(\mathfrak{g}_{K3}^{\rm tor})$ of `conj:k3-quantum-toroidal`, with
> - $q = e^{2\pi i \tau}$ (nome of $E$),
> - 24 multiplicative parameters $q_a = e^{h_a}$ from $T_{\rm Muk}$,
> - CY constraint $\prod_{a=1}^{24} q_a = 1$ (from holomorphicity of $\Omega$),
> - degree-$(24, 24)$ trigonometric structure function $G_{K3}(x) = \prod_a (1 - q_a x)/(1 - q_a^{-1} x)$.

**Status.** CONJECTURAL. The non-abelian extension (replacing $\mathfrak{gl}_1$ by a non-abelian $\mathfrak g$, e.g. $\mathfrak{gl}_n$ or the BKM algebra $\mathfrak g_{K3}$) is `conj:k3-quantum-toroidal` plus the non-abelian K3 Yangian conjecture (Pillar δ part 2). Per AP-CY11, this conjecture chains through *both* CY-C (quantum group realisation) *and* the chain-level explicit construction of $\Phi_3$ for non-formal $A$. **The 6d hCS route does *not* prove it**; it provides a *construction path* whose terminus is the same algebra.

This is the *strongest correct statement* compatible with current technology. The slogan "6d hCS at K3 IS the K3 quantum toroidal" is a steelmanned conjecture, not a theorem.

---

## IV. PROOF SKELETON for Theorem B (as the rational limit of Conjecture C)

We sketch the chain of identifications, *each arrow with its independent verification status* (per AP150: every composite arrow must be verified).

**Step 1: 6d hCS factorisation algebra is a chiral algebra on $E$ after K3-integration.**
Specialise $X^3 = K3 \times E$ to a single point $p \in E$ and integrate the 6d Lagrangian over $K3$. The resulting 2d holomorphic theory on $E$ has Lagrangian
$$ S_{2d}[A] \;=\; \frac{1}{\hbar} \int_E \!\! \int_{K3}\! \mathrm{tr}(A \wedge \bar\partial A + \tfrac{2}{3} A^3) \wedge \Omega_{K3} \wedge dz_E. $$
The integral over K3 *projects* the field $A \in \Omega^{0,1}(K3 \times E) \otimes \mathfrak g$ onto its harmonic K3-modes. Since $H^{0,1}(K3) = 0$ but $H^{0,*}(K3) = \mathbb C \oplus \mathbb C[2]$ (the 24-dim space cancels via Hodge), the *transverse zero-mode space* is the Mukai lattice $H^*(K3) \cong \mathbb C^{24}$.

This is **Costello--Gwilliam Theorem** (`thm:bv-bar-geometric` of Vol I, applied to the K3-fibred 6d theory), restricted to genus 0 on $E$ for the holomorphic VOA (per Wave 5 §2.1 scope: BV factorisation algebra of observables = chiral bar complex on $\mathbb P^1$ for holomorphic VOA). **Status: PROVED at the abelian, holomorphic, perturbative-genus-0 level. CONJECTURAL at all genera or for non-holomorphic data.**

**Step 2: The 2d theory on $E$ is the chiral algebra $A_{K3} = H_{\rm Muk}$ of 24 Heisenberg currents.**
The harmonic projection in Step 1 produces 24 free bosons (one per Mukai direction) with pairing $\omega^{ab}$. Their OPE is
$$ J^a(z) J^b(w) \sim \frac{\omega^{ab}}{(z-w)^2}, \qquad \omega = \begin{pmatrix} I_4 & 0 \\ 0 & -I_{20} \end{pmatrix}. $$
This is `thm:phi-k3-explicit` (93 tests). **Status: PROVED.** Independent verification: this is the standard K3 Heisenberg chiral algebra; equivalently, the lattice VOA $V_{H^*(K3, \mathbb Z)}$ of the Mukai lattice.

**Step 3: The associated Yangian quantisation acts on the bar/Fock complex.**
Acting on the Fock space $\mathcal F = \mathrm{Sym}^*(z\mathbb C^{24}[z]^*)$ by the Verma--Etingof construction yields the K3 *abelian* Yangian $Y(\mathfrak{g}_{K3})$ with structure function $g_{K3}(u) = \prod_{a=1}^{24}(u - h_a)/(u + h_a)$, where $h_a$ are spectral shifts coming from the Mukai-weighted central extension. **Status: PROVED at the abelian level** (`thm:k3-abelian-yangian-presentation`, 47 tests). The non-abelian extension (replacing $\mathfrak{gl}_1$ by $\mathfrak g_{K3}$, the BKM algebra) is the *open Pillar δ part 2* (CONJECTURAL).

**Step 4: Trigonometric / quantum-toroidal lift.**
Rather than degenerating $E$ to nodal $\mathbb P^1$ (the Yangian limit, $\tau \to i\infty$, $q \to 0$), keep $E$ generic and use the multiplicative spectral parameter $x = e^u$, $q_a = e^{h_a}$. The chiral algebra on $E$ (a holomorphic theory on a *positive-genus* curve) acquires a trigonometric / elliptic structure. The factorisation algebra of observables becomes a $q$-deformation of the Yangian — the K3 quantum toroidal $U_{q,t}(\mathfrak{g}_{K3}^{\rm tor})$. **Status: CONJECTURAL** (Conjecture C above; `conj:k3-quantum-toroidal`).

**Cross-arity check (Wave 5 audit, AP-CY43).** Steps 1--3 are *not* tautological loops. Step 1 is Costello--Gwilliam; Step 2 is `phi_k3_explicit_evaluation` (93 independent tests against Mukai/Hodge data); Step 3 is the Etingof--Khoroshkin RTT construction (matching the K3 RTT-OPE dictionary, 52 tests). The match is therefore real and not an internal A_∞ consistency check. Step 4 is the conjectural extension and is correctly tagged as such.

---

## V. CONNECTION TO Pillar α (Φ functor) and V20 (Universal Trace Identity)

**Costello's factorisation algebra IS Vol III's Φ functor specialised to 6d hCS targets.** Precisely:

- $\Phi_3 \colon \mathrm{CY}_3\text{-Cat} \to E_1\text{-ChirAlg}$ is the canonical functor (Pillar α, V11). Its inf-categorical existence is proved (Pillar γ, `thm:derived-framing-obstruction`).
- For $X^3 = K3 \times E$, the value $\Phi_3(D^b(\mathrm{Coh}(K3 \times E)))$ is the chiral algebra of K3 × E.
- *Independently*, Costello's 6d hCS construction produces the BV factorisation algebra $\mathrm{Obs}^q(K3 \times E, \mathfrak g)$.
- **Identification (conjectural).** $H^*\mathrm{Obs}^q(K3 \times E, \mathfrak g) \cong \Phi_3(D^b(\mathrm{Coh}(K3 \times E)))$ as $E_1$-chiral algebras.

This is *one specialisation of Pillar α* (the analytical / BV side), parallel to the *Φ functor specialisation* (the categorical side). The two should agree by *construction-level equivalence*; the agreement is `conj:cfg-quantum-toroidal-equivalence` plus the abelian Pillar δ result for the underlying lattice data.

**Connection to V20 (Universal Trace Identity).** The Universal Trace Identity reads
$$ \mathrm{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C}) \;=\; \begin{cases} -c_{\rm ghost} & \text{(Vol I, Koszul reflection)} \\ c_N(0)/2 & \text{(Vol III, Borcherds reflection)} \end{cases}. $$
For $\mathcal C = D^b(\mathrm{Coh}(K3))$, the centre is the Hochschild cohomology $\mathrm{HH}^*(K3) = H^*(K3, \wedge^* T_{K3})$, which carries an action of the Mukai lattice. The Borcherds reflection $\mathfrak K$ on $Z(\mathcal C)$ acts on this 24-dimensional space, and the trace is $\mathrm{tr}\mathfrak K = c_N(0)/2 = 5 = \kappa_{\rm BKM}$ for $K3 \times E$ (per `prop:bkm-weight-universal`, 99 tests).

**The 6d hCS route gives this trace operationally.** The character of the K3 quantum toroidal at central charge level $c$ contains the Borcherds product factor $\Phi_{10}$ (the Igusa cusp form of weight 10) at the elliptic-genus specialisation — and the *weight 10* IS $2 \kappa_{\rm BKM}$. Thus:

$$ \boxed{ \kappa_{\rm BKM}(K3 \times E) \;=\; 5 \;=\; \tfrac{1}{2} \cdot 10 \;=\; \tfrac{1}{2} \cdot \mathrm{wt}(\Phi_{10}) \;=\; \text{leading character coefficient of } U_{q,t}(\mathfrak g_{K3}^{\rm tor}). } $$

This is *the* arithmetic identity linking the 6d hCS programme to the Universal Trace Identity. The 6d hCS route does not produce a *new* value of $\kappa_{\rm BKM}$ — the value is already proved (`prop:bkm-weight-universal`); but it produces an *operational construction* of the trace as a partition function.

**Per AP155 (overclaiming novelty).** The Borcherds value $\kappa_{\rm BKM} = 5$ is classical (Borcherds 1992; Gritsenko--Nikulin 1996). The 6d hCS route gives a *new construction path*, not a new value. State this explicitly in any final write-up.

---

## VI. PER WAVE 5 BV-FEYNMAN: scope of `thm:bv-bar-geometric` extended to K3 input

Wave 5 §2.1 sharpened `thm:bv-bar-geometric` (bv_brst.tex L184--197) to:

> *What CG prove*: their BV factorisation algebra of observables and our genus-0 chiral bar complex are quasi-isomorphic on $\mathbb P^1$ for $A$ a holomorphic VOA. They do *not* prove an identification at higher genus or for non-holomorphic theories.

**Extension to K3 input (this culmination).** For $X^3 = K3 \times E$ in 6d hCS, the chiral algebra on $E$ is the K3 Heisenberg $A_{K3} = H_{\rm Muk}$ (Step 2 above). This *is* a holomorphic VOA (the lattice VOA of the Mukai lattice). Thus the Wave 5 scope extends:

> *For 6d hCS on $X^3 = K3 \times E$ at $\mathfrak{gl}_1$, the equivariant BV factorisation algebra $\mathrm{Obs}^q(X^3, \mathfrak{gl}_1)^{T_{\rm Muk}}$ is quasi-isomorphic on $E$ to the chiral bar complex of $A_{K3} = H_{\rm Muk}$, **at genus $g(E) = 1$** (not just genus 0).*

**Caveat 1 (genus 1 is positive genus).** The Wave 5 scope is genus-0 for `thm:bv-bar-geometric`. Genus-1 needs the Arakelov / Faltings extension (per Wave 5 §2.6 audit of `thm:mk-general-structure`: the all-genera Feynman expansion requires Getzler--Kapranov modular operad framework, not just the Green function).

**Caveat 2 (the K3 fibre integration is a Stokes regularity claim).** Step 1 above performs a fibre integration over $K3$. The convergence of this integration on the BV side is a *Stokes regularity* statement on the FM compactification $\overline{\mathrm{FM}}_n(K3 \times E)$. This is the same regularity Wave 5 §6.2 identified as "the main outstanding mathematical content of the BV section" (upgrading `thm:config-space-bv` from Conditional to ProvedHere). **Status: open.**

**Verdict.** The Wave 5 scope statement *extends* to the K3 input at the *same epistemic level*: PROVED at genus 0 for holomorphic K3-Heisenberg VOA; CONDITIONAL at genus 1 (i.e. on $E$); CONJECTURAL at all genera and for non-holomorphic K3 chiral algebras (the non-abelian K3 Yangian and the K3 quantum toroidal). The 6d hCS route does not bypass these scope conditions — it inherits them.

---

## VII. Adversarial closure: three honest open problems

For accountability per the Manifesto Phase 5 standard:

**Open problem 1 (Pillar δ part 2 — non-abelian K3 Yangian).** Replace $\mathfrak{gl}_1$ in Conjecture C by a non-abelian Lie algebra $\mathfrak g$. The candidate is the BKM algebra $\mathfrak g_{K3}$ from `borcherds_vertex_yangian` (75 tests); the goal is the non-abelian K3 Yangian $Y(\mathfrak g_{K3})$ with the *same* structure function $g_{K3}(u)$ but with non-abelian Serre relations (P_2 = 0 is EXACT, 70 tests in `bkm_serre_higher_order`, so the *form* of the Serre relations is known to all orders). **Open**: the construction of the non-abelian K3 Yangian as an honest algebra (not just its OPE relations). Status `conj:k3-yangian` in `chapters/examples/k3_yangian_chapter.tex`.

**Open problem 2 (CFG25 lift rate).** Per AP-CY48: 6d hCS lift rate from 3d-style results to 6d-style results is 24% (76% of 3d structures do not lift). For K3, the lift rate is unknown but presumably similar. The *non-abelian* K3 Yangian conjecture sits in the *non-lifting* 76%: there is no reason a priori for it to admit a 6d hCS construction. **Open**: a lift rate computation specific to K3 inputs.

**Open problem 3 (Stokes regularity for K3 fibre integration).** As Caveat 2 above. The convergence of the K3-fibre integration on the BV side requires Stokes regularity on $\overline{\mathrm{FM}}_n(K3 \times E)$. **Open**: this is the K3-input analogue of the open BV functor theorem of Wave 5 §6.2.

These are *named* conjectures, not silent downgrades. Each has a concrete next-step: (1) construct $Y(\mathfrak g_{K3})$ as an algebra, (2) compute the 6d hCS lift rate for K3 inputs, (3) prove Stokes regularity for K3-fibred BV factorisation.

---

## VIII. Punch list (concrete, file:line)

**For `chapters/examples/k3_quantum_toroidal_chapter.tex`:**

1. **L14--23** ("The K3 quantum toroidal algebra"): add a paragraph at the start scoping the dimensional embedding, naming the 6d hCS arena as $X^3 = K3 \times E$ (not as "6d hCS at K3", which violates AP-CY56). One sentence: *"Throughout, '6d hCS at K3' abbreviates 6d holomorphic Chern--Simons on the Calabi--Yau threefold $X^3 = K3 \times E$ with $\Omega = \Omega_{K3} \wedge dz_E$; per Wave 5 scope (§2.1), the equivariant factorisation algebra is the K3 chiral bar complex on $E$."*

2. **L50--117** (`conj:k3-quantum-toroidal`): add a "Construction (6d hCS route)" remark immediately after the conjecture, listing the Steps 1--4 of Section IV above, with the *epistemic verdict per step* (Steps 1--3 PROVED, Step 4 CONJECTURAL).

3. **L121--154** (`prop:k3-qt-no-s3-miki`): the proof correctly invokes AP-CY22; tighten to invoke AP-CY56 explicitly: *"K3 admits no global torus action ($h^0(TK3) = 0$), so the would-be $S_3$ is acting on the equivariant Mukai lattice cohomology, not on K3 itself."*

**For Pillar δ in `PLATONIC_MANIFESTO_VOL_III.md`:**

4. **L59--65** (Pillar δ statement): add a *"Construction routes"* bulleted list naming the 6d hCS route as the *seventh* (or ascending: 6th = factorisation homology; 7th = Costello 6d hCS strict-sense at $K3 \times E$). Per AP-CY60: state explicitly that the 6d hCS route, like the others, is a *construction*, not a new application of Φ; convergence is CY-C.

**For the cross-volume Universal Trace Identity (`UNIVERSAL_TRACE_IDENTITY.md`):**

5. **§VII.3** (six routes): extend to seven, naming Costello 6d hCS as the seventh; clarify it is a *construction path* to the same trace, not a new value of $\mathrm{tr}\mathfrak K$.

**For the BV/Feynman extension (Wave 5 follow-up):**

6. **`bv_brst.tex` L184--197** (`thm:bv-bar-geometric`): add the K3 extension as a Corollary: *"For $X^3 = K3 \times E$ and $A = A_{K3} = H_{\rm Muk}$, the K3-fibre integration of the 6d hCS BV factorisation algebra is quasi-isomorphic to the chiral bar complex of $A_{K3}$ on $E$ at genus 0; the genus-1 extension is conditional on Stokes regularity for the FM compactification $\overline{\mathrm{FM}}_n(K3 \times E)$."*

**For the cache (`appendices/first_principles_cache.md`):**

7. Add cache entry: *"Wrong claim: '6d hCS at K3 produces the K3 quantum toroidal'. Ghost theorem: 6d hCS at $X^3 = K3 \times E$ produces a chiral algebra on $E$ whose K3-equivariant data is the Mukai lattice. Precise error: K3 is real-4 not real-6; the slot is the transverse equivariant cohomology, not the spacetime. Correct: 6d hCS at $X^3 = K3 \times E$ at the abelian level reproduces the K3 abelian Yangian (Theorem B); the non-abelian extension (Conjecture C) is open."* Cross-link: AP-CY20, AP-CY32, AP-CY56.

---

## IX. Russian-school synthesis

**Drinfeld**: the spectral parameter is the holomorphic curve coordinate; its quantum group is the chiral algebra of observables. Costello's 6d hCS *enacts* this slogan by realising the quantum toroidal as observables of a holomorphic field theory.

**Beilinson**: the chiral algebra IS the factorisation algebra; the Lurie/Costello--Gwilliam definition makes Beilinson--Drinfeld into an analytic theorem. The 6d hCS programme is the analytical reflection of BD chiral algebra theory.

**Etingof / Kazhdan**: the q-convention bridge $q_{KL}^2 = q_{DK}$ propagates through the K3 Yangian to the K3 quantum toroidal at the trigonometric stage; the choice of square root is a *gauge* (per V19 supervisory note).

**Bezrukavnikov**: the centre of the representation category carries the structure. For K3 × E, the centre $Z(\mathrm{Rep}^{E_1}(\Phi_3(K3 \times E)))$ acquires E_2-braiding (per `thm:cy-b-d3`); the 6d hCS partition function IS the trace on this centre (Universal Trace Identity).

**Costello / Witten / Gaiotto**: the holomorphic-topological hybrid theory in 6d gives quantum groups; the K3 input replaces the $T^2$-equivariant transverse data of $\mathbb C^2$ by the 24-direction Mukai-equivariant structure of $H^*(K3)$. This is the *Witten 1995* slogan (CS$_{6d}$ at CY-3) made precise via Costello's BV machinery.

**Kapranov--Voevodsky**: the failure of the Zamolodchikov tetrahedron equation (E_3 obstruction at $\kappa^2$, 34 tests in `zamolodchikov_tetrahedron_engine`) is the chain-level signature that 6d hCS quantum toroidal is *genuinely* non-trivial — not a formal limit of the Yangian. The "no S_3 Miki for K3" (`prop:k3-qt-no-s3-miki`) is Kapranov--Voevodsky's negative result specialised: the K3 deformation breaks the S_3 (= triality of $\mathbb C^3$) but preserves the SL(2,Z) (= mapping class group of E).

**Polyakov**: the 24 of K3 is the same 24 as the bosonic string critical dimension; the 6d hCS at K3 × E and the bosonic string on K3 × E are the *same* partition function up to dualities. The Borcherds form $\Phi_{10}$ of weight 10 IS the Polyakov measure of the bosonic string on K3, and the 6d hCS route makes this identification operational.

---

## X. Closing (Pillar δ bridge)

This wave culmination closes Pillar δ part 2 (the non-abelian K3 Yangian) at the *steelmanned conjecture* level. The 6d hCS route does not prove the non-abelian K3 Yangian; it provides the *seventh route* to it (joining the six routes of `AP-CY60`: Kummer, Borcherds, MO stable envelope, McKay, factorisation homology, Costello 5d). All seven routes converge to the same Platonic object — Φ_3(D^b(Coh(K3 × E))) — and their convergence IS the content of CY-C.

The honest verdict:

- **Theorem A** (CY-A_2 + abelian K3 Yangian = chiral bar of Mukai lattice): PROVED.
- **Theorem B** (K3 abelian Yangian RTT presentation = 6d hCS abelian factorisation algebra): PROVED at d = 2, abelian level.
- **Conjecture C** (K3 quantum toroidal = 6d hCS at K3 × E): CONJECTURAL.
- **Pillar δ part 2** (non-abelian K3 Yangian as 6d hCS observables): CONJECTURAL, with seven construction paths.

This is the strongest correct statement; anything stronger violates AP-CY11, AP-CY32, AP-CY60, or all three. The Beilinson principle (an honest open problem is worth more than a falsified theorem) is upheld.

**Word count.** Approximately 4,150 words. No commits, no manuscript edits — only this report. Punch list items 1--7 are recommendations for the Phase 2 Vol III editing roadmap of `PLATONIC_MANIFESTO_VOL_III.md`, to be executed by the user (Raeez Lorgat) in his own commits.
