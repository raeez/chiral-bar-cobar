# Attack-Heal: ClaimStatus tag discipline audit, Vol I (2026-04-18)

Author: Raeez Lorgat.

Target: discipline audit of `\ClaimStatus*` tags across Vol I chapters,
appendices, and standalones, with targeted verification that the
downgrades/rescopings of the 2026-04-17 / 2026-04-18 waves are
reflected in the manuscript and in `standalone/theorem_index.tex`.
Mission per session brief (AP1721-AP1740 reserved, used sparingly
per AP314).

## Phase 1. Programme-wide tag counts

Raw `grep -c '\\ClaimStatus<tag>'` across
`chapters/**/*.tex`, `appendices/**/*.tex`, `standalone/**/*.tex`,
`chapters/frame/**/*.tex` (Vol I only; no cross-repo scan).

| Tag                       | Occurrences | Files touched |
|---------------------------|-------------|---------------|
| `\ClaimStatusProvedHere`     | 2986        | 155           |
| `\ClaimStatusProvedElsewhere`| 602         | 112           |
| `\ClaimStatusConjectured`    | 407         | 84            |
| `\ClaimStatusConditional`    | 30          | 18            |
| `\ClaimStatusHeuristic`      | 49          | 31            |
| total                     | 4074        | —             |

Observation 1. ProvedHere dominates at a 5:1 ratio over ProvedElsewhere
and a 7:1 ratio over Conjectured. Given the Beilinson-rectified scope
remarks in CLAUDE.md (Theorem A fixed-curve only; Theorem C/T1-T9
restricted; Theorem D clause (iv) Conditional; Theorem B weight-completed
only; MC3 evaluation-generated core only; MC4^0 generic parameters
Conjectural; CY-D stratification Hodge-supertrace only), the raw 2986
count is an upper bound on "programme-accepted proved locally in Vol I"
and many instances trace to per-clause tags in multi-clause theorems,
prose references (`\ClaimStatus*` as a literal token in a remark body
listing status-tag semantics), concordance entries, and status-table
rows — not individually distinct theorem inscriptions.

Observation 2. `\ClaimStatusConditional` is the rarest tag (30
occurrences in 18 files). Given the session's downgrades (Theorem A
modular-family, Theorem C T1/T2 scope, Theorem D clause (iv), Theorem A
UCH gravity chain-level at g>=1), the low Conditional count confirms
the discipline that the programme prefers to downgrade directly to
Conjectured rather than use the intermediate Conditional tag. CLAUDE.md
HZ-11 healing uses Conditional as the stopping point for cross-volume
ProvedHere discipline; the low count indicates Conditional is reserved
for that one specific healing pattern rather than used broadly.

## Phase 2. Recently-healed theorems: verification of tag alignment

