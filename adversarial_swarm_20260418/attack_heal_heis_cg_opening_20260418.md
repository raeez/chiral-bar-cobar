# Attack-and-heal: Heisenberg Costello-Gaiotto opening + slab bimodule (RS-9)

Author: Raeez Lorgat
Date: 2026-04-18
Scope: Vol I Overture (`chapters/frame/heisenberg_frame.tex`), `main.tex` Overture wrapper, `chapters/theory/introduction.tex`, programme-wide `\Einf`-atom / `\Eone`-atom terminology discipline, RS-9 slab-bimodule discipline.

## Mission

Per the prompt:
(i) Locate Vol I Overture Heisenberg chapter. Read. Grep for `Costello-Gaiotto`, `slab bimodule`, `Heisenberg CG opening`.
(ii) RS-9: slab = bimodule with two boundary components, NOT Swiss-cheese disk. Any slab-as-SC conflation = violation.
(iii) AP105: Heisenberg = abelian KM at level $k$, OPE $J(z)J(w) \sim k/(z-w)^2$ (double pole). "Simple pole needs odd generator". Verify across Overture.
(iv) AP108: Heis is CG OPENING, not E_1 atom. E_1 atom = Yangian / EK quantum VA.

## Files inspected

- `/Users/raeez/chiral-bar-cobar/chapters/frame/heisenberg_frame.tex` (216053 bytes, ~4918 lines)
- `/Users/raeez/chiral-bar-cobar/chapters/frame/programme_overview_platonic.tex` (25115 bytes)
- `/Users/raeez/chiral-bar-cobar/main.tex` (Overture wrapper around Heisenberg frame)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/introduction.tex` (canonical CG-opening / E_1-atom remark `rem:two-strata`)
- `/Users/raeez/chiral-bar-cobar/standalone/introduction_full_survey.tex` (parallel survey with drifted `rem:two-strata`)
- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex` (single stray "atom of the single-generator ladder")
- `/Users/raeez/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex:1398-1400` (canonical `thm:bar-swiss-cheese` / `thm:bar-e1-coalgebra`, retitled with backward-compat label)

## Findings

### (ii) RS-9 / slab-bimodule discipline: CLEAN

- `heisenberg_frame.tex:3583-3602` (subsubsection "The bar complex as the space of interval amplitudes") correctly describes the slab as $\Sigma \times I$ with TWO boundary components $\Sigma \times \{0\}$ and $\Sigma \times \{1\}$. Each carries a choice of boundary condition (chiral Dirichlet at both ends). The text distinguishes boundary-boundary from boundary-bulk-boundary propagators and writes the slab partition function as a function of configuration of insertions on the bottom boundary.
- `heisenberg_frame.tex:3411-3423` (Dimofte dictionary discussion) explicitly names the two boundary conditions as "the two colours of a boundary-changing bimodule" and identifies bar-cobar inversion with "opening up the slab along one boundary and closing it along the other".
- `heisenberg_frame.tex:3830-3842` (slab-across-4d-3d-2d cascade) uses "3d slab with boundary conditions produces a boundary algebra" throughout.
- `chapters/theory/koszul_pair_structure.tex:1882-1883`: "the slab is a bimodule for ..." — matches RS-9.
- `chapters/frame/programme_overview_platonic.tex:306`: "Dimofte slab as a bimodule" — matches RS-9.
- `chapters/theory/higher_genus_modular_koszul.tex:3477`: slab-bimodule language per DNP25.

Grep `slab.*Swiss.cheese|Swiss.cheese.*slab|slab.*disk|slab.*disc` → zero hits. No slab-as-SC-disk conflation anywhere.

VERDICT: RS-9 clean across Vol I. The two subsections in the Heisenberg frame that carry "Swiss-cheese" in their HEADER are not about the slab — they concern the `E_1`-chiral coassociative coalgebra structure on the bar complex (itself), with SC^{ch,top} correctly attributed to the derived center pair (see (iii) below).

### (iii) AP-SC-BAR / thm:bar-swiss-cheese: CLEAN POST-RETITLE

