# Attack-then-heal: PBW degree vs conformal weight disambiguation (AP64/AP75) audit

Date: 2026-04-18.
Scope: Light adversarial audit of Vol I, focused on:
  (i) co-occurrences of "PBW degree" and "conformal weight";
  (ii) `thm:pbw-koszulness-criterion` scope discipline;
  (iii) "bar cohomology concentrated in degree 1" qualifier hygiene;
  (iv) Theorem H "chiral Orlik-Solomon" route (AP128 heal) for grading discipline.

Author: Raeez Lorgat.

## Summary verdict

**No genuine AP64/AP75 drift discovered.** The programme's grading discipline is intact at the proof-body level. Three observations of varying severity:

- **F1 (CLEAN):** `thm:pbw-koszulness-criterion` (chapters/theory/chiral_koszul_pairs.tex:787-811) properly distinguishes PBW degree, bar degree, and conformal weight in hypotheses and proof. Hypothesis (iii) names "bar degree $n$ and conformal weight $h$" explicitly.
- **F2 (TERMINOLOGICAL, NOT DRIFT):** The slogan "bar concentrated in weight 1" in `ftm_seven_fold_tfae_platonic.tex` uses "weight" as a LOCAL ALIAS for bar degree, defined explicitly at the definition site (lines 99-106). The reader is told "the weight grading coinciding with bar degree." This is a terminological landmine (same word "weight" is also the universal name for CONFORMAL WEIGHT elsewhere) but not a mathematical drift.
- **F3 (AP236 VIOLATION, peripheral, build-neutral):** `chapters/examples/bar_complex_tables.tex` carries 4 instances of `\ap{62}` / `\ap{63}` in typeset prose (lines 4136, 4172, 4187, 4207). Manuscript-metadata-hygiene violation per CLAUDE.md. Out of scope for this audit; flagged for separate heal.

No new APs registered; no heals applied in this session.

## (i) PBW degree / conformal weight co-occurrence

Files with both terms co-occurring (Vol I chapters/ + standalone/):
- `chapters/theory/chiral_koszul_pairs.tex:787-811` (`thm:pbw-koszulness-criterion`)
- `chapters/examples/bar_complex_tables.tex` (witness tables, e.g. :1939)
- `chapters/theory/computational_methods.tex` (e.g. :779-781)
- `chapters/theory/higher_genus_modular_koszul.tex` (PBW all-genera propagation theorems)

In every co-occurrence inspected, the two terms are correctly distinguished:
- "PBW degree" / "PBW filtration" refers to the mode-count filtration $F_p$.
- "Conformal weight" / "weight $h$" refers to the Virasoro $L_0$-eigenvalue.
- "Bar degree" refers to the tensor-power index on $T^c(s^{-1}\bar\cA)$.

No sentence in the scanned corpus conflates the three.

## (ii) thm:pbw-koszulness-criterion spot-check

Inscribed at `chapters/theory/chiral_koszul_pairs.tex:787-811`. Status-table cites :784 (off by 3 lines from `\label`, acceptable). Label resolves; proof body follows immediately (:813-857) with PBW-filtered spectral sequence, $E_0 = \operatorname{gr}_F K$, collapse at $E_1$ by classical Koszulness hypothesis.

Hypotheses:
1. (flat) PBW filtration, each $F_p / F_{p-1}$ free of finite rank in each conformal weight.
2. (classical Koszul) $\operatorname{gr}_F \cA$ is classically Koszul.
3. (bounded) $\barBgeom^n_h(\cA)$ finite-dimensional for each BAR DEGREE $n$ and CONFORMAL WEIGHT $h$.

The three-way distinction (PBW degree = filtration index; bar degree = tensor-power index; conformal weight = $L_0$-eigenvalue) is enacted cleanly.

