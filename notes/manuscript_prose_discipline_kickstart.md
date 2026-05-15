# Manuscript prose-discipline audit — kickstart

Self-contained protocol to resume the chapter-prose audit after a
`/clear`. Read this file first; it contains everything needed to
continue without prior conversation context.

---

## What this is

A long-running editorial audit of Vol I chapter prose against the
CLAUDE.md "Writing standard" (Russian-school / Chriss--Ginzburg voice).
The dominant gap to platonic-ideal manuscript realisation is
chapter-internal prose discipline: meta-narration, bookkeeping
vocabulary, symbol-before-definition, definition-without-question,
hedging, AI-slop, bare process titles. Structural architecture, the
five reconstruction theorems, KSDual table, and 666/666 numerical
verification tests are all in place; what remains is editorial.

---

## Where the live state lives

- **Progress log**: `notes/prose_discipline_progress.md` — current
  cursor (chapter + offset), per-fire edit log, deferred items, scan
  notes. **Always read this first** to find where to resume.
- **The CLAUDE.md mandate**: `/Users/raeez/chiral-bar-cobar/CLAUDE.md`
  §"Writing standard: Chriss--Ginzburg north star" defines the prose
  voice.

---

## Iteration protocol

1. Read `notes/prose_discipline_progress.md`; find current chapter
   and offset. If absent, start at
   `chapters/theory/introduction.tex` offset 1.
2. Read 200–400 lines of the current chapter from that offset.
3. Identify CONCRETE violations from the inventory below; do NOT
   skip; do NOT defer.
4. Fix the top 3–5 violations in place via Edit. Each fix is a real
   prose rewrite, not just a label rename.
5. Append a dated section to `notes/prose_discipline_progress.md`:
   chapter, offset advanced past audited region, list of edits with
   line numbers, deferred items with reason.
6. End with a 2–3 sentence summary of what was rewritten.

Budget per iteration: 5–9 minutes; advance the offset by ~300–400
lines per fire so a chapter is fully audited in ~10 fires. Many
chapters need fewer fires once the title pass is done — the body
prose of the theory chapters is largely already in CG voice.

---

## Violation inventory (CLAUDE.md "Writing standard")

A) **Meta-narration**: "we now turn to", "having established", "let
us now", "this brings us to", "it is worth noting", "notably",
"crucially", "remarkably", "furthermore", "moreover", "in the
present work", "we shall see", "it should be emphasized" — DELETE;
replace with direct mathematical statement.

B) **Bookkeeping vocabulary**: "Wave N", "round M", "batch K", "DNA
strand", "AP$n$", "Pattern $n$", "cache entry", "CG-rectify pass",
"HZ-n inscription" — DELETE; this belongs in `notes/`, never in
`chapters/`.

C) **Hedging**: "is closely related to", "may be viewed as", "can be
interpreted as", "is essentially", "is morally", "in some sense",
"roughly", "approximately" — when $X=Y$ is proved, rewrite as the
equality.

D) **Definition-without-question**: every definition needs the
motivating question within 10 lines BEFORE it. If absent, add a 1–2
sentence question paragraph.

E) **Symbol-before-definition**: every symbol on first appearance
must be defined or carry a parenthetical first-principles gloss.

F) **Section-boundary discipline**: at every `\section` boundary,
three sentences of mathematics — what was just established, the
question the next section resolves, the construction that resolves it.

G) **Bare process titles**: section/subsection titles that name
processes ("Constructing the bar complex") not objects ("The bar
complex of an augmented chiral algebra") — rename to
objects/theorems/questions. Likewise drop "Synthesis", "Summary",
"Warm-up", "Master ...", "Precise", "Motivating", "preview",
"revisited" generic-prefix forms.

H) **AI-slop phrasing**: "delve", "dive deep", "embark", "journey",
"tapestry", "robust", "leverage" (verb), "comprehensive", "key
insight", "fundamental insight", "fascinating" — DELETE.

