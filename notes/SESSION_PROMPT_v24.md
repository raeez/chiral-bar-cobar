> **Historical prompt note (March 13, 2026).**
> This file is retained for provenance and should not be treated as a live control document.
> Active doctrine is `notes/SESSION_PROMPT_v23.md` together with `notes/autonomous_state.md`, `notes/VISION.md`, `notes/PROGRAMMES.md`, and `chapters/connections/concordance.tex`.
> Current constitutional status: MC1/MC2 resolved on the printed loci; live frontier MC3/MC4; MC5 downstream; periodicity orthogonal.

# SESSION PROMPT v24 — Doctrinal Stabilization
# Launch: "Read notes/SESSION_PROMPT_v24.md and execute it."
# Supersedes: v23 (proof forge). References CLAUDE.md for invariants.
# Date: March 2026
# Trigger: raeeznotes21.md (external deep review)

> **Superseded doctrine note (March 13, 2026).**
> This prompt contains a historical pre-resolution MC2 routing frame and
> is retained for provenance. Active execution doctrine is
> `notes/SESSION_PROMPT_v23.md` under
> `chapters/connections/concordance.tex`
> (MC2 resolved; live frontier MC3/MC4; MC5 downstream; periodicity orthogonal).

---

## PERMANENT MANDATE

Treat the monograph as the definitive dimension-one treatise of modular
homotopy theory for factorization algebras on curves, not as a proved
core with an optional programme appendix.

Therefore every session should prefer work that materially builds one
of the load-bearing missing foundations: modular-operadic functoriality,
curved/coderived factorization on `Ran(X)`, the H-level bar-cobar
adjunction, the cyclic deformation complex `Def_cyc(A)`, the universal
Maurer-Cartan class `Theta_A`, and the shifted-symplectic/Lagrangian
package.

Status discipline remains absolute: these foundations are build targets
until proved, not licenses to overclaim.

---

## PHASE 0: GROUNDING (mandatory, before anything else)

Read these files IN THIS ORDER. Do not skip. Do not paraphrase from memory.

```
1. raeeznotes21.md                          — the external verdict
2. chapters/connections/concordance.tex     — the constitution (skim first 200 lines)
3. chapters/theory/introduction.tex:1020-1054  — the stale universal-resolution statement
4. appendices/nilpotent_completion.tex:119-260 — the frontier theorem cluster
5. appendices/existence_criteria.tex:1-40      — the comparison framing
6. chapters/theory/higher_genus.tex:83-130     — the differential convention (CLEAN)
7. chapters/theory/introduction.tex:1258-1295  — the existence regimes remark (CLEAN)
```

After reading, state in extended thinking: what is the ONE-SENTENCE doctrinal
shift that raeeznotes21 forces? (Answer: "The core is credible; the remaining
defects are localized stale statements and frontier overreach, not structural
flaws." If your reading yields a different one-sentence summary, trust your
reading over this hint.)

---

## PHASE 1: FIVE DOCTRINAL AXIOMS

These axioms are the decision procedure for ALL edits in this session.
Every change must be justified by exactly one axiom. If a proposed edit
cannot be justified, do not make it.

**D1 (Locus Discipline)**: Bar-cobar INVERSION (Omega(B-bar) ~> A) is
theorematic ONLY on the Koszul locus or in explicitly completed/coderived
regimes. CONSTRUCTIONS (B-bar, Omega) exist always. Any sentence that says
"Omega B-bar ~ id holds universally/without quadraticity" violates D1.

**D2 (Family Specificity)**: The resolved entry theorem (PBW concentration)
is a FAMILY-SPECIFIC package for affine KM, Virasoro, and principal
finite-type W. Proposition 8.17.23 is the MECHANISM (unique-weight-2 d_2),
not a universal unconditional upgrade. Any sentence that claims a single
universal all-families PBW theorem violates D2.

**D3 (Frontier Containment)**: Appendix O (nilpotent completion) is a
FRONTIER theorem package. Its theorems are valid under their stated
hypotheses (finite D_X-generation, polynomial growth, finite Hochschild,
E_2 degeneration), but those hypotheses are NOT the proved core. Any
theorem in Appendix O that reads as extending the proved core without
invoking its hypotheses violates D3. The fix is NOT to cut but to
REFRAME as frontier-conditional.

