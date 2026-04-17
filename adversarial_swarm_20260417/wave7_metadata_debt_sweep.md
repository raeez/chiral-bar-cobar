# Wave 7 — Metadata-debt sweep (2026-04-17)

Author: Raeez Lorgat.

Mission: heal the six CLAUDE.md / manuscript metadata-debt items
accumulated across Waves 3–7. Every item is a metadata-hygiene
finding (CLAUDE.md advertising mismatched with inscribed manuscript
state) — not a mathematical falsification. The heals are surgical
rewrites and atomic renames, not mathematical retractions.

## Item 1 — Drinfeld-Heis VERIFIED mispromotion

**Source.** CLAUDE.md:626 theorem-status row

> "Drinfeld center Heis | VERIFIED | conj:drinfeld-center-equals-bulk
> for H_k: 5 invariants at 6 levels. Naive dim 1 vs derived dim 3. 72
> tests."

Cross-reference: Vol I preface.tex:4228 inscribes
`conj:v1-drinfeld-center-equals-bulk` as `\begin{conjecture}` (honest
conjecture). Vol I chiral_center_theorem.tex:1967
`prop:derived-center-explicit` is `ClaimStatusProvedHere` and
computes $\ChirHoch^*(\cH_k)$ explicitly as the three-term polynomial
model $1 + t + t^2$, with generators $\{1, \xi_k, \eta\}$ and
$P_{\cH_k}(t) = 1 + t + t^2$. The Drinfeld-double comparison
$Z(U_{\cH_k}) \simeq \cZ^{\mathrm{der}}_{\mathrm{ch}}(\cH_k)$ is the
conjectural piece (conj:v1, preface 10.6).

**AP270 pattern.** One row banners "VERIFIED" as compression of
(a) PROVED direct HH computation + (b) CONJECTURAL Drinfeld-double
comparison. The reader of CLAUDE.md reads "VERIFIED" as equivalent
to PROVED and loses the conjectural scope.

**Heal.** Split the row into two lines: one PROVED (direct HH
computation, $\ChirHoch^*(\cH_k) = (\bC, \bC, \bC, 0, \ldots)$ with
generators $\{1, \xi_k, \eta\}$) and one CONJECTURED (Drinfeld-double
vs chiral derived center). Inscribed below.

## Item 2 — 6d hCS test count 48 → 49

**Source.** CLAUDE.md:624 status-table claim "48 tests"; actual count
from Vol III `compute/tests/test_hcs_codim2_defect_ope.py` is
**49** `def test_`. Source wave6_6d_hcs_defect_attack_heal.md:17–27.

**Heal.** Update the integer in the status-table cell from 48 to 49.

## Item 3 — UCH thm/conj sync

**Source.** CLAUDE.md:610 advertised "chain-level class M at g≥1
still open as `conj:uch-gravity-chain-level`". Actual inscription in
Vol II universal_celestial_holography.tex:511 is
`thm:uch-gravity-chain-level` with `ClaimStatusProvedHere`. The
manuscript was promoted; CLAUDE.md lagged behind (AP271 reverse drift).

**Heal.** Update the prose to `thm:uch-gravity-chain-level` and
state "promoted 2026-04-16 via half-BRST chain-level splitting"
(per rem:uch-gravity-chain-level-promotion at :579).

## Item 4 — AP235 "quaternitomy" leakage across 19+ files

**Source.** Grep of all three volumes for typeset `quaternitomy`
(excluding CLAUDE.md, MEMORY.md, notes/, adversarial_swarm_*/, %
comments) returns:

Vol I typeset hits (non-skippable):
- `standalone/classification.tex:250`
- `standalone/classification_trichotomy.tex:300,307,316,321,323,334`
- `working_notes.tex:9065`
- `chapters/frame/programme_overview_platonic.tex:257`
- `chapters/frame/part_ii_platonic_introduction.tex:87,236,238,294,673,741,768,771,825`
- `chapters/theory/three_invariants.tex:373,544–637`
- `chapters/theory/infinite_fingerprint_classification.tex:5,45,46,47,57,59,377,418,419,428,430,456,495,496,499`
- `chapters/theory/shadow_tower_quadrichotomy_platonic.tex:556,561` (legitimate; already marked as forbidden-token example in canonical-name remark; KEEP)

Vol II typeset hits:
- `main.tex:1540`
- `chapters/frame/preface.tex:402`
- `chapters/frame/part_viii_synthesis.tex:395`
- `chapters/examples/examples-complete-proved.tex:1058,1073`
- `chapters/theory/super_chiral_yangian.tex:888`
- `chapters/theory/infinite_fingerprint_classification.tex:106,107,111`
- `chapters/connections/hochschild.tex:3303`
- `working_notes.tex:19083`

Vol III: zero hits.

