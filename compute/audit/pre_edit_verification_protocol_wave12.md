# Pre-Edit Verification Protocol (Wave 12)

**Scope**: Mandatory fill-in-the-blank self-check agents must complete BEFORE writing any formula in Vol I / Vol II / Vol III of the Modular Koszul Duality programme.

**Rationale**: The anti-pattern catalog in `CLAUDE.md` (AP1-AP141) lists rules in prose. Prose rules are not actionable during flow: agents read them, nod, and then violate them. Empirical evidence from the 300-commit deep archaeology and the 48-agent cross-volume sweep: 30+ new AP126 (r-matrix level) instances appeared in a SINGLE rectification session, all post-dating the original AP126 warning. The fix is NOT "remind harder" -- it is to force the agent to EXECUTE the check as a precondition to writing. Filling out a template IS the verification.

This document defines 12 templates, each ~10 lines, each mechanically fillable, each impossible to fake-fill without actually performing the check. An invocation protocol and integration plan follow.

---

## Template 1 -- r-matrix write (AP126, AP141, AP19, AP20)

**Trigger**: Any new r-matrix formula, any edit touching an existing r-matrix, any reference to `r(z)` / `r_{ij}` / classical r-matrix.

```
## PRE-EDIT: r-matrix
family:                    [Heisenberg / affine KM / Virasoro / W_N / lattice / Yangian / other: _____]
r(z) written:              [_______________________________ full formula with level prefix]
level parameter symbol:    [k / k+h^v / hbar / c / Psi / other: _____]
OPE pole order p:          [_____]
r-matrix pole order p-1:   [_____]  # AP19: d log absorbs one pole
AP126 check (level=0):     r(z)|_{level=0} = [_______________]
                           expected per AP126: 0 (else NOT a level-stripped r-matrix)
  match?                   [Y/N]  # must be Y
AP141 grep check:          ran Grep for "Omega/z" and "\\Omega / z" in edit scope: [found _____ bare instances]
  bare Omega/z allowed?    [N]    # always N unless explicitly abelian level-1
critical-level check (KM): r(z)|_{k=-h^v} = [_______________]  (N/A for non-KM)
sign of level prefix:      [positive / negative]   # KM: +k; Heis: +k; verify against landscape_census.tex
source for formula:        [computed now / landscape_census.tex line _____ / Vol I chapter _____]
FORBIDDEN bare forms logged: Omega/z (no level), Omega/(z(k+h^v)) (wrong normalization for KM)
```

**Reject condition**: blank `match?` or `N`, or missing source citation, or family = `other` without explanation.

---

## Template 2 -- kappa formula write (AP1, AP9, AP24, AP39, AP48, AP136)

**Trigger**: Any formula involving the shadow constant kappa or its variants (kappa_eff, kappa(B), kappa_ch, kappa_BKM, kappa_cat, kappa_fiber). Any r-matrix scalar computation. Any obs_g / lambda_g formula.

```
## PRE-EDIT: kappa
family:                    [Heis / Vir / KM / W_N / bc / beta-gamma / symplectic fermion / other: _____]
kappa formula written:     [_______________________________]
census citation:           landscape_census.tex line [_____], kappa^{family} = [_____]
  match?                   [Y/N]  # must be Y; if N, STOP and re-read landscape_census.tex
AP39 uniqueness check:     is kappa = S_2 (stress tensor self-OPE)? [Y/N]
  if Y, is family Virasoro? [Y/N]    # only Vir has kappa = S_2/2 = c/2
AP1 evaluation paths:
  at trivial/free limit:   kappa|_{k=0}      = [_____]  expected [_____]
  at critical level (KM):  kappa|_{k=-h^v}   = [_____]  expected [_____]
  at c=13 (Vir):           kappa|_{c=13}     = [_____]  expected 13/2
AP136 boundary (W_N only): kappa formula uses [H_N / H_{N-1} / H_N-1]
  substitute N=2:          [_____]  expected c*(1/2)
common wrong variants avoided:
  - NOT kappa(Vir) = c (correct: c/2)
  - NOT kappa(W_N) = c*H_{N-1}      (AP136: correct c*(H_N-1))
  - NOT kappa(Heis) = k/2           (correct: k)
  - NOT kappa(KM) = (k+h^v)/(2h^v)  (missing dim(g) factor)
```

