# Wave 12 — Vol II Standalones (adversarial audit)

**Date**: 2026-04-16
**Scope**: `~/chiral-bar-cobar-vol2/standalone/` (8 files; 3,855 lines total)
**Methodology**: read-only adversarial review (Read/Grep/Bash). Cross-referenced V2-AP catalogue (`~/chiral-bar-cobar-vol2/CLAUDE.md`) and Vol I prior wave findings (waves 2, 6, 7, 11). No edits, no commits.
**Posture**: heal by realising the strongest possible mathematical statement; downgrade only when no upgrade path exists.

The Vol II standalone directory is a less-attacked surface than the chapters. It is NOT a single coherent set: it mixes (a) one large preface-style survey (~1,759 lines, no bibliography, depends on chapter `\ref` keys), (b) one substantive monograph-shaped paper (`bar_chain_models...`, 875 lines, self-contained), (c) six 170--250 line "Annals-grade proof spine" sketches with storyboards. The audit found clear caveat-drift, two convention clashes within a single standalone (AP151 self-violation), and a documented inflated-counts pattern matching Vol I wave 6.

---

## Section 1 — Standalone inventory

| File | Lines | Topic | Form | Self-contained bib? |
|------|-------|-------|------|---------------------|
| `preface_full_survey.tex` | 1,759 | Volume preface (full survey) | Preface | NO (depends on chapter `\ref`/`V1-thm:` keys) |
| `bar_chain_models_chiral_quantum_groups.tex` | 875 | $E_1$-chiral QGs and the $E_N$ ladder | Article (5 sections + frontier) | YES (8 entries) |
| `stokes_gap_kzb_regularity.tex` | 248 | KZB regularity at generic level | Annals-grade spine | NO |
| `bcfg_chiral_coproduct_folding.tex` | 215 | Folding for $B_n,C_n,F_4,G_2$ | Spine + storyboard | NO |
| `class_m_global_triangle.tex` | 206 | Class M bulk-boundary-line triangle | Spine + storyboard | NO |
| `monster_voa_orbifold_e3.tex` | 190 | $V^\natural$ via orbifold hCS | Spine + storyboard | NO |
| `rpt_convergence_shapovalov.tex` | 185 | Vir spectral $R$-matrix = PT kernel | Spine + storyboard | NO |
| `curved_dunn_two_complex_bridge.tex` | 177 | Curved Dunn additivity bridge | Spine + storyboard | NO |

Status-bearing environments declared in standalones (theorem/proposition/lemma/conjecture):

```
bar_chain_models_chiral_quantum_groups.tex : 12
preface_full_survey.tex                    : (no \ClaimStatus*; uses \cite/\ref into chapters)
class_m_global_triangle.tex                :  5
bcfg_chiral_coproduct_folding.tex          :  5
stokes_gap_kzb_regularity.tex              :  5
rpt_convergence_shapovalov.tex             :  5
monster_voa_orbifold_e3.tex                :  4
curved_dunn_two_complex_bridge.tex         :  3
```

The seven non-preface standalones use bare AMS theorem environments (no `\ClaimStatus*` macros). Status is communicated by environment name and `[Proved]` / `[Target]` / `[Conjecture]` tags in brackets. This sidesteps the `\ClaimStatus*` regex audit but does NOT remove the substantive AP60 risk: the same conformance check applies to bare `\begin{theorem}` blocks.

---

## Section 2 — Status consistency

### 2.1 ProvedHere drift between standalones and parent chapters

The seven non-preface standalones do not use `\ClaimStatus*`. Status comparison is therefore between bracket tags (`[Proved]`, `[Target]`, `[Conjecture]`) and the underlying chapter ProvedHere/Conjectured tagging.

| Standalone claim | Bracket tag in standalone | Parent-chapter status | Consistent? |
|------------------|---------------------------|------------------------|-------------|
| `bar_chain_models` Thm 1.1 (Yangian as $E_1$-chiral QG) | `[Definition + Theorem]` | Vol II frontier (no bare $E_1$-chiral QG existence theorem in chapters; question:genuine-e1 is open) | **MISALIGNED**: standalone presents Yangian as instance of definition, but the construction of the chiral algebra structure on a curve is left as `\begin{question}` (Q5.2). Calling Section 1 "The Yangian as $E_1$-chiral quantum group" overstates: at present Yangian is a candidate. |
| `bar_chain_models` Thm 5.1 ("Topologisation for KM") | `[Theorem]`, `Proved for KM` | Vol II `holomorphic_topological.tex` and Vol I `thm:topologization` (PROVED, KM only). | OK (both scope to KM; W-algebras moved to corollary). |
| `bar_chain_models` Conj 5.2 ("Topologisation general") | `[Conjecture]` | Vol I `conj:topologization-general`, Vol II `conj:E3-topological-climax` (CONJECTURAL). | OK. |
| `class_m_global_triangle` Prop 3.1 (DS--Hochschild) | `[Proposition]` | Vol II `concordance.tex` L139, `foundations.tex` L688 — **explicitly scoped to GENERIC level, critical $k=-h^\vee$ EXCLUDED because $\dim\ChirHoch^0$ can be infinite**. | **AP-CY83 / AP5 caveat drift** (see §3.1 below). |
| `class_m_global_triangle` Thm 4.1 (HPL transfer) | `[Target]` | No parent counterpart (this is a target, not a chapter result). | OK as target. |
| `monster_voa_orbifold_e3` Thm 2.1 ($\Zder(V_\Lambda^+)$ is $E_3$-top) | `[Theorem]`, **proved** | No parent ProvedHere counterpart found in `chapters/connections/holomorphic_topological.tex`. The "abelian Sugawara" mechanism is invoked inline ("Lurie HA 5.1") with no chapter-side theorem to cite. | **NEW STANDALONE CLAIM with no chapter cross-ref.** AP60 / AP4 risk: claimed proved here, no chapter-side ProvedHere anchor. |
| `bcfg` Prop 1.1 (Yangian-level $B_2$ folding) | `[Proved]` | Molev's classical Yangian folding; chapter side has no parent theorem. | Classical material — should be `\begin{remark}[after Molev]` rather than `\begin{proposition}[Proved]` (AP60). |
| `stokes_gap` Thm 1.1 (Target) | `[Target]` | Vol II `modular_swiss_cheese_operad.tex` lists composition-associativity as open at generic non-integral $k$. | OK (consistent: target is the open piece). |
| `rpt_convergence` Thm 1.1 (Eberhardt Route D) | `[Conditional]` | No chapter counterpart. | OK as conditional. |
| `curved_dunn` Prop 3.1 (genus-1 twisted Künneth) | `[Proved]` | Vol II `twisted_holography_quantum_gravity.tex` has analogous statements but they are scoped to $\mathrm{Mon}(R)=\id$ in some places. | **Possible scope drift** — see §3.4. |

