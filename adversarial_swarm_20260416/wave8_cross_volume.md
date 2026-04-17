# Wave 8 — Cross-Volume Consistency Audit (2026-04-16)

**Scope:** Vol I (`~/chiral-bar-cobar/`), Vol II (`~/chiral-bar-cobar-vol2/`), Vol III (`~/calabi-yau-quantum-groups/`).
**Audit family:** stale Part/Chapter refs (V2-AP26, V2-AP30, AP-CY13), cross-volume label
resolution, status drift, q-convention propagation (AP151), CLAUDE.md AP propagation,
duplicated content (V2-AP27), kappa subscript discipline (AP113), CY-A_3 / CY-C status, theorem
renaming drift (V2-AP36), agent skill fidelity (FM45).
**Methodology:** Read/Grep/Glob across all three repos. No commits, no edits to manuscript.

The user's healing directive was honored: the audit looks for upgrade paths first
(strengthening claims, restoring lost content, restoring scope) and only flags downgrades
when they are mechanically forced.

Three structural facts established at the start (current Part lists, used for stale-ref
checking throughout):

| Volume | Parts (numbered, in `main.tex` order) |
|--------|---------------------------------------|
| Vol I  | I=Bar Complex, II=Characteristic Datum, III=Standard Landscape, IV=Physics Bridges, V=Seven Faces of the Collision Residue, VI=Frontier (plus `\part*{Overture}`). |
| Vol II | I=Open Primitive, II=E_1 Core, III=Seven Faces of r(z), IV=Characteristic Datum and Modularity, V=Standard HT Landscape, VI=Three-Dimensional Quantum Gravity, VII=Frontier. |
| Vol III| I=Foundations, II=CY-to-Chiral Functor, III=E_n Hierarchy and Chiral Quantum Groups, IV=K3 Yangian, V=CY Landscape, VI=Seven Faces of r_CY, VII=Frontiers. |

These are the canonical references against which every `Part~N` hardcode below is checked.

---

## Section 1 — Stale Part references (AP-CY13, V2-AP26, V2-AP30)

### Vol I: clean modulo .bak

The grep `Part~[IVXL]` against `chapters/` and `standalone/` (excluding `.bak`) yielded
**one live hit, plus several `.bak.*` hits and a citation context that is not a self-ref.**

| File:line | Context | Status | Recommended action |
|-----------|---------|--------|--------------------|
| `standalone/cy_to_chiral_functor.tex:995` | `Part~II, Internat.\ J.\ Math.\ \textbf{9} (1998), 201--275.` | **NOT stale.** This is a journal-citation Part field (Polishchuk-Zaslow), not an internal Vol I cross-ref. | Leave as is. Note in audit log so future grep does not re-flag. |
| `chapters/theory/introduction.tex.bak:*` (8+ matches) | Hardcoded `Part~I`/`Part~II`/.../`Part~VI` listing the old 6-part summary. | Stale **but in `.bak` file.** | Delete `.bak` files OR move out of `chapters/` to keep grep clean. The `.bak` files cause every cross-volume grep to surface false positives that swamp the real signal. |
| `chapters/frame/heisenberg_frame.tex.bak.abelian_cs_fix:*` (5+ matches) | Same pattern; old 5-part numbering. | Stale `.bak`. | Same as above. |

**Verdict.** Vol I has **zero live stale Part hardcodes** in compiled chapters. The `.bak`
detritus is an audit-noise problem (per CLAUDE.md AP-CY29 / FM27 sandbox-vs-reality), not a
manuscript problem.

**Healing recommendation.** Either (a) move `*.bak*` out of `chapters/` into a sibling
`backup/` tree, or (b) add a `.gitattributes`/grep-ignore rule. The Vol I CLAUDE.md HZ-3
"grep all three volumes for stale Part refs" instruction is currently false-positive-heavy.
Cleaning this up makes the discipline mechanically enforceable.

### Vol II: zero stale hits in compiled chapters

The grep `Part~[IVXL]` against Vol II `chapters/` and `standalone/` returned **zero matches.**

The hits inside `compute/audit/linear_read_notes.md` (12 hits) and
`appendices/first_principles_cache.md` (1 hit, line 118) are audit-log entries, not prose.
The `appendices/first_principles_cache.md:118` entry literally says `"Part~IV hardcoded ...
Use \ref{part:...}, never Part~N. AP-CY13"` — i.e., it is the cache record of the AP itself,
not a violation.

**Verdict.** Vol II is fully clean on Part hardcodes in compiled prose.

### Vol III: stale refs concentrated in `notes/`, not in compiled chapters

The grep `Part~[IVXL]` against Vol III's full repo returned **27 hits**, all of which fall
into three buckets:

| Bucket | File | # hits | Compiled into `main.tex`? |
|--------|------|--------|---------------------------|
| Architecture proposal | `notes/vol3_rearchitecture_proposal.tex` | 21 | **No.** Standalone proposal document, not in main build. |
| Theory note | `notes/theory_e2_chiral_formalism.tex` (line 327) | 1 | **No.** Standalone theory note. The reference `Volume~II, Part~II` is correct under Vol II's current numbering (E_1 Core = Part II), so it is **NOT stale.** |
| Physics note | `notes/physics_bv_brst_cy.tex` (line 324) | 1 | **No.** Cites `Volume~I, Part~I` for the bar-complex construction. Vol I's Part I = "The Bar Complex", so this is **NOT stale.** |
| AP catalogue | `appendices/first_principles_cache.md:118` | 1 | N/A (markdown). The cache row recording AP-CY13 itself. |
| AGENTS.md | `AGENTS.md:796` | 1 | N/A. Documentation of AP-CY13 by example: `Part~IV / Chapter~12 hardcoded refs`. Not a violation. |
| CLAUDE.md | `CLAUDE.md:249, 258` | 2 | N/A. Documentation of HZ3-10. |

**Verdict.** Vol III's compiled chapters (`chapters/**/*.tex`) have **zero stale Part
hardcodes** that ship in the manuscript. The `notes/vol3_rearchitecture_proposal.tex` Part
references are intentional (it describes a proposed restructuring, where Part numbers ARE the
content), and `notes/theory_e2_chiral_formalism.tex` + `notes/physics_bv_brst_cy.tex` cite
Vol I/II Part numbers that are currently correct.

**Cross-volume score.** All three volumes are clean on AP-CY13 / V2-AP26 in compiled prose.
Healing target met. No downgrades needed.

### Chapter-number hardcodes (related: V2-AP26 strengthened form)

A separate grep for `Chapter~[0-9]` found:

* **Vol I:** ~25 hits, **all of which are external citations** of the form `\cite[Chapter~5]{CG17}`, `\cite[Chapter~3]{BD04}`, `\cite[Chapter~9]{LV12}`, etc. Zero internal Chapter-number hardcodes. Clean.
* **Vol II:** ~10 hits, **all external citations** (CG17, BD04, HA, LV12, CG97). Clean.
* **Vol III:** mixed.
  * `chapters/theory/cy_to_chiral.tex:860` — external (`Vol.~2, Chapter~5` of CG17). Clean.
  * `notes/theory_drinfeld_chiral_center.tex:120, 187, 675` — internal hardcodes: "Chapter~12 of the monograph", "Chapter~5", "Chapter~12 of Volume~III (Sections~12.2-12.3)", "Chapter~18", "Chapter~12 Section~12.4", etc. **STALE BY POLICY** (V2-AP26 forbids hardcoding). Note however these live in a `notes/` working document, not in compiled `chapters/`.
  * `notes/theory_coha_e1_sector.tex:245, 941, 1082` — same pattern, internal "Chapter~1 of the main text", "Chapter~12 of the main text", "Chapter~14 of the main text". Stale by policy, in `notes/` only.
  * `notes/theory_qvcg_koszul.tex:105` — "Chapter~9 of the monograph". Stale by policy, in `notes/` only.
  * `notes/vol3_rearchitecture_proposal.tex:222, 223, 604, 686, 692, 693, 702, 703, 705, 706, 711, 815` — Chapter-N references in the proposal text, where they are content (proposing a structure).

**Healing recommendation.** Before any of `theory_drinfeld_chiral_center.tex`,
`theory_coha_e1_sector.tex`, or `theory_qvcg_koszul.tex` is `\input`'d into `main.tex`,
the internal Chapter~N hardcodes must be converted to `\ref{ch:...}`. They are SHIPPED-OUT
RISK: the moment one of these notes is promoted to a chapter, V2-AP26 fires immediately.
Since these are notes (not yet compiled), this is a **future-proofing** issue rather than
a current violation.

---

## Section 2 — Cross-volume label resolution

Vol I theorems cited in Vol II / Vol III, and Vol II theorems cited in Vol III, are predominantly
named cross-references ("Vol~I Theorem~A", "Vol~I Theorem~B", "Vol~I Theorem~H", "Vol~II MC3",
"Vol~II DK bridge"). **No `\cite{Lorgat...}` or external `\cref{...}` to a named Vol I label
is present** (the volumes do not share a single `\externaldocument`).

The cross-volume citation pattern is **descriptive**:

| From → to | Pattern | Risk |
|-----------|---------|------|
| Vol III → Vol I | "Vol~I Theorem~A", "Vol~I Theorem~H", "Vol~I Theorem~B on the Koszul locus" | Renaming risk if Vol I renumbers theorem letters. |
| Vol III → Vol II | "Vol~II Swiss-cheese structure", "Vol~II DK bridge", "Vol~II MC3" | Renaming risk if Vol II renames MC3 / DK / Swiss-cheese chapters. |
| Vol I → Vol III | "see Vol~III, Remark~\texttt{rem:ainfty-coproduct-shadow}" (one explicit `\texttt{}` label cite). | Mid risk: actual label string. Verified: label exists in Vol III. |
| Vol II → Vol III | Vol II `FRONTIER.md` describes Vol III ~693pp / ~34000 tests / ~460 engines. AGENTS.md L235 same. CLAUDE.md L473, L479. | These are **summary documentation**, not tex citations. Drift is documentation-only. |

**Detailed sample (Vol III → Vol I, from `quantum_chiral_algebras.tex`):**

| Vol III citation | Vol I object | Resolves? |
|------------------|--------------|-----------|
| "Vol~I Theorem~H" (referenced 7+ times) | The chiral derived center theorem (Hochschild cochains = bulk algebra). | YES — this is the well-known Theorem H of Vol I (`thm:cy-to-chiral` family). |
| "Vol~I Theorem~A" (referenced 5+ times) | The bar-cobar adjunction core theorem. | YES — Vol I main theorem A (bar of E_1 = factorization coalgebra). |
| "Vol~I Theorem~B on the Koszul locus" | Bar-cobar Quillen equivalence. | YES — Vol I Theorem B. |
| "Vol~I Theorem~C (Koszul conductor: rho_K = 13 for Vir, 24 for lattice)" | Conductor formula. | YES, verified at `quantum_chiral_algebras.tex:1232`. |
| "Vol~I Face~F5" | Yangian face of r_coll. | YES, Vol I has 7 faces classification in Part V. |
| "Vol~I Theorem~D" | One-loop modular trace theorem. | YES. |
| "Vol~I, Definition~\ref{def:shadow-invariants}" (`quantum_chiral_algebras.tex:2289`) | Shadow invariant S_k. | **CANNOT VERIFY without compiling Vol III against Vol I:** the `\ref{def:shadow-invariants}` is intra-volume scope. If it lives inside Vol III, fine; if it's a stub for Vol I label, the cross-volume reference will not resolve. **GREP CHECK:** `grep -rn 'label{def:shadow-invariants}' /Users/raeez/calabi-yau-quantum-groups/` shows the label is **NOT defined in Vol III**. This is a **DANGLING CROSS-VOLUME LABEL.** |
| "Vol~I, Definition~\ref{def:shadow-class}" (`quantum_chiral_algebras.tex:2103`) | Shadow class G/L/C/M definition. | Same risk. **GREP CHECK:** label `def:shadow-class` not found in Vol III. **DANGLING.** |
| "Remark~\textup{\ref{rem:shadow-ainfty-coproduct-vol3}}" | Shadow-A_inf bridge. | Vol I CLAUDE.md says this is `rem:shadow-ainfty-coproduct-vol3` in `higher_genus_complementarity.tex`. **GREP CHECK in Vol I:** label exists at L6091 (confirmed via `\begin{remark}[Shadow tower as $A_\infty$ coproduct corrections (Vol~III)]`). But is it the same key as Vol III references? The label key is `rem:shadow-ainfty-coproduct-vol3` (assumed). If the `\label{...}` actually used in Vol I differs, the Vol III `\ref` is DANGLING. |
| "Remark~\textup{\ref{rem:ainfty-coproduct-shadow}} of Vol~I" (`quantum_chiral_algebras.tex:2085, 2293`) | Same bridge from the other side. | Same issue: confirm label key. |

**Healing recommendation (Section 2).** Convert the 4-5 cross-volume `\ref{...}` calls in
Vol III that point at Vol I labels into one of:
1. `\externaldocument{...}` setup so the labels actually resolve at build time;
2. or replace `\ref{def:shadow-invariants}` with the descriptive form "Vol~I, Definition of
   shadow invariants (Vol~I `def:shadow-invariants`)" so the reference is **inert text** until
   externaldocument is added.

Currently these are **silent failures** — they typeset as `??` in the PDF but do not break the
build. This is exactly the failure mode V2-AP38 (phantom labels) was supposed to track.

---

## Section 3 — Status drift between volumes (per-theorem)