Remark `rem:pbw-vs-diagonal-critical` (:1477-1509) explicitly handles the subtle critical-level point: PBW $E_2$-collapse is $k$-independent, but DIAGONAL Ext concentration fails at $k = -h^\vee$ because $H^0(\barB(V_{-h^\vee}(\fg))) = \operatorname{Fun}(\Op) \neq \bC$. This is model AP75 discipline: PBW-Koszulness vs. Ext-diagonal Koszulness are distinguished as conditions (ii) and (iv) of `thm:koszul-equivalences-meta`.

## (iii) "Bar cohomology concentrated in degree 1" qualifier hygiene

Eleven prose sites inspected. Pattern:

- "bar cohomology concentrated in degree~$1$" (preface.tex:585, bar_cobar_adjunction_inversion.tex:2151, garland_lepowsky.tex:155, shadow_towers_v2.tex:146, chiral_chern_weil.tex:1657): In each case the surrounding paragraph names the degree convention (bar degree, with the Koszul-diagonal collapse). `bar_cobar_adjunction_inversion.tex:2144-2151` is especially clear: "PBW/bar spectral sequence collapses at $E_2$; ... $H^*(\barB_X(\cA))$ concentrated on the Koszul diagonal (bar degree equal to internal degree, or after the reindexing... concentrated in bar degree 1)".

- "bar concentrated in weight 1" (ftm_seven_fold_tfae_platonic.tex:21,106,382,608; algebraic_foundations.tex:2470; N1_koszul_meta.tex:1131; five_theorems_modular_koszul.tex:817): "weight" here is LOCAL ALIAS defined at ftm_seven_fold_tfae_platonic.tex:99-106 as bar degree (= bigrading second index $p$). Slogan form; not mathematical drift.

**Terminological risk (not drift):** the same word "weight" is used in two senses across the programme:
  (a) BAR DEGREE, in the Priddy/Koszul slogan "concentrated in weight 1" (alias convention, defined at FTM7 site).
  (b) CONFORMAL WEIGHT $h$ = Virasoro $L_0$-eigenvalue, used universally (and correctly) in every hypothesis and witness table (e.g. `chiral_koszul_pairs.tex:1107` "$\dim H^2 = 5$ (concentrated at weight $h = 3$)").

Sense (a) and sense (b) coexist in `bar_complex_tables.tex:1939`: "$H^2_{\mathrm{CE}} = 5$ (all at weight~$3$: ...)" — here "weight $3$" is CONFORMAL WEIGHT (the $h=3$ stratum where $\{L_{-3}, L_{-2}L_{-1}, \ldots\}$ live), NOT bar degree. Context disambiguates but the same word does double duty. A global rename is not warranted for this audit — the terminological double-duty is explicit in the FTM7 definition and disambiguated in context at every witness site.

## (iv) Theorem H chiral Orlik-Solomon route grading check

Theorem `thm:hochschild-concentration-E1` at `chapters/theory/chiral_hochschild_koszul.tex:1370-1391` states ChirHoch^n(A) = 0 for $n \notin \{0,1,2\}$. Proof chain (`lem:chiral-homotopy-transport`:1258-1341 + main proof :1393-):

- Pure-braid arrangement $A_{m-1}$: supersolvable → Shelton-Yuzvinsky Koszulity of $\operatorname{OS}(A_{m-1})$.
- Koszul property yields Priddy homotopy $h_m$ on $\operatorname{OS}(A_{m-1})^{\geq 1}$ (this is OS-GRADING, = PBW degree of the quadratic OS algebra, equivalently the form-degree on $\FM_m(\C)$).
- Transport through Fresse map $\sigma$ to chiral bar complex $\barB^{\mathrm{ord}}_\bullet(\cA)|_{\FM_m(\C)} \simeq \operatorname{OS}(A_{m-1}) \otimes \cA^{\otimes m}$.
- Apply to Theorem H by spectral-sequence argument on collision depth.