### 2.2 AP60 violations (ProvedHere-equivalent on classical material)

| Location | Material | Why it is classical | Suggested rewrite |
|----------|----------|---------------------|-------------------|
| `bar_chain_models` Section 1 (entire) | Yang $R$-matrix RTT presentation, Drinfeld coproduct, hexagon, etc. | Standard Drinfeld 1985, Faddeev-Reshetikhin-Takhtajan 1989. | Open Section 1 with: "We recall the classical Yangian presentation (Drinfeld 1985, FRT 1989)." |
| `bar_chain_models` Prop 3.2 (CYBE for $r(z) = k\Omega/z$) | Classical Belavin-Drinfeld 1982. | This is the rational classical $r$-matrix; CYBE is a Casimir computation. | "(Classical $r$-matrix; cf. Belavin-Drinfeld 1982)." Already implicit but no attribution. |
| `bcfg` Prop 1.1 | Molev's Yangian folding $Y(\fsl_4)^\sigma = Y(\fso_5)$. | Standard Yangian construction, Molev 2007. | Replace `\begin{proposition}[Proved]` with `\begin{remark}[after Molev]`. |
| `stokes_gap` Prop 2.2 (KZ regularity at integrable level) | Kazhdan-Lusztig, TUY. | Cited inline (good). | OK as currently stated; just confirm `[Proved]` tag attributes correctly. |
| `monster_voa_orbifold_e3` Thm 2.1 | Lurie HA 5.1 $E_n$-invariants. | Mostly invoking Lurie. | Cite specific theorem, not "HA 5.1" (Section 5 of Lurie HA is huge — see AP-CY citation precision risk in §7.1). |

---

## Section 3 — Caveat drift (Vol I AP-CY83 analog)

This is the highest-yield section. The pattern: chapters carry careful caveats; standalones drop them when the standalone is presenting "the headline".

### 3.1 ChirHoch concentration — critical level dropped (CRITICAL)

**File**: `class_m_global_triangle.tex`, lines 83--96.

**Standalone claim**:
```
\begin{proposition}[DS--Hochschild at all degrees]
\ChirHoch^0(V_k(\fsl_2)) = C  --> C  = ChirHoch^0(Vir_c)
\ChirHoch^1(V_k(\fsl_2)) = sl_2 --> 0  = ChirHoch^1(Vir_c)
\ChirHoch^2(V_k(\fsl_2)) = C  --> C  = ChirHoch^2(Vir_c)
\ChirHoch^{>=3} = 0 --> 0
```

**Parent-chapter scope** (multiple sites): `concordance.tex` L139, L707, L711; `foundations.tex` L688--691; `ym_synthesis.tex` L229, L313; `ym_boundary_theory.tex` L286, L366; `anomaly_completed_topological_holography.tex` L1694; `twisted_holography_quantum_gravity.tex` L2746; `ordered_associative_chiral_kd_frontier.tex` L5847.

Every one of these chapter sites carries the caveat:

> "at generic level; the critical level $k = -h^\vee$ is excluded because $\dim \ChirHoch^0$ can be infinite there, see Vol~I Remark~\ref*{rem:critical-level-lie-vs-chirhoch}"

**The standalone Proposition 3.1 has NO such caveat.** Stated unconditionally, it is FALSE at $k=-h^\vee = -2$ for $\widehat{\fsl}_2$ where Feigin-Frenkel gives $\ChirHoch^0 = \mathfrak{Z}(\widehat{\fsl}_2) = \mathbb{C}[J^a_{-1}, J^a_{-2}, \ldots]^{\widehat{\fsl}_2}$ infinite-dimensional.

