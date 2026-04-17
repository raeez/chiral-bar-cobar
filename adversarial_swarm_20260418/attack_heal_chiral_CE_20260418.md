# Attack + Heal: Chiral CE claim $B(U^{\mathrm{ch}}(L)) = \mathrm{CE}_*(L)$

Date: 2026-04-18
Mission: adversarial audit of the "Chiral CE complex: $B(U^{\mathrm{ch}}(L)) = \mathrm{CE}_*(L)$ PROVED" advertisement in Vol III CLAUDE.md:107, AGENTS.md:176, and FRONTIER.md:834.
Author: Raeez Lorgat.
AP block reserved: AP1041-AP1060. Used: **AP1041, AP1042, AP1043, AP1044** (four genuinely distinct patterns surfaced).

## Summary verdict

**RETRACTION REQUIRED.** The advertised "PROVED" identification $B(U^{\mathrm{ch}}(L)) \simeq \mathrm{CE}_*(L)$ is a **load-bearing confabulation** composed of five stacked errors:

1. the engine `compute/lib/chiral_ce_complex.py` computes the **classical** Chevalley-Eilenberg complex $\bigwedge^\bullet L_{\mathrm{gen}}$ of the finite-dimensional **generator space** $L_{\mathrm{gen}}$ and **calls it** the chiral bar complex of $U^{\mathrm{ch}}(L)$ (AP1041);
2. the `BarCEComparison.poincare_match()` at `chiral_ce_complex.py:1052-1054` is a **vacuous tautology** (AP277 / AP287 variant): it compares a single computation to itself and returns `True` by construction, so the advertised "cross-check" verifies nothing;
3. the Vol III numerics **directly contradict** Vol I `prop:derived-center-explicit` at `chiral_center_theorem.tex:1967`:
   - Heisenberg: Vol III says Poincaré $(1+t)$, total 2; Vol I says $1+t+t^2$, total 3. Contradiction at $\ChirHoch^2$ (the level deformation class $\eta$);
   - affine $\widehat{\fsl}_2$: Vol III says $(1+t)^3$, total 8; Vol I says $1+3t+t^2$, total 5. Contradiction in degrees $\geq 2$;
   - Virasoro: Vol III says $(1+t)$ total 2; Vol I says $1+t^2$ total 2. Same total, wrong bar-degree distribution (AP312 three-way value contradiction, specialised to Poincaré polynomials);
4. the proof body at `quantum_chiral_algebras.tex:299-308` cites Loday-Vallette "Theorem 10.1.6" for "$B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$"; LV Theorem 10.1.6 is about **Koszul duality for operads**, not about bar-CE. The classical $B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$ is Loday-Vallette Proposition 3.3.6 / Corollary 3.3.6, or Cartan-Eilenberg Ch. XIII §7. This is **AP285** (alias section-number drift, but a more serious variant: the cited theorem does not prove anything near the claimed statement);
5. the correct primary-source statement, Beilinson-Drinfeld 2004 **Theorem 4.8.1** (cited correctly elsewhere in Vol I at `bar_construction.tex:440` and `chiral_koszul_pairs.tex:5809`), identifies chiral homology of a chiral envelope with the **Chevalley complex of derived global sections**, $\int_C \mathrm{CE}(L) = \mathrm{CE}(\mathrm{R}\Gamma(C, L))$, NOT with the naive exterior algebra $\bigwedge^\bullet L_{\mathrm{gen}}$. At $g \geq 1$ the two differ by nontrivial $H^1(C, L)$ contributions; at $g = 0$ they differ by the OPE simple-pole structure (central charge / level deformations).

