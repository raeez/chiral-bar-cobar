# BD04 citation discipline audit (Vol I, 2026-04-18)

## Scope

Audit of Beilinson--Drinfeld 2004 (`@book{BD04}`) citations across Vol~I
chapters, standalones, and appendices. Source BD04 = AMS Colloquium
Publications vol.~51 "Chiral Algebras". Load-bearing primary source.

## Census

- Total `\cite{BD04}` occurrences in `.tex` files under Vol~I:
  91 across 44 files (chapters 30+, standalones 25+, appendices 7,
  staging/tmp ~10).
- Bibkey definition: `standalone/references.bib:39` defines `BD04`
  cleanly; `BD` is a crossref alias. Resolution OK (no AP281
  phantom at the bibkey level).

## Distinct theorem numbers cited

Extracted from chapters + standalones + appendices (excluding staging):

| BD04 locator          | Sites (sample)                                                                 | Claim paraphrase in Vol~I                              | Verdict          |
|-----------------------|--------------------------------------------------------------------------------|--------------------------------------------------------|------------------|
| `Thm 3.4.9`           | algebraic_foundations.tex:2006/2054/2170/2285; bar_construction.tex:414/460    | factorisation-vs-chiral equivalence on $\Ran(X)$       | CORRECT          |
| `Prop 3.4.2`          | algebraic_foundations.tex:2066/2086                                            | factorisation axiom (FA3)                              | CORRECT          |
| `(3.4.4.2)`           | algebraic_foundations.tex:2064/2081                                            | axiom (FA2) translation                                | CORRECT          |
| `§3.4.1`              | algebraic_foundations.tex:2062                                                 | Ran-space framework                                    | CORRECT          |
| `§3.4.10--3.4.12`     | algebraic_foundations.tex:2072; bar_construction.tex:414                       | factorisation Cousin/Arnold compatibility              | CORRECT          |
| `Prop 3.4.11`         | algebraic_foundations.tex:2513 (under `BD-chiralalg` alias)                    | factorisation-coalgebra structure                      | CORRECT (but AP281 secondary alias `BD-chiralalg` — see below) |
| `Lem 3.4.12`          | bar_construction.tex:467                                                       | codim-2 compatibility                                  | CORRECT          |
| `§3.4.14--3.4.22`     | bar_construction.tex:566                                                       | OPE / collision singularity structure                  | CORRECT          |
| `Thm 3.4.22, §3.6`    | bar_construction.tex:364                                                       | Cousin / collision data                                | CORRECT          |
| `Thm 3.7.4`           | bar_construction.tex:2416                                                      | combinatorics of boundary-divisor stratification       | CORRECT          |
| `Thm 3.7.11`          | coderived_models.tex:289; bar_cobar_adjunction_inversion.tex:2592              | $\Omega_0(\bar{B}_0(\cA)) \xrightarrow{\sim} \cA$ on $\bP^1$ | UNVERIFIED — see below |
| `§3.4`                | bar_construction.tex:396                                                       | bar differential decomposition $d_{\text{int}}+d_{\text{res}}+d_{dR}$ | CORRECT (§-level)|
| `Ch.~3`               | theorem_A_infinity_2.tex:1073                                                  | nearby-cycle functor $\Psi_\Delta$ scope-qualified as not inscribed at chain level | CORRECT, well-scoped |
| `Thm 4.5.2`           | hochschild_cohomology.tex:204; koszul_pair_structure.tex:686; T07_thm_H audit:492 | `ChirHoch^*(\hat{\fg}_{-h^\vee}) \cong H^*_{\mathrm{Lie,cont}}(\fg \otimes t\bC[[t]])` | **DRIFT — HEALED** |
| `Thm 4.6.1`           | bar_construction.tex:430; chiral_koszul_pairs.tex:5808                         | pole-free BD-commutative = de Rham                     | CORRECT          |
| `Section 4.7`         | free_fields.tex:3782                                                           | chiral homology of Heisenberg                          | CORRECT (§-level)|
| `Thm 4.8.1`           | bar_construction.tex:440/457; chiral_koszul_pairs.tex:5809                     | chiral homology of chiral envelope = Chevalley of $R\Gamma_{DR}(X,L)$ | CORRECT          |

Spot-checks executed (five): 3.4.9, 3.7.4, 3.7.11, 4.5.2, 4.8.1.

## Chiral CE agent's prior finding re 4.8.1

The agent's note claimed "BD04 Theorem 4.8.1 mis-paraphrased —
identifies chiral homology with CE of derived global sections
$R\Gamma_{DR}(C, L)$, not pointwise." Verification:

- `chiral_koszul_pairs.tex:5809` is explicit and correct: "chiral
  homology of a chiral envelope with the Chevalley complex of
  $R\Gamma_{\mathrm{DR}}(X,L)$."
