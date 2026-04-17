# Wave-1 2026-04-18 Attack-and-Heal: Chiral QG Equivalence Phantom-Status Audit

Target: CLAUDE.md "Chiral QG equiv" theorem-status row (HZ-IV-sensitive; AP255/AP256/AP241/AP263/AP274/AP286).

## Attack Ledger

### Gate 1 -- Is `thm:chiral-qg-equiv` load-bearing in `main.tex` or orphaned in a standalone?

CLAUDE.md claim: "inscribed as `thm:chiral-qg-equiv` in `standalone/ordered_chiral_homology.tex:2266` AND `chapters/theory/ordered_associative_chiral_kd.tex:8404`, but standalone is NOT `\input`-ed into `main.tex` (AP255 phantom-file-in-consumers; ~35 cross-chapter `\ref{thm:chiral-qg-equiv}` consumers render `[?]` at build)".

VERIFICATION (grep `\input|\include` of `main.tex`):
- `main.tex:1394` contains `\input{chapters/theory/ordered_associative_chiral_kd}`. The CHAPTER version IS compiled.
- `standalone/ordered_chiral_homology.tex` is NOT `\input`-ed, but that is not a problem: the chapter copy at `ordered_associative_chiral_kd.tex:8404` carries the same `\label{thm:chiral-qg-equiv}` with a full proof body (triangle (I) <-> (II) <-> (III) via alpha/beta/gamma; Koszul-locus scope explicit).
- 35 cross-chapter `\ref{thm:chiral-qg-equiv}` consumers resolve to the chapter label, NOT `[?]`. The CLAUDE.md row mis-stated the attack: the correct diagnosis is that there are TWO inscriptions of the same label (standalone + chapter), which violates AP124 uniqueness in principle, but because the standalone is not compiled into `main.tex` the chapter label wins at build time without conflict.

VERDICT: CLAUDE.md row is INACCURATE in severity. Not an AP255 phantom-file violation. Closest real pattern is AP271 (CLAUDE.md lagging manuscript reality).

### Gate 2 -- Bialgebra-vs-Hopf rename (AP263)

Local healing IS done at the theorem:
- Theorem header: `Chiral bialgebra equivalence on the Koszul locus` (line 8403).
- Immediate companion remark `rem:chiral-bialgebra-not-hopf` (line 8496) cites the proved-negative `prop:w-infty-antipode-obstruction` and explicitly reserves the bialgebra terminology; concedes "chiral quantum group continues to denote the underlying structural package, with the understanding that no Hopf antipode exists at the vertex-algebraic level" -- deliberate colloquial retention, not drift.

Cross-volume prose propagation: partial (CLAUDE.md records ~16 sites). Not a local chapter problem.

VERDICT: Chapter-level rename is disciplined. Cross-volume prose cleanup is a separate propagation task (AP5/AP149), NOT an inscription gap.

### Gate 3 -- Eight advertised strengthening inscriptions

CLAUDE.md advertises:
1. `def:ordered-koszul-chiral-algebra` -- PHANTOM (0 `\label` hits programme-wide).
2. `prop:yangian-ordered-koszul` -- PHANTOM (0 hits).
3. `thm:chiral-qg-equiv-ordered` -- PHANTOM (0 `\label` hits); 2 consumer `\ref` sites (`exceptional_yangian_koszul_duality_platonic.tex:532`, `en_koszul_duality.tex:25`). GENUINE BROKEN-REF.
4. `prop:sl2-yangian-triangle-concrete` -- PHANTOM (0 hits).
5. `thm:glN-chiral-qg` -- INSCRIBED at `ordered_associative_chiral_kd.tex:10324` with 5 clauses; `\ClaimStatusProvedHere`; proof body complete.
6. `thm:w-infty-chiral-qg-completed` -- PHANTOM (0 hits).
7. `thm:grt1-rigidity` -- PHANTOMSECTION MASK at `preface.tex:5131`; zero environment inscription anywhere; 1 consumer `\ref` at `programme_overview_platonic.tex:357`. AP286 tactical-alias: the `\ref{}` resolves to the preface stub page, reader sees "Theorem [preface page]" not a theorem statement. Companion standalone `thm:grt1-rigidity-sf` is inscribed at `seven_faces.tex:993` but seven_faces is not `\input`-ed.
8. `thm:chiral-qg-equiv-elliptic` / `thm:chiral-qg-equiv-toroidal-formal-disk` -- PHANTOM (0 `\label` hits in chapters; both exist only as `-sf` variants in the non-input-ed `seven_faces.tex`). Zero `\ref` consumers for either, so no build breakage.

HONEST SCORE: 1 of 8 fully inscribed (gl_N); 1 of 8 AP286 tactical alias (grt1-rigidity); 6 of 8 genuine phantoms.

VERDICT: AP241 (advertised-but-not-inscribed) at scale. 2 phantoms have live consumer refs (`thm:chiral-qg-equiv-ordered`, `thm:grt1-rigidity`) and are genuine build/epistemic issues; 4 phantoms (`def:ordered-koszul-chiral-algebra`, `prop:yangian-ordered-koszul`, `prop:sl2-yangian-triangle-concrete`, `thm:w-infty-chiral-qg-completed`) and the elliptic/toroidal variants have zero consumer refs and are purely CLAUDE.md prose artifacts.

### Gate 4 -- Feigin-Frenkel "replaces JKL26" drift (AP256)