The slogan $B(U^{\mathrm{ch}}(L)) \simeq \mathrm{CE}_*(L)$ holds with multiple caveats only if: (a) $\mathrm{CE}_*(L)$ is read as **derived global sections** of a sheaf-of-CE-complexes on the curve (BD04 sense), not the naive exterior algebra; (b) the $\Ainf$-structure on $U^{\mathrm{ch}}(L)$ is strict (class G only, i.e. the zeroth product exhausts the OPE); (c) the test is against the BD04 Theorem 4.8.1 derived-global-sections formula, not against $\bigwedge^\bullet L_{\mathrm{gen}}$. None of (a)-(c) is enforced in Vol III's inscription or engine.

## Attack ledger

### A1. Primary inscription sites

- **Vol III** `chapters/theory/cy_to_chiral.tex:3868-3886`, `prop:bar-ce-chiral`, `\ClaimStatusProvedHere{}`.
  - **AP4 violation**: the proposition carries `\ClaimStatusProvedHere{}` but has NO `\begin{proof}` block; only a one-line "Verification: cross-checked against chiral_ce_complex.py". An HZ-IV-level inscription without a proof body, downstream of `\ClaimStatusProvedHere`. The status tag is illegitimate.
  - **AP1041 (new)**: classical-CE-of-generator-space masquerading as chiral-CE-of-factorization-envelope. The proposition writes $B(U^{\mathrm{ch}}(L)) \simeq \mathrm{CE}_*(L)$ with $\mathrm{CE}_*(L) = (\bigwedge^* L, d_{\mathrm{CE}})$. If $L$ is read as the generator space (finite-dim), the RHS is finite-dim; but $U^{\mathrm{ch}}(L)$ is infinite-dim (full vertex algebra), and its bar complex $T^c(s^{-1} \bar A)$ with $A = U^{\mathrm{ch}}(L)$ cannot be isomorphic as graded vector space to $\bigwedge^* L_{\mathrm{gen}}$. The reader is invited to conflate two $\mathrm{CE}_*$: (i) BD04 derived-global-sections $\mathrm{CE}$ of a sheaf of Lie algebras; (ii) classical $\bigwedge^\bullet L$ of a finite-dim generator space.

- **Vol III** `chapters/theory/quantum_chiral_algebras.tex:285-308`, `prop:bar-ce-identification`, `\ClaimStatusProvedHere`.
  - **Honest proof attempt** at lines 299-308, but the proof body contains four falsifiable claims:
    1. (line 300) "Loday-Vallette 2012, Theorem 10.1.6" as citation for $B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$: **wrong reference**. LV Theorem 10.1.6 is about Koszul duality for operads. The classical statement is LV Proposition 3.3.6 / Cartan-Eilenberg Ch. XIII. **AP285** (alias section-number drift); also **AP272** (unstated cross-lemma via folklore citation — the cited theorem does not state the lemma).
    2. (line 304) "Heisenberg ... $\HH^\bullet = \{1, 1\}$": contradicts Vol I `prop:derived-center-explicit(i)` total dim 3.
    3. (line 305) "Kac-Moody $\widehat{\fsl}_2$ Poincaré $(1+t)^3$": total dim 8, contradicts Vol I `prop:derived-center-explicit(ii)` total dim 5.
    4. (line 305) "$d_{\mathrm{CE}}^2 = 0$ verified on all basis elements": true for the naive classical CE of $\fsl_2$, but this only proves $d^2 = 0$ for the **classical** bracket differential, not for the chiral bar differential. The chiral bar differential has higher contributions from simple-pole OPE terms (see A2 below).

- **Vol III** `compute/lib/chiral_ce_complex.py` (1200+ lines) and `compute/tests/test_chiral_ce_complex.py` (66 tests).
  - **AP128**: engine and test synchronized to the same wrong mental model.
  - **AP277 / AP287**: `BarCEComparison.poincare_match` at lines 1052-1054 returns `bar_poincare() == ce_poincare()`, where both methods return the same underlying call `self.ce.poincare_polynomial()` (lines 1046, 1050). This is comparing a computation to itself and cannot fail. The "cross-check" is tautological.
  - **AP288** (HZ-IV label-disjoint, computation-identical): the engine has no independent bar-side computation; the "bar" number is a relabelling of the CE number.