**Heal**: insert "for $k \neq -2$" into the Proposition statement and a remark referencing `concordance.tex` L711 ("for $\widehat{\fsl}_2$ at critical level, $\ChirHoch^*$ is..."). Strongest correct form: the proposition holds at generic level $k \notin \{-2\} \cup \mathbb{Q}_{<0}$ where the Verma module is irreducible and the BRST cohomology truncation argument applies.

This is the same Vol-I-pattern caveat drift documented in earlier waves (BP self-dual, $L^{sh}$ poles, ChirHoch occupation).

### 3.2 The $V^\natural$ / abelian Sugawara claim — Heisenberg scope

**File**: `bar_chain_models...tex` lines 419--427 (Remark following `Theorem~\ref{thm:topologise}`):

> "$\mathcal{H}_k$ ($k \ne 0$) and lattice VOAs are not stuck at $\mathrm{SC}^{\mathrm{ch,top}}$: $\mathcal{H}_k$ carries the abelian Sugawara conformal vector $T = \frac{1}{2k}{:}JJ{:}$ ($c = 1$) and abelian holomorphic Chern--Simons theory provides the 3d HT bulk."

This is **stated unconditionally**. Two sub-issues:

(a) The case $k = 0$ is excluded by `$k \neq 0$` — fine; $1/(2k)$ requires $k \neq 0$. **OK as stated.**

(b) The lattice VOA generalisation is asserted but the conformal vector is not given (general lattice $\Lambda$ requires a choice of dual basis). For $V_\Lambda$ with even unimodular $\Lambda$ of rank $n$, the abelian Sugawara $T = \frac{1}{2}\sum :J^i J_i:$ at $c = n$. For $n = 24$ (Leech), $c = 24$.

