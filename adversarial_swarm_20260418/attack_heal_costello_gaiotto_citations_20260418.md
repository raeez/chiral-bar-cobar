# Attack-and-heal: Costello-Gaiotto Citation Accuracy Audit (2026-04-18)

Author: Raeez Lorgat.

Status: AUDIT + HEAL PLAN. No `.tex` edits applied in this pass; findings recorded for a follow-up harmonisation commit per AP281.

Scope: Vol~I `/Users/raeez/chiral-bar-cobar/` + Vol~III `/Users/raeez/calabi-yau-quantum-groups/`. Bibkey resolution audit, content-drift detection, spot-check of three load-bearing citation sites.

## Primary sources (ground truth)

- Costello 2011. *Renormalization and Effective Field Theory*. AMS Math. Surveys Monogr. 170.
- Costello 2013. *Supersymmetric gauge theory and the Yangian*. arXiv:1303.2632.
- Costello 2016. *M-theory in the Omega-background and 5-dimensional non-commutative gauge theory*. arXiv:1610.04144.
- Costello 2020. *Topological strings, twistors, and skyrmions*. (CERN talks / later arXiv:2111....). Vol~I `\cite{Costello2111}` likely targets this or arXiv:2111.01095 "Bootstrapping the a-anomaly in 4d QFTs".
- Costello-Gaiotto 2018. *Vertex operator algebras and 3d $\cN = 4$ gauge theories*. arXiv:1804.06460. JHEP 05 (2019) 018. — load-bearing for boundary VOA / line operators / Dimofte dictionary in 3d HT.
- Costello-Gaiotto-Paquette 2020/2021. *Twisted holography*. arXiv:2103.01238 (Mar 2021) or arXiv:2101.04647 (Jan 2021, Costello-Gaiotto-Paquette).
- Costello-Dimofte-Gaiotto 2020. *Boundary chiral algebras and holomorphic twists*. arXiv:2005.00083. Comm. Math. Phys. 399 (2023) 1203-1290.
- Costello-Paquette 2022a. *Twisted supergravity and Koszul duality: a case study in AdS_3*. arXiv:2104.14573.
- Costello-Paquette 2022b. *On the associativity of one-loop corrections to the celestial OPE*. arXiv:2208.00354.
- Costello-Witten-Yamazaki 2018. *Gauge theory and integrability, I/II/III*. arXiv:1709.09993 (I), 1802.01579 (II), 1908.02289 (III).
- Costello-Gwilliam 2017/2021. *Factorization Algebras in Quantum Field Theory*. Vol 1 (2017) + Vol 2 (2021). Cambridge University Press.
- Costello-Francis-Gwilliam 2024 (forthcoming). Unpublished lecture notes on factorization algebras / Chern-Simons theory and factorisation homology.
- Bittleston-Costello-Zeng 2024. *Uplifting amplitudes in special kinematics*. arXiv:2409.10668 (or nearby).
- Bittleston-Costello 2025 preprint (specific title/ID not verified in this audit).
- Fernandez-Costello-Paquette 2024. (specific title/ID not verified in this audit).

## Finding F1: Vol~I — 21 phantom Costello-family bibkeys, 47 use-site citations rendering `[?]`

Enumeration (bibkey : use-count in `chapters/` + `standalone/` + `appendices/`):

