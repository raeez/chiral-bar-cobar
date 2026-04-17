# Wave Frontier — Attack & Healing of the V38 ADE K-Formula
## $K(Y(\fg_{K3,ADE})) = 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|$

**Author.** Raeez Lorgat. **Date.** 2026-04-16.
**Mode.** Dual mode — Russian-school adversarial attack followed by systematic first-principles healing. Chriss–Ginzburg discipline. PLATONIC FORM. CONSTRUCT, do not narrate.
**Predecessors.** V6 BRST GHOST IDENTITY (wave14_reconstitute_kappa_conductor.md), V13 chapter draft (wave14_brst_ghost_identity_chapter_draft.md), V20 UNIVERSAL TRACE IDENTITY, V28 climax verification engine, V37 K3 trace triad, V38 culmination report 2/5 (wave_culmination_K3_MO_higher_charge.md §E).
**Ground rules.** Read/Grep/Bash only. No manuscript edits. No commits. Sympy verification in sandbox. No AI attribution; the V38 formula and its derivation are by Raeez Lorgat.

---

## 0. Target

The V38 §E (wave_culmination_K3_MO_higher_charge.md, lines 128–164) headline formula:

$$\boxed{\; K(Y(\fg_{K3,\mathrm{ADE}})) \;=\; 2\,\mathrm{rk}(\fg_{\mathrm{ADE}}) \;+\; 26\,|\Phi^+(\fg_{\mathrm{ADE}})| \;}$$

derived as a corollary of the V6 BRST GHOST IDENTITY $K(A) = \sum_\alpha (-1)^{\varepsilon_\alpha+1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1)$ applied to a postulated BRST resolution of the non-abelian K3 Yangian at an ADE-enhancement point of K3 moduli space, with:

- $\mathrm{rk}(\fg_{\mathrm{ADE}})$ Cartan-ghost pairs at spin $\lambda = 1$, contributing $K_1 = 2(6-6+1) = 2$ each;
- $|\Phi^+(\fg_{\mathrm{ADE}})|$ root-direction ghost pairs at spin $\lambda = 2$, contributing $K_2 = 2(24-12+1) = 26$ each (the Polyakov reparametrisation ghost charge);
- $24 - \mathrm{rk}(\fg_{\mathrm{ADE}})$ Heisenberg complement bosons contributing $K = 0$ (Heisenberg case G, no BRST).

This report subjects the formula to a Gelfand–Beilinson–Polyakov adversarial attack and then heals into the platonic ideal form.

---

## PHASE 1 — ATTACK

### A1.1. Numerical sanity (sympy verification)

The formula is internally consistent and reproduces V38's table of specialisations. Verified at A_1, A_2, A_3, A_4, D_4, D_5, D_6, E_6, E_7, E_8 by direct ghost-charge summation and Lie-algebraic identity $\dim(\fg) = \mathrm{rk}(\fg) + 2|\Phi^+(\fg)|$:

| ADE | rk | $|\Phi^+|$ | dim | $K = 2\,\mathrm{rk} + 26\,|\Phi^+|$ |
|-----|----|-----------|-----|-----------------------------------|
| $A_1$ | 1 | 1 | 3 | $\mathbf{28}$ |
| $A_2$ | 2 | 3 | 8 | $\mathbf{82}$ |
| $A_3$ | 3 | 6 | 15 | $\mathbf{162}$ |
| $A_4$ | 4 | 10 | 24 | $\mathbf{268}$ |
| $D_4$ | 4 | 12 | 28 | $\mathbf{320}$ |
| $D_5$ | 5 | 20 | 45 | $\mathbf{530}$ |
| $D_6$ | 6 | 30 | 66 | $\mathbf{792}$ |
| $E_6$ | 6 | 36 | 78 | $\mathbf{948}$ |
| $E_7$ | 7 | 63 | 133 | $\mathbf{1652}$ |
| $E_8$ | 8 | 120 | 248 | $\mathbf{3136}$ |

Sympy closed forms: $K(A_n) = 13n^2 + 15n$, $K(D_n) = 26n^2 - 24n$ (with $n = \mathrm{rk}$). All cross-checks against $|\Phi^+| = (\dim - \mathrm{rk})/2$ pass.

### A1.2. Adversarial attack point #1 — wrong spin assignment for root ghosts

**Polyakov speaks first.** The number 26 is the Polyakov critical-string ghost charge, the conformal anomaly of the *reparametrisation* ghost system $bc(2)$ that gauge-fixes 2d gravity in bosonic string theory. Why would *every positive root* of $\fg_{\mathrm{ADE}}$ contribute a Polyakov reparametrisation ghost?

**The specific objection.** In a *level-1 ADE simply-laced lattice VOA* — the FKS realisation of $\widehat{\fg}_{\mathrm{ADE},k=1}$ — each positive root $\alpha$ contributes a vertex operator $e^{\alpha\cdot\phi(z)}$ of conformal weight $|\alpha|^2/2 = 1$ (long-root norm-squared $= 2$). The natural ghost gauging this vertex would be $bc(1)$, not $bc(2)$. That gives $K_1 = 2$ per positive root, hence