**`monster_voa_orbifold_e3.tex` Theorem 2.1** then leverages this: `\Zder(V_\Lambda^+)$ carries an $E_3$-topological algebra structure" — proof = "$V_\Lambda$ is $E_3$-topological (abelian holomorphic CS for $U(1)^{24}$ with Leech lattice charge lattice)". But the abelian holomorphic CS construction giving $E_3$-topological for $V_\Lambda$ specifically (rather than the general "abelian Sugawara works") is NOT in the chapter. The standalone is asserting a fresh result with no parent ProvedHere anchor.

**Heal options** (in priority order):

1. **Strongest upgrade**: extract the abelian-Sugawara $E_3$-topological theorem into a chapter-side proposition (so it has a ProvedHere anchor). Then standalone Theorem 2.1 cites it. Currently the chapter side has only "Costello-Li for non-abelian KM" (cited as proved) — the abelian case is implicit as a corollary but not isolated.

2. **Status downgrade**: replace `\begin{theorem}` with `\begin{proposition}[after Costello-Li, abelian case]` to make clear it's a specialisation of a known theorem.

3. **Independent proof**: write out the explicit abelian hCS construction in the standalone (the Sugawara identity $T = \frac{1}{2}:JJ:$, BRST $Q$, antighost $G$, identity $T = [Q, G]$). The standalone Step 5 "BRST identity in the orbifold bulk" alludes to this but does not provide it for the un-orbifolded case.

### 3.3 Bar-chain-models Proposition "curvature" (3.4) — kappa scoping

**File**: `bar_chain_models...tex` lines 243--251:

> "At genus $g \ge 1$, the bar complex has $d_B^2 = \kappa_{\mathrm{ch}} \cdot \omega_g$, where $\kappa_{\mathrm{ch}}$ is the shadow obstruction class and $\omega_g$ is the Arakelov $(1,1)$-form on the genus-$g$ surface, normalised so that $\int_{\Sigma_g} \omega_g = 1$."

The standalone uses $\kappa_{\mathrm{ch}}$ (subscripted — good, complies with AP113). But the proposition statement does NOT say which obstruction-tower convention is in force. The kappa-spectrum (manifold vs algebraization invariants from Vol III AP-CY55) is irrelevant here (Vol II is purely algebraization-side), but the formula has a **uniform-weight scope** (Vol I AP32): for multi-weight algebras (W-algebras with distinct primary weights), the scalar formula $d_B^2 = \kappa \cdot \omega_g$ FAILS — there is a per-weight cross-channel correction. Vol I CLAUDE.md AP32: *"Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS."*

The standalone Prop 3.4 is stated for an arbitrary $E_1$-chiral algebra without a uniform-weight tag. **AP32 violation**.

**Heal**: Add `(UNIFORM-WEIGHT)` tag, or restrict to algebras with a single primary weight (Heisenberg, KM, Vir). For $\mathcal{W}_N$ with $N \ge 3$, the cross-channel correction is the operative content of Vol I §"shadow free energies — multi-weight cross-channel".

### 3.4 Curved Dunn — $\mathrm{Mon}(R) = \id$ scope

**File**: `curved_dunn_two_complex_bridge.tex` Prop 3.1 (line 52):

> "$\Bmod(\mathcal{O}^{\Ainf\text{-ch}})\big|_{g=1} \simeq \Bmod(\mathrm{SC}^{\mathrm{ch,top}})\big|_{g=1} \otimes^{\mathrm{Mon}(R)} \mathbf{B}(E_1^{\mathrm{tr}})$"

The Eilenberg-Zilber twisted tensor product $\otimes^{\mathrm{Mon}(R)}$ requires $\mathrm{Mon}(R)$ to be unipotent (or quasi-isomorphism control on the twist). Section 1.2 of the same standalone says: "Vanishes when $\mathrm{Mon}(R) = \mathrm{id}$." The Prop 3.1 statement does NOT propagate the obstruction-vanishing scope.

**Heal**: state Prop 3.1 with the explicit condition: "for $E_1$-chiral algebras with unipotent $\mathrm{Mon}(R)$" or "with formal $\hbar$-deformation of $\mathrm{Mon}(R)$ around id". For class M (Virasoro), $\mathrm{Mon}(R)$ is non-trivially semisimple and the simple twisted-tensor-product formulation needs the twisted Künneth machinery which is itself the conjectural Phase 2.

---

## Section 4 — Inflated counts

The Vol I wave 6 finding ("7 faces", "14 chars") has direct Vol II analogs in `preface_full_survey.tex`:

| Count | Location | Verifiable? |
|-------|----------|-------------|
| "the five theorems" | line 52, 85 | The five Vol I "main theorems" are real (A--E in `~/chiral-bar-cobar/CLAUDE.md`); but at line 85 the standalone introduces THREE additional "structure theorems" (Algebraicity, Formality identification, Complementarity) on top of "five main theorems". Five vs five+three is bookkeeping confusion. **Total Vol I theorem inventory = ?** — not "five" if "structure theorems" are counted. |
| "Six direct faces" | line 655 | Six rows in the table at lines 663--684. Counting checks out (6 rows). But row 5 (closed genus expansion: `$\Theta_\cA$ Polyakov programme`) and row 6 (closed cohomology: PVA) are NOT projections of the SAME 3d MC element $\alpha_T$ in a uniform sense — row 5 is genus-tower deformation, row 6 is shape-cohomology. The six "faces" are heterogeneous in indexing degree. |
| "twelve faces" / "Koszul dodecahedron" | line 860--900 | Twelve enumerated items. Item (xi) Lagrangian transversality: explicitly conditional on perfectness (parenthetical). Item (xii) Hodge purity: "forward implication proved; converse open". So 10 of 12 are unconditional, 1 conditional, 1 partial. Headline "twelve faces follow from one condition" overstates. **AP155 / Vol-I-wave-6 inflated count.** |
| "the fourteen theorems" (§XIV) | line 1547 | Fourteen entries (A')--(N'). Inspection: (E') and (I') flagged "internal scope: derived-center identification proved in boundary-linear exact sector; line-module identification on chirally Koszul locus" (lines 1685--1689). (G') flagged "applies the framework via the bridge theorem". (M') and (N') "contain conditional or conjectural components". So **out of 14: 9 unconditional, 5 partial/conditional/conjectural**. The headline "fourteen theorems" with disclaimer at the bottom is exactly the wave-6 Vol I pattern. |

**Heal pattern**: each inflated-count headline should be replaced by `"N principal results, of which $a$ are unconditional and $b$ are conditional/scoped"`. The disclaimer at line 1684 already exists; promoting it into the headline removes the inflation.

---

## Section 5 — AP151 (q convention) and AP126 (r-matrix level)

### 5.1 AP151 self-violation in `bcfg_chiral_coproduct_folding.tex`

This is the cleanest self-contained AP151 instance found in the audit.

| Line | Content |
|------|---------|
| 51 (Prop 1.1) | "$R^{B_2}(u) = 1 - \hbar P/u + \hbar Q/(u - 2)$" (Yangian convention; spectral parameter $u$, deformation parameter $\hbar$) |
| 123 (target Thm 3.1) | "$R^{B_2}(z) = 1 - k\,P/z + k\,Q/(z - 2k)$" (level convention; $z$, $k$) |

Both presented as the SAME object (the $B_2$ R-matrix). One file, two conventions. The conversion $\hbar \leftrightarrow k$ is implicit — neither line states which is in force.

**Heal**: pick one convention. Most common in Vol II is $k$ (level); or state explicitly "for the Yangian: substitute $k \mapsto \hbar$". Cleanest: state the dictionary up front.

### 5.2 AP126 / AP141 r-matrix level audit

`bar_chain_models...tex` line 224:
> "$r(z) = \frac{k\,\Omega}{z}$"

**Correct**: level $k$ explicit, $k = 0 \Rightarrow r = 0$. Passes AP126/AP141 check.

`bar_chain_models...tex` line 60:
> "$R(z) = 1 - \frac{\hbar P}{z}$" (Yangian)

**OK** for Yangian (no level — Yangian is $\hbar$-deformation of $U(\fg[t])$, no Kac-Moody level structure).

`bar_chain_models...tex` line 623:
> "For class~L (Kac--Moody, $R(z) = 1 + \hbar P/z$), the integral evaluates to zero: $m_3 = 0$"

**AP126 SUSPECT**: this is the Kac-Moody $R$-matrix written with $\hbar$ but no level $k$. The classical $r$-matrix for $V_k(\fg)$ should be $r(z) = k\Omega/z$ (Prop 3.2 in same file). The transition $\hbar \leftrightarrow k$ is implicit. At $k = 0$ (critical level for $\fsl_2$? — no, critical is $-h^\vee$; at $k=0$ for KM the algebra is degenerate $V_0(\fg)$), $R(z) = 1 + 0 \neq 1$ which is fine for Yangian-style but inconsistent with the level-$k$ prescription of Prop 3.2.

**Heal**: write line 623 as "$R(z) = 1 + k P/z$" to match Prop 3.2's level-$k$ convention; or state explicitly "with $\hbar$ playing the role of $k$".

### 5.3 No bare $\Omega/z$ found in Vol II standalones

Grep for `Omega/z` without level: no instances in standalones. AP126 risk concentrated in cross-convention drift between $\hbar$ and $k$ rather than missing level prefix.

---

## Section 6 — Novelty audit (AP155)

### 6.1 `bar_chain_models...tex` Sections 1, 6, 7 — what is new

Section 1 ("The Yangian as $E_1$-chiral quantum group"): the Yangian RTT construction is **classical Drinfeld 1985, FRT 1989**. The novelty claim is the FRAMING: viewing the RTT presentation as an instance of "$E_1$-chiral quantum group" (Definition 2.1). The Yangian itself is not new.

Section 7 (Prop 7.1, "Cohomological coproduct from MO $R$-matrix"): the explicit form (iii) of the coproduct on $\psi$, $e$, $f$ generators (lines 696--718) is the **Schiffmann-Vasserot spectral coproduct**. The standalone says so explicitly (lines 720, 762: "These match the Schiffmann-Vasserot spectral coproduct"). Novelty = new derivation path (via $\gamma^{-1} = \beta \circ \alpha$) of a known coproduct.

**AP155 status**: explicitly handled — the standalone names SV. Good practice. **No AP155 violation here.**

### 6.2 `bcfg` — folding novelty

The Yangian-level folding $Y(\fsl_4)^\sigma = Y(\fso_5)$ is **Molev** (2007). The standalone's Phase 1 is therefore Molev recapitulation. Novelty is the chiral-level extension (Phases 2--4), which is conjectural.

**AP155 risk**: Phase 1 presented as `[Proposition][Proved]` with self-contained 3-line proof, no Molev citation. The proof IS Molev's argument. **Heal**: add "(Molev 2007)" attribution.

### 6.3 `monster_voa_orbifold_e3` — orbifold construction

The orbifold construction $V^\natural = V_\Lambda^+ \oplus V_\Lambda^{\mathrm{tw},+}$ is **Frenkel-Lepowsky-Meurman 1988**. The phase 5 mention of van Ekeren-Möller-Scheithauer covers extension to Schellekens 71 list. The novelty claim: lifting these orbifold constructions through the $E_3$-topological route via orbifold BV.

**AP155 status**: classical inputs (FLM, Schellekens, vEMS) cited. Novelty (the BV master equation for orbifold abelian CS) is genuine conjecture. **No AP155 violation.**

### 6.4 `stokes_gap` — KZB analytics

Kazhdan-Lusztig regularity at integrable level (Prop 2.2) attributed correctly inline. The conjectured generic-$k$ extension is the genuine new content. **No AP155 violation.**

### 6.5 `rpt_convergence` — PT identification

The Ponsot-Teschner fusion kernel is from PT (2001). Eberhardt's difference-Galois uniqueness theorem is invoked (Thm 1.1) — should be cited (paper not in standalone bibliography; standalone has no bibliography). **AP155-adjacent: Eberhardt is the load-bearing classical input and is uncited.**

### 6.6 `class_m_global_triangle` — DS-Hochschild

The DS reduction's effect on Hochschild cohomology is implicit in **de Sole-Kac** and the BRST formulation in **Feigin-Frenkel**. The standalone Prop 3.1 (degree-by-degree) is a recapitulation/specialisation. **AP155 mild**: no attribution given; would benefit from "(after Feigin-Frenkel; cf. de Sole-Kac)".

### 6.7 `curved_dunn` — Dunn additivity

Dunn additivity (genus 0) = **Dunn 1988, Lurie HA 5.1.2.2**. Curved version is genuinely conjectural (Conj 2.2 / 4.1).

---

## Section 7 — V2-AP self-violations

V2-AP catalogue is in `~/chiral-bar-cobar-vol2/CLAUDE.md` lines V2-AP1--V2-AP39.

| AP | Site | Violation |
|----|------|-----------|
| **V2-AP6** ("BD do NOT study $E_1$") | Not violated (Section 4 of `bar_chain_models` is well-scoped). | OK |
| **V2-AP7** ("Heisenberg $R$-matrix = $\exp(k\hbar/z)$") | `preface_full_survey` line 746: "$R(z) = e^{k\hbar/z}$" | OK — matches V2-AP7. |
| **V2-AP21** (PVA $\neq P_\infty$-chiral) | Not violated. | OK |
| **V2-AP22** (full hierarchy) | `preface_full_survey` line 87 says "$E_1 \supsetneq E_\infty$" using the Vol II Recast convention; line 116 of `bar_chain_models` repeats it. **Possible V2-AP22 friction**: V2-AP22 hierarchy is `Comm assoc < PVA < E_inf-chiral < P_inf-chiral < E_1-chiral`, so $E_1$-chiral is the LARGEST class. The standalones use $E_1 \supsetneq E_\infty$ — symbol direction OK. | OK |
| **V2-AP25** ($\bar\partial$ Im sign) | Not encountered (no $\bar\partial$ Im computations in standalones). | N/A |
| **V2-AP26** (no hardcoded Part numbers) | Compliant: standalones use `\ref{...}` not "Part~II". | OK |
| **V2-AP27** (no duplicated theorems) | `preface_full_survey` Section XIV (lines 1547--1681) reproduces statements of theorems with `\ref{...}` to chapters but does NOT duplicate the proofs. | OK |
| **V2-AP28** (test expected values from 2+ independent sources) | `rpt_convergence` table at lines 87--96 ($\lambda_{\min}$ data N=1..8). The data are presented but NO independent verification is shown. The data come from a single computation; if `Vol1` engine has a bug, the table inherits it. | **V2-AP28 risk**: numerical evidence presented without an independent computation path. |
| **V2-AP29** (AI slop scan) | `preface_full_survey` searched: no "moreover", "additionally", "notably", "remarkably", "it is worth noting" violations. | OK |
| **V2-AP31** (proof block follows theorem) | `monster_voa_orbifold_e3` Theorem 2.1: proof block follows. `bar_chain_models` Thm 5.1: proof block follows. `class_m_global_triangle` Thm 4.1: NO proof block (only "Step 1...Step 4" outline). **V2-AP31 risk** for `class_m_global_triangle` — `[Target]` bracket tag justifies absence, but presenting it as `\begin{theorem}` and not `\begin{conjecture}[Target]` invites confusion. | **`class_m_global_triangle` Thm 4.1**: change `\begin{theorem}` to `\begin{conjecture}[Target theorem, precise form]` to comply with V2-AP31. |
| **V2-AP32** (no `\title`/`\maketitle` in chapter files) | Not applicable to standalones (which SHOULD have `\title`/`\maketitle`). | N/A |
| **V2-AP34** (divided-power Vol II convention $c/12$ not $c/2$) | Not encountered (no $\lambda$-bracket OPE expansions in standalones). | N/A |

---

## Section 8 — First-principles probes

### 8.1 The "Yangian as $E_1$-chiral QG" claim

**Wrong claim (overstated)**: "The Yangian $Y_\hbar(\fsl_2)$ is an $E_1$-chiral quantum group on a curve $X$" — Section 1 of `bar_chain_models...tex`.

**Ghost theorem**: The Yangian carries (i) RTT multiplication, (ii) Drinfeld coproduct, (iii) $R$-matrix, (iv) antipode — all the ingredients of Definition 2.1 of an $E_1$-chiral QG. So as a FORMAL ALGEBRAIC object, $Y_\hbar$ "is" an $E_1$-chiral QG.

**What's missing**: the chiral algebra structure on a curve $X$. Definition 2.1 demands "$\cA$ is an $E_1$-algebra in factorisation algebras on $X$". The Yangian as classically defined is not on a curve; it lives in the formal-variable presentation. To make it a chiral algebra ON a curve requires identifying a curve $X$, a $\mathcal{D}$-module structure, and OPE on $X$ — none of which are constructed in the standalone.

**Correct relationship**: the Yangian is a candidate for an $E_1$-chiral quantum group; the obstruction to making it one is the construction of a chiral algebra structure on $X$. This is acknowledged in Question 5.6.2 ("Construct an $E_1$-chiral quantum group $\cA$ that is not $E_\infty$... the Yangian $Y_\hbar(\fsl_2)$ is the candidate; the missing ingredient is a rigorous construction of the chiral algebra structure on a curve $X$").

**Confusion type**: object/structure (V2-AP self-mapped). The Yangian-as-formal-algebra IS an $E_1$ Hopf-with-$R$-matrix; the Yangian-as-chiral-algebra-on-$X$ is open.

**Heal in standalone**: the headline "Section 1: The Yangian as $E_1$-chiral quantum group" should become "The Yangian as candidate $E_1$-chiral quantum group: the formal-variable picture". The body is honest about this when it gets to Question 5.6.2; the section opener is not.

### 8.2 The "twelve faces follow from one condition" claim

**Wrong claim**: "Twelve consequences follow from [Koszul concentration], each expressing a different face of the same concentration." (line 857)

**Ghost theorem**: Items (i)--(x) are genuine equivalent characterisations of Koszulness in the chiral setting, lifting Priddy-BGG-BGS for classical Koszulness.

**What's wrong**: items (xi) Lagrangian transversality and (xii) Hodge purity are NOT direct consequences. (xi) requires perfectness and chain-level nondegeneracy (parenthetical conditions). (xii) is one-directional (forward implication proved; converse open). They are CONNECTED to Koszulness but not "consequences of" the single condition.

**Correct relationship**: Koszul concentration of bar cohomology in degree 0 gives the ten direct equivalences (i)--(x). Items (xi), (xii) are RELATED structural results that are partial: (xi) is Koszul-implies-Lagrangian-splitting (under perfectness); (xii) is Koszul-implies-Hodge-purity (one direction).

**Heal**: rewrite "twelve faces" as "ten equivalent characterisations and two related partial results".

### 8.3 The `class_m_global_triangle` ChirHoch table

**Wrong claim** (silently): the table at lines 86--96 is presented without the critical-level caveat.

**Ghost theorem**: At GENERIC level the DS-induced map IS the indicated isomorphism on each ChirHoch degree. The proof uses the Wakimoto-style BRST resolution which works exactly when the Verma module is irreducible and Sugawara is non-degenerate — i.e., generic level.

**What's wrong**: at $k = -h^\vee$ the Sugawara denominator $1/(k+h^\vee)$ blows up, the centre of the Kac-Moody algebra at critical level becomes the Feigin-Frenkel commutative algebra of infinite rank, and $\ChirHoch^0$ is no longer $\mathbb{C}$ — it is the polynomial algebra on Sugawara modes.

**Correct relationship**: the table is the GENERIC-LEVEL DS-Hochschild reduction; at critical level the structure is genuinely different and $\ChirHoch^*$ is no longer concentrated.

**Heal**: in the proposition statement, replace `V_k(\fsl_2)` with `V_k(\fsl_2)$ at generic $k \neq -2$"; reproduce the chapter caveat verbatim.