I) **Em-dash overuse, redundant comma chains, three-word phrases
that should be one, smart-quotes in math.**

---

## Discipline (hard rules)

- NO new propositions/remarks/theorems; this is editorial work, not
  propositional decoration.
- NO label renames as a substitute for prose rewrite — when you
  rename a label, also rewrite the surrounding prose.
- TRUST existing mathematical content; modify ONLY the prose.
- NEVER cut content; only rewrite. If a passage looks redundant
  with another chapter, mark for deferred deletion in `notes/`; do
  not delete this iteration.
- NEVER use destructive git: `git checkout`, `restore`, `reset`,
  `stash`, `clean -f`, `branch -D`, force push (CLAUDE.md absolute
  prohibition).
- NEVER add AI attribution (no `Claude`, `Anthropic`,
  `Co-Authored-By`, `Generated with`, 🤖 in commits, code, or
  manuscript).
- Author of any commits: **Raeez Lorgat** only.

---

## Chapter rotation order

```
chapters/theory/introduction.tex →
chapters/theory/algebraic_foundations.tex →
chapters/theory/configuration_spaces.tex →
chapters/theory/bar_construction.tex →
chapters/theory/chiral_koszul_pairs.tex →
chapters/theory/theorem_A_infinity_2.tex →
chapters/theory/chiral_hochschild_koszul.tex →
chapters/theory/hochschild_cohomology.tex →
chapters/theory/chiral_center_theorem.tex →
chapters/theory/higher_genus_foundations.tex →
chapters/theory/higher_genus_complementarity.tex →
chapters/theory/higher_genus_modular_koszul.tex →
chapters/theory/climax_theorem.tex →
chapters/theory/chiral_climax_platonic.tex →
chapters/theory/universal_conductor_K_platonic.tex →
chapters/theory/kappa_conductor.tex →
chapters/connections/master_concordance.tex →
chapters/connections/master_reconstruction.tex →
chapters/examples/landscape_census.tex →
chapters/examples/kac_moody.tex →
chapters/examples/heisenberg_eisenstein.tex →
chapters/examples/beta_gamma.tex →
chapters/examples/free_fields.tex →
chapters/examples/w_algebras.tex →
chapters/frame/programme_overview_platonic.tex →
chapters/frame/preface.tex →
[loop back]
```

---

## Status snapshot (last updated 2026-05-15)

Closed chapters (audited end-to-end):

| Chapter | Lines | Edits | Notes |
|---|---:|---:|---|
| algebraic_foundations.tex | 2916 | 17 | 9 titles + 8 body; "Synthesis" → named content; "Master verification" → "Factorization axiom verification"; AP-126/AP-141 labels removed. |
| configuration_spaces.tex | 6408 | 5 | Body uniformly clean; titles renamed to drop "General setup", "simplest case", "Synthesis". |
| bar_construction.tex | 3393 | 6 | 3 "in this monograph" body rewrites + 3 title rewrites. |
| chiral_koszul_pairs.tex | 8106 | 5 | Body had ZERO standard-CG violations; titles "Warm-up", "Summary", "Synthesis (continued)" → named-object forms. |

Earlier (out-of-rotation) cleanup of `chern_weil_level_shift_platonic.tex`:
6 AP-numbered label renames + 4 title rewrites + 1 body regex-noise
rewrite.

**Next cursor**: `chapters/theory/theorem_A_infinity_2.tex` offset 1.

**Observation**: theory chapters are *much* cleaner than expected.
The dominant violation type is generic section titles (Summary,
Synthesis, Warm-up, Master ...); per-chapter audit usually closes
in 2–4 fires once the title pass is done. The `examples/` and
`connections/` chapters have not yet been touched and may carry more
prose-level violations.

---

## How to resume

### Manual mode (one iteration at a time)