### A2. The OPE simple-pole contributions that break the identification

For a Lie conformal algebra $L$, the $\lambda$-bracket $\{a_\lambda b\}$ expands as a polynomial in $\lambda$:
$$\{a_\lambda b\} = \sum_{n \geq 0} \frac{\lambda^n}{n!} a_{(n)} b,$$
where $a_{(n)} b$ is the $n$-th product. The **zeroth** product $a_{(0)} b$ is the Lie bracket (classical CE contribution). The **simple-pole** terms $a_{(n)} b$ for $n \geq 1$ are the higher-order OPE data that define the vertex algebra structure of $U^{\mathrm{ch}}(L)$.

For Heisenberg $L = \bC J$ with $\{J_\lambda J\} = k \lambda$: the zeroth product is $J_{(0)} J = 0$ (abelian), but the first product $J_{(1)} J = k$ is nonzero (the level). Vol I correctly captures this: $\ChirHoch^2(\cH_k) = \bC \cdot \eta$, where $\eta$ is the level-deformation class. The classical CE complex $\bigwedge^\bullet \bC J = \{1, J\}$ misses this.

For Virasoro with $\{T_\lambda T\} = (\partial + 2 \lambda) T + \frac{c}{12} \lambda^3$: the zeroth product $T_{(0)} T = \partial T$ (not zero if $T$ is a generator of itself — depends on linearisation), the first and third products carry the central charge. Classical CE of a 1-dim $L$ gives $\bigwedge^\bullet \bC T = \{1, T\}$ Poincaré $(1+t)$. Vol I computes $\ChirHoch^\bullet(\mathrm{Vir}_c)$ with Poincaré $1 + t^2$ (bar degree 2 from central charge deformation $\Theta \in \ChirHoch^2$, not bar degree 1 from generator $T$).

For affine $\widehat{\fsl}_2$: even with strict bracket, the chiral bar complex has nontrivial contractions at OPE simple poles $(k \text{ in the central-extension slot})$. Vol I computes $\ChirHoch^2 = \bC$ (from central charge), $\ChirHoch^1 = \fsl_2$ (from outer derivations), $\ChirHoch^0 = \bC$. Classical CE $\bigwedge^\bullet \fsl_2$ gives $\{1, 3, 3, 1\}$ total 8. The spectral sequence from classical CE to chiral bar has nontrivial differentials at pages $\geq 2$; Vol I AP128 healing corrected the total from 6 (classical Riordan) to 5 (chiral Orlik-Solomon form factor).

### A3. What the correct statement looks like

**Claim (BD04 Theorem 4.8.1, correctly stated):** Let $C$ be a smooth curve and $L$ a Lie* algebra on $C$ (a sheaf of Lie algebras in the $\cD_C$-module sense). Let $\mathrm{Env}^{\mathrm{ch}}(L)$ be the **chiral envelope**. Then the chiral homology $H^{\mathrm{ch}}_\bullet(C, \mathrm{Env}^{\mathrm{ch}}(L))$ is quasi-isomorphic to the **Chevalley-Eilenberg complex of derived global sections**:
$$H^{\mathrm{ch}}_\bullet(C, \mathrm{Env}^{\mathrm{ch}}(L)) \simeq \mathrm{CE}(\mathrm{R}\Gamma_{\mathrm{DR}}(C, L)) = \bigwedge^\bullet \mathrm{R}\Gamma_{\mathrm{DR}}(C, L),$$
where $\mathrm{R}\Gamma_{\mathrm{DR}}(C, L)$ is the de Rham cohomology of $L$ as a $\cD_C$-module (two-term complex concentrated in degrees 0 and 1 for a smooth curve). At genus $g \geq 1$, $H^1(C, L)$ is nonzero and the RHS has **both** exterior and symmetric contributions (in cohomological degrees 0 and 1, respectively, with a sign flip upon suspension).

This is an **integrated** statement over the curve, not a pointwise bar complex statement.

