# Wave 3 (2026-04-18): Verlinde recovery — adversarial attack and heal

**Target.** CLAUDE.md status-table row (line 599):
`| Verlinde recovery | PROVED | Verlinde Z_g = sum S_{0j}^{2-2g} recovered from ordered chiral homology at integer level (prop:verlinde-from-ordered). |`

**Inscription.**
- Vol I `chapters/theory/higher_genus_modular_koszul.tex:33369--33518` (`prop:verlinde-from-ordered`, `\ClaimStatusProvedHere`, subsection `subsec:verlinde-from-ordered` at :33324).
- Standalone `standalone/ordered_chiral_homology.tex:6145--6295` (identical statement, no `\ClaimStatus` tag — standalone inherits from parent).
- Engine: `compute/lib/verlinde_ordered_engine.py` (three code paths: direct S-matrix, quantum-dimension, handle recursion).
- HZ-IV decorator: `compute/tests/test_hz_iv_decorators_wave1.py:316--366` (`test_verlinde_from_ordered_boundary_checks`).
- CLAUDE.md entry at line 599 and the "Unconditional (high confidence)" list at line 1317.
- AGENTS.md:675.

Russian-school voice: Etingof, Kazhdan, Beauville--Laszlo, Tsuchiya--Ueno--Yamada, Bezrukavnikov, Polyakov.

**Relation to prior audit.** Wave 7 (2026-04-17, `adversarial_swarm_20260417/wave7_verlinde_ds_attack_heal.md`) visited the same target and declared "SURVIVES". This wave re-attacks with a finer tooth comb, specifically against AP241/AP255/AP259/AP272/AP280/AP287 patterns.

---

## Phase 1 — attack ledger

### A1. [MODERATE] Inscription locus is inverted; standalone is the template, chapter holds the `\ClaimStatusProvedHere` tag

**Severity:** MODERATE. **Category:** AP286 (tactical alias vs semantic heal) variant / inscription-home discipline.

The canonical `\ClaimStatusProvedHere` tag lives at `higher_genus_modular_koszul.tex:33372`. The standalone `standalone/ordered_chiral_homology.tex:6147` carries the same `\label{prop:verlinde-from-ordered}` (AP124 near-miss: label uniqueness requires one inscription-home) with no status tag. This is legitimate under AP127 (migrating `\input{chapter}` produces `\phantomsection\label{}` stubs) IF the standalone is `\input`-ed from `main.tex`; otherwise it is a duplicate. Grep of `main.tex` shows `ordered_chiral_homology` is standalone-only (not `\input`-ed), so the duplicate label is benign for the main build but rots under any future standalone compile that imports Vol I. Not load-bearing for the mathematical claim; flagged for consistency.

**Action:** leave as is; note in the heal ledger.

### A2. [MODERATE-HIGH] Clause (iii) proof delegates the load-bearing step to TUY89 via citation, with no locally inscribed bridge lemma

**Severity:** MODERATE-HIGH. **Category:** AP272 (unstated cross-lemma via folklore citation).

The clause (iii) proof at `higher_genus_modular_koszul.tex:33482--33493` reads:

> "The Verlinde formula [Verlinde88] gives Z_g = sum_j S_{0j}^{2-2g} as the dimension of the space of conformal blocks on a genus-g curve with no insertions. From the ordered chiral homology: the symmetric coinvariants of the ordered chain complex compute the conformal blocks via the factorization property (TUY [TUY89]). The KZB local system at integrable level decomposes into k+1 channels ... each channel j contributes S_{0j}^{2-2g} to the partition function."

The load-bearing bridge is the sentence "the symmetric coinvariants of the ordered chain complex compute the conformal blocks via the factorization property (TUY)." This is NOT a locally inscribed lemma. It is a citation to TUY89 for a specific theorem: Theorem 1 (the sheaf of covacua on `\overline{\cM}_{g,n}` is locally free of finite rank, recovering the Verlinde formula at integer level via Propagation of Vacua + Factorization). TUY89 works with the symmetric coinvariants directly; our statement is that the ORDERED chiral homology followed by the AVERAGING MAP `\av` agrees with the symmetric coinvariants. That ordered→symmetric step is NOT what TUY prove; they take symmetric as input. So the load-bearing step is actually:

**(B)** "`H_0` of the ordered chiral chain complex, symmetrised via `\av_0`, equals TUY's sheaf of covacua at degree 0."

Step (B) is CITED implicitly via TUY, but the object TUY work with is the symmetric quotient, not the ordered bar. The bridge that ordered-modded-out-by-S_n = TUY covacua is asserted, not proved. In the averaging-map framework (AP152), `\av_n: g^{E_1}_A \to g^{\mathrm{mod}}_A` is LOSSY at n>=1 (by definition, it is `\Sigma_n`-coinvariants) but the composition with `H_0` at GENUS `g >= 0, n = 0` is at degree 0 so `\av_0` is an isomorphism (nothing to symmetrise at degree 0). Clause (ii) proof explicitly uses this at line 33476--33479 ("nothing to symmetrise at degree 0, so all k+1 dimensions survive"). But that argument is a genus-1 computation. At `g >= 2`, the object `H^0(\cM_{g, 0}, V_k(\fg))` is NOT a degree-0 H_0 in the ordered bar sense — it is the space of CONFORMAL BLOCKS at genus g, which TUY build as covariants under a D-module system on `\overline{\cM}_{g, n}`, NOT as `\av_0` of something.

**Bottom line.** The phrasing "ordered chiral homology ... via factorization (TUY)" conflates two steps:
  1. Ordered → symmetric via `\av`.
  2. Symmetric coinvariants of chiral chain complex = TUY covacua = Verlinde.

Step 2 is TUY89 Theorem 1. Step 1 at g=0 n=0 is trivial (scalar vacuum line). Step 1 at g=1 n=0 uses the Zhu algebra + `\av_0`-iso argument. Step 1 at g>=2 is UNINSCRIBED — the text jumps from ordered bar to Verlinde-at-g through "factorization", but the factorization of the ordered bar at g>=2 requires the MODULAR-FAMILY EXTENSION of Theorem A (which is Conditional per Theorem A row; cf. AP249 and `rem:A-infinity-2-modular-family-scope` at `theorem_A_infinity_2.tex:890`). The g>=2 Verlinde recovery therefore INHERITS the modular-family-Theorem-A gap.

**Beilinson falsification test:** find an integrable-level chiral algebra where ordered→symmetric at g>=2 fails to land on TUY covacua. (Answer: none known for `\widehat{\fsl}_2` at integer level, by Beauville--Laszlo moduli-space identification; but that independent path makes Z_g(k) agree with TUY without routing through the ordered bar at g>=2.)

### A3. [MODERATE] Clause (iv) "handle attachment" asserts the identity `H_j = S_{0j}^{-2}` without deriving it from the bar complex sewing map

**Severity:** MODERATE. **Category:** AP259 (tautological-by-definition) variant / AP272 (unstated cross-lemma).

Clause (iv) proof at :33494--33501:

> "Handle attachment: a genus-g surface with a non-separating cycle cut open gives a genus-(g-1) surface with two extra marked points. The bar complex sewing map reglues these marked points, summing over the k+1 intermediate representations with the propagator S_{0j}^{-2} (the inverse of the j-th eigenvalue of the sewing operator). This gives Z_{g+1} = sum_j H_j * S_{0j}^{2-2g}."

The propagator `S_{0j}^{-2}` is inserted by hand as "the inverse of the j-th eigenvalue of the sewing operator". Nowhere in the proof (or in the companion Vol I `ordered_chiral_homology` standalone at :6271--6278) is this eigenvalue derived from the bar complex sewing map. Classical TQFT tells us `H_j = S_{0j}^{-2}` (Moore--Seiberg 1989) because the genus-g partition function satisfies `Z_{g+1} = Z_g` times the trace of the handle operator, and the handle operator is `C = \sum_j |j>(S_{0j}^{-2})<j|` in the basis of integrable representations. This is classical material; the gap is that our proof does not make the independent derivation from the bar complex sewing — it asserts `S_{0j}^{-2}` citation-free. AP259 flavor: assuming the handle propagator is the Moore--Seiberg handle propagator IS the derivation of Verlinde `\Sigma_j S_{0j}^{2-2g}`.

