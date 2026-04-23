# Wave Supervisory — Vol III main.tex Part Re-architecture — Upgrade 2026-04-22

**Status.** Lossless appendix to `wave_supervisory_volIII_part_rearchitecture.md` (2026-04-16, 644 lines). The 2026-04-16 document stands verbatim; the Option C decision is preserved; the seven-Part four-pillar layout of §§3–5 is preserved; the fourteen-step migration checklist of §VIII is preserved. The reconstitution waves 11–19 (2026-04-17 through 2026-04-22, catalogued in `PLATONIC_MANIFESTO_VOL_III_FRONTIER_RECONSTITUTION_20260422.md`) return four architectural refinements to the four Part-openers and one execution-status update to the migration checklist. Section numbering continues from §12 of the source document.

**Author.** Raeez Lorgat. **Date.** 2026-04-22. **Cross-volume siblings.** `PLATONIC_MANIFESTO_UPGRADE_20260422.md` (Vol I sister upgrade, §§XII–XVII), `PLATONIC_MANIFESTO_VOL_III_FRONTIER_RECONSTITUTION_20260422.md` (Vol III reconstitution, §§I–XII), `UNIVERSAL_TRACE_IDENTITY.md` (cross-volume centrepiece).

---

## §13. Pillar α Part II opener — two-stage factorisation precedes per-$d$ specialisation

The 2026-04-16 Part II opener (source §5, Theorem Platonic Φ) states Φ as one symmetric-monoidal $(\infty,1)$-functor with $n = n_{\mathrm{native}}(d)$. The reconstitution §II sharpens: Φ factors canonically,
$$
\Phi_d \;=\; \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d \;:\;
\mathrm{CY}\text{-cat}_d \xrightarrow{\Phi^{\mathrm{FA}}_d} E_d\text{-}\mathrm{HolFA}(X)
\xrightarrow{\mathrm{Sp}_{\Sigma_{d-1}, C}} E_1\text{-}\mathrm{ChirAlg}(C),
$$
Stage 1 canonical up to contractible choice, Stage 2 the choice of transverse cycle $\Sigma_{d-1} \subset X$ and reference curve $C \subset X$. The four universal properties (U1)–(U4) are properties of Stage 1 alone.

**Opener rewrite.** Stage 1 is stated canonical first; Stage 2 specialisation second:

> **Theorem (Platonic Φ, two-stage form).** *There exists a unique symmetric-monoidal $(\infty,1)$-functor $\Phi^{\mathrm{FA}}_d: \mathrm{CY}_d\text{-Cat} \to E_d\text{-}\mathrm{HolFA}(X)$ characterised by (U1) Hochschild pullback, (U2) CY-morphism functoriality, (U3) Drinfeld-centre compatibility, (U4) standard-input recovery. For every $\Sigma_{d-1} \subset X$ and $C \subset X$, fibrewise factorisation homology defines $\mathrm{Sp}_{\Sigma_{d-1}, C}: E_d\text{-}\mathrm{HolFA}(X) \to E_1\text{-}\mathrm{ChirAlg}(C)$; the CY-to-chiral functor is the composition $\Phi_d = \mathrm{Sp}_{\Sigma_{d-1}, C} \circ \Phi^{\mathrm{FA}}_d$.*

At $d = 3$ Stage 1 is realised by Costello–Gwilliam observables of 6D holomorphic Chern–Simons: $\mathrm{Obs}_{\mathrm{hCS}}(X) \simeq \mathrm{CE}^{\bullet}_{\bar\partial, \mathrm{chir}}(\mathcal{E}_{\mathrm{hCS}}, \mathcal{O}_X)$ as an $E_3$-algebra in $\mathrm{Ch}(\mathrm{Dolb})$, Bochner–Martinelli propagator, $\pi_1(S^5) = 0$ commutativity. The apparent conflict "$\Phi$ produces $E_d$-chiral" vs "$\Phi$ produces $E_1$-chiral" dissolves: Stage 1 outputs $E_d$-hFA on $X$, Stage 2 outputs $E_1$-chiral on $C$; both native, different targets. Corollaries Φ.1–Φ.4 re-read as Stage-2 specialisations (Φ.1: $\Sigma_0 = \mathrm{pt}$; Φ.2: Nakajima $S^1 \subset K3$; Φ.3: K3-fibre in $K3 \times E$; Φ.4: higher-codimension choice).