### 8.4 The `bar_chain_models` Section 4 "What the bar complex sees and does not see"

**Wrong claim** (subtle): "It does not see: (i) the chiral coproduct $\Delta\colon \cA \to \cA \otimes \cA$ ... (ii) the full quantum $R$-matrix ... only its classical limit appears in the shadow tower."

**Ghost theorem**: The bar complex computes $k \otimes_\cA^L k$, the factorisation homology of the interval with augmentation boundary. This sees the multiplication and its $A_\infty$ tower; it does NOT see additional algebraic structure (coproduct, antipode, etc).

**What's right**: the bar complex is a FUNCTOR on the algebra structure of $\cA$; coproduct/antipode are independent extra data.

**What's almost-wrong but not quite**: "only its classical limit $r(z)$ appears in the shadow tower" — this glosses over the wheel-diagram / loop corrections. The $A_\infty$ deformation $m_3, m_4, ...$ on the shadow ENCODES quantum corrections to the classical $r$. So the bar complex DOES see SOME quantum information, just not the full $R$-matrix.

**Heal**: "the bar complex sees the classical $r$-matrix and its all-loop $A_\infty$ deformation; the full quantum $R$-matrix as an exponential of the spectral wheel-tower is reconstructed from this data on the chirally Koszul locus, but is independent input off it."

