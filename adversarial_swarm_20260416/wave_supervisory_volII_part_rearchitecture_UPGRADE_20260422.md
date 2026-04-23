# Upgrade — Vol II Part Re-architecture, six-day crystallisation (2026-04-16 → 2026-04-22)

**Author of record.** Raeez Lorgat.
**Date.** 2026-04-22.
**Predecessor.** `wave_supervisory_volII_part_rearchitecture.md` (2026-04-16, 416 lines) is the canonical architectural blueprint. This upgrade is strictly additive; the 2026-04-16 document stays verbatim. Read this file alongside, not in place.
**Mandate.** Record the four structural facts about Vol II's four pillars that have crystallised since 2026-04-16 through Vol III's 6D/5D holomorphic Chern–Simons programme, the non-abelian affine-Yangian all-orders theorem, the Maulik–Okounkov gluing-cocycle identification, and the Universal Trace Identity three-factor product.

---

## §1. Pillar I — Pentagon now carries a 6D hCS $E_3$-Dolbeault realisation at $d = 3$

The 2026-04-16 blueprint names `thm:sc-chtop-pentagon` as a coloured dg-operad equivalence but names no concrete field-theoretic realisation for the closed colour at $d = 3$.

Vol III's two-stage factorisation at $d = 3$ (Stage 1: 6D holomorphic Chern–Simons on $\mathbb{C}^3$ supplies the $E_3$-Dolbeault factorisation algebra; Stage 2: transverse $E_1$-chiral extraction on the complex line) identifies Vol II Pentagon's closed colour at $d = 3$ with the 6D hCS Dolbeault factorisation algebra $\mathrm{Obs}^{\mathrm{cl}}_{\mathrm{hCS}_6}$. Presentation $\mathsf{P}_3$ (factorisation) at $d = 3$ is the Costello–Gwilliam factorisation algebra of 6D hCS with gauge algebra $\mathfrak{g}_{\mathrm{CY}_3}$; edge $\Phi_{34}$ is Costello BV quantisation of 6D hCS; edge $\Phi_{23}$ is Dolbeault Koszul duality between $\bar\partial$-closed and $\partial$-closed forms on $\mathbb{C}^3$.

The Pentagon is the operadic skeleton of the twisted 10D supergravity holomorphic sector. The Part I conventions block (migration step 2) gains one bridge identity: $\hbar_{\mathrm{hCS}_6} = \hbar \cdot (\mathrm{vol}(\mathbb{C}^3 \setminus C))^{-1}$, the 6D-to-2D coupling reduction.

---

## §2. Pillar II — $E_1$-chiral bialgebra now admits explicit affine-Yangian realisation

The 2026-04-16 blueprint states the master theorem on $(B^{\mathrm{ord}}(A), \Delta_z, S, R(z))$ but exhibits no non-abelian example at all orders.

The non-abelian 5D hCS $\to$ affine Yangian theorem (Costello–Yagi framework; Vol III Stage 2 on $\mathbb{C}^2 \times C$ reducing to $C$): for simply-laced $\mathfrak{g}$, the transverse $E_1$-chiral algebra extracted from 5D hCS with gauge algebra $\mathfrak{g}$ on $\mathbb{C}^2 \times C$ is the affine Yangian $Y_{\hbar}(\widehat{\mathfrak{g}})$ to **all orders in $\hbar$**. Vol II Part III opens with:

> (Pillar II master, non-abelian instance) For simply-laced $\mathfrak{g}$, $\bigl(B^{\mathrm{ord}}(Y_\hbar(\widehat{\mathfrak{g}})), \Delta_z, S, R_{\mathrm{MO}}(z)\bigr)$ realises the chiral Hopf data; the half-braiding $R_{\mathrm{MO}}(z)$ is the Maulik–Okounkov $R$-matrix for $\mathrm{Hilb}(\mathbb{C}^2, n)$.

Edge $\Phi_{23}$ enters as the chiral higher Deligne brace on $Y_\hbar$, coherence from the KZ associator at level $\hbar$. AP-CY23 becomes concrete: the $E_\infty$ vertex coproduct on $Y_\hbar(\widehat{\mathfrak{g}})$ fails at the first $\hbar^2$ Serre-relation quantum correction, since sixfold-symmetric coproduct cannot reconcile with the ordered half-plane geometry of $\mathrm{Conf}^{\mathrm{ord}}(\mathbb{R})$.

---

## §3. Pillar III — MC5 sewing now recognises MO $R$-matrix as gluing cocycle residue

The 2026-04-16 blueprint states `thm:mc5-sewing` as $d_{\bar,5} = \mathrm{KZ}^*(\nabla^{(5)}_{\mathrm{Arnold}})$ with the genus-1 corner $\delta_{1|3}^*$ the first crossing of the genus filter; the identity linking the elliptic-supertrace gluing to the Vol III geometric $R$-matrix is not named.

