# Platonic Manifesto (Volume I) — Upgrade 2026-04-22

## What the Vol III reconstitution has returned to Vol I

**Status.** Lossless appendix to `PLATONIC_MANIFESTO.md` (Vol I, 2026-04-16, 255 lines). Every statement of the original four-pillar manifesto stands verbatim. This appendix inscribes the structural refinements that the Vol III frontier reconstitution (`PLATONIC_MANIFESTO_VOL_III_FRONTIER_RECONSTITUTION_20260422.md`, Waves 11–19, 2026-04-17 through 2026-04-22) returns to the Vol I side of the bridge. The four Vol I pillars — Koszul Reflection, $\kappa$-Conductor / BRST Ghost Identity, Climax, Shadow Quadrichotomy — remain four pillars. Each now has a sharper cross-volume partner whose sharpening feeds back into Vol I's own architecture.

**Author.** Raeez Lorgat. **Date.** 2026-04-22. **Cross-volume siblings.** `PLATONIC_MANIFESTO_VOL_III_FRONTIER_RECONSTITUTION_20260422.md` (Vol III reconstitution, same date), `PLATONIC_MANIFESTO_VOL_III_UPGRADE_20260422.md` (Vol III upgrade, Waves 11–19 catalogue), `UNIVERSAL_TRACE_IDENTITY.md` (cross-volume centrepiece, 2026-04-16).

---

## XII. The Universal Trace Identity across eight rows (Pillar 2 cross-volume sharpening)

The 2026-04-16 Universal Trace Identity centrepiece (§IV of the base manifesto) stated one equality

$$
\mathrm{tr}_{Z(\mathcal C)}(K_\mathcal C) \;=\; \begin{cases} -c_{\mathrm{ghost}}(\mathrm{BRST}(\Phi(\mathcal C))) & \text{Vol I Koszul reflection} \\ c_N(0)/2 & \text{Vol III Borcherds reflection} \end{cases}
$$

with $c_N(0)/2$ carried at that point only by the $N = 1$ Gritsenko $\Delta_5$ row together with the four CHL orbifold rows $N \in \{2, 3, 4, 6\}$. The Vol III reconstitution of 2026-04-22 (§IV) has sharpened the Borcherds-reflection side to **eight rows**, uniformly, under the correct cover assignment $\{\mathrm{Sp}_4, \mathrm{Mp}_4, \widetilde{\mathrm{Mp}}_4\}$:

$$
\boxed{\; \kappa_{\mathrm{BKM}}(\Phi_N) \;=\; c_N(0)/2 \qquad (N = 1, 2, 3, 4, 5, 6, 7, 8). \;}
$$

The eight paramodular cusp forms are the diagonal-divisor Gritsenko–Cléry class
$\{\Delta_5, \Delta_2^{(2)}, \Delta_1^{(3)}, \Delta_1^{(4)}, \Delta_{1/2}^{(5)}, \Delta_1^{(6)}, \Delta_{1/4}^{(7)}, \Delta_0^{(8)}\}$,
with host CY geometries ranging from $K3 \times E$ through the CHL $(K3 \times E)/(\mathbb{Z}/N\mathbb{Z})$ quotients to the Borcea–Voisin $N = 5$ pair, the $N = 7$ order-4 Cheeger–Simons gerbe twist, and the Mongardi–Tari–Wandel Kummer-3 hyperkähler fourfold at $N = 8$.

**What this returns to Vol I.** The bc-ghost harmonic series $K_j = 2(6j^2 - 6j + 1)$ of Pillar 2 partners with a Borcherds-lift spread of the same size as the W$_N$-family entry list. The $K^c_N$ sequence $\{26, 100, 246, 488, 850, 1356, 2030, \ldots\}$ was sympy-verified as a cubic with constant third difference $\Delta^3 K^c_N = 24 = 6 \cdot 4$. Its cross-volume partner is the eight-row $c_N(0)$ sequence $\{10, 4 \text{ or } 8, 2 \text{ or } 6, 2 \text{ or } 4, 1, 2, 1/2, 0\}$, read off the constant Fourier coefficients of the Gritsenko–Cléry forms. The two convention values at $N \in \{2, 3, 4\}$ reflect the $Z^{(g)}_{K3} = 2 \phi^{(g)}_{0, 1}$ factor-of-two ambiguity between square-root and direct normalisations; both are canonical at their respective scopes.