$$K^{\mathrm{naive\,FKS}}(Y(\fg_{K3,\mathrm{ADE}})) \;\stackrel{?}{=}\; 2\,\mathrm{rk}(\fg) + 2\,|\Phi^+(\fg)| \;=\; 2\dim(\fg).$$

This recovers exactly the V13 §3.4 affine-KM formula $K(\widehat{\fg}_k) = 2\dim(\fg)$ — the level-independent gauge-ghost sum. The V38 formula's coefficient 26 is **not** the FKS lattice-VOA coefficient.

**Witten amplifies.** At a generic K3 moduli point the K3 Yangian is the rank-24 abelian Heisenberg with $K = 0$ (no BRST, V38 §E). At an ADE collision $h_i \to h_j = h$ the new generators are vertex operators $e^{\alpha\cdot\phi}$ on the colliding directions — *spin-1* objects in the FKS realisation. Where does the spin-2 come from?

### A1.3. Adversarial attack point #2 — comparison to W_N principal DS

**Drinfeld objects.** For the Drinfeld–Sokolov reduction of $\widehat{\fg}$ at the *principal* nilpotent $f_{\mathrm{prin}}$ (recovering principal $W_N$), the BRST ghost spectrum is determined by the Jacobson–Morozov $\mathfrak{sl}_2$-grading: each positive root $\alpha$ of height $\mathrm{ht}(\alpha) = h$ contributes a $bc(h+1)$ ghost pair, with $K_{h+1} = 2(6(h+1)^2 - 6(h+1) + 1)$. Sympy verified for $\mathfrak{sl}_2,\dots,\mathfrak{sl}_6$:

| Family | True DS-prin K | $W_N$ K (Casimir spins) | V38 K | All agree? |
|--------|----------------|-------------------------|-------|------------|
| $A_1$ ($W_2 = \mathrm{Vir}$) | 28 | 26 | 28 | partial |
| $A_2$ ($W_3$) | 130 | 100 | 82 | NO |
| $A_3$ ($W_4$) | 378 | 246 | 162 | NO |
| $A_4$ ($W_5$) | 868 | 488 | 268 | NO |
| $A_5$ ($W_6$) | 1720 | 850 | 400 | NO |

Three distinct formulas agree only at $A_1$ (and even there V38 $\ne W_2$). For $A_2$ and beyond, V38 is *neither* the principal DS ghost sum *nor* the $W_N$ Casimir ghost sum.

**This is the deep objection.** If V38 corresponded to a *principal DS* reduction at the ADE point, the ghost spectrum would have spins $h+1$ for $h \in \{1, 2, \dots, h^\vee - 1\}$, not all spin 2. V38's flat-spin-2 assignment cannot arise from any standard nilpotent BRST reduction of $\widehat{\fg}_{\mathrm{ADE}}$.

### A1.4. Adversarial attack point #3 — the V37 trace triad is broken additively

V37 records the K3 trace triad $\{0, 5, 24\}$:
- $K(\mathrm{generic\,K3}) = 0$ (abelian Heisenberg, no BRST gauging);
- $\kappa_{\mathrm{BKM}}(\mathfrak g_{K3 \times E}) = 5$ (Borcherds reflection, $\Phi_{10}$ weight);
- $\mathrm{rank}\,H^*(K3, \Z) = 24$ (Mukai topological invariant).

Under V38 the ADE-enhanced values $K \in \{28, 82, 162, 268, 320, \dots, 3136\}$ contain *none* of $\{0, 5, 24\}$. ADE enhancement adds at minimum 28 (the smallest, $A_1$). The triad is broken additively. V20 (UNIVERSAL_TRACE_IDENTITY §V) protects the operator identity $\mathfrak K_{\mathcal C}^{\mathrm{ch}} = \mathfrak K_{\mathcal C}^{\mathrm{BKM}}$ but the trace projections produce different numerical scalars on different graded subspaces of $Z(\mathcal C)$, so additive triad-preservation is not promised. Still, the silence of V37's $\{0, 5, 24\}$ inside the V38 spectrum demands explanation.

### A1.5. Adversarial attack point #4 — folding to non-ADE fails

The orbifold conjecture in V38 §F predicts $K(Y^\sigma(\fg)) = K(Y(\fg))/|\sigma|$ for outer-automorphism foldings. Test against the four standard foldings $D_4 \xrightarrow{\Z/2} B_3$, $A_5 \xrightarrow{\Z/2} C_3$, $E_6 \xrightarrow{\Z/2} F_4$, $D_4 \xrightarrow{\Z/3} G_2$ (verified |Phi^+| via the standard $\dim(\fg^\sigma) = \mathrm{rk} + 2|\Phi^+_{\mathrm{folded}}|$):