**D4 (Constitutional Supremacy)**: concordance.tex (Chapter 34) is the
normative ledger. When earlier chapters disagree, concordance is right.
The five-layer architecture (A_0/A_1/A_2, B, C_0/C_1, D_scal/D_Delta, H)
and the scalar/spectral/full modular package hierarchy are CANONICAL.
Any formulation that flattens this hierarchy violates D4.

**D5 (Theta Discipline)**: The full modular characteristic Theta_A is
CONJECTURAL (MC2 frontier). The scalar shadow kappa(A) is PROVED. The
spectral invariant Delta_A is PROVED but NOT determined by kappa alone.
Any sentence that speaks of Theta_A as theorematic violates D5.

---

## PHASE 2: STRIKE LIST — Systematic Audit

This is the main work of the session. For each strike category below,
GREP the full source tree, READ every hit, and record file:line for
each violation. Do not edit yet. Collect the complete list first.

### Strike Category S1: Universal bar-cobar quasi-isomorphism (D1 violation)

Search patterns (run ALL):
```
grep -rn "universal resolution" chapters/ appendices/ --include='*.tex'
grep -rn "without quadraticity" chapters/ appendices/ --include='*.tex'
grep -rn "every augmented" chapters/ appendices/ --include='*.tex'
grep -rn "Omega.*bar.*simeq.*id" chapters/ appendices/ --include='*.tex'
grep -rn "quasi-isomorphism.*always" chapters/ appendices/ --include='*.tex'
grep -rn "bar.*cobar.*universal" chapters/ appendices/ --include='*.tex'
```

**Known primary target**: introduction.tex:1031-1036 (item (ii) of
rem:three-koszul-mechanisms). This is the sharpest live contradiction
in the source. It must be REWRITTEN, not softened.

**Replacement doctrine for item (ii)**: "Bar and cobar are universal
CONSTRUCTIONS: every augmented chiral algebra admits a bar complex and
every conilpotent coalgebra admits a cobar algebra. The counit
Omega(B-bar(A)) -> A is a quasi-isomorphism on the Koszul locus
(Theorem B) and in completed/coderived regimes under additional
hypotheses (Appendix O). Off the locus, one has completed/coderived
persistence but NOT ordinary quasi-isomorphism."

### Strike Category S2: Universal PBW claims (D2 violation)

Search patterns:
```
grep -rn "PBW.*all.*famil" chapters/ appendices/ --include='*.tex'
grep -rn "PBW.*universal" chapters/ appendices/ --include='*.tex'
grep -rn "unconditional.*PBW" chapters/ appendices/ --include='*.tex'
grep -rn "Proposition.*8.17.23.*implies" chapters/ appendices/ --include='*.tex'
```

Each family-specific PBW theorem must EXPLICITLY cite the extra
family-specific closure argument beyond Prop 8.17.23.

### Strike Category S3: Appendix O overclaiming (D3 violation)

Targets: nilpotent_completion.tex:119-260. Three theorems:
- thm:completion-convergence (line 119)
- thm:completed-bar-cobar (line 172)
- thm:koszul-dual-characterization (line 215)

For each: verify that the proof is COMPLETE at the hard points:
1. Obstruction vanishing from polynomial growth (Step 3, line ~148)
2. Mittag-Leffler / lim^1 control (Step 4, line ~150)
3. Essential-image from E_2 degeneration (backward direction, line ~251)

If any proof compresses at a hard point, the fix is to:
- Keep the theorem statement
- Add a FRONTIER REMARK after the proof identifying the compressed step
- Change ClaimStatusProvedHere to ClaimStatusProvedHere ONLY if the
  proof is genuinely complete; otherwise change to ClaimStatusConjectured
  with a remark explaining what remains

### Strike Category S4: Theta_A spoken of as theorematic (D5 violation)

Search patterns:
```
grep -rn "Theta.*proved\|Theta.*theorem\|full.*modular.*characteristic.*proved" chapters/ appendices/ --include='*.tex'
grep -rn "Theta.*construct" chapters/frame/ --include='*.tex'
```

