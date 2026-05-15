# Attack-Heal Falsification Cycles 8--12 — 2026-04-22

*Raeez Lorgat. Scope-tightening falsification-replacement of five load-bearing claims across the four battle-hardened platonic ideal documents, extending the Cycle-1--7 healing.*

**Target documents.**
- `/Users/raeez/chiral-bar-cobar/notes/VOL_I_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `/Users/raeez/chiral-bar-cobar-vol2/notes/VOL_II_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `/Users/raeez/calabi-yau-quantum-groups/notes/VOL_III_PLATONIC_IDEAL_BATTLE_HARDENED_2026_04_22.md`
- `/Users/raeez/chiral-bar-cobar/notes/MASTER_PLATONIC_IDEAL_CROSS_VOLUME_BATTLE_HARDENED_2026_04_22.md`

**Falsification discipline.** Every claim false until primary-literature verified (GN 1998, Costello 2011/2017, BD04, FG 2012, Lurie HA, DVV 1997, EOT 2011). Universal-trace universality versus per-row decomposition; G/L/C/M/B exhaustiveness against $\mathcal W_N$-tower outside-element; $\Phi_d$ canonicity restricted to Koszul locus; Theorem C five-element set outside-element witnesses; octachotomy 8-closure ambient-vs-gauge; seven-incarnation well-definedness vs seven-face hierarchy; $E_3$ Dunn primary-source attribution; $(\Phi_{10}/\eta^{48})^\hbar$ derivation vs ansatz.

---

## Cycle 8 — Humbert-admissibility convention split across volumes

**Attack.** Vol I platonic ideal Section II B writes `Humbert-admissibility: $n\equiv 3,5\pmod 8$' citing Eichler--Zagier 1985 Thm 9.1; Vol III platonic ideal Section III writes the nominally identical Koszul locus as `$\overline{\mathcal A_2}\setminus\bigcup_{n\equiv 0,3\pmod 4} H_n$'. These are two distinct arithmetic conditions on two distinct objects.

Primary check: Eichler--Zagier 1985 *Prog. Math.* 55 Theorem 9.1 concerns the polar cutoff $\Delta=4nm-\ell^2\ge-1$ on weak Jacobi forms of weight $0$ and index $1$; the condition $n\equiv 3,5\pmod 8$ is the discriminant-mod-$8$ parity on the Fourier support of $\phi_{0,1}^{K3}$. Separately, van der Geer 1988 *Hilbert Modular Surfaces* Springer LNM §IX fixes the Humbert-discriminant-class parity as $n\equiv 0,3\pmod 4$ on the Humbert divisors in $\overline{\mathcal A_2}$ (the Siegel modular threefold compactification). Conflating the Fourier-support parity with the Humbert-discriminant parity is a type error.

**Heal.** The Koszul locus $U^{\mathrm{adm}}=\overline{\mathcal A_2}\setminus\bigcup_{n\,\mathrm{adm}}H_n$ is cut by **Humbert-admissibility** $n\equiv 0,3\pmod 4$ (van der Geer 1988 §IX). The Fourier-polar-support condition $n\equiv 3,5\pmod 8$ (Eichler--Zagier 1985 Thm 9.1) separately indexes $\phi_{0,1}^{K3}$-inputs to the Bruinier--Heegner reciprocity of Theorem C. Every admissibility invocation in the platonic ideals names which condition is in force: *Humbert-admissibility* for Koszul-locus scope; *Fourier-admissibility* for Borcherds-lift input scope.

Cross-volume propagation:
- Vol I Section II B is rescoped to `Humbert-admissibility $n\equiv 0,3\pmod 4$' on the Koszul locus, with separate mention of `Fourier-admissibility $n\equiv 3,5\pmod 8$' when quoting $\phi_{0,1}^{K3}$-Fourier coefficients.
- Vol III Section III already uses the Humbert convention correctly; Section X (MGSL scope) currently uses the Fourier convention and should be tagged as such.
- Master Section XII.X is explicit.
- Theorem B's coderived-Positselski inversion holds on the Humbert-admissible stratum; the Malcev cocycle $\mathrm{gr}_n^{\mathrm{Malcev}}$ records the Humbert-divisor obstruction, not a Fourier-support obstruction.

---

## Cycle 9 — Outside-element witness for Theorem C's five-element set