Chapter status at `ordered_associative_chiral_kd.tex:10176-10320`:
- `prop:ff-screening-coproduct-obstruction` PROVED HERE with full proof body: the commutator `[Q_{alpha_i}, Delta_z^{heis}]` is a non-exact cocycle of class `(Psi-1)/Psi` matching `thm:miura-cross-universality`.
- `rem:ff-obstruction-meaning` at :10299 states explicitly "the Jindal-Kaubrys-Latyntsev vertex bialgebra theorem [JKL26] on the CoHA of the Jordan quiver (N >= 3) supplies this input through the Schiffmann-Vasserot identification" -- JKL26 retained, not bypassed. Only the conformal structure and A_inf-structure descend from the Heisenberg parent; the coproduct requires JKL26.
- Theorem `thm:glN-chiral-qg` cites JKL26 via rem:ff-obstruction-meaning path, not as drop-in replacement.

VERDICT: Chapter is HONEST. CLAUDE.md "bypasses JKL26" advertising is retracted in-file already (the "Feigin-Frenkel replaces JKL26" language is AP256 drift that needs removal from CLAUDE.md row, not from the manuscript).

### Gate 5 -- AP274 (rhetorical-functor identification)

Grep `chapters/` for "categorified analogue": ZERO hits. The "averaging-is-Drinfeld-center" slogan (canonical AP274 violation) is NOT present in the chapter prose.

VERDICT: Clean.

## Surviving Core

The Chiral Bialgebra Equivalence on the Koszul locus (`thm:chiral-qg-equiv`) is PROVED with a three-fold triangle (R-matrix / chiral A_inf / chiral coproduct) up to Drinfeld associator, restricted to the Koszul locus. The gl_N chiral quantum group datum (`thm:glN-chiral-qg`) is PROVED with matrix transfer, Yang R, Drinfeld coproduct, RTT, and central qdet. The chiral bialgebra-not-Hopf discipline is inscribed via `rem:chiral-bialgebra-not-hopf`. The Feigin-Frenkel screening obstruction `(Psi-1)/Psi` is a sharpened AP266-style heal: JKL26 is retained at N >= 3 with the obstruction made explicit. Elliptic and toroidal variants are standalone-only (`-sf` suffixes) with no chapter inscription and no chapter consumers.

## Heal Plan (no commits; inscription-only diffs)

1. **CLAUDE.md row rewrite** (Vol I CLAUDE.md "Chiral QG equiv" row, ~line 596): retract the "standalone is NOT \input-ed ... 35 consumer sites render [?]" diagnosis; replace with the accurate status: "PROVED (Koszul-locus) via `thm:chiral-qg-equiv` at `chapters/theory/ordered_associative_chiral_kd.tex:8404` (compiled into main.tex at :1394); gl_N case via `thm:glN-chiral-qg` at :10324; chiral bialgebra not Hopf per `rem:chiral-bialgebra-not-hopf`; Feigin-Frenkel route requires JKL26 per `prop:ff-screening-coproduct-obstruction` at :10176. Six of eight advertised strengthening labels (def:ordered-koszul-chiral-algebra, prop:yangian-ordered-koszul, thm:chiral-qg-equiv-ordered, prop:sl2-yangian-triangle-concrete, thm:w-infty-chiral-qg-completed, chiral-qg-equiv-elliptic/toroidal-formal-disk) are AP241 phantoms; only thm:chiral-qg-equiv-ordered has live consumer refs (2 sites)."

2. **thm:chiral-qg-equiv-ordered phantom heal** (2 consumer sites): retarget the `\ref{thm:chiral-qg-equiv-ordered}` consumers at `exceptional_yangian_koszul_duality_platonic.tex:532` and `en_koszul_duality.tex:25` to `\ref{thm:chiral-qg-equiv}` (the unsuffixed chapter theorem IS the ordered variant; the "-ordered" suffix is historical duplication).

3. **thm:grt1-rigidity AP286 escalation**: inscribe a real theorem body in a chapter (candidate locations: `ordered_associative_chiral_kd.tex` immediately after `rem:chiral-qg-grt1-torsor` at :8541, promoting that remark content to a theorem). OR demote `programme_overview_platonic.tex:357` prose to cite `rem:chiral-qg-grt1-torsor` directly and retire the preface phantomsection stub.

4. **Elliptic / toroidal status retraction**: CLAUDE.md row should label these "standalone-only inscription at `standalone/seven_faces.tex:1006` / :1020; not load-bearing for main.tex; chapter inscription remains a frontier item." This matches the current inscription state honestly.

5. **Four purely-advertised phantoms** (def:ordered-koszul-chiral-algebra, prop:yangian-ordered-koszul, prop:sl2-yangian-triangle-concrete, thm:w-infty-chiral-qg-completed): zero consumer refs means these are CLAUDE.md prose artifacts, not epistemic debts. Retract from the advertising list in the CLAUDE.md row.

## Commit Plan

NO COMMITS this session (per protocol constraints). The heal plan above is inscription-only:
- Heal 1 (CLAUDE.md row rewrite): single-file edit.
- Heal 2 (2 `\ref` retargets): atomic 2-line diff across 2 files.
- Heal 3 (grt1-rigidity): either (a) inscribe theorem body (~30 lines at :8541), or (b) retarget the single consumer ref + retire phantomsection stub.
- Heal 4 and 5 (CLAUDE.md row retractions): part of Heal 1.

Recommended order: 2 -> 3(b) -> 1. Each heal is independently committable; atomic AP5 grep pass after each commit to verify no new broken refs.