Grading discipline in this chain:
  - OS-grading = PBW degree in $\operatorname{OS}(A_{m-1})$ (quadratic Koszul algebra on Arnold generators).
  - Tensor factor grading $\cA^{\otimes m}$ carries its OWN internal conformal weight, independent of OS-grading.
  - ChirHoch degree = COHOMOLOGICAL degree on the full bar complex.

**Verdict:** The AP128 heal (Heisenberg $H^2 = 5$ not $6$, via chiral OS) uses OS-degree (= PBW degree = form degree on $\FM_m(\C)$), NOT conformal weight, and the chain-level transport preserves the distinction. `sl_2 bar_H^2 = 5` is the bar-degree-2 bar cohomology (at conformal weight $h=3$, per `chiral_koszul_pairs.tex:1107`). Two independent gradings, cleanly separated.

## Peripheral finding: AP236 residual in bar_complex_tables.tex

`chapters/examples/bar_complex_tables.tex` contains 4 instances of the forbidden `\ap{NN}` token in typeset prose:
- :4136 — `(\ap{63}): the chiral bar complex ...`
- :4172 — `$H^2 = 5$ (not $6$; \ap{63}) &`
- :4187 — (truncated in grep; part of the same table)
- :4207 — `\ap{62}: the generating functions here record ...`

These are AP236 violations (blacklist-slug leakage into typeset parenthetical). Build-neutral (the `\ap` macro if defined prints a number; if undefined prints nothing with a warning). Out of scope for this audit; registered as a separate heal target. Heal template: delete the `\ap{NN}` tag, keep the mathematical substance of the surrounding sentence.

## Audit trail

Files read end-to-end (relevant excerpts):
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex` (lines 770-970; :1100-1150; :1430-1510).
- `/Users/raeez/chiral-bar-cobar/chapters/theory/ftm_seven_fold_tfae_platonic.tex` (lines 1-140).
- `/Users/raeez/chiral-bar-cobar/chapters/theory/algebraic_foundations.tex` (lines 2460-2490).
- `/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_inversion.tex` (lines 2130-2170).
- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_hochschild_koszul.tex` (lines 1260-1420).
- `/Users/raeez/chiral-bar-cobar/standalone/N1_koszul_meta.tex` (lines 1120-1145).
- `/Users/raeez/chiral-bar-cobar/chapters/frame/preface.tex` (lines 575-605).
- `/Users/raeez/chiral-bar-cobar/chapters/examples/landscape_census.tex` (lines 2660-2680; :3068-3085).
- `/Users/raeez/chiral-bar-cobar/chapters/examples/bar_complex_tables.tex` (spot-checks for `\ap{NN}`).

Greps:
- `PBW degree` (Vol I): zero files returned (Grep treats the phrase with strict spacing; "PBW" + "degree" co-occurrence exists in chiral_koszul_pairs.tex at :124,:649,:806,:1163,:1188 under varied phrasings).
- `bar cohomology concentrated` (Vol I): 11 hits, all scope-correct.
- `pbw-koszulness-criterion` label: 1 `\label{}` inscription (chiral_koszul_pairs.tex:788); 40+ `\ref{}` consumers across chapters, standalones, concordance; all resolve.
- `Shelton-Yuzvinsky` in chiral_hochschild_koszul.tex: proof body cites at :1273 and :1403 (correctly attributing OS Koszulity).
- `\ap\{[0-9]+\}` in chapters/: 4 hits in 1 file (bar_complex_tables.tex).

## No APs registered, no cache entries added

Per the MINIMAL-inscription mandate (AP314 budget), this audit surfaced no genuine AP64/AP75 drift, hence no new APs registered in the AP1321-AP1340 block. The terminological-risk observation (F2) is catalogued in this report only; it does not rise to AP-level because:
  - the alias convention is EXPLICITLY defined at its use site,
  - every witness table disambiguates via context,
  - no mathematical proof step depends on the naming.

The AP236 observation (F3) is a separate pre-existing anti-pattern; no new AP needed.

Verdict: audit returns CLEAN on grading discipline. Zero heals applied.