| Theorem/prop label                              | Expected (session wave)                      | Manuscript state                                                                                                                                             | Verdict  |
|--------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `conj:n4-mc4-zero-generic-parameters`            | conjecture + Conjectured                     | `standalone/N4_mc4_completion.tex:942` `\begin{conjecture}` + `\label{conj:n4-mc4-zero-generic-parameters}` + `\ClaimStatusConjectured` (line 944). Prior `thm:n4-mc4-zero-unconditional` label retired; zero grep hits for the old label across Vol I. | ALIGNED  |
| `prop:verlinde-from-ordered`                     | proposition + ProvedElsewhere                | `chapters/theory/higher_genus_modular_koszul.tex:33435` `\begin{proposition}` + `\label{prop:verlinde-from-ordered}` + `\ClaimStatusProvedElsewhere` (line 33438). Scope remark `rem:verlinde-from-ordered-scope` follows at :33610. | ALIGNED  |
| `thm:v-natural-e3-topological`                   | theorem + ProvedElsewhere                    | `chapters/examples/chiral_moonshine_unified.tex:383` theorem environment, title line carries `\ClaimStatusProvedElsewhere` inside the optional argument. Cross-chapter consumers in `chiral_moonshine_unified.tex:504,524,905` + `chapters/frame/part_ii_platonic_introduction.tex:812`. | ALIGNED  |
| `prop:theorem-D-factorization-homology-alt`      | proposition + Conditional (clause iii)       | `chapters/theory/higher_genus_foundations.tex:6169` `\begin{proposition}` title "Factorization-homology derivation via PTVV; \ClaimStatusConditional". Clause (iii) carries `\ClaimStatusConjectured`, the overall env is Conditional. Consumers at `chapters/theory/clutching_uniqueness_platonic.tex:619,685` resolve. | ALIGNED  |
| `thm:A-infinity-2` modular-family extension      | fixed-curve ProvedHere; modular Conditional  | `chapters/theory/theorem_A_infinity_2.tex:879-915` `rem:A-infinity-2-modular-family-scope` explicitly records that the Francis–Gaitsgory six-functor base-change and Mok25 log-FM sewing are cited not inscribed; clauses (i)-(iii) ProvedHere; clause (iv) Conditional pattern mirrored in `thm:lagrangian-complementarity-global-upgrade` at `chapters/theory/higher_genus_complementarity.tex:5051`. | ALIGNED  |
| `thm:lagrangian-complementarity-global-upgrade`  | clauses (i)-(iii) ProvedHere; (iv) Conditional | `chapters/theory/higher_genus_complementarity.tex:5051` theorem title "clauses (i)-(iii) \ClaimStatusProvedHere; clause (iv) \ClaimStatusConditional" with per-clause tag in (iv) at :5104. Comment at :5046 records the 2026-04-17 HZ-11 heal. | ALIGNED  |
| `thm:C-PTVV-alternative`                         | mixed per-clause tags                        | `chapters/theory/theorem_C_refinements_platonic.tex:437` theorem with clause (i) ProvedElsewhere, clause (ii) ProvedHere, clause (iii) Conjectured. Chapter opening comment :1-30 honestly records that T1/T2/T4/T6/T9 of the "nine strengthenings" are scope-restricted or retracted. | ALIGNED  |
| `conj:uch-gravity-chain-level` cross-vol ref     | phantomsection stub at `main.tex:2207`; consumer at `chapters/theory/e1_modular_koszul.tex:2776` labels class M g>=1 Conjectured | confirmed `main.tex:2207` + `chapters/frame/part_iv_platonic_introduction.tex:556` + `chapters/theory/e1_modular_koszul.tex:2776`. | ALIGNED  |

All seven recently-healed theorems verified. No stale `ProvedHere` tags
survive on the downgrade targets.

## Phase 3. AP40 multi-tag / env-tag mismatch sweep

Automated scan for (a) a single `\begin{env}...\end{env}` containing
more than one `\ClaimStatus*` tag, (b) a `conjecture` environment
carrying a `ProvedHere` tag, (c) a `theorem|proposition|lemma|corollary`
carrying `Conjectured`.

Raw hits: 21 multi-tag candidates; 1 env/tag mismatch candidate. Manual
triage:

### Multi-tag candidates — legitimate per-clause patterns (NOT AP40 violations)

Per-clause tagging is the intended discipline for multi-clause
theorems whose parts carry different epistemic statuses. The session's
AP149 discipline explicitly supports this pattern (e.g.
`thm:lagrangian-complementarity-global-upgrade` (i)-(iii) ProvedHere +
(iv) Conditional; `thm:C-PTVV-alternative` (i) ProvedElsewhere + (ii)
ProvedHere + (iii) Conjectured).

Verified legitimate per-clause patterns:

- `chapters/theory/higher_genus_complementarity.tex:5051`
  `thm:lagrangian-complementarity-global-upgrade` — ProvedHere x3 +
  Conditional. Title inscribes the split. HEALED 2026-04-17.
- `chapters/theory/theorem_C_refinements_platonic.tex:436`
  `thm:C-PTVV-alternative` — ProvedElsewhere + ProvedHere +
  Conjectured. Title inscribes the mixed status.
- `chapters/frame/part_iv_platonic_introduction.tex:551, 647, 756`
  `thm:part-iv-*` — Part-IV introduction theorems listing multi-proof
  compound claims. Per-clause tags.
- `chapters/connections/arithmetic_shadows.tex:10698`
  `prop:*-conditional` — ProvedHere primary + Conditional caveat tag
  on scope-limited corollary line.
- `chapters/connections/master_concordance.tex:35` — concordance entry
  listing two sibling theorems with different statuses in the same
  table row.
- `chapters/connections/genus1_seven_faces.tex:460` — two-clause
  elliptic-r-matrix theorem (Belavin primary ProvedHere; KZB bridge
  ProvedElsewhere).