**Claim (specialisation to $g = 0$, $L$ strict, abelian input):** If $L$ is abelian and we restrict to the formal disc $C = \mathrm{Spec}\,\bC[[z]]$, then $\mathrm{R}\Gamma(D, L) = L \otimes \bC[[z]]$ (as a vector space) and the BD04 identification specialises to a statement about $\ChirHoch^\bullet$ of the factorization algebra. For Heisenberg $L = \bC J$, this gives the Poincaré $1 + t + t^2$ (Vol I `prop:derived-center-explicit(i)`): degree 0 is the vacuum, degree 1 is the level-deformation derivation $\xi_k$, degree 2 is the Koszul-dual generator $\eta$. The Vol III slogan "(1+t)^1" misses degrees 1 and 2.

### A4. Numerical summary of contradictions

| Algebra | Vol I `prop:derived-center-explicit` Poincaré | Vol III `prop:bar-ce-chiral` Poincaré | Total Vol I | Total Vol III |
|---|---|---|---|---|
| Heisenberg $\cH_k$ | $1 + t + t^2$ | $(1+t)^1 = 1 + t$ | 3 | 2 |
| Affine $\widehat{\fsl}_2$ at non-critical | $1 + 3t + t^2$ | $(1+t)^3 = 1 + 3t + 3t^2 + t^3$ | 5 | 8 |
| Virasoro $\mathrm{Vir}_c$ | $1 + t^2$ | $(1+t)^1 = 1 + t$ | 2 | 2 |

All three rows differ in Poincaré polynomial. The Virasoro row agrees on total but not on bar degree.

## Heal plan (Option-menu per AP266)

The honest structural move is the Beilinson sharpened-obstruction pattern: exhibit the precise failure as a computation-level discrepancy against a primary source, then downgrade the headline to the scope it actually supports.

### H1. Engine fix

- `compute/lib/chiral_ce_complex.py:1046-1054`: the `BarCEComparison.poincare_match` method must compute the BAR-SIDE Poincaré polynomial from a genuinely disjoint source (BD04 Theorem 4.8.1 derived global sections, or Vol I `prop:derived-center-explicit` direct values) and compare to the classical CE side. The current tautological comparison has to be replaced by a numerical equality check against the hard-coded Vol I values. Expected result on the honest check: **MISMATCH** at Heisenberg and $\widehat{\fsl}_2$, revealing the scope restriction.
- `compute/lib/chiral_ce_complex.py:32-40` docstring: the claim "Bar Poincare poly = (1+t)" for Heisenberg contradicts Vol I. Either (a) retract and document that the engine computes the classical CE, NOT the chiral bar, and rename accordingly to `classical_ce_of_generator_space.py`; or (b) rewrite to compute the actual chiral bar and verify $\{1, 1, 1\}$ for Heisenberg.
- `compute/tests/test_chiral_ce_complex.py:302-345`: tests asserting Poincaré $(1+t)^n$ for strict class-G/L algebras must be reclassified as tests of the **classical** generator-space CE, not the **chiral** bar of the envelope. Tests 302-345 as currently written are either (a) vacuous relabellings of CE self-equality, or (b) wrong if read as chiral-bar assertions.

### H2. Vol III chapter healing

