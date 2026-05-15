# FRONTIER — Vol I Open Frontiers

The platonic-ideal frontier of Vol I: open mathematical problems whose
resolution would advance Theorems A, B, C, D, H or one of the five
archetypes G / L / C / M / B in load-bearing form. Each frontier
carries a hypothesis package, a reconstruction-theorem statement, and
a heal path. Wave numbers, drafting-history cascades, and
session-dated status snapshots are deliberately omitted — the
manuscript and `chapters/connections/master_concordance.tex` carry
the current state. Historical session records live in
`adversarial_swarm_*/`, `notes/rectification_map_*`, and the legacy
snapshots `notes/claude_md_legacy_*.md` /
`notes/agents_md_legacy_*.md`.

---

## Manuscript layout (six-part platonic ideal)

| # | Part | Beilinson level | Theorem |
|---|------|-----------------|---------|
| I  | Foundations and the Open Beilinson Tower | 0–1 | Morita reconstruction |
| II | The Bar–Cobar Engine                     | 1↔2 | Theorem A |
| III| The Bulk                                 | 3   | Theorems H, B |
| IV | The Five-Archetype Landscape             | —   | Theorem C ($5{\times}5$ matrix) |
| V  | The Modular Tower                        | 4–5 | Theorem D |
| VI | Seven Faces and the Frontier             | —   | Master Reconstruction (climax) |

The Master Reconstruction Theorem at the close of Part VI subsumes
Theorems A through H as corollaries restratified by Beilinson-tower
level; KSDual is the $\mathbb{Z}/2$-fixed sublocus where every
forgetful step degenerates from adjunction to strict equivalence;
cross-volume vertical equivalences to Vols II / III are inscribed at
levels 0, 2, and 4.

---

## The proved core

| Theorem | Statement | Level | Status |
|:-------:|-----------|:-----:|--------|
| **A** | $K^2 \simeq \mathrm{id}$ on $\mathrm{Kosz}(X)$ | 1 ↔ 2 | ProvedHere on a fixed smooth curve at $(\infty,2)$-properad level (`thm:A-infinity-2`); modular-family extension over $\overline{M}_{g,n}$ conditional on Francis–Gaitsgory six-functor base-change + log-FM nodal-sewing |
| **B** | $\Omega(B(C)) \xrightarrow{\sim} C$ in $D^{\mathrm{co}}_{\mathrm{ch}}(X)$ | 1 → 3 | ProvedHere on Koszul locus (class G/L explicit MacLane-splitting); class M chain-level original-complex genuinely false in $\mathrm{Ch}(\mathrm{Vect})$, true in completed / pro / weight-completed / $J$-adic ambients |
| **C** | $\kappa + \kappa^!$ ceiling per family stratum | 5 (per stratum) | C0/C1 ProvedHere on Koszul locus; C2 shifted-symplectic / BV upgrade conditional on the BV package; +3-shift contradiction at $g=0$ resolved via `thm:theorem-C-g0` |
| **D** | $\mathrm{obs}_g = \kappa \cdot \lambda_g$ uniform-weight, all $g \ge 1$ | 4 (on $\overline{M}_{g,n}$) | ProvedHere; multi-weight extension carries cross-channel correction $\delta F_g^{\mathrm{cross}}$; clutching-uniqueness pins the scalar |
| **H** | $\mathrm{ChirHoch}^\bullet \subset \{0,1,2\}$ on Koszul locus, generic level | 3 | ProvedHere; Feigin–Frenkel companion at $k = -h^\vee$ (infinite-dim centre, non-exclusion) |

**Master conjectures MC1–MC5** all proved at their inscribed scopes.
MC3 proved on the evaluation-generated core (per AP47); MC5 analytic,
coderived, and canonical-ambient chain-level proved; class-M MC5 holds
on the coderived / pro-object / weight-completed / $J$-adic ambient,
while the raw direct-sum ambient $\mathrm{Ch}(\mathrm{Vect})$ remains
the naive-ambient exception (concordance.tex:1980).

**Universal chain-homotopy normalisation** (load-bearing):
$h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ where
$\mathcal N(A_b) = \kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$ is the
Verdier-Ran-on-bar norm at level 2 (Convention
`conv:A-two-kappa-shriek` of `theorem_A_infinity_2.tex`). Distinct
from the algebra-level scalar Verdier sum $K^\kappa(A_b)$ of
`master_concordance.tex`. Archetype witnesses
$\mathcal N(\mathsf G)=1$, $\mathcal N(\mathsf L)=2(k+h^\vee)$,
$\mathcal N(\mathsf C)=1$, $\mathcal N(\mathsf M)=c(5c+22)/10$,
$\mathcal N(\mathsf B)=8$ inscribed in
`chapters/theory/theorem_A_infinity_2.tex`.