- `chapters/examples/heisenberg_eisenstein.tex:214` — multi-clause
  compound theorem with primary ProvedHere + attribution
  ProvedElsewhere + three sub-clauses ProvedHere.
- `chapters/connections/editorial_constitution.tex:1630` — editorial
  table listing five sibling entries with ProvedElsewhere each.
- `chapters/theory/universal_conductor_K_platonic.tex:411`
  `conj:...` + subsequent ProvedHere lemma inside the same extended
  block (scanner false-positive from a single `\begin{conjecture}`
  whose closing `\end{conjecture}` is preceded by an inline `\begin`
  pair inside a displayed proof-sketch — not a true env violation;
  conjecture environment's own `\ClaimStatusConjectured` is at :413,
  the second tag belongs to a nested `\begin{proposition}` inside the
  proof-sketch remark that follows the conjecture at :519). Scanner
  limitation, not a discipline breach.

### Multi-tag candidates — scanner false positives on table rows / concordance prose

- `chapters/connections/concordance.tex:5077` — table row inside a
  concordance listing; both tags are cell contents of a multi-row
  table, not a single-environment ambiguity.
- `chapters/connections/frontier_modular_holography_platonic.tex:1672` — status-table row.
- `chapters/connections/holographic_datum_master.tex:274, 487, 575` — status-table cells.
- `chapters/connections/genus_complete.tex:469` — concordance block
  with five sibling rows.
- `chapters/examples/genus_expansions.tex:370, 385` — two independent
  conjectures in a shared subsection; scanner merged them.
- `chapters/examples/chiral_moonshine_unified.tex:695` — "bridge"
  theorem listing primary ProvedElsewhere attribution alongside
  per-clause ProvedHere; status-table pattern.
- `standalone/seven_faces.tex:1005` — orphan standalone (not `\input`
  into `main.tex`; AP255 phantom-in-chapters) listing three candidate
  equivalence statements. Already flagged in CLAUDE.md as AP255.
- `chapters/theory/higher_genus_foundations.tex:2971` — five
  consecutive per-clause ProvedHere tags on a compound theorem; this
  is the intended pattern for an all-clauses-proved compound theorem.

### Env/tag mismatch — single flagged instance is a comment header, not live code

- `chapters/theory/theorem_C_refinements_platonic.tex:13` flagged as
  `env=conjecture tag=ProvedHere`. Inspection: line 13 is inside the
  chapter-opening `%` comment block (lines 1-30) documenting the
  scope of the 2026-04-16 T1-T9 audit. The token `ProvedHere` appears
  inside a prose description of the tag vocabulary, not as a live
  `\ClaimStatus` command. Scanner false positive.

### Genuine AP40 violations

Zero. No theorem/proposition/lemma environment carries `Conjectured`
as its live status tag; no conjecture environment carries `ProvedHere`
as its live status tag. Per-clause tagging in multi-clause compound
theorems is the accepted discipline and matches the session's AP149 /
HZ-11 healing pattern.

## Phase 4. `standalone/theorem_index.tex` cross-check

The theorem index is a 2449-line auto-collated registry. Spot-check
against the session's healed theorems:

| Label                                              | Index entry   | Index tag        | Notes |
|----------------------------------------------------|---------------|------------------|-------|
| `prop:verlinde-from-ordered`                       | line 986      | `ProvedElsewhere`| ALIGNED with chapter body. |
| `conj:uch-gravity-chain-level` (Vol II cross-ref)  | line 2405     | `Conjectured`    | ALIGNED with Vol II + Vol I phantomsection stub + consumer `chapters/theory/e1_modular_koszul.tex:2776`. |
| `thm:uch-main` (Vol II cross-ref)                  | line 2404     | `ProvedHere`     | Consistent with Vol II chapter body. |
| `thm:theorem-D-factorization-homology-alt` (Vol I chapter `prop:...`) | absent  | —                | **INDEX GAP**: `prop:theorem-D-factorization-homology-alt` not in the index. |
| `thm:v-natural-e3-topological` (Vol I chapter)     | absent        | —                | **INDEX GAP**: Vol I chapter-level entry missing from the index. |
| `conj:n4-mc4-zero-generic-parameters` (standalone) | absent        | —                | **INDEX GAP**: standalone-only inscription; the index is nominally auto-collated from chapter files, and standalones are excluded. This is a discipline question not a violation. |
| `thm:lagrangian-complementarity-global-upgrade`    | absent        | —                | **INDEX GAP**: multi-clause mixed-status theorem not in the index. |
| `thm:C-PTVV-alternative`                           | absent        | —                | **INDEX GAP**: mixed-status theorem not in the index. |

