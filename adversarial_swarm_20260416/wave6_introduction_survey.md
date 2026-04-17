# Wave 6 — Adversarial audit of Vol I narrative / overview material

**Audit date:** 2026-04-16
**Auditor scope (read-only):** introduction_full_survey.tex, programme_summary[*].tex,
survey_modular_koszul_duality[_v2].tex, survey_track_[ab]_compressed.tex, editorial.tex,
preface.tex, preface_section1_v2.tex, guide_to_main_results.tex, plus chapter cross-checks
(chiral_koszul_pairs.tex, holographic_codes_koszul.tex, editorial_constitution.tex).
**Methodology:** sceptical referee. The user's brief: HEAL by realising the strongest
defensible claims; do not downgrade where an upgrade path exists.

---

## Executive summary

The narrative material exhibits a recognisable failure mode: the high-level
documents (intro, programme summary, surveys) accumulate a *self-flattering
reading* of the underlying chapters. The chapters say "twelve" — the
standalone titles itself "fourteen". The chapters give a six-component
differential — the intro and programme summary give five, with two
*different* enumerations of the five (i.e. the inflated-then-deflated count
isn't even consistent with itself between two pages of the same intro). The
abstract advertises "single open conjecture" while the same document has a
section titled "The single open problem" containing a `\begin{theorem}`
whose proof depends on Vol III material that is itself only proved at the
∞-categorical level.

Eight overclaim/inflation classes are catalogued below (§1–§3). Two
upgrade paths and one near-Annals statement are identified for promotion
(§4, §6). A 27-item punch list closes the report (§7). Two new
cross-volume cache entries are proposed for AP-CY61 (§5).

The pattern repeats prior wave findings (seven faces, fourteen
characterisations, triple redundancy, universal N-formula, BBL triangle,
status overclaim, within-volume contradiction). Five new instances are
documented here.

---

## Section 1 — Status overclaim audit

### 1.1 Master overclaim table

| # | Document | Line | Claim | Source ground truth | Diagnosis |
|---|---|---|---|---|---|
| O1 | programme_summary.tex | 98 (abstract) | "single open conjecture is the CY-A correspondence at d = 3" | §"single open problem" L2589 immediately writes `\begin{theorem}[CY-A at d=3]` with no ClaimStatus tag; in CLAUDE.md (Vol III) CY-A_3 is **PROVED at ∞-cat level only**; chain-level remains conditional for non-formal algebras. | Self-contradictory abstract. CY-A_3 is neither "single open conjecture" nor a `\begin{theorem}`. Upgrade path: `\begin{theorem}[…; \ClaimStatusProvedElsewhere]` citing Vol III thm:derived-framing-obstruction, plus a remark stating chain-level conditionality. |
| O2 | programme_summary.tex | 2599–2607 | `\begin{theorem}[CY-A at d=3]` + `\label{thm:cy-a3}` with no proof block, no ClaimStatus, no Vol III citation. | Same. AP40 violation: theorem environment without proof and without status tag. | Add `\ClaimStatusProvedElsewhere` and Vol III citation. |
| O3 | programme_summary.tex | 2619–2635 | "No open conjecture in the programme has unresolved algebraic prerequisites." | CLAUDE.md: CY-C is `\begin{conjecture}` (Vol III), nonabelian K3 Yangian open, ZTE genuine E_3 lift open, Sp_4(Z) modularity pipeline programme, root-of-unity CY QG conjectural. AP15. | Replace by "No open Vol I conjecture has unresolved algebraic prerequisites; the Vol III/CY-C frontier remains conjectural." |
| O4 | introduction_full_survey.tex | 499–534 | `\begin{theorem}[E_1 primacy; \ClaimStatusProvedHere]` with `\begin{proof}[Proof sketch]` whose body says "Parts (i)–(iii) are proved in Chapter~\ref{chap:e1-modular-koszul}". | AP60 / AP40: tag is `ProvedHere` but the proof is elsewhere. The text proves nothing here; it cites. | Either keep the full proof inline (preferred — this is a strong, citable result) or downgrade tag to `\ClaimStatusProvedElsewhere`. The standalone is intended to be a SURVEY; tag should be `ProvedElsewhere`. |
| O5 | introduction_full_survey.tex | 1765–1819 | `\begin{theorem}[Central charge complementarity; \ClaimStatusProvedHere]` with proof citing thm:w-algebra-koszul-main + thm:w-koszul-precise. | The c+c'=2dim g part is genuinely proved here (5-line algebraic identity). The W-algebra part is computed elsewhere. Mixed. | Split into `\begin{theorem}` (Lie part, ProvedHere) + `\begin{theorem}` (W-algebra part, ProvedElsewhere) OR keep combined as `\ClaimStatusProvedElsewhere`. |
| O6 | introduction_full_survey.tex | 2168–2189 | `\begin{theorem}[\hat A-genus universality; \ClaimStatusProvedHere]` for the all-genera identity. | Body confesses "for arbitrary modular Koszul algebras (including multi-weight families), the genus-1 coefficient F_1=κ/24 holds unconditionally" — i.e. ALL-GENERA holds only on uniform-weight; multi-weight at g≥2 has δF_g^cross ≠ 0. The `ProvedHere` tag does not specify the scope restriction. | Add UNIFORM-WEIGHT regime tag inside the theorem (per AP32 which Vol I already enforces in chapter source). Tag stays ProvedHere only if scope-tagged. |
| O7 | introduction_full_survey.tex | 2125–2133 | "The gravitational cross-channel correction has a universal closed form for all principal W_N algebras (Proposition~\ref{prop:universal-gravitational-cross-channel}): δF_2^grav = (N-2)(N+3)/96 + (N-2)(3N^3+14N^2+22N+33)/(24c), vanishing iff N=2 (Virasoro). The formula is exact for W_3 and a lower bound for N≥4." | "Universal closed form" + "exact for N=3 only, lower bound for N≥4" is internally inconsistent. The pattern matches prior wave-3 finding. | Reword: "exact at N=3; a uniform lower bound at N≥4". The "universal" framing is misleading. |
| O8 | introduction_full_survey.tex | 4843 | "saturated at the self-dual point c=13" without distinguishing which self-duality. | L5427 of the SAME document distinguishes "chiral Koszul self-dual at c=13" from "quadratic self-duality at c=0". L4843 drops this caveat. | Within-document inconsistency. Match L5427 phrasing: "saturated at the chiral Koszul self-dual point c=13 (Pitfall: not c=0, where quadratic self-duality holds with κ=0)". |
| O9 | introduction_full_survey.tex | 4856–4862 (MC table) | MC1 "proved", MC2 "proved", MC3 "proved", MC4 "proved", MC5 "analytic part proved". | Same intro text immediately below table says: "MC3 holds for all simple types on the evaluation-generated core; the residual DK-4/5 problem is downstream of MC3"; MC5 only the analytic HS-sewing is proved with BV/BRST/bar identification at higher genus conjectural and tree-level pairing CONDITIONAL. The single-word "proved" in column 3 of the table elides this. | Replace single-word status by status with scope: "MC3 — proved on evaluation core; DK-4/5 downstream"; "MC4 — proved on standard landscape; one-stop limit conditional"; "MC5 — analytic proved; BV/BRST/bar conjectural at g≥1". |
| O10 | guide_to_main_results.tex | 73 | "ten unconditionally proved equivalent, one conditional (Lagrangian criterion, pending perfectness/nondegeneracy), one one-directional (D-module purity)". | Matches chapters/theory/chiral_koszul_pairs.tex exactly. **No overclaim.** | OK. |

### 1.2 ProvedHere tags inside standalones

A standalone document is a SURVEY. By Vol I AP60: "Tag only genuinely new content ProvedHere. Classical parts ProvedElsewhere with attribution." Of the 8 ProvedHere tags inside `introduction_full_survey.tex` (lines 499, 1765, 2168, 2718, 3514, 3584, 5084), only thm:central-charge-complementarity (1765) has a self-contained proof. The others either delegate to chapters (thm:e1-primacy, thm:ahat-universality-intro) or are stated without proof (thm:hochschild-poly-growth at 3584). All 7 should be `ProvedElsewhere`. The single self-contained one is borderline — its proof relies on `thm:w-algebra-koszul-main` and `thm:w-koszul-precise` cited as "verified for sl_2 in" and "for sl_3 in".

---

## Section 2 — Inflated-count audit

### 2.1 Twelve vs. fourteen Koszul characterisations

**Ground truth:** chapters/theory/chiral_koszul_pairs.tex,
`thm:koszul-equivalences-meta` (\ClaimStatusProvedHere), enumerates **(i)–(xii)**:
ten unconditional + Lagrangian (xi, conditional) + D-module purity (xii,
one-directional). The auxiliary file holographic_codes_koszul.tex uses K1–K12.

| Document | Stated count | Diagnosis |
|---|---|---|
| chapters/theory/chiral_koszul_pairs.tex (canon) | **12** ((i)–(xii)) | ground truth |
| chapters/connections/holographic_codes_koszul.tex | **12** (K1–K12) | consistent |
| chapters/theory/introduction.tex | **12** (K1–K12) | consistent |
| chapters/frame/guide_to_main_results.tex (line 67–73) | **12** | consistent |
| standalone/introduction_full_survey.tex (line 4839) | **12** (K1–K12) | consistent |
| standalone/programme_summary.tex (line 1072) | **12** | consistent |
| standalone/programme_summary_sections2_4.tex (line 496) | **12** | consistent |
| standalone/survey_modular_koszul_duality.tex (line 3026, 5410) | **12** | consistent |
| standalone/survey_modular_koszul_duality_v2.tex (line 633, 3357) | **12** | consistent |
| standalone/survey_track_a_compressed.tex (line 293, 1704, 2104, 2155) | **12** | consistent |
| **standalone/koszulness_fourteen_characterizations.tex** (title, abstract, theorem) | **14** | **OUTLIER** |

The standalone `koszulness_fourteen_characterizations.tex` re-numbers
(i)–(xiv) by interleaving five "named" auxiliary conditions (shadow-tower
formality, E_2-formality of ChirHoch, curve independence, PBW universality,
tropical Koszulness, Sklyanin H^2=0) into the canonical twelve. Its own
Remark (line 516–531) explicitly notes the parent monograph counts twelve.
This is INTERNAL DOCUMENTATION OF AN INCONSISTENCY: the standalone's title
claim "fourteen" is admitted to be a re-grouping, not a count of distinct
results.

**Healing:** Either (a) align the standalone title to "Fourteen formulations
of twelve characterisations" or (b) reconcile to twelve and present the
five auxiliary conditions as named refinements within the (i)–(xii)
framework (preferred — the parent monograph theorem is the ground truth).
The Sklyanin condition (xiv in the standalone) is explicitly affine-only,
not on the same logical footing as the universally-applicable (i)–(x).

### 2.2 Five-component vs. six-component differential D

**Ground truth:** survey_modular_koszul_duality.tex §3.9 (line 1733) and
survey v2 (line 2044) enumerate **six** components:

> $D^{\log}_{\mathrm{mod}} = d_{\check C} + d_{\mathrm{Ch}_\infty} +
> d_{\mathrm{coll}} + d_{\mathrm{sew}} + d_{\mathrm{pf}} + \hbar\Delta$.

| Document | Stated count | Listed components | Diagnosis |
|---|---|---|---|
| survey v1 §3.9 | 6 | čech, Ch∞, coll, sew, pf, ħΔ | ground truth |
| survey v2 §3.9 | 6 | same | consistent |
| introduction_full_survey.tex L2615 | **5** | int, [τ,−], sew, pf, ħΔ | OMITS čech AND coll, conflates them as `[τ,−]` |
| introduction_full_survey.tex L4374 | **5** | čech, Ch∞, coll, sew, loop | OMITS d_pf (planted-forest); renames ħΔ → d_loop |
| programme_summary.tex (search "five-component") | 1 hit | … | matches L2615 |

So within the SAME standalone (intro), the differential D is given two
DIFFERENT five-tuples, neither matching the survey's six-tuple. The
planted-forest correction d_pf is silently dropped in one passage; the
čech and Ch∞ summands are silently merged in the other. These are not
reformulations — d_pf is an independent operator on a distinct boundary
stratum.

**Diagnosis:** wave-3 inflation pattern, but here it's the *opposite*:
DEFLATION (six → five). The narrative under-counts components when
listing them inline because the AP-CY57 narration habit ("the
differential has K components, here are some") doesn't enforce a complete
enumeration. AP-CY57 / AP155.

**Healing:** All four narrative occurrences should give the canonical six
in the same order as survey §3.9, or cite it.

### 2.3 Seven faces of r(z)

**Ground truth audit:** intro L1438–4136 and programme_summary.tex §"seven
faces" enumerate seven "faces" of r(z):

1. F1 bar collision residue
2. F2 spectral R-matrix of ordered bar (CYBE)
3. F3 λ-bracket of PVA (Laplace transform)
4. F4 KZ connection
5. F5 Drinfeld r-matrix (KM-only)
6. F6 Sklyanin bracket (KM-only)
7. F7 Gaudin Hamiltonians (KM-only)

Self-confessed structure: F1–F4 hold for every modular Koszul algebra; F5–F7
specialize to affine Kac–Moody; the prose says "Faces (F5)–(F7) specialize
to affine Kac–Moody; the general case is obtained by replacing
$\Omega/((k+h^\vee)z)$ with $r_\cA(z)$".

**Diagnosis:** The four genuinely distinct invariants are F1–F4. F5, F6,
F7 are three classical KM-specialisations of F1 (collision residue evaluated
on KM, in three notational packagings). The prose effectively admits this
("not seven theorems but seven readings"). But the headline count is still
7, and the table is sold as a seven-fold identification.

This is the wave-1+3+4-confirmed pattern: **4 distinct objects inflated
to 7 presentations**.

**Healing options:**
- (a) Honest: "Four invariants, seven classical packagings" — keep the
  Drinfeld/Sklyanin/Gaudin trio as classical-literature pointers.
- (b) Aggressive: "Four faces" with sub-cases for KM. Loses citation
  appeal.
- (c) Strongest: keep "seven faces" as the citable unit but BOLDFACE the
  fact that F5, F6, F7 are *the same* face in three notational
  conventions (already in the prose; just promote it from prose to a
  formal Remark and to the table caption).

### 2.4 Five theorems

The intro and surveys consistently advertise "five theorems A, B, C, D, H".
This count is correct (A bar-cobar adjunction, B inversion, C complementarity,
D modular characteristic, H chiral Hochschild). But Theorem D is in fact
**two** theorems: D_scal (scalar modular characteristic, ProvedHere) and
D_Δ (spectral discriminant, separately proved non-scalar invariant).
introduction_full_survey.tex L1599–1644 explicitly distinguishes them.

**Diagnosis:** *minor*. The "five theorems" framing is justified at the
level of dramatic exposition (five invariants are five facets of Θ_A,
the Principle:five-facets at L1671). The promotion to "six theorems"
(A, B, C, D_scal, D_Δ, H) is an honest option.

**Verdict:** keep "five" — the D_scal/D_Δ split is internal to D; counting
it separately would require justification. But intro should *flag* the
split when it appears (currently does).

### 2.5 Three-pillar architecture

**Ground truth:** intro §4271 lists three pillars (MS24 hca, RNW19 conv-L_∞,
Mok25 log-FM). guide_to_main_results.tex repeats this. The number 3 is not
inflated — it is genuinely three independent preprints providing three
levels of upgrade.

**However**, the §4333 subtitle "Eleven identification theorems" lists 11
items, of which #11 is "ambient D^2=0 via Mok's Theorem 3.3.1(1)" (which is
*application* of Pillar C, not an independent identification). 10 vs 11 is
borderline; defensible. Compare to the "10 unconditional + 1 conditional +
1 one-directional" structure of the K-12 — this is the same accounting habit.

### 2.6 Four-test interface

guide_to_main_results.tex L298-319 and intro §4905 advertise "four
independent proved tests" (D^2=0, obs_g=κλ_g uniform-weight,
complementarity, sewing). Within Vol I AP32 enforces UNIFORM-WEIGHT
tagging. The intro's statement of test 2 is correctly tagged "(uniform-weight
lane)". The guide's `princ:guide-four-test-interface` is also tagged
correctly. **No overclaim.**