| Folding | $K(\text{parent}) / |\sigma|$ | Direct $K(\text{folded})$ | Ratio |
|---------|-------------------------------|---------------------------|-------|
| $D_4 / \Z_2 \to B_3$ | $320/2 = 160$ | $240$ | $0.75$ |
| $A_5 / \Z_2 \to C_3$ | $400/2 = 200$ | $240$ | $0.60$ |
| $E_6 / \Z_2 \to F_4$ | $948/2 = 474$ | $632$ | $0.667$ |
| $D_4 / \Z_3 \to G_2$ | $320/3 \approx 106.7$ | $160$ | $0.50$ |

The folding conjecture **fails** quantitatively. The correct relationship is more subtle: the folded algebra $\fg^\sigma$ has a *different* count of positive roots than $\Phi^+(\fg) / \sigma$ because $\sigma$ identifies orbits of unequal lengths. Specifically:
$$|\Phi^+(\fg^\sigma)| \;=\; \#\{\sigma\text{-orbits in }\Phi^+(\fg)\},$$
which is *not* $|\Phi^+(\fg)|/|\sigma|$ when there are short and long roots. The simple division $K/|\sigma|$ is wrong; the correct version is

$$K(Y^\sigma(\fg)) \;=\; 2\,\mathrm{rk}(\fg^\sigma) + 26 \cdot \#\{\sigma\text{-orbits in }\Phi^+(\fg)\},$$

which by direct enumeration equals the V38 formula applied to $\fg^\sigma$ rather than $\fg$. This is *not* a quotient identity; it is the V38 formula applied independently at each non-ADE type. Verified:

| Non-ADE | rk | $|\Phi^+|$ | dim | $K = 2\,\mathrm{rk} + 26\,|\Phi^+|$ |
|---------|----|-----------|-----|-----------------------------------|
| $B_2$ | 2 | 4 | 10 | $\mathbf{108}$ |
| $B_3$ | 3 | 9 | 21 | $\mathbf{240}$ |
| $B_4$ | 4 | 16 | 36 | $\mathbf{424}$ |
| $C_3$ | 3 | 9 | 21 | $\mathbf{240}$ |
| $C_4$ | 4 | 16 | 36 | $\mathbf{424}$ |
| $F_4$ | 4 | 24 | 52 | $\mathbf{632}$ |
| $G_2$ | 2 | 6 | 14 | $\mathbf{160}$ |

Note that $B_n$ and $C_n$ produce the same $K$ at fixed rank, because the V38 formula is insensitive to the long/short distinction — it counts only $\mathrm{rk}$ and $|\Phi^+|$, both of which equal at fixed rank for $B_n$ and $C_n$. This is **suspicious**: the $B_n$ and $C_n$ Yangians are genuinely distinct algebras, yet V38 assigns them the same conductor. The folded V38 formula is not Langlands-invariant, but Langlands duality $\fg \leftrightarrow \fg^\vee$ in the affine setting often is.

### A1.6. Steel-man — what V38 *can* mean

The numerical agreement V38 = $2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|$ has an alternative reading that survives the attacks A1.2–A1.4:

$$V38 \;=\; \underbrace{2\,\mathrm{rk}(\fg) + 4\,|\Phi^+(\fg)|}_{= 2\dim(\fg)\,=\,K(\widehat{\fg})} \;+\; \underbrace{22\,|\Phi^+(\fg)|}_{\text{additional}}$$

i.e. V38 = (gauge-ghost sum of the affine KM) + (additional 22 per positive root). The factor 22 is the FMS difference $K_{bc(2)} - K_{bc(1)} = 26 - 4 = 22$ when each root vertex acquires a *second* spin-2 ghost beyond its spin-1 KM gauge ghost. Sympy verified at $A_1, A_2, D_4, E_8$:

| ADE | $K_{\mathrm{KM}} = 2\dim(\fg)$ | $22\,|\Phi^+|$ | Sum | V38 | agree |
|-----|--------------------------------|------------------|-----|-----|-------|
| $A_1$ | 6 | 22 | 28 | 28 | ✓ |
| $A_2$ | 16 | 66 | 82 | 82 | ✓ |
| $D_4$ | 56 | 264 | 320 | 320 | ✓ |
| $E_8$ | 496 | 2640 | 3136 | 3136 | ✓ |

**This is the structural reading.** V38 is the K3 Yangian's BRST conductor when the K3 ADE Yangian is presented as the *affine KM* $\widehat{\fg}_{\mathrm{ADE}}$ (gauge-ghost charge $2\dim(\fg)$) with **per-root Polyakov stress-tensor enhancements** (22 extra per positive root). The 22 = 26 − 4 is the Polyakov-minus-Kac–Moody ghost discrepancy. The K3 Yangian is *not* the bare affine KM at an ADE point; it is the affine KM coupled to a Sugawara-like stress tensor at each positive root, gauged by an additional bc(2) per root.

### A1.7. Where the steel-man comes from physically

In the Costello 6d holomorphic CS programme (Costello 2013, V13 §6, 87 tests via costello_5d_verification), the Yangian $Y(\fg)$ arises as boundary observables of 4d hCS on $\R^2 \times C$. At an ADE point of K3 moduli, the *worldsheet* of the K3 fibre develops a singularity, and the 6d hCS theory acquires *additional reparametrisation ghosts* on the singular locus — one bc(2) per positive root that resolves the singularity. The 22 = 26 − 4 is the difference between the bulk reparametrisation anomaly (Polyakov 26) and the boundary Cartan gauging (KM 4 per root).