**Heal:** either (a) cite Moore--Seiberg 1989 / Bakalov--Kirillov Ch. 5 for the handle-propagator formula directly, with an attribution remark noting that clause (iv) is classical TQFT handle-attachment applied to the ordered-bar sewing map, not a first-principles ordered-bar derivation; or (b) construct the handle-propagator from the ordered-bar sewing map as a local lemma.

### A4. [MODERATE] Clause (v) "separating factorization" cites `Theorem A for the ordered bar complex on Ran^{ord}` which is Conditional at g>=2 per the Theorem A row

**Severity:** MODERATE. **Category:** AP249 (base-change/extension theorems require inscription) + AP287 (cross-volume theorem existence without HZ-11 attribution).

Clause (v) proof at :33503--33508:

> "Separating factorization: the bar complex factorization under separating degeneration (Theorem A for the ordered bar complex on Ran^{ord}) decomposes the genus-g partition function into a sum over channels of the product of the two lower-genus contributions, normalized by the propagator S_{0j}^{-2}."

Clause (v) INHERITS the Theorem A modular-family gap. Theorem A (row in CLAUDE.md, healed 2026-04-17 `wave1_theorem_A_attack_heal.md`) is PROVED unconditional on a FIXED SMOOTH CURVE X; the modular-family extension across `\overline{\cM}_{g, n}` including boundary is CONDITIONAL on Francis--Gaitsgory GR17 Ch. III §10 base-change on the relative Ran prestack + Mok25 logarithmic factorization-gluing. The separating-degeneration factorization of the ordered bar on `\Ran^{\mathrm{ord}}` at g1+g2=g crosses the boundary of `\overline{\cM}_g`; without the modular-family extension, the cited "Theorem A" argument is CITATION-LEVEL for the specific boundary stratum, not inscribed. The clause therefore silently relies on a Conditional ingredient and should be tagged `\ClaimStatusConditional` or attributed via `\begin{remark}[Attribution]` pointing to the modular-family scope remark `rem:A-infinity-2-modular-family-scope`.

**Heal:** scope-qualify clause (v) — either (a) add an attribution remark noting that the boundary-stratum factorization inherits the Theorem A modular-family conditional; or (b) downgrade clause (v) to `\ClaimStatusConditional` locally while keeping the other clauses (i)--(iv) `\ClaimStatusProvedHere`. Independent physical verification exists (Beauville--Laszlo 1994, Faltings 1994) but those route through moduli-of-bundles global sections, not through the ordered bar.

### A5. [LOW] HZ-IV decorator test body is numerically sound but scope-restricted

**Severity:** LOW. **Category:** AP277 (vacuous HZ-IV test body) check — PASSES.

The HZ-IV test `test_verlinde_from_ordered_boundary_checks` at `test_hz_iv_decorators_wave1.py:343--366` verifies:
  - `Z_0(k) = 1` via `verify_genus0_unitarity` (unitarity; k = 1..5).
  - `Z_1(k) = k+1` via `verify_genus1_count` (k = 1..5).
  - `Z_2(k) > 0` and integer for k in {1, 2, 3}.

Disjointness (a) S-matrix unitarity, (b) WZW rep count, (c) Beauville--Laszlo moduli-space formula — all independent of chiral-homology construction. This is a GENUINE HZ-IV decoration, not tautological (AP277 pass). The numerical body for g>=2 is weak — only `Z_2 > 0` is tested, not `Z_2 = 4, 10, 20, 35, 56` as tabulated in clause (iii). The g>=2 closed-form integer values are advertised as "part of the derived theorem" and therefore excluded from independent verification at HZ-IV — an honest scope qualifier, not a vacuous decoration.

**Heal (optional, LOW):** augment the test body to verify `Z_2(1) = 4` against Beauville--Laszlo `dim H^0(\cM_{SU(2)}(\Sigma_2), L) = (k+1)(k+2)(2k+3)/6` at k=1 gives 4; at k=2 gives 10; at k=3 gives 20. This pins the closed form at g=2 independently of S-matrix summation.

### A6. [LOW] CLAUDE.md status-row "at integer level" scope is honest but could be sharper

**Severity:** LOW. **Category:** AP283 (formula confabulation) check — PASSES.

