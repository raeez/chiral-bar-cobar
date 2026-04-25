# Manuscript Healing Task List, 2026-04-24

## Scope

This queue records live repair obligations found by hostile audit and
current manuscript scans. It excludes `appendices/first_principles_cache.md`,
where AP and pattern identifiers are deliberate local memory rather than
reader-facing mathematics.

## A. Theorem C Residual Drift

- [x] Replace the undefined Hinich source with an actual bibliography key:
  `Hin97`.
- [x] Correct the GR17 attribution from Francis--Gaitsgory to
  Gaitsgory--Rozenblyum.
- [x] Insert the weightwise-to-total bridge in
  `prop:perfectness-standard-landscape`: conformal blocks identify
  `H^0` of the flat bar fiber, and degree-zero concentration supplies
  total fiber finiteness on the stated affine lanes.
- [x] Remove process-history prose from
  `chapters/theory/theorem_C_refinements_platonic.tex`.
- [x] Replace independent-verification decorator comments in
  `chapters/theory/theorem_C_refinements_platonic.tex` by mathematical
  verification remarks or remove them.
- [x] Update `standalone/theorem_index.tex` so
  `thm:C-PTVV-alternative` is a conditional compatibility criterion, not
  a mixed-status independent mapping-stack alternative.
- [x] Update `FRONTIER.md` so CL7 no longer says the perfectness bridge is
  still in progress.

## B. MC5 Class-M Ambient Discipline

- [x] Treat raw direct-sum failure and pro-object completion as compatible:
  the former is false in bounded `Ch(Vect)`, the latter is proved in the
  retained filtered/pro ambient.
- [x] Remove "cache entry" process vocabulary from
  `chapters/theory/mc5_class_m_chain_level_platonic.tex`, replacing it
  with named mathematical obstructions and homotopies.

## C. Reader-Facing Process Residue

- [x] Remove AP/FM/HZ/cache/decorator/process strings from ordinary
  chapters and frame files, excluding deliberate notes/cache material.
- [x] Replace test-decorator language with mathematical verification
  language: independent paths, source disjointness, and explicit files
  may remain; implementation slang should not.
- [x] Remove process comments in chapter headers that record campaigns,
  waves, AP identifiers, or editorial history.

## D. Meta-Narration

- [x] Remove exact meta-narration signatures from ordinary chapters:
  "present chapter", "present section", "in the present work",
  "we now turn to", "having established", "let us now",
  "this brings us to", "it is worth noting", "notably", "crucially",
  "remarkably", "furthermore", and "moreover".
- [x] Prefer direct mathematical assertions over signposting.

## E. Status-Surface Phantoms

- [x] Audit `standalone/theorem_index.tex` entries explicitly marked
  `[PHANTOM FILE: chapter does not exist on disk]`.
- [x] Retarget phantom entries to actual labels when they are aliases;
  otherwise downgrade/remove them from the proved surface.

## F. Verification

- [x] Rerun the exact forbidden-process scan on `chapters/` and relevant
  status surfaces.
- [x] Rerun the exact meta-narration scan on `chapters/`.
- [x] Regenerate metadata if claim-status-bearing TeX changed.
- [x] Run `git diff --check`.
- [x] Run only targeted tests touched by compute or claim-surface changes.
  No compute library was changed in this pass, so metadata regeneration and
  static manuscript scans were the targeted verification surface.

## G. Proved-to-Weak Dependency Closure

- [x] Audit Vol I `metadata/claims.jsonl` for every
  `ClaimStatusProvedHere` claim whose local reference block points to a
  `Conjectured`, `Conditional`, `Heuristic`, or `Open` claim.
- [x] Repair Vol I by demoting or rewriting every surviving source in the
  dependency graph. Final Vol I metadata: 3919 tagged claims; 1951
  `ProvedHere`, 456 `ProvedElsewhere`, 370 `Conjectured`, 1110
  `Conditional`, 29 `Heuristic`, 3 `Open`; proved-to-weak edges: 0.
- [x] Run the same fixed-point audit on Vol II after metadata regeneration.
  Final Vol II metadata: 3132 tagged claims; 2351 `ProvedHere`, 264
  `ProvedElsewhere`, 234 `Conjectured`, 238 `Conditional`, 44
  `Heuristic`, 1 `Open`; proved-to-weak edges: 0.
- [x] Run the same fixed-point audit on Vol III after metadata regeneration.
  Final Vol III metadata: 1770 tagged claims; 755 `ProvedHere`, 300
  `ProvedElsewhere`, 315 `Conjectured`, 390 `Conditional`, 10
  `Heuristic`, 0 `Open`; proved-to-weak edges: 0.

## H. Cross-Volume Claim-Surface Closure

- [x] Repair the W-algebra/Bershadsky--Polyakov same-family duality
  overclaim across Vol I and Vol II: the proved statement is the
  characteristic companion equality; algebra equality remains conditional
  on DS/bar transport.
- [x] Remove the false cross-volume duplicate label
  `prop:harmonic-factorization` from Vol II by renaming the standalone
  bar-Hochschild proposition to
  `prop:bar-hochschild-harmonic-factorization`.