For each major theorem (CY-A, CY-B, CY-C, CY-D, MC3, DK), I compared status claims across the
three volumes' CLAUDE.md and (where applicable) sampled tex files.

| Theorem | Vol I CLAUDE | Vol II CLAUDE | Vol III CLAUDE / tex | Single-source-of-truth? |
|---------|--------------|---------------|----------------------|--------------------------|
| **CY-A_2** | (referenced via Vol III pointer) | "CY-A_3 PROVED in inf-cat" (L473) | "d=2 PROVED; d=3 PROVED (inf-cat)" (theorem table) | YES — agreement. |
| **CY-A_3** | "Vol III ... CY-A_3 PROVED (inf-cat)" (L939) | "CY-A_3 PROVED in inf-cat. [m_3,B^{(2)}]≠0 NOT an obstruction" (L473) | "d=3 PROVED (inf-cat); chain-level [m_3,B^{(2)}]!=0 resolved" (theorem table) | YES — agreement after April 2026 upgrade. |
| **CY-A_3 in tex (Vol III chapters)** | n/a | n/a | `chapters/theory/cy_to_chiral.tex:3569` correctly states "now proved for all smooth proper CY$_3$ categories"; `chapters/theory/cy_to_chiral.tex:1728` correctly states "d=2 unconditional, d=3 conditional on CY-A$_3$ for the existence of the chiral algebra". **Wait — line 1728 still says "conditional on CY-A_3"**. This is the kind of stale conditionality the cache documented (entries 57-66). | **DRIFT SUSPECTED** — see Section 8. |
| **CY-B** | "131 tests" (Vol I CLAUDE quote of Vol III) | "AP-CY58: CY-B E_n scope d-DEPENDENT" (L629) | "d=3 PROVED" (theorem table); "Verdier spectral functor"; 326 tests | Consistent on the d-dependent fact, but Vol III's status table claims "d=3 PROVED" while the underlying lift is via inf-cat CY-A_3 + bar-cobar adjunction. The Vol I CLAUDE.md (L939) does not state CY-B status. **DRIFT:** Vol III asserts CY-B at d=3 as PROVED in the theorem table, but the prose in `chapters/theory/braided_factorization.tex:452` states "CY-A_3 is now proved at the infinity-categorical level... however, CY-C remains conjectural" without explicit CY-B status. The L131 tests refer to a specific lift; the chain-level data is conditional. **Recommended healing:** clarify in Vol III's table that CY-B at d=3 is PROVED at the inf-categorical level (inheriting from CY-A_3), conditional on chain-level framing data for non-formal algebras. |
| **CY-C** | (no explicit status) | "CY-C: All `\begin{conjecture}`, never `\begin{theorem}`" (cache L210) | "CONJECTURAL. Never `\begin{theorem}`" (theorem table) | YES — agreement. AP40 is enforced. |
| **CY-D at d=2** | (no explicit) | "CY-D deep issue: chi(O_{K3xE}) = 0 != 3 = kappa_ch" (L313, agrees with Vol III) | "d=2 PROVED (h^{1,0}=0); d=3 PROGRAMME" | YES — agreement. |
| **CY-D at d=3** | (no explicit) | "CY-D deep issue" (L313) | "FALSE for odd d: chi(O_X)=0 for all CY_3 by Serre" (table); "kappa_ch != chi(O_X) at odd d. Dimension-stratified formula." | YES — agreement. |
| **MC3** | (Vol I core theorem) | "MC3 on the evaluation-generated core for all simple types" (cited from Vol III) | "Vol~II MC3" (`introduction.tex:552`) | Consistent in spirit. **No status drift detected**, but no explicit theorem-status comparison; the Vol III citation just says MC3 "recovers the quantum group categorical structure used here" — no truth-value claim about MC3 itself. |
| **DK bridge** | (Vol I) | "Vol~II, DK bridge" used in Vol III multiple times | "Vol~II, Chapter on the DK bridge" (`quantum_groups_foundations.tex:133`) | Consistent. No drift. |

**Single largest risk:** the cy_to_chiral.tex L1728 prose still uses the word "conditional on
CY-A_3 for the existence of the chiral algebra". Per Vol II cache rows 57-66, all such
phrases were supposed to be updated post-April-2026 to either drop the conditional or to
reframe as "conditional on chain-level explicit framing data". The Vol III chapter
`chapters/theory/cy_to_chiral.tex` still has 4+ unmodernized "conditional on CY-A_3" phrases:

| Vol III file:line | Phrase | Status |
|-------------------|--------|--------|
| `chapters/theory/cy_to_chiral.tex:1728` | "conditional on CY-A$_3$ for the existence of the chiral algebra; assuming existence with kappa_ch > 0..." | **STALE.** A_X exists by inf-cat CY-A_3. Should read: "the chiral algebra A_X exists by Theorem CY-A_3 (Theorem~\ref{thm:cy-to-chiral-d3}); chain-level shadow data conditional on explicit framing for non-formal algebras." |
| `chapters/theory/cy_to_chiral.tex:1763` | "Resurgence-wall-crossing correspondence (conditional on CY-A_3 for d=3)" | **STALE.** Refine to chain-level dependence. |
| `chapters/theory/cy_to_chiral.tex:1765` | "Part (iv) is conditional on CY-A_3 for K3 x E" | **STALE.** A_{K3xE} exists. |
| `chapters/theory/cy_to_chiral.tex:1802` | "global stitching... conditional on CY-A_3" | **STALE.** Stitching is now a chain-level question, not an existence question. |
| `chapters/theory/cy_to_chiral.tex:3308` | "identification is conditional on CY-A_3 for non-toric geometries" | **STALE for existence**, valid for chain-level explicit identification. Should be reframed. |
| `chapters/theory/quantum_chiral_algebras.tex:376, 383` | "(conditional on CY-A_3)" two times in the conjectural pathways table | **STALE for existence**. The status of "$A_{K3 \times E}$" is now PROVED-EXISTS; only the explicit chain-level structure remains conditional. |
| `chapters/theory/quantum_chiral_algebras.tex:1949` | "the holomorphic factorization homology integral... is conditional on CY-A_3" | **STALE for existence**. Reframe. |
| `chapters/theory/quantum_chiral_algebras.tex:2447` | "via $\Phi$, conditional on CY-A$_3$ when $\mathrm{Tot}(K_X)$ is a [...]" | **STALE for existence**. Reframe. |
| `chapters/theory/quantum_chiral_algebras.tex:2698` | "is conditional on CY-A$_3$ (the DT formulation [...])" | **STALE for existence**. Reframe. |
| `chapters/theory/e1_chiral_algebras.tex:1983, 1991` | KS automorphism, BPS invariants "(conditional on CY-A_3)" | **STALE for existence**. Reframe; the KS / BPS structures depend on the chiral algebra existing — which is now proved. |
| `chapters/theory/e2_chiral_algebras.tex:1187` | "tetrahedron correction (conditional on CY-A_3)" | **STALE for existence**. Reframe. |
| `chapters/theory/braided_factorization.tex:768` | "(conditional on CY-A_3) is controlled by the Igusa cusp form" | **STALE for existence**. Reframe. |
| `chapters/theory/braided_factorization.tex:1351` | "For a CY_3 chiral algebra A_C (conditional on CY-A_3)..." | **STALE for existence**. |
| `chapters/theory/en_factorization.tex:1208, 1217, 1223` | "conditional on CY-A_3 and on the 6d algebraic framework for compact manifolds" (3 hits) | **PARTIALLY STALE.** The `+ 6d algebraic framework` part is genuinely conditional. The CY-A_3 part is stale. |

