# LaTeX Pitfall Blacklist -- Wave 12

Modular Koszul Duality programme (Vols I/II/III). This blacklist enumerates every LaTeX
pattern observed in agent work that either (a) breaks the build outright, (b) injects a
silent math/prose error the build still accepts, or (c) violates a CLAUDE.md prose/labelling
rule. Each entry ships with a regex that the Beilinson gate can run, the failure mode, a
fix template, and a proposed hook tier.

Scope: the three working trees
`/Users/raeez/chiral-bar-cobar`, `/Users/raeez/chiral-bar-cobar-vol2`,
`/Users/raeez/calabi-yau-quantum-groups`. All regexes use ERE unless flagged PCRE.

Severity tiers

- CRITICAL: hard build failure, silently wrong theorem statement, or cross-volume
  label collision. Block the edit; require manual intervention.
- MODERATE: silent math/prose error that the build accepts (wrong constant, wrong
  scope, stale attribution). Surface as a warning, do not block.
- MINOR: hygiene (prose slop, spacing, unused labels, orphan cites). Warn only.

Hook integration: entries with a `[hook]` tag are ready to drop into
`.claude/hooks/beilinson-gate.sh` or `scripts/verify_edit.sh`. Those without are
structural audits that belong in `scripts/integrity_gate.sh` (whole-repo sweep).

---

## CRITICAL -- Build-breaking

### L01. Stray `>` in `\end{...}` delimiter
- Pattern: `\\end\{[A-Za-z*]+>`
- Failure mode: pdflatex hard error "Argument of \end has an extra }". Caught in
  Wave 10-8 (N2). Tool edits that mistype `}` as `>` on the closing environment are
  invisible in diff review and survive visual inspection.
- Fix template: replace the terminating `>` with `}`, rerun build.
- [hook]: grep on every `.tex` write; block the edit if the regex fires. Pair with
  the mirror check `\\begin\{[A-Za-z*]+>`.

### L02. `\newcommand` inside `chapters/` or `appendices/`
- Pattern (path + body): file matches `(chapters|appendices)/.*\.tex`; body matches
  `^[^%]*\\newcommand\{`.
- Failure mode: the preamble already defines the canonical macro set. A chapter-level
  `\newcommand` either collides (hard error) or shadows the preamble (silent
  divergence between standalones and the main build). CLAUDE.md rule: chapter files
  must use `\providecommand`.
- Fix template: move the macro to `main.tex` preamble; in-chapter uses
  `\providecommand` only.
- [hook]: on write, if the path matches `(chapters|appendices)/` and the new_string
  contains `\newcommand{`, block.

### L03. Undefined macro in standalone extraction
- Pattern (heuristic): any `\[A-Za-z@]+` in a standalone paper under
  `standalones/` that is not defined in either the standalone's own preamble or
  `main.tex`.
- Failure mode: `\cW`, `\hv`, `\cat`, `\brk`, `\Ran`, `\sE`, etc. are declared only
  in the Vol I `main.tex` preamble. Standalone extractions inherit none of this and
  die on "undefined control sequence".
- Fix template: for each standalone, generate a `standalone_macros.sty` snapshot of
  main.tex preamble, include it in the standalone preamble, and freeze.
- [hook]: structural, not inline. Propose `scripts/standalone_macros_audit.py` that
  (a) tokenises every `\[A-Za-z@]+` in each standalone, (b) subtracts the set defined
  in its preamble and any `\input`'d `.sty`, (c) flags the remainder.

### L04. Duplicate `\label{}` across chapters or volumes (AP124)
- Pattern: any label string that appears in `\label{X}` at 2+ distinct file
  locations across `chapters/ appendices/ standalones/` of any volume.
- Failure mode: LaTeX silently uses the last definition. Cross-refs point to the
  wrong page; agents grepping for `\label{thm:foo}` see ambiguous results and
  re-derive the wrong theorem.
- Fix template: rename all but one occurrence, update every `\ref`/`\eqref`/
  `\cref` target atomically.
- [hook]: partial. The current `beilinson-gate.sh` already checks duplicates within
  Vol I chapters/appendices. Extend the scan to Vol II and Vol III trees and to
  `standalones/` before blocking.