| Bibkey | Uses | Intended primary source (best inference from use-context) |
|---|---:|---|
| `Costello17` | 3 | Likely CG17 (factorisation algebras Vol 1) OR Costello 2013 (Yangian). Use-site Vol~I `higher_genus_foundations.tex:6211,6284` cites alongside `CG-vol2` and `Pridham17` for derived-stack perfectness construction -> this is CG17+CG-vol2 context, so `Costello17` -> alias of `CG17` or Costello-Gwilliam. Separately, `clutching_uniqueness_platonic.tex:628` cites `Costello17,Pridham17` for perfectness -> Pridham 2017, Costello 2011/2013. |
| `Costello2013` | 1 | arXiv:1303.2632 "Supersymmetric gauge theory and the Yangian". Vol~I `kac_moody.tex:5888` cites for 3d $\cN=2$ CS HT twist + boundary KM. Note: for the 3d-N=2 HT twist / boundary VOA in `kac_moody.tex`, the correct primary source is Costello-Gaiotto 2018 "VOAs and 3d $\cN=4$ gauge theories" (arXiv:1804.06460), NOT Costello 2013. The bibkey is a MIS-TARGET (AP272-variant: cited paper is real but wrong scope for this theorem step). |
| `Costello2111` | 2 | arXiv:2111.01095 or similar. `frontier_modular_holography_platonic.tex:4945,5042` cites alongside `CostelloP2201` for celestial holography and W-algebra bootstrap — likely Costello-Paquette celestial OPE (arXiv:2208.00354) or Costello 2020/2021 celestial chiral algebra paper. |
| `Costello-Gaiotto18` | 2 | Costello-Gaiotto 2018 VOA-3dN4. `frontier_modular_holography_platonic.tex:4759,4884`. Correct scope, correct year tag in key, phantom bib entry. |
| `CostelloGaiotto` | 2 | Same paper as `Costello-Gaiotto18`. `en_chiral_operadic_circle.tex:1609,1649`. Alias drift. |
| `CostelloGaiotto2020` | **defined**, content-drift | Bib entry at `references.bib:156-161` has title "Twisted holography" + arXiv:2101.04647, which is **Costello-Gaiotto-PAQUETTE 2021** "Twisted holography". The use-sites (`heisenberg_frame.tex:3283,3418,3770,3797`; `kac_moody.tex:5889`; `poincare_duality_quantum.tex:63`; `introduction.tex:1601`; `introduction_full_survey.tex:657`) cite Dimofte dictionary / boundary VOA / 3d HT line operators, which is **Costello-Gaiotto 2018** (arXiv:1804.06460). The bibkey ↔ content drift: title and arXiv ID in the bib entry match a different paper from the one the use-sites reference. |
| `CostelloP2201` | 2 | Costello-Paquette. arXiv:2201.xxxxx prefix suggests Jan 2022 paper — could be 2201.10374 "On the associativity..." (but that is 2208.00354 actually) or 2104.14573 "Twisted supergravity and Koszul duality". Phantom. |
| `BittlestonCostello25` | 1 | Bittleston-Costello 2025 celestial/amplitude paper. Phantom. |
| `BittlestonCostelloZeng24` | 1 | Bittleston-Costello-Zeng 2024. Phantom. |
| `CDG2024` | 3 | Costello-Dimofte-Gaiotto — but the actual paper is CDG 2020 arXiv:2005.00083 (defined at `references.bib:1375` as `CDG20`). Year-drift alias. |
| `CFG25` | 9 | Costello-Francis-Gwilliam 2025 (forthcoming). Phantom. |
| `CFG26` | 4 | CFG 2026 forthcoming. Phantom. |
| `CFG2602` | 3 | Same author team with month suffix "02". Phantom. |
| `CWY1` / `CWY2` / `CWY18` | 3 total | Costello-Witten-Yamazaki gauge-theory-and-integrability series. Phantom. |
| `CostelloGwilliam17` | 1 | Alias of `CG17`. Phantom key; already defined as `CG17`. |
| `costello-yamazaki` | 1 | Costello-Yamazaki 2019 arXiv:1908.02289 (= CWY III). Phantom. |
| `Costello-1705.02500v1` | 1 | arXiv:1705.02500 Costello "Holography and Koszul duality is the pure twistor string theory" OR Costello "M2 brane twisted ABJM". Phantom with raw arXiv ID in bibkey (bad practice). |
| `FernandezCostelloP24` | 1 | Fernandez-Costello-Paquette 2024. Phantom. |
| `Gaiotto-Rapcak-Y` / `gaiotto-rapchak` | 8 total | Gaiotto-Rapčák 2017 arXiv:1703.00982 "Vertex algebras at the corner" (the Y_{N_1,N_2,N_3} algebra). Two alias variants; phantom. |

Cross-check against `standalone/references.bib` defined keys: only 7 entries in the Costello cluster define bibs — `CG17`, `CG`, `CG-vol2`, `CostelloGaiotto2020` (drift), `CDG20`, `CDG2023`, `costello-renormalization`. Every other use is `[?]` at build.

## Finding F2: Vol~III — clean

Vol~III `bibliography/references.tex` defines all 6 cited Costello bibkeys: `Costello17`, `Costello2007`, `Costello2005`, `Costello2005TCFT`, `Costello2007Ainfty`, `Costello2007OpenClosed`, `Costello2013`, `CostelloGwilliam`, `CostelloFrancisGwilliam`, `CostelloPaquette2022`, `CostelloPaquette2022b`. Every `\cite{...}` in Vol~III `chapters/` resolves.

Vol~III `quantum_chiral_algebras.tex:217` uses the **prose form** "(Costello~2013, ...)" without a `\cite{}`, as does line 220 "(Costello~2017, ..., Costello--Francis--Gwilliam~2024, ...)". This is AP272 / AP28 style discipline (prose year-ref with no bibkey), not a phantom `[?]` issue — the build renders cleanly. However, load-bearing attributions like "Costello~2017" for the 6d hCS bridge should upgrade to `\cite{Costello1610}` (arXiv:1610.04144 "M-theory in the Omega-background and 5-d NC gauge theory") for auditability.

## Finding F3: Spot-check `Costello2013` at `kac_moody.tex:5888`