The status row says "recovered from ordered chiral homology at integer level (prop:verlinde-from-ordered)." The prop IS inscribed (A1 noted), "integer level" is the proposition's hypothesis `k >= 1` positive integer (matches). No AP283 drift. The sharper honest form: "recovered for `\widehat{\fsl}_2` at positive integer level; g=0 and g=1 clauses unconditional; g>=2 clause inherits Theorem A modular-family extension gap via clauses (iv)--(v) sewing arguments."

### A7. [LOW] Clause (ii) third bullet ("ordered center") routes through `prop:ell-degree0` but the chapter version cites `eq:sl2-kappa` and a non-existent prop

**Severity:** LOW. **Category:** AP264 (phantom `\ref` to non-existent remark) check.

The chapter proof at :33473--33479 says: "The degree-0 center at integrable level is `\CC^{k+1}` (the center of the integrable quotient of `Y_\hbar` at the root of unity q = e^{2\pi i/(k+2)})."

No `\ref` is given in the chapter body. The standalone at :6176--6179 does cite `prop:ell-degree0`. Grep:


```
grep -rn '\label{prop:ell-degree0}' chapters/ standalone/ appendices/
```

Result: only `standalone/ordered_chiral_homology.tex:5519`. The chapter body at :33473--33479 uses the argument without a `\ref` — it states the result in prose. This is NOT a phantom `\ref` (no `\ref` is written), but it IS a load-bearing claim about the integrable-level degree-0 center of Y_hbar(sl_2) that is NOT inscribed anywhere in Vol I chapters. If the chapter intends to invoke `prop:ell-degree0` from the standalone, that is cross-file without cross-volume HZ-11 attribution (AP287 variant scoped within Vol I between chapters and standalones).

**Heal (LOW):** either (a) inscribe `prop:ell-degree0` (integrable-level degree-0 center = C^{k+1}) into the chapter, or (b) add a Remark[Attribution] in the chapter proof pointing to `\ref{standalone:prop:ell-degree0}` (the standalone-sourced proposition) — preferred for canonical-home purposes.

### A8. [MODERATE] Wave 7 audit noted "HZ-IV decorator properly articulated" but the Beauville--Laszlo path at g>=2 is cited, not inscribed

**Severity:** MODERATE. **Category:** AP243 (HZ-IV decorator non-disjoint dependency) variant — disjoint at the literature level, but the g>=2 closed-form values `Z_2(k) in {4, 10, 20, 35, 56}` at k in {1,...,5} in the chapter table are NOT independently verified in the HZ-IV test body (A5 note). The decoration "verified_against Beauville--Laszlo 1994 / Faltings 1994" is textual — the literature does pin `Z_g(k)` at g>=2 independently, but the HZ-IV test does not invoke that path computationally. Genuine disjointness at the literature level is sound; the test-body disjointness is weaker than the decorator prose suggests.

**Heal (optional, paired with A5):** extend the HZ-IV test body with Beauville--Laszlo closed-form spot-checks at g=2 for sl_2 (e.g. via the Hirzebruch--Riemann--Roch formula `\dim H^0(\cM_{SU(2)}(\Sigma_2), L^k) = (k+1)(k+2)(2k+3)/6`).

### A9. [INFO] The "Verlinde formula via bar complex" at `chiral_modules.tex:868` is a SEPARATE, `\ClaimStatusProvedElsewhere` theorem

**Severity:** INFO. **Category:** cross-reference note.

`chiral_modules.tex:868` inscribes `thm:verlinde-bar` as `\ClaimStatusProvedElsewhere` with `\cite{Verlinde}`, scope-qualified to positive integer level with integrable modules. This is the companion citation-level theorem at the modules-of-Zhu-algebra level. `prop:verlinde-from-ordered` is the ordered-chiral-homology version, tagged ProvedHere with three-path engine verification. Both coexist; this is not a duplicate label and not a conflict.

### A10. [INFO] The `chiral_climax_platonic.tex:740` corollary is a CLIMAX-THEOREM specialization

**Severity:** INFO. **Category:** cross-reference.