---

## §14. Pillar β Part V opener — eight rows under cover-assignment spread

The 2026-04-16 Part V opener states $\kappa_{\mathrm{BKM}} = c_N(0)/2$ for $N \in \{1, \ldots, 8\}$ on the diagonal symplectic family. The reconstitution §IV sharpens: the identity holds **uniformly across all eight diagonal-divisor Gritsenko–Cléry paramodular cusp forms** under the cover assignment $\{\mathrm{Sp}_4, \mathrm{Mp}_4, \widetilde{\mathrm{Mp}}_4\}$ selected by weight integrality of $\Phi_N$.

**Opener rewrite.** The eight forms are $\{\Delta_5, \Delta_2^{(2)}, \Delta_1^{(3)}, \Delta_1^{(4)}, \Delta_{1/2}^{(5)}, \Delta_1^{(6)}, \Delta_{1/4}^{(7)}, \Delta_0^{(8)}\}$ with constant Fourier coefficients $\{10, 4\text{ or }8, 2\text{ or }6, 2\text{ or }4, 1, 2, 1/2, 0\}$. Integer weights $N \in \{1, 2, 3, 4, 6\}$ lift to $\mathrm{Sp}_4(\mathbb{Z})$; half-integer $N = 5$ requires Bruinier 2002 metaplectic $\mathrm{Mp}_4$; quarter-integer $N = 7$ requires the Freitag–Hermann 1985 spin double cover $\widetilde{\mathrm{Mp}}_4$; weight zero at $N = 8$ is the abelian-lattice endpoint. The two convention values at $N \in \{2, 3, 4\}$ reflect the $Z^{(g)}_{K3} = 2\,\phi^{(g)}_{0,1}$ normalisation ambiguity (square-root vs direct); both canonical. AP-CY37 (naïve $\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})$ as $N = 1$ coincidence) preserved as guard.

The **two-scope split** is named explicitly:
- *BKM-denominator scope*, CHL subset $N \in \{1, 2, 3, 4, 6\}$ ($\varphi(N) \mid 2$): each $\Phi_N$ is the GKM superalgebra denominator on twisted reduced DT moduli, character $-1/\Phi_N^2$, conditional on Bryan–Oberdieck 2018.
- *Borcherds-weight scope*, full class $N \in \{1, \ldots, 8\}$: singular theta lift of a twined weak Jacobi form, weight $c_N(0)/2$ read directly off the constant Fourier coefficient.

Per-form host-CY catalogue: $N = 1$ on $K3 \times E$; $N \in \{2, 3, 4, 6\}$ on $(K3 \times E)/(\mathbb{Z}/N)$; $N = 5$ on Borcea–Voisin $(S_5 \times E_5)/(\iota_S \times \iota_E)$; $N = 7$ on $(K3 \times E)/\mathbb{Z}_7$ with order-4 Cheeger–Simons gerbe; $N = 8$ on the Mongardi–Tari–Wandel Kummer-3 hyperkähler fourfold. The Vol I partner is the $K^c_N = 4N^3 - 2N - 2$ cubic of the W$_N$ family; the Universal Trace Identity is an eight-voice cross-volume cadence (sister §XII).

---

## §15. Pillar γ Part III opener — 6D hCS observables realise Level 3 concretely

The 2026-04-16 Part III opener states CY-A$_3$ inf-categorically: $HH^{-2}_{E_1}(A,A) = 0$, Goodwillie layers vanish, $E_3$-liftings contractible. The three-level taxonomy (chain / operadic / inf-cat, `def:three-levels` in `m3_b2_saga.tex`) is preserved. The reconstitution §II–V supplies the concrete Level-3 realisation the 2026-04-16 opener lacked: Costello–Gwilliam observables of 6D hCS at $d = 3$ as an explicit $E_3$-algebra in $\mathrm{Ch}(\mathrm{Dolb})$, sum-over-shuffles associativity by Čech–Dolbeault Mayer–Vietoris on $\overline{\mathrm{Conf}}_n(\mathbb{C}^3)$, Bochner–Martinelli propagator.