**Universal Borcherds-weight identity**:
$\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ for
$N \in \{1, 2, 3, 4, 6\}$ plus half- / quarter-integer continuations.
Replaces the additive
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$,
which fails at every $N$ including $N = 1$.

---

## Open frontiers

### F1 — W(p) triplet placement

The logarithmic triplet $W(p)$ ($p \ge 2$) is currently outside the
G / L / C / M four-class partition. The Adamovic–Milas
character-amplitude bound is the candidate path.

- **Hypothesis package**: extend the partition to a five-class
  G / L / C / M / log including unbounded-Massey LCFTs.
- **Reconstruction theorem**: replace Zhu-bounded-Massey with direct
  character-amplitude growth.
- **Heal path**: inscribe the Adamovic–Milas amplitude bound; verify
  the partition is exhaustive.

### F2 — Multi-weight cross-channel correction

Theorem D extension: $\mathrm{obs}_g = \kappa \cdot \lambda_g$
uniform-weight is proved; the multi-weight version carries an
explicit $\delta F_g^{\mathrm{cross}}$. The closed form for
$\delta F_g^{\mathrm{cross}}$ at $g \ge 2$ is open.

- **Hypothesis package**: Hodge bundle over $\overline{M}_{g,n}$ with
  multi-weight stratification; explicit cross-channel cocycle.
- **Reconstruction theorem**: $\delta F_g^{\mathrm{cross}}$ in terms
  of named cohomology classes on $\overline{M}_{g,n}$.
- **Heal path**: compute $g = 2$ from first principles in `compute/`.

### F3 — Class M strict chain-level $E_3$-topological structure

Class M chain-level $E_3$-topological structure in
$\mathrm{Ch}(\mathrm{Vect})$ remains genuinely open; the
weight-completed, pro-object, and $J$-adic ambients are
unconditional. The Felder BRST chain-level bridge is the candidate.

- **Hypothesis package**: explicit Mittag–Leffler tower in
  $\mathrm{Ch}(\mathrm{Vect})$ converging to the weight-completed
  result.
- **Reconstruction theorem**: chain-level $E_3$-action via Felder
  BRST in original complex.
- **Heal path**: inscribe the Mittag–Leffler tower; verify chain
  homotopies in `compute/`.

### F4 — Theorem B at nodal boundary off Koszul locus

Theorem B chain-level on a smooth curve is proved; the nodal
boundary statement requires either Koszul hypothesis or Mok25-style
nodal-sewing data.

- **Hypothesis package**: log-FM nodal-sewing data on
  $\overline{M}_{g,n}$ + Koszul hypothesis on the boundary stratum.
- **Reconstruction theorem**: extension of $\Omega(B(C))
  \xrightarrow{\sim} C$ to nodal $C$ with prescribed clutching.
- **Heal path**: Mok25 + chain-level nodal clutching at separating /
  non-separating boundary divisors.

### F5 — Drinfeld-double global obstruction at $g \ge 1$

The universal Drinfeld double $D(A, A^!)$ exists globally over
$\overline{M}_{g,n}$ for $g = 0$ unconditionally and extends to
$g = 1$ via Enriquez's $\mathrm{GRT}_1^{\mathrm{ell}}(\mathbb{Q})$.
For $g \ge 2$, the explicit cohomological obstruction is
$\mathrm{obs}^{(1)}_{\mathrm{double}} \in H^2(\mathfrak{grt}^{\mathrm{ell}},
\mathfrak{sp}(A) \otimes \mathfrak{sp}(A^!))$
with elliptic 2-cocycle $\omega_{\mathrm{ell}} = \wp(\tau) \cdot \langle\cdot,\cdot\rangle_{\mathfrak{sp}}$;
**vanishes iff $r_{\max}(A) = 2$** (class G only). All of L, C, M, B
are $g \ge 1$ obstructed.

- **Hypothesis package**: $r_{\max}(A) = 2$.
- **Reconstruction theorem**: vanishing of
  $\mathrm{obs}^{(1)}_{\mathrm{double}}$ in
  $H^2(\mathfrak{grt}^{\mathrm{ell}}, \cdot)$.
- **Heal path**: explicit cocycle calculation per archetype.