---

## Section 9 — Three upgrade paths

### Path A: caveat reinstatement (lowest cost, highest value)

For each `class_m_global_triangle`, `bar_chain_models` Prop 3.4 (kappa scoping), `curved_dunn` Prop 3.1 (Mon(R) scoping): copy the parent-chapter caveat verbatim into the standalone. No new mathematics; a 3-line edit per location. Resolves caveat drift and AP32 / V2-AP-3.4 violations.

### Path B: status downgrade where no chapter anchor exists

For `monster_voa_orbifold_e3` Theorem 2.1: either add a chapter-side ProvedHere anchor for "abelian Sugawara $\Rightarrow$ $E_3$-topological" (preferred), or downgrade to `\begin{proposition}[after Costello-Li, abelian case]`. For `class_m_global_triangle` Theorem 4.1: change `\begin{theorem}` to `\begin{conjecture}[Target]` to comply with V2-AP31.

### Path C: novelty re-attribution

For `bar_chain_models` Section 1: insert opening sentence "We recall the classical Yangian RTT presentation (Drinfeld 1985, FRT 1989)" so that the section is honest about what is recapitulation. For `bcfg` Prop 1.1: change `\begin{proposition}[Proved]` to `\begin{remark}[after Molev 2007]`. For `class_m_global_triangle` Prop 3.1: cite Feigin-Frenkel and de Sole-Kac in the proof.

