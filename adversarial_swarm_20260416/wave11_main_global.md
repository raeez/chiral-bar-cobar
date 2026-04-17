# Wave 11 — Vol I main.tex global structure (adversarial audit)

Date: 2026-04-16  
Auditor: adversarial referee, read-only pass on `~/chiral-bar-cobar/main.tex` (1956 lines), `Makefile` (469 lines), `CLAUDE.md` (1073 lines), and immediate front/back-matter dependencies. **No commits, no manuscript edits.** All findings are recommendations for the manuscript author (Raeez Lorgat). Where the wave brief proposed an upgrade path, that path is preserved as the default; downgrades appear only where no upgrade is feasible.

---

## §1. main.tex skeleton (Parts, chapters, standalones)

### 1.1 Document class and edition switch

`\documentclass[11pt]{memoir}` (inferred from `\PassOptionsToClass{draft}{memoir}` in the Makefile draft target). The Annals/Archive switch is the single most consequential preamble macro:

```
141  \newif\ifannalsedition
142  \annalseditiontrue                  % default = Annals (public)
144  \ifdefined\archivebuild              % override
145    \annalseditionfalse
146  \fi
```

`make fast` therefore builds the Annals edition by default. The full archive build requires `pdflatex "\def\archivebuild{1}\input{main}"` or equivalent, which is **not** wired into a Makefile target — see §5.

### 1.2 Part / opener structure

Six numbered parts plus an unnumbered Overture, all defined in `main.tex` itself (no `\part{}` declarations leak into chapter files — verified with `grep '\part'` over `chapters/frame/`):

| # | Line | `\part{...}` | `\label`                         |
|---|------|--------------|----------------------------------|
| Overture | 871 | `\part*{Overture}` (unnumbered) | (none — uses `\addcontentsline`) |
| I | 899 | The Bar Complex | `part:bar-complex` |
| II | 1088 | The Characteristic Datum | `part:characteristic-datum` |
| III | 1182 | The Standard Landscape | `part:standard-landscape` |
| IV | 1390 | Physics Bridges | `part:physics-bridges` |
| V | 1511 | The Seven Faces of the Collision Residue | `part:seven-faces` |
| VI | 1544 | The Frontier | `part:v1-frontier` |

Cross-references to parts inside `main.tex` (8 hits) all use `\ref{part:...}` (no hardcoded `Part~II` strings). **AP-CY13 / V2-AP26 clean within `main.tex`.**

Two structural caveats:

(a) **Overture is unnumbered (`\part*`)**, but the body cross-refs Overture content as if it were a real part (e.g. line 1186 `Chapter~\ref{ch:heisenberg-frame}` jumping straight from the proved core into the Overture chapter). Memoir's TOC-line trick (`\addcontentsline`) gives it a TOC entry but no Roman numeral, so the printed numbering is `Part I = Bar Complex` not `Part II`. This is intentional but creates a subtle off-by-one when prose writes "Parts~\ref{part:bar-complex}--\ref{part:seven-faces}" (line 1548): the Overture is silently excluded.

(b) **Parts V and VI are gated by `\ifannalsedition\else ... \fi`** (lines 1510 and inside 1544). In Annals edition, Parts V and VI are **invisible** but the abstract (lines 724–799) still claims results that live there (e.g. the seven-face identification of the collision residue). See §6 for the cascade.

### 1.3 Chapter inputs (81 `\input`/`\include` directives)

By directory:

- `chapters/frame/`: preface, guide_to_main_results (Annals only), heisenberg_frame.
- `chapters/theory/`: 22 chapters, including one stub-dispatcher pattern (3 chapters split into `_foundations` / `_complementarity` / `_inversion` units; the dispatcher `.tex` files are 5–6-line `\input` shells preserved at `chapters/theory/{higher_genus,bar_cobar_adjunction,examples/yangians}.tex` but **no longer included** from `main.tex`; the substantive files are `\input`'d directly).
- `chapters/examples/`: 22 chapters.
- `chapters/connections/`: 14 chapters across Parts IV–VI (some Annals-quarantined).
- `appendices/`: 8 reference appendices.

**Stale/dead `\input` paths within main.tex: NONE** — every `\input{...}` and `\include{...}` resolves to an extant file. Verified by enumerating all 81 paths and checking each against `ls`. The sole 5–6-line dispatcher stubs (`yangians.tex`, `higher_genus.tex`, `bar_cobar_adjunction.tex`) are no longer wired in (lines 1002, 1038, 1348 are commented out and a comment explicitly notes the substantive chapters are compiled directly). This is a **clean** state.

### 1.4 Standalone material

`standalone/` holds 36 `.tex` files (cover letters, surveys, theorem index). **None** are `\input`'d into `main.tex`; each is built by a separate Makefile pass (`standalone/$(paper).pdf`, see §5.2). The structural split is:

- Cover letters: `cover_letter_{garland_lepowsky, seven_faces, shadow_towers, virasoro_r_matrix}.tex` — pre-built PDFs already present.
- Surveys: `programme_summary{,_section1,_sections2_4,_sections5_8,_sections9_14}.tex`, `survey_modular_koszul_duality{,_v2,_track_a_compressed,_track_b_compressed}.tex`, `introduction_full_survey.tex`.
- Atomic results: `N1_koszul_meta`, `N2_mc3_all_types`, `N3_e1_primacy`, `N4_mc4_completion`, `N5_mc5_sewing`, `N6_shadow_formality`.
- Index/lookup: `theorem_index.tex`, `notation_index.tex`.

**Standalone artifact leak (V2-AP32) audit**: `\title{}/\maketitle/\begin{abstract}/\tableofcontents` appearing inside `chapters/frame/{preface,heisenberg_frame,guide_to_main_results}.tex` and `chapters/theory/introduction.tex` — **count = 0** in all four files. Front-matter chapters are clean; no double-rendering risk.

### 1.5 Phantom-label load

Lines 1616–1924 of `main.tex` contain ~280 `\phantomsection\label{...}` declarations gated by `\ifannalsedition`. These exist because Annals quarantines Parts V and VI plus several archive-only files (`genus_complete.tex`, `landscape_census.tex`, `editorial_constitution.tex`, `genus_expansions.tex`, `bar_complex_tables.tex`, etc.). Without the phantom stubs, every cross-reference to those files would render `??` in the Annals PDF.

This is **technically correct** but operationally fragile: it is a 280-entry parallel manifest that must be maintained by hand whenever an archive-only label is added/removed. Phantom-label management is V2-AP38 (retirement schedule) made manifest at scale. Recommendation surfaced in §10.

---

## §2. Abstract / title / front-matter audit

### 2.1 Title and author

Line 574: `\title{\textit{Modular Homotopy Theory for Algebraic Factorization Algebras on Algebraic Curves}\\[0.5em]\large Volume~1: Modular Koszul Duality and Holographic Corrections}`  
Line 575: `\author{Raeez Lorgat}`  
Line 576: `\date{August 2025}`  

**AI attribution check**: zero hits across `main.tex`, `chapters/frame/preface.tex`, `chapters/theory/introduction.tex`, `chapters/frame/guide_to_main_results.tex` for any of `AI|Claude|GPT|ChatGPT|Anthropic|noreply@anthropic|generated by AI|by Claude|with assistance|Co-Authored`. **Clean.**

**Date staleness**: The manuscript date reads "August 2025"; today is 2026-04-16. After ~9 months of intensive work (~30 closed waves, CY-A_3 promotion across the programme, 7-part rearchitecture in Vol III, etc.), an unchanged front-page date misrepresents the manuscript's age and currency. Not a bug, but a low-cost healing in §10.

### 2.2 Abstract scope vs Annals quarantine (cascade bug)

Abstract (lines 724–799) claims the **five theorems** plus the chiral-quantum-group equivalence ("vertex R-matrix, chiral A_∞-structure, chiral coproduct" — line 769ff) and the "Higher Deligne Conjecture, derived chiral center is E_3" identification (line 786ff). Two of these claims live in archive-only files:

- The "seven faces of the collision residue" centerpiece is Part V (`chapters/connections/holographic_datum_master.tex` and `chapters/connections/genus1_seven_faces.tex`). In Annals build these are quarantined behind `\ifannalsedition\else ... \fi` (line 1510).
- The chiral-quantum-group equivalence statement bridges to Part VI frontier material (`chapters/connections/frontier_modular_holography_platonic.tex`, `thqg_entanglement_programme.tex`), all `\ifannalsedition\else`-gated.

**The Annals abstract therefore advertises content the Annals reader cannot find.** The phantom-label stubs preserve cross-references at the syntactic level (`??` is suppressed) but the body of the cited results is absent. This is a **scope-inflation cascade** identical in structure to AP-CY15 (README scope inflation) but at the front-matter level: the abstract was written for the full archive and has not been retracted for the public edition.

Healing options:

(i) **Best**: build a separate `\ifannalsedition` abstract that lists only the four properties of the categorical logarithm (A–D) plus theorem (H) and explicitly forwards the seven-face / quantum-group material to the archive edition. ~8 lines of `\ifannalsedition...\else...\fi` around the affected paragraphs.

(ii) **Quick**: add a one-line Annals-only footnote `In the Annals edition, the seven-face identification (\S Part~V archive) and the chiral-quantum-group equivalence (\S Part~VI archive) are summarised but their proofs and computations live in the archive companion.` Honest framing without restructuring.

### 2.3 Notation block (lines 821–834)

The post-abstract notation block is correct. It introduces the curve-vs-disk distinction (`E_∞-chiral`, `E_1-chiral`, `P_∞-chiral` are curve-based; bare `E_n` is little-disks) and warns at line 832 that "a complex curve therefore enters the topological ladder at `n = 2`, not `n = 1`". This anchors **V2-AP1 / V2-AP12** at the front of the document — well-placed and load-bearing.

### 2.4 Keywords (lines 809–817)

Keywords are correct and current. Notably present: "shadow obstruction tower" (post-AP V2-AP36 rename, fully propagated; no residual "shadow Postnikov"), "modular convolution L_∞-algebra", "modular twisting morphism".

---

## §3. Part-opener audit

Each numbered Part has an opener paragraph immediately after its `\part{}` declaration. Quality varies:

### Part I: The Bar Complex (lines 899–960)

**A model opener.** Direct geometric construction (place sections at points, wedge against `d log(z_i - z_j)`, extract residues; Arnold's three-term identity forces `d^2 = 0`), then immediately enumerates four properties of the categorical logarithm (A–D) with theorem-quality precision and a clean (H) addendum. The "but `\kappa(\cA)` is only the *linear* leading term" sentence at line 949 is a load-bearing rhetorical bridge into Part II. **Chriss-Ginzburg-style per AP106**: opens with the problem, not "this chapter constructs". **No edits required.**

### Part II: The Characteristic Datum (lines 1088–1110)

**Strong opener.** Explicitly anchors `\kappa(V_k(\fg)) = \mathrm{av}(r(z)) + \dim(\fg)/2` against the abelian/scalar baseline (no AP39 violation), then forwards to the shadow obstruction tower. The "even this scalar is extracted from the collision residue r(z) by a Σ_2-coinvariant integral" sentence (lines 1097–1099) honestly admits curve-geometry dependency from the start. **No edits required.**

### E_1 Wing (lines 1136–1147)

This is **not** a numbered part — it's a section-like preamble inside Part II. The opener correctly states "The commutative engine of Parts ... uses symmetric configurations and the Fulton-MacPherson operad. The E_1 wing develops the ordered parallel: ribbon modular operads, FAss, E_1 convolution algebras, ordered shadow obstruction towers." But:

- The header comment (lines 1123–1136) calls this "E_1 Wing (absorbed into Part II)" — i.e. the wing was **promoted** out of being a standalone part. The promotion left the prose intact but removed the part header. **Result**: a major structural unit (E_1 modular Koszul duality, ordered associative chiral KD, E_n Koszul duality, the open/closed THQG realization chapter) sits inside Part II without a sub-part marker. Recommendation in §10.

### Part III: The Standard Landscape (lines 1182–1223)

Strong opener. Lines 1197–1213 give a substantive scientific narrative ("the bar cohomology dimensions of apparently unrelated algebras share a common discriminant Δ(x) = (1−3x)(1+x)... the Feigin-Frenkel involution k ↦ −k − 2h^∨ is Koszul duality..."). The classification axis "from the E_∞-commutative atom (Heisenberg) to the E_1-associative atom (Yangian)" lines up with the chapter ordering (lattice → free fields → Heisenberg → KM → W → N=2 → BP → Y-algebras → W_3 holographic → deformation quantization → Yangians → symmetric orbifolds → log-W). **No edits required.**

### Part IV: Physics Bridges (lines 1390–1410)

Strong opener. The "one kernel, one relation, many incarnations" framing (line 1410) is good. A subtle issue: the paragraph asserts the bar differential **is** the BRST differential (line 1403, `Chapter~\ref{ch:v1-bv-brst}`), but `bv_brst.tex` is `\input`'d only when **NOT** `\ifannalsedition` (line 1454). In Annals build, the BRST chapter is replaced by 12 `\phantomsection\label{ch:v1-bv-brst}...` stubs (lines 1416–1450). So the opener cross-references a chapter the Annals reader cannot read. Same cascade as §2.2. Recommendation in §10.

### Part V: Seven Faces (lines 1511–1521)

**Annals-quarantined entirely** (`\ifannalsedition\else` at line 1510 wraps the whole `\part`). The opener "One mathematical object... realized in seven independent mathematical frameworks, all proved to agree" exists in archive build only. In Annals build the centerpiece is invisible.

### Part VI: The Frontier (lines 1544–1565)

Annals **does** include this part header (line 1544 is outside the `\ifannalsedition\else` of line 1510), but most of its body chapters (`frontier_modular_holography_platonic`, `entanglement_modular_koszul`, `thqg_entanglement_programme`, `holographic_codes_koszul`, `semistrict_modular_higher_spin_w3`) are themselves built unconditionally — meaning **Annals readers do see Part VI**. Then the opener at line 1548 references `Parts~\ref{part:bar-complex}--\ref{part:seven-faces}` which includes Part V (the quarantined seven-faces part). In Annals, `\ref{part:seven-faces}` resolves only because `part:seven-faces` is defined inside an `\ifannalsedition\else` block — meaning **in Annals build, this `\ref` is undefined**. (To verify: `grep \\label{part:seven-faces}` only matches at line 1512, inside the `\ifannalsedition\else` guard at 1510.) **Genuine bug in the Annals build.** See §6 / §10.

### Reading paths

**There are no reading paths in Vol I.** Vol III's Part-opener wave installed three reading paths (algebraist, physicist, number theorist; cf. Vol III CLAUDE.md "Part openers + reading paths"). Vol I's preface hints at multi-audience structure (`chapters/frame/preface.tex` is 4717 lines and includes audience-targeted chapter assessments) but no explicit reading-path tables exist in `main.tex` or `guide_to_main_results.tex`. **Healing opportunity**, see §8(b).

---

## §4. Preamble and macro audit

### 4.1 Macro layer count

`main.tex` declares macros across at least **three** zones:

- Lines 380–525: theorem environments, operad/category macros, `\Eone/\Etwo/\Ethree/\En/\Einf` family, chiral operad macros (`\chirAss`, `\chirCom`, `\chirPois`, `\chirLie`, `\chirtensor`, `\facttensor`).
- Lines 470–525: `\providecommand` block for cross-volume migration safety (`\Barchord`, `\BarchFG`, `\BarchSig`, `\sewop`, `\sewker`, `\Defcyc`, `\Convstr`, `\Convinf`, `\Definfmod`, `\Gmod`, `\gAmod`, `\Perbr`, `\Ydg`, `\QGspec`, `\Factord`, `\Uvert`, `\Thetaenv`, `\chienv`, `\LCA`, `\JacF`).
- Lines 595–720: a **second** `\providecommand` block, executed inside `\begin{document}`, redefining many of the same symbols (`\Barchord` at L470 and L579; `\BarchFG` at L471 and L580; `\BarchSig` at L472 and L581; `\Cop`, `\Perf`, `\sewop`, `\sewker`, `\secquant`, `\zetareg`, `\GL`, `\Imag` all double-defined).

This is **safe** under `\providecommand` (silent no-op if already defined), but the duplication is a maintenance hazard: if a future edit upgrades the L470 definition to a `\renewcommand` for any reason, the L579 entry will silently fail to override and the upgraded definition will be lost. **Operational AP candidate** — see §10.

### 4.2 ClaimStatus tag definitions

Lines 148–164 define the six `\ClaimStatusXxx` macros conditionally on `\ifannalsedition`:

```
148–164:
  Annals build  -> all six \ClaimStatusXxx are no-ops (silent)
  Archive build -> textual tags [proved here], [proved elsewhere], [open],
                   [conjectured], [physical heuristic], [conditional]
```

This is the right design (Annals readers don't see internal provenance tags), but it has a **side effect**: the `make census` and `make audit` Makefile targets parse `.tex` for `\ClaimStatusProvedHere` etc. in `chapters/`, and they get the same count regardless of which edition built. Good. But the **AP4-style audit** ("the ClaimStatus tag must match the proof environment") cannot be enforced visually in the Annals PDF — a missing `\begin{proof}` after a `\ClaimStatusProvedHere` is invisible to the Annals reader. The discipline must come from `make verify` / `make integrity`. Verified those targets exist (Makefile lines 222, 293).

### 4.3 Style packages and conflicts

`ebgaramond` for body text + `garamondthm` / `garamonddef` theorem styles (declared via `thmtools`). 32 `\declaretheorem` registrations for theorem-like environments (lines 167–238). Notable: `theorem`, `lemma`, `proposition`, `corollary`, `verification`, `computation`, `conjecture`, `definition`, `example`, `remark`, `notation`, `convention`, `principle`, `motivation`, `insight`, `problem`, `setup`, `observation`, `idea`, `strategy`, `openproblem`, `hypothesis`, `warning`, `heuristic`, plus a `maintheorem` (only one in the document — line 210).

`\theH...` rebinding for hyperref (lines 244–289) covers all 32 environments. Stable hyperref anchors. Clean.

### 4.4 Cross-volume macro export

`main.tex` defines macros that Vols II and III use (e.g. `\SCchtop`, `\barBch`, `\Omegach`, `\ChirHoch`, `\Walg`, `\critLevel`, `\dzero`, `\dfib`, `\Dg`, `\Dtot`, `\mcurv`, `\Defcyc`, `\Gmod`, `\gAmod`). If these definitions drift between volumes, downstream cascade. The cross-volume migration discipline (V2-AP39: `\providecommand` for every imported macro in Vol II's preamble) is in force here, but **only Vol II** has the corresponding catch in its preamble. **Vol III's status is not visible from this audit** — flag for cross-volume sync, §10.

---

## §5. Makefile and build-target inventory

### 5.1 Standard targets

| Target | Action | Issue |
|--------|--------|-------|
| `make` (= `make all`) | `\$(STAMP) working-notes` -> 6-pass build of `main.tex` + 2-pass `working_notes.tex` -> `out/main.pdf`, `out/working_notes.pdf` | None |
| `make fast` | 4-pass quick build | Default Annals edition; no archive override exposed |
| `make release` | `clean` + 4-pass main + working-notes + standalone + `make icloud` | Calls all sub-targets; standalone target alone is 36 papers, ~3 passes each |
| `make working-notes` | 2-pass `working_notes.tex` | Suppresses pdflatex output; on failure shows nothing useful |
| `make standalone` | 36-paper iteration with 3 passes each | No `--halt-on-error`; failures silently logged |
| `make watch` | `latexmk -pvc` on `main.tex` | Standard latexmk |
| `make check` | Single halt-on-error pass | The CI gate |
| `make integrity` | `./scripts/integrity_gate.sh` | External script — not audited here |
| `make phase0-index` | Theorem dependency index | External Python |
| `make draft` | `\PassOptionsToClass{draft}{memoir}` single pass | Useful for iteration |
| `make clean` / `veryclean` / `clean-builds` | Standard | `clean-builds` removes `/tmp/mkd-*-*` across all three volumes — useful |
| `make count` | Statistics | Counts `.tex` files and PDF pages |
| `make metadata` / `census` / `audit` | Python-based metadata regeneration | External |
| `make verify` | `./scripts/verify_edit.sh --all` | Anti-pattern verification |
| `make test` / `test-full` | pytest on `compute/tests/` | Fast / full split |
| `make verify-independence` / `-verbose` | Audit independent-verification registry | New (per Vol III install) |
| `make icloud` | Copy PDFs to iCloud Drive | Personal workflow |
| `make editorial` | Build `standalone/editorial.tex` | One-off |
| `make dist` | Create `Vol1Archive.zip` | Distribution |

### 5.2 Coverage gaps

(a) **No archive-build target.** `make fast` and `make` always produce the Annals edition. To produce the full archive, the user must invoke `pdflatex` manually with `\def\archivebuild{1}\input{main}`. This makes archive-build regressions invisible — a chapter that compiles in Annals but breaks in archive (e.g. because of phantom-label collisions) won't be caught. **Recommend** new target `make archive` that sets `\def\archivebuild{1}` and runs the converging build.

(b) **No "build both editions" target.** A reviewer would want to see both PDFs side by side. Trivially: `make both: fast archive`.

(c) **No phantom-label audit target.** The 280 phantom-section labels in `main.tex` (lines 1616–1924) need auditing every session: each label must (i) be referenced from at least one Annals-included chapter, (ii) NOT be redundantly defined inside Annals-included content (which would cause a "label multiply defined" warning that's muted by `\providecommand`-style usage). A `make audit-phantoms` target — invoking a small Python script that scrapes Annals-included `.tex` files for the labels and reports orphans — would close V2-AP38 mechanically.

(d) **No part-opener / abstract scope audit.** §2.2 / §3 cascade is exactly the kind of bug that should be caught by a Makefile target. A `make audit-scope` that (i) parses the abstract for "Theorem X" claims, (ii) checks the corresponding chapter is in the active edition, (iii) reports mismatches — would catch the seven-face / Part V cascade.

(e) **No `\input`-graph integrity check.** The 81 `\input`/`\include` directives are checked manually here (§1.3). A 30-line bash script that walks `main.tex` and verifies every target exists would let a CI pass catch a deleted file. Recommend `make audit-inputs`.

### 5.3 Cross-volume orchestration

Makefile has no targets for invoking Vols II and III. CLAUDE.md (Vol III) lists three side-by-side build commands (`make fast` from each repo). A cross-volume `make all-volumes` would close that gap, but it requires the three volumes to share a build script (currently they do not — each volume has its own `Makefile`).

---

## §6. Global consistency table

Cross-checked claims of the form "Theorem X states Y" across `main.tex` abstract, `chapters/frame/guide_to_main_results.tex`, `standalone/theorem_index.tex`, and the cover letters.

| Claim | Abstract (main L724–799) | guide_to_main_results.tex | theorem_index.tex | Status |
|-------|--------------------------|---------------------------|-------------------|--------|
| **Theorem A**: bar-cobar adjunction with Verdier intertwining | "(A) bar-cobar adjunction with Verdier intertwining" (L753) | "Bar-cobar adjunction; intertwined with Verdier duality" | (auto-generated index of all `\begin{theorem}` blocks; 1121 entries) | **Consistent** |
| **Theorem B**: bar-cobar inversion on Koszul locus | "(B) bar-cobar inversion on the Koszul locus" (L754) | "Bar-cobar inversion: on the Koszul locus, the counit ... is a quasi-isomorphism at all genera" | — | **Consistent** |
| **Theorem C**: complementary Lagrangian decomposition | "(C) complementary Lagrangian decomposition of the center local system" (L755-757) | "Complementarity: $Q_g(\cA) \oplus Q_g(\cA^!) \cong H^*(\overline{\cM}_g, \cZ_\cA)$ for all $g \ge 1$" | — | **Consistent** |
| **Theorem D**: genus expansion `F_g = κ λ_g^{FP}` (uniform-weight) | "(D) the genus expansion $F_g = \kappa(\cA)\cdot\lambda_g^{\mathrm{FP}}$ (uniform-weight; corrections $\delta F_g^{\mathrm{cross}}$ at $g \geq 2$)" (L758-761) | (D continues — not extracted in lines 27–50) | — | **Consistent (uniform-weight tag present per AP32)** |
| **Theorem H**: chiral Hochschild cohomology in degrees `{0,1,2}`, polynomial Hilbert series | "(H) chiral Hochschild cohomology in degrees {0,1,2} with polynomial Hilbert series" (L762-763) | (H continues — not extracted) | — | **Consistent** |
| Shadow obstruction tower G/L/C/M classification | "The shadow obstruction tower classifies chiral algebras into depth classes G/L/C/M (Heisenberg, affine Kac-Moody, βγ, Virasoro/W_N)" (L764-768) | (not in opener table) | (auto-indexed) | **Consistent** |
| Chiral quantum group equivalence (vertex R + chiral A_∞ + chiral coproduct on B^ord) | "The chiral quantum group equivalence identifies three structures on $B^{\mathrm{ord}}(\cA)$..." (L769-772) | (not in opener table) | — | **Lives in E_1 wing inside Part II + Part VI frontier; Annals-included** |
| Five examples (Heis G, sl_2 L, βγ C, Vir M, Yangian) | L774-779 | (not in opener table) | — | **Consistent** |
| Higher Deligne: derived chiral center is E_3 for E_∞-chiral A | L784-789 | (not in opener table) | — | **Lives in en_koszul_duality.tex; Annals-included** |
| E_3-deformation space = ℏ H^3(g)[[ℏ]]; CFG perturbative E_3 identification "conjectural beyond formal disk" | L792-798 | (not in opener table) | — | **Conjectural per AP153/AP154; honestly framed in abstract** |
| Seven faces of r(z) | (no abstract claim) | (no entry) | — | **Quarantined to archive Part V** |
| theorem_index Part bucketing | — | — | "Frame / Part I: Theory / Part II: Examples / Part III: Connections" (L36-43) | **STALE 3-PART STRUCTURE** |

### 6.1 Confirmed prior-wave finding: theorem_index Part labels stale

Wave 6 reported: *"theorem_index Part labels stale (3-part vs main.tex's 6-part)."* **Confirmed at theorem_index.tex L38–41**:

```
Part I: Theory & 1125
Part II: Examples & 713
Part III: Connections & 405
```

These are not the actual Parts. They are **directory buckets** (`chapters/theory/`, `chapters/examples/`, `chapters/connections/`) misleadingly labeled "Part I/II/III". The real `main.tex` Parts are I=Bar Complex (chapters from `chapters/theory/`), II=Characteristic Datum (mostly `chapters/theory/`), III=Standard Landscape (mostly `chapters/examples/`), IV=Physics Bridges (mostly `chapters/connections/`), V=Seven Faces (a subset of `chapters/connections/`), VI=Frontier (the rest of `chapters/connections/`). So:

- The 1125 "Part I: Theory" hits are **mostly** Parts I and II content, with some Part VI frontier bleed.
- The 713 "Part II: Examples" hits are **mostly** Part III plus some E_1-wing items in Part II.
- The 405 "Part III: Connections" hits are spread across **Parts IV, V, and VI**.

Auto-generation script (the index says "auto-generated from `chapters/**/*.tex`", date 2026-04-13) groups by directory rather than by `\part{}` declaration. **Recommend** rewriting the part-bucketing logic to walk `main.tex` from each `\part{...}` declaration to the next, recording which chapter files are included between, and bucketing theorem labels by that map. ~30 lines of Python, but produces a much more useful index.

### 6.2 No CY-A_3 references in Vol I main matter

`grep` for `CY-A|CY_A|CY-A_3|inf-cat|infinity-categor` across `main.tex`, `preface.tex`, `introduction.tex`, `guide_to_main_results.tex` returns **zero hits**. Vol I does **not** depend on or claim CY-A_3 status — the latter is a Vol III result. The Wave 6 introduction_survey finding ("CY-A_3 status overclaim cascade in programme_summary") refers to `standalone/programme_summary*.tex`, **not** to `main.tex`. Confirmed: `main.tex` is clean of CY-A_3 status confusion.

### 6.3 Part V cross-reference under Annals quarantine

`\label{part:seven-faces}` is defined only at L1512, inside the `\ifannalsedition\else ... \fi` block opened at L1510. Therefore in **Annals build**, this label is undefined. But it is **referenced** in archive-mode (and via the `\ifannalsedition\else`-skipped) opener at L1548 inside Part VI's body (which IS Annals-included).

To make this concrete: L1548 in Part VI opener reads `Parts~\ref{part:bar-complex}--\ref{part:seven-faces}`. In Annals build, `\ref{part:seven-faces}` resolves to `??`. **This is a genuine Annals-build undefined-reference.** (The Annals PDF currently shows `??` between em-dashes in the Part VI opener.) §10 lists the fix.

### 6.4 Bare-`\kappa` audit (Vol I context)

AP113 forbids bare `\kappa` in **Vol III**. Vol I has no such embargo because Vol I has a single `\kappa` (the modular characteristic). Verified: `main.tex` uses `\kappa(\cA)`, `\kappa(V_k(\fg))`, `\kappa(\cA^!)`, etc. — always paired with an algebra argument. **AP113 not applicable to Vol I, no violation.**

### 6.5 Volume-cross-reference pattern

`main.tex` cites "Vol II" twice (L1170, L1571) and "Vol III" once (L1571), both in comments. In live prose: master_concordance.tex (and several Annals-archive files) carry the cross-volume bridges. **No problematic cross-volume citation in main.tex itself.** Phantom labels for Vol II results (L1896–1923) are present and correctly tagged.

---

## §7. Steelman: both sides

### 7.1 Steelman of the current 6-part structure

(a) **The Overture is structurally separate from Part I** because it is *example-first* (the Heisenberg atom shown end-to-end before the theory). Numbering it as Part 0 would weaken the "example, then theory" pedagogy. The current `\part*{Overture}` (unnumbered) keeps the Chriss-Ginzburg posture intact.

(b) **The Annals quarantine of Parts V and VI** is editorial: a public Annals of Mathematics Studies edition cannot include 600+ pages of frontier conjectures. The split is intentional and the phantom-label machinery makes it work. The cascade bugs in §3 / §6.3 are implementation gaps, not design flaws.

(c) **The "E_1 wing inside Part II" decision** (lines 1136–1147) reflects the mathematical reality that the ordered/E_1 formulation is a **parallel** to the symmetric/E_∞ formulation, not a sequel. Putting it inside Part II preserves the bar/cobar/genus/Koszul/shadow fivefold theme. Spinning it out as Part II.5 or Part III would create a numbering bump that propagates to every cross-reference.

(d) **The theorem_index stale 3-part bucketing** is a directory-based heuristic that survived Part restructuring. Easy to fix without disrupting anything else.

(e) **Front-matter date "August 2025"** is the **submission date**, not the audit date. Some journals expect this to remain stable. Not a bug.

### 7.2 Steelman of the upgrade paths

(a) The seven-face cascade in the abstract (§2.2) **does** misadvertise the Annals edition. A reader who picks up the Annals edition reads "the chiral quantum group equivalence identifies three structures..." and finds the supporting chapters absent. This is reputationally costly.

(b) The `\ref{part:seven-faces}` undefined under Annals (§6.3) is a **rendering bug**, visible to every Annals reader who reaches the Part VI opener. It produces a literal `??` in the PDF.

(c) The theorem_index's stale bucketing (§6.1) misleads a reviewer who uses the index to gauge proof distribution across the manuscript's structure.

(d) Three reading paths (algebraist / physicist / number theorist), per Vol III, would substantially reduce the entry barrier for a 1100+ page volume. The audience-targeted preface chapters in `chapters/frame/preface.tex` already provide the raw material.

---

## §8. Three strongest possible upgrade paths

### 8.1 Upgrade path A: Edition-aware abstract + Part V repair

**Cost**: ~30 minutes. Three edits, all in `main.tex`:

(i) Wrap the chiral-quantum-group paragraph (L769–772) and the higher Deligne paragraph (L784–798) of the abstract in `\ifannalsedition...\else...\fi`. In Annals edition, replace with one-sentence forwarding: "The chiral quantum group equivalence and the higher Deligne identification are surveyed in the Annals companion; their full proofs and the seven-face identification appear in the archive edition."

(ii) Move `\label{part:seven-faces}` outside the `\ifannalsedition\else` guard. Add a phantom Part V label that exists in **both** editions (placed at L1509, before the `\else` branch opens) — `\phantomsection\label{part:seven-faces-summary}` for Annals, with `\label{part:seven-faces}` resolving to either the real Part V (archive) or the phantom (Annals).

(iii) Update the Part VI opener (L1548) to use the always-defined label.

**Outcome**: Annals build no longer renders `??`; the abstract no longer over-promises.

### 8.2 Upgrade path B: Three reading paths + scope-aware reading guide

**Cost**: ~2 hours. One new file `chapters/frame/reading_paths.tex` (~150 lines), one `\input` in `main.tex` immediately after `\include{chapters/frame/preface}`. Three tables:

```
ALGEBRAIST PATH
  Introduction §1-3 → Part I (full) → Part II ch. on Koszul pair
  structure → en_koszul_duality.tex → Yangians → Drinfeld-Kohno bridge
  → Higher Deligne in Part VI.

PHYSICIST PATH
  Overture (Heisenberg atom) → Part III examples → Part IV: bv_brst,
  feynman_diagrams, feynman_connection → Part V: seven faces →
  Part VI: frontier_modular_holography_platonic.

NUMBER THEORIST PATH
  Introduction → Part I §kappa → Part III: lattice_foundations,
  moonshine, level1_bridge → Part IV: arithmetic_shadows →
  Part V: collision residue → Part VI: outlook.
```

The Vol III precedent shows this approach works for ~600 pp manuscripts; Vol I at 1100+ pp benefits more strongly.

**Outcome**: lowers entry barrier for an Annals-of-Mathematics-Studies reader by ~3-5x.

### 8.3 Upgrade path C: Promote a single structural climax theorem to the front

**Cost**: ~30 minutes. The unification "the bar differential is simultaneously the Drinfeld-Kohno braid relation, the Verlinde recursion (genus 0), the Borcherds product (genus 1), and the BV master equation (all genera)" lives scattered across (a) Part IV bv_brst.tex, (b) Part V genus1_seven_faces.tex, (c) Part VI thqg_open_closed_realization.tex, (d) Vol II spectral-braiding-core.tex.

Promote a **Climax Theorem** stated as the last equation of the abstract (after the existing `\Einf` / Higher Deligne paragraph), naming it explicitly:

```
\textbf{Climax (Drinfeld-Kohno + Verlinde + Borcherds = bar differential).}
For any E_∞-chiral algebra A on a smooth projective curve X, the bar
differential of B^Σ_X(A) restricts on each genus-g moduli stratum to:
  - genus 0: the Drinfeld-Kohno braid relation on conformal blocks;
  - genus 1: the Verlinde fusion ring recursion on Hom(C_n, T^2);
  - genus g≥1: the Borcherds product expansion on Hom(C_n, M_g);
all four equivalent statements reduce to Arnold's three-term identity.
```

This is not a new claim — every component is proved within the existing Parts I-IV. The promotion is **rhetorical**: it gives the reader a single sentence to take away. Vol III's "Five load-bearing open problems" section in CLAUDE.md is the model.

**Outcome**: positions Vol I as the algebraic-geometric foundation that **unifies four classical structures** (braid relations, fusion, Borcherds, BV) under a single bar differential.

---

## §9. First-principles protocol on the four findings

### 9.1 Theorem index 3-part bucketing (stale)

**Wrong claim**: Part I/II/III in the theorem_index are the manuscript Parts.
**Ghost theorem**: There **is** a 3-bucket structure that's correct — namely, the **directory** structure (`theory/`, `examples/`, `connections/`). The bucketing is correctly computed; it is mislabeled.
**Correct relationship**: directory structure ≠ part structure. The 3 directories cut **across** the 6 parts; bucketing by directory is a coarser equivalence. The wrong label inherits from the era when the manuscript *was* organized as Part I = Theory, Part II = Examples, Part III = Connections — a structure that survives in `chapters/`'s top-level directories but no longer in `main.tex`.
**Type**: temporal (status changed; old status persists) + label/content mismatch.
**Healing**: rename buckets to "Theory chapters / Example chapters / Connection chapters" (honest), OR rebuild the script to walk `main.tex` from `\part{}` to `\part{}` and bucket by actual part membership (best).

### 9.2 Annals abstract scope inflation

**Wrong claim**: The Annals abstract advertises five theorems plus seven-face plus chiral-QG.
**Ghost theorem**: All these results ARE proved/conjectured in **the archive edition**. The abstract is correct for the archive; it is over-claiming for Annals.
**Correct relationship**: Edition-conditional results require edition-conditional advertisement.
**Type**: scope error (edition mismatch).
**Healing**: edition-conditional `\ifannalsedition` wrapping of the affected paragraphs (§8.1).

### 9.3 `\ref{part:seven-faces}` undefined in Annals

**Wrong claim**: The label `part:seven-faces` is universally available.
**Ghost theorem**: There IS always a Part-V-like idea ("the centerpiece collision-residue identification") — even in Annals, where the full identification is forwarded to the archive edition, **a phantom label representing the forwarding** is the correct mechanism.
**Correct relationship**: A label that is referenced from Annals-included chapters MUST be defined unconditionally (either as a real label in Annals-included content or as a `\phantomsection` outside the `\ifannalsedition` guard).
**Type**: object/structure (the Part exists in archive only, but its **forwarding marker** must exist in both editions).
**Healing**: `\phantomsection\label{part:seven-faces}` placed outside the `\ifannalsedition\else` block at L1509-1510, with a comment noting the real Part V follows in archive only.

### 9.4 Two-block macro definitions (lines 470–525 + lines 595–720)

**Wrong claim**: The duplication is a redundancy bug.
**Ghost theorem**: The duplication HAS a real reason — the L595–720 block is gated by `\begin{document}` and is reached even when chapter `.tex` files have been written assuming `\providecommand`-style availability. The L470–525 block runs in the preamble (where `\newcommand` is permissible) and the L595–720 block runs in `\begin{document}` where some imported chapter fragments may try to redefine.
**Correct relationship**: There are TWO distinct macro lifecycles — preamble (where `\newcommand` is the strong assertion) and post-`\begin{document}` (where `\providecommand` is the safe fallback). Both blocks have legitimate roles.
**Type**: lifecycle/scope (each block addresses a different macro lifetime).
**Healing**: comment header clarifying the two lifecycles. No code change needed.

---

## §10. Punch list

Concrete healing actions, ordered by cost-to-impact ratio (lowest cost, highest impact first). All recommendations; none implemented in this audit.

### Priority 1 (do this session)

1. **Move `\label{part:seven-faces}` outside the `\ifannalsedition\else` guard**, or add a `\phantomsection\label{part:seven-faces}` immediately before the `\ifannalsedition\else` at L1509. Eliminates the `??` rendering in the Part VI opener of the Annals PDF.
2. **Fix theorem_index Part bucketing**: either (a) rename "Part I/II/III" buckets to "Theory chapters / Example chapters / Connection chapters", or (b) rewrite the bucketing logic to walk `main.tex` `\part{}` declarations. (a) is a 3-line edit; (b) is ~30 lines of Python.
3. **Edition-aware abstract**: wrap the chiral-quantum-group and higher-Deligne paragraphs (L769–798) of the abstract in `\ifannalsedition\else`. In Annals, replace with one-sentence forwarding.

### Priority 2 (do this week)

4. **Add `make archive` Makefile target**: invokes `pdflatex` with `\def\archivebuild{1}` so archive-build regressions are caught. Also `make both: fast archive` for side-by-side review.
5. **Add `make audit-inputs` target**: bash script that walks `main.tex` for every `\input{...}` / `\include{...}` and verifies the file exists. Catches deletion-induced compile failures before they hit `make`.
6. **Add `make audit-phantoms` target**: Python script that scrapes Annals-included `.tex` files for the labels declared in L1616–1924, reporting orphans (defined-but-unreferenced) and shadows (defined here AND in an Annals-included real label, which causes warnings).
7. **Add `make audit-scope` target**: reads the abstract, extracts `Theorem X` / `(X)` claims, checks each is supported by an Annals-included chapter. Catches §2.2-style cascades.
8. **Comment header on the two-block macro design** (L470 and L595): one paragraph explaining preamble vs `\begin{document}` lifecycles. Saves the next maintainer ~30 minutes of head-scratching.
9. **Update front-page date to "April 2026"** (or "Revised April 2026", preserving "Submitted August 2025"). The 9-month staleness misrepresents the manuscript's currency.

### Priority 3 (do this month)

10. **Install three reading paths** (algebraist / physicist / number theorist) per Vol III, in a new `chapters/frame/reading_paths.tex` `\input`-ed after the preface. ~150 lines.
11. **Promote a Climax Theorem** to the abstract (Drinfeld-Kohno + Verlinde + Borcherds = bar differential, all four equivalent to Arnold). One paragraph; positions Vol I as the unification of four classical structures. (§8.3)
12. **Sub-part marker for the E_1 wing** (lines 1136–1213). Either restore the Part declaration with a name like "The E_1 Wing" (between Part II and Part III, breaking numbering) or add a `\section*{The E_1 Wing}` heading inside Part II to give the wing a TOC entry.
13. **Cross-volume macro sync check**: extract the `\providecommand{\foo}{...}` block from `main.tex` (L470–525, L595–720), Vol II's `main.tex`, and Vol III's `main.tex`; diff. Any macro defined differently across volumes is a latent V2-AP39 violation. ~50 lines of script.

---

## Cache write-back candidates

The following patterns appear at least twice across waves and merit promotion to `~/chiral-bar-cobar/CLAUDE.md` (Vol I) and/or `appendices/first_principles_cache.md`:

### Candidate 1 — Edition-conditional scope cascade

**Pattern**: Annals/Archive edition switch with `\ifannalsedition` quarantining major content (Parts V and/or VI), but front-matter (abstract, openers) written for the archive edition without edition guards. Phantom labels suppress the `??` for cross-references but the **content** described by abstract/opener prose remains absent in the Annals reader's PDF.

**Where seen**: §2.2 (abstract claims chiral-QG / Higher Deligne while their support is Annals-quarantined); §3 Part IV (opener cross-refs `ch:v1-bv-brst`, which is Annals-quarantined); §6.3 (`\ref{part:seven-faces}` resolves to `??` in Annals build).

**Mechanism**: edition switch is a powerful tool but creates an asymmetric obligation — every claim made in **shared** content (abstract, openers, TOC) must be **independently true in both editions** OR be `\ifannalsedition`-conditioned itself. This is V2-AP32 (standalone artifact leak) inverted: instead of standalone artifacts leaking into included content, **archive-only content leaks into shared front matter** through unguarded prose.

**Proposed AP** (Vol I AP-V1-XXX placeholder; the next available number): "**Edition-conditional scope cascade.** When `\ifannalsedition` quarantines a Part or chapter, every reference to that Part's content from shared (always-included) front matter — abstract, Part openers in earlier parts, TOC, keyword list — must either be wrapped in `\ifannalsedition\else` itself OR have a phantom-label placeholder defined unconditionally. Counter: after any `\ifannalsedition\else` chapter quarantine, grep shared front matter for references to the quarantined content and add edition guards."

### Candidate 2 — Directory-based bucketing surviving structural restructure

**Pattern**: An auto-generated index/registry/script buckets entries by **directory** path (`chapters/theory/`, `chapters/examples/`, `chapters/connections/`) and labels the buckets "Part I/II/III" — accurate for the era when the directory layout matched the part structure, **stale** after a `\part{}` restructuring.

**Where seen**: §6.1 (`theorem_index.tex` L38–41 still uses 3-part directory buckets despite main.tex being 6-part). Also Vol II's chapter migration left similar directory/part mismatches (V2-AP38 phantom-label retirement schedule is the same family).

**Mechanism**: directory structure is **persistent** (renames are heavyweight); part structure is **fluid** (new parts get spun out, merged, renumbered). A script bucketing by directory will be silently wrong after every restructuring.

**Proposed AP** (Vol I): "**Directory-based bucketing trap.** Auto-generated indices and registries that bucket by directory name should NEVER be labeled with Part numbers, because Parts are restructured but directories are not. Counter: bucket by `\part{}` membership (walk `main.tex` from `\part{...}` to `\part{...}` and record chapter membership), or label buckets with the directory name itself (`Theory chapters / Example chapters / Connection chapters`)."

### Candidate 3 — Two-block macro lifecycle design (positive pattern, NOT an AP)

**Pattern**: A macro file with **two** `\providecommand` blocks — one in preamble (L470–525), one inside `\begin{document}` (L595–720) — defining many of the same symbols. Initial appearance: redundancy bug. Reality: distinct macro lifecycles.

**Where seen**: §4.1 (Vol I `main.tex` L470 and L595 blocks).

**Mechanism**: chapter `.tex` fragments imported from various sources may try to redefine macros; the post-`\begin{document}` `\providecommand` block survives those redefinitions (silent if already defined). The preamble block is the **strong** declaration; the post-`\begin{document}` block is the **fallback** for chapter-internal `\providecommand`-style assumptions.

This is a **healing pattern**, not an AP. Document it inline in the preamble (Priority 2 item 8 above) so the next maintainer doesn't "deduplicate" them.

---

End of wave 11 report.