- [x] Correct Vol II sewing statuses where the theorem bodies carry local
  proofs: `thm:general-hs-sewing` and `thm:heisenberg-sewing` are
  `ProvedHere` in Vol II.
- [x] Re-run the exact-label cross-volume status scan. Cross-volume
  exact-label status conflicts across Vol I, Vol II, and Vol III: 0.

## I. Active Duplicate-Label Closure

- [x] Repair active duplicate labels in Vol I, Vol II, and Vol III.
- [x] Re-run the active-label scan from each volume's metadata parser.
  Final active duplicate labels: Vol I 0; Vol II 0; Vol III 0.

## J. Residual Verification Boundary

- [x] Regenerate Vol I, Vol II, and Vol III metadata after claim-status
  edits.
- [x] Regenerate `standalone/theorem_index.tex` from current Vol I
  metadata so it no longer carries stale duplicate notes or stale
  `ProvedHere` rows for conditional claim surfaces.
- [ ] Full LaTeX builds were not run in this pass; builds remain
  session-end/user-opt-in verification.

## K. Theorem-Shaped Heuristic Closure

- [x] Audit all `ClaimStatusHeuristic` claims whose environment is not a
  remark across Vol I, Vol II, and Vol III.
- [x] Convert theorem/proposition/corollary/conjecture heuristic surfaces
  to `ClaimStatusConjectured`, and computation heuristic surfaces to
  `ClaimStatusConditional`.
- [x] Regenerate metadata in all three volumes and verify:
  non-remark heuristic claims are now zero in Vol I, Vol II, and Vol III.

## L. Open-Status Closure

- [x] Convert the Vol I Langlands-gap surfaces from open-ended status to
  conditional scope barriers.
- [x] Convert the Vol II Type~H existence surface from `Open` to a normal
  conjectural existence claim.
- [x] Remove residual raw `ClaimStatusOpen` tokens from chapter and
  standalone sources in Vol I, Vol II, and Vol III, either by deleting
  status tags from genuine questions/problems or by replacing them with
  conjectural/conditional status where a mathematical claim is asserted.
- [x] Regenerate metadata. Final open-status counts: Vol I 0; Vol II 0;
  Vol III 0.

## M. Reopened Proof-Graph Closure

- [x] Repair Vol II proof-graph defects exposed by fresh metadata:
  principal `\(\mathcal W_N\)` finite-envelope compatibility, KZB
  two-edge corner obstruction, conditional harmonic beta-radius, Virasoro
  Zwegers-shadow scalar specialization, logarithmic `\(\mathcal W(p)\)`
  regular-sector reduction, and inactive duplicate YM/spectral labels.
- [x] Repair Vol III proof-graph defects exposed by fresh metadata:
  the CY-C residual comparison register and the K3\(\times\)E
  Hall--BKM completion package are conditional registers, not proved
  theorem surfaces.
- [x] Re-run strict proved-to-weak audits. Final strict-edge counts:
  Vol I 0; Vol II 0; Vol III 0.
- [x] Re-run exact-label status conflict audit across Vol I, Vol II, and
  Vol III. Final exact-label status conflicts: 0.

## N. Final Targeted Verification

- [x] Final metadata counts:
  Vol I total 3919, PH 1951, PE 456, CJ 372, CD 1113, H 27, O 0;
  Vol II total 3141, PH 2359, PE 264, CJ 256, CD 243, H 19, O 0;
  Vol III total 1793, PH 773, PE 300, CJ 310, CD 401, H 9, O 0.
- [x] `git diff --check` passes in Vol I, Vol II, and Vol III.
- [x] Targeted Vol I tests pass:
  `317 passed, 4 xfailed`.
- [x] Targeted Vol II tests pass:
  `277 passed, 1 skipped`.
- [x] Targeted Vol III tests pass:
  `223 passed`.
- [ ] Full LaTeX builds were not run; builds remain user-opt-in
  session-end verification.

## O. Three-Volume Front-Matter and Session-Spoils Rectification

- [x] Re-audit Vol I, Vol II, and Vol III dirty working state after the
  interrupted merge/build work, including live worktrees and background TeX
  processes.
- [x] Re-read the Chriss--Ginzburg rectification instructions and the
  cross-volume propagation instructions before writing into front matter.
- [x] Locate the active abstract, preface, and introduction surfaces in all
  three volumes and distinguish them from superseded notes, standalones, and
  extraction PDFs.
- [x] Load each volume's concordance and theorem registry around the
  front-matter claims that will be named explicitly.
- [x] Extract the session-spoils spine from the recent commits: Vol I sextic
  shadow correction, Stokes pole \(c_S=-218/45\), Borel radius
  \(|\omega|^2(c)=c^2(5c+22)/[4(45c+218)]\), Riccati-on-\(U\) master
  equation, BP conductor label hygiene, \(\beta_N=12(H_N-1)\), W2
  Monster--K3 \(c_+\)-product \(24\), and
  \(c_{25}^{(\mathrm{depth}\ 5)}=\zeta(3,3,5,5,9)/25!\).