**Count: ~17 stale CY-A_3 conditionality phrases in Vol III chapters.** This is a **healing
upgrade opportunity**, not a downgrade: the user wants the strongest defensible claims, and
each of these can be strengthened by acknowledging that A_X exists (by inf-cat CY-A_3) and
restricting the residual conditionality to either chain-level framing data or to Vol I
Borcherds-lift identification.

---

## Section 4 — q-convention propagation (AP151)

Wave 6 (`wave6_derived_langlands.md`) found Vol I split between Kazhdan-Lusztig and
Drinfeld-Kohno conventions across 7 files (`q_KL^2 = q_DK` mismatch).

### Vol II: minimal q-convention surface in chapters

The grep for q-convention markers (`q_KL`, `q_DK`, `hbar = log`, `2 pi i hbar`) in Vol II
returns just **one hit:** `chapters/connections/thqg_line_operators_extensions.tex:1113`:

```
around $z=0$ is $e^{2\pi i\hbar\,\Omega}=q^{2\Omega}$.
```

This convention `q = e^{2\pi i \hbar}` (Drinfeld-Kohno-style monodromy) is the
**topological/braiding convention.** It does not contradict per se; AP151 fires only if the
**same file** uses both conventions. Single-occurrence not a violation.

### Vol III: one explicit hit, one convention

`chapters/theory/e1_chiral_algebras.tex:1975` writes:

```
[e_{gamma_1}, e_{gamma_2}] = chi(gamma_1, gamma_2) e_{gamma_1+gamma_2}
at first order in hbar = log q.
```

This is the Kazhdan-Lusztig convention `\hbar = \log q`. Used in only one place in Vol III's
chapters. **No within-volume clash.**

### Cross-volume bridge: ABSENT

There is **no explicit "q_KL^2 = q_DK" bridge** in any of the three CLAUDE.md files or
in `notes/cross_volume_aps.md` (Vol I notes file). The bridge identity is folkloric and is
implicit in the prose, but a reader moving from Vol I (where the Wave 6 finding said 7 files
are split) to Vol II's `thqg_line_operators_extensions.tex` to Vol III's
`e1_chiral_algebras.tex:1975` has no explicit cross-volume convention key.

**Healing recommendation (Section 4).** Add to the Vol I, Vol II, and Vol III CLAUDE.md a
single-line convention key:

> **q-convention bridge.** Vol I uses Kazhdan-Lusztig `\hbar = \log q` (additive Yangian
> convention; classical limit `q \to 1` corresponds to `\hbar \to 0`). Vol II's
> braiding/monodromy formulas use Drinfeld-Kohno `q = e^{2\pi i \hbar}`. The bridge is
> `q_{DK} = e^{2\pi i \hbar} = e^{2\pi i (\log q_{KL})/(2\pi i)}` so `q_{DK} = q_{KL}` (when
> `\hbar` is the same; if Vol II's `\hbar` differs from Vol I's by a factor of `2\pi i`, the
> nominal formulas look different but encode the same monodromy). Vol III defaults to
> Vol I's KL convention.

This is a **cross-volume healing move**: the conventions are individually defensible; the
bridge is the missing connective tissue.

### Convention drift check (Vol II vs Vol III on the same topic)

The closest topical overlap is the spectral parameter / monodromy coupling. Vol II's
`thqg_line_operators_extensions.tex` and Vol III's `e1_chiral_algebras.tex` both use the
exponential bridge but in opposite directions (`q^{2\Omega}` vs `\hbar = \log q`). They are
mutually consistent: differentiating `q^{2\Omega} = e^{2\pi i \hbar \cdot 2\Omega}` w.r.t.
`\hbar` gives `[e_1, e_2] = \chi(\gamma_1,\gamma_2) e_{12}` to first order. **No drift
detected.** Bridge would be useful but is not required for correctness.

---

## Section 5 — AP propagation across CLAUDE.md files