- `cy_to_chiral.tex:3868-3886` (`prop:bar-ce-chiral`): downgrade `\ClaimStatusProvedHere{}` to `\ClaimStatusConjectured{}` with explicit scope: "the identification holds at the level of derived global sections on the curve, in the sense of BD04 Theorem 4.8.1; the naive pointwise identification of chiral bar with classical exterior CE FAILS at the OPE simple-pole structure, as witnessed by the Vol I computations for Heisenberg ($1+t+t^2$), $\widehat{\fsl}_2$ (total 5), Virasoro ($1+t^2$)".
- `quantum_chiral_algebras.tex:285-308` (`prop:bar-ce-identification`): rewrite the proof.
  - Line 300: replace "Loday-Vallette 2012, Theorem 10.1.6" with the correct "Loday-Vallette 2012, Proposition 3.3.6" and add Cartan-Eilenberg Ch. XIII §7 as a parallel classical reference. Add an explicit statement that this is the CLASSICAL bar-CE identification for $U(\fg)$, and the CHIRAL version requires BD04 Theorem 4.8.1.
  - Lines 304-306: retract numerics. Replace "Heis $\HH^\bullet = \{1,1\}$" with Vol I `{1,1,1}` and cite `prop:derived-center-explicit(i)`. Replace "sl_2 Poincaré $(1+t)^3$ total 8" with Vol I total 5 and cite `prop:derived-center-explicit(ii)`. Replace "Yangian Poincaré $(1+t)^3$" with an explicit scope statement: "for the strict-Lie truncation at class L; the chiral bar differs by the simple-pole structure of the W_{1+∞} OPE."
  - Replace `\ClaimStatusProvedHere` with `\ClaimStatusConditional` and attribution remark to Vol I.

### H3. Status-table healing

- Vol III `CLAUDE.md:107`: the entry "Chiral CE complex: PROVED B(U^ch(L)) = CE_*(L)" must downgrade to "NUMERICAL COINCIDENCE at class G / strict-L, CONJECTURAL otherwise. At the level of BD04 Theorem 4.8.1 (derived global sections): chiral homology of chiral envelopes matches CE of derived global sections; the NAIVE pointwise identification with exterior algebra of generator space is FALSE (contradicts Vol I `prop:derived-center-explicit`)".
- `AGENTS.md:176` and `AGENTS.md:1214`: same downgrade.
- `FRONTIER.md:834` (list of "10 proofs at publication standard"): remove "chiral CE complex" from the list, or add a scope caveat.
- Vol I `CLAUDE.md` "Vol III 6d hCS Session Cross-Awareness" section at line 1302 (where the claim appears verbatim): retract.

### H4. Primary-source inscription

Write a short section `subsec:bd04-chiral-envelope-ce-statement` in `quantum_chiral_algebras.tex` stating BD04 Theorem 4.8.1 **verbatim** (or as close to verbatim as permissible) with the derived-global-sections formulation, and list the two ingredients: (a) the genus-dependent $\mathrm{R}\Gamma(C, L)$ complex, (b) the CE differential on $\bigwedge^\bullet$ of this derived complex. This closes the AP272 (folklore citation) gap by inscribing the actual content of the cited theorem.

## New anti-patterns

### AP1041 (Classical-operad-of-generator-space masquerading as chiral-operad-of-factorization-envelope)

A formula valid for a finite-dimensional Lie algebra $\fg$ (classical enveloping $U(\fg)$, classical CE $\bigwedge^\bullet \fg$) is transported verbatim to the chiral setting by notational substitution: write $L$ for $\fg$, $U^{\mathrm{ch}}$ for $U$, and claim $B(U^{\mathrm{ch}}(L)) = \bigwedge^\bullet L$. The substitution fails because:

- $U^{\mathrm{ch}}(L)$ is an **infinite-dimensional** vertex algebra, not a finite-dim associative algebra; its bar complex $T^c(s^{-1} \bar A)$ has infinitely many generators, not $\bigwedge^\bullet L_{\mathrm{generator-space}}$;
- the correct "chiral CE" of BD04 is derived global sections $\mathrm{CE}(\mathrm{R}\Gamma(C, L))$, which at $g = 0$ still carries infinitely many modes, and at $g \geq 1$ picks up $H^1(C, L)$ contributions;
- the OPE simple-pole structure (higher products $a_{(n)} b$ for $n \geq 1$) contributes non-classically to the bar cohomology: level-deformation classes, central-charge classes, Koszul-dual generators, all absent in $\bigwedge^\bullet L_{\mathrm{gen}}$.