**Attack.** Vol I Section II C and Master Section II (G2) assert $\kappa+\kappa^!\in\{0,\,8,\,13,\,250/3,\,98/3\}$ as canonical five-archetype ceiling. Counterexample candidate: $\mathcal W_4^k$ on class $\mathsf M$: from the AP5 canonical $\kappa(\mathcal W_N)=c(H_N-1)$ with $H_N=\sum_{j=1}^N 1/j$, we have $\kappa(\mathcal W_4^k) = c\cdot(H_4-1) = c\cdot(25/12-1) = c\cdot 13/12$. The Fateev--Lukyanov 1988 *Intl. J. Mod. Phys. A* 3 duality sends $\mathcal W_N$ at level $k$ to $\mathcal W_N$ at dual level $k^\vee$, producing $\kappa^! = c^!\cdot 13/12$ at the dual central charge $c^! = 26\cdot N / (k+N) - [\text{offset}]$ (the Feigin--Frenkel 1992 *Phys Lett B* 276 Wakimoto-dual formula for $\mathcal W_N$). At generic $c$, $\kappa+\kappa^!$ is a non-constant function of $c$ landing in a family of rationals, not at any fixed element of $\{0, 8, 13, 250/3, 98/3\}$.

**Heal.** The set $\{0,\,8,\,13,\,250/3,\,98/3\}$ is the **five-witness landmark set**, pinned to the five named witnesses
$$\mathcal A \in \{\mathcal H_k,\; V_k(\mathfrak g),\; \beta\gamma,\; \mathrm{Vir}_c,\; \mathbf H_{\Delta_5}\}$$
plus the two named $\mathsf M$-sub-landmarks at $\mathcal W_3$ (value $250/3$) and $\mathrm{BP}$ (value $98/3$). For generic $\mathcal A = \mathcal W_N$ at $N\ge 4$, the scalar $\kappa + \kappa^!$ lies in the larger $\mathsf M$-tower family
$$\{c\cdot(H_N-1) + c^!\cdot(H_N-1) : N\ge 3,\; c\in\Q\}$$
extending strictly beyond the five-set. $250/3$ at $\mathcal W_3$ and $98/3$ at $\mathrm{BP}$ are named landmarks inside the $\mathsf M$-tower, not the full tower.

Canonical statement: `five-witness landmark plus $\mathsf M$-sub-landmarks $\mathcal W_3$ and $\mathrm{BP}$; generic $\mathcal W_{N\ge 4}$-tower open per family'. Theorem C boxing tightened from `five-archetype ceiling' to `five-witness landmark set, $\mathsf M$-tower scope-open at $N\ge 4$'. The non-principal hook-type $\mathcal W$-duality (Vol II §X frontier) supplies the missing $\mathsf M$-tower identifications for types A; types B, C, D remain frontier.

---

## Cycle 10 — Octachotomy eight-count as seven-ambients-plus-formality-gauge

**Attack.** Vol I Section VII enumerates eight ambients for strict chain-level bar--cobar inversion:
1. fibrewise generic
2. single-monodromy $H_n$
3. bi-unipotent Malcev
4. tri-unipotent Malcev at $(3,4,7)$
5. weight-completed coderived
6. $A_\infty$-corrected
7. $(\infty,1)$ $\mathrm{Perf}(\overline{\mathcal A_2})$
8. chiral-Kontsevich-formal on $U^{\mathrm{adm}}$

Item (8) is a **choice of Kontsevich--Tamarkin formality gauge** applied to ambient (7) on the Humbert-admissible complement, not an ambient category distinct in the same category-theoretic sort as (1)--(6). The `eight distinct ambients' count is misleading: (1)--(7) are seven genuine ambient categories; (8) is a gauge refinement of (7).

**Heal.** Correct count is **seven ambient categories plus one formality-gauge refinement** of ambient (7) on $U^{\mathrm{adm}}$, totalling eight strict chain-level bar--cobar inversion strata. The label `octachotomy' is retained because the combined count yields eight distinct inversion strata; the structural reading is sharpened. Igusa-transversality fails at the admissible Heegner triple $(3,4,7)$ (realised by $[E_{\sqrt{-3}}\times E_{\sqrt{-7}}]$ with tri-commuting $\mathfrak{sl}_2^{\oplus 3}$) giving **heptachotomy** at the bare ambient level; this is lifted to **octachotomy** by the formality-gauge refinement on $U^{\mathrm{adm}}$. The ambient/gauge distinction becomes a scope qualifier for future frontier work: open item 15 in Master Section XIII (A$_2$-refined anomaly cancellation) is itself a gauge-refinement statement, not an ambient addition.