---

## Section 3 — Cross-reference & convention breakage

### 3.1 r-matrix level normalisation (AP126)

Two conventions coexist across the standalones for the KM r-matrix:

| Convention | Literal | k=0 limit | Document |
|---|---|---|---|
| trace-form | r(z) = k Ω/z | 0 (correct) | programme_summary.tex L1480; preface.tex L738 etc. |
| critical-level | r(z) = Ω/((k+h^∨)z) | Ω/(h^∨ z) ≠ 0 (suspicious — see AP126) | programme_summary_sections5_8.tex L122, L176, L191; programme_summary_sections9_14.tex L128; intro L488 |

The proposition body of `thm:seven-faces` in
programme_summary_sections5_8.tex L174–179 reads:

> The Drinfeld r-matrix (for $\cA = \widehat\fg_k$): $r(z) = \Omega/((k+h^\vee)z)$.
> Equivalently, in the trace-form convention $r(z) = k\Omega_{\mathrm{tr}}/z$
> with $k\Omega_{\mathrm{tr}} = \Omega/(k+h^\vee)$ at generic $k$.

This is honest about the convention bridge — **but** the table at L122
records `Ω/((k+h^∨)z)` as the bare entry without the trace-form bridge
side-by-side. By itself, that entry is an AP126 violation pattern: at
k=0 this does not vanish.