**Opener rewrite.** The taxonomy now integrates the concrete $E_3$-algebra at Level 3:
- *Level 1 (strict chain, often fail):* $[m_3, B^{(2)}] \neq 0$ per-$k$ cyclic invariance.
- *Level 2 (total-cohomology operadic):* $\{b, B^{(2)}\}$ total via Costello TCFT, conjecture-status per AP40.
- *Level 3 (inf-categorical, always hold):* realised concretely at $d = 3$ by $\mathrm{Obs}_{\mathrm{hCS}}(X)$ as an $E_3$-algebra; $E_3$-liftings contractible by Goodwillie-layer vanishing plus Costello–Li BV-anomaly $\kappa_{\mathrm{anom}} \propto \hbar A(\mathfrak{g}) \chi_{\mathrm{top}}(X) = 0$ on $\mathbb{C}^3$ and $K3 \times E$ (both $c_3 = 0$).

The non-abelian ADE all-orders theorem $\partial\,\mathrm{hCS}_5(\mathfrak{g}) \simeq Y_{\epsilon_1, \epsilon_2, \epsilon_3}(\widehat{\mathfrak{g}})$ (reconstitution §V) enters as **Corollary γ.2**: Level 3 at $d = 3$ supplies the quantum-group target of Stage-2 specialisation at $K3 \times E$. The $[m_3, B^{(2)}]$ saga, dualisability scope (Gwilliam–Williams 2021 Proposition 5.3.2 non-abelian infinity; Serre–Grothendieck recovery on compact CY$_3$), and Francis–Gaitsgory / Fresse compatibility are absorbed as three Wave 13–18 refinements in the opener-proof expansion.

---

## §16. Pillar δ Part IV opener — six-route convergence as three-tier hierarchy

The 2026-04-16 Part IV opener states Theorem δ (K3 Abelian Yangian) with Corollary δ.1 "six routes are six specialisations of Φ". The reconstitution §VI restructures the six-route claim: arithmetic faces of $r_{\mathrm{CY}}$ on $K3 \times E$ sort into **three tiers**, and only Tier (iii) faces are genuine siblings in the two-stage sense.

**Opener rewrite.**
- *Tier (i) CY-datum intrinsics:* Mukai lattice $(\Lambda_{\mathrm{Muk}}, (4, 20))$; Hodge supertrace $\kappa_{\mathrm{ch}}(K3 \times E) = 0$. Read directly off $X$.
- *Tier (ii) Stage-1 invariants of $\mathcal{F}_{K3 \times E}$:* K3-fibre rank $\kappa_{\mathrm{fiber}} = 24$ (Mukai 1988); $\kappa_{\mathrm{cat}} = \chi(\mathcal{O}_{K3 \times E}) = 0$ Künneth-multiplicative.
- *Tier (iii) $(\Sigma_2, C)$-specialisations:* BKM $\mathfrak{g}_{\Delta_5}$ with $\kappa_{\mathrm{BKM}} = 5$; Niemeier 23-twist family; Humbert boundary at $H_1 \cup H_4$; CHL $\mathbb{Z}/N$-family at $N \in \{1, 2, 3, 4, 6\}$.

Four routes are Tier-(i)/(ii) invariants of the same $\mathcal{F}_{K3 \times E}$; the rest are Tier-(iii) specialisations at different $(\Sigma_2, C)$ choices. Convergence is the content of the two-stage factorisation §13 read on one canonical Stage-1 object, not a six-way coincidence. AP-CY60 is preserved as a guard; the upgrade promotes it from "convergence conjecture" to "structured hierarchy".