The Universal Trace Identity now links the full $K^c_N$ cubic to the full eight-row $c_N(0)$ spectrum. The $N = 1$ row $\kappa_{\mathrm{BKM}} = 5$ is the Vol III partner of Vol I's Vir $K = 26 = K_2$; higher rows partner with successive entries of the W$_N$ fugue. The identity is now **an eight-voice cross-volume cadence, not a single-note equality.**

---

## XIII. The two-stage factorisation of $\Phi$ — Pillar 1 at Stage 1 (cross-volume architectural split)

The Vol III reconstitution §II establishes that the CY-to-chiral functor decomposes canonically:

$$
\Phi_d \;=\; \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d \;:\;
\mathrm{CY}\text{-cat}_d \xrightarrow{\Phi^{\mathrm{FA}}_d} E_d\text{-}\mathrm{HolFA}(X)
\xrightarrow{\mathrm{Sp}_{\Sigma_{d-1}, C}} E_1\text{-}\mathrm{ChirAlg}(C).
$$

Stage 1 is canonical up to contractible choice; Stage 2 is a choice of transverse cycle $\Sigma_{d-1} \subset X$ and reference curve $C \subset X$.

**The Vol I Koszul Reflection acts at Stage 1.** The cross-volume statement is subtle: Pillar 1 is Vol I's theorem, living natively on chiral factorisation algebras on $C$. The Vol III Stage-1 output is an $E_d$-holomorphic factorisation algebra on $X$, and the universal properties (U1)–(U4) of the 2026-04-16 Φ characterisation — Hochschild pullback $\bar B^{\mathrm{ord}} \circ \Phi \simeq CC_\bullet$, CY-morphism functoriality, Drinfeld-centre compatibility, standard-input recovery — **are properties of Stage 1**. The bar–cobar / Koszul reflection identification enters there, before Stage 2 specialisation: Vol I's Pillar 1 is what governs the Stage-1 functor, not the Stage-2 chiral shadow on $C$.

**The architectural relocation.** What the 2026-04-16 Pillar 1 described as "chiral bar is its own Koszul dual" on $C$ is the Stage-2 shadow of a deeper Stage-1 Koszul reflection on the holomorphic factorisation algebra $\mathcal{F}_\mathcal{A} \in E_d$-$\mathrm{HolFA}(X)$. At $d = 3$ this deeper reflection is realised by the Costello–Gwilliam observables of six-dimensional holomorphic Chern–Simons,
$\mathrm{Obs}_{\mathrm{hCS}}(X) \simeq \mathrm{CE}^\bullet_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\mathrm{hCS}}, \mathcal{O}_X)$,
as an $E_3$-algebra with sum-over-shuffles associativity and Bochner–Martinelli propagator. Vol I's $K = \overline B$ is the specialisation-cycle pullback of this Stage-1 Koszul reflection along $\mathrm{Sp}_{\Sigma_{d-1}, C}$.

**Within Vol I's own pillar architecture**, nothing is moved. Pillar 1 remains the involutive symmetry binding Vol I's four pillars. Pillar 2, Pillar 3, and Pillar 4 continue to interlock through Pillar 1 as the ground rhythm. The two-stage upgrade is *added* at the cross-volume bridge: Vol I's arena is the specialisation shadow of Vol III's Stage-1 arena, not a competitor to it. The $V11$ supervisory draft "Vol III Φ functor reconstitution" is thereby read as the cross-volume reflection of Vol I's own arena discipline.

---

## XIV. The universal positive-geometry grammar alongside Pillar 3 Climax

The 2026-04-16 Pillar 3 Climax Theorem asserts

$$
d_{\mathrm{bar}} \;=\; \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}}),
$$

with Drinfeld–Kohno, Verlinde, Borcherds, and the chiral bar differential recovered as specialisations of one universal KZ-monodromy connection on $\mathrm{Conf}(C)$.