The strongest mathematical assertion the standalone collection can support, after these heals:

1. **The Yangian is a candidate $E_1$-chiral QG; the construction of its chiral-algebra structure on a curve is the principal open problem of the volume.** (Replaces the headline assertion that Yangian "is" such an object.)

2. **At generic non-critical level, DS reduction induces the explicit ChirHoch map of `class_m_global_triangle` Prop 3.1.** (Adds critical-level scope.)

3. **Koszul concentration of bar cohomology in degree 0 has ten direct equivalent characterisations and two related partial results.** (Replaces "twelve faces follow".)

4. **Of the fourteen results in the §XIV catalogue, nine are unconditional and five carry explicit scope.** (Replaces "fourteen theorems" headline.)

5. **The orbifold $E_3$-topological route for $V^\natural$ proceeds in five steps, of which the BV master equation and anomaly cancellation are anomaly-checked unconditionally and the boundary identification reduces to known orbifold bulk-boundary results.** (Replaces uncited Lurie HA 5.1.)

---

## Section 10 — Punch list (priority-ordered)

**P0 (factually misleading without fix)**

1. `class_m_global_triangle.tex` Prop 3.1 (lines 83--96): add "at generic level $k \neq -h^\vee$" qualifier; add critical-level remark referencing `concordance.tex` L711. **AP-CY83 / V2-AP4 caveat drift, mathematical FALSE statement at $k=-2$.**

2. `bar_chain_models...tex` Prop 3.4 (lines 243--251): add `(UNIFORM-WEIGHT)` tag to the kappa formula, or restrict to single-primary-weight algebras. **AP32 violation.**

3. `bcfg_chiral_coproduct_folding.tex` lines 51 vs 123: pick one of $\hbar$ / $k$ convention and propagate. **AP151 self-violation in single file.**

**P1 (status-tagging hygiene)**