### F6 — Theorem H on the nodal boundary without Koszul hypothesis

Hochschild concentration $\subset \{0, 1, 2\}$ on the smooth Koszul
locus is proved. Extension to the nodal boundary without Koszul
hypothesis is open.

- **Hypothesis package**: factorisation algebra on the nodal locus
  with non-Koszul stratification.
- **Reconstruction theorem**: Theorem H on nodal $C$.
- **Heal path**: separating / non-separating nodal sewing of
  $\mathrm{ChirHoch}^\bullet$.

### F7 — MC4 completion / H3 failure regime (coderived control)

The non-finitely-generated MC4 regime, where the H3 finite-dim graded
hypothesis fails, requires coderived-only $K^2 \simeq \mathrm{id}$
control via Chenevier determinants at irregular primes.

- **Hypothesis package**: Chenevier-determinant control at
  $p \in \{691, 3617\}$ via Kubota–Leopoldt + Herbrand–Ribet.
- **Reconstruction theorem**:
  $\mathrm{det}\,\rho_{S_{11}(V_1(\mathfrak{g})), 691}
  = \chi_{\mathrm{cyc}}^{11} \cdot \epsilon_{B_{12}} \mod 691$.
- **Heal path**: extend the Chenevier identity to all $r \ge 5$
  irregular-prime levels.

### F8 — Chart-class enumeration per archetype

For each archetype G / L / C / M / B, enumerate the
Morita-equivalence classes of chart presentations $(\mathcal{C}, b)$.
Whether each archetype has one Morita class or several determines
whether the five-archetype dichotomy is chart-independent or
chart-bound.

- **Hypothesis package**: factorisation dg-cat
  $\mathcal{C}^{\mathrm{op}}$ on $(X, D, \tau)$ with chart $b$.
- **Reconstruction theorem**: Morita-class invariance of the
  five-archetype label.
- **Heal path**: inscribe the chart-class enumeration in
  `chapters/examples/landscape_census.tex`; verify Morita-class
  stability of the five-archetype dichotomy.

### F9 — Functor-level CY → chiral two-stage equivalence at $d \ge 4$

The two-stage factorisation $\Phi_d^{(\Sigma_{d-1}, C)} =
\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C} \circ \Phi_d^{\mathrm{FA}}$
is proved at object level for $d \le 3$ on the K3-Class A locus and
functor level at $d \le 2$. The functor-level statement at $d \ge 4$
requires Kontsevich–Tamarkin $E_d$-formality of the CY$_d$ category
(not the operad), proved at $d \le 3$ via three-vanishing.

- **Hypothesis package**: category-level $E_d$-formality of
  $\mathrm{HH}^\bullet(\mathcal{C})$ at $d \ge 4$.
- **Reconstruction theorem**: $\Phi_d^{(\Sigma_{d-1}, C)}$ as a
  natural transformation of symmetric-monoidal $(\infty,1)$-functors.
- **Heal path**: extend the three-vanishing to $d \ge 4$ or find an
  alternative category-level formality argument. Cross-volume Vol III
  frontier.

### F10 — Pixton ideal from class-M shadows

Class-M algebras are conjectured to generate the Pixton ideal via the
infinite MC tower. Computationally supported at $g = 2, 3$.

- **Hypothesis package**: tautological ring on $\overline{M}_{g,n}$;
  Pixton's three-spin relations.
- **Reconstruction theorem**:
  $\langle \kappa_M \cdot \lambda_g \rangle = $ Pixton ideal.
- **Heal path**: extend the $g \le 3$ computation to $g = 4$;
  verify ideal-theoretic generation.

### F11 — Operator-level Pfaffian for $\Delta_5$

The Igusa cusp form $\Delta_5$ is the Borcherds denominator and
protected scalar shadow on K3 × E. The construction of an
operator-level object whose protected Pfaffian is $\Delta_5$ is open.

- **Hypothesis package**: virtual $K_0$-determinant package +
  Hall–Borcherds residual.
- **Reconstruction theorem**:
  $\mathrm{Pf}\,(\mathcal{O}_{\mathrm{op}}) = \Delta_5$.
- **Heal path**: cross-volume Vol III + `~/igusa-cusp-form`.

### F12 — Compact dynamical-metric path integral from algebraic HT sector