Conclusion: the index covers a large fraction of ordinary chapter
theorems but does NOT currently track (a) multi-clause mixed-status
theorems inscribed in the recently-healed files, (b) propositions
carrying the PTVV-route / alternative-derivation tagging, or (c) the
V-natural Monster E_3 theorem. This is an index-generation gap, not
an individual-theorem tagging violation.

Heal options:

1. Regenerate the index from a fresh sweep, including the missing
   entries. Requires knowing the generator script
   (`scripts/generate_theorem_index.py` or similar — not inspected
   this session).
2. Hand-inscribe the five missing entries below the existing rows.
3. Accept the gap as scope-limited: the index is a convenience
   artifact, and the chapter bodies + CLAUDE.md status table are the
   sources of truth.

Recommended heal: option 3 for this session (defer regeneration to a
future build-artifact commit), with the explicit note that the index
under-reports by approximately five recently-healed entries. A later
`scripts/generate_metadata.py` or equivalent invocation should regenerate
the index to absorb the gap.

## Phase 5. Discipline findings (ap register, minimal per AP314)

### AP1721 (Conditional tag under-utilisation).

The programme-wide `\ClaimStatusConditional` count is 30, of which
roughly one-third trace to the 2026-04-17 HZ-11 cross-volume heal
pattern (`thm:lagrangian-complementarity-global-upgrade` clause (iv)
and downstream consumers). The remaining two-thirds appear in
per-clause compound theorems. The tag's discipline is consistent
but its domain of use is narrow: Conditional is reserved for
cross-volume dependency scoping (HZ-11) and for clauses of compound
theorems whose closure depends on an externally cited lemma. It is
NOT used for in-file scope qualifications; those use Conjectured.

Counter: when downgrading a theorem clause whose proof chain depends
on an in-file retracted mechanism (see AP300, same-file drift), the
correct tag is `Conjectured`, not `Conditional`. Conditional is
reserved for dependency on an external (cross-volume or cross-file)
proved theorem whose local inscription is a citation rather than a
proof body. The 30/4074 ratio (0.74%) suggests the discipline is in
equilibrium.

### AP1722 (Theorem-index regeneration debt).

`standalone/theorem_index.tex` under-reports the Vol I mixed-status
compound theorems inscribed in 2026-04-17 / 2026-04-18 heals. Five
representative gaps identified above. Regeneration is a build-artifact
task; hand-inscription is an AP149 propagation expense (update the
index concurrent with each theorem-status downgrade). Neither
approach is undertaken in this session per mission scope ("report
findings; minimal heals"). The gap is registered as a known
debt for the next build-artifact commit.

Counter: before any `make census` or theorem-index regeneration, grep
the chapter bodies for `\ClaimStatus*` tags and compare against the
index's own tag column; any mismatch should block the regeneration
commit until the underlying theorem has been triaged.

### (No further APs inscribed this session per AP314 throttling.)

## Phase 6. Summary

- Programme-wide tag counts established at 2986/602/407/30/49 across
  Vol I. Conditional is the rarest tag (30), confirming its discipline
  as HZ-11-reserved.
- Every session-downgraded theorem is aligned between its chapter
  body tag and its environment header. Seven out of seven spot-checks
  pass.
- No genuine AP40 multi-tag or env/tag-mismatch violations. All 21
  flagged candidates are legitimate per-clause tagging, concordance /
  status-table rows, or scanner false positives.
- `standalone/theorem_index.tex` under-reports five representative
  recently-healed multi-clause theorems. Index regeneration debt
  logged as AP1722; heal deferred to the next build-artifact pass.
- Two preventative APs registered: AP1721 (Conditional tag
  under-utilisation ⇒ reserved for HZ-11 patterns; not for in-file
  drift, which uses Conjectured), AP1722 (theorem-index regeneration
  debt with grep-against-body gate for the regeneration commit).

Files touched: none (read-only audit + this report).

No AI attribution. No commits created.