`chiral_climax_platonic.tex:740` inscribes `cor:climax-verlinde` stating: "the Moore--Seiberg (1989) presentation of the Verlinde formula is recovered at genus 0 as a rational-fusion specialization of the climax theorem." This is a corollary inside the climax chapter of Vol I Part VI; it is a third re-inscription at the corollary level, specialising the universal climax to Verlinde at rational fusion. Not load-bearing for `prop:verlinde-from-ordered`; included for situational awareness.

---

## Phase 2 — surviving core (2--3 Drinfeld sentences)

At `\widehat{\fsl}_2` with k a positive integer, the S-matrix entries `S_{0j}` (0 <= j <= k) are independently definable from the modular transformation of characters of integrable modules and from the braiding of the quantum group `U_q(\fsl_2)` at q = exp(2*pi*i/(k+2)); the integer `Z_g(k) = sum_j S_{0j}^{2-2g}` is the Verlinde formula, coinciding (by Tsuchiya--Ueno--Yamada 1989 + Beauville--Laszlo 1994) with `\dim H^0(\overline{\cM}_g, V_k(\fsl_2))`. The ordered chiral bar complex of `V_k(\fsl_2)` evaluated on a genus-g curve, averaged to symmetric coinvariants, agrees with the TUY sheaf of covacua at genera 0 and 1 (proved, clauses (i)--(ii), via unitarity of S and the Zhu algebra) and at genus `g >= 2` via the TUY factorization property and the Moore--Seiberg handle-propagator `H_j = S_{0j}^{-2}`, with the g>=2 recursion inheriting the Theorem A modular-family extension gap as a conditional ingredient. The Beilinson falsification test: at any positive integer level for any simply-laced simple g, the ordered-bar Z_g must coincide with the algebro-geometric rank of the Verlinde bundle; a discrepancy at g>=2 would falsify the ordered→symmetric factorization bridge (currently routed through TUY).

---

## Phase 3 — heal proposal (per finding)

| Finding | Severity | Heal Option | Status Tag Change |
|---------|----------|-------------|-------------------|
| A1 | MODERATE | Note inscription home; AP127 benign | none |
| A2 | MOD-HIGH | Add Remark[Attribution] to clause (iii) making the ordered→symmetric step and its routing through TUY89 Theorem 1 + factorization property explicit; note that at g>=2 the bridge relies on the modular-family extension of Theorem A (Conditional) | split tag: clauses (i)--(ii) `ProvedHere`, clauses (iii)--(v) `Conditional` on Theorem A modular-family + Moore--Seiberg handle propagator |
| A3 | MODERATE | Cite Moore--Seiberg 1989 + Bakalov--Kirillov Ch. 5 for the handle propagator; note clause (iv) is classical TQFT handle-attachment pulled back through bar sewing, not a first-principles ordered-bar derivation | part of A2 retag |
| A4 | MODERATE | Attribution remark citing `rem:A-infinity-2-modular-family-scope`; note the boundary-stratum sewing inherits the Theorem A conditional | part of A2 retag |
| A5 | LOW | Extend HZ-IV test body with Beauville--Laszlo closed-form `\dim H^0(\cM_{SU(2)}(\Sigma_2), L^k) = (k+1)(k+2)(2k+3)/6` at k=1..3 | none |
| A6 | LOW | Sharpen CLAUDE.md row: "PROVED at g=0,1; CONDITIONAL at g>=2 on Theorem A modular-family" | CLAUDE.md row update |
| A7 | LOW | Add Remark[Attribution] in chapter proof for clause (ii) third bullet pointing to `standalone:prop:ell-degree0`; OR inscribe prop:ell-degree0 locally | none |
| A8 | MODERATE | Paired with A5: verified_against extended with computational Beauville--Laszlo path, not just prose | none |
| A9, A10 | INFO | No action | none |

**Proposed CLAUDE.md status row (post-heal):**

`| Verlinde recovery | PROVED at g in {0, 1}; CONDITIONAL at g >= 2 on Theorem A modular-family extension + Moore--Seiberg handle propagator | Verlinde Z_g = sum S_{0j}^{2-2g} for sl_2 at positive integer level recovered from ordered chiral homology (prop:verlinde-from-ordered). Genus 0 (S-matrix unitarity) and genus 1 (Zhu algebra + ordered degree-0 center, k+1 integrable reps) unconditional. Genus g >= 2 inherits the Theorem A modular-family extension (currently conditional on Francis-Gaitsgory base-change + Mok25 log-FM gluing per rem:A-infinity-2-modular-family-scope) and invokes the Moore-Seiberg handle propagator H_j = S_{0j}^{-2} classically. Three-path engine verification (S-matrix summation, quantum-dimension, handle recursion); HZ-IV decorator against S-matrix unitarity, WZW rep count, Beauville-Laszlo moduli bundle. |`