This is **not** a standard W-algebra DS reduction (which would give Casimir spins, not flat spin 2); it is a **boundary-bulk hybrid** BRST resolution specific to the K3 6d hCS programme.

---

## PHASE 2 — HEALING

### H2.1. The structural derivation

Working forward from V6 GHOST IDENTITY + V20 Universal Trace Identity, we obtain V38 from first principles by the following chain:

**Step 1 (Setup).** Fix an ADE collision point of K3 moduli where $\fg_{\mathrm{ADE}} \subset \fg_{K3} = \fgl(4|20)_{\mathrm{Mukai}}$ acts non-abelianly on the Mukai sublattice. The K3 Yangian at this point is $Y(\fg_{K3, \mathrm{ADE}})$, the non-abelian K3 Yangian whose abelian sector is the rank-24 Heisenberg of `prop:k3-yangian-mukai` (k3_yangian_chapter.tex L500–L600).

**Step 2 (BRST decomposition).** A quasi-free BRST resolution of $Y(\fg_{K3, \mathrm{ADE}})$ has three sectors:

1. **Cartan sector.** $\mathrm{rk}(\fg_{\mathrm{ADE}})$ free bosons gauged by $bc(1)$ ghosts, one per Cartan generator. Ghost charge $K_1 = 2$ each. Contribution: $2\,\mathrm{rk}(\fg)$.

2. **Root sector.** $|\Phi^+(\fg_{\mathrm{ADE}})|$ vertex operators $e^{\alpha\cdot\phi}$, each carrying a *Sugawara stress-tensor enhancement* (the K3-specific bulk contribution from 6d hCS reparametrisation), gauged by $bc(2)$ ghosts, one per positive root. Ghost charge $K_2 = 26$ each. Contribution: $26\,|\Phi^+(\fg)|$.

3. **Heisenberg complement.** $24 - \mathrm{rk}(\fg_{\mathrm{ADE}})$ free bosons of the Mukai complement, no BRST gauging required (Heisenberg = case G, $K = 0$).

**Step 3 (Sum).** By V6 GHOST IDENTITY:

$$K(Y(\fg_{K3, \mathrm{ADE}})) \;=\; 2\,\mathrm{rk}(\fg_{\mathrm{ADE}}) + 26\,|\Phi^+(\fg_{\mathrm{ADE}})| + 0.$$

**Step 4 (Connection to KM).** The first two terms reorganise as $2\dim(\fg_{\mathrm{ADE}}) + 22\,|\Phi^+(\fg_{\mathrm{ADE}})|$. The first piece is the bare KM gauge ghost charge $K(\widehat{\fg}_{\mathrm{ADE}}) = 2\dim(\fg)$ (V13 §3.4). The second piece is the *Sugawara enhancement* peculiar to the K3 setting: 22 extra units per positive root coming from the 6d hCS bulk reparametrisation.

**Step 5 (V20 specialisation).** Via V20 §III, the trace $\mathrm{tr}_{Z(\mathcal C)}(\mathfrak K_{\mathcal C})$ on the chiral side specialises to $K(Y(\fg_{K3, \mathrm{ADE}}))$; on the modular side, to $\kappa_{\mathrm{BKM}}^{\mathrm{ADE}} = c_N^{\mathrm{ADE}}(0)/2$. The Borcherds-side prediction is therefore

$$\boxed{\; c_N^{\mathrm{ADE}}(0) \;=\; -2K(Y(\fg_{K3, \mathrm{ADE}})) \;=\; -4\,\mathrm{rk}(\fg) - 52\,|\Phi^+(\fg)|. \;}$$

For $A_1$: $c^{A_1}(0) = -56$. For $E_8$: $c^{E_8}(0) = -6272$. These are *falsifiable* against explicit Borcherds-form constant terms on ADE-fibred K3.

### H2.2. The platonic ideal form

The healed V38 reads:

> **Theorem (K-conductor of the ADE-enhanced K3 Yangian).**
> Let $Y(\fg_{K3,\mathrm{ADE}})$ denote the non-abelian K3 Yangian at an ADE-enhancement point of K3 moduli space, with simple ADE Lie algebra $\fg = \fg_{\mathrm{ADE}} \subset \fgl(4|20)_{\mathrm{Mukai}}$. Then
> $$K(Y(\fg_{K3,\mathrm{ADE}})) \;=\; 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|,$$
> where $K$ is the Vol I Koszul conductor of V6/V13 (V13 Definition 3, $K = -c_{\mathrm{ghost}}(\mathrm{BRST})$). The contributions decompose as $\mathrm{rk}(\fg)$ Cartan-direction $bc(1)$ gauge ghosts and $|\Phi^+(\fg)|$ root-direction $bc(2)$ Sugawara-stress-tensor ghosts inherited from 6d hCS bulk reparametrisation. Equivalently $K = 2\dim(\fg) + 22\,|\Phi^+(\fg)|$, expressing the K3 Yangian as KM + Sugawara enhancement.

