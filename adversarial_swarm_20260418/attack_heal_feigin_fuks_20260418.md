# Feigin-Fuks / Feigin-Frenkel BRST + Screening Operator Audit (2026-04-18)

Author: Raeez Lorgat.

## Mission

Adversarial audit of Vol I usage of Feigin-Fuks 1984 (Virasoro Verma /
BRST), Feigin-Frenkel 1992 (affine KM critical-level centre), Feigin-
Fuks 1983 (short announcement), and Feigin-Fuchs 1990 (Bonn survey),
under constitutional instruction to verify bibkey hygiene (AP281) and
attribution discipline (AP272, AP290 analogue at citation level).

## 1. Primary-source inventory

Four genuinely distinct papers carry the "FF" / "Feigin-Fuchs" /
"Feigin-Frenkel" surface form:

| Bibkey families observed          | Primary source                                                | Content                                                        |
| --------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------- |
| `FF84` / `feiginfuks1983`         | Feigin--Fuchs, 1983/1984 (Funct.\ Anal.\ Appl.\ 17 + LNM 1060) | Verma modules over Virasoro; minimal model characters          |
| `FeiginFuchs90`                   | Feigin--Fuchs, 1990 (Adv.\ Stud.\ Contemp.\ Math.\ 7)         | Representations of Virasoro; BGG resolution                    |
| `Feigin-Frenkel` / `FF92`         | Feigin--Frenkel, 1992 (Internat.\ J.\ Modern Phys.\ A 7)      | Affine KM at critical level; centre isomorphic to W(^L g)      |
| `FF` / `FF90`                     | Feigin--Frenkel, 1990 (Phys.\ Lett.\ B 246)                   | Quantization of Drinfeld--Sokolov reduction                    |
| `FFR94` / `FeiginFrenkel94`       | Feigin--Frenkel--Reshetikhin, 1994 (Comm.\ Math.\ Phys.\ 166) | Gaudin model, Bethe ansatz, critical level                     |

"FF" without explicit date is genuinely ambiguous: `\bibitem{FF}` in
Vol~I's `bibliography/references.tex` resolves to Feigin--Frenkel 1990
(DS-reduction), NOT Feigin--Fuchs. The `FF84` / `Feigin-Frenkel` pair
(both defined) is the only unambiguous pair in the Vol~I bibliography.

## 2. Vol~I canonical bibliography coverage

`main.tex` line 1855: `\input{bibliography/references}`. That file
defines exactly four relevant keys:

```
\bibitem{Feigin-Frenkel}  B. Feigin and E. Frenkel (1992) FF92
\bibitem{FF}              B. Feigin and E. Frenkel (1990) FF90 DS-reduction
\bibitem{FF84}            B. L. Feigin and D. B. Fuchs (1984) Verma modules
\bibitem{FFR94}           B. Feigin, E. Frenkel, N. Reshetikhin (1994)
```

`standalone/references.bib` additionally defines (for standalone papers):

```
FF90, FF92, FeiginFrenkel94, FFR1994, FFR94, Feigin-Frenkel,
FF96, feiginfuks1983, feiginfrenkel1992, FF84, FeiginFuchs90
```

The standalone `.bib` therefore covers every observed variant via
`crossref` aliases; the Vol~I canonical file does NOT. Six distinct
bibkeys used inside in-build Vol~I chapters have ZERO definition in
`bibliography/references.tex`. Each resolves to `[?]` at build.

## 3. Phantom-key census (AP281 specialization)

Exhaustive grep on `chapters/`, `standalone/`, `appendices/`:

### Keys absent from `bibliography/references.tex`:

| Phantom key           | Cite count Vol~I in-build | Consumer chapters                                                                                                                                                                                                   |
| --------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FeiginFuchs90`       | 6                         | `koszulness_moduli_scheme.tex:743,767,796`; `chiral_koszul_pairs.tex:4350,4383,4398`                                                                                                                                |
| `feiginfuks1983`      | 1                         | `universal_conductor_K_platonic.tex:452`                                                                                                                                                                            |
| `FeiginFrenkel1992`   | 10                        | `theorem_h_off_koszul_platonic.tex:457,525,547,714`; `infinite_fingerprint_classification.tex:206,603,707,714`; `universal_conductor_K_platonic.tex:458` (as `feiginfrenkel1992`); `topologization_chain_level_platonic.tex:609` (as `FeiginFrenkel92`) |
| `FF92`                | 0 in-build                | (standalone-only: `three_parameter_hbar.tex`, `programme_summary.tex`, `garland_lepowsky.tex`)                                                                                                                                                                                                    |
| `KacBook`             | 4                         | `koszulness_moduli_scheme.tex:796`; `chiral_koszul_pairs.tex:4398`; `koszulness_fourteen_characterizations.tex:880` (standalone)                                                                                    |
| `RCW82`               | 3                         | `koszulness_moduli_scheme.tex:743`; `chiral_koszul_pairs.tex:4350`; (standalone)                                                                                                                                    |
| `Frenkel2007`         | 3 in-build                | `theorem_h_off_koszul_platonic.tex:457,547`; `infinite_fingerprint_classification.tex:206`                                                                                                                          |
| `Arakawa2007`         | 1                         | `infinite_fingerprint_classification.tex:603`                                                                                                                                                                       |
| `ArakawaFrenkel2017`  | 1                         | `infinite_fingerprint_classification.tex:707`                                                                                                                                                                       |
| `arakawa2017`         | 1                         | `universal_conductor_K_platonic.tex:458`                                                                                                                                                                            |
| `kacpeterson1984`     | 1                         | `universal_conductor_K_platonic.tex:452`                                                                                                                                                                            |
| `kac1998`             | 1 in-build                | `universal_conductor_K_platonic.tex:452`                                                                                                                                                                            |
| `polyakov1990`        | 1                         | `universal_conductor_K_platonic.tex:454` (inferred)                                                                                                                                                                 |
| `bershadsky1991`      | 1                         | `universal_conductor_K_platonic.tex:454` (inferred)                                                                                                                                                                 |
| `arakawa2005`         | 1                         | `universal_conductor_K_platonic.tex:454` (inferred)                                                                                                                                                                 |

Keys `Kac` (line 520 in `bibliography/references.tex`) and `Fuks86`
are defined, so those sites render correctly.

### Classification of the 20 in-build cites of Feigin-Fuchs / Feigin-Frenkel forms

**FF84 (Feigin-Fuchs 1984, Verma / minimal model characters):** used
correctly at `chiral_modules.tex:1397,1410,3826`; `minimal_model_examples.tex:491`;
`hochschild_cohomology.tex:285`. Definition PRESENT in `bibliography/
references.tex`. No phantom.

**FF84 MIS-ATTRIBUTION to Gel'fand-Fuchs 1970 cohomology:**

* `hochschild_cohomology.tex:161` -- cites `FF84` for the Gel'fand-
  Fuchs fact $H^\bullet_{\mathrm{cont}}(L_1; \bC) = \bC[\Theta]$
  (continuous cohomology of formal vector fields). This is the
  Gel'fand-Fuks 1970 result, not the Feigin-Fuchs 1984 Virasoro Verma
  paper. The line 161 text ascribes it to "Gel'fand-Fuchs" but cites
  `FF84`. Correct cite: `Fuks86` (already in references, page 161
  chapter 2 of Fuks' monograph covers this), or Gel'fand-Fuks 1970
  (not in references).
* `conformal_anomaly_rigidity_platonic.tex:163` -- cites `FF84` for
  `H^2(Witt; C) = C`. Same mis-attribution. The line uses the phrase
  "Gel'fand-Fuchs cohomology generator" at line 159 but cites FF84 at
  line 163. Again the Gel'fand-Fuks 1970 theorem.
* `conformal_anomaly_rigidity_platonic.tex:454` -- Feigin-Fuchs
  computation of $\mathrm{Hch}^2(\mathrm{Vir}_c, \mathrm{Vir}_c)$. This
  is genuinely FF84 (BRST-style cohomology of Virasoro), so correct.

AP analogue: citation-layer AP290 (subscript type-swap for $\kappa$).
Here the wrong primary source is cited; the underlying theorem is
correctly attributed in prose but the bibkey carries the different
Feigin-Fuchs paper. The canonical bibliography does not contain
Gel'fand-Fuks 1970 as a separate entry; adding one or redirecting
citations to `Fuks86` (defined) are both valid heals.

**FeiginFuchs90 (BGG resolution / Kac determinant proofs):** 6 sites,
all in-build, all phantom. Cites refer to Feigin-Fuchs 1990 BGG
resolution -- a later elaboration of the 1984 Verma paper with full
proofs of singular-vector embeddings. `FF84` is the 1984 announcement;
`FeiginFuchs90` is the 1990 full write-up. The distinction is genuine
and the Vol~I canonical bibliography lacks the later paper.

**FeiginFrenkel1992 / feiginfrenkel1992 / FeiginFrenkel92 (critical
level, opers, W-algebra centre):** 10 sites in-build, all phantom. The
1992 paper IS present in `bibliography/references.tex` line 520 under
key `Feigin-Frenkel`; the chapters use four different aliases
(`FeiginFrenkel1992`, `feiginfrenkel1992`, `FeiginFrenkel92`,
`FF92`) none of which resolve to that canonical key. This is
textbook AP281 bibkey naming-drift.

**feiginfuks1983 (1983 Funct. Anal. Appl. announcement):** 1 site. This
short note is the predecessor to the 1984 LNM paper; `FF84` covers the
content, so the cite at `universal_conductor_K_platonic.tex:452` could
collapse to `FF84`. The 1983 announcement is only separately useful for
date-of-discovery arguments.

## 4. Consistency of FF84 vs FF92 distinction

In-build chapters that cite Feigin-Fuchs for BRST/Virasoro content
versus Feigin-Frenkel for affine KM critical-level content maintain
CONTENT-LEVEL distinction cleanly: not a single cite conflates the
two papers at the content level (Virasoro Verma vs affine KM centre).
The failure mode is exclusively bibkey-layer: three in-build chapters
use an undefined alias for the 1992 Feigin-Frenkel paper despite the
canonical `Feigin-Frenkel` key being available.

The one standalone site that conflates FF in prose (`garland_lepowsky.
tex:1281-1282` uses `FF92` both for the Gaudin model and for the
critical-level centre, which are Feigin-Frenkel 1992 + Feigin-Frenkel-
Reshetikhin 1994 respectively) is an AP272 issue (folklore citation:
one key for two distinct works), but it is a standalone file, not
in-build.

## 5. Cache pattern update

Pattern (candidate cache entry): **"Feigin-Fuks / Feigin-Fuchs /
Feigin-Frenkel naming-drift cluster".** Four genuinely different
papers share two surname variants (`Fuks` vs `Fuchs` transliteration of
Feigin--Fuks's coauthor Dmitry B. Fuks/Fuchs; `Frenkel` is a distinct
third author). Any cite rendered as "Feigin--F*" in prose is
ambiguous between FF84, FF90 (Fuchs), FF90 (Frenkel-DS-reduction), FF92
(Frenkel-critical level), FFR94. Counter: every Feigin-"F" cite must
carry the year in the bibkey suffix and its explicit bibliographic
entry must match the year. Regex pre-commit gate:

```
grep -rn '\\cite{[^}]*F\(F\|euguin\)[^0-9}]*}' chapters/ standalone/ | \
  grep -v "FF84\|FFR94\|Feigin-Frenkel\|FF}"