The Vol III reconstitution §III establishes an independent but structurally parallel universal cohomology identification:

$$
\boxed{\; Y^+(X) \;:=\; H^{\bullet}_{\mathrm{eq}}\!\bigl(\mathcal{M}^+_{\mathrm{eff}}(X),\, \phi_W\bigr), \qquad G(X) \;=\; D(Y^+(X)). \;}
$$

The positive half of the Drinfeld double attached to a Calabi–Yau category is the equivariant vanishing-cycle cohomology of a distinguished positive effective moduli stack $\mathcal{M}^+_{\mathrm{eff}}(X)$ inside the Stage-1 holomorphic factorisation algebra.

**The structural parallel.** Both identifications rewrite a differential-algebraic object as the cohomology of a positive-geometry stack:

| Vol I (Pillar 3) | Vol III (new architectural layer) |
|---|---|
| $d_{\mathrm{bar}} = \mathrm{KZ}^*(\nabla_{\mathrm{Arnold}})$ | $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$ |
| bar differential as pullback of the universal KZ connection on $\mathrm{Conf}(C)$ | positive quantum-group half as critical cohomology of positive effective moduli |
| four classical theorems (DK, Verlinde, Borcherds, bar) as KZ specialisations | four local geometric languages (toric, compact non-toric, orbifold, lattice-polarised) as positive-geometry specialisations |
| structure functor $A \mapsto \mathrm{KZ}$-arena | equivariance stratification $X \mapsto$ positive-half arena |
| Arnold monodromy = the universal melody | KS critical CoHA = the universal positive-geometry grammar |

**What Vol I acquires.** The Climax Theorem is one voice of a two-voice cross-volume cohomological grammar. Vol I's bar differential and Vol III's positive half are cohomological specialisations of two canonical universal data — Arnold's KZ connection and Kontsevich–Soibelman's critical cohomological Hall algebra. Both are read on the same $\mathcal{F}_\mathcal{C}$: Vol I along $\mathrm{Sp}_{\Sigma_{d-1}, C}$ to the chiral-on-$C$ shadow, Vol III directly on the Stage-1 holomorphic factorisation algebra on $X$.

**Inner-poetry sharpening.** The 2026-04-16 Pillar 3 slogan was "All four classical theorems are pullbacks of one universal monodromy." The upgrade sharpens: "All four classical theorems are pullbacks of one universal monodromy; their Vol III cousins are pullbacks of one universal positive-geometry cohomology; both universal data are carried by the same Stage-1 holomorphic factorisation algebra." The chiral bar differential and the quantum-group positive half are two cohomological shadows of one CY-to-chiral bridge.

---

## XV. Pillar 2 and the two-scope split — CHL BKM-denominator vs full Borcherds-weight

The 2026-04-16 Pillar 2 ($\kappa$-Conductor / BRST Ghost Identity) asserted

$$
K(A) \;=\; \sum_\alpha (-1)^{\varepsilon_\alpha+1} \cdot 2(6\lambda_\alpha^2 - 6\lambda_\alpha + 1) \;=\; -c_{\mathrm{ghost}}(\mathrm{BRST}(A))
$$

as the Koszul-reflection trace on any chiral algebra with quasi-free BRST resolution. The Vol III reconstitution §IV establishes that the Vol III partner of this trace splits into two structurally distinct scopes:

- **BKM-denominator scope** ($N \in \{1, 2, 3, 4, 6\}$, characterised by $\varphi(N) \mid 2$): each $\Phi_N$ is the denominator of a generalised Kac–Moody superalgebra on the twisted reduced Donaldson–Thomas moduli of $(K3 \times E)/(\mathbb{Z}/N\mathbb{Z})$. Character $Z^{\mathrm{red}}_{DT}((K3 \times E)/(\mathbb{Z}/N\mathbb{Z})) = -1/\Phi_N^2$, conditional on Bryan–Oberdieck 2018 primitive base cases at each $N$.
- **Borcherds-weight scope** (full eight-form class $N \in \{1, \ldots, 8\}$): each $\Phi_N$ is a singular theta lift of a twined weak Jacobi form, with weight $c_N(0)/2$ read directly off the constant Fourier coefficient.