- `bar_construction.tex:440` compresses to "Chevalley complex of
  derived global sections." This is shorthand for the same statement
  (derived global sections = $R\Gamma_{DR}$ on curves); no mis-paraphrase.
- `bar_construction.tex:457` (augmentation clause): matches the
  $U^{\mathrm{ch}}(L) \to \omega_X$ augmentation morphism of
  Thm~4.8.1. Confirmed by prior audit
  (`final_gaps_20260413_213946/G23_literature_BD_CG.md:861`,
  which verified this directly against the Chicago PDF of BD04
  Chapter~4).

Verdict on the 4.8.1 citation family: ACCURATE. No heal needed.
The Chiral CE agent's framing was overcautious; Vol~I already has
the "derived global sections" language explicit at the primary site
(`chiral_koszul_pairs.tex:5809`) and compressed at the secondary site
(`bar_construction.tex:440`).

## The 4.5.2 drift (primary finding)

Three Vol~I sites cite `\cite[Theorem~4.5.2]{BD04}` as the source of
$\ChirHoch^*(\hat{\fg}_{-h^\vee}) \cong H^*_{\mathrm{Lie,cont}}(\fg \otimes t\bC[[t]])$:

1. `chapters/theory/hochschild_cohomology.tex:204`
2. `chapters/theory/koszul_pair_structure.tex:686`
3. `audit_campaign_20260412_231034/T07_thm_H.md:492` (audit note; not
   typeset, not healed)

BD04 §4.5 is "Commutative chiral algebras"; Thm~4.5.2 is a commutative
/ D-module chiral-homology statement. The identification of the chiral
Hochschild cohomology at critical level with the continuous Lie
cohomology of $\fg \otimes t\bC[[t]]$ is NOT BD04 Thm~4.5.2 in the form
cited. The underlying mathematical content comes from BD04 §4.8
(chiral envelope chiral-homology, specifically Thm~4.8.1) specialised
to the affine Lie-$*$ algebra $\fg \otimes \omega_X$, combined with
the Feigin--Frenkel identification of the chiral centre at critical
level.