The Maulik–Okounkov $R$-matrix as gluing-cocycle residue $R^{\mathrm{MO}}_{C_+ C_-}(u) = \mathrm{Res}_{u = u_\star} \phi^+_{UV}(u)$ enters as the concrete Tier-(iii) mechanism; Yang–Baxter descends from Koszul-homotopy cocycle closure. The algebraic-seven of `cy_holographic_datum_master.tex` is an orthogonal slicing of the same $\mathcal{F}_{K3 \times E}$, not a competing seven. The sibling catalogue §VII (Borcherds Monster at $d = 3$ on $(T^{24}_{\mathrm{Leech}} \times E)/\mathbb{Z}_2$; Igusa $\mathfrak{g}_{\Delta_5}$ at $d = 3$; Fake Monster at $d = 5$ on $K3 \times K3 \times E$) attaches as Remark δ.2, resolving the 2026-04-16 Fake-Monster-at-$d = 3$ confusion (Retraction #4).

---

## §17. Migration checklist §VIII — execution status under the 2026-04-22 inscription wave

The fourteen-step checklist of source §VIII remains in force unchanged. The 2026-04-22 wave has executed approximately 8–10 of 14 steps; the content-inscription and cross-volume axes are substantially complete, the structural `\part` restructure remains pending.

**Executed or substantially in progress:**
- **Step 1** (pre-flight inventory) — done; 0 cross-volume Part-references confirmed.
- **Step 3** (new chapter files) — partial: `chapters/theory/phi_universal_trace_platonic.tex` inscribed; `diagonal_siegel_orbifolds.tex`, `universal_trace_identity.tex`, and the three frontier chapters (nonabelian Yangian, ZTE, root of unity) pending.
- **Step 4** (stub development in pillar context) — `quantum_groups_foundations.tex` rectified through multiple CG-rectify passes 2026-04-20 through 2026-04-22; `modular_koszul_bridge.tex`, `geometric_langlands.tex`, `matrix_factorizations.tex` present with ongoing rectification.
- **Step 8** (kappa-spectrum appendix) — partial via Vol I/III eight-row inscription; Vol III-side table update pending.
- **Step 9** (cross-volume `\ref` audit) — done; zero current cross-volume Part-references to Vol III, alias strategy unneeded.
- **Step 11** (independent verification anchor) — partial: $\Phi$ universality engines running under `make test`; 5/283 coverage target not yet achieved.
- **Step 12** (tautology registry healings) — four of five entries healed: Entry #1 $\kappa_{\mathrm{BKM}}$ scope (eight-row in `k3e_bkm_chapter.tex`), Entry #3 Costello TCFT downgrade, Entry #4 $P_2 = 0$ status downgrade, Entry #5 six-routes rewrite (three-tier §16 above). Entry #2 CY-A$_3$ scope restriction pending.
- **Step 13** (CLAUDE.md update) — done: `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md` reflects four-pillar architecture, seven parts, two-stage Φ, eight-row BKM.

**Not yet executed:**
- **Step 2** (new Part-opener prose blocks) — six openers pending in `notes/` draft form.
- **Step 5** (restructure `main.tex` `\part` declarations) — `main.tex` retains the old seven-Part layout (Foundations / CY-to-Chiral / $E_n$ Hierarchy / K3 Yangian / CY Landscape / Seven Faces / Frontiers); pillar-anchored renaming pending.
- **Step 6** (chapter `\input` relocations) — `m3_b2_saga.tex`, `modular_trace.tex`, `modular_koszul_bridge.tex` still in 2026-04 positions.
- **Step 7** (reading-paths block) — `chapters/theory/introduction.tex` reading paths pre-rearchitecture.
- **Step 10** (build verification) — partial.
- **Step 14** (single commit) — open.

**Structural observation.** The wave has attacked content-inscription (Steps 3, 4, 12) and cross-volume / CLAUDE.md axes (Steps 9, 13), which proceed independently of the `\part` restructure. The structural axis (Steps 2, 5, 6) is the single pending migration move. The §9 risk assessment holds: principal risk is AP-CY27 / FM42 bulk-substring corruption on Part-rename, mitigated by per-Part Edit discipline.

Cross-volume harmony §11 is strengthened. Vol I has adopted the two-stage Pillar 1 location (sister §XIII), the eight-row Pillar 2 partner (sister §XII), and the positive-geometry grammar alongside Pillar 3 (sister §XIV). The Vol III Part V opener (Pillar β) and Vol I Part III opener (Pillar 2) now carry the same eight-row spread under the same cover assignment; the Universal Trace Identity is an eight-voice cross-volume cadence, not a single-note equality.

The Platonic form of the geometric-register programme is fully specified. What remains is to execute Steps 2, 5, 6, 7, 10, 14 — the structural restructure of `main.tex` around the four-pillar spine.

— Raeez Lorgat, 2026-04-22
