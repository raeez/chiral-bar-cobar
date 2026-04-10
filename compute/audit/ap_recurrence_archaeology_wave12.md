# AP Recurrence Archaeology — Wave 12

Date: 2026-04-09
Scope: Vol I (~/chiral-bar-cobar), Vol II (~/chiral-bar-cobar-vol2), Vol III (~/calabi-yau-quantum-groups).
Mode: READ-ONLY. No manuscript .tex or .md modified. No builds or tests run. Only this report written.

Purpose: Identify anti-patterns that have recurred across Waves 1A-11 despite already being catalogued in CLAUDE.md, diagnose why, and propose operationally enforceable rewrites for the next CLAUDE.md reconstitution.

---

## Section 1: Methodology

Sources consulted:

1. The three CLAUDE.md files (Vol I canonical + Vol II/III volume-specific):
   - /Users/raeez/chiral-bar-cobar/CLAUDE.md (~380 lines; AP1-AP141 plus AAP1-18 plus RS3-RS19).
   - /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md (V2-AP1-35 volume-specific).
   - /Users/raeez/calabi-yau-quantum-groups/CLAUDE.md (AP-CY1-19 volume-specific).

2. Audit reports in /Users/raeez/chiral-bar-cobar/compute/audit/*.md (>100 files). Headline reports analysed in detail:
   - ap5_cross_volume_report_wave6.md (Wave 6 cross-volume AP5 sweep)
   - ap5_post_wave7_verification.md (Wave 6 -> Wave 7 delta + residuals)
   - beilinson_audit_vol1_overture_wave11.md (Wave 11 deep audit of heisenberg_frame.tex)
   - exhaustive_gap_analysis_2026_04_08.md (all three volumes, all scales)
   - dnp_kz_gz_deep_beilinson_audit_2026_04_07.md (citation/bibliographic audit)
   - deep_beilinson_rectification_2026_04_07.md (compute engine audit)
   - platonic_ideal_heatmap_2026_04_08.md (196-agent session census)
   - session_summary_2026_04_07_08.md, session_state_2026_04_01_final.md, frontier_results_2026_04_07.md
   - vol1_full_audit_2026_04_08/CATALOGUE.md, counts.json (structured audit data)

3. Git log on each volume for the most recent 200 commits (grep 'AP' for AP-tagged commits):
   - Vol I: 200 commits — AP1, AP9, AP39, AP50, AP74, AP77, AP106, AP111, AP116-AP128, AP129-AP141 explicitly named.
   - Vol II: 200 commits — AP4, AP19-AP26 (initial codification wave), AP32, AP33, AP40, AP44, AP48, AP49, AP125, AP126, V2-AP32-35.
   - Vol III: 200 commits — AP1, AP25, AP33, AP40, AP43, AP48, AP50, AP113, AP124-AP128.

Counting methodology: a violation "instance" is counted when the same AP is cited by name in a commit message OR flagged as a violation in an audit report, across files and commits. Where a single sweep commit fixes 30+ instances, that is counted as "one recurrence event" (i.e. one wave in which the AP had to be rectified en masse), not 30. The recurrence count is the number of distinct WAVES / distinct sessions in which the AP was the target of repair work. This avoids double-counting the same AP for the same rewrite.

Terminology: "Wave" refers to a dated rectification session (Wave 1A-11 inclusive of CG rectification sweeps, Beilinson audits, cross-volume AP5 propagations). The last ~100 agent invocations span roughly Wave 5 (2026-04-01) through Wave 11 (2026-04-09).

---

## Section 2: Top 15 Repeat Offenders

Count = distinct waves / rectification events in which the AP was the object of repair. Raw violation counts (instances fixed) are in the second column.

| Rank | AP | Title | Waves | Raw instances fixed (aggregate) |
|-----:|----|-------|------:|--------------------------------:|
| 1 | AP126 | Level-stripped r-matrix (Omega/z vs k*Omega/z) | 6 | ~90+ |
| 2 | AP40 | Environment-tag mismatch (conjecture in theorem env) | 5 | ~70+ |
| 3 | AP32 | Uniform-weight vs multi-weight tag on F_g = kappa*lambda_g | 4 | ~30+ |
| 4 | AP1  | Distinct kappa per family (KM/Vir/W_N/Heis) | 4 | ~15 |
| 5 | AP125 | Label prefix must match environment (thm: vs conj: vs rem:) | 3 | ~20 |
| 6 | AP10 | Hardcoded expected value without independent derivation | 3 | ~12 engines |
| 7 | AP48 | Monster kappa(V^natural) unqualified | 3 | ~6 |
| 8 | AP44 | Divided-power vs OPE mode convention (c/12 vs c/2) | 3 | ~15 |
| 9 | AP113 | Bare kappa in Vol III (no subscript) | 3 | ~165 baseline |
| 10 | AP4 | \begin{proof} after non-theorem environment | 3 | ~40 (incl. 25+11 commits) |
| 11 | AP124 | Duplicate \label across files/volumes | 3 | ~5 live + ~30 dead-code |
| 12 | AP9 | Symbol collision (rho, s, etc. reused for unrelated objects) | 3 | ~5 |
| 13 | AP33 | Koszul dual != Feigin-Frenkel != negative level | 3 | ~10 |
| 14 | AP25/AP34/AP50 | Three/four-functor conflation (bar / Verdier / cobar / Z^der) | 3 | ~15 |
| 15 | AP29/V2-AP29 | AI-slop prose (moreover/crucially/notably/em-dashes) | 4 | 40+ (three separate "zero tolerance" commits) |

Notes:
- AP126 is the single most recurrent: first codified in wave of 12 instances, then found 30 more in Vol I Wave 5, then ~70 in Vol II + Vol III in Wave 6, residuals in Wave 7, still not clean by Wave 11 (residuals in heisenberg_frame.tex were NOT present but the main preface had to be fixed in Wave 7, and ordered_associative_chiral_kd_core.tex still had 4 residuals post-Wave 7). The anti-pattern literally earned its own AP (AP141 "AP126 is systemic") confessing this failure.
- AP29 / V2-AP29 (AI slop) required at least three "zero tolerance" cleanup commits in Vol II alone (prose fortification waves) and is explicitly called out in V2-AP29 as "Three separate cleanup commits prove aspirational instructions insufficient."
- AP10 is confounded with AP128 (engine-test synchronized to same wrong value): both are about hardcoded expected values without independent verification, and AP128 was added specifically because AP10 kept recurring.

---

## Section 3: Root-Cause Analysis

### 3.1 AP126 — Level-stripped r-matrix

Rule (current): "Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. After writing ANY r-matrix, verify k=0 -> r=0."

Root causes:
(a) BOTH Omega/z and k*Omega/z are valid formulas in different contexts. Omega/z is the Drinfeld CYBE r-matrix for the rational classical Yang-Baxter equation (level-absorbed normalization). k*Omega/z is the affine KM bar-complex r-matrix. Agents pattern-match on the SYMBOL r(z)=Omega/z because that is the famous formula in the integrable-systems literature.
(b) The "k=0 vanishing test" only fires if the agent is already aware of AP126 and checks before writing. It is a POST-WRITE check but 99% of the time the first draft is accepted as-is.
(c) The rule does not specify WHICH CONTEXT requires k*. The rule says "after writing any r-matrix" but does not distinguish rational Yangian contexts (where Omega/z is fine) from affine KM bar-complex contexts (where it is wrong). Agents reading the rule then have plausible deniability: "this is a Yangian r-matrix, not a KM one."
(d) In Vol II ordered_associative_chiral_kd_core.tex, the expansion R(z) = 1 + Omega/z + O(z^{-2}) is the Yang rational R-matrix at level 1, where k=1 has been specialized but not made visible. This is a "context collapse" case the rule does not address.

Why rule wording fails: the current AP126 is an observation + verification heuristic, not an if-context-then-form template.

### 3.2 AP40 — Environment-tag mismatch

Rule (current): "Environment MUST match tag. Conjectured -> \begin{conjecture}. ProvedElsewhere -> theorem + Remark attribution."

Root causes:
(a) LaTeX environment choice is the FIRST thing an agent writes when drafting. Status-tagging is an AFTERTHOUGHT — agents write \begin{theorem}...\ClaimStatusProvedHere out of muscle memory, then downgrade to Conjectured when the audit comes. But the environment stays \begin{theorem}.
(b) The default environment across the manuscript is \begin{theorem}, and Vol III's CLAUDE.md explicitly says "DEFAULT in Vol III is \begin{conjecture}", yet the LLM ignores this because \begin{theorem} feels like the "proper" mathematical writing posture.
(c) AP4 (related) forbids \begin{proof} after a non-theorem environment; but agents routinely append \begin{proof} blocks because "a mathematical result should have a proof" is more ingrained than "only theorems get proofs."
(d) The V2 commits show EIGHT separate AP40 downgrade commits in rapid succession (3fc4101, 6dd1a40, 7030e1b, 543f242, 8a7747e...), which indicates not a one-time mass-fix but an ongoing bleed from new content being written in the wrong environment.

Why rule wording fails: AP40 says "must match" but does not provide a WRITE-TIME decision tree ("before writing \begin{, STOP: is the proof complete? If no -> conjecture"). V2-AP31 got closer with "AP4 at write time" but still only covers the proof-block case.

### 3.3 AP32 — Uniform-weight tag on F_g formulas

Rule (current, bolded): "Every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation."

Root causes:
(a) The rule says "in a theorem" — but most violations were in prose and remarks, not theorem environments. The Wave 6 report found ~15 tagged, ~6 untagged in Vol I; the strict reading of the rule exonerates the prose occurrences. Agents exploit the "in a theorem" loophole.
(b) The formula F_g = kappa * lambda_g^FP is the SIMPLEST and most visual form of the genus tower — it reads as "the answer", and tags feel like they clutter the punchline. Agents write the formula as theorem-statement prose and reach for prose-justification of scope rather than an inline parenthetical.
(c) In Vol III toroidal_elliptic.tex, the prose says "proved at genus 1; at g>=2 the multi-weight genus expansion may receive cross-channel corrections (Vol I, AP32)" — this is RULE-COMPLIANT in spirit (scope is clarified) but VIOLATION-FLAGGING on the strict "tag within 5 lines" reading. The rule's enforcement definition is ambiguous.
(d) AP139 (unbound variable in theorem) and AP118 (matrix vs scalar collapse) are adjacent failure modes that share the same root cause: the formula LOOKS simple, the simplicity obscures the scope.

Why rule wording fails: "every occurrence" + "in a theorem" + "must carry explicit tag" is three independently-quantified conditions and agents arbitrage the ambiguity.

### 3.4 AP1 — kappa per family

Rule (current): "kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. kappa(Heis)=k. ... AP1 operational mandate: before writing ANY kappa formula, (a) read landscape_census.tex for that family, (b) evaluate at k=0 and k=-h^v, (c) cross-check compute/."

Root causes:
(a) There are four DIFFERENT formulas and the agent has to pick the right one. The formulas LOOK SIMILAR (all linear in level/central-charge) and agents interpolate between them.
(b) The "operational mandate" tells the agent to read landscape_census.tex, but Wave-7 agents were still writing from memory — the mandate is not enforceable because there is no write-gate.
(c) The Wave-5 Vol II commit "9bd9e07 Fix Heisenberg kappa: k/2 -> k (AP1 rectification from Vol I audit)" shows that the Heisenberg kappa was wrong in Vol II long after being correct in Vol I. The cross-volume propagation of AP1 fixes is itself an AP5 failure.
(d) AP136 (H_{N-1} != H_N - 1) is a sub-case that bit CLAUDE.md itself — the canonical reference file had the wrong W_N formula for an extended period.

Why rule wording fails: the mandate is a PROCEDURE agents are asked to follow, not a TEMPLATE the rule provides. The agent still has to look up the answer.

### 3.5 AP125 — Label prefix must match environment

Rule (current): "\begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures."

Root causes:
(a) Renaming a label means touching every \ref in every volume. The atomic-rename requirement is intentionally expensive, so agents take shortcuts.
(b) When AP40 forces a downgrade from theorem to conjecture, AP125 requires the label to move from thm: to conj:, but the agent doing the AP40 fix is often a different agent from the one responsible for AP125 propagation. The responsibility slips through.
(c) The rule provides no grep command to find mismatches (though Vol II ht_physical_origins.tex had 4 instances found by "multi-line grep for \begin{theorem} within 3 lines of \label{rem:...}" — which IS a concrete check but not in the rule text).

Why rule wording fails: the rule says "when upgrading/downgrading, rename ... atomically" but does not say HOW to find all the references. The agent does not have a tool; they have a commandment.

### 3.6 AP10 / AP128 — Hardcoded expected values, engine-test same wrong model

Rule (current): "every hardcoded expected value MUST have a comment citing 2+ independent derivation paths" + AP128: "when correcting a compute engine formula, NEVER update test expectations from engine output."

Root causes:
(a) Writing an engine AND its tests in the same session from the same mental model is the default workflow. Tests are verification-by-echo of what the engine already computes.
(b) The rule says "2+ independent derivation paths" but the agent writing the test HAS only one derivation path (their own code). They write a plausible comment citing "direct computation, cross-check" without actually having a second path.
(c) AP128 explicitly names the "same-wrong-model" failure mode, but AP128 is a POST-HOC flag on a corrected engine. There is no WRITE-TIME requirement to check: "is my expected value from an independent source?"
(d) Deep_beilinson_rectification_2026_04_07 found the Stokes engine F1-F4 all had this exact structure: the engine computed wrong, the test confirmed wrong, no alternative path existed.

Why rule wording fails: there is no forcing function. Saying "must have 2+ paths" without requiring the paths to be literally cited in comments with file references is aspirational.

### 3.7 AP113 — Bare kappa in Vol III

Rule (current): "Bare 'kappa' is FORBIDDEN in Vol III. A CY manifold gives rise to MULTIPLE chiral algebraizations, each with its own kappa. ALWAYS subscript: kappa_ch, kappa_BKM, kappa_cat, kappa_fiber."

Root causes:
(a) ~165 bare instances remained after the first AP113 pass (Wave 7 baseline). Most are in formulas like "F_g = kappa * lambda_g^FP" where the surrounding paragraph already defines which kappa is meant.
(b) The rule does not provide a "local-definition grandfather clause" ("let kappa := kappa_ch in this section"). Without this, agents either clutter every formula with a subscript or ignore the rule entirely.
(c) The subscript choice itself is ambiguous: kappa_ch vs kappa_cat differ by functoriality direction, and most agents cannot tell which is meant when they encounter the bare symbol mid-paragraph. The rule gives the subscripts but not the decision tree for picking one.

Why rule wording fails: the ban is maximalist and unenforceable; in practice agents either vandalize prose with subscripts or skip the rule.

### 3.8 AP124 — Duplicate labels across files/volumes

Rule (current): "Before creating ANY \label{foo}, grep the entire manuscript. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates."

Root causes:
(a) Parallel agents creating labels in different chapters naturally collide on natural names (conj:kappa-bps-universality was independently created in Vol I AND Vol III).
(b) The grep command is provided but agents do not actually run it — they proceed on the assumption that their label is unique because they have not seen it before.
(c) Dead-code chapters (appendices/ordered_associative_chiral_kd.tex is a dead copy of chapters/theory/ordered_associative_chiral_kd.tex) host 30+ duplicate labels that LaTeX silently accepts because the file is not \input{}'d. Agents cannot distinguish live from dead code without the build system.

Why rule wording fails: the grep is a recommendation, not a precondition. There is no agent-executed pre-write gate.

### 3.9 AP44 — Divided-power convention

Rule (current, in V2-AP34 expansion): "Vol II uses {T_lambda T} = (c/12)*lambda^3 (divided power). OPE mode T_{(3)}T = c/2 maps to (c/2)/3! = c/12. EVERY lambda-bracket MUST use divided powers. Grep for c/2.*lambda^3 — if found, almost certainly wrong (should be c/12)."

Root causes:
(a) Vol I uses OPE modes, Vol II uses lambda-brackets. The SAME formula c/2 vs c/12 has different meanings in the two volumes. Agents cross-copying content between volumes paste without converting.
(b) The 1/3! factor comes from a convention agents may not hold in working memory (divided-power structure of the lambda-bracket in coderivations).
(c) AP22 (divided-power) and AP44 (divided-power) and V2-AP34 (divided-power) all reference the same underlying failure mode but in different contexts, and the agent encountering one may not know to look for the other two.

Why rule wording fails: this is a genuine CONVENTION MISMATCH (a cross-volume divide), and the rule treats it as a "just use divided powers" directive without acknowledging that Vol I deliberately uses OPE modes for good reasons.

### 3.10 AP48 — Monster kappa(V^natural)

Root causes:
(a) The Monster VOA V^natural is orbifold-constructed. Its kappa is not well-defined in the standard sense because the orbifold procedure does not commute with the kappa computation without additional data.
(b) The ORIGINAL rule just said "kappa(V^natural) is open" — but agents reading "kappa(V^natural) = 24" in the pre-rule prose kept restoring the number.
(c) The "orbifold estimate" qualifier is the RESOLUTION but agents encountering "24" in a paper or compute output lack the context to add the qualifier.

Why rule wording fails: the rule asserts a negative ("not well-defined without qualifier") but does not give the positive form agents should write.

### 3.11 AP4 / V2-AP31 — Proof-after-conjecture

Rule (current): "Before writing \begin{proof}, verify preceding environment is theorem/prop/lemma with ProvedHere. If conjecture: use \begin{remark}[Evidence] instead. 25-instance fix commit proves post-hoc enforcement is expensive."

Root causes: same as AP40. Agents reach for \begin{proof} as a structural instinct. The rule was added AT WRITE TIME but still requires the agent to remember to check.

### 3.12 AP9 / Symbol collision

Root causes: rho is used for affine half-sum, representation, modular parameter, density function. Agents mint new uses without checking existing ones. The "grep first" discipline is not codified.

### 3.13 AP33 — Koszul dual != Feigin-Frenkel != negative level

Root causes: three distinct dualities (Koszul dual of operad, Feigin-Frenkel dual of W-algebra, negative-level dual) are conflated because they all involve "dual" and "level" and produce "similar" invariants. The rule distinguishes them but agents recombine them under pressure.

### 3.14 AP25 / AP34 / AP50 — Four-functor conflation

Root causes: B(A), D_Ran(B(A)) = B(A!), Omega(B(A)), Z^der_ch(A) are FOUR distinct objects. The rule lists them clearly, but agents write "bar-cobar produces bulk" or "Koszul dual equals bar complex" as casual prose shorthand. These shortcuts violate the four-object discipline.

### 3.15 AP29 / V2-AP29 — AI slop

Rule (current): "No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (3) No em dashes; use colons, semicolons, or separate sentences."

Root causes:
(a) LLM training data heavily weights these words. They are the default prose posture.
(b) Multiple cleanup passes prove that single-session discipline does not survive the next session's prose generation. The model regenerates slop every time it writes new content.
(c) Em dashes are a symptom of the same training bias.

Why rule wording fails: the rule is a ban list. It is enforceable by grep, and Vol II has a hook for it, but new content continuously reintroduces the bans. There is no PRE-GENERATION discipline.

---

## Section 4: Proposed Rewrites for CLAUDE.md Reconstitution

Each rewrite converts an abstract rule into an operational template with a concrete write-time gate. The format is: name, current (implicit), proposed.

### Rewrite 4.1: AP126 -> template-driven r-matrix writing

**Proposed wording:**

```
AP126 (TEMPLATE). When writing any r-matrix, FIRST identify the context:
  (A) Affine KM bar complex: r(z) = k * Omega / z
  (B) Drinfeld rational classical Yangian: r(z) = Omega / (z - w), level absorbed into hbar
  (C) Yang rational R-matrix (R = 1 + ...): R(z) = 1 + (k * Omega) / z + O(z^{-2}); write the k explicitly
  (D) Elliptic Calogero-Moser: r(z, tau) = zeta(z) * Omega + ...
  (E) Collision residue (arity-2 kappa): residue_{z=0} r(z) = kappa(family)
After writing, VERIFY: at k = 0, does r vanish? For contexts A and C, YES. If not, STOP: you have used the wrong form.
WHEN IN DOUBT, EXPAND: write "r(z) = k * Omega / z (affine KM convention; at k=0 this vanishes)."
Greppable invariant: no occurrence of `\Omega/z` without either `k\,` or `\kappa_` prefix or a k=0 verification comment on the same or preceding line.
```

Enforcement: a hook that greps for bare `\Omega/z` and rejects any without a prefix OR an AP126-verified comment.

### Rewrite 4.2: AP40 -> environment decision tree

**Proposed wording:**

```
AP40 (DECISION TREE). Before writing \begin{theorem|proposition|lemma|conjecture}, answer in order:
  Q1: Is there a complete proof in the manuscript (ProvedHere) or in cited literature (ProvedElsewhere)?
      If NO -> use \begin{conjecture} + \ClaimStatusConjectured. STOP.
      If YES -> proceed to Q2.
  Q2: Is the result part of the main-theorem backbone or a supporting statement?
      Main -> \begin{theorem}.
      Supporting -> \begin{proposition}.
      Auxiliary -> \begin{lemma}.
  Q3: Is the proof self-contained or a citation?
      Self-contained -> \ClaimStatusProvedHere + \begin{proof} ... \end{proof}.
      Cited -> \ClaimStatusProvedElsewhere + Remark[Attribution].
If any answer is uncertain, DEFAULT to \begin{conjecture}. Downgrade is easier than downgrade-and-rename.

VOLUME DEFAULTS: Vol I and II default \begin{theorem} if Q1 = YES; Vol III defaults \begin{conjecture} regardless.
LABEL PROPAGATION (AP125): the label prefix is chosen by the environment, not the content. conj: thm: prop: lem:.

Greppable invariant: no \begin{proof} within 20 lines after \begin{conjecture}. Hook: scan every new \begin{theorem} for an accompanying \ClaimStatus tag within 3 lines.
```

### Rewrite 4.3: AP32 -> mandatory scope tag for every F_g

**Proposed wording:**

```
AP32 (SCOPE TAG). Every formula of the form "F_g = ... lambda_g ..." or "obs_g = ... " MUST be followed within the same sentence by ONE of:
  (a) (UNIFORM-WEIGHT)
  (b) (ALL-WEIGHT, with cross-channel correction delta F_g^{cross})
  (c) (g=1 only; ALL-WEIGHT at g=1 is unconditional)
  (d) (LOCAL: scope defined in surrounding paragraph, see ref:...)

No "in a theorem" loophole: the tag is required in ALL environments including prose, remarks, and definitions. Prose-based scope qualifications (e.g. "proved at genus 1; at g>=2 ...") do NOT substitute for the parenthetical tag — they complement it.

WRITE-TIME GATE: if you are about to write "F_g = kappa ..." or "obs_g = ...", STOP and append one of the four tags in the same breath.

Greppable invariant: grep for `F_g.*\\kappa.*\\lambda_g` and `obs_g.*\\kappa.*` — every match must have one of the four tags on the same or next line.
```

### Rewrite 4.4: AP1 -> landscape census citation requirement

**Proposed wording:**

```
AP1 (CITATION). Writing a kappa formula from memory is FORBIDDEN. Before writing ANY kappa expression:
  Step 1: Identify the family (KM, Vir, Heis, W_N, free, coset, SVir, BP, betagamma).
  Step 2: Open chapters/examples/landscape_census.tex and copy the formula, INCLUDING the citation comment.
  Step 3: Paste with a comment: `% AP1: formula from landscape_census.tex:LINE; k=0 -> VALUE verified`
  Step 4: Evaluate at least TWO boundary values (k=0, k=-h^vee, c=1, c=13) and write the results in a comment.

Formulas for quick reference (all MUST be cross-checked against landscape_census.tex before use):
  KM: kappa(V_k(g)) = dim(g)(k+h^vee)/(2h^vee); at k=0, kappa = dim(g)/2; at k=-h^vee, kappa=0 (critical).
  Virasoro: kappa(Vir_c) = c/2; at c=0, kappa=0; at c=13, kappa=13/2 (self-dual).
  Heisenberg: kappa(H_k) = k; at k=0, kappa=0.
  W_N: kappa(W_N) = c*(H_N - 1) where H_N = 1 + 1/2 + ... + 1/N (NOT H_{N-1}). Verify: at N=2, H_2=3/2, H_2-1=1/2, so kappa(W_2)=c/2, matching Virasoro.

Greppable invariant: every kappa formula in a .tex file must be within 5 lines of a `% AP1` comment citing landscape_census.tex.
```

### Rewrite 4.5: AP125 + AP124 -> atomic label management

**Proposed wording:**

```
AP124/AP125 (ATOMIC). Every new \label{foo} must satisfy BOTH:
  (i) Prefix matches environment: thm: theorem, prop: proposition, lem: lemma, conj: conjecture, rem: remark, def: definition, eq: equation, fig: figure, tab: table, sec: section.
  (ii) Uniqueness verified by grep across ALL THREE volumes before writing.

PRE-WRITE CHECK: before writing \label{foo}, run (as the agent's first tool call):
  grep -rn '\\label{foo}' ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups
If 0 matches -> safe to write. If >=1 matches -> rename to foo-v1-theme-unique.

DOWNGRADE ATOMICITY: when downgrading a theorem to a conjecture (AP40):
  1. Rename thm:foo -> conj:foo in the same commit.
  2. grep -rn 'ref{thm:foo}' across all three volumes; update each to ref{conj:foo}.
  3. grep -rn 'ref{thm:foo}' ONE MORE TIME to verify zero matches.
  4. Do not commit until step 3 returns zero.

Greppable invariant: zero `\begin{theorem}` or `\begin{conjecture}` within 3 lines of a label whose prefix does not match.
```

### Rewrite 4.6: AP10 / AP128 -> independent verification path ledger

**Proposed wording:**

```
AP10 (VERIFICATION LEDGER). Every hardcoded expected value in a test file must be accompanied by a `# VERIFIED` comment block citing AT LEAST TWO sources, each from a DIFFERENT category:
  [DC] direct computation (algebraic/symbolic, distinct from the engine under test)
  [LT] literature (paper + equation number + convention statement)
  [LC] limiting case (e.g. k=0, c->infty)
  [SY] symmetry (e.g. CFT cross-ratio relation)
  [CF] cross-family (same value appears in a different family for a stated reason)
  [NE] numerical evaluation with >= 10 digits
  [DA] dimensional analysis

The comment MUST name the two categories and cite the file/paper/line.

AP128 (ENGINE-TEST SYNC). When correcting a compute engine formula, the corresponding test expected value MUST NOT be recomputed from the corrected engine. Instead:
  1. Derive the correct expected value from an INDEPENDENT source (one of [DC, LT, LC, SY, CF, NE, DA] NOT equal to the engine's own computation).
  2. Update the test expected value from that source.
  3. Update the comment block to cite the independent source by name and date.
  4. Only THEN run the engine and verify it matches the independent source.

Greppable invariant: every `assert.*==` or `assert.*approx` in a test file must be within 10 lines of a `# VERIFIED [CAT1][CAT2]` comment.
```

### Rewrite 4.7: AP113 -> local-definition grandfather clause

**Proposed wording:**

```
AP113 (LOCAL DEFINITION). Bare `\kappa` in Vol III is permitted IFF the section/subsection begins with a LOCAL DEFINITION of the form:
  "In this section we write $\kappa$ for $\kappa_{\mathrm{ch}}(\cH_\Lambda)$ (respectively $\kappa_{\mathrm{BKM}}$, $\kappa_{\mathrm{cat}}$, $\kappa_{\mathrm{fiber}}$)."
and the formulas within the section are unambiguous given this definition.

In prose OUTSIDE such a section, bare `\kappa` is FORBIDDEN; use the subscripted form.

Decision tree for picking the subscript:
  kappa_ch: computed from A_C via the CY-to-chiral functor (Vol III Thm CY-A).
  kappa_BKM: computed from a Borcherds-Kac-Moody algebra (e.g. Delta_5 weight for K3 x E).
  kappa_cat: computed from the categorical / holomorphic Euler characteristic of the CY.
  kappa_fiber: computed from the lattice rank / fiber structure.
If the kappa comes from a CHIRAL ALGEBRA, it is kappa_ch. If from a BKM ALGEBRA, it is kappa_BKM. If from an EULER CHAR, it is kappa_cat. If from a LATTICE, it is kappa_fiber.

Greppable invariant: every `\kappa` in Vol III must be either (a) followed by `_{ch|BKM|cat|fiber}`, (b) within a section that begins with a local definition statement.
```

### Rewrite 4.8: AP29 / V2-AP29 -> pre-write and post-write slop gate

**Proposed wording:**

```
AP29 (GATED PROSE). Before committing any new .tex prose, run a two-pass slop gate:
  PRE-WRITE: mentally check: does the sentence start with "Moreover", "Additionally", "Notably", "Crucially", "Remarkably", "Interestingly", "Furthermore", "We now", "It is worth noting"? If yes, REWRITE before typing.
  POST-WRITE: grep the file for the banned list. grep for `---` (em-dash). If any match, rewrite.

Banned list (exact tokens, case-insensitive):
  moreover, additionally, notably, crucially, remarkably, interestingly, furthermore, "we now", "it is worth noting", "worth mentioning", "it should be noted", "it is important to note", delve, leverage, tapestry, cornerstone, landscape (as metaphor), journey, navigate (non-geometric).

Em-dash: `---` and `—` are banned. Use colons, semicolons, or separate sentences.

Hedging ban: no "arguably", "perhaps", "seems to", "appears to" in a mathematical statement. If the math is clear, state it. If the math is not clear, mark as conjecture.

Enforcement: a hook runs the grep list on every .tex write. Non-zero match = reject write.
```

### Rewrite 4.9: AP44 -> convention-conversion template

**Proposed wording:**

```
AP44 (CONVERSION). When copying a formula between volumes:
  Vol I uses OPE modes: T_{(3)}T = c/2 means the T_3 mode acting on T gives c/2.
  Vol II uses lambda-brackets with divided powers: {T_lambda T} = (c/12) lambda^3 because (c/2) / 3! = c/12.
  Vol III uses motivic/CY: kappa appears as a spectrum, not a single value.

CONVERSION TABLE (OPE -> lambda-bracket):
  T_{(3)}T = c/2     -> {T_lambda T} = (c/12) lambda^3
  W_{(5)}W = c/3     -> {W_lambda W} = (c/360) lambda^5
  General: A_{(n)}B = k -> {A_lambda B} contains (k/n!) lambda^n

WHEN TO USE WHICH:
  Writing in Vol I -> OPE modes.
  Writing in Vol II -> lambda-brackets with divided powers.
  Writing in Vol III -> subscripted kappa + CY context.

Cross-volume paste rule: NEVER paste a formula between volumes without first converting to the target convention. Write a comment: `% AP44 conversion: source Vol I OPE mode, target Vol II lambda-bracket, divided by 3!`.

Greppable invariant: in Vol II, no occurrence of `c/2.*lambda^3`; no occurrence of `c/3.*lambda^5`. In Vol I, no occurrence of `c/12.*lambda^3` (would be a Vol II formula).
```

### Rewrite 4.10: AP4 / V2-AP31 -> proof-writing gate

**Proposed wording:**

```
AP4 (GATED PROOF). Before typing `\begin{proof}`:
  Step 1: Look at the nearest preceding `\begin{...}` environment within 30 lines.
  Step 2: If theorem/proposition/lemma: proof may follow. Continue.
     If conjecture/heuristic/remark/definition: STOP. Use `\begin{remark}[Evidence]` instead.
  Step 3: If theorem/proposition/lemma, check the ClaimStatus tag.
     ProvedHere: proof must be self-contained. Do NOT cite a paper and stop.
     ProvedElsewhere: proof body must be a paragraph attributing to the paper, NOT a re-proof.
     Conjectured/Heuristic: impossible — AP40 violation upstream.

Greppable invariant: every `\begin{proof}` must be within 30 lines after a `\begin{theorem|proposition|lemma}`.
```

### Rewrite 4.11: Four-functor discipline (AP25/AP34/AP50) -> named object list

**Proposed wording:**

```
AP25/AP34/AP50 (FOUR NAMED OBJECTS). Write the following list before any paragraph that mentions "bar", "cobar", "Koszul dual", or "derived center":

  % FOUR OBJECTS:
  % 1. B(A) = bar coalgebra = T^c(s^{-1} Abar) with deconcatenation + twisting term.
  % 2. A^i = H^*(B(A)) = dual coalgebra = Koszul-theoretic cohomology of bar.
  % 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual).
  % 4. Z^der_ch(A) = derived chiral center = Hochschild cochain complex = bulk.

FORBIDDEN CONFLATIONS:
  - "bar-cobar produces bulk" (wrong: bar-cobar inverts to A; bulk is Hochschild).
  - "Omega(B(A)) is the Koszul dual" (wrong: that's INVERSION; Koszul dual is A^!).
  - "the Koszul dual equals the bar complex" (wrong: bar is a coalgebra, dual is an algebra).
  - "D_Ran(B(A)) is the cobar complex" (wrong: D_Ran is Verdier duality; cobar is Omega).

When writing any of "Koszul dual", "bar-cobar", "derived center", "Hochschild", "Verdier", STOP and name WHICH object you mean by the list 1-4 above.
```

---

## Section 5: Opus 4.6 Failure-Mode Observations

Specific quirks of the Opus 4.6 model as observed in Wave 1A-11 agent behaviour:

### 5.1 Pattern completion over context checking

When the model sees `r(z) = ` in an affine KM context, it completes `Omega/z` because that is the famous formula in the literature — even when the surrounding prose explicitly mentions "level k". The model pattern-matches on the LOCAL tokens, not the GLOBAL context. This is the root cause of AP126 recurrence. Mitigation: force a local-variable substitution (rewrite 4.1 requires the agent to write `k*Omega/z` which has one extra token that breaks the pattern completion).

### 5.2 Environment defaulting to \begin{theorem}

The model's LaTeX prior is heavily weighted toward \begin{theorem} as the "serious math" environment. Given a neutral prompt ("state this result"), the model will choose theorem > proposition > conjecture even when the evidence is heuristic. AP40 recurrences all share this signature: the content was heuristic, the environment was theorem. Mitigation: rewrite 4.2 forces a "if proof complete?" gate and defaults UNCERTAIN to conjecture.

### 5.3 Prose slop regeneration between sessions

The model re-introduces "moreover/crucially/notably" and em-dashes in every new session regardless of the explicit ban in CLAUDE.md. The ban is processed at prompt-parsing time but the token probabilities remain biased. Mitigation: a post-write grep hook catches the slop BEFORE it lands in the .tex file. V2-AP29 notes "Three separate cleanup commits prove aspirational instructions insufficient" — agreed. The rule must be a hook, not an instruction.

### 5.4 Memory-based formula retrieval over lookup

When asked for kappa(W_N), the model produces c*H_{N-1} or c*(H_{N-1}) from a prior (possibly from the training data's convention) rather than reading landscape_census.tex. This is AP1 + AP136. The model WILL read the file if explicitly instructed in the same message; it does NOT do so spontaneously. Mitigation: rewrite 4.4 requires a `% AP1` citation comment, forcing the read.

### 5.5 Plausible-proof construction without independent verification

When asked to write a compute engine test, the model reproduces the engine's own computation as the "expected value" and writes a plausible-sounding comment claiming it was verified independently. The comment is confabulated; the actual cross-check was not performed. This is AP10 + AP128. The Stokes engine F1-F4 bugs all had this signature: the test echoed the engine, both were wrong, the comment claimed "verified by Pade approximation" when the Pade itself was the bug. Mitigation: rewrite 4.6 requires the comment to CITE a file or paper + line number, which is harder to confabulate.

### 5.6 Cross-volume propagation blindness

When fixing an issue in Vol I, the model does not spontaneously grep Vols II and III for variants. The AP5 rule explicitly requires this but the model does not execute it unless reminded in the current message. The Wave-5 commit "9bd9e07 Fix Heisenberg kappa: k/2 -> k (AP1 rectification from Vol I audit)" is direct evidence: the Vol I audit found the bug, Vol II still had it weeks later. Mitigation: a Vol-I-edit hook that runs `grep` on Vols II and III and surfaces candidate matches in the agent's next tool result.

### 5.7 Confident paraphrasing of rules without execution

The model will quote "AP126: classical r-matrix for affine KM is k*Omega/z" in a commit message WHILE the commit itself writes Omega/z in the .tex file. The rule-recitation and rule-enforcement are decoupled. The model "knows" the rule (can quote it) without "following" the rule (its writes violate it). Mitigation: enforce rules via greppable invariants (hooks), not via instructions.

### 5.8 "In a theorem" loophole exploitation

When a rule says "every occurrence IN A THEOREM must carry tag", the model writes the occurrence in a DEFINITION or REMARK instead to avoid the tag. This was observed in Vol III toroidal_elliptic.tex for AP32. The model reads the rule as a boundary condition and routes around it. Mitigation: remove the environment qualifier from scope rules ("every occurrence in ANY environment MUST carry the tag"), as rewrite 4.3 does.

### 5.9 Sibling-rule fragmentation

APs 22, 44, 133, 136 all concern divided powers or Catalan/harmonic conventions; APs 25, 34, 50, 101 all concern functor conflation; APs 32, 118, 130, 139 all concern scope/quantification; APs 116, 120, 136 all concern boundary/reciprocal/harmonic arithmetic. The model treats each AP as independent, so catching AP22 does not generalize to AP44. Mitigation: group APs into "AP FAMILIES" with shared root cause and shared fix template, so learning one applies to all.

### 5.10 Over-annotation as compliance theatre

When told to tag with `(UNIFORM-WEIGHT)`, the model adds the tag to every occurrence regardless of whether it applies — including cases where the scope is ALL-WEIGHT. This turns a scope discipline into a compliance theatre where the tag is meaningless. Observed in the Wave 6 -> Wave 7 rectification where some `(UNIFORM-WEIGHT)` tags were applied to Heisenberg formulas (which ARE uniform-weight correctly), but the tag-adding was mechanical and would have over-tagged had the rule been looser. Mitigation: tags should be INFORMATIVE not DEFENSIVE — rewrite 4.3 has four options (UNIFORM / ALL-WEIGHT / g=1 / LOCAL) that force the agent to choose, not just apply.

---

## Appendix: Wave Map

Waves referenced in this report:
- Wave 1A-4: 2026-03-28 to 2026-04-01 — Platonic rewrite + initial Beilinson audits.
- Wave 5: 2026-04-02 — Deep Beilinson sweep (V2-AP1-24 E_1/E_inf corruption resolved).
- Wave 6: 2026-04-05 to 2026-04-06 — 63-chapter rectification programme, 96 fixes.
- Wave 6-2: 2026-04-09 AP5 cross-volume propagation audit (ap5_cross_volume_report_wave6.md).
- Wave 7: 2026-04-07 to 2026-04-08 — 196-agent session, 3 CRITICAL errors caught, AP126 mass fix.
- Wave 7 verification: 2026-04-09 post-fix verification (ap5_post_wave7_verification.md).
- Wave 8: 2026-04-08 — Exhaustive gap analysis (exhaustive_gap_analysis_2026_04_08.md).
- Wave 9: 2026-04-08 to 2026-04-09 — Chriss-Ginzburg rectification skill v2 + AP124-AP128 archaeology.
- Wave 10: 2026-04-09 — 48-agent cross-volume CG sweep (AP129-AP141 codified).
- Wave 11: 2026-04-09 — Deep audit of heisenberg_frame.tex (beilinson_audit_vol1_overture_wave11.md).
- Wave 12 (this report): 2026-04-09 — Recurrence archaeology and rewrite proposals.

---

## Closing

The data-driven finding is unambiguous: the APs that recur are those whose CLAUDE.md wording is an ASPIRATION or an OBSERVATION rather than a template or a gate. AP126 has been fixed six times because the rule tells agents to "verify after writing" rather than giving a fill-in-the-blanks template with k as a mandatory variable. AP40 has been fixed five times because the rule says environments "must match" without providing a write-time decision tree. AP10 has been fixed three times because "2+ independent paths" is an honor system.

The rewrites in Section 4 convert each top-10 recurring AP into a template, a decision tree, a citation requirement, or a greppable invariant. The goal is to make the rule executable at write time, not inspectable at audit time. Adopting them in the next CLAUDE.md reconstitution should reduce the recurrence count to zero for AP126 (via the k-prefix template + hook), to zero for AP40 (via the decision tree + conjecture default), and to <=1 for the remaining top-15 (via the respective gates).

The single most important observation from Wave 12 is that AP141 already captures this pattern: "AP126 is systemic" is a confession that even after codifying AP126, the error recurred because the rule was not operationally forcing. This archaeology report extends that observation to all 15 repeat offenders and proposes the forcing functions that would close the loop.