- [x] Extract the Vol II session-spoils spine: the
  \(\mathsf{SC}^{\mathrm{ch,top}}\) heptagon, the chain model
  \(C^\bullet_{\mathrm{ch}}(A,A)\simeq
  \Omega^{\mathrm{ch}}(B^{\mathrm{ch}}(A))\), the normalization
  \(h_A=h_{\mathrm{LV}}/(\kappa+\kappa^!)\), fat-diagonal BD
  associativity, weight-completed class-\(\mathsf M\) topologisation,
  celestial \(W_{1+\infty}\) endpoint scope, and the KZ/BV analytic-SDR
  conditional package.
- [x] Extract the Vol III session-spoils spine: two-stage
  \(\Phi_d=\mathrm{Sp}^{\mathrm{ch}}_{\Sigma_{d-1},C}\circ
  \Phi^{\mathrm{FA}}_d\), six-route \(K3\times E\) common-limit cone,
  \(\mathfrak{so}(4,20)\) K3 Yangian trichotomy, K3 Hall--Drinfeld
  crown, \(S^3\)-framing on generic compact CY\(_3\) Lagrangians,
  generic CY\(_3\) MNOP via Joyce \(V_X\) and KPS orientation, and
  class-\(\mathsf M\) \(E_3\)-bar past genus \(3\).
- [x] Rewrite Vol I abstract losslessly, preserving every mathematical claim
  while inserting the new session spine in CG voice.
- [x] Rewrite Vol I preface in place where the old front-matter architecture
  does not yet carry the session spine.
- [x] Rewrite Vol I introduction in place, including body-proper propagation
  where the front matter names a theorem whose proof surface has moved.
- [x] Rewrite Vol II abstract losslessly, including the KZ/BV conditional
  status and the heptagon/topologisation/celestial scope.
- [x] Rewrite Vol II preface and introduction without upgrading conditional
  KZ/BV claims to proved claims.
- [x] Rewrite Vol III abstract if present, otherwise insert the equivalent
  abstract/front-matter opening into the active preface/introduction surface.
- [x] Rewrite Vol III preface and introduction so the two-stage functor,
  K3 Yangian, Hall--Drinfeld, and generic CY\(_3\) statements are stated
  with subscripted \(\kappa_\bullet\)-discipline.
- [x] Run cross-volume phrase sweeps for the old unsafe claims: unconditional
  KZ all-loop recursion, single-output \(\Phi_d\) wording, raw class-\(\mathsf
  M\) direct-sum topologisation, bare \(\kappa\), and stale sextic/Borel
  formulas.
- [x] Regenerate metadata in each edited volume if claim-status-bearing
  manuscript sources changed. No regeneration needed: edits changed prose only,
  added no labels, and changed no claim-status tags.
- [x] Run conflict-marker scans and `git diff --check` across all edited
  volumes.
- [x] Commit source/front-matter changes separately from generated metadata
  or binary artifacts, with Raeez-only exhaustive messages.
- [x] Preserve and merge the remaining Vol II KZ side-worktree staged
  Makefile parity state without discarding it.

## P. Four-Volume Extension: Vol IV Realization Layer

- [x] Extend the dirty-state and recent-history audit to
  `~/chiral-bar-cobar-vol4`.
- [x] Read Vol IV `CLAUDE.md`, `AGENTS.md`, active `main.tex`,
  `chapters/frame/preface.tex`, and
  `chapters/realization/realization_programme.tex` before writing.
- [x] Inspect Vol IV recent commits around the arithmetic realization
  branch: critical-line Hadamard support, post-Tate quotient,
  Meyer graph-dual no-go, and final residual ledger.
- [x] Identify Vol IV side worktrees. The branch heads are ancestors of
  `main`, but many locked worktrees contain dirty state owned by a live
  Claude process; this thread must not mutate those worktrees.
- [x] Add a Vol IV abstract to `main.tex` carrying the realization functor,
  the Vol I/II/III session-spoils corpus, the finite-jet KZ/BV scope, the
  Joyce--KPS compact-CY3 lane, and the native Vol IV arithmetic residual.
- [x] Upgrade the Vol IV preface so the realization input corpus includes
  the corrected Virasoro shadow tower, four-conductor split,
  Gritsenko--Clery spread, KZ/BV analytic-SDR scope, Joyce--KPS compact
  CY3 scope, and post-Tate/Hadamard support no-go.
- [x] Upgrade the Vol IV realization-programme body with realization
  obligations for the Khan--Zeng finite-jet BV/PVA lane, the Joyce--KPS
  compact Calabi--Yau threefold lane, and the post-Tate Hadamard/Meyer
  graph-dual no-go.
- [x] Correct the Vol IV programme-wide coverage arithmetic from
  `5 / 3692` with `3687` remaining to `5 / 3695` with `3690` remaining.
- [x] Remove front-facing AP/HZ process residue from the edited Vol IV
  front-matter and realization-programme passages where it was not
  mathematical terminology.
- [ ] Do not run full LaTeX builds unless explicitly requested; Vol IV
  verification in this pass is static TeX/diff hygiene plus targeted scans.
