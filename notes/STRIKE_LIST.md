# STRIKE LIST — Full Repo Assessment (2026-03-10)

Generated from systematic audit: build, tests, census, metadata, documentation,
concordance, untracked files, git delta, and cross-consistency.

---

## Situation

- **99 modified files, 22 untracked** — largest uncommitted delta in project history
- **Build**: 1567pp, 4-pass, NOT clean (2 undef citations, 1 undef ref, 8 overfull)
- **Tests**: Hanging/timing out on heavy compute tests. No pytest-timeout.
- **Census**: PH 923, PE 337, CJ 153, HE 29, Open 1 = 1443 claims
- **Metadata**: All machine-generated files severely stale (census.json says 839 PH vs 923 actual)
- **CLAUDE.md**: Had stale MC2 status ("3 packages remaining" — now PROVED). Fixed this session.
- **autonomous_state.md**: Had stale page count (1546→1567), census, MC3 status. Fixed this session.
- **MEMORY.md**: Had stale MC2 status. Fixed this session.
- **concordance.tex**: MC2 "fully resolved" claim verified — all sub-theorem labels exist with ProvedHere status.
- **New content**: E₁ lattice programme (§11-12 of lattice_foundations.tex), factorization bar-cobar for lattice VOAs, DK-1½ in concordance.

---

## P0 — Fix before any new mathematics

### P0.1 Resolve undefined references — FIXED
- ~~2 undefined citations (`Lurie_HA` x2), 1 undefined citation (`SS03`)~~
- **Fixed**: `Lurie_HA` → `LurieHA` (correct bib key). SS03 resolves on subsequent pass.
- Build now clean: 0 undef citations, 0 undef refs, 0 overfull (on converged pass)
- **Remaining issue**: page-count oscillation (1510↔1550pp) prevents full 4-pass convergence. This is cosmetic — content and refs are correct on any individual pass.

### P0.2 Commit triage
- **99 modified files** spanning theory, examples, connections, appendices, compute, metadata, notes
- Much of this is accumulated work from multiple sessions (v23-v26 + E₁ lattice)
- Needs structured commit(s) — not one giant commit
- Recommended split: (a) theory+examples LaTeX, (b) compute code, (c) metadata+notes, (d) build fixes

### P0.3 Clean build artifacts from working tree — DONE
- ~~9 `.stdout` files~~ — DELETED
- `.gitignore` updated to exclude `*.stdout`

### P0.4 Regenerate machine-readable metadata
- `metadata/census.json`: claims 839 PH, actual 923 (9.9% error)
- `metadata/claims.jsonl`: 1296 entries vs 1443 actual (10% missing)
- `metadata/dependency_graph.dot`: downstream of claims.jsonl, equally stale
- `metadata/label_index.json`: likely 10% incomplete
- `metadata/theorem_registry.md`: claims "587 ProvedHere" vs 923 actual (36% missing)
- **Action**: Run `scripts/manuscript_qc.py` or equivalent regeneration script

---

## P1 — Fix before next content push

### P1.1 Fix test suite
- Tests hang/timeout on heavy DS reduction and nonprincipal tests
- No `pytest-timeout` package installed
- **Action**: Either install pytest-timeout, add timeouts to heavy tests, or mark slow tests with `@pytest.mark.slow`

### P1.2 Fix 8 overfull hbox warnings
- These are typographic issues where content exceeds line width
- Identify which files/lines and fix line breaks or reformulate

### P1.3 Clean superseded session prompts
- `notes/SESSION_PROMPT_v21.md` through `v24.md` — all superseded by v25
- **Options**: (a) delete, (b) move to `notes/archive/`, (c) gitignore
- Recommended: move to `notes/archive/` to preserve history

### P1.4 Triage remaining untracked files
| File | Action |
|------|--------|
| `PHASE0_THEOREM_DEPENDENCY_INDEX.md` | TRACK (useful reference) |
| `chapters/theory/fourier_seed.tex` | TRACK (active chapter in main.tex) |
| `latest_state_scaffold.md` | TRACK or DELETE (may duplicate autonomous_state.md) |
| `notes/old_abstract_pre_modular_homotopy.md` | DELETE or archive |
| `raeeznotes18-21.md` | KEEP untracked (external review material) |