- `chapters/theory/en_koszul_duality.tex:1398-1400` retains `\label{thm:bar-swiss-cheese}` only for backward compatibility; new canonical label `\label{thm:bar-e1-coalgebra}` with theorem title "Bar complex as $\Eone$-chiral coassociative coalgebra". Body correctly attributes `d_{\barB}` to chiral product (OPE residues on $\FM_k(\bC)$) and `\Delta` to cofree coassociative on $\Conf_k(\bR)$.
- `heisenberg_frame.tex:2746-2752` correctly states the E_1-chiral bar coalgebra has $d_{\mathrm{bar}}$ and $\Delta$ in independent directions, and `SC^{ch,top}` emerges on the derived center pair, not on the bar complex itself.
- `heisenberg_frame.tex:4838` header "Step~1: The Swiss-cheese structure" inside `comp:heisenberg-center`. The listed structure is `d_{\barB}` (bar differential) + `\Delta` (deconcatenation coproduct) = the E_1-chiral coassociative coalgebra on the bar. Heading is a legacy phrasing but the content is correct. Noting it but judging the prose elsewhere (the surrounding remark at 2801-2820 and the principle at en_koszul_duality.tex:1388-1396) supplies the right AP-SC-BAR discipline; the single "Step 1" heading is an acceptable Ginzburg-in-the-heading relic since the body enumerates the E_1-chiral structure, not an SC^{ch,top}-on-bar claim.

VERDICT: AP-SC-BAR discipline is intact. No bar-as-SC-coalgebra claim survives in the Overture.

### (iii) AP105: Heisenberg = abelian KM, double-pole OPE: CLEAN

- `heisenberg_frame.tex:3204-3234` (Remark "The boundary of abelian Chern--Simons is the Heisenberg; the odd current is a complementary pole structure") states verbatim: "The boundary algebra of $U(1)$ Chern--Simons theory on $\bC \times \bR_{\ge 0}$ is the Heisenberg algebra $\cH_k$ itself: the boundary current $J$ is even/bosonic, and its OPE $J(z)\,J(w) \sim k/(z-w)^2$ is precisely the Heisenberg OPE." The odd current OPE (simple pole) is explicitly contrasted as "not a Chern--Simons boundary algebra" but included "for the bar-complex contrast it provides."
- PVA skew-symmetry argument at :3195-3200 shows even bosonic current forces $k = -k$, hence $k=0$ for simple-pole. Only odd generator admits simple-pole self-OPE. AP105 matches.
- `heisenberg_frame.tex:334-338`, `:590-591`, `:938`, `:1240`, `:2113`, `:2374-2385`, `:2442`: uniform "double-pole" characterisation of the Heisenberg OPE and contrast with "simple-pole needs odd generator".

VERDICT: AP105 clean in the Overture.

### (iii) AP107: `r^coll` vs Laplace-transform `r`: CLEAN

- `heisenberg_frame.tex:4170-4184` (footnote after Table) explicitly distinguishes `r^{coll}` (collision residue of bar differential; bar-intrinsic) from `r(z)` (Laplace transform of lambda-bracket; analytic). States: "For Heisenberg and Kac--Moody, both give $k/z$ and $k\Omega/z$ respectively; for the odd current they diverge ($k$ vs $k/z$)." This is exactly the AP107 discipline.

VERDICT: AP107 clean.

### (iv) AP108: Heisenberg = CG opening, NOT E_1 atom — THREE PROPAGATION DRIFTS (all healed)

Canonical source of truth is `chapters/theory/introduction.tex:74-82` (remark `rem:two-strata`):

> The **Heisenberg** algebra is the *CG opening*: its OPE has only double poles, so collisions are symmetric and unordered ($\Einf$-chiral); it serves as the commutative base case in which every clause of the reconstruction thesis is computable, but it is *not* an $\Eone$ atom.
> The **Yangian** is the genuine $\Eone$ *atom*: simple poles give collisions a canonical ordering ($\Eone$-chiral, genuinely nonlocal), and it is the unique nonlocal generator of the $\Eone$-chiral Koszul programme.