**Diagnosis:** AP126 the most-violated AP across volumes (per Vol III
CLAUDE.md). The fix is to write the entry as `(k Ω)_{tr}/z` or to add
the bridge inline. The intro at L488 has the same issue.

### 3.2 c+c' vs κ+κ' in the master invariant table

introduction_full_survey.tex §5241 master invariant table column "K":
Heisenberg K=2, free fermion K=0, sl_2_k K=6, βγ K=0, Vir K=26, W_3 K=100.

But the *meaning* of K is mixed:
- For KM (sl_2): K = c+c' = 2 dim g = 6 (proved; this is c-conductor)
- For Heisenberg: K = c+c' = 1+1 = 2 (c-conductor)
- For free fermion: K = 0 — but c=1/2, so c+c' = 0 means c'=-1/2; this is consistent with κ+κ'=0 (κ-conductor) for free-field Koszul self-duality
- For Vir: K = 26 (c-conductor, c+c'=26)
- For W_3: K = 100 (c-conductor)
- For βγ: K = 0 (κ-conductor or c-conductor? βγ has c=2; if c+c'=0 then c'=-2; if κ+κ'=0 then κ=-1)

The same column is being used for two different conductors depending on
the family. This is the AP-CY55 pattern (manifold/algebraization invariant
conflation; here: c-conductor vs κ-conductor).

**Diagnosis:** AP-CY55-style conflation in a Vol I table. Either split into
two columns (K_c and K_κ), or pick one and stick with it.

### 3.3 v1 vs v2 survey: both shipped

Both `survey_modular_koszul_duality.tex` and
`survey_modular_koszul_duality_v2.tex` exist. Headers differ
(report → amsart). Section numbering differs (v2 has new §1.10–1.11 on
E_n hierarchy and §2.8–2.9 on E_n hierarchy and bar-chain models;
§7.5b for bc system; §7.10–7.13 are entirely new). Both are 8500 lines.

If both ship, readers will receive contradictory accounts (e.g. v1 §1.5
"Two duals"; v2 §1.5 "Chain-level Heisenberg ordered bar"). If only one
ships, the older should be retired.

**Diagnosis:** v2 supersedes v1. Recommend deletion (or move v1 to
`/standalone/_archive/`). Decision belongs to author.

### 3.4 Preface variants

`chapters/frame/preface.tex` (4717 lines, current),
`chapters/frame/preface_section1_v2.tex` (581 lines),
`chapters/frame/preface_section1_draft.tex` (27864 bytes),
`chapters/frame/preface_sections2_4_draft.tex` (46760 bytes),
`chapters/frame/preface_sections5_9_draft.tex` (37103 bytes),
`chapters/frame/preface_sections10_13_draft.tex` (30508 bytes).

Five draft files in addition to the live preface. Drafts are clearly
working state. The live preface is consistent with intro on most
results. **No drift detected within the live preface itself**, but the
existence of the drafts creates risk of accidental input.

### 3.5 editorial.tex consistency

editorial.tex is a build wrapper (18 lines) that includes
`chapters/connections/concordance.tex` and `editorial_constitution.tex`.
The constitution chapter (2910 lines) carries Conjectured/Conditional tags
for the AdS/CFT bridge, NC Hodge, analytic completion, V1 Vassiliev
conjectures (~10 ClaimStatusConjectured tags). These are correctly
distinguished from the ProvedHere statements and consistent with the
intro's MC frontier section. **No editorial overclaim detected** within
the editorial chapter itself.

The build wrapper does NOT include the standalones; the editorial PDF
is the constitution-only build, separate from the surveys. This is
fine architecturally; the issue is that the standalone surveys are not
under the editorial discipline that the chapters are.

### 3.6 Cross-volume Part references

Spot-checked `Part~[IVXL]` patterns in narrative documents. No stale
hardcoded Part numbers found in target files (intro, programme summary,
surveys, preface, guide_to_main_results). AP-CY13 / V2-AP26 holding.

---

## Section 4 — Buried strong results (candidates for promotion)

The narrative occasionally buries an Annals-grade statement in
sub-section prose. Candidates:

| # | Result | Buried at | Strength | Promotion path |
|---|---|---|---|---|
| B1 | **All-genus generating function** $\sum F_g \hbar^{2g} = \kappa(\hat A(i\hbar) - 1)$, radius $2\pi$ INDEPENDENT of A. | introduction L2179–2185 (Theorem~\ref{thm:ahat-universality-intro}, ProvedHere) | High: a single closed-form Hirzebruch genus governs every uniform-weight chiral algebra. | Promote to Theorem 1.1 of intro. Currently it's tucked in §2202 (subsection 2.5). The *radius of convergence is universal* clause is what makes this Annals-grade — it is buried in a parenthetical. |
| B2 | **Bosonic-string critical dimension as an algebraic shadow**: c+c'=26 for sl_2 W-Koszul without invoking BV/bar bridge (preface L2156, intro L1821 Remark). | intro Remark L1821 | Medium-high. The remark *explicitly* says "the bosonic string critical dimension follows from Koszul duality at the scalar level without this bridge." This is the cleanest algebraic recovery of c=26 outside string theory's BRST construction. | Promote to a named Corollary `cor:bosonic-string-from-koszul`, currently buried in a Remark. |
| B3 | **W_3 closed-form cross-channel correction** $\delta F_2 = (c+204)/(16c)$. | intro L2118 | Medium. First explicit multi-channel computation. | Already a `\begin{equation}` and footnoted to `Theorem~\ref{thm:multi-weight-genus-expansion}(vi)`. Could be promoted to a named Computation in the master table at §5241. |
| B4 | **Koszul self-duality classification**: Heisenberg NOT self-dual, Vir self-dual at c=13 (chiral) and c=0 (quadratic). | intro L5417, L5427 (in "Critical pitfalls" subsection at the END) | Medium. This is a clean classification — Vol I has classified Koszul self-duality across all standard families. | Promote into the master invariant table as a "self-dual?" column. |
| B5 | **Five-facets principle for $\Theta_\cA$** (existence/faithfulness/decomposition/leading-coeff/coefficient-ring). | Principle L1671–1719 | High. Replaces five separate theorems with five facets of one element. This is the structural climax of Vol I. | Already a Principle environment. Should appear in the abstract of intro/programme summary, not just in §"The five theorems". |
| B6 | **The MC element is automatically Maurer–Cartan from D^2=0**: $\Theta_\cA := D_\cA - d^{(0)}_\cA$ MC because $D_\cA^2=0$. (intro L1363–1366; thm:mc2-bar-intrinsic) | intro L1361 | Very high — this is "MC2" of the MC frontier. The proof is one line of expansion. | Already a theorem with a label. Promote a one-line statement to the abstract: *"the universal MC element exists by intrinsic construction, not by perturbation theory"*. |

---

## Section 5 — First-principles analyses (AP-CY61 protocol)

For each confusion uncovered in §1–§3:

### 5.1 "Single open conjecture is CY-A_3" (O1, O3)

- **Ghost theorem.** *Vol I is autonomously self-contained.* The Vol I
  programme is closed under its own four-test interface.
- **Precise error.** Conflates *Vol I autonomy* with *programme
  completion across volumes*. CY-A_3 is a Vol III result; saying it
  was the "last unresolved input" elides Vol III's continuing work
  (CY-C abelian, nonabelian K3 Yangian, ZTE T-matrix existence,
  Sp_4(Z) modularity, root-of-unity).
- **Correct relationship.** Vol I closes its own MC1–MC5 frontier (with
  named conditional pieces as documented in MC table O9). The CY-A_3
  ∞-cat proof closes the 3D extension *as an algebraic prerequisite*,
  but the Vol III/CY-C frontier remains open. The Vol I narrative may
  honestly say: *"Within Vol I, no proved theorem depends on an
  unresolved Vol III input. The Vol III frontier itself is not the
  subject of this volume."*

### 5.2 "Five components" vs "six components" of D (§2.2)

- **Ghost theorem.** *The bar differential decomposes by boundary
  stratum of $\overline{\cM}_{g,n}$.*
- **Precise error.** Two narration modes emerged: (a) the algebraic
  three-stratum mode (sep, pf, ns) plus internal +twist = 5; (b) the
  geometric six-stratum mode (čech + Ch∞ + coll + sep + pf + ns) = 6.
  Both are correct *given which strata you count*. The narrative oscillates
  without flagging the convention.
- **Correct relationship.** Six is the geometric count;
  five is the algebraic count after čech and Ch∞ are absorbed into the
  *internal differential* of A^ch_∞. The two are related by the
  identification d_internal := d_čech + d_Ch∞ when A is presented as a
  čech complex with Ch∞-vertices. Either is fine; **the narrative must
  pick one and cite the bridge**.

### 5.3 "Twelve characterisations" vs "fourteen" (§2.1)

- **Ghost theorem.** *Chiral Koszulness is detected by a closed
  list of equivalent conditions across multiple mathematical domains.*
- **Precise error.** The standalone re-numbers the canonical (i)–(xii)
  to (i)–(xiv) by promoting two named refinements (shadow-tower
  formality, Sklyanin H^2=0) to the level of independent characterisations
  rather than corollaries-of-the-meta-theorem. The standalone's own
  Remark concedes this.
- **Correct relationship.** Twelve is the canonical count. Five
  refinements — shadow-tower formality, E_2-formality of ChirHoch, curve
  independence, PBW universality, tropical Koszulness — are *consequences*
  with their own named status, not new equivalent conditions. Sklyanin
  H^2=0 is an *affine-only* characterisation, not on the same footing.

### 5.4 "Universal closed form" for $\delta F_2^{\mathrm{grav}}$ (§1, O7)

- **Ghost theorem.** *The leading multi-weight cross-channel correction
  for W_N has a closed-form polynomial expression in (N, c).*
- **Precise error.** "Universal" suggests *all-genera, all-N, exact*.
  In fact: (a) genus-2 only; (b) exact at N=3, lower bound at N≥4; (c)
  proves only that δF_2^grav vanishes iff N=2.
- **Correct relationship.** Three honest statements:
  1. *Existence:* δF_2^grav has a closed-form polynomial in (N, c).
  2. *Exactness:* the formula is exact at N=3 (W_3).
  3. *Lower bound:* the formula is a lower bound at N≥4; the gap
     is bounded by sub-leading channels not yet computed.
  None of these is "universal closed form".

### 5.5 c+c' vs κ+κ' in master table (§3.2)

- **Ghost theorem.** *Koszul duality constrains a sum of invariants.*
- **Precise error.** Two distinct conductors (c+c' for KM/Vir/W;
  κ+κ' for free-field Koszul self-duality) are listed in a single
  column "K". For free fermion the entry K=0 means κ+κ'=0; for sl_2 the
  entry K=6 means c+c'=6.
- **Correct relationship.** Two conductors:
  - *c-conductor:* $K_c(\cA) = c(\cA) + c(\cA^!)$. Equals 2 dim g for KM
    and a fixed root-datum constant for W (Theorem L1765).
  - *κ-conductor:* $K_\kappa(\cA) = \kappa(\cA) + \kappa(\cA^!)$. Equals 0
    for KM/free-field; nonzero for W (e.g. 13 for Vir).
  Listing them in one column conflates the two.

---

## Section 6 — Three upgrade paths (the strongest claims the intro can safely make)

The following claims are *defensible from existing chapter results* but
are currently understated in the narrative:

### Upgrade U1 — "Hirzebruch–Vol-I universality theorem"

**Current narrative (intro §2.5):** "the generating function is the
$\hat A$-genus … with radius of convergence $|\hbar| = 2\pi$, independent
of $\cA$."

**Strongest defensible upgrade:** This is a *Hirzebruch-class theorem*
identifying a $\overline{\cM}_g$-valued characteristic class (the
genus-$g$ obstruction $\mathrm{obs}_g$) with a single classical
multiplicative genus on the Hodge bundle $(x/2)/\sin(x/2)$, with one
universal scalar coefficient $\kappa(\cA)$. The radius-of-convergence
universality is genuinely independent of the algebra — a strong claim
deserving the abstract.

**Suggested abstract phrasing:**

> *Vol I proves that for every uniform-weight chirally Koszul algebra,
> the genus expansion of the modular Koszul obstruction is governed by
> a single classical multiplicative genus on the Hodge bundle, with one
> universal scalar — the modular characteristic — independent of all
> other algebraic data. The radius of convergence $2\pi$ is a universal
> geometric constant.*

### Upgrade U2 — "MC element exists by construction, not by perturbation"

**Current narrative (intro §1.5 / Theorem mc2):** "$\Theta_\cA$ is automatically
Maurer–Cartan because $D_\cA^2 = 0$."

**Strongest defensible upgrade:** This is a *zero-perturbation existence
theorem* for the universal Maurer–Cartan element — no order-by-order
extension, no obstruction theory required. The MC element is present in
the bar differential from the outset; the shadow obstruction tower is its
finite-order *projections*, not its successive *constructions*.

**Suggested abstract phrasing:**

> *Vol I exhibits the universal Maurer–Cartan element of the modular
> convolution dg Lie algebra as the positive-genus part of the bar
> differential itself. No order-by-order extension is required: the MC
> equation is a tautology of $D_\cA^2 = 0$.*

### Upgrade U3 — "Free-field exactness as a structure theorem"

**Current narrative (intro §"the standard families"):** "Heisenberg has
$r_{\max} = 2$ (formal, $\Delta=0$); affine KM has $r_{\max}=3$; βγ
has $r_{\max}=4$; Virasoro and W_N have $r_{\max}=\infty$."

**Strongest defensible upgrade:** The bar spectral sequence collapses
at $E_1$ for *every* free-field algebra (Heisenberg, free fermion,
βγ, bc, lattice). This is a strong family-level *exactness* theorem,
not a case-by-case computation.

**Suggested narrative upgrade:**

> *For every free-field chiral algebra (Heisenberg, free fermion, βγ, bc,
> lattice), the bar spectral sequence collapses at $E_1$ and the bar
> cohomology is concentrated in degree~1 with explicit polynomial
> Hilbert series. Free-field exactness is the algebraic shadow of
> Wick's theorem.*

---

## Section 7 — Punch list

Twenty-seven discrete items the author can address in a focused session:

### Status / overclaim

1. programme_summary.tex L98 abstract: replace "single open conjecture is
   the CY-A correspondence at d=3" with scope-aware language.
2. programme_summary.tex L2599: tag `thm:cy-a3` with
   `\ClaimStatusProvedElsewhere`, cite Vol III thm:derived-framing-obstruction.
3. programme_summary.tex L2619: replace "No open conjecture in the
   programme has unresolved algebraic prerequisites" with Vol-I-scoped
   version.
4. introduction_full_survey.tex L499: change `\ClaimStatusProvedHere` →
   `\ClaimStatusProvedElsewhere` for thm:e1-primacy (the "proof sketch"
   delegates to chap:e1-modular-koszul).
5. introduction_full_survey.tex L1765: thm:central-charge-complementarity
   — keep ProvedHere only if the W-algebra computation citations are
   demoted to "verifications"; otherwise downgrade.
6. introduction_full_survey.tex L2168: thm:ahat-universality-intro —
   add UNIFORM-WEIGHT regime tag in the theorem header (not just in body
   prose).
7. introduction_full_survey.tex L2125–2133: rephrase "universal closed
   form" → "exact at N=3, lower bound at N≥4".
8. introduction_full_survey.tex L4843: add quadratic-vs-chiral self-dual
   distinction at first mention.
9. introduction_full_survey.tex L4856–4862 (MC table): replace
   single-word "proved" by scoped status for each MC.
10. introduction_full_survey.tex L3514, L3584, L5084 (other ProvedHere
    standalone tags): audit each for AP60 compliance.

### Inflated counts

11. **DECISION**: standalone/koszulness_fourteen_characterizations.tex —
    align to twelve (rename + restructure) OR retitle as
    "Twelve characterisations and two refinements".
12. introduction_full_survey.tex L2615 (five-component differential):
    replace by canonical six-component decomposition (matching survey
    §3.9).
13. introduction_full_survey.tex L4374 (five-component differential,
    different five): same fix.
14. programme_summary.tex (one inline "five-component"): same fix.
15. programme_summary_sections5_8.tex L194–197: keep "seven faces" but
    promote the F5/F6/F7-are-three-conventions remark to a formal Remark
    or table footnote.
16. introduction_full_survey.tex §"Eleven identification theorems":
    consider whether item #11 (ambient D^2=0) is an identification or an
    application; minor.

### Cross-reference / convention

17. programme_summary_sections5_8.tex L122 (KM table entry
    `Ω/((k+h^∨)z)`): rewrite as `kΩ_{tr}/z` with bridge inline (AP126).
18. programme_summary_sections5_8.tex L176 (face F5 in seven-faces
    theorem): same.
19. programme_summary_sections9_14.tex L128: same.
20. introduction_full_survey.tex L488: same.
21. introduction_full_survey.tex master invariant table L5249–5260:
    split column "K" into "K_c" and "K_κ" (or pick one and add the
    other as a row under the table caption).
22. **DECISION**: archive or retire
    standalone/survey_modular_koszul_duality.tex (v1) in favour of v2.
23. **DECISION**: archive five preface_section*draft.tex files in
    chapters/frame/.

### Buried strong results to promote

24. Promote thm:ahat-universality-intro radius-of-convergence-universality
    clause to the abstract (B1).
25. Promote rem:bosonic-string-26 to a named corollary (B2).
26. Promote Principle:five-facets to the abstract / Theorem 1 (B5).

### Cache write-back (for cross-volume protocol)

27. Add to first_principles_cache (Vol III) — see §8 below.

---

## Section 8 — Cache write-back (cross-volume AP-CY61)

Two new entries proposed for `appendices/first_principles_cache.md`
(or its Vol I analogue):

### Cache entry C1: "K columns mix two conductors"

| Field | Content |
|---|---|
| Wrong claim | "K = c + c' = 0 for free fermion (table column)" combined with "K = 26 for Virasoro (same column)" |
| Ghost theorem | Two distinct *Koszul-duality conductors*: c-conductor $K_c = c+c'$, κ-conductor $K_\kappa = \kappa + \kappa'$ |
| Correct relationship | $K_c(KM) = 2\dim\fg$, $K_c(W) = 2r + 4h^\vee \dim\fg$. $K_\kappa(KM) = 0$, $K_\kappa(\mathrm{free}) = 0$, $K_\kappa(W)$ root-datum constant |
| Confusion type | label/content (one column label, two contents), part/whole (two conductors collapsed) |

### Cache entry C2: "Five-component bar differential" deflation

| Field | Content |
|---|---|
| Wrong claim | "The total bar differential D has five components" (with two different five-tuples in same document) |
| Ghost theorem | The bar differential decomposes by boundary stratum of $\overline{\cM}_{g,n}$ on the log-FM compactification |
| Correct relationship | Geometric count: SIX (čech, Ch∞, coll, sep, pf, ns). Algebraic count: FIVE (internal, twist, sep, pf, ns) where internal := čech + Ch∞ + coll absorbed into A^ch_∞ |
| Confusion type | label/content, narration/construction, part/whole |

---

## Section 9 — Coda: the editorial discipline gap

The CHAPTERS in Vol I are under a strict editorial discipline: every
ProvedHere has a proof, every Conjecture has a label, every cross-volume
result has a ProvedElsewhere tag with attribution, AP32 enforces
UNIFORM-WEIGHT vs ALL-WEIGHT tagging, AP126 enforces
level-prefix on r-matrices.

The STANDALONES (intro, programme summary, surveys, preface
section drafts, fourteen-characterisations, BP self-duality, etc.) are
NOT under that discipline. The audit found:

- 8 ProvedHere tags in intro that AP60 would downgrade to ProvedElsewhere
- 1 untag​ged `\begin{theorem}[CY-A at d=3]` in programme_summary
- 4 distinct enumerations of the bar differential (some 5, some 6, with
  different summands)
- 2 separate inline values of "twelve" vs "fourteen" K-characterisations
- 2 r-matrix conventions coexist in the same standalone passage
- Mixed c-conductor / κ-conductor in a single table column
- Within-document drop of the chiral-vs-quadratic self-duality caveat

These are not errors of mathematical content — every proved chapter
result really IS proved. They are errors of *narrative discipline*: the
narrative under-states scoping qualifiers and over-states presentation
counts. This is the AP15 (README scope inflation) pattern catalogued in
Vol III, here observed in Vol I.

The healing path is not new mathematics; it is a discipline pass: align
every standalone status tag, count, and convention to the canonical
chapter source, and promote the truly strong results (U1, U2, U3) that
the chapters earn but the narrative buries.

---

**End of report.**