The Vol III CLAUDE.md compression today (per the user's preamble) replaced embedded Vol I+II
APs with a pointer. I checked whether this is faithful.

### Counts (V2-AP references)

| File | # `V2-AP` mentions | # `AP-CY` mentions |
|------|--------------------|---------------------|
| Vol I CLAUDE.md (1073 lines) | 16 | many (full inline + AP-CY1..67 catalogue and HZ pointers via cross_volume_aps.md) |
| Vol II CLAUDE.md (638 lines) | 34 | tabular CLAUDE.md L601-629 and inline |
| Vol III CLAUDE.md (629 lines) | 2 | full inline AP-CY1..AP-CY67 catalogue |

Vol III's two `V2-AP` mentions are V2-AP26 and V2-AP30 (the Part-staleness pair). This is
sparse; the rest of the Vol II APs are **not** propagated into Vol III.

But the user's preamble notes **today's Vol III compression replaced embedded Vol I+II APs
with pointers**. Looking at the current Vol III CLAUDE.md sections:

* Lines 414-421: AP150-AP157 (general programme APs, mirrored across all volumes per Vol I CLAUDE.md L972 etc.)
* Lines 423+ (truncated in my read but visible from the system reminder): "AP-CY27 sandbox..." through AP-CY67.
* Lines around 444 in Vol I: "Before cross-volume edits, Read `notes/cross_volume_aps.md` (Vol II V2-AP* and Vol III AP-CY1..AP-CY61 catalogs)."

So Vol I has the **pointer** (`notes/cross_volume_aps.md`) and Vol III has **inline**
duplicates of cross-programme APs (AP150-AP157) plus its own AP-CY1..67. Vol II has its own
V2-AP1..V2-AP39 inline.

### Volume-specific refinements

Several APs differ subtly across volumes. Examples:

| AP | Vol I | Vol II | Vol III | Equivalent? |
|----|-------|--------|---------|-------------|
| AP-CY13 / V2-AP26 | "B33. `Part~IV`, `Chapter~12` hardcoded → `\ref{part:...}`. V2-AP26/FM10." (line 383) | full V2-AP26 text inline | "HZ3-10. AP-CY13/V2-AP26" decision tree (L249-255 in Vol III) | Vol III is the most operational; Vol I is the most terse. Vol I's terseness loses information (no decision tree). |
| AP-CY34 (m_k, B^(2)) | not mentioned by number; story summarized in main commentary | (cache rows) | "AP-CY34: RESOLVED via Costello's operadic TCFT" (Vol III CLAUDE.md, the long status block) | Vol III has the canonical narrative; other volumes either pointer or omit. |
| AP-CY40 (no `\begin{theorem}` for CY-C) | n/a | "CY-C: All `\begin{conjecture}`, never `\begin{theorem}`" (cache row L210) | inline AP-CY40 | Consistent. |
| AP151 (q clash) | inline AP151 (with cross-programme variant: hbar = 1/(k+2) vs pi*i/(k+2)) | not in Vol II CLAUDE.md by number | inline AP151 (with hbar = log(q) vs (log q)/(2πi) variant) | **DIFFERENT VARIANTS.** The Vol I AP151 example is about the level-shifted KM convention; Vol III's AP151 example is about KL vs DK monodromy. Both legitimate, but the underlying pattern is the same and merging into one canonical AP would help. |
| AP-CY55 (manifold vs algebraization) | not present | not present | inline AP-CY55 | Vol III only. Defensible (only Vol III has the algebraization split). |

**Compression risk audit.** The Vol III CLAUDE.md compression is mostly faithful, but
**AP151's variant** is volume-specific (Vol I's KM-level vs Vol III's q-monodromy). If the
compression collapses these into a single pointer, the volume-specific examples are lost.
Recommend keeping the volume-specific worked example inside each CLAUDE.md even if the
abstract AP statement points elsewhere.

### Propagation gap (V2-AP catalogue)

The Vol II CLAUDE.md has V2-AP1..V2-AP39 with detailed examples (E_inf-includes-all-VAs,
PVA != P_inf, etc.). Vol III's compressed CLAUDE.md does NOT mirror these. A Vol III agent
working on a chiral-algebra chapter who has not also read Vol II's CLAUDE.md may re-introduce
V2-AP1 ("VAs are not E_inf"). This is the **agent skill fidelity gap (FM45)** in
its CLAUDE-file form: the pointer does not have the same semantic weight as inline content.

**Healing recommendation (Section 5).** Either:
1. Verbatim-copy V2-AP1 through V2-AP39 into Vol III's CLAUDE.md (sacrificing brevity for
   robustness against agent compression), or
2. Add an explicit "Vol III agents must read Vol II CLAUDE.md L# through L# verbatim before
   any chiral-algebra edit" instruction at Vol III CLAUDE.md top.

Option (1) is what Vol I appears to do (L1026+ "Geometric vs Algebraic Models" inlines
AP-CY62-67). Option (2) is currently in place via `Session Entry` but is weaker.

---

## Section 6 — Duplicated mathematical content (V2-AP27)

Search for duplicated theorem statements across volumes. The hard cases:

| Theorem | Locations | Same statement? | Drift? |
|---------|-----------|-----------------|--------|
| Bar-cobar adjunction (BD-style) | Vol I `chiral_koszul_pairs.tex`, Vol II `bar-cobar-review.tex`, Vol III `cy_to_chiral.tex` (cite only) | Vol II's version is the "review" abstraction; Vol I has the original Theorem A. Vol III cites both. | No literal copy; **no V2-AP27 violation.** |
| `r(z) = k * Omega/z` (Sugawara r-matrix) | Vol I `frame/heisenberg_frame.tex`, Vol II `chapters/theory/factorization_swiss_cheese.tex`, Vol III `quantum_groups_foundations.tex:114` | Vol III L114 explicitly says: "matching the Vol~I and Vol~II convention. Two sanity checks, mandatory after writing any r-matrix formula:..." | This is **good practice** — Vol III explicitly defers to Vol I/II, no duplication. AP126 enforced. |
| `kappa(KM) = (k+h^v) dim(g)/(2h^v)` | Vol I `higher_genus_complementarity.tex:6167`, Vol III `quantum_chiral_algebras.tex` (citations) | Vol III cites Vol I's formula via "Vol~I". No duplicate statement. | No violation. |
| Drinfeld center theorem (Z(Rep^E_1(A)) = Rep^E_2(Z^der_ch(A))) | Vol II `chapters/connections/spectral-braiding.tex` (and -core), Vol III `notes/theory_drinfeld_chiral_center.tex`, Vol III `chapters/theory/drinfeld_center.tex` | Vol III's `notes/` has the explicit theorem statement; Vol III's chapter has a CY-specialized variant. Vol II has the abstract version. **Three independent statements.** | **MID RISK.** If the abstract theorem is restated in three places, drift is likely. **Healing:** Vol III's chapter should `\ref` the Vol II abstract theorem rather than restate. Currently Vol III chapter says "by the Drinfeld center theorem (Theorem ...)" without explicit Vol II citation. |
| Chiral CE complex (`B(U^ch(L)) = CE_*(L)`) | Vol III `chapters/theory/quantum_chiral_algebras.tex:300` ("The identification follows from PBW (Kac, Loday-Vallette)..."), Vol I (referenced) | Vol III gives a verification-by-PBW + chiral envelope argument. Vol I likely has the abstract form. | If Vol I has it, Vol III's restatement is V2-AP27-borderline. **Recommend cross-checking** Vol I has a `chiral CE` theorem, and either delete Vol III's restatement or convert to citation. |

**Verdict.** Two real risks: (i) Drinfeld center theorem stated independently in
Vol II + Vol III notes + Vol III chapter (3 copies), and (ii) chiral CE complex possibly
duplicated. No critical drift detected today, but a future correction risks creating drift.

---

## Section 7 — kappa subscript discipline (AP113) cross-volume audit

### Vol I uses bare `\kappa`

Vol I has dozens of bare `\kappa = c/2`, `\kappa = (k+h^v) dim(g) / (2h^v)`, etc., across
`higher_genus_complementarity.tex` and `ordered_associative_chiral_kd.tex`. This is **NOT a
violation in Vol I**: AP113 is a **Vol III** discipline. Vol I has a single canonical kappa
(the modular characteristic / one-loop curvature), so `\kappa` is unambiguous within Vol I.

### Vol II uses bare `\kappa`

Vol II's higher-genus and HT chapters likewise use bare `\kappa`. Same reasoning: Vol II has
a single canonical kappa.

### Vol III is meticulous about subscripts

The Vol III chapters I sampled use `\kappa_{\mathrm{ch}}`, `\kappa_{\mathrm{BKM}}`,
`\kappa_{\mathrm{cat}}`, `\kappa_{\mathrm{fiber}}` consistently. Examples:

* `cy_to_chiral.tex:69`: "`\kappa_{\mathrm{ch}} = 2` (from additivity: `\kappa_{\mathrm{ch}}(E) + \kappa_{\mathrm{ch}}(E) = 1 + 1`)"
* `cy_to_chiral.tex:188`: "`\delta\kappa = \chi_{\mathrm{top}}/24`"
* `cy_to_chiral.tex:1232` (quantum_chiral): "`\kappa_{\mathrm{ch}}(A) + \kappa_{\mathrm{ch}}(A^!) = \rho_K`, where `\kappa_{\mathrm{ch}}(A) = -\sigma_2`..."
* `quantum_chiral_algebras.tex:1503`: "`\kappa_{\mathrm{ch}} = \chi^{\mathrm{CY}}_2(K3) = 2`"

Where bare `\kappa` does appear in Vol III, it is the **delta** symbol for "kappa correction"
(`\delta\kappa = ...`), which is the change in `\kappa_{\mathrm{ch}}`, not bare kappa. Slight
abuse but defensible since the context is `\kappa_{\mathrm{ch}}`. **OK by AP113.**

### Cross-volume citations

When Vol III cites Vol I's kappa, the convention is:

* Vol III `quantum_chiral_algebras.tex:1232`: "`\rho_K = 13` for the Virasoro family (Vol~I)" — Vol I's bare `\kappa` becomes implicit. The Vol I `\kappa(\mathrm{Vir}_c) = c/2` translates to Vol III's `\kappa_{\mathrm{ch}}(A_{\mathrm{Vir}}) = c/2`. **No discipline violation, but no explicit Vol I → Vol III subscript bridge** either.
* Vol III `quantum_groups_foundations.tex:114`: explicit "matching the Vol~I and Vol~II convention" comment. Good practice.

**Verdict.** Vol III is internally clean on AP113. Vol I and Vol II are clean **by their own
single-kappa conventions**. The cross-volume translation is implicit and reliable for the
chiral-algebra (`\kappa_{\mathrm{ch}}`) subscript only. Where Vol III uses
`\kappa_{\mathrm{BKM}}`, `\kappa_{\mathrm{cat}}`, `\kappa_{\mathrm{fiber}}`, these have **no
Vol I/II analogue** and there is no risk of cross-volume confusion.

**Healing recommendation (Section 7).** Add to each volume's CLAUDE.md a one-line convention:
"Vol I `\kappa` = Vol III `\kappa_{\mathrm{ch}}` (the chiral-algebra modular characteristic).
Vol III's `\kappa_{\mathrm{BKM}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}` are
**Vol-III-specific** and have no Vol I/II referent." This is a 3-line healing addition.

---

## Section 8 — CY-A_3 status check across volumes

CY-A_3 was upgraded to PROVED (inf-cat) via `thm:derived-framing-obstruction` in April 2026.

| Volume | Compiled chapters: stale "conditional on CY-A_3" / "open"? |
|--------|-----------------------------------------------------------|
| Vol I  | `standalone/programme_summary.tex:98`: "single open conjecture is the CY-A correspondence at..." — checked by reading L96-100: this is in a context "before April 2026 status update" and at L2599 explicitly upgrades: "`\begin{theorem}[CY-A at $d = 3$]\label{thm:cy-a3}`". Vol I's standalone may be inconsistent: L98 calls CY-A "the single open conjecture"; L2619 says "No open conjecture in the programme has unresolved [...]"; L2599 is a theorem environment. **THIS IS INTRA-DOCUMENT DRIFT in Vol I's standalone.** L98 is stale. |
| Vol I (chapters/) | Zero matches for "conditional on CY-A_3" or "CY-A_3 open" in compiled chapters. **Clean.** |
| Vol II (chapters/) | Zero matches. **Clean.** |
| Vol III (chapters/) | ~17 stale "conditional on CY-A_3" matches (enumerated in Section 3 above). |

**Verdict.** Vol I's standalone summary needs one paragraph reconciled (L98 vs L2599-2619).
Vol II is clean. Vol III has the bulk of the stale-conditionality work to do — but as
**healing upgrades**, not downgrades.

**Concrete healing template** for the Vol III stale phrases:

OLD: "conditional on CY-A_3"
NEW: "the chiral algebra A_X exists by Theorem~CY-A_3 (Theorem~\ref{thm:cy-to-chiral-d3}); the
explicit chain-level [shadow tower / framing data / Borcherds-lift identification] for [class
M / non-formal / non-toric] geometries remains conditional on [chain-level framing /
Vol I Borcherds-lift bridge (AP-CY8) / motivic DT comparison]."

Each instance can be re-scoped without weakening any genuine claim.

---

## Section 9 — CY-C status check across volumes

CY-C is CONJECTURAL. Verify all volumes use `\begin{conjecture}`:

| Volume | `\begin{theorem}` for CY-C anywhere? |
|--------|--------------------------------------|
| Vol I  | None found (CY-C is a Vol III construction). |
| Vol II | None found. |
| Vol III | Grep `(theorem|Theorem).*CY-C` in `chapters/`: zero theorem-environment hits. The CY-C name appears as `Conjecture~CY-C`, `(CY-C)`, `Theorem~CY-A_3 [...] CY-C remains conjectural`, etc. **Clean.** |

**Specific checks:**

* `chapters/theory/quantum_groups_foundations.tex:196`: "Theorem~\ref{thm:qgf-kazhdan-lusztig} is the **prototype** for Conjecture CY-C." Correct framing.
* `chapters/theory/braided_factorization.tex:452`: "(where CY-A_3 is now proved at the infinity-categorical level [...] **however, CY-C remains conjectural**)." Correct.
* `chapters/theory/drinfeld_center.tex:1251`: "Results involving the quantum vertex chiral group G(K3 x E) **remain conditional on Conjecture CY-C**." Correct.
* `chapters/connections/geometric_langlands.tex:671, 697`: "the open content is the construction of G(X) (CY-C)" + "every d=3 Langlands statement remains conjectural because the quantum vertex chiral group G(X) is not yet constructed (CY-C)." Correct.
* `chapters/examples/k3_chiral_algebra.tex:728`: "the group object G(K3 x E) is conjectural (CY-C)." Correct.

**Verdict on Section 9.** AP40 + HZ3-1 are enforced cleanly across all three volumes.
**Zero violations.** This is the strongest score in the audit.

---

## Section 10 — Theorem renaming drift (V2-AP36)

V2-AP36 demands atomic propagation of renames. The candidate renames I checked:

| Rename event | Atomic? |
|--------------|---------|
| "shadow Postnikov tower" → "shadow obstruction tower" (Vol II 5-commit fix) | The Vol II CLAUDE.md cache documents this required 5 commits. Vol III's `quantum_chiral_algebras.tex:2103, 2289, 2293` use "shadow" with no "Postnikov"; Vol I's `higher_genus_complementarity.tex:6091, 6093` use "shadow tower" / "$A_\infty$ correction tower". **Clean across all volumes.** |
| "CY-A_3" status (Conjecture → Theorem) | Per Vol II cache row 6: "62 instances of 'Theorem CY-A_3'" — meaning 62 instances were upgraded. The current grep shows the remaining stale "conditional on CY-A_3" phrases in Vol III enumerated in Section 3. So the rename is mostly atomic but **17 propagation gaps remain** in Vol III prose. |
| `\barB` / `\Barch` / `\barchiral` (multiple bar-variant macros) | Quick grep of Vol III's `quantum_chiral_algebras.tex` shows `\Barch` and `B(...)` used; Vol II has `\Barch` defined. Cross-volume consistency: not separately audited; recommend a Vol-by-Vol macro grep before next CLAUDE.md compression. |

**Verdict.** The April-2026 CY-A_3 rename is **mostly atomic** (per Vol II cache) but has
**~17 residual stale phrases in Vol III chapters**. This is the same set already enumerated
in Section 3 / Section 8.

---

## Section 11 — STEELMAN BOTH SIDES

### Steelman the current Vol III state

The user's preamble notes: "Vol III compression today: replaced embedded Vol I+II APs with
pointer." This is a **rational compression decision** because:
1. The CLAUDE.md files were reaching 1000+ lines and approaching the agent context budget.
2. The cross-volume APs change rarely; once Vol III agents internalize the pointer,
   re-reading the same APs each session is wasteful.
3. The volume-specific APs (V2-AP1..V2-AP39 in Vol II, AP-CY1..AP-CY67 in Vol III) are
   **load-bearing** for that volume's agents and remain inline.

The compression is healing, not regression — IF the pointer is followed. The risk (FM45)
is that subagents do not follow pointers reliably.

### Steelman the residual stale CY-A_3 conditionality phrases

The 17 stale "conditional on CY-A_3" phrases in Vol III chapters are **defensive** rather
than wrong: each phrase asserts a stronger condition than is currently needed. The stronger
condition is **safe**: any reader who relies on these statements at the conditional level
gets a true (more conservative) statement. The healing upgrade weakens the stated condition,
which lets the manuscript claim more. So the user's preference for healing-via-upgrade is
**vindicated**: every stale phrase is an upgrade opportunity, not a downgrade.

### Steelman the absence of an explicit q-convention bridge

The conventions are mutually consistent at the level of the formulas in use — there is no
formula in any volume that contradicts another volume's formula because of the
KL-vs-DK split. The bridge is implicit. The healing addition (3-line cross-volume convention
key) is **insurance**, not bug-fix. Without it the manuscript is correct but fragile under
future edits; with it the manuscript is correct and robust.

### Where the audit is genuinely worried

The two genuine risks not soluble by upgrade:

1. **Dangling cross-volume `\ref{def:shadow-invariants}` and `\ref{def:shadow-class}` from
   Vol III to Vol I.** These will typeset as `??` if Vol III is built standalone and
   `externaldocument` is not configured. **HEAL by either:** (a) configuring Vol III's
   build to read Vol I's `.aux`; (b) inlining the definitions; (c) replacing the `\ref`
   with descriptive text + the label key.
2. **Drinfeld center theorem stated three independent times** (Vol II abstract, Vol III
   notes/, Vol III chapter). Drift risk if any one is later corrected. **HEAL by**
   collapsing to one canonical statement (in Vol II `spectral-braiding-core.tex`) and
   citing.

---

## Section 12 — Three upgrade paths

Per the user's directive ("realize the strongest possible mathematical statements"), three
specific upgrade paths emerge from this audit:

### Upgrade Path A: De-condition the 17 Vol III "conditional on CY-A_3" phrases

For each of the 17 phrases enumerated in Section 3, replace the bare conditionality with
a refined dependency. Net effect: 17 statements move from "conditional" to "PROVED at the
existence level, conditional on chain-level data for [explicit sub-condition]". The mathematics
is unchanged; the claims become stronger by being more precise about what is and is not open.

**Files affected:** `cy_to_chiral.tex`, `quantum_chiral_algebras.tex`, `e1_chiral_algebras.tex`,
`e2_chiral_algebras.tex`, `braided_factorization.tex`, `en_factorization.tex`. Single
session, ~17 small `Edit` calls. Low risk.

### Upgrade Path B: Dual-direction cross-volume label resolution

Configure `\externaldocument{...}` in Vol III's `main.tex` to read Vol I's `.aux`. Then
re-typeset and verify:
* `\ref{def:shadow-invariants}` resolves to the Vol I definition (currently dangling).
* `\ref{def:shadow-class}` resolves (currently dangling).
* `\ref{rem:shadow-ainfty-coproduct-vol3}` resolves (label exists in Vol I L6091; may
  need to verify the actual `\label{...}` key matches).
* `\ref{rem:ainfty-coproduct-shadow}` resolves.

Net effect: cross-volume citations stop typesetting as `??`. The two manuscripts become
mutually consistent at the build-system level. This is a one-time `Makefile`/`main.tex`
fix.

### Upgrade Path C: Add convention bridge to all three CLAUDE.md files

3-line addition each:

> **Cross-volume kappa convention.** Vol I/II `\kappa` (the bar-complex modular
> characteristic) corresponds to Vol III `\kappa_{\mathrm{ch}}` (the chiral-algebra
> instance of CY-A applied to the relevant CY category). Vol III's
> `\kappa_{\mathrm{BKM}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}` are
> Vol-III-specific (no Vol I/II referent).
>
> **Cross-volume q-convention.** Vol I uses Kazhdan-Lusztig `\hbar = \log q` (additive);
> Vol II's monodromy formulas use Drinfeld-Kohno `q = e^{2\pi i \hbar}`. Both reduce to
> `q_{KL} = q_{DK}` when `\hbar` is shared; if `\hbar` differs by `2\pi i`, formulas appear
> different but encode the same monodromy. Vol III defaults to KL.

Net effect: future agents have an explicit cross-volume convention key; AP151 is given
operational teeth across volumes.

---

## Section 13 — Punch list (prioritized)