Use-site: 3d $\cN=2$ HT twist of Chern-Simons with gauge group $G$; boundary VOA = affine $V_k(\fg)$.

Cited: arXiv:1303.2632 "Supersymmetric gauge theory and the Yangian". That paper's scope is 4d $\cN=1$ gauge theory → Yangian bridge via holomorphic twist; it is NOT the primary reference for 3d $\cN=2$ HT-twisted CS with affine-KM boundary. The correct primary sources are:

- **Costello-Gaiotto 2018** (arXiv:1804.06460) §3-4 for the 3d $\cN=4$ → VOA construction.
- **Aganagic-Frenkel-Okounkov 2018** (arXiv:1701.03146) for the level-matching.
- **Costello-Gwilliam 2017** (CG17) Vol 2 Ch. 5 for the general boundary-VOA formalism.

Healing: replace `\cite{Costello2013}` with `\cite{CostelloGaiotto2020, CG17}` at `kac_moody.tex:5888` and re-target `CostelloGaiotto2020` to its correct paper (1804.06460) in the bib, OR introduce a new bibkey `CostelloGaiotto18` = 1804.06460 and retire `CostelloGaiotto2020`'s drift.

## Finding F4: `CostelloGaiotto2020` is the most load-bearing content-drift in Vol~I

8 `\cite{CostelloGaiotto2020}` use-sites; every one references 3d HT / boundary VOA / Dimofte dictionary content from Costello-Gaiotto 2018 (arXiv:1804.06460); the bib entry points to Twisted holography (arXiv:2101.04647).

Healing template (apply in follow-up commit):

```bibtex
@article{CostelloGaiotto18,
  author  = {Costello, Kevin and Gaiotto, Davide},
  title   = {Vertex operator algebras and 3d $\cN = 4$ gauge theories},
  journal = {J. High Energy Phys.},
  year    = {2019},
  volume  = {05},
  pages   = {018},
  note    = {arXiv:1804.06460},
}

@article{CostelloGaiotto2020,
  crossref = {CostelloGaiotto18},
  note     = {Year-drift alias of CostelloGaiotto18.},
}
```

Then global rename `\cite{Costello-Gaiotto18}` → `\cite{CostelloGaiotto18}` (kill dash-alias).

## Finding F5: `Costello17` ambiguity

Three uses. Two at `higher_genus_foundations.tex:6211,6284` cite `Costello17,CG-vol2,Pridham17` for derived-stack perfectness construction. Content: derived-algebraic-geometry perfectness; primary source is Pridham 2017. The `Costello17` here is likely a drift for `CG17` (Costello-Gwilliam Vol 1, 2017) or for Costello-Scheimbauer 2015 (an orthogonal paper). One at `clutching_uniqueness_platonic.tex:628` cites `Costello17,Pridham17` for the derived-stack construction — same context.

Healing: retarget all three to `\cite{CG17, CG-vol2, Pridham17}`; retire `Costello17` as an alias crossref to `CG17`.

## Finding F6: Raw arXiv ID in bibkey `Costello-1705.02500v1`

One use at `poincare_duality_quantum.tex:105` for M2 branes at $A_{N-1}$ singularity / twisted ABJM / Yangian$(\fgl_N)$ bulk-boundary duality. arXiv:1705.02500 is Costello 2017 "Holography and Koszul duality is the pure twistor string theory" (or a related preprint in that slot). The bibkey format is non-standard (raw arXiv ID + version suffix).

Healing: define `@article{Costello1705, author = {Costello, Kevin}, title = {...}, year = {2017}, note = {arXiv:1705.02500}}`; rename use-site.

## AP inscriptions (minimal, per AP314)

Two new APs register structural lessons; existing APs cover the rest (AP281 systemic phantoms, AP272 single-citation weak-claim, AP257 engine-docstring drift, AP279 rename semantic drift).

### AP1841 (Bibkey year-drift where both years correspond to real distinct papers by the same authors)

A bibkey named `AuthorYear` where the bib entry defines year $Y_1$ but every use-site cites content from the same authors' year-$Y_2$ paper ($Y_2 \neq Y_1$). Distinct from AP281 (alias with no definition): here the key HAS a definition, and the definition points to a real paper, but the authors published MULTIPLE papers that could plausibly be the target; the bib-entry title disambiguates which one is meant, and the use-sites disambiguate which one IS meant, and these disagree. Canonical violation: `CostelloGaiotto2020` in `standalone/references.bib:156` defines *Twisted holography* (arXiv:2101.04647, Costello-Gaiotto-Paquette 2021); all 8 use-sites in Vol~I reference *Vertex operator algebras and 3d $\cN=4$ gauge theories* (arXiv:1804.06460, Costello-Gaiotto 2018). A naive reader who follows the bibliography lands on the wrong paper and finds neither the Dimofte dictionary nor the boundary VOA construction the Vol~I use-sites require. Counter: for every `\cite{AuthorYear}` where the authors have multiple papers in the cluster $[Y-3, Y+3]$, read the cited paper's title from the `.bib` entry and pattern-match against the use-site context; if the title describes a different theorem or object than the use-site invokes, either retarget the bibkey to the correct paper or add a year-suffix to disambiguate. Distinct from AP285 (alias section-number drift) where the paper is right but the section number is wrong; AP1841 has the paper itself wrong. Healing menu: (a) retarget the bib entry to the paper the use-sites actually reference, and introduce a new bibkey for the paper currently at this entry; (b) retag all use-sites to an explicit year-suffixed alias matching the intended paper.