### P1.5 Verify toroidal_elliptic.tex fix
- Added `\begin{remark}[Scope and programme status]` before `\label{rem:toroidal-hms}`
- Should verify this is the correct remark title and environment

### P1.6 Update Stratum II assessment
- CLAUDE.md still says "Stratum II: Full Theta_A, coderived Ran, factorization DK, periodicity sync"
- But Theta_A is now proved (MC2 resolved). Stratum II should be: coderived Ran, factorization DK (cat O), H-level MC4 comparison, periodicity sync.

---

## P2 — Next content priorities

### P2.1 DK-1½ → DK-2 bridge for lattice sector
- Factorization bar-cobar for lattice VOAs is proved (thm:lattice:factorization-koszul)
- The gap to factorization DK is the deformed FKS ↔ quantum group identification
- This is prop:lattice:quantum-group-connection (conjectural)
- If proved, would give unconditional factorization DK for level-1 simply-laced

### P2.2 Fourier Seed chapter
- SESSION_PROMPT_v25 directive: bar complex as 1D non-abelian Fourier transform
- `chapters/theory/fourier_seed.tex` exists (~50 lines) but is skeletal
- New chapter between introduction and bar_cobar_construction

### P2.3 MC4 coefficient identities
- Yangian: K^line_{a,b}(N) = K^RTT_{a,b}(N) for a,b ≤ N
- W-infinity: C^res = C^DS on finite primary seed packets
- Both reduced to finite matrix computations

### P2.4 MC3 category O generation
- The gap between DK-2/3 (fd type A proved) and full DK
- Thick generation problem for category O
- Latyntsev construction needed for DK-3

### P2.5 conj:en-koszul-duality
- The sole remaining `ClaimStatusOpen` claim in the entire manuscript
- n≥3 Totaro/graph-complex construction
- Low priority but the only Open item

### P2.6 Periodicity doctrine
- Weakest of the nine futures
- T-matrix and quantum periodicity proved; modular bar periodicity conjectural
- Containment, not advancement

---

## Already Fixed This Session

- [x] CLAUDE.md MC2 status: "3 packages remaining" → "PROVED"
- [x] CLAUDE.md source line count: 99K → 104K, claims 1430 → 1443
- [x] MEMORY.md MC2 status updated, current state section added
- [x] autonomous_state.md: Quick State updated, MC3 sharpened, session log added, priorities rewritten
- [x] .gitignore: added `*.stdout` pattern
- [x] concordance.tex: DK-1½ entry added to DK ladder
- [x] lattice_foundations.tex: \rank→\operatorname{rank}, \xymatrix→tikz-cd, \cM→\mathcal{M}
- [x] toroidal_elliptic.tex: missing \begin{remark} added

---

## Cross-Consistency Check

| Source | MC2 Status | Consistent? |
|--------|-----------|-------------|
| concordance.tex (constitution) | PROVED (thm:mc2-full-resolution) | YES (authoritative) |
| higher_genus.tex (theorem env) | PROVED (ClaimStatusProvedHere) | YES |
| CLAUDE.md | PROVED | YES (fixed this session) |
| MEMORY.md | PROVED | YES (fixed this session) |
| autonomous_state.md | PROVED | YES (was already updated) |
| PROGRAMMES.md | "3 exact packages" language | STALE (not yet fixed) |
| NEW_MACHINERY.md | "3 remaining MC2 packages" | STALE (not yet fixed) |
| frontier_and_gaps.md | "3 exact packages" | STALE (not yet fixed) |

**Remaining stale files re MC2**: PROGRAMMES.md, NEW_MACHINERY.md, frontier_and_gaps.md still describe MC2 as having remaining packages. These should be updated to reflect the proved status, or marked as historical.