**Reject condition**: missing census citation, or family=Heis/KM/W_N with formula pasted from another family.

---

## Template 3 -- complementarity sum (AP24, AP33, AP8)

**Trigger**: Any equation of the form `kappa + kappa' = [RHS]`, `c + c' = [RHS]`, any Koszul conductor write, any self-duality claim.

```
## PRE-EDIT: complementarity / Koszul conductor
family:                    [KM / free-field / Virasoro / W_N / bc / beta-gamma / other: _____]
equation written:          kappa + kappa' = [_____]  or  c + c' = [_____]
family-qualifier in SAME sentence?  [Y/N]   # must be Y (AP8)
expected RHS per family:
  KM / free:               0
  Virasoro:                13  (Feigin-Frenkel c <-> 26-c; conductor K = 26)
  W_N:                     rho_N * K_N   (from landscape_census.tex)
  lattice:                 depends on rank; cite source
match?                     [Y/N]  # must be Y
self-duality point:        c = [_____]  or kappa = [_____]
AP140 check: is this c+c' (global Koszul conductor) or a local constant (ghost number, grading shift)?  [global / local]
  if local, rename to avoid "Koszul conductor"
AP36 "iff" check:          is this written as biconditional "<=>"?  [Y/N]
  if Y, is the converse proved in the same theorem?  [Y/N]   # must be Y, else downgrade to "implies"
```

**Reject condition**: universal-quantifier phrasing ("self-dual" without family), or "iff" without converse, or missing family qualifier.

---

## Template 4 -- bar complex formula (AP132, AP22, AP23, AP44)

**Trigger**: Any write of `B(A)`, `T^c(...)`, any bar-construction formula, any desuspension.

```
## PRE-EDIT: bar complex
object written:            B(A) = [_______________________________]
T^c argument uses:         [s^{-1} A-bar / s A-bar / A / bare A]
AP132 augmentation:        augmentation ideal present?  [Y/N]   # must be Y
  A-bar = ker(epsilon) explicitly cited?  [Y/N]   # must be Y
AP22 desuspension sign:    |s^{-1} v| = |v| - [1 / +1]   # must be -1 (LOWERS)
  is s^{-1} written (NOT bare s)?  [Y/N]   # must be Y
AP44 LaTeX check:          in source, is it `s^{-1}` or `s`?  [s^{-1} / s]
  must be s^{-1}
coproduct type:            [deconcatenation (T^c, n+1 terms) / coshuffle (Sym^c, 2^n) / coLie (Harrison)]
  match to intended bar?   [B^ord -> deconc / B^Sigma -> coshuffle / B^Lie -> coLie]
differential d^2 = 0?      [always, AP132: even for curved A-inf; curvature lives in m_1^2]
grading convention:        cohomological, |d| = +1?  [Y/N]
```

**Reject condition**: `A` instead of `A-bar`, `s` instead of `s^{-1}`, missing coproduct type, or mismatch between bar flavor and coproduct.

---

## Template 5 -- Vol III kappa write (AP113)

**Trigger**: ANY occurrence of kappa in a Vol III file (`~/calabi-yau-quantum-groups/**/*.tex`). Zero tolerance.

```
## PRE-EDIT: Vol III kappa
volume confirmed:          [Vol III]        # if not, use Template 2
subscript written:         [kappa_ch / kappa_cat / kappa_BKM / kappa_fiber / OTHER: _____]
subscript present?         [Y/N]            # must be Y; bare kappa is FORBIDDEN in Vol III
subscript justification:   why this subscript? [chiral shadow / categorified / BKM / fiber correction]
landscape citation:        Vol III landscape_census_cy.tex line [_____]
grep verification:         ran Grep on file for bare `\kappa[^_]` BEFORE write:  [ _____ hits]
                           ran Grep on file for bare `\kappa[^_]` AFTER write:   [ _____ hits]
  delta must be 0          [Y/N]
```

**Reject condition**: blank subscript, or grep delta > 0, or volume check fails.

---

## Template 6 -- exceptional group / Lie-algebraic dimension (AP10, AP39)

**Trigger**: Any write of `dim E_8`, `dim g`, a fundamental representation dimension, a dual Coxeter number, a root lattice invariant.