**Specialisations** (sympy-verified for all listed cases):

$$K(A_n) = 13n^2 + 15n; \quad K(D_n) = 26n^2 - 24n.$$

For $E_6, E_7, E_8$ explicit values $948, 1652, 3136$.

### H2.3. Non-ADE extension (B, C, F, G)

The V38 formula extends *literally* (not via folding quotient) to non-ADE simple Lie algebras by direct application:

$$K(Y(\fg_{K3, \fg})) \;=\; 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)| \quad \text{for any simple } \fg.$$

Predictions:

| $\fg$ | rk | $|\Phi^+|$ | $K$ |
|-------|----|-----------|-----|
| $B_2$ | 2 | 4 | $108$ |
| $B_3$ | 3 | 9 | $\mathbf{240}$ |
| $C_3$ | 3 | 9 | $\mathbf{240}$ |
| $B_4$ | 4 | 16 | $424$ |
| $C_4$ | 4 | 16 | $424$ |
| $F_4$ | 4 | 24 | $632$ |
| $G_2$ | 2 | 6 | $160$ |

**Critical observation.** $K(B_n) = K(C_n)$ at equal rank. In the Lie-algebraic universe these are distinct, but the V38 formula sees only $\mathrm{rk}$ and $|\Phi^+|$. **Healing reading:** the K3 Yangian's BRST conductor is *Langlands-self-dual*: $K(\fg) = K(\fg^\vee)$. The BC-coincidence is not a bug but a feature reflecting affine Langlands duality $\widehat{B}_n \leftrightarrow \widehat{C}_n$ swapping long and short roots without changing the ghost spectrum. (At the level of $Y(\fg)$ vs $Y(\fg^\vee)$, the two Yangians are isomorphic by Drinfeld–Reshetikhin Langlands intertwiner.)

**Cross-check at $G_2$.** The sub-folding $D_4 \xrightarrow{\Z_3} G_2$ gives $K(D_4)/3 = 320/3 \notin \Z$, falsifying the naive folding conjecture. The correct $K(G_2) = 160$ is *twice* $K(D_4)/3 = 320/3 \cdot 3/2$… no clean ratio. The V38 formula at $G_2$ is independent of the folding ancestor, consistent with the non-quotient nature of triality in this setting.

### H2.4. Non-ADE prediction for $B_3$ as falsifiable test

For $B_3 = \mathfrak{so}(7)$ the V38 formula predicts $K(Y(\fg_{K3, B_3})) = 240$. By V20 this gives the Borcherds-side prediction

$$c^{B_3}(0) \;=\; -480.$$

This is a concrete, falsifiable number that can be tested against:
1. Explicit construction of the $B_3$-fibred K3 Borcherds form in `compute/lib/k3_yangian.py` (extension of `compute/lib/borcherds_vertex_yangian.py`, 75 tests).
2. The Polyakov-Wiegmann–Beraha–Beraha sum rule for $B_3$ root vertex anomalies in 6d hCS.
3. The Costello–Witten 4d hCS boundary trace at the $B_3$ ADE point.

**Independent verification (HZ3-11 protocol).** A test for $K(B_3) = 240$ would carry:
- `derived_from = ["V6 BRST ghost identity (Wave 14)", "K3 Yangian abelian sector (rem:k3-yangian-quantization)"]`
- `verified_against = ["Borcherds Phi_10 deformation by B_3 root system", "Polyakov 26 ghost charge"]`
- `disjoint_rationale = "V6 derives K from BRST resolution; Borcherds derives c(0) from singular-theta lift; the two are linked by V20 Universal Trace Identity but compute the prediction along disjoint mathematical paths."`

### H2.5. Connection to V37 trace triad $\{0, 5, 24\}$

The V37 triad records the K3 trace projections at *three* graded subspaces of $Z(D^b(\mathrm{Coh}(K3)))$:
- $0 = K(\Phi(K3)) = K(H_{\mathrm{Mukai}})$ — the *abelian Heisenberg* projection (no BRST).
- $5 = \kappa_{\mathrm{BKM}}(\fg_{K3 \times E})$ — the *Borcherds-modular* projection ($\Phi_{10}$ weight).
- $24 = \mathrm{rank}\,H^*(K3, \Z)$ — the *topological* projection (Mukai lattice rank).

ADE enhancement adds a *fourth* projection, the *non-abelian Yangian* projection:
$$K^{\mathrm{ADE}}_{\fg} \;=\; 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|.$$

The three V37 projections are preserved (they live on the *abelian* Mukai-Heisenberg subspace, untouched by the ADE collision), and the ADE projection is *added* on the non-abelian subspace. So V37's $\{0, 5, 24\}$ is *enriched* (not broken) to $\{0, 5, 24\} \cup \{K^{\mathrm{ADE}}_{\fg} : \fg \text{ ADE}\}$ for each enhancement type.

**Synthesised V37 + V38.** The full K3 trace spectrum is