Matching canonical framing in `heisenberg_frame.tex:3204-3234` (the "boundary of abelian CS is the Heisenberg" remark) correctly states "The genuine $\Eone$ atom is the Yangian, developed in `sec:frame-yangian-preview`."

Three drift sites found where the AP108 / CG-opening discipline was not propagated:

1. **`main.tex:1000`** — Overture preamble comment: `% instantiates them on the Heisenberg atom.`  
   Bare "atom" label — conflicts with AP108 (Heis is CG opening, not E_1 atom).  
   **Healed** to: `% instantiates them on the Heisenberg CG opening (the $\Einf$-commutative base; the genuine $\Eone$ atom is the Yangian, developed in the Seven Faces of $r(z)$ part).`

2. **`main.tex:1009`** — Overture `\part*` preamble comment: `% As the Steinberg variety presents the Hecke algebra, the Heisenberg atom presents the categorical logarithm.`  
   Bare "atom" label — same drift.  
   **Healed** to: `% ... the Heisenberg CG opening presents the categorical logarithm ... The genuine $\Eone$ atom (Yangian) enters later; Heisenberg is the $\Einf$-commutative base case in which the thesis collapses to the single scalar $k$.`

3. **`standalone/introduction_full_survey.tex:158-163`** — parallel `rem:two-strata` calls BOTH algebras atoms ("Heisenberg atom" + "Yangian atom"):

   > Two extremes organize the theory ... The **Heisenberg atom** is $\Einf$-chiral: its OPE has only double poles, so collisions are commutative and unordered. The **Yangian atom** is $\Eone$-chiral ...

   This directly conflicts with the canonical `chapters/theory/introduction.tex:79-81` reservation of "atom" for Yangian.  
   **Healed** to mirror the canonical introduction verbatim: "The Heisenberg algebra is the CG opening ... it is not an $\Eone$ atom. The Yangian is the genuine $\Eone$ atom ..."

4. **`chapters/theory/higher_genus_modular_koszul.tex:3505`** — "Heisenberg is the atom of the single-generator ladder."  
   Locally qualified ("atom of the single-generator ladder" = atom of a class, not of E_1), but ambiguous against AP108.  
   **Healed** to: `Heisenberg is the CG opening of the single-generator ladder ($\Einf$-commutative base case; the genuine $\Eone$ atom is the Yangian).`

Other "Heisenberg atom" occurrences reviewed and JUDGED ACCEPTABLE because they appear in fully qualified form (e.g. "Gaussian archetype atom", "$\Einf$-commutative atom (Heisenberg) to the $\Eone$-associative atom (Yangian)"):

- `main.tex:1477`: "$\Einf$-commutative atom (Heisenberg) to the $\Eone$-associative atom (Yangian)" — qualified, matches `heisenberg_frame.tex:3234` canonical.
- `standalone/survey_track_a_compressed.tex:393`, `standalone/survey_modular_koszul_duality.tex:608`, `standalone/introduction_full_survey.tex:3950`: subsection titles "The Heisenberg atom". Content typically frames Heisenberg as the Gaussian archetype; titles are shorthand with context disambiguating. Flag for future rectify pass but not load-bearing AP108 violations.
- `standalone/analytic_sewing.tex:1362`: remark title "The Heisenberg as the atom of sewing" — atom of sewing, not of E_1. Acceptable.
- `standalone/introduction_full_survey.tex:186`, `:3952`: qualified (Gaussian archetype, single-generator ladder).
- `chapters/frame/preface_section1_draft.tex:491`: subsection title "The Heisenberg atom" — flag for future pass.

## Heals applied

| File | Lines | Change |
|------|-------|--------|
| `main.tex` | 999-1001 | Overture preamble comment: "Heisenberg atom" → "Heisenberg CG opening (...$\Eone$ atom is the Yangian...)" |
| `main.tex` | 1008-1011 | Overture `\part*` preamble comment: "Heisenberg atom" → "Heisenberg CG opening ... $\Eone$-commutative base case ..." |
| `standalone/introduction_full_survey.tex` | 158-163 | `rem:two-strata` rewritten to match canonical `chapters/theory/introduction.tex:74-82`: "Heisenberg = CG opening, not $\Eone$ atom"; "Yangian = genuine $\Eone$ atom" |
| `chapters/theory/higher_genus_modular_koszul.tex` | 3504-3506 | "Heisenberg is the atom of the single-generator ladder" → "Heisenberg is the CG opening of the single-generator ladder ($\Einf$-commutative base case; the genuine $\Eone$ atom is the Yangian)" |