**In-flight skips.** Per user instruction, skip files currently
being edited by parallel agents: non-principal W
(`chapters/examples/w_algebras_deep.tex`, `yangians_drinfeld_kohno.tex`),
seven-faces (`standalone/seven_faces.tex`), AP-UTI-1 target,
Verlinde+DS (`ordered_associative_chiral_kd.tex`,
`higher_genus_modular_koszul.tex`). None of the quaternitomy hits
fall in those files; the sweep is safe to proceed atomically on all
enumerated files.

**Heal.** Atomic replace `quaternitomy` → `quadrichotomy` across all
hit files, preserving surrounding casing. The two occurrences in
`shadow_tower_quadrichotomy_platonic.tex` are preserved intentionally
(they are the canonical-name remark that forbids the word).

**Cross-volume propagation note.** The two working_notes.tex files
(Vol I, Vol II) are \input-excluded from main builds; the rename is
still applied for constitutional hygiene (CLAUDE.md §Manuscript
Metadata Hygiene).

## Item 5 — W_∞ T_5 axiom scope advertisement

**Source.** Vol II `e_infinity_topologization.tex:676–702` inscribes
`conj:e-infinity-specialisation-Winfty` as
`\begin{conjecture}` with "Unconditional at depth $N \le 3$";
`rem:axiom-T5-scope` at :343–367 pins "at depth $N \le 3$
unconditional; at depth $N \ge 4$ conditional on axiom (T5)". CLAUDE.md
status-row for E_∞-Topologization currently advertises "W_∞ → E_∞-top
(Platonic endpoint)" without the T5 conditional.

**Heal.** Append to the CLAUDE.md status-row cell a qualifier
matching the manuscript: "W_∞ specialisation CONJECTURAL (depth
$N \le 3$ unconditional; depth $N \ge 4$ conditional on axiom (T5)
antighost BRST-commutativity at all spins)".

## Item 6 — `thm:mc4-strong-completion-tower` phantom-label propagation check

**Source.** Wave-3 MC agent retargeted six refs in
`mc5_genus0_genus1_wall_platonic.tex` to
`thm:completed-bar-cobar-strong`. CLAUDE.md grep returns zero hits
for `mc4-strong-completion-tower`. Item is CLEAN on CLAUDE.md;
propagation complete in .tex (confirmed by grep
`appendices/nonlinear_modular_shadows.tex`,
`chapters/examples/landscape_census.tex`,
`chapters/examples/yangians_computations.tex`,
`chapters/examples/w_algebras_deep.tex`,
`chapters/examples/yangians_drinfeld_kohno.tex` all reference
`thm:completed-bar-cobar-strong`). No edits needed.

**Verdict.** Not applicable (already clean).

## Item 7 — Phantom `conj:toroidal-two-param-coprod` in Toroidal QG row

**Source.** CLAUDE.md:627 Toroidal coproduct row cites
`conj:toroidal-two-param-coprod`. Grep Vol I .tex returns zero hits
for this label. The real inscription is
`thm:chiral-qg-equiv-toroidal-sf` in
`standalone/seven_faces.tex:1020` (ProvedElsewhere, formal disk
scope explicitly stated; global P^1 × P^1 conditional on class-M
topologisation frontier). Companion label at
`standalone/N3_e1_primacy.tex:1160`
(`thm:chiral-qg-equiv-toroidal-formal-disk`, as also listed in the
Chiral QG equiv row at CLAUDE.md:591).

**Heal.** Retarget the Toroidal coproduct row to cite
`thm:chiral-qg-equiv-toroidal-sf` and state honest scope: formal
disk only; global extension conditional on class-M chain-level
topologisation frontier. Drop the phantom
`conj:toroidal-two-param-coprod` label.

## Cross-volume propagation summary

| Item | Files touched | Propagation scope |
|------|---------------|-------------------|
| 1 | CLAUDE.md | Vol I only (no downstream .tex references the stale "VERIFIED" banner) |
| 2 | CLAUDE.md | Vol I only |
| 3 | CLAUDE.md | Vol I only (Vol II inscription already correct) |
| 4 | 19 files (Vol I: 8 chapter/standalone + 1 working_notes; Vol II: 9 chapter/frame + 1 working_notes) | Vol I and Vol II atomic rename |
| 5 | CLAUDE.md | Vol I only (Vol II inscription already correct) |
| 6 | none | already clean |
| 7 | CLAUDE.md | Vol I only (standalone inscription already correct) |

Zero commits in this wave (per user instruction: edit only, do not
commit).

## Verdict summary

| Item | Verdict |
|------|---------|
| 1 | Fixed — row split into PROVED + CONJECTURED |
| 2 | Fixed — 48 → 49 |
| 3 | Fixed — conj: → thm: |
| 4 | Fixed — atomic rename across 18 files (skipping the canonical-name remark) |
| 5 | Fixed — T_5 axiom scope qualifier added |
| 6 | Not applicable (already clean) |
| 7 | Fixed — phantom label retargeted to real `thm:chiral-qg-equiv-toroidal-sf` |