**Counter:** before writing $B(U^{\mathrm{ch}}(L)) = \mathrm{CE}_*(L)$, substitute **two** small test cases ($L$ abelian rank 1 = Heisenberg, $L$ simple = $\fsl_2$) and compute the chiral bar Poincaré polynomial from an independent Vol I source (`prop:derived-center-explicit` or `thm:main-koszul-hoch`); if the result differs from $(1+t)^{\dim L}$, the identification is false at the pointwise level and holds only at the derived-global-sections level. Healing: state BD04 Theorem 4.8.1 verbatim and restrict to that scope.

**Related:** AP274 (rhetorical functor identification across disjoint objects) is the sibling in the functor-level case; AP1041 is the bar-complex-level specialisation. AP289 (Künneth-multiplicative vs additive) is the sibling for product-structure confusion; AP1041 is the bar-vs-CE confusion.

### AP1042 (Tautological comparison of engine self-equality posing as cross-verification)

An engine advertises a "bar vs CE cross-check" via a method `comparison_match()` that returns `True` whenever a computed value equals itself. The implementation routes both sides of the comparison through the same underlying function; the check cannot fail. The advertised "verification" consists of re-running the same computation twice and asserting they agree. Under AP277 / AP287 nomenclature this is a structural tautology; under AP128 it is engine-test synchronization on the same wrong mental model. AP1042 distinguishes the variant where the tautology is **at the engine-library level**, not at the test-file level: the engine's own comparison method is self-equating before any test invokes it. Pre-heal instance: `compute/lib/chiral_ce_complex.py:1041-1054`, where `bar_poincare()` and `ce_poincare()` both return `self.ce.poincare_polynomial()`.

**Counter:** every engine "cross-check" method must route its two compared quantities through **two genuinely disjoint computations**. The disjointness must be visible at the AST level (different function calls, different data sources). Extend HZ-IV infrastructure: `assert_computational_paths_disjoint` should lint engine library methods in addition to test bodies.

**Related:** AP277 (vacuous HZ-IV test body behind sound decorator prose) at test layer; AP287 (structural impossibility primitive tautology) at primitive level; AP288 (label-disjoint computation-identical) at HZ-IV-decorator layer. AP1042 is the engine-internal-comparison layer — an upstream tautology that invalidates every downstream test.

### AP1043 (Section-number-plausible-but-wrong-theorem citation drift)

A proof body cites `\cite[Theorem N.M.K]{AuthorYear}` where the theorem number resolves within the cited text but names a theorem on a **different topic** than the proof step claims. Stronger than AP285 (alias section-number drift — the section number is a transcription error, but the cited content is the same object): AP1043 is the case where the cited section-number POINTS TO A REAL THEOREM, but that theorem is about something else entirely. Canonical violation: Vol III `quantum_chiral_algebras.tex:300` cites Loday-Vallette "Theorem 10.1.6" for $B(U(\fg)) \simeq \mathrm{CE}_*(\fg)$; LV Theorem 10.1.6 exists, is correct, and is about **Koszul duality for quadratic operads** (the operadic cobar-bar adjunction for $\mathcal{P}$-algebras), NOT about bar-CE for enveloping algebras. The classical bar-CE statement is LV Proposition 3.3.6 (or Cartan-Eilenberg Ch. XIII §7 in the original source).

**Counter:** every `\cite[Thm N.M.K]{X}` at a load-bearing step must (a) quote the cited theorem's statement verbatim in a comment or remark, (b) pattern-match the cited content against the inference the proof draws. If the cited theorem is about a different topic, the citation is wrong even if the number resolves. Pre-commit discipline: for every new `\cite[Thm X.Y.Z]{AuthorYear}`, grep the cited source's table-of-contents or index for the theorem number; compare the theorem title against the local context.