### L05. Label prefix / environment mismatch (AP125)
- Pattern (multiline, PCRE `-U --multiline-dotall`):
  `\\begin\{(theorem|lemma|proposition|corollary|conjecture|definition|remark|example|construction|principle)\}[\s\S]{0,400}?\\label\{([^}]+)\}`
  with a mismatch between the captured environment and the prefix of the captured
  label:
    - `theorem`   -> prefix `thm:`
    - `lemma`     -> `lem:`
    - `proposition` -> `prop:`
    - `corollary` -> `cor:`
    - `conjecture` -> `conj:`
    - `definition` -> `def:`
    - `remark`    -> `rem:`
    - `example`   -> `ex:`
    - `construction` -> `constr:`
    - `principle` -> `princ:`
- Failure mode: `\begin{conjecture}\label{thm:foo}` misleads every subsequent grep.
  Agents looking for "all conjectures" filter on `conj:` and miss this one; agents
  looking for "all theorems" filter on `thm:` and cite a conjecture as theorem.
  Caught repeatedly in CG rectification sweeps.
- Fix template: rename the label to the correct prefix and run the Vol I/II/III
  `\ref`/`\eqref` sweep to retarget.
- [hook]: multiline grep on every write; report mismatches as CRITICAL. Use a Python
  helper (awk is too brittle).

### L06. `\eqref` pointing at a non-equation label
- Pattern: `\\eqref\{(conj|rem|def|sec|ch|prop|thm|lem|cor|constr|comp|princ|tab|fig|subsec|chap|part|ex|constr|alg|princ):`
- Failure mode: `\eqref` wraps the reference in parentheses intended for equation
  tags. Feeding it a `thm:` or `prop:` label produces `(Theorem 3.4)` in running
  prose, which looks correct at first glance but doubles the parenthesization if
  the calling sentence already has `(see ...)`. Self-caught in Wave 6-6.
- Fix template: `\ref{...}` or `\Cref{...}` for non-equation labels; `\eqref{...}`
  strictly for `eq:` labels.
- [hook]: simple grep on write, warn.

### L07. `\ref{}` to undefined label (within-file fast check)
- Pattern: collect every `\ref\{([^}]+)\}` and every `\label\{([^}]+)\}` in the
  single file; flag `\ref` keys with no matching `\label` anywhere in the repo
  label index.
- Failure mode: LaTeX reports "Reference `foo' on page X undefined" but the build
  still succeeds with `??`. Ship-blocker only at integrity gate; MODERATE at edit
  time.
- Fix template: add the label or retarget the `\ref`.
- [hook]: whole-repo audit in `integrity_gate.sh` (already partially covered by
  the `UNDEF_REF` metric). Proposed extension: write a persistent label index to
  `/tmp/chiral_label_index` on every build, and make `beilinson-gate.sh` consult it.

### L08. Tool-call markup leak (AAP1)
- Pattern: `antml|</invoke>|<tool_call>|<function_calls>|<parameter name=`
- Failure mode: pdflatex chokes on `<`; even when it does not, the bytes commit to
  `main.tex` and the build leaks tool-call residue into the PDF.
- Fix template: delete the residue, re-run the edit.
- [hook]: already present in `beilinson-gate.sh`. Keep CRITICAL tier.