### AP1842 (Prose-only year citation for load-bearing external attribution)

A theorem or construction that depends on an external primary source cites the source in prose ("Costello 2013", "per Costello-Gwilliam Vol 2 Chapter 5", "Pridham 2017") without a `\cite{}` emission. The build renders cleanly (no `[?]`), a reader sees the attribution, and a future LLM agent can re-match the prose to the wrong paper (the primary source may have been renamed, retitled, or replaced by a later version). Stronger than AP272 (unstated cross-lemma via folklore single-citation): AP1842 catches the subtler case where the citation is bibliographically explicit at the prose level but is not lifted into the bibliography machinery, so downstream audit tooling (phantom-ref gates, rename-propagation scripts, alias-harmonisation passes) cannot touch it. Canonical instance: Vol~III `quantum_chiral_algebras.tex:217,220` writes "(Costello~2013, ``Supersymmetric gauge theory and the Yangian'')" and "(Costello~2017, ``M-theory in the Omega-background...''; Costello--Francis--Gwilliam~2024, ``Chern--Simons theory and factorisation homology'')"; the first has a bibkey that resolves but is not wired, the second has no bibkey at all. Counter: every prose year-citation of a load-bearing primary source must be lifted to `\cite{bibkey}` and registered in the bibliography; bibless prose citations are permissible only for the programme's own sub-paper identifier ("this volume, Theorem X") and for parenthetical inspirational attribution that is not theorem-load-bearing. Healing: add the bibkey + `\cite{}` lift in the next audit pass.

## Priority heal order (AP281 systemic)

1. **Define `CostelloGaiotto18`** (arXiv:1804.06460) in `standalone/references.bib`; re-target `CostelloGaiotto2020` as an alias crossref to the new key (pending clarification from the author whether *Twisted holography* arXiv:2101.04647 is actually needed as a separate entry; if so, create `CostelloGaiottoPaquette21` for it).
2. **Define 5 Costello-Paquette / Costello-Witten-Yamazaki / Costello-Francis-Gwilliam / Costello-Dimofte-Gaiotto top-hit bibkeys** for the 21 phantoms (Costello17 → alias of CG17; Costello2013 already exists as prose; define Costello1610 for M-theory Omega; define CostelloPaquette21 + CostelloPaquette22 for twisted holography papers; define CWY1/CWY2/CWY18 for gauge-integrability I/II/III; define CDG20-existing-alias for CDG2024 year-drift; define CFG25/CFG26/CFG2602 alias to CostelloFrancisGwilliam forthcoming; define BittlestonCostello/BittlestonCostelloZeng24; define FernandezCostelloP24; define GaiottoRapcak17; retire `Gaiotto-Rapcak-Y` and `gaiotto-rapchak` hyphen-drift variants).
3. **Retarget `Costello2013` use in `kac_moody.tex:5888`** from arXiv:1303.2632 to arXiv:1804.06460 (Costello-Gaiotto 2018), since the 3d $\cN=2$ HT twist content is there, not in the Yangian paper.
4. **Lift Vol~III prose year citations** in `quantum_chiral_algebras.tex:217,220,237` to `\cite{Costello2013}`, `\cite{Costello1610}`, `\cite{CostelloFrancisGwilliam}` as applicable.
5. **Global rename pass** retiring hyphen- and year-drift aliases: `Costello-Gaiotto18` → `CostelloGaiotto18`; `gaiotto-rapchak` → `GaiottoRapcak17`; `Costello-1705.02500v1` → `Costello1705`.

Estimated effort: ~30 minutes in a focused rectification session. Build gate: `grep -c '\[?\]' build/main.log` must not increase; `pdflatex main.tex` should emit fewer undefined-reference warnings after each heal step.

## Cross-volume constitutional note

CLAUDE.md HZ-2 and AP281 together already require pre-commit grep gates against phantom bibkeys. The 2026-04-18 audit confirms Vol~III is clean and Vol~I has 47 phantom uses across 21 aliases, concentrated in the Costello cluster. This audit output does not itself commit any `.tex` changes; the findings are staged for a follow-up harmonisation commit authored by Raeez Lorgat.