```
## PRE-EDIT: exceptional dimension
group / algebra:           [E_6 / E_7 / E_8 / F_4 / G_2 / sl_n / so_n / sp_n / other: _____]
written value:             [_____]
canonical set cited:
  E_8 fundamentals:        {248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}
  E_7 fundamentals:        {56, 133, 912, 1463, 1539, 6480, 7371, ...}
  E_6 fundamentals:        {27, 78, 351, 650, 2925, 17550, 46332, ...}
  F_4 fundamentals:        {26, 52, 273, 324, 1053, 1274, ...}
  G_2 fundamentals:        {7, 14, 27, 64, 77, 189, ...}
  dual Coxeter h^v:        E_8=30, E_7=18, E_6=12, F_4=9, G_2=4, sl_n=n, so_{2n}=2n-2, so_{2n+1}=2n-1, sp_{2n}=n+1
written value in set?      [Y/N]   # must be Y
source for value:          [landscape_census.tex line _____ / Bourbaki ch. _____ / Atlas / computed]
AP10 derivation paths (>=2):
  path 1:                  [_____]
  path 2:                  [_____]
```

**Reject condition**: value not in canonical set, or fewer than 2 derivation paths, or missing source.

---

## Template 7 -- Label creation (AP124, AP125)

**Trigger**: Any `\label{...}` write, any new theorem/proposition/conjecture/definition/remark/lemma.

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma / corollary / section]
label written:             \label{[_____]:[_____]}
AP125 prefix match:
  environment -> prefix:   theorem->thm, proposition->prop, conjecture->conj, definition->def,
                           remark->rem, lemma->lem, corollary->cor, section->sec
  prefix used:             [_____]
  match?                   [Y/N]   # must be Y
AP124 duplicate check:
  ran Grep for label in Vol I:    [_____ matches]
  ran Grep for label in Vol II:   [_____ matches]
  ran Grep for label in Vol III:  [_____ matches]
  total matches BEFORE write:     [_____]
  total matches AFTER write:      [_____]
  delta = 1 exactly?              [Y/N]    # must be Y
if duplicate found, rename with volume suffix (e.g., thm:koszul-v2) and update all \ref
```

**Reject condition**: prefix mismatch, delta != 1, or duplicate unresolved.

---

## Template 8 -- Cross-volume formula (AP5, AP3)

**Trigger**: Any formula shared across volumes (kappa, r-matrix, Theta_A, bar differential, connection 1-form, complementarity, any named constant).

```
## PRE-EDIT: cross-volume formula
formula:                   [_______________________________]
Vol I grep:                ran Grep in /Users/raeez/chiral-bar-cobar/            [_____ hits, canonical form: _____]
Vol II grep:               ran Grep in /Users/raeez/chiral-bar-cobar-vol2/       [_____ hits, canonical form: _____]
Vol III grep:              ran Grep in /Users/raeez/calabi-yau-quantum-groups/   [_____ hits, canonical form: _____]
consistent across volumes? [Y/N]
if inconsistent:
  canonical volume:        [Vol I / Vol II / Vol III]
  canonical form:          [_____]
  other volumes updated same session?  [Y/N]   # must be Y (AP5)
convention-conversion needed?  [OPE modes (Vol I) -> lambda-brackets (Vol II) / motivic (Vol III)]
conversion applied?        [Y/N/NA]
```

**Reject condition**: inconsistency found without atomic same-session fix, or missing convention conversion when crossing Vol I <-> Vol II.

---

## Template 9 -- Summation / harmonic number (AP116, AP136)

**Trigger**: Any `\sum_{j=a}^{b}`, any `H_N`, any finite-product notation, any boundary-sensitive formula.

```
## PRE-EDIT: summation boundary
summation written:         sum_{j=[_____]}^{[_____]} [_____]
smallest-index substitution:
  at j = [lower bound]:   term = [_____]
  expected smallest term: [_____]
  match?                  [Y/N]
largest-index substitution:
  at j = [upper bound]:   term = [_____]
  match?                  [Y/N]