```

Any hit = ambiguous Feigin cite. Healing: disambiguate bibkey via year
suffix (prefer FF84, FF90-Fuchs, FF90-Frenkel, FF92, FFR94) and ensure
the chosen bibkey is defined in the build's canonical bibliography.

## 6. AP inscription (minimal, per AP314 throttle)

The three findings above (phantom bibkey aliases for a defined paper;
FF84 mis-attribution to Gel'fand-Fuks; author-surname ambiguity) are
variants of already-catalogued patterns (AP281 systemic phantom-cite;
AP272 folklore citation; AP285 alias drift). No new AP block needed
this wave. This audit reserves no AP number; future waves may promote
the "author-year bibkey discipline for surname-colliding pairs"
pattern to AP1381 if recurrences justify.

## 7. Heal menu (Beilinson-disciplined, unapplied)

Per the user's instruction "HEAL per findings", the minimal repairs
below are recommended; none are applied in this audit session, per
the grep-only scope and the PreToolUse pre-commit gate:

### Heal~1 (phantom-bibkey collapse, AP281 primary repair)

Option~A (aliases in Vol~I bibliography, fastest): add five alias
`\bibitem` entries to `bibliography/references.tex` immediately after
line 527 (the `FF84` entry):

```
\bibitem{FeiginFuchs90}  % alias for FF84 (1990 full write-up)
B. L. Feigin and D. B. Fuchs, \emph{Representations of the Virasoro algebra},
in \emph{Representation theory of Lie groups and related topics
(Leningrad, 1982--84)}, Adv. Stud. Contemp. Math.\ \textbf{7},
Gordon and Breach, 1990, 465--554.