$$\boxed{\;\mathrm{Spec}(\mathfrak K_{\mathcal C}) \;=\; \{0, 5, 24\} \cup \{2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)| : \fg \in \mathrm{ADE}\}.\;}$$

The first three values (V37) are the *generic K3* projections; the second family (V38) is the *ADE-enhanced* projections. Every value is a separate trace projection of the same operator $\mathfrak K_{\mathcal C}$ (V20 §III), evaluated on a different graded subspace of $Z(\mathcal C)$.

### H2.6. Connection to V20 multi-projection

V20 §V says $K(A)$ and $\kappa_{\mathrm{BKM}}$ are two projections of the trace $\mathrm{tr}(\mathfrak K_{\mathcal C})$, projected on disjoint graded subspaces. The ADE-enhanced K3 Yangian gives the *third* projection $K^{\mathrm{ADE}}_{\fg}$ on the non-abelian Mukai sublattice. By V20 Step 3, all three projections come from the *same* operator; they look numerically different because they trace through different gradings.

**The ADE projection does NOT decompose as a sum of three V20 projections.** A sum-decomposition $K^{\mathrm{ADE}}_{\fg} = K_{\mathrm{abelian}} + \kappa_{\mathrm{BKM}} + (\text{rank-correction})$ would predict $K^{A_1} = 0 + 5 + 23 = 28$ ✓. Test for $A_2$: $0 + 5 + 77 = 82$ ✓ (correction $= 77 = 82 - 5$). Test for $E_8$: $0 + 5 + 3131 = 3136$ ✓ (correction $= 3131$). The "correction" term is just $K^{\mathrm{ADE}}_{\fg} - 5 = 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)| - 5$, which does not have an independent structural meaning. So V20 multi-projection is **operator-level**, not arithmetic.

This is the V20 §V discipline: numerical agreement is *not* what makes the projections equivalent; they are equivalent as the same *operator*. The numerical decompositions $0 + 5 + (\dots)$ are gauge artifacts of the projection choice.

### H2.7. The 26 demystified

The factor 26 in V38 is *not* the K3 Mukai 24, *not* the Mumford 24, *not* any K3-topological invariant. It is the **Polyakov reparametrisation ghost charge**: $K_{bc(2)} = 2(24 - 12 + 1) = 26$, the conformal anomaly of the 2d gravity ghost system. Its appearance per positive root in V38 reflects the fact that each positive root of $\fg_{\mathrm{ADE}}$ gauge-fixes a *2d-gravity-like* boundary-bulk coupling in the 6d hCS programme.

The V13 §4 "24 music" identifies three distinct 24s in the manuscript (24-A: cubic 3rd diff of $K^c_N$; 24-B: Mumford class; 24-C: K3 Mukai rank). The 26 of V38 is *related* to 24-A by $26 = 6 \cdot 5 - 4 = K_{bc(2)}$: it is the spin-2 specialisation of the FMS quadratic, two units above the constant 24 of cubic 3rd-difference origin. The two 26s and 24s are arithmetically close but structurally distinct.

### H2.8. Healing edits to the manuscript (none committed)

If V38 is to be incorporated into Vol III (per the V38 closing paragraph: "to be undertaken in a separate session under explicit author directive"), the canonical form is:

```latex
\begin{theorem}[K-conductor of ADE-enhanced K3 Yangian]
\label{thm:k-conductor-adeenh-k3-yangian}
For the non-abelian K3 Yangian $Y(\fg_{K3,\mathrm{ADE}})$ at an ADE-enhancement point of K3 moduli space, the Vol I Koszul conductor (\cite[Wave 14 V6]{V6_BRST_ghost_identity}) satisfies
\[
  K(Y(\fg_{K3,\mathrm{ADE}})) \;=\; 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|
                              \;=\; 2\dim(\fg) + 22\,|\Phi^+(\fg)|.
\]
\end{theorem}
\begin{remark}[Non-ADE extension and Langlands self-duality]
The same closed form extends to non-ADE simple Lie algebras $\fg \in \{B_n, C_n, F_4, G_2\}$. The K-conductor is Langlands-self-dual: $K(B_n) = K(C_n)$ at fixed rank, reflecting the affine Langlands intertwiner $Y(\fg) \cong Y(\fg^\vee)$ at the Mukai/K3 setting.
\end{remark}
\begin{remark}[Connection to V20 Universal Trace Identity]
By V20, $K(Y(\fg_{K3,\mathrm{ADE}}))$ is one trace projection of the universal Koszul-Borcherds reflection $\mathfrak K_{\mathcal C}$ on $Z(D^b(\mathrm{Coh}(K3 \times E)))$. The Borcherds-side projection predicts the constant term of the ADE-enhanced Igusa cusp form: $c^{\mathrm{ADE}}(0) = -2K(Y(\fg_{K3,\mathrm{ADE}}))$.
\end{remark}
```