4. `class_m_global_triangle.tex` Thm 4.1: change `\begin{theorem}` to `\begin{conjecture}[Target theorem, precise form]`. **V2-AP31.**

5. `monster_voa_orbifold_e3.tex` Thm 2.1: either add chapter-side anchor for abelian-Sugawara $\Rightarrow$ $E_3$-top, or downgrade to `\begin{proposition}[after Costello-Li, abelian case]`. **AP60.**

6. `bcfg_chiral_coproduct_folding.tex` Prop 1.1: change `\begin{proposition}[Proved]` to `\begin{remark}[after Molev 2007]`. **AP60.**

**P2 (caveat tightening)**

7. `bar_chain_models...tex` line 623 (R-matrix for KM): rewrite "$R(z) = 1 + \hbar P/z$" as "$R(z) = 1 + k P/z$" to match Prop 3.2 convention. **AP126/AP141 partial.**

8. `curved_dunn_two_complex_bridge.tex` Prop 3.1: state explicit scope "for $E_1$-chiral algebras with unipotent $\mathrm{Mon}(R)$" (or equivalent). **§3.4 caveat drift.**

9. `monster_voa_orbifold_e3.tex` line 66: replace "Lurie, HA~5.1" with specific theorem ref (e.g. HA 5.1.2.2 if that is what's meant). **Citation precision.**

**P3 (count adjustments)**

10. `preface_full_survey.tex` line 860: rewrite "twelve faces" as "ten equivalent characterisations and two related partial results". **§4 inflated count.**

11. `preface_full_survey.tex` §XIV header: add count breakdown ("nine unconditional, five with internal scope") to the heading rather than a footnote at the end. **§4 inflated count.**

**P4 (citations)**

12. `rpt_convergence_shapovalov.tex`: add bibliography entry for Eberhardt's difference-Galois theorem (the load-bearing reduction step Thm 1.1). **§6.5.**

13. `bar_chain_models...tex` Section 1: open with "We recall the classical Yangian RTT presentation (Drinfeld 1985, FRT 1989)." **§6.1 / AP155.**

**P5 (preface bibliography)**

14. `preface_full_survey.tex` has no bibliography and uses chapter-internal `\ref` keys. As a standalone PDF it WON'T compile. Either: (a) document that it is not intended to be compiled standalone (rename to `frame/preface_survey_input.tex`), or (b) add a bibliography and resolve all `\ref` to either `\href` or local labels. **Structural / build hygiene.**

---

## Cross-volume notes

- **Nish26**: `\bibitem{Nish26}` exists in `main.tex` L2044 ("in preparation, 2026"). One in-text `\cite{Nish26}` at `chapters/connections/thqg_gravitational_complexity.tex` L1724. Vol I wave 7 finding: 33 sites in Vol I — Vol II has just 1 site, much smaller surface. **Lower-priority follow-up than Vol I.**

- **GL76, Bor98-Grassmannian, GN97**: NOT cited in Vol II standalones (grep returned 0 hits). Vol I bibliography gap does not propagate to Vol II.

- **KZ25 / Khan-Zeng**: cited in `bar_chain_models...tex` and `monster_voa_orbifold_e3.tex` and `preface_full_survey.tex`. Bibitem present in `main.tex` (with duplicate KZ2025 alias). Healthy.

- **GRZ, JKL**: 2023, 2026 papers cited in `bar_chain_models...tex` bibliography (entries 4, 5). Forward-dated 2026 entry (JKL = arXiv:2603.21707) is consistent with the user's normal workflow.

---

## Summary

The Vol II standalones are honest at the medium-resolution level (status tags, scope bracketing) but show the same MICRO-CAVEAT-DRIFT pattern Vol I exhibited:

- **One factually wrong-without-caveat statement**: `class_m_global_triangle` Prop 3.1 (ChirHoch concentration without critical-level exclusion). This is the highest-leverage fix.
- **One self-violation of AP151 within a single file**: `bcfg` $\hbar$ vs $k$ convention. Trivial to heal.
- **Two count-inflation patterns matching Vol I wave 6**: "twelve faces" and "fourteen theorems" in `preface_full_survey`. Already self-disclosed at the bottom; promoting the disclaimer to the headline removes the inflation.
- **One uncited classical input**: Eberhardt difference-Galois in `rpt_convergence`.
- **One structural anomaly**: `preface_full_survey.tex` does not compile as a standalone PDF (no bibliography, chapter-internal `\ref`).

No deep mathematical errors found — the standalones are at present internally consistent with their parent chapters at the level of theorem statements; the friction is at the level of caveat propagation, status tagging, and (a single) convention clash. Three of the seven non-preface standalones (`bar_chain_models`, `bcfg`, `monster_voa_orbifold_e3`) make CONTENTFUL extensions beyond the chapters; the other four (`stokes_gap`, `class_m_global_triangle`, `rpt_convergence`, `curved_dunn`) are storyboard documents whose theorem environments would benefit from more uniform `[Target]` / `[Conjecture]` / `[Conditional]` tagging.

**Recommended next wave**: focus on the `bar_chain_models...tex` standalone in isolation — it is the most substantive (875 lines, 12 environments, real bibliography) and its Section 4 "what the bar complex sees and does not see" is the load-bearing claim that ought to be a stand-alone theorem in Vol II's `theory/` chapters with a ProvedHere anchor.