Special attention: heisenberg_frame.tex must preview Theta_A but never
claim it is constructed. The frame chapter's Remark at line ~33 already
does this correctly — verify it still does after edits.

### Strike Category S5: Existence criteria as legislative (D4 violation)

Verify that appendices/existence_criteria.tex ONLY operates as a
comparison appendix. Check that no sentence in it claims to ENLARGE
the proved core. The existing framing (rem:existence-comparison-role)
appears correct — confirm and record.

### Strike Category S6: Differential convention normalization (D4 — PROMOTE)

The convention at higher_genus.tex:83-119 is CANONICAL. Search for
any theorem elsewhere that uses d_g ambiguously (without specifying
whether it means d_fib, D_g, or d_0).

```
grep -rn '\\(d_g\\|d_{g}\\)' chapters/ appendices/ --include='*.tex'
grep -rn 'bar differential.*genus' chapters/ appendices/ --include='*.tex'
```

Any ambiguous d_g should be normalized to the convention.

### Strike Category S7: Yangian/W-infinity full-category overclaim (D3)

```
grep -rn "full.*category.*equivalence\|categorical.*Koszul.*duality" chapters/examples/yangians.tex --include='*.tex'
```

Keep evaluation-locus and chain-level statements. Flag any statement
that claims full-category DK beyond the evaluation-generated locus
without explicit hypotheses.

### Strike Category S8: Periodicity classification overclaim (D3)

```
grep -rn "classification.*periodicity\|periodicity.*theorem" chapters/theory/deformation_theory.tex --include='*.tex'
```

The periodicity package is an orthogonal weak flank, NOT a
classification theorem. Verify that local rhetoric does not
re-inflate the profile/criterion results.

---

## OUTPUT FORMAT FOR PHASE 2

After completing all searches, produce a numbered list:

```
STRIKE LIST
===========
[S1.1] introduction.tex:1031-1036 — "universal resolution" + "without quadraticity" (D1)
[S1.2] ...
[S2.1] ...
...
[S8.n] ...

ALREADY CLEAN (no violations found):
- S5: existence_criteria.tex correctly framed
- ...
```

Do not proceed to Phase 3 until the complete strike list is recorded.

---

## PHASE 3: SURGICAL REPAIR

Execute the strike list. Rules:

1. **One strike at a time**. Do not batch.
2. **Read before writing**. For every edit, first read 50 lines of
   context around the target.
3. **Minimal diff**. Change only the violating language. Do not
   rewrite surrounding paragraphs. Do not add new content.
4. **Compile gate**: After every 5 edits, run:
   `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast`
   If build fails, fix the break before continuing.
5. **Doctrinal justification**: For each edit, state which axiom
   (D1-D5) it serves.
6. **Concordance update**: If any edit changes a claim status
   (ProvedHere -> Conjectured, or vice versa), update concordance.tex
   to match. The constitution must never be stale.

### Repair templates

**For S1 (D1 violations)**: Replace universal-resolution language with
"constructions are universal; inversion is theorematic on the Koszul
locus or under completed/coderived hypotheses."

**For S2 (D2 violations)**: Add explicit family citation:
"Theorem X (proved for affine KM by [ref], for Virasoro by [ref],
for principal W by [ref]) via the common d_2 mechanism of Prop 8.17.23
together with the family-specific closure argument of [ref]."

**For S3 (D3 violations)**: Add frontier remark after the proof:
"\begin{remark}[Frontier status] The preceding proof depends on [specific
hypothesis]. This places the result in the completion frontier regime of
Remark~\ref{rem:existence-regimes}(ii), not in the strict finite-type
core. The missing verification is [specific step].\end{remark}"

**For S5/S7/S8 (D3/D4 violations)**: Downgrade rhetoric, not content.
Change "we have shown" to "under the hypotheses of Theorem X",
"this establishes" to "this establishes on the [named] locus", etc.

---

## PHASE 4: CONSEQUENCE PROPAGATION

After all strikes are executed, the source is in a new doctrinal state.
Now ask: WHAT DOES THE REPAIRED ARCHITECTURE IMPLY?

### 4A. Positive consequences (what becomes clearer/stronger)