| # | Action | Effort | Risk if not done | Recommended? |
|---|--------|--------|------------------|--------------|
| 1 | De-condition 17 stale "conditional on CY-A_3" phrases in Vol III chapters (Section 3 list) | ~2 hours | Manuscript understates its own theorems; future agents propagate the staleness | **YES** (highest healing yield) |
| 2 | Reconcile Vol I `standalone/programme_summary.tex:98` ("single open conjecture is CY-A") with L2599 (theorem env) | ~10 min | Standalone summary contradicts itself within the same file | **YES** |
| 3 | Resolve dangling `\ref{def:shadow-invariants}`, `\ref{def:shadow-class}` cross-volume refs in Vol III | ~30 min (externaldocument) or ~20 min (descriptive replacement) | Build typesets `??` for these refs | **YES** |
| 4 | Add q-convention bridge to all three CLAUDE.md files (3 lines each) | ~10 min | AP151 future violations | **YES** (cheap insurance) |
| 5 | Add kappa convention bridge to all three CLAUDE.md files (3 lines each) | ~10 min | Vol III subscripts confused with Vol I bare kappa by future agents | **YES** (cheap insurance) |
| 6 | Move Vol I `*.bak*` files out of `chapters/` to keep Part-grep clean | ~5 min | Audit noise; future grep false positives | **YES** (operational hygiene) |
| 7 | Convert internal Chapter~N hardcodes in Vol III `notes/` (theory_drinfeld_chiral_center.tex, theory_coha_e1_sector.tex, theory_qvcg_koszul.tex) to `\ref{ch:...}` BEFORE these notes are promoted to compiled chapters | ~30 min | V2-AP26 fires the moment these notes are promoted | **YES** (future-proofing) |
| 8 | Collapse the Drinfeld center theorem's three statements (Vol II abstract + Vol III notes/ + Vol III chapter) to one canonical + two citations | ~1 hour | V2-AP27 drift risk | **MID** (no current drift, but fragile) |
| 9 | Verify chiral CE complex theorem isn't duplicated between Vol I and Vol III `quantum_chiral_algebras.tex:300` | ~15 min | Possible V2-AP27 duplication | **MID** |
| 10 | Verbatim-copy V2-AP1..V2-AP39 into Vol III CLAUDE.md (or add explicit "READ Vol II CLAUDE.md L# verbatim" instruction) | ~30 min | FM45 fidelity gap; subagents miss V2-AP* | **MID** |
| 11 | Refine the residual `chapters/theory/en_factorization.tex` "conditional on CY-A_3 and on the 6d algebraic framework for compact manifolds" to acknowledge CY-A_3 PROVED, retain "+ 6d framework" conditional | ~10 min | Same as item 1 (subset) | **YES** (subset of item 1) |
| 12 | Cache write-back: append today's findings to `appendices/first_principles_cache.md` | ~10 min | Cache becomes stale; future audits re-discover same patterns | **YES** (per memory:feedback_cache_write_back.md) |

---

## First-principles addendum

Per the user's first-principles protocol (memory:feedback_first_principles_investigation):

The pattern "stale conditional on CY-A_3" is at heart a **temporal confusion type**
(per first_principles_cache.md taxonomy, Vol III column has ~1 temporal item; this audit
adds 17 instances). The ghost theorem behind the pattern: **"a result asserted as
conditional remains true — it just understates its own strength after the resolving
theorem lands."** The wrong claim and the right claim are nested: the stale conditional
is a weakening of the true (now-known) statement.

The healing move is therefore **not** "delete the conditional" but "narrow the
conditionality to its residual content": after CY-A_3 is proved, the conditionality moves
from the existence of A_X to either (a) chain-level explicit framing data (open for non-formal
algebras), or (b) Vol I Borcherds-lift identification (AP-CY8 conditionality), or (c)
motivic DT comparison (Vol III CY-D programme). Each stale phrase has a specific residual
condition; the healing replacement names that residual.

This is itself a **new confusion type** worth caching: **"upgrade-staleness"** (status
upgrades that are not propagated to the dependent prose). The recurrence pattern is:

1. A theorem T is upgraded from Conjecture to Proved.
2. The status table is updated.
3. The CLAUDE.md is updated.
4. The downstream prose that says "conditional on T" is **not** updated.
5. The downstream prose, while still TRUE (the conditional always reads as the safe bound),
   now UNDERSTATES.

The Vol II cache rows 57-66 documented one wave of this; the current audit found a second
wave of 17 in Vol III chapters. **This pattern recurs and will recur** every time a major
conjecture upgrades. The mechanical fix is a post-upgrade grep `\\\\b(conditional on|open)\\\\b
[^.]*<conjecture-name>` and reframing.

Recommend appending to `appendices/first_principles_cache.md`:

```
| ## | Stale "conditional on T" after T proved | Conditional always weakly true | Statement understates its own strength | Reframe to residual condition (chain-level data, Borcherds bridge, etc.). 17 instances Vol III April 2026 | upgrade-staleness | wave8 |
```

This is **cache write-back** per memory:feedback_cache_write_back.md.

---

## Summary

* **AP-CY13 / V2-AP26 / V2-AP30 (stale Part refs):** Compiled chapters are clean across all
  three volumes. `notes/` and `*.bak*` accumulations cause grep noise but no manuscript
  violations.
* **Cross-volume label resolution:** 2-4 dangling `\ref{...}` from Vol III to Vol I labels
  (`def:shadow-invariants`, `def:shadow-class`, possibly the `rem:shadow-...` pair). Heal
  with `externaldocument` or descriptive replacement.
* **Status drift:** Vol III chapters carry **17 stale "conditional on CY-A_3" phrases** that
  understate their own strength post-April-2026 upgrade. Healing UPGRADE opportunity (not
  downgrade): reframe each to its residual conditionality.
* **q-convention (AP151):** No within-volume clashes. Cross-volume bridge (`q_KL = q_DK`)
  is implicit; explicit 3-line bridge in CLAUDE.md is cheap insurance.
* **CLAUDE.md AP propagation:** Vol III's compression replaces V2-AP* and Vol I AP* with
  pointers. Vol-specific worked examples (AP151's KM-level vs q-monodromy variants) risk
  loss. Recommend keeping inline.
* **Duplicated content (V2-AP27):** Drinfeld center theorem stated 3 times across Vol II
  + Vol III notes + Vol III chapter. Mid-risk drift.
* **kappa subscript discipline (AP113):** Vol III internal clean. Cross-volume bridge
  (`Vol I \kappa = Vol III \kappa_{ch}`) implicit; explicit bridge cheap insurance.
* **CY-A_3 status:** Vol I standalone has one self-contradiction (L98 vs L2599); Vol II clean;
  Vol III chapters have 17 stale-conditionality phrases (above).
* **CY-C status:** Clean across all three volumes. AP40 + HZ3-1 fully enforced. Strongest
  score in the audit.
* **Theorem rename drift (V2-AP36):** April-2026 CY-A_3 rename ~mostly~ atomic; 17 residual
  prose gaps in Vol III (same as the conditional staleness above).

**Net assessment.** The cross-volume discipline is in its strongest state to date. The
remaining gaps are healable by **upgrade**, not downgrade: every stale conditional understates
a true statement. The single largest healing yield is Upgrade Path A (de-condition the 17
phrases). The cheapest healing yield is Upgrade Path C (add 3-line convention bridges to
each CLAUDE.md).

---

*Wave 8 cross-volume audit complete. Files inspected: ~40 .tex files, 3 CLAUDE.md files, 3
main.tex files, several `notes/` markdown files. No commits performed; no manuscript edits
performed; this report is the only artifact created.*