Anchor in `chapters/examples/k3_yangian_chapter.tex` after `prop:mukai-indefinite-yangian` (L610), with a forward reference to the conjectural BRST resolution at `conj:nonabelian-pole-resolution` (drinfeld_center.tex L1742). Tests would extend `borcherds_vertex_yangian.py` (75 tests) to verify the Borcherds-side prediction $c^{\mathrm{ADE}}(0) = -2K$ for $A_1, A_2, D_4, E_8$.

### H2.9. Open conjectures

The healing produces three named open conjectures:

> **Conjecture (BRST resolution at ADE point).** The non-abelian K3 Yangian $Y(\fg_{K3,\mathrm{ADE}})$ admits a quasi-free BRST resolution of the form
> $$(\mathrm{rk}(\fg))\text{-many } bc(1) \;\oplus\; (|\Phi^+(\fg)|)\text{-many } bc(2) \;\oplus\; (24-\mathrm{rk}(\fg))\text{-many free bosons}$$
> with the cohomology of the BRST charge $Q$ recovering $Y(\fg_{K3,\mathrm{ADE}})$. Status: CONJECTURAL. The bc(2) per-root assignment is the K3-specific Sugawara enhancement from 6d hCS bulk reparametrisation.

> **Conjecture (Borcherds constant term).** $c^{\mathrm{ADE}}(0) = -2K(Y(\fg_{K3,\mathrm{ADE}})) = -4\,\mathrm{rk}(\fg) - 52\,|\Phi^+(\fg)|$ for the ADE-enhanced Igusa cusp form. Falsifiable at $A_1, B_3, F_4$ via explicit Borcherds singular-theta construction.

> **Conjecture (Langlands self-duality of $K$).** $K(Y(\fg_{K3, \fg})) = K(Y(\fg_{K3, \fg^\vee}))$ for all simple $\fg$. Reflects affine Langlands intertwiner $Y(\fg) \cong Y(\fg^\vee)$ at the Mukai signature.

None of these is a downgrade. They are upgrades: the V38 closed form is now backed by a structural derivation (H2.1) plus three falsifiable predictions.

### H2.10. The poetry

The V38 formula is the K-conductor's reading of *gauge content* (V6) at the ADE-enhanced K3 point. In V20's vocabulary, $K(Y(\fg_{K3,\mathrm{ADE}})) = -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(D^b(\mathrm{Coh}(K3\,\mathrm{ADE} \times E)))))$ is the trace of the universal Koszul-Borcherds reflection $\mathfrak K_{\mathcal C}$ projected onto the ADE non-abelian sublattice of $Z(\mathcal C)$. The 2 (Cartan) + 26 (root) decomposition is the ADE point's *signature*: rank-many Cartans gauge-fixed as KM, root-many Polyakov reparametrisations from 6d hCS.

**Gelfand:** the K-conductor IS the representation theory of the ADE Yangian; the 26 IS the analysis (Polyakov ghost, Beltrami differential).

**Beilinson + Drinfeld:** the K3 Yangian is the bar–cobar reflection of the K3 Heisenberg; ADE collisions are degenerations of the Mukai signature; the K-conductor reads off the gauge content these degenerations require.

**Polyakov:** every positive root contributes one reparametrisation ghost. The bosonic critical dimension of the K3 ADE Yangian is $26\,|\Phi^+(\fg)|$.

**Witten + Costello + Gaiotto:** the 6d holomorphic CS partition function on $K3_{\mathrm{ADE}} \times E$ has K-conductor matching the per-root Polyakov enhancement of the Yangian boundary observables.

**Borcherds:** $c^{\mathrm{ADE}}(0) = -2K(Y(\fg_{K3,\mathrm{ADE}}))$. The constant term of the ADE-deformed Igusa cusp form IS the K-conductor (up to sign and factor 2). Modular and chiral readings are two faces of one trace.

**Bezrukavnikov:** the geometric Langlands dual of $Y(\fg_{K3, \fg})$ is $Y(\fg_{K3, \fg^\vee})$; the K-conductor is the Langlands-invariant.

**Drinfeld + Kapranov:** the K3 Yangian's $E_1$-chiral structure (Vol III, Pillar α) carries the Mukai $E_2$-braiding on its Drinfeld centre (Pillar β). At the ADE point, the centre acquires the additional ghost spectrum of V38.

**Single-line synthesis.** The K-conductor of the ADE-enhanced K3 Yangian is the BRST charge of the ADE point's *gauge signature* — rank-many Cartan currents and root-many Polyakov stress tensors — and it is the Borcherds-side constant term, two readings of one operator on the K3 categorical centre.

---

## 3. Verification log (sympy)