**Related:** AP272 (unstated cross-lemma via folklore citation — the paper does not state the lemma at all); AP285 (section-number transcription error — the drift is in the number, the content is right); AP309 (primary-source citation for a strictly weaker claim — the cited theorem is right but too weak). AP1043 is the case where the citation LOOKS precise (specific section number), RESOLVES to a real theorem, but POINTS TO THE WRONG THEOREM. Detection by pattern-match at citation-insertion time, not at resolution time.

### AP1044 (Verbatim-advertisement proliferation: same wrong claim in CLAUDE.md + AGENTS.md + FRONTIER.md)

A single load-bearing slogan "X PROVED" appears verbatim in three or more metacognitive files: CLAUDE.md, AGENTS.md, FRONTIER.md, notes/*.md, session ledgers. Each occurrence independently advertises "PROVED". A reader encountering any one of them treats it as a stable fact. When the underlying claim is retracted, the cross-file propagation is incomplete: two of the three files are updated, the third carries the stale advertisement, and subsequent AP271 (reverse drift) fires on the stale file. Canonical violation: "B(U^ch(L)) = CE_*(L) PROVED" appears at Vol III CLAUDE.md:107, CLAUDE.md:765, AGENTS.md:176, AGENTS.md:1214, FRONTIER.md:834 — five occurrences across three files. Vol I CLAUDE.md:1302 has a cross-volume awareness line that re-advertises the claim.

**Counter:** the source of truth for any "PROVED" status is the `.tex` theorem body plus the `\ClaimStatus*` tag. Metacognitive files (CLAUDE.md, AGENTS.md, FRONTIER.md, notes) are **derivative** and must cite the source `.tex` label when repeating a status claim. Enforcement: pre-commit gate that for every "PROVED" line in a metacognitive file, a `grep` for the `\label{...}` of the cited theorem returns a live `.tex` inscription with matching `\ClaimStatus*` tag. On retraction, the propagation step is not optional: atomic in the same commit per AP5.

**Related:** AP149 (resolution-propagation failure across files); AP256 (aspirational-heal drift); AP271 (reverse drift CLAUDE.md vs manuscript); AP304 (concurrent-agent AP-numbering collision in shared metacognitive file). AP1044 is specifically the **verbatim multi-file advertisement** pattern: the slogan is copy-pasted across three to five files, making retraction a multi-point commit. Stronger than AP149 because AP1044 catches the case where the proliferation was deliberate (canonical status-table maintenance) rather than accidental.

## Infrastructure notes

- This attack was performed WITHOUT an isolation worktree; no uncommitted heals are at risk of stranding (AP316 preventative).
- The engine code `compute/lib/chiral_ce_complex.py` was not modified by this attack-heal pass; only the report + AP inscriptions are delivered. Healing H1 (engine fix) and H2 (chapter healing) are left for follow-up by a subsequent swarm agent or main-thread rectification pass. This avoids AP266 sharpened-obstruction without load-bearing cascade on the live test suite.
- The five primary-source ingredients of the correct statement (BD04 Theorem 4.8.1 + LV Prop 3.3.6 + Cartan-Eilenberg Ch. XIII + Frenkel-Ben-Zvi §18 + Quillen 1969 Appendix B) have been enumerated but not yet inscribed.

## Next-wave recommendations

1. Agent to execute H1 (engine retrofit) with falsification test at Heisenberg and $\fsl_2$ Vol I values; expected outcome: the current engine fails; retagged as `classical_ce_of_generator_space.py`.
2. Agent to execute H2 (Vol III chapter downgrades); atomic commit with CLAUDE.md / AGENTS.md / FRONTIER.md propagation (AP1044 atomic discipline).
3. Agent to execute H4 (primary-source inscription of BD04 Theorem 4.8.1) as a Vol I chapter inscription (natural home: `bar_construction.tex` where BD04 is already cited correctly at line 440).

## Signatures

Author: Raeez Lorgat, 2026-04-18.
AP reservation honoured: AP1041-AP1044 of reserved block AP1041-AP1060; AP1045-AP1060 released for subsequent wave reuse per AP306 block-reservation discipline.
No AI attribution.