harmonic number (if applicable):
  H_N written as:         [sum_{j=1}^{N} 1/j / sum_{j=1}^{N-1} 1/j / other]
  AP136 check: is H_{N-1} intended or H_N - 1?  [H_{N-1} / H_N - 1 / same -- WRONG]
  evaluate at N=2: H_1 = 1;  H_2 - 1 = 1/2.  These DIFFER.
  written form matches intent?  [Y/N]
off-by-one check (smallest N where boundary matters): [_____]
```

**Reject condition**: mismatch at smallest-index substitution, or `H_{N-1}` confused with `H_N - 1`.

---

## Template 10 -- Genus / arity / scope quantifier (AP6, AP7, AP32, AP139)

**Trigger**: Any theorem statement, any formula for obs_g / F_g / lambda_g / m_k, any universal quantifier.

```
## PRE-EDIT: scope quantifier
statement:                 [_______________________________]
genus specified?           [g = 0 / g = 1 / g >= 2 / all g / unspecified -- REJECT]
arity specified?           [n = _____ / all n / unspecified -- REJECT]
level (convolution vs ambient)? [convolution M-bar_{g,n} / ambient Mok25 log FM / both / N/A]
AP32 uniform-weight tag:   (if obs_g / F_g / lambda_g present)
  tag:                     [(UNIFORM-WEIGHT) / (ALL-WEIGHT with delta F_g^cross) / N/A]
  tagged in statement?     [Y/N]   # must be Y for any g >= 2 claim
AP139 free-variable audit:
  variables on LHS:        {_____}
  variables on RHS:        {_____}
  LHS \supseteq RHS?       [Y/N]   # if N, bind the free variable or reject
AP7 universal quantifier: does "for all" hide a hypothesis?  [Y/N]
  hidden hypotheses:       [_____]