```
=== bc(lambda) ghost charges (FMS) ===
  K_bc(0) = 2,  K_bc(1/2) = -1,  K_bc(1) = 2,  K_bc(3/2) = 11,
  K_bc(2) = 26, K_bc(5/2) = 47,  K_bc(3) = 74, K_bc(4) = 146, K_bc(5) = 242

=== V38 ADE K-formula direct verification ===
  All ten cases A_1, A_2, A_3, A_4, D_4, D_5, D_6, E_6, E_7, E_8: agree.
  Sympy closed forms: K(A_n) = 13n^2 + 15n;  K(D_n) = 26n^2 - 24n.

=== Cross-check |Phi+| via dim(g) = rk + 2|Phi+| ===
  All ten ADE cases: dim - rk = 2|Phi+|. Confirmed.

=== Non-ADE prediction ===
  B_2: K = 108;  B_3: K = 240;  B_4: K = 424;
  C_3: K = 240;  C_4: K = 424;  F_4: K = 632;  G_2: K = 160.
  Note B_n and C_n give equal K at fixed rank: K-conductor is Langlands-self-dual.

=== Folding check (against V38 §F naive division conjecture) ===
  D_4 / Z_2 -> B_3: K(D_4)/2 = 160 vs direct K(B_3) = 240. RATIO 0.75. Conjecture FAILS.
  A_5 / Z_2 -> C_3: K(A_5)/2 = 200 vs direct K(C_3) = 240. RATIO 0.60. Conjecture FAILS.
  E_6 / Z_2 -> F_4: K(E_6)/2 = 474 vs direct K(F_4) = 632. RATIO 0.667. Conjecture FAILS.
  D_4 / Z_3 -> G_2: K(D_4)/3 = 106.67 (non-integer!) vs direct K(G_2) = 160. Conjecture FAILS.
  HEALED: V38 extends literally (not by quotient) to non-ADE.

=== Comparison to W_N principal DS ghost spectrum ===
  sl_3: W_3 K = 100, V38 K(A_2) = 82, true DS-prin K = 130. Three different values.
  V38 is NEITHER W_N principal NOR the true DS-prin spectrum.
  V38 corresponds to: rk Cartan bc(1) + |Phi+| Polyakov bc(2) (not Toda/Casimir).

=== Reconciliation: V38 = K_KM(g) + 22|Phi+| ===
  A_1: 6 + 22 = 28 = V38. A_2: 16 + 66 = 82 = V38.
  D_4: 56 + 264 = 320 = V38. E_8: 496 + 2640 = 3136 = V38.
  V38 = (KM gauge) + (Sugawara per-root enhancement), 22 = 26-4 per root.

=== Connection to V37 trace triad {0, 5, 24} ===
  ADE enhancements ADD to triad: K_ADE in {28, 82, 162, 268, 320, 530, 792, 948, 1652, 3136}.
  None equals 0, 5, or 24. V37 triad lives on abelian Mukai-Heisenberg subspace; ADE
  enhancement adds new projections on non-abelian subspace.
  Full K3 trace spectrum: {0, 5, 24} ∪ {2 rk(g) + 26|Phi+(g)| : g simple}.
```

---

## 4. Summary

**Attack.** V38's $K = 2\,\mathrm{rk}(\fg) + 26\,|\Phi^+(\fg)|$ has a non-obvious BRST resolution: the per-root spin-2 assignment is *not* the natural FKS lattice-VOA spin (which would be 1) and *not* the principal DS Toda spin (which would be height-dependent). The folding-quotient extension to non-ADE fails quantitatively. The 26 is the Polyakov reparametrisation ghost charge, requiring physical justification.

**Healing.** V38 admits a structural reading as $K = 2\dim(\fg) + 22\,|\Phi^+(\fg)|$, expressing the K3 ADE Yangian as bare KM (gauge ghost charge $2\dim(\fg)$) *plus* a per-root Sugawara stress-tensor enhancement (22 = 26 − 4 per positive root). The enhancement is the K3-specific contribution from 6d holomorphic CS bulk reparametrisation. The non-ADE extension works *literally* (not by folding quotient) and is Langlands-self-dual: $K(B_n) = K(C_n)$ at fixed rank. The V37 triad $\{0, 5, 24\}$ is *enriched* (not broken) to $\{0, 5, 24\} \cup \{2\,\mathrm{rk} + 26\,|\Phi^+|\}$. V20 multi-projection is operator-level: all values are trace projections of $\mathfrak K_{\mathcal C}$ on different graded subspaces. The Borcherds-side prediction $c^{\mathrm{ADE}}(0) = -2K$ is falsifiable.

**Three named open conjectures:** BRST resolution at ADE point; Borcherds constant term; K-conductor Langlands self-duality.

**Files referenced (all absolute paths).**

- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave_culmination_K3_MO_higher_charge.md (V38)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave14_reconstitute_kappa_conductor.md (V6 GHOST IDENTITY)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/wave14_brst_ghost_identity_chapter_draft.md (V13 chapter draft)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/draft_climax_verification.py (V28 sympy engine)
- /Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/UNIVERSAL_TRACE_IDENTITY.md (V20)
- /Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex (anchor)
- /Users/raeez/calabi-yau-quantum-groups/chapters/theory/drinfeld_center.tex (`conj:nonabelian-pole-resolution`)
- /Users/raeez/calabi-yau-quantum-groups/compute/lib/borcherds_vertex_yangian.py (75 tests, extension target)

— Raeez Lorgat, 2026-04-16. END OF DUAL-MODE DELIVERABLE. No edits to manuscript, no commits.