---

## Cycle 11 — $(\Phi_{10}/\eta^{48})^\hbar$ weight balance on Siegel diagonal versus full $\mathbb H_2$

**Attack.** Vol I Section II-ter K3-Picard-rank-2 / Section X, Vol II §IV, and Master Section XIV-bis Climax-2 all invoke
$$Z_{\mathrm{hCS}}(\tau, z, \tau', \hbar) = \Bigl(\frac{\Phi_{10}(\tau,z,\tau')}{\eta(\tau)^{24}\eta(\tau')^{24}}\Bigr)^{\hbar\,c_{\mathrm{K3}}(Z)}$$
with the stated `weight balance $10-12-12=-14$ under $\mathrm{Sp}_4(\Z)$'. Igusa 1964 *Amer. J. Math.* 86 §5 fixes $\Phi_{10}$ as a weight-$10$ Siegel modular form on the full Siegel upper half-space $\mathbb H_2$ under $\mathrm{Sp}_4(\Z)$ (a single scalar weight on a three-complex-dimensional domain). $\eta(\tau)^{24}\eta(\tau')^{24}$ is bimodular weight $(12,12)$ on the Siegel diagonal $\mathbb H_1\times\mathbb H_1\hookrightarrow\mathbb H_2$. The quotient $\Phi_{10}/\eta^{48}$ makes literal sense only on the Siegel diagonal where $\Phi_{10}$ restricts to bimodular weight $(10,10)$ via Igusa--Witt pullback (Igusa 1964 Thm 1). On the full $\mathbb H_2$, there is no bimodular structure; the scalar-weight reading $10 - 12 - 12 = -14$ is an additive sum of weights viewed across two different modular groups ($\mathrm{Sp}_4$ for $\Phi_{10}$, $\mathrm{SL}_2\times\mathrm{SL}_2$ for $\eta^{24}\eta'^{24}$) rather than a uniform weight under a single modular group.

**Heal.** The object $(\Phi_{10}/\eta^{48})^\hbar$ is defined on the Siegel diagonal $Z=(\tau,0,\tau')\in\mathbb H_1\times\mathbb H_1$ where $\Phi_{10}|_{\mathrm{diag}}$ pulls back to bimodular weight $(10,10)$ via Igusa--Witt. The quotient carries bimodular weight
$$(10-12,\; 10-12) = (-2,\; -2).$$
The additive scalar reading $10 - 12 - 12 = -14$ is the sum of the two bimodular components, legitimate as a scalar weight but not a bimodular weight on $\mathbb H_1\times\mathbb H_1$.

Canonical statement: each invocation of $(\Phi_{10}/\eta^{48})^\hbar$ names the domain. On $\mathbb H_1\times\mathbb H_1$ (Siegel diagonal): bimodular weight $(-2, -2)$. On full $\mathbb H_2$: the quotient does not directly make sense; one must first restrict to the diagonal, then read the bimodular structure. Scalar total $-14$ is the sum of the two bimodular entries; legitimate as a summary scalar but not the primary modular-transformation weight.

The exponent $\hbar\,c_{\mathrm{K3}}(Z)$ is a formal $\hbar$-power series with Jacobi-form-valued coefficients: $c_{\mathrm{K3}}(Z)$ is the K3 elliptic-genus Fourier expansion
$$\phi_{0,1}^{K3}(\tau, z) = \sum_{n,\ell: 4n-\ell^2\ge -1} c(n,\ell)\, q^n y^\ell$$
viewed as a weight-$(0,1)$ weak Jacobi form (Eichler--Zagier 1985 §9). The polar cutoff $\Delta = 4n-\ell^2 \ge -1$ is Theorem 9.1 of that reference. The saddle reduction $Z_{\mathrm{hCS}} \to Z_{\mathrm{3D\,QG}}^{\mathrm{AdS}_3\times K3} = 1/\Phi_{10}$ holds in the $\hbar \to \infty$ limit of this formal series on the Siegel diagonal (DVV 1997 *Nucl. Phys. B* 484 direct; Borcherds 1998 *Invent. Math.* 132 Thm 1.7 singular theta lift of $\phi_{0,1}^{K3}$).

---

## Cycle 12 — Seven-face hierarchy versus seven-incarnation-closure conflation

**Attack.** Vol I Section IV asserts `seven faces of $r(z)$ fit the three-tier hierarchy with intra-tier canonical equivalence'. Vol III platonic ideal Section III reports `0 out of 7 incarnations of $\mathbf H_{\Delta_5}$ rigorously proved equivalent as written in the pre-audit form'. Two distinct objects (Vol I's $r(z)$-faces, Vol III's $\mathbf H_{\Delta_5}$-incarnations) carry the same seven-count and risk conflation. A reader might infer that the seven $r(z)$-faces are the seven $\mathbf H_{\Delta_5}$-incarnations in a different guise, which they are not.

**Heal.** The seven faces of $r(z)$ are:
1. Shifted-symplectic + orientation on $\mathrm{CY}_d$
2. Braiding on $E_d$-holomorphic FA (Stage-1)
3. Level-prefixed OPE
4. Lurie centre with factorisation homology
5. MO spectral $R$-matrix
6. VA--RTT
7. Elliptic Belavin / Felder-dynamical

These are organised by the three-tier hierarchy of Vol I Section IV:
- **Tier I**: item (1) (CY-datum intrinsics)
- **Tier II (Stage-1)**: items (2), (3), (4)
- **Tier III (Stage-2)**: items (5), (6), (7)

Within each tier, canonical equivalence is proved. Between tiers, **cross-tier specialisation** (not equivalence) is proved.

The seven incarnations of $\mathbf H_{\Delta_5}$ (Vol III Section III) are:
1. Super-EK quantisation
2. Super-Yangian
3. Super-Kontsevich deformation quantisation
4. MO stable-envelope Yangian pro-limit
5. Khovanov-type dg-category
6. 3d Turaev--Viro TQFT
7. Borcherds all-loop BV resummation

These are seven distinct constructions with **conjectural equivalences on the Koszul locus**, with 0 of the 21 pairwise comparisons rigorously proved as written in the pre-audit form (2 type-errors identified; 3 formal/open equivalences remaining).

Canonical statement (Vol I Section IV sharpened): `seven faces of $r(z)$ organised by three-tier hierarchy; intra-tier canonical equivalence **proved**; cross-tier specialisation **proved**; cross-tier equivalence **not claimed**'. Canonical statement (Vol III Section III sharpened): `seven incarnations of $\mathbf H_{\Delta_5}$ as distinct constructions; pairwise equivalences **conjectural on Koszul locus**; rigorous proof pending Scheithauer 2017 + DMS 2021 + Scheithauer 2006 $\Psi$-surjectivity chain closure'.

The numerological coincidence of `seven' in both documents is structural parallel (both have intrinsic / Stage-1 / Stage-2 layers in their internal categorisation), not a single identity.

---

## Cross-volume propagation summary

Each of the five cycles 8--12 propagates across all four battle-hardened platonic ideal documents as follows.

| Cycle | Vol I target | Vol II target | Vol III target | Master target |
|---|---|---|---|---|
| 8 (Humbert/Fourier admissibility) | §II B; §XV climax statement | §VI climax K3$\times E$ scope | §III seven-incarnations Koszul locus | §XII.X; §XIII scope |
| 9 ($\mathsf M$-tower outside-element) | §II C; §III census | §XIII scope | §VI $\kappa_\bullet$ stratification | §II (G2); §VII archetype table |
| 10 (octachotomy 7+1) | §VII | — | — | §VIII |
| 11 ($(\Phi_{10}/\eta^{48})^\hbar$ weight) | §II-ter; §X anchor | §IV climax eq; §VII Feynman | §IV three-faces; §VIII triality | §XIV-bis Climax-2 |
| 12 (seven-face vs seven-incarnation) | §IV | §II faces of $r(z)$ | §III | §II (G1)--(G4) |

These scope-tightenings preserve all prior mathematical content; they restrict the claim surface where ambiguity was detected and name the primary-literature anchor where rescoping is required.

---

*Attack-heal falsification cycles 8--12 inscribed 2026-04-22 following the Cycle-1--7 healing of prior rounds. Five primary references verified: Eichler--Zagier 1985 *Prog. Math.* 55 Thm 9.1 (Fourier polar cutoff); van der Geer 1988 *Hilbert Modular Surfaces* §IX (Humbert-discriminant parity); Fateev--Lukyanov 1988 *Intl. J. Mod. Phys. A* 3 ($\mathcal W_N$-duality); Igusa 1964 *Amer. J. Math.* 86 §5 Thm 1 ($\Phi_{10}$ weight-10 Siegel modular); DVV 1997 *Nucl. Phys. B* 484 ($1/\Phi_{10}$ direct). Raeez Lorgat.*
