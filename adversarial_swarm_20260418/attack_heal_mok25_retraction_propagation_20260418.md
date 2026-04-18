# Mok25 retraction propagation — attack-and-heal (2026-04-18)

Raeez Lorgat. Wave-X follow-through on the Mok25 programme-wide audit
(`attack_heal_mok25_programme_audit_20260418.md`). Propagates the
retraction of the iteration-2 Theorem A OF1 audit's "Mok25 is FABRICATED
(AP269/AP281)" framing, based on the Mok25 primary-source verification
(Siao Chi Mok, arXiv:2503.17563, "Logarithmic Fulton--MacPherson
configuration spaces", March 2025, v2 May 2025).

Scope: ledger annotations + three-volume bibkey harmonization + Vol I
CLAUDE.md + FRONTIER.md status-row scope refinement. No new APs
inscribed (task is propagation of the existing Mok25-audit finding into
cross-referenced sites).

## Executive verdict

The iteration-2 Theorem A modular-family OF1 audit's claim that Mok25
is a phantom / fabricated mechanism was a bibkey-drift artefact: the
`standalone/references.bib` entry recorded `author = {Mok, Chung-Pang}`
and a drifted title "Log Fulton--MacPherson compactifications and
tropicalization of planted forests", causing the iteration-2 audit to
search against Chung-Pang Mok's publications (automorphic forms,
Purdue) and find no match. The actual preprint is by SIAO CHI MOK
(algebraic geometry, Cambridge / Imperial), arXiv:2503.17563,
"Logarithmic Fulton--MacPherson configuration spaces" (submitted 21
March 2025, v2 21 May 2025); the paper exists and covers the claimed
topic area.

Consequence: the "AP269 fabricated-mechanism" + "AP281 phantom-citation"
labels attached to Mok25 by iteration-2 are withdrawn. The residual
concern is single-preprint-pillar risk (AP1241): Mok25 is cited at
citation level across Vol I + Vol II + Vol III for load-bearing log-FM
sewing / nodal-factorization-gluing / modular-family base-change, and
is a 2025 preprint without venue publication, so programme-wide load on
a single unpeer-reviewed source remains a legitimate scope item, not a
fabrication item.

## Phase 1. Ledger annotations

Grep target: `adversarial_swarm_20260418/*.md` + `patches/` carrying
`Mok25` / `Chung-Pang` / `fabricat` language.

Files surveyed: 11 total hits across the directory. Classification by
language-usage:

1. `attack_heal_mok25_programme_audit_20260418.md` — the canonical
   audit. No retraction needed; this IS the primary source of the
   propagation.
2. `attack_heal_thmA_modular_20260418.md` — iteration-2 ledger
   carrying "The `Mok25` bibkey resolves against no primary source ...
   fabricated-mechanism check" at lines ~88-96. **Retraction banner
   inscribed at top** (20 lines) citing the Mok25 programme-wide audit
   as superseding.
3. `attack_heal_d2_zero_convolution_20260418.md` — carries the
   inherited phantom-bibkey framing at lines ~119-134.
   **Retraction banner inscribed at top** (12 lines).
4. `patches/patch_thmA_modular_20260418.patch` — carries
   "Mok25 ... resolves against no arXiv, DOI, or venue" +
   "attributed author-title combination does not match any known work
   of Chung-Pang Mok". **Retraction banner inscribed at top** (18
   lines); the E2 bibkey-edit hunk is marked superseded (the correct
   heal is bibkey harmonization, see Phase 2).
5. Other 7 files (`attack_heal_theorem_A_20260418.md`,
   `wave3_cy_c_pentagon_attack_heal.md`, `attack_heal_verlinde_20260418.md`,
   `wave3_verlinde_attack_heal.md`, `wave3_theorem_D_attack_heal.md`,
   `attack_heal_theorem_D_20260418.md`,
   `wave1_theorem_A_attack_heal_v2.md`): Mok25 cited at
   citation-level only ("conditional on Mok25 log-FM sewing" etc.),
   NO "fabricated" or "phantom" framing. No retraction annotation
   needed; these ledgers already treat Mok25 as a real cited preprint.

## Phase 2. Cross-volume bibkey harmonization

Four load-bearing bibkey-definition sites across the three volumes.

### Vol I, standalone BibTeX database

`standalone/references.bib:601-607`. Before:

```
@article{Mok25,
  author  = {Mok, Chung-Pang},
  title   = {Log {F}ulton--{M}ac{P}herson compactifications and
             tropicalization of planted forests},
  year    = {2025},
  note    = {Preprint},
}
```

After:

```
@article{Mok25,
  author        = {Mok, Siao Chi},
  title         = {Logarithmic {F}ulton--{M}ac{P}herson configuration spaces},
  year          = {2025},
  eprint        = {2503.17563},
  archivePrefix = {arXiv},
  primaryClass  = {math.AG},
  note          = {Submitted 21 March 2025; v2 21 May 2025},
}
```

Edits: author Chung-Pang -> Siao Chi; title "Log FM compactifications
and tropicalization of planted forests" -> "Logarithmic FM configuration
spaces"; eprint + archivePrefix + primaryClass added; note scope
sharpened from "Preprint" to explicit submission/revision dates.