### L09. Markdown pollution (AP121): backtick numerals and code spans
- Pattern: `` `[0-9] `` and `` `[A-Za-z]{1,6}` `` in `.tex` (outside `verbatim`,
  `lstlisting`, `minted` environments).
- Failure mode: backticks render as open-quote characters. `` `29` `` becomes
  `'29'`. Mathematical content looks superficially fine but grades out as a typo.
- Fix template: numerals to `$29$`, names to `\(\kappa\)` or `\texttt{foo}`.
- [hook]: already present in `beilinson-gate.sh` for digits. Extend to alphabetic
  runs of 1-6 chars.

### L10. Markdown bold and italic (AP121 cont.)
- Pattern: `\*\*[^*]+\*\*` and `(?<![\*])_[A-Za-z][A-Za-z0-9 ]+_(?![\*])`.
- Failure mode: `\*\*bold\*\*` prints as literal asterisks in the PDF;
  underscore-italic in math mode produces subscripts and collapses spaces.
- Fix template: `\textbf{...}` and `\emph{...}` respectively.
- [hook]: grep on write, warn.

---

## MODERATE -- Silent math / scope / attribution errors

### L11. Bare `\Omega/z` r-matrix without level prefix (AP126 / AP141)
- Pattern (PCRE, negative lookbehind):
  `(?<![kK]\\?\s)(?<![hg]\^\vee\s)\\Omega\s*/\s*z(?![\^])`
  plus the narrower form `r\s*\(z\)\s*=\s*\\Omega\s*/\s*z`.
- Failure mode: the affine KM classical r-matrix is `k \Omega / z`. Writing
  `\Omega / z` is correct only at level `k=1` and silently wrong elsewhere. AP126
  is the single most-violated AP across all three volumes (42+ instances). Every
  r-matrix formula must vanish at `k=0`.
- Fix template: rewrite as `r(z) = k\, \Omega/z`; evaluate at `k=0` as a
  sanity check before committing.
- [hook]: grep on write. Any `\Omega/z` without a preceding `k`, `K`, or level
  prefix within the same line warns.

### L12. Bare `\kappa` in Vol III (AP113)
- Pattern: file under `/Users/raeez/calabi-yau-quantum-groups/`; body matches
  `\\kappa(?![_A-Za-z0-9])`.
- Failure mode: Vol III has MULTIPLE kappa's (`kappa_ch`, `kappa_BKM`, `kappa_cat`,
  `kappa_fiber`). Bare `\kappa` collapses them and produces the K3xE contradiction
  (3 vs 5) that motivated AP113.
- Fix template: subscript every occurrence; if the expression is symbolic across
  spectra, say so explicitly.
- [hook]: already present in `beilinson-gate.sh`. Keep MODERATE.

### L13. Bar complex missing `\bar A` (AP132)
- Pattern (PCRE): `T\^c\s*\(\s*s\^\{-1\}\s*A(?![^)]*\\bar)`
- Failure mode: the bar construction uses the augmentation ideal
  `\bar A = \ker(\epsilon)`, not `A`. Writing `T^c(s^{-1} A)` silently includes
  the unit and breaks `d^2=0`.
- Fix template: `T^c(s^{-1} \bar A)` and render `\bar A` explicitly throughout.
- [hook]: grep on write, warn.

### L14. Missing desuspension `s^{-1}` in bar-complex formulas
- Pattern: `T\^c\s*\(\s*A` or `T\^c\s*\(\s*\\bar\s*A` (no `s^{-1}` before the `A`).
- Failure mode: bar = down = desuspension. Omitting `s^{-1}` breaks the grading
  and flips the sign of every differential.
- Fix template: `T^c(s^{-1} \bar A)`.
- [hook]: grep on write, warn.

### L15. Quadratic Virasoro r-matrix (AP19/AP21)
- Pattern (ERE):
  `r_?c?\s*\(z\)\s*=\s*.*z\^\{-4\}|(c/2)/z\^\{?4\}?|Vir.*r.*matrix.*z\^\{?-4\}?`
- Failure mode: the Virasoro classical r-matrix is `(c/2)/z^3 + 2T/z`. `d log`
  absorbs one pole, so the r-matrix poles are ONE LESS than the OPE poles
  (`T(z)T(w) \sim (c/2)/(z-w)^4 + ...`). Writing `(c/2)/z^4` as r-matrix conflates
  the two invariants.
- Fix template: `r(z) = (c/2)\, z^{-3} + 2T\, z^{-1}`.
- [hook]: grep on write, warn.

### L16. `\begin{proof}` inside `\begin{conjecture}` (AP40)
- Pattern (multiline):
  `\\begin\{conjecture\}[\s\S]*?\\begin\{proof\}[\s\S]*?\\end\{proof\}[\s\S]*?\\end\{conjecture\}`
- Failure mode: conjectures do not carry proofs. A proof environment inside a
  conjecture environment is either a mis-classified theorem (upgrade the tag) or a
  heuristic dressed up as proof (downgrade to `\begin{remark}[Evidence]`).
- Fix template: either upgrade conjecture to theorem + ProvedHere + legitimate
  proof, or demote the proof to a Remark[Evidence].
- [hook]: multiline grep at write time, warn.

### L17. `\ClaimStatusConjectured` inside a proof-bearing environment (AP40)
- Pattern (already in beilinson-gate.sh): `\ClaimStatusConjectured` within 10
  lines below `\begin{theorem|proposition|lemma|corollary}`.
- Failure mode: environment says "proved", status tag says "conjectured".
  Readers and agents disagree on the truth value.
- Fix template: either change environment to `conjecture` or upgrade status to
  `ProvedElsewhere` / `ProvedHere`.
- [hook]: already live. Keep MODERATE.

### L18. `\ClaimStatusProvedHere` on unreviewed content (AP60)
- Pattern: every `\ClaimStatusProvedHere` occurrence, annotated with file + line.
- Failure mode: `ProvedHere` claims original credit for classical content. AP60
  requires that classical parts carry `\ClaimStatusProvedElsewhere` with attribution.
- Fix template: manual review. Cannot be automated; produce a weekly report of
  all `ProvedHere` tags for the author to audit.
- [hook]: structural; add to `integrity_gate.sh` as a metrics dump, not a blocker.

### L19. `\ClaimStatusConjectured` inside `\begin{proposition}` (AP40 variant)
- Pattern: same as L17, restricted to `proposition`.
- Failure mode: proposition carrying a conjectured tag fails AP40. The common
  case is a lemma labelled proposition with a speculative corollary stapled on.
- Fix template: split into `\begin{proposition}` (the proved part) and
  `\begin{conjecture}` (the speculative part).
- [hook]: covered by L17's regex.

### L20. `\text{word}` containing a single word of prose
- Pattern: `\\text\{[A-Za-z]+\}` where the argument is exactly one word.
- Failure mode: `$\text{modular}$` forces a text-mode context for a single word
  that is neither a unit nor a function name. Usually the right fix is prose
  outside math mode; occasionally `\mathrm{...}` or `\operatorname{...}`.
- Fix template: move the word out of math mode, or use `\operatorname{}`.
- [hook]: grep on write, minor warning. Tier is MODERATE because single-word
  `\text{}` can hide off-by-one convention errors (e.g. `$h^{\text{dual}}$` vs
  `$h^\vee$`).

### L21. Reciprocal transcription (AP129)
- Pattern: hard to regex generically; propose a watchlist of known-dangerous
  ratios. For Vol I, seed the list with
  `S_4(\mathrm{Vir})\s*=|\\kappa\s*/\s*S_4|S_4\s*/\s*\\kappa|(5c+22)`.
- Failure mode: `a/b` and `b/a` contain the same symbols. `S_4(Vir) = 10/[c(5c+22)]`
  was transcribed as `-(5c+22)/(10c)` and passed visual review. Only a numerical
  substitution catches it.
- Fix template: when writing any such ratio, substitute a known value (e.g. c=1)
  and verify the number before committing.
- [hook]: MODERATE warn on any match from the watchlist; prompt the author to
  verify by substitution.

### L22. Fiber-base confusion in Hodge class expressions (AP130)
- Pattern (PCRE): `\\omega_g\s*=\s*d\\tau|c_1\(\\lambda\)\s*=\s*d\s*z|c_1\(E\)\s*=.*H\^\{1,0\}`
  and the broader `\\omega_g\s*=[^,]*d(\\tau|z|w)`.
- Failure mode: `\omega_g = c_1(\mathbb{E})` lives on `M-bar_g`. `d\tau` lives on
  the elliptic fiber. Equating them confuses fiber and base.
- Fix template: `\omega_g = c_1(\mathbb{E}_g)` as a class on moduli; `d\tau` as a
  form on the fiber; relate them only through a carefully stated period pairing.
- [hook]: grep on write, warn.

### L23. Cohomological amplitude vs virtual dimension (AP134)
- Pattern: `virtual\s+dimension\s+(2|=\s*2)` near `ChirHoch` or
  `amplitude\s*\[0,\s*(d|2)\]`.
- Failure mode: writing "virtual dimension 2" when the correct statement is
  "cohomological amplitude `[0,2]`". The two are different invariants.
- Fix template: say "cohomological amplitude `[0,d]`"; reserve "virtual dimension"
  for Euler-characteristic-level statements.
- [hook]: grep on write, warn.

### L24. Unbound variable in theorem statement (AP139)
- Pattern: structural, not regex. Parse every `\begin{theorem|proposition|lemma}`
  body, collect the displayed equations, and check that every free symbol in the
  equation appears bound (`\forall`, context clause, or explicit quantifier) in
  the theorem statement.
- Failure mode: LHS depends on `g` but RHS depends on `g, n` and the theorem
  quantifies only over `g`. Caught in Theorem C^{E1} during Wave 10.
- Fix template: add an explicit `for all n` or a context clause
  "at each arity n with 2g-2+n>0".
- [hook]: propose `scripts/unbound_variable_audit.py`. Not an inline hook; run in
  the integrity gate.

### L25. Harmonic number off-by-one (AP136)
- Pattern: `H_\{N-1\}` or `H_\{?N-1\}?\s*-\s*1|H_N\s*-\s*1`.
- Failure mode: `H_{N-1} != H_N - 1`. CLAUDE.md itself had this error once.
  Evaluate at `N=2` to distinguish.
- Fix template: pick the intended sum range explicitly and write it as
  `\sum_{j=a}^{b} 1/j`.
- [hook]: grep on write, warn with the evaluate-at-N=2 prompt.

### L26. Bosonic/fermionic partner confusion (AP137)
- Pattern: `c_\{?\\beta\\gamma\}?\s*\+\s*c_\{?bc\}?\s*=\s*([^0]|0[0-9])`
  and the misspelled `c_{\beta\gamma}(\lambda)\s*=\s*1-3\(2\lambda-1\)^2` or
  `c_{bc}(\lambda)\s*=\s*2\(6\lambda\^2-6\lambda+1\)` (both are the wrong partner).
- Failure mode: `c_{\beta\gamma}(\lambda) = 2(6\lambda^2-6\lambda+1)` and
  `c_{bc}(\lambda) = 1-3(2\lambda-1)^2` satisfy `c_{\beta\gamma}+c_{bc}=0`. Swapping
  them silently flips the sign of c.
- Fix template: verify `c_total=0` at `\lambda=1` before committing.
- [hook]: grep on write, warn with the substitution prompt.

### L27. Koszul conductor confused with local constant (AP140)
- Pattern: `K_?\{?BP\}?\s*=\s*2(?!\d)` in any file that also contains `c + c'`
  or `Koszul conductor`.
- Failure mode: `K_{BP}=196`, not 2. The number 2 is the ghost constant
  `C_{(2,1)}`; mistaking one for the other ships the wrong global invariant.
- Fix template: verify by reading the Koszul conductor definition from the
  current draft, not from memory; cite the derivation.
- [hook]: grep on write, warn.

### L28. Heisenberg R-matrix written as trivial (V2-AP7)
- Pattern: `Heisenberg.*R\s*\(z\)\s*=\s*1|R_\{?\\mathrm?\{Heis\}?\}\s*=\s*1`
- Failure mode: `R(z) = \exp(k\hbar/z)`, not 1. Monodromy `\exp(-2\pi i k)`. A
  trivial Heisenberg R-matrix silently destroys the CG opening.
- Fix template: `R(z) = \exp(k\hbar/z)`.
- [hook]: grep on write, warn.

### L29. Hardcoded Part number (V2-AP26)
- Pattern: `Part~[IVX]+|Part [IVX]+` outside `\ref{part:...}` and `\label{part:...}`.
- Failure mode: Part restructurings leave stale Roman-numeral references.
- Fix template: `\ref{part:foo}` everywhere; `\Cref{part:foo}` where grammar allows.
- [hook]: already present in `beilinson-gate.sh`. Keep MODERATE.

### L30. Narration block openings (AP106 / RS-5)
- Pattern: `This chapter (constructs|establishes|proves|develops|introduces|discusses)`
  and `The chapter proceeds as follows|What this chapter proves`.
- Failure mode: CLAUDE.md forbids "This chapter constructs..." openings. Every
  chapter must open with the CG deficiency: the problem the existing literature
  cannot solve.
- Fix template: rewrite the opening to state the deficiency.
- [hook]: already present in `beilinson-gate.sh`. Keep MODERATE.

### L31. AI slop words (prose standard)
- Pattern: case-insensitive word-boundary match on the set
  `notably, crucially, remarkably, interestingly, importantly, furthermore,
   moreover, additionally, delve, leverage, utilize, underscore, facilitate,
   pivotal, nuanced, intricate, streamline, tapestry, multifaceted, cornerstone,
   navigate, seamless`.
- Failure mode: every occurrence is an LLM tell. CLAUDE.md prose law #1.
- Fix template: delete or replace with a direct assertion.
- [hook]: already present in `beilinson-gate.sh`. Extend with the Wave 12
  additions: `intricate, seamless, navigate`.

### L32. Em-dash Unicode (prose standard)
- Pattern: the literal character `—` (U+2014), also `\textemdash`.
- Failure mode: CLAUDE.md bans em dashes. Use colon, semicolon, or separate
  sentences.
- Fix template: replace with `: `, `; `, or a period.
- [hook]: grep on write, MODERATE.

### L33. AI attribution in `.tex` or commit messages
- Pattern (case-insensitive):
  `co-authored-by|anthropic|claude(?!\sduality)|chatgpt|llm-generated|
   ai-assisted|generated-by|assistant:\s|🤖|written by an AI`.
- Failure mode: CLAUDE.md git attribution rule -- all commits by Raeez Lorgat,
  no AI attribution anywhere (prose or metadata). This includes `.tex` prose,
  `README.md`, and `git commit -m`.
- Fix template: remove the attribution. If the prose references the collaboration
  narrative, use human co-authors only.
- [hook]: CRITICAL blocker on any `.tex` write; CRITICAL blocker in a `prepare-
  commit-msg` hook. The "Claude" carve-out avoids false positives on "Claude
  Chevalley" or future references to Claude-named mathematicians.

### L34. `\cite{}` to an undefined bibkey
- Pattern: collect every `\cite[*]?\{([^}]+)\}` key; cross-check against the
  union of `.bib` files in the volume. Keys not present are warnings.
- Failure mode: LaTeX emits `UNDEF_CITE` warnings that the integrity gate already
  gates on. MODERATE at edit time because the author might be in the middle of
  adding the bib entry.
- Fix template: add the entry to the bib file or fix the key.
- [hook]: edit-time warn; integrity gate block.

### L35. Orphan `\label{}`
- Pattern: any label with zero `\ref|\eqref|\Cref|\autoref` targeting it across
  the volume.
- Failure mode: dead label; ships with the PDF but no cross-reference reaches it.
- Fix template: either delete the label or add the missing cross-reference.
- [hook]: whole-repo audit, not inline. MINOR.

### L36. Genus formula sign on `(2g-2+n)`
- Pattern: `-\s*\(\s*2\s*g\s*-\s*2\s*\+\s*n\s*\)|-\(2g-2\+n\)|2g\s*+\s*2\s*-\s*n`.
- Failure mode: the stability condition is `2g-2+n > 0`. Writing `-(2g-2+n)`
  flips the sign, producing vacuous ranges; writing `2g+2-n` is a common
  transposition.
- Fix template: `2g-2+n`, with the stability inequality stated explicitly where
  relevant.
- [hook]: grep on write, warn.

### L37. Forbidden ghost character in `.tex`: `\textbf{...}` holding numerals
- Pattern: `\\textbf\{[0-9][0-9A-Za-z ]*\}`
- Failure mode: numeric bold in prose is a Markdown relic. Typography standard
  uses math-mode numerals.
- Fix template: `$\mathbf{29}$` or remove the bold.
- [hook]: MINOR warn.

### L38. Bare `s` in bar-complex formula (AP22/AP46)
- Pattern (PCRE): `T\^c\s*\(\s*s\s+` without `^{-1}`.
- Failure mode: `T^c(s \bar A)` is a SUSPENSION, not a desuspension. In
  cohomological grading `|s^{-1}v|=|v|-1`; writing `s` instead of `s^{-1}` in
  the bar complex flips the grading.
- Fix template: `T^c(s^{-1} \bar A)`.
- [hook]: grep on write, warn. Overlaps with L14 but catches the specific typo.

### L39. `H_k^!` equated to `H_{-k}` (AP33)
- Pattern: already in `beilinson-gate.sh`. Keep MODERATE.

### L40. `kappa+kappa'=0` unqualified (AP24)
- Pattern: already in `beilinson-gate.sh`. Keep MODERATE.

### L41. Duplicate theorem text across files (V2-AP27)
- Pattern: structural. For every `\begin{theorem}...\end{theorem}` block, compute
  a hash of the normalized text (strip whitespace and label). If the same hash
  appears in two files, warn.
- Failure mode: copy-pasted theorems diverge silently over time.
- Fix template: move to a shared file and `\input{}` it.
- [hook]: integrity gate audit, not inline.

---

## MINOR -- Hygiene

### L42. `\begin{equation}` containing a single symbol
- Pattern: `\\begin\{equation\}\s*[A-Za-z\\]+\s*\\end\{equation\}`.
- Failure mode: single-symbol displayed equations usually belong inline.
- Fix template: inline math mode.
- [hook]: MINOR warn.

### L43. Double `\\` at end of line in prose paragraphs
- Pattern: `\S\\\\\s*$` outside `tabular|array|align|matrix|cases|pmatrix` environments.
- Failure mode: forces a line break in body text; the current standard uses only
  paragraph breaks.
- Fix template: remove the `\\`.
- [hook]: MINOR warn.

### L44. Trailing whitespace on code lines
- Pattern: `[ \t]+$`
- Failure mode: diff noise, no functional impact.
- Fix template: strip on save.
- [hook]: MINOR.

### L45. Smart quotes (U+2018 U+2019 U+201C U+201D)
- Pattern: literal `'`, `'`, `"`, `"`.
- Failure mode: non-ASCII glyphs in source. EB Garamond renders them, but the
  manuscript standard is ``...'' and `...'.
- Fix template: replace with LaTeX quotes.
- [hook]: MINOR warn.

### L46. Signpost phrases (prose standard)
- Pattern: already present in `beilinson-gate.sh`. Keep MINOR.

### L47. `Moreover,` as sentence opener (prose standard)
- Pattern: already present in `beilinson-gate.sh`. Keep MINOR.

### L48. Stub chapters (AP114)
- Pattern: file length < 50 non-blank lines AND contains zero
  `\begin{theorem|proposition|lemma|definition|construction}` blocks.
- Failure mode: stubs create false coverage. AP114 requires develop-or-comment.
- Fix template: develop or `%`-out in `main.tex`.
- [hook]: integrity gate metrics dump.

---

## Hook integration priority

Top 10 highest-leverage hook additions (by impact per line of shell added):

1. **L01** stray `>` in `\end{...}`: CRITICAL build-breaker, 1-line regex, zero
   false positives. Deploy immediately.
2. **L02** `\newcommand` in chapters: CRITICAL per CLAUDE.md, trivial path + body
   regex. Deploy immediately.
3. **L05** label prefix/environment mismatch: CRITICAL per AP125, catches the
   single most-frequent mislabelling class. Needs a small Python helper.
4. **L11** bare `\Omega/z` r-matrix: AP126 is the most-violated AP in the
   manuscript (42+ instances). One regex with a negative lookbehind for `k`.
5. **L08** tool markup leak (already live): verify the hook is active in all
   three volume worktrees; extend to `standalones/`.
6. **L04** cross-volume duplicate labels: extend the existing within-Vol-I
   duplicate check to scan Vol II and Vol III as well.
7. **L33** AI attribution in `.tex` and commit messages: CRITICAL per CLAUDE.md
   git rule; needs a new `prepare-commit-msg` hook alongside the edit-time check.
8. **L32** em-dash Unicode: one-character regex, catches every occurrence.
9. **L13** bar complex missing `\bar A` (AP132): one PCRE lookahead, catches the
   twice-observed augmentation-ideal error.
10. **L16** proof inside conjecture (AP40): multiline regex, catches the
    environment/status mismatch that ships the manuscript with a conjecture
    labelled as proved.

Integrity-gate-only additions (not inline, but worth adding to
`scripts/integrity_gate.sh` as metrics with a zero threshold):

- L03 undefined macros in standalones.
- L07 `\ref` to undefined label (already partially covered by `UNDEF_REF`).
- L18 `\ClaimStatusProvedHere` manual-review dump.
- L24 unbound variables in theorem statements.
- L35 orphan labels.
- L41 duplicate theorem text hashes.
- L48 stub chapters.

---

## Cross-references

- Existing hook: `/Users/raeez/chiral-bar-cobar/.claude/hooks/beilinson-gate.sh`
  (covers L08, L09, L12, L17, L29, L30, L31, L39, L40, L46, L47)
- Existing hook: `/Users/raeez/chiral-bar-cobar/.claude/hooks/convergence-gate.sh`
  (orthogonal -- enforces rectification-loop convergence, not LaTeX patterns)
- Existing script: `/Users/raeez/chiral-bar-cobar/scripts/verify_edit.sh`
  (16 historically-recurring false math claims; complements this blacklist on
  the math-semantic side)
- Existing script: `/Users/raeez/chiral-bar-cobar/scripts/integrity_gate.sh`
  (whole-repo build + structural metrics; L07, L24, L41 belong here)

This blacklist does not modify any of the above. Installation is a separate
editing pass, gated on author review.