The Vol II climax theorem identifies the algebraic holographic HT
sector with $\partial = A$, bulk $= Z^{\mathrm{der}}_{\mathrm{ch}}(A)$,
interaction $= \mathsf{SC}^{\mathrm{ch,top}}$-brace. Construction of a
compact dynamical-metric path integral from this sector requires the
Hall–Borcherds residual and BTZ / Cardy hypotheses (modular
invariance + vacuum dominance + saddle).

- **Hypothesis package**: BTZ / Cardy + Maloney–Witten +
  Manschot–Moore Farey-tail completion.
- **Reconstruction theorem**:
  $Z_{\mathrm{3d\ QG, Virasoro}}(S^2 \times S^1_\tau) =
  q^{(1-c)/24} (1-q)/\eta(\tau)$ as the gravity-line completion.
- **Heal path**: cross-volume Vol II + `~/topological-strings`.

---

## Cross-volume vertical equivalences

| Level | Vol I (Open) | Companion |
|:-----:|--------------|-----------|
| 0 | factorisation dg-cat on $(X, D, \tau)$ | Vol III: CY-cat via 6d hCS, formal locus + global descent (anomaly **quartic** $\int_X \mathrm{Tr}_{\mathrm{ad}}(A(F_A)^3)$) |
| 1 | chart $A_b$ | Vol III: $\Phi_d^{\mathrm{FA}}$ |
| 2 | bar $B(A_b)$ | Vol III: $\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1}, C}$ |
| 3 | derived chiral centre | Vol II: $\mathsf{SC}^{\mathrm{ch,top}}$-brace bulk (climax) |
| 4 | line / brane operators | Vol III: Drinfeld double $G(X) = D(Y^+(X))$ + descent |
| 5 | modular trace + clutching | Vol III: $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$; Vol II: gravity-line completion |

---

## The 5 × 5 $\kappa$-stratification matrix

Each archetype G / L / C / M / B admits five $\kappa$-measurements:
$\{\kappa_{\mathrm{cat}}, \kappa^{\mathrm{Hodge}}_{\mathrm{ch}},
\kappa^{\mathrm{Heis}}_{\mathrm{ch}}, \kappa_{\mathrm{BKM}},
\kappa_{\mathrm{fiber}}\}$. K3 × E anchors row B at $(0, 0, 3, 5, 24)$.
The remaining 24 entries are computed and 3-path verified in
`compute/tests/test_kappa_stratification.py`. The collapse pattern
across rows is itself a refined classification axis.

---

## The seven faces of $r(z)$

Refined to two GRT-orbits + Brown motivic bridge:

- **Orbit I (algebraic, 5 faces)**: F1 bar collision residue;
  F2 KZ associator $\Phi_{\mathrm{KZ}}$; F3 Yangian $R(z)$;
  F5 Drinfeld double $D(A, A^!)$; F7 Wick / trace-form $r$-matrix.
- **Orbit II (geometric, 2 faces)**: F4 KZ flat sections;
  F6 FM residue stratum.
- **Brown motivic bridge** at binary degree connects Orbit I to
  Orbit II.

All six historical $\Phi_{1i}$ ($i = 2, \ldots, 7$) lie in
$\mathrm{GRT}_1^{\mathrm{fin}}(\mathbb{Q})$ (Drinfeld 1989/1991,
Furusho 2010). $F_8$ Brown motivic and $F_9$ Willwacher graph cocycle
exit $\mathrm{GRT}_1^{\mathrm{fin}}$ and live in the full motivic
Galois group of $\mathrm{MTM}$ over $\mathrm{Spec}(\mathbb{Z})$
(Brown 2012; Deligne–Ihara injectivity conjectural).

---

## Reading guide

For the platonic-ideal architecture: `./CLAUDE.md`, `./AGENTS.md`,
`chapters/connections/master_concordance.tex`.

For canonical formulas: `chapters/examples/landscape_census.tex`.

For anti-patterns and master patterns MA-1 … MA-13:
`notes/antipatterns_catalogue.md`.

For the first-principles confusion-pattern registry:
`notes/first_principles_cache_comprehensive.md`.

For independent verification:
`notes/INDEPENDENT_VERIFICATION.md`,
`compute/lib/independent_verification.py`.

For cross-volume bridges: Vol II `~/chiral-bar-cobar-vol2`,
Vol III `~/calabi-yau-quantum-groups`, adjacent
`~/igusa-cusp-form`, `~/topological-strings`.

For the historical record: `notes/claude_md_legacy_*.md`,
`notes/agents_md_legacy_*.md`,
`adversarial_swarm_*/SYNTHESIS*.md`,
`notes/rectification_map_*.md`. Grep by index — do not read whole.