AP36 implies vs iff:       [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
```

**Reject condition**: unspecified genus/arity, missing uniform-weight tag, free variable, or unjustified iff.

---

## Template 11 -- Connection 1-form / propagator / differential form type (AP117, AP27)

**Trigger**: Any write of a connection 1-form, KZ connection, Arnold form, bar propagator.

```
## PRE-EDIT: differential form
what is being written?     [connection 1-form / bar propagator / Arnold form / KZ / other: _____]
form written:              [_______________________________]
form type declared:
  connection 1-form:       must be r(z) dz     NOT r(z) d log(z)
  KZ:                      must be sum r_{ij} dz_{ij}
  Arnold form:             d log(z_i - z_j)    (bar coefficient, NOT connection)
  bar propagator:          d log E(z,w)        (weight 1, ALWAYS, AP27)
match?                     [Y/N]
AP27 weight check:         is propagator weight 1?  [Y/N]   # must be Y; weight h is FORBIDDEN
AP117 d log check:         if `d log` appears, is it Arnold-form context?  [Y/N]
  if N (connection context), REWRITE as dz
on what space does the form live?  [fiber Sigma_g / base M-bar_{g,n} / FM_n(X) / Ran(X)]
AP130 fiber-base check:    object on fiber vs class on base correctly distinguished?  [Y/N]
```

**Reject condition**: `d log` in connection context, weight != 1 propagator, or fiber-base confusion.

---

## Template 12 -- Modal / prose slop / LaTeX hygiene (AP121, AAP1, prose laws)

**Trigger**: Any prose edit in a .tex file (paragraphs, chapter intros, remark blocks).

```
## PRE-EDIT: prose hygiene
text block (first 20 words): [_____]
AI-slop scan (forbidden): notably, crucially, remarkably, interestingly, furthermore, moreover,
                          delve, leverage, tapestry, cornerstone, importantly, in essence
  any hits?                [Y/N]   # must be N
em-dash scan:              any `--` or `---` or unicode em-dash?  [Y/N]   # must be N
markdown leak (AP121):     any backtick numerals `29`?  [Y/N]     # must be N
                           any **bold** or _italic_?    [Y/N]     # must be N
AAP1 injection check:      any `antml` or `</invoke>` in file?  [Y/N]   # must be N (grep after write)
passive-voice hedge scan:  "it can be shown that", "we may note that", "it is worth noting"  [Y/N]   # must be N
scope explicitly stated?   [Y/N]   # must be Y (prose law 7)
state-once-prove-once?     [Y/N]   # must be Y (prose law 6)
```

**Reject condition**: any slop hit, any em-dash, any markdown, any AAP1 injection.

---

## Invocation Protocol

### Option analysis

**(a) On every Edit call touching that formula type.** Maximum safety. High friction: every kappa edit carries a 15-line preamble. Unless enforced by hook, agents skip under load.

**(b) Only on explicit "formula write" mode.** Lowest friction but unenforceable: agents forget to enter mode. Empirical failure: AP126 was "well known" yet produced 30+ new violations in one session.

**(c) As a mandatory comment block before the Edit tool call.** Middle ground. Agent writes the template as a fenced code block in the reply text (NOT in the .tex file), then invokes Edit. The fill-in process happens in-chat, visible to the caller.

### Recommended integration: **(c) hybrid -- mandatory in-chat block + hook enforcement**

1. **In-chat template**: Before every Edit touching a trigger pattern, the agent writes the relevant template as a fenced block in the reply BEFORE the Edit call. This is visible to human reviewers and becomes part of the session transcript. The block ends with a single-line `verdict: ACCEPT` or `verdict: REJECT` sentinel.

2. **Hook enforcement (settings.json PreToolUse hook)**: a lightweight hook scans Edit tool calls for trigger patterns (regex over `new_string`): `\\kappa`, `r\\(z\\)`, `\\label\\{`, `\\sum_{j=`, `B\\(A\\)`, `T\\^c`, `d\\log`, `dim\\s*E_`, etc. On match, the hook requires that the previous assistant message contains a fenced `## PRE-EDIT: [template name]` block with `verdict: ACCEPT`. If absent, the hook denies the Edit. This shifts enforcement from agent discipline to harness discipline.

3. **Template shortcuts**: each template gets a short slug (`PE-1` through `PE-12`). In practice, the agent writes `PE-1 (r-matrix):` followed by the fill-in. Slugs make audit grep trivial.

4. **Triggers -> templates mapping** (for hook):

   | Regex trigger                                        | Template |
   |------------------------------------------------------|----------|
   | `r\(z\)`, `\\mathcal R`, `r_{ij}`, `\b r\^`          | PE-1     |
   | `\\kappa` (not in Vol III)                           | PE-2     |
   | `\\kappa` (in Vol III file path)                     | PE-5     |
   | `\\kappa\s*\+`, `c\s*\+\s*c'`, `Koszul conductor`    | PE-3     |
   | `B\(A\)`, `T\^c`, `s\^\{-1\}`, `\\bar A`             | PE-4     |
   | `E_[678]`, `\\mathfrak{e}_[678]`, `h\^\\vee`         | PE-6     |
   | `\\label\{`                                          | PE-7     |
   | `cross-volume` keyword, or shared-formula heuristic  | PE-8     |
   | `\\sum_\{j=`, `H_\{?N`, `\\sum_\{k=`                 | PE-9     |
   | `\\obs_g`, `F_g`, `\\lambda_g`, `\\begin\{theorem`   | PE-10    |
   | `d\\log`, `dz_\{ij\}`, `KZ`, `Arnold`                | PE-11    |
   | prose-paragraph edit heuristic                       | PE-12    |

5. **Escape hatch**: for pure typo fixes (single-character), the agent may write `PE-skip: typo` instead of a full template. The hook allows skip only if `len(new_string) - len(old_string) < 5` and no trigger regex matches the delta.

---

## Example filled-in template (PE-1, genuine)

```
## PRE-EDIT: r-matrix
family:                    affine KM (sl_2, level k)
r(z) written:              r(z) = k * Omega / z   where Omega = sum_a t_a otimes t^a (Casimir)
level parameter symbol:    k
OPE pole order p:          2   (J^a(z) J^b(w) ~ k delta^{ab} / (z-w)^2 + f^{abc} J^c / (z-w))
r-matrix pole order p-1:   1
AP126 check (level=0):     r(z)|_{k=0} = 0 * Omega / z = 0
                           expected: 0
  match?                   Y
AP141 grep check:          ran Grep for "Omega/z" bare in chapters/e1_core/: 0 bare instances
  bare Omega/z allowed?    N
critical-level check (KM): r(z)|_{k=-h^v} = -2 * Omega / z (h^v=2 for sl_2)  -- regular, no pole at k=-h^v
sign of level prefix:      positive (+k)
source for formula:        landscape_census.tex line 414 (affine KM classical r-matrix)
FORBIDDEN bare forms logged: Omega/z (no level), Omega/(z(k+h^v)) -- neither written
verdict: ACCEPT
```

## Example filled-in template (PE-2, caught error)

```
## PRE-EDIT: kappa
family:                    W_3
kappa formula written:     kappa(W_3) = c * H_2 = c * (1 + 1/2) = 3c/2
census citation:           landscape_census.tex line 728, kappa^{W_N} = c * (H_N - 1)
  match?                   N  -- STOP
AP39 uniqueness check:     kappa = S_2 ?  N (only Vir)
AP1 evaluation paths:
  AP136 boundary N=2:      my formula: c * H_2 = 3c/2
                           census:     c * (H_2 - 1) = c/2
                           DIFFERENT -- my formula is WRONG
  corrected:               kappa(W_3) = c * (H_3 - 1) = c * (1 + 1/2 + 1/3 - 1) = 5c/6
  re-check N=2:            c * (H_2 - 1) = c * 1/2 = c/2  (W_2 = Vir, kappa = c/2: MATCH)
common wrong variants avoided:
  - NOT c * H_{N-1}  (AP136)
  - NOT c * H_N      (my initial error)
verdict: REJECT original, ACCEPT corrected c * (H_N - 1) form
```

---

## CLAUDE.md integration path

**Phase 1 (immediate, this session)**: Add a single line to CLAUDE.md `Session Protocol` section:

> 10. Before every Edit touching a trigger pattern (r-matrix, kappa, B(A), labels, exceptional dimensions, cross-volume formulas, summations, connection forms, scope quantifiers), fill out the relevant PE-1..PE-12 template from `compute/audit/pre_edit_verification_protocol_wave12.md` as a fenced block in the reply, ending with `verdict: ACCEPT` before invoking Edit. Hook enforces.

**Phase 2 (next session)**: Implement the settings.json PreToolUse hook that scans Edit `new_string` for trigger regexes and denies the call unless the preceding assistant message contains a matching PE-N block. Hook is a 50-line bash script (grep + awk on transcript).

**Phase 3 (ongoing)**: Track template rejection rate per session. If PE-1 rejects > 20% of r-matrix writes, that indicates CLAUDE.md's r-matrix canonical form is still unclear -- update census. If PE-5 rejects > 5% of Vol III kappa writes, subscripts are still being forgotten -- audit Vol III.

**Phase 4 (maturity)**: Every new anti-pattern added to CLAUDE.md MUST ship with a template. AP without template is unenforced prose.

---

## Template priority ranking (for initial rollout)

Most critical (ship first): **PE-1 (r-matrix), PE-2 (kappa), PE-5 (Vol III kappa), PE-7 (labels)**. These four cover the highest-recurrence AP violations (AP126, AP1, AP113, AP124/125) and have the cleanest trigger regexes.

Middle priority: **PE-4 (bar complex), PE-8 (cross-volume), PE-10 (scope quantifier)**. High value but triggers are harder to regex-match; rely on agent discipline until hook matures.

Lower priority (but still mandatory): **PE-3, PE-6, PE-9, PE-11, PE-12**. Lower recurrence or harder to mechanize.

---

## Refusal criteria (the agent MUST reject its own edit if...)

1. Template has `match? N` on any line where `Y` is required.
2. Template has blank source citation.
3. Template has `family = other` without explicit explanation.
4. Grep delta does not match expected delta (labels, Vol III kappa).
5. Any `FORBIDDEN` line is ticked.
6. Any prose-slop hit in PE-12.
7. Any AP reference in a Y/N line has `N` where `Y` required.

On rejection: the agent re-drafts the formula, re-fills the template, and only proceeds when `verdict: ACCEPT`.

---

## Closing note on why this works

Prose anti-patterns are advisory; templates are executable. An agent in flow will skim `"verify at k=0"` and move on. An agent filling out `level=0 check: r(z)|_{k=0} = [_____]` cannot move on without substituting. The blank forces the computation; the computation catches the error.

This protocol does not replace CLAUDE.md. It operationalizes the subset of CLAUDE.md that governs formula writing. The rest (prose standards, architectural decisions, theorem-status discipline) remains with CLAUDE.md and the Beilinson loop.