The repaired source now has:
- A clean construction/inversion split everywhere
- Family-specific PBW with explicit closure arguments
- A properly contained frontier

This STRENGTHENS the core: the theorems that survive the audit are
now unimpeachable. Look for places where the cleaned-up doctrine
lets you:
1. State a sharper theorem (e.g., "on the Koszul locus" is more
   precise than "under completeness hypotheses")
2. Tighten a proof (the correct hypotheses may simplify an argument)
3. Add a one-line corollary that was obscured by the old vagueness

### 4B. Frontier crystallization

With Appendix O properly contained, the EXACT gap between proved core
and frontier becomes visible. Document this in concordance.tex as a
new remark:

"The completion frontier (Appendix O) extends the strict core under
three explicit hypotheses: [H1], [H2], [H3]. Of these, [H1] is
verified for all Master Table families, [H2] is verified for finite-type
families, and [H3] is the open lemma."

### 4C. Next-session targets

After the repair, what is the FIRST thing the next session should do?
Record this in autonomous_state.md. Likely answers:
- MC2 cyclic L-infinity model (if the frontier is now clean enough
  to build on)
- Appendix O proof expansion (if the frontier remark exposed a
  specific lemma that can be proved)
- Theorem A proof-density pass (raeeznotes21 says "keep but tighten")

---

## PHASE 5: VERIFY AND CLOSE

1. Full build: `make` (multi-pass)
2. Fresh census: compare with Mar 10 baseline (PH 888, PE 344, CJ 163, HE 31, Open 4)
3. If census changed: record the change and justify it
4. Tests: `cd compute && .venv/bin/python -m pytest tests/ -q`
5. Update autonomous_state.md with session results
6. Update MEMORY.md ONLY if a new verified fact was discovered
   (not for session-specific state)

---

## ANTI-PATTERNS — Specific to this session

| # | Anti-pattern | Signal | Why it fails |
|---|-------------|--------|--------------|
| A1 | Rewriting Appendix O | "Let me rewrite the completion theorems..." | raeeznotes21 says DO NOT CUT. Reframe, don't rewrite. |
| A2 | Adding new content during repair | "While fixing this, I should also prove..." | Phase 3 is REPAIR ONLY. New content belongs in Phase 4. |
| A3 | Softening instead of replacing | Changing "universal" to "essentially universal" | D1 requires a clean construction/inversion split. Hedging is not repair. |
| A4 | Editing concordance without reading it | Updating the constitution from memory | ALWAYS re-read concordance.tex before touching it. |
| A5 | Skipping the compile gate | "I'll compile at the end" | Each 5-edit batch must compile. Non-negotiable. |
| A6 | Grepping one pattern when eight exist | Running only the first S1 grep | EVERY grep pattern in Phase 2 must be run. Partial audits are worse than none. |
| A7 | Claiming repairs are "done" before Phase 5 | "All strikes executed" without build verification | The session is not done until make succeeds and census is verified. |
| A8 | Diffuse exploration of "implications" | Spending all time in Phase 4 discovering new corollaries | Phase 4 is capped: 3 positive consequences, 1 frontier remark, 1 next-session note. No more. |
| A9 | Editing the wrong d_g | Normalizing d_fib to D_g or vice versa | Read higher_genus.tex:83-119 before EVERY S6 edit to confirm which differential is meant. |
| A10 | Treating raeeznotes21 as infallible | Accepting every claim without checking source | raeeznotes21 is an EXTERNAL review. Verify each claim against the actual source before acting. |

---

## TIME BUDGET

| Phase | Fraction | Gate |
|-------|----------|------|
| 0 (Grounding) | 10% | All 7 files read |
| 1 (Axioms) | 5% | Axioms stated in thinking |
| 2 (Strike list) | 30% | Complete numbered list produced |
| 3 (Repair) | 35% | All strikes executed, compiles clean |
| 4 (Consequences) | 15% | 3+1+1 items recorded |
| 5 (Verify) | 5% | Build + census + state update |

If at any point you are unsure whether an edit is correct, STOP and
state the uncertainty. A skipped strike is better than a wrong edit.
The dual imperative (CLAUDE.md): precision enables ambition.