### Vol I, hand-written bibliography

`bibliography/references.tex:1022-1023`. Before:

```
\bibitem{Mok25}
C.-P. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

After:

```
\bibitem{Mok25}
S.~C. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

Edit: initial drift `C.-P. Mok` -> `S.~C. Mok` matching Siao Chi Mok.
Title, arXiv ID, year already correct.

### Vol II, main bibliography in-line

`~/chiral-bar-cobar-vol2/main.tex:2210-2211`. Before:

```
\bibitem{Mok25}
C.-P. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

After:

```
\bibitem{Mok25}
S.~C. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

Edit: same initial harmonization `C.-P. Mok` -> `S.~C. Mok`.

### Vol III, hand-written bibliography

`~/calabi-yau-quantum-groups/bibliography/references.tex:185-186`. Before:

```
\bibitem{Mok25}
C.-P. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

After:

```
\bibitem{Mok25}
S.~C. Mok, \emph{Logarithmic Fulton--MacPherson configuration spaces}, arXiv:2503.17563, 2025.
```

Edit: same.

All four sites now attribute the preprint consistently to Siao Chi Mok
(S.~C. Mok / `author = {Mok, Siao Chi}`) with arXiv:2503.17563 and
2025.

## Phase 3. Vol I CLAUDE.md status-row edits

### Theorem A row

Added explicit primary-source attribution inside the existing "(b)
Mok25 logarithmic factorization-gluing at the nodal boundary" clause:

- Before: `(b) Mok25 logarithmic factorization-gluing at the nodal
  boundary, to globalise the equivalence across the full compactified
  base.`
- After: `(b) Mok25 logarithmic factorization-gluing at the nodal
  boundary (Siao Chi Mok, arXiv:2503.17563, March 2025 v2 May 2025),
  to globalise the equivalence across the full compactified base.`

Row was already correctly citation-level in its modular-family-CONDITIONAL
scope; no "fabricated" framing to retract.

### D^2=0 row

Retraction of inherited phantom-bibkey framing. The row previously
carried "Wave-18 Thm-A-OF1 audit ... finds Mok25 bibkey is AP281
phantom with no locatable primary source"; rewritten to cite the
Mok25 programme-wide audit as superseding, name the bibkey-drift
root cause (Siao-Chi-Mok vs Chung-Pang-Mok conflation), and downgrade
the AP label from "AP281 phantom" to "AP1241 single-preprint pillar".
Ambient-level status-tag `ClaimStatusProvedHere` conditional on Mok25
remains; the conditional dependency is on a real 2025 arXiv preprint,
not on a fabricated mechanism.

## Phase 4. FRONTIER.md CL2 row

`/Users/raeez/chiral-bar-cobar/FRONTIER.md:13`, in the list of three
open inscription targets for Theorem A modular-family extension:

- Before: `(b) Mok25 log-FM nodal sewing at chain level;`
- After: `(b) Mok25 log-FM nodal sewing at chain level (Siao Chi Mok,
  arXiv:2503.17563, March 2025, v2 May 2025 — per Wave-X Mok25
  programme-wide audit 2026-04-18, author identity is verified; prior
  iteration-2 "fabricated-mechanism" framing was a
  Siao-Chi-Mok / Chung-Pang-Mok bibkey-drift confusion, now
  retracted);`

No other FRONTIER.md line required revision: CL2 is the sole Mok25
mention, and the downgrade-to-CONDITIONAL framing is the correct
scope.

## Phase 5. AP inventory

AP block AP1401-AP1420 was reserved for this mission per the prompt.
Zero new APs inscribed. The retraction is propagation of the existing
AP1241 / AP281 / AP269 discipline applied through the Mok25
programme-wide audit's verdict; all new patterns were already
registered there.

## Phase 6. Delivery inventory (per AP316)

Files modified in this session:

1. `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/attack_heal_thmA_modular_20260418.md`
2. `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/attack_heal_d2_zero_convolution_20260418.md`
3. `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260418/patches/patch_thmA_modular_20260418.patch`
4. `/Users/raeez/chiral-bar-cobar/standalone/references.bib`
5. `/Users/raeez/chiral-bar-cobar/bibliography/references.tex`
6. `/Users/raeez/chiral-bar-cobar-vol2/main.tex`
7. `/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex`
8. `/Users/raeez/chiral-bar-cobar/CLAUDE.md` (Theorem A + D^2=0 rows)
9. `/Users/raeez/chiral-bar-cobar/FRONTIER.md` (CL2)

No isolated-worktree patches required: all edits run directly in the
main repos (no `isolation: worktree` Agent invoked).

## Residual

The AP1241 single-preprint-pillar scope item remains open: Mok25 is a
March 2025 preprint cited at citation level for load-bearing log-FM
sewing / nodal factorization-gluing across ~30+ sites programme-wide.
Venue publication tracking, specific-theorem cross-check against
arXiv:2503.17563 (Theorems 3.3.1 + 5.3.4 cited at
`higher_genus_modular_koszul.tex:32418` ambient-level D^2=0 theorem),
and per-site `ClaimStatusConditional` retag for sites that genuinely
consume Mok25 chain-level (rather than citation-level) content are
Wave-N+1 targets.