```
Read notes/prose_discipline_progress.md → find cursor →
Read 300 lines of the current chapter from that offset →
Identify 3-5 concrete violations → Edit in place →
Append dated entry to notes/prose_discipline_progress.md →
2-3 sentence summary.
```

### Loop mode (cron, session-only)

If you want the loop to run unattended in the current session,
re-create the cron with the prose-discipline prompt:

```
CronCreate cron="*/7 * * * *" recurring=true
prompt="/loop CHAPTER-PROSE-DISCIPLINE AUDIT — read
notes/manuscript_prose_discipline_kickstart.md for the protocol,
then execute one iteration per fire. Cursor in
notes/prose_discipline_progress.md. Begin now."
```

The earlier cron `29ff8f97` was cancelled by the user 2026-05-14.

### Cloud mode

For a durable schedule that survives session close, invoke
`/schedule` instead of `/loop` and pick the cloud option.

---

## Discoveries worth carrying forward

- "Synthesis" / "Summary" / "Conclusion" generic section titles
  appear across many chapters (~10 instances flagged in
  `algebraic_foundations`, `configuration_spaces`,
  `chiral_koszul_pairs`, `cobar_construction`, `koszul_pair_structure`,
  `computational_methods`, `infinite_fingerprint_classification`,
  `nilpotent_completion`, `chiral_koszul_pairs`). When you hit one,
  rename it to whatever content it actually surveys (look at the
  inscribed Remarks/Theorems inside the section).
- AP-numbered labels (`rem:apN-xxx`, `cor:apN-xxx`, `sec:hz-iv-...`,
  `sec:fp-cache-...`) appear in `chern_weil_level_shift_platonic`,
  `chiral_center_theorem`, `infinite_fingerprint_classification`,
  `topologization_chain_level_platonic`, `mc5_genus0_genus1_wall_platonic`,
  `shadow_tower_quadrichotomy_platonic`, `motivic_shadow_tower`,
  `clutching_uniqueness_platonic`, `genus_2_ddybe_platonic`,
  `concordance`, `bar_cobar_adjunction_inversion`. These violate the
  bookkeeping-vocabulary rule (AP-N is a notes/ artifact). When you
  hit a chapter with these, rename the label to a mathematical name
  and update all internal `\ref{}` calls — verify with `grep -rn`
  that zero orphans remain.
- The early theory chapters (introduction, algebraic_foundations,
  configuration_spaces, bar_construction, chiral_hochschild_koszul,
  higher_genus_foundations) have ZERO instances of the standard CG
  dictionary in body prose. The discipline pays off — assume body
  prose is in voice unless `grep -inE` (case-insensitive) finds
  otherwise; spend the fire budget on titles and AP-labels.
- Legitimate technical usage to NOT flag: "essentially surjective"
  (category theory term), "in this monograph" inside a Convention
  block declaring scope, "for our purposes" inside a definitional
  scope statement. Use judgement.

---

## Honest assessment (what remains beyond this audit)

This audit is necessary but not sufficient. Additional gaps to the
platonic ideal:

1. **Twelve open frontier items in `FRONTIER.md` (F1†–F12)** — none
   resolved by prose work. F1† (chain-level Priddy contraction
   verifying $\mathcal N(\mathsf L) = 2(k+h^\vee)$) and F8 (chart-class
   enumeration per archetype) are the most tractable.
2. **Vertical holographic equivalences** inscribed at levels 0, 2,
   4 only; levels 1, 3, 5 missing.
3. **Master Reconstruction Theorem proof is sketch-level**; M1
   cites 5 sub-theorems without chain-level unification.
4. **Chapter-internal "inevitability"** — every definition arriving
   with its motivating question — is the standard CLAUDE.md sets;
   the audit catches violations but does not by itself raise the
   floor.

The prose audit is dominant work but pure prose; it does not move
the mathematical frontier. After this audit closes, the next
substantial work is one of F1†, F8, F11, or the vertical-equivalence
inscriptions at levels 1, 3, 5.