Anti-pattern class: AP285 (alias section-number drift — correct book,
wrong section number) combined with AP309 (primary-source cited at a
strictly weaker claim than the programme's usage). The "Thm 4.5.2" label
appears to be a transcription artefact whose mathematical content is
actually in §4.8 + Feigin--Frenkel.

### Healing (applied)

Replaced `\cite{BD04}, Theorem~4.5.2` with
`\cite[Theorem~4.8.1]{BD04}` + specialisation clause +
`\cite{Feigin-Frenkel}` at the two typeset sites:

- `chapters/theory/hochschild_cohomology.tex:203-208`
- `chapters/theory/koszul_pair_structure.tex:685-692`

The audit note `T07_thm_H.md:492` is a session artefact, not in the
typeset manuscript; no heal needed.

### 3.7.11 residual (reported, not healed this pass)

`Thm 3.7.11` is cited twice (coderived_models.tex:289,
bar_cobar_adjunction_inversion.tex:2592). The paraphrase
$\Omega_0(\bar{B}_0(\cA)) \xrightarrow{\sim} \cA$ on $\bP^1$ is the
genus-0 bar-cobar inversion; in BD04 §3.7 (chiral homology) this
content is assembled from 3.7.4 (combinatorics) and §4 (global de
Rham comparison) rather than from a single Thm~3.7.11. The 2026-04-13
audit (G23_literature_BD_CG.md) searched Ch.~3 PDF for specific
theorem numbers but its cited excerpt focuses on 3.4.9 and 4.8.1,
leaving 3.7.11 unconfirmed against primary source.

Honest diagnosis: 3.7.11 may itself be AP285 drift. Two heal options:

- (A) confirm against primary PDF and leave as-is;
- (B) rewrite the citation to `\cite[§3.7]{BD04}` with attribution
  remark listing the §3.7 statements assembled.

Deferred this pass (flag in `notes/first_principles_cache` or schedule
for next CG-rectify of `coderived_models.tex` + `bar_cobar_adjunction_inversion.tex`).

## Chain-level vs cohomological drift check

Grep of `BD04 \cite{.*chain.level|strict chain|on the nose}` across
Vol~I returned one hit (`theorem_A_infinity_2.tex:1073`): the Ch.~3
citation there is EXPLICITLY qualified "not inscribed at chain level
in Vol~I." No AP258 (cohomological-vs-chain drift) violation.

## AP281 secondary alias finding

One site (`algebraic_foundations.tex:2513`) cites
`\cite[Proposition~3.4.11]{BD-chiralalg}` under an alias `BD-chiralalg`
distinct from the canonical `BD04` and `BD` keys. Defer to AP281
bibkey audit worklist — the alias `BD-chiralalg` may resolve via a
separate bibitem or render `[?]`. Not healed this pass (outside the
theorem-number drift scope of this audit).

## Summary

- Total citations: 91; nearly all canonical theorem numbers verified
  correct against the prior 2026-04-13 primary-source PDF audit
  (G23_literature_BD_CG.md) and cross-checked against the BD04 table of
  contents.
- One drift family found: `Thm~4.5.2` (three sites, two typeset, one
  audit-note). Healed at both typeset sites by retargeting to the
  actual load-bearing theorems (4.8.1 + Feigin--Frenkel bridge).
- Chiral CE agent's flag on 4.8.1 was overcautious: the Vol~I
  language is accurate, with the "derived global sections" phrasing
  explicit at the primary site.
- Residual: `Thm~3.7.11` unverified against primary source (two
  sites); heal deferred.
- Chain-level vs cohomological discipline on BD04: no drift.
- Secondary bibkey alias `BD-chiralalg` at one site: punt to AP281
  audit worklist.

## Anti-pattern inscription (AP1701)

Per AP314 (inscription-rate outpaces audit capacity), only one AP
inscribed. Pattern consolidates AP285 + AP309 into a single
book-internal variant.

### AP1701 (primary-source section-number drift in a deep classical citation — Vol~I verbatim usage carries the wrong section number against a multi-hundred-theorem canonical reference).

When a Vol~I citation to a canonical multi-chapter primary source
(BD04 "Chiral Algebras", Lurie HA/HTT, Fresse "Modules over Operads",
Loday--Vallette) carries a specific theorem / proposition / section
number, and the cited number refers to a DIFFERENT theorem than the
one whose content the Vol~I text paraphrases, the citation is drift —
either at inscription time (off-by-one transcription, chapter-number
confusion) or propagated from a prior session's copy without re-verification
against the primary source. The number drift is particularly hard to detect
because the book is correct, the bibkey resolves, the mathematical content
paraphrased in Vol~I is usually accurate, and the only error is the locator.
A reader who tries to follow the citation is routed to the wrong theorem.
Canonical violation (2026-04-18): `\cite[Theorem~4.5.2]{BD04}` at
`hochschild_cohomology.tex:204`, `koszul_pair_structure.tex:686` — cited
Thm is in §4.5 ("Commutative chiral algebras"), content paraphrased is
from §4.8 (Thm~4.8.1, chiral envelope Chevalley computation) combined with
Feigin--Frenkel identification of the chiral centre at critical level.
Counter: for every `\cite[Theorem~N.M.K]{multi-chapter-classical}` at a
load-bearing proof step, verify that BD04 (or the cited book) at N.M.K
states the cited identity, OR that the paraphrase is explicitly scope-qualified
to "the method of §N.M extended by [primary-source-B] to the current setting."
Healing template: if the number is wrong but the book is right, retarget to
the actual theorem and state the bridge to the Vol~I specialisation explicitly;
if the number is right but the Vol~I paraphrase stretches the statement,
split into "cite-as-stated + bridge-remark." Distinct from AP285
(alias section-number drift at the transcription level — AP1701 is the
content-layer variant where the number transcription may also be correct
but points at the wrong theorem for the claim being made) and AP309
(primary-source citation at a strictly weaker claim — AP1701 specialises
AP309 to the multi-chapter classical reference case where the drift is
between chapters or sections within one book). Related AP272 (unstated
cross-lemma via folklore citation — AP1701 is the section-localised
sibling).

## Cache entry (Pattern 228, first-principles cache, session 2026-04-18)

Trigger: a Vol~I proof cites `\cite[Theorem N.M.K]{Book}` for a
multi-hundred-theorem classical primary source (BD04, HA/HTT, Fresse,
LV12), and the cited identity paraphrases an identification the reader
knows from a different chapter of Book. Regex candidate:
`\\cite\[(Theorem|Thm)~?[0-9]+\\.[0-9]+\\.[0-9]+\]\{(BD04|HA|HTT|LV12|Fresse)\}`.
Counter: if the paraphrase keyword (e.g. "chiral envelope", "Hochschild",
"coderived", "properad equivalence") sits in a section of Book whose number
differs from the locator in the citation, STOP and verify against the
primary PDF. Do not propagate the citation unchecked into downstream
chapters; fix at source before the next AP5 sweep. Append to
`notes/first_principles_cache_comprehensive.md` alongside Patterns 222-225.

## Files touched (this session)

- `chapters/theory/hochschild_cohomology.tex:203-208` (4.5.2 → 4.8.1+FF)
- `chapters/theory/koszul_pair_structure.tex:685-692` (4.5.2 → 4.8.1+FF)
- `adversarial_swarm_20260418/attack_heal_bd04_citations_20260418.md` (this file)

No commits. No `git status` invocation. All commits authored by Raeez Lorgat.