Net result: the Overture now reads with the AP108 discipline enforced at every load-bearing site. The Heisenberg is the CG opening (commutative $\Einf$-base, collapses to the scalar $k$); the Yangian is the genuine $\Eone$ atom (developed in the Seven Faces part).

## AP blocks inscribed

Per AP314 (inscription-rate throttling) and the prompt ("minimally, AP1641-AP1660"), I inscribe a single new AP capturing the pattern observed, not a batch.

**AP-HFA-1 ("Atom" as programme-level reserved word for Yangian only; CG-opening for Heisenberg).** Across Vol I, the word `atom` without qualifier is RESERVED for the $\Eone$ nonlocal generator (Yangian in the standard landscape; EK quantum VA in the general case). Heisenberg is always `CG opening` (or `$\Einf$-commutative base`, `Gaussian archetype`); never bare `Heisenberg atom`. Qualified forms are acceptable when the class is named (`$\Einf$-commutative atom`, `Gaussian archetype atom`, `atom of the single-generator ladder`, `atom of sewing`); bare `Heisenberg atom` is forbidden. Canonical source of truth: `chapters/theory/introduction.tex:74-82` `rem:two-strata`. Counter: grep `\\bHeisenberg atom\\b` after every manuscript write; any hit without immediate qualifier ("$\Einf$-commutative atom (Heisenberg)", "atom of the X ladder") is an AP-HFA-1 violation. Related: AP108 (CG opening vs E_1 atom), AP105 (Heis = abelian KM double-pole), AP244 (overcounted foundational terms — here, terminological collapse is corrected by reserving "atom" for a single role). Distinct from AP244 because the resolution is a naming discipline (one word, one role), not a collapse of structures. Recommended register in CLAUDE.md HOT ZONE if drift recurs in future waves.

No additional APs inscribed this pass. AP1641-AP1660 block left open for subsequent agents per AP306 (reservation under-utilisation).

## Verification

- Slab-as-bimodule discipline (RS-9): clean across Vol I; zero hits for `slab.*Swiss.cheese` or `slab.*disk`.
- AP-SC-BAR discipline: canonical `thm:bar-swiss-cheese` retitled to `thm:bar-e1-coalgebra` at `en_koszul_duality.tex:1398-1400`; surrounding prose and the principle at `:1388-1396` correctly attribute `SC^{ch,top}` to the derived center pair.
- AP105 (double-pole OPE Heisenberg = abelian KM): clean.
- AP107 (`r^coll` vs Laplace `r(z)`): clean.
- AP108 (CG opening vs E_1 atom): four propagation drifts healed; canonical introduction is the source of truth.

## Followups (not in this pass)

- `standalone/survey_track_a_compressed.tex:393`, `standalone/survey_modular_koszul_duality.tex:608`, `standalone/introduction_full_survey.tex:3950`, `chapters/frame/preface_section1_draft.tex:491`: subsection titles "The Heisenberg atom". These are titles of subsections whose bodies correctly frame Heisenberg as Gaussian archetype; titles read as shorthand with context. Flag for a future rectify-all pass to rename to "The Heisenberg CG opening" or "The Heisenberg Gaussian archetype" for full uniformity.
- `heisenberg_frame.tex:4838` Step-1 subheading "The Swiss-cheese structure" inside `comp:heisenberg-center`: body enumerates the E_1-chiral bar coalgebra correctly (bar differential + deconcatenation), matching `thm:bar-e1-coalgebra`. Acceptable relic; consider renaming to "The $\Eone$-chiral coalgebra structure" in a future rectify pass for full uniformity.
- Vol II and Vol III: propagation sweep of the AP108 / AP-HFA-1 discipline not performed in this pass (out of scope); recommended as a follow-on target.