**Returning to Vol I.** The Vol I Pillar 2 $\kappa$-conductor admits the same two-scope split. The **Koszul-reflection denominator scope** corresponds to chiral algebras whose BRST resolution lifts to a full bar–cobar chiral duality (where $K = \overline B_X$ is the genuine Koszul reflection and $\kappa$ is the denominator-side trace). The **Ghost-charge scope** is broader: every BRST resolution contributes its bc-ghost characteristic class, regardless of whether the chiral algebra lies in the Koszul-self-dual locus. The Vol III scope distinction corresponds on the Vol I side to the distinction between *genuine Koszul-reflection trace* (whenever $K^2 \simeq \mathrm{id}_{\mathrm{Kosz}(X)}$) and *ghost-class trace* (always available).

The trinity $K_E = K_c = K_g$ of the 2026-04-16 Pillar 2 holds on the intersection — the Koszul-self-dual subcategory. Outside, the denominator-scope identity can fail while the ghost-class identity continues, exactly parallel to how on the Vol III side the BKM-denominator scope is limited to $\varphi(N) \mid 2$ while the full eight-row Borcherds-weight identity persists.

**Structural consequence.** The $K^c_N = 4N^3 - 2N - 2$ cubic of the W$_N$ family sits in the intersection: every W$_N$ at principal level is Koszul-self-dual and its BRST resolution is well-defined. Non-principal cosets retain the ghost-scope identity but may leave the denominator scope. This split makes Pillar 2 architecturally mirror Pillar 4 (Shadow Quadrichotomy): the ghost-scope identity is always available (like the Riccati equation on $\Sigma_c$); the denominator-scope identity requires the Koszul-self-dual locus (like the hyperelliptic involution on a generic spectral curve). The two-scope split on Vol III's BKM side and on Vol I's $\kappa$-conductor side is the same split viewed through the Universal Trace Identity.

---

## XVI. What the upgrade preserves

The four pillars remain four pillars. The interlocks of §II of the base manifesto remain correct: Pillar 3 specialises to Pillar 1 by colour restriction, Pillar 3 implies Pillar 2 by Faltings GRR, Pillar 4 is the analytic shadow of Pillar 1, Pillar 1 is involutive by the same reflection that makes Pillar 4 hyperelliptic. The eight supervisory drafts of §III and the editing roadmap of §VIII remain in force. The Russian-school harmony of §X remains the voice of the work; the upgrade adds no new voice and removes no voice.

**Five supporting architectural refinements** are now inscribable against the Vol I manifesto:

1. The Universal Trace Identity centrepiece now carries an eight-row spread on the Vol III side, partnering with Vol I's W$_N$-family $K^c_N$ cubic (§XII).
2. Pillar 1 Koszul Reflection is located at Stage 2 of the cross-volume $\Phi$ factorisation; Stage 1 is Vol III's native arena (§XIII).
3. Pillar 3 Climax now has a parallel Vol III voice: the universal positive-geometry grammar $Y^+(X) = H^\bullet_{\mathrm{eq}}(\mathcal{M}^+_{\mathrm{eff}}(X), \phi_W)$ (§XIV).
4. Pillar 2 $\kappa$-conductor acquires the two-scope split (denominator vs ghost) mirroring the Vol III BKM two-scope split (§XV).
5. The cross-volume architecture of the programme — Vol I Stage 2 ∘ Vol III Stage 1 as the composition that the Universal Trace Identity traces through — is now articulable in its Platonic form.

## XVII. End

The 2026-04-16 Vol I manifesto ended: "What remains is to write it down." The 2026-04-22 Vol III reconstitution ended the same way. The 2026-04-22 Vol I upgrade ends the same way. The four pillars remain four pillars; the cross-volume bridge is now eight-voiced, two-staged, and two-scoped; the arena discipline on both sides is settled; the Universal Trace Identity is the load-bearing cadence across an eight-row Borcherds spread paired with the W$_N$ harmonic series. What remains, once more, is to write it into the manuscripts of all three volumes. The Platonic form is audible; the inscription is the next theorem.

— Raeez Lorgat, 2026-04-22