---

## Phase 4 — commit plan (no commits in this wave per task constraint)

If commits were in scope:

1. **Edit `chapters/theory/higher_genus_modular_koszul.tex:33369--33518`.** Split the `\ClaimStatusProvedHere` tag: clauses (i)--(ii) keep `ProvedHere`; clauses (iii)--(v) downgrade to `\ClaimStatusConditional` via a clause-level tag. Add `\begin{remark}[Scope and conditionals]` immediately after the proposition environment referencing `rem:A-infinity-2-modular-family-scope` and citing Moore--Seiberg 1989 + Bakalov--Kirillov for the handle propagator. Add Remark[Attribution] for clause (ii) bullet 3 pointing to `standalone:prop:ell-degree0` OR inscribe prop:ell-degree0 locally.

2. **Edit `standalone/ordered_chiral_homology.tex:6145--6295`.** Propagate the same split-tag + attribution remark.

3. **Edit `CLAUDE.md` line 599 and 1317.** Update status row to the post-heal phrasing above; move `Verlinde recovery` from "Unconditional (high confidence)" list to a new "g in {0, 1} unconditional; g >= 2 conditional" slot (or retain in "Unconditional" with the genus qualifier in parentheses).

4. **Edit `compute/tests/test_hz_iv_decorators_wave1.py:316--366`.** Augment `test_verlinde_from_ordered_boundary_checks` with Beauville--Laszlo closed-form `(k+1)(k+2)(2k+3)/6` at k in {1, 2, 3} for g=2; rename to indicate augmented coverage.

5. **Run builds + tests.** `pkill -9 -f pdflatex; sleep 2; make fast` (Vol I). `pytest compute/tests/test_hz_iv_decorators_wave1.py -k verlinde -v`. Grep cleanup per manuscript-metadata-hygiene constitutional rule (no `AP\d+`, `HZ-[0-9]+`, `FM\d+` in typeset lines).

6. **Cross-volume propagation (AP5).** Grep Vols I/II/III for `verlinde-from-ordered` and any referencing prose; sync scope qualifiers.

7. **MEMORY.md / session notes update.** Record the split-tag heal as a "genus-stratified scope qualifier" heal per AP266 (sharpened-obstruction register).

No AI attribution anywhere in any commit. All commits would be authored by Raeez Lorgat.

---

## Verdict

- `prop:verlinde-from-ordered`: **SURVIVES at g in {0, 1}**, **CONDITIONAL at g >= 2** pending Theorem A modular-family extension + explicit Moore--Seiberg handle-propagator attribution. Wave 7's "SURVIVES" verdict is upheld for g in {0, 1} but the g>=2 clauses should be retagged Conditional to match the Theorem A scope discipline introduced in `adversarial_swarm_20260417/wave1_theorem_A_attack_heal.md`.
- HZ-IV decorator: **genuine** at the literature level (A5 PASS for AP277), **strengthenable** at the test-body level by adding Beauville--Laszlo computational path for g=2.
- CLAUDE.md row: **stale-but-not-drifting** (AP271 PASS); the "PROVED" banner is sound at g in {0, 1} and misses the g>=2 Conditional inheritance.

**Residual frontier for later waves:**
  1. Inscribe a local lemma "ordered bar H_0 on Sigma_g, symmetrised, equals TUY covacua at integer level" with full proof — would close the clause (iii) load-bearing gap and remove the Theorem A modular-family inheritance at g >= 2 (at least for `\widehat{\fsl}_2`).
  2. Extend `prop:verlinde-from-ordered` to affine KM beyond sl_2 at positive integer level (simply-laced g, then non-simply-laced); currently sl_2-only.
  3. Admissible-level Verlinde (Creutzig--Ridout 2013 pseudo-traces) — explicitly scoped OUT in the current proposition; open frontier for the logarithmic / non-rational extension.