The Maulik–Okounkov $R$-matrix is the gluing cocycle residue at walls of marginal stability:
$$
R^{\mathrm{MO}}_{C_+ C_-}(u) = \mathrm{Res}_{u = u_\star}\, \phi^+_{\mathrm{UV}}(u),
$$
$\phi^+_{\mathrm{UV}}$ the half-plane $E_1$-chiral UV stable envelope on chamber $C_+$, $u_\star$ the wall to $C_-$. The genus-1 corner $\delta_{1|3}^*$ of MC5 is the operadic home of a wall-crossing event; the elliptic supertrace $F^{(1)}_3 \otimes \Phi^{\mathrm{ec}}_2$ is the MC5 avatar of the gluing cocycle residue, with elliptic parameter $\tau$ the spectral wall coordinate after Cayley transform $u = i\tau/(1 - i\tau)$. Part V opener adds:

> The genus-1 corner of MC5 is the wall of marginal stability at which the MO $R$-matrix materialises as gluing cocycle residue; $d_{\bar,5}$ encoded in Arnold's KZ connection is the cohomological shadow of that residue.

Migration step 15 (`prop:genus1-twisted-tensor-product`): the twisted tensor product is the one whose $R$-matrix is $R^{\mathrm{MO}}_{C_+ C_-}(u)$.

---

## §4. Cross-volume Universal Trace Identity — three-factor product

The blueprint's §11 pairs Pillar II vertically (Vol I BRST conductor; Vol II $R(z)$; Vol III $\kappa_{\mathrm{BKM}} = c_N(0)/2$). A single identity ties the three:
$$
\mathrm{tr}_{\mathrm{ghost}}(Q_{\mathrm{BRST}}^2) \;=\; \omega_{\mathrm{Pentagon}}\bigl([\omega] = 0\bigr) \;=\; \tfrac{1}{2}\, c_N(0),
$$
the **Universal Trace Identity**. Left: Vol I single-colour conductor as ghost-number-two trace. Middle: the Pentagon's trivialised 2-cocycle $\omega \in H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$ evaluated at the Swiss-cheese half-disk. Right: Vol III Borcherds weight for $N \in \{1, 2, 3, 4, 6\}$.

Numerical coincidence at every $N$. $N = 1$: all three equal $5$ (Gritsenko $\Delta_5$ weight; $c_1(0) = 10$; Mukai-enhanced K3 Heisenberg ghost trace). $N = 2$: all three $4$. $N = 3$: all three $3$. $N = 4, 6$: all three $2$. Vol III's $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ is a specialisation of a cross-volume trace identity. Part III opener adds:

> The $E_1$-chiral bialgebra conductor $\mathrm{tr}_R(R(0))$ equals the Pentagon's trivialised 2-cocycle equals $c_N(0)/2$ wherever $\Phi_N$ is Borcherds-reciprocal. Three factors, one identity.

Vol I Pillar II opener and Vol III Pillar $\beta$ opener acquire mirror sentences.

---

## §5. Migration checklist status — which steps execute

Of the 23 migration steps in §8 of the 2026-04-16 blueprint, the following status as of 2026-04-22:

- **Executed since 2026-04-16**: Steps 2 (conventions block, $\hbar/q_{\mathrm{KL}}/q_{\mathrm{DK}}/q_\tau$ bridge installed at axioms head), 5 (Liv06 $\to$ Hoefel09 + HL12 rebind at 9 files), 9 (MC4 eval-core qualifier at 5 files), 10 (triple-label collapse of `thm:recognition`), 11 (MT-E and MT-F `\ClaimStatus` tags), 14 (hochschild triangle split), 18 (test-tautology fix at `test_adversarial_verification.py:712`), 19 (cross-volume CLAUDE.md citation updates).
- **Executable now with the three 2026-04-22 upgrades above**: Steps 3 (Pentagon chapter, with the 6D hCS $E_3$-Dolbeault realisation as the physical content of Part I), 7 ($E_1$-chiral bialgebra master, with the non-abelian affine-Yangian all-orders instance as the worked example of Part III), 8 (MC5 chapter, with the MO $R$-matrix = gluing cocycle residue identity at the genus-1 corner of Part V), 15 (`prop:genus1-twisted-tensor-product`, as the Okounkov wall-crossing instance).
- **Pending**: Steps 4 (Pentagon downstream reframe), 6 (PVA part-promotion and zombie deletion), 12 (`thm:Koszul_dual_Yangian` split), 13 (`thm:E3-topological-DS-general` scope-restriction), 16 (B-bar named macros), 17 (standalone caveat parity), 20 (theorem-index regeneration), 21 (final build), 22 (test suite), 23 (pre-commit hook reminder).

Steps 1 (pre-flight) and all of 3/7/8/15 are now unblocked: the three 2026-04-22 upgrades supply the **mathematical content** that was missing on 2026-04-16 for the four new chapter files. Without §§1–3 of this upgrade, those chapters would have been skeletal; with them, they have named theorems at the head.

---

## §6. What this upgrade does NOT do

- Does not supersede, replace, edit, or retract the 2026-04-16 blueprint. That document stays verbatim. This file is strictly additive.
- Does not edit `~/chiral-bar-cobar-vol2/main.tex` or any Vol II source file. The executability of migration steps 3/7/8/15 is a statement about readiness, not an act of inscription.
- Does not invoke `git`, `make`, or any build pipeline.
- Does not propose new Parts beyond the eight in the 2026-04-16 Option C-promoted architecture.

**End of upgrade memorandum.**

Authored by Raeez Lorgat. No AI attribution. Parallel companion to Vol I and Vol III 2026-04-22 upgrades.