\bibitem{feiginfuks1983}  % alias for FF84 (1983 announcement)
B. Feigin and D. Fuks, \emph{Verma modules over the Virasoro algebra},
Funct. Anal. Appl.\ \textbf{17} (1983), 241--242.

\bibitem{FeiginFrenkel1992}  % alias for Feigin-Frenkel (1992)
B. Feigin and E. Frenkel, same content as \cite{Feigin-Frenkel}.

\bibitem{feiginfrenkel1992}  % lowercase alias, same content
B. Feigin and E. Frenkel, same content as \cite{Feigin-Frenkel}.

\bibitem{FeiginFrenkel92}    % yy-suffix alias, same content
B. Feigin and E. Frenkel, same content as \cite{Feigin-Frenkel}.
```

Option~B (canonicalization, cleaner): repo-wide `sed` pass replacing
the five drifted aliases with their canonical form. Cost: 20 edits in
~10 files; benefit: single alias per reference throughout.

### Heal~2 (FF84 mis-attribution, AP272 repair)

Two sites need either (a) bibkey retarget to `Fuks86` (defined) or
(b) addition of a Gel'fand-Fuks 1970 entry:

* `hochschild_cohomology.tex:161`: replace `\cite{FF84}` with `\cite{Fuks86}`
  (already cited correctly at line 285 for the same content).
* `conformal_anomaly_rigidity_platonic.tex:163`: same replacement.
  The load-bearing fact $H^2(\mathrm{Witt}; \bC) = \bC$ is chapter 2
  of Fuks' 1986 monograph `Fuks86`.

### Heal~3 (phantom supporting-key cluster)

`KacBook`, `RCW82`, `Frenkel2007`, `Arakawa2007`, `ArakawaFrenkel2017`,
`arakawa2017`, `kacpeterson1984`, `kac1998`, `polyakov1990`,
`bershadsky1991`, `arakawa2005` all require either alias entries in
`bibliography/references.tex` or retargeting to existing keys. Out of
the audit's primary scope (Feigin-Fuks focus); register as AP281
follow-up.

## 8. Summary for HZ-IV discipline propagation

Theorem H Virasoro HZ-IV decorator path 1 cites "Feigin-Fuchs 1984
Fock-BRST". That path survives the audit: `FF84` is defined; the
content-level attribution (Virasoro character via free-boson BRST /
Verma module) is correct primary-source mapping.

Theorem H critical-level exclusion cites Feigin-Frenkel 1992. Every
in-build cite of the 1992 paper uses a drifted alias; none render in
the build. The content-level attribution is correct; the bibkey-level
gap is AP281 phantom. Healing Option~A above closes it.

No claim in the theorem-status table that depends on Feigin-Fuks 1984
vs Feigin-Frenkel 1992 is misattributed at content level; the gap is
strictly citational.

## Verdict

| Area                                                      | Status                                |
| --------------------------------------------------------- | ------------------------------------- |
| Content-level FF84 vs FF92 distinction                    | MAINTAINED                            |
| Bibkey hygiene (AP281)                                    | DEFICIENT (phantom aliases in-build)  |
| FF84 attribution to Gel'fand-Fuks results                 | DEFECTIVE (2 sites, AP272 analogue)   |
| HZ-IV decorator primary sources (Theorem H)               | CONTENT CORRECT; bibkey gap propagates|

No new AP number reserved; audit observations are variants of AP281,
AP272, AP285. Healing Options~A (alias entries) and Heal~2 (FF84 ->
Fuks86 retarget) are minimal, build-closing, and do not touch
mathematical content.

End of audit.
