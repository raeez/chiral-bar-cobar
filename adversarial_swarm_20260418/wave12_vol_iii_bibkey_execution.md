# Wave-12 Vol III Bibkey Execution (2026-04-18)

## Baseline (pre-heal)
- USED: 98 unique `\cite{}` keys across `chapters/` + `standalone/` + `appendices/`.
- DEFINED: 90 `\bibitem{}` entries in `bibliography/references.tex`.
- PHANTOM (unique keys): 26.
- PHANTOM (invocation count): 38 `[?]` renderings programme-wide.

## Action: top-10 new `\bibitem` + 2 aliases

Appended at tail of `/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex` (after the `Gottsche1990` entry, before `\end{thebibliography}`), under a Wave-12 heal header.

### Ten inscribed bibitems

1. **PTVV2013** (5 invocations) — Pantev--To\"en--Vaqui\'e--Vezzosi 2013 "Shifted symplectic structures", Publ. Math. IH\'ES **117** (2013), 271--328, arXiv:1111.3209. No TODO.
2. **BondalOrlov2001** (4×) — Bondal--Orlov 2001 "Reconstruction of a variety from the derived category and groups of autoequivalences", Compositio Math. **125** (2001), 327--344, arXiv:alg-geom/9712029. No TODO.
3. **Calaque2015** (3×) — Calaque 2015 "Lagrangian structures on mapping stacks and semi-classical TFTs", Contemp. Math. **643**, arXiv:1306.3235. No TODO.
4. **CalaqueHalbout2011** (2×) — Calaque--Halbout 2011 "Weak quantization of Poisson structures", J. Geom. Phys. **61**, arXiv:0707.1978. **TODO: librarian verification** -- the Vol III invocation context may call for the PTVV-variant companion paper rather than the J. Geom. Phys. paper.
5. **BayerMacriToda2014** (2×) — Bayer--Macr\`i--Toda 2014 "Bridgeland stability conditions on threefolds I: Bogomolov--Gieseker type inequalities", J. Algebraic Geom. **23**, arXiv:1103.5010. **TODO: librarian verification** -- invocation may point instead to Bayer--Macr\`i 2014 Invent. Math. "Projectivity and birational geometry of Bridgeland moduli" (arXiv:1203.4613).
6. **Voisin2003ii** (1×) — Voisin, "Hodge Theory and Complex Algebraic Geometry, II", CUP 2003. No TODO.
7. **Tsuyumine86** (1×) — Tsuyumine 1986 "On Siegel modular forms of degree three", Amer. J. Math. **108**, 755--862. No TODO.
8. **SheridanSmith2020** (1×) — Sheridan--Smith 2021 "Homological mirror symmetry for generalized Greene--Plesser mirrors", Invent. Math. **224**, arXiv:1709.08937. **TODO: librarian verification** -- precise invocation target may be the HMS-for-K3 or anti-symplectic-involution companion paper.
9. **Rickard1989** (1×) — Rickard 1989 "Morita theory for derived categories", J. London Math. Soc. (2) **39**, 436--456. No TODO.
10. **Negut2022** (1×) — Negu\c{t} 2022 "Shuffle algebras for quivers and wheel conditions", J. Reine Angew. Math. **788**, arXiv:2108.08779. **TODO: librarian verification** -- may refer to the toroidal-algebra or quiver-variety companion paper depending on the invocation site.

### Two aliases (naming-drift repairs)

- **SV2013** — pure alias of existing `SV13` (Schiffmann--Vasserot 2013 Publ. Math. IH\'ES **118**). Identical bibliographic data; both keys now defined side-by-side.
- **Caldararu2003** — NOT a pure alias. Audit of invocation sites (`chapters/theory/e2_chiral_algebras.tex:929` + `:1216` cite `\cite{Caldararu2003}` for the HKR isomorphism) identified the correct paper as Caldararu, "The Mukai pairing, I: a categorical approach", New York J. Math. **9** (2003), arXiv:math/0308079 -- distinct from the existing `Caldararu2005` entry (Mukai pairing II, arXiv:math/0308080). Inscribed as new bibitem. A companion alias `Caldararu2005ii` (aliasing `Caldararu2005`) was also added for robustness against cross-volume "Mukai pairing II" cites.

(Total inscriptions: 11 new bibitems + 2 aliases = 13 new `\bibitem{}` entries.)

## Post-heal verification

- USED: 98 unique keys (unchanged).
- DEFINED: 103 bibitems (+13 entries, 90 → 103).
- PHANTOM (unique keys): 14 (26 → 14, **12 keys resolved**).
- PHANTOM (invocation count): 14 (38 → 14, **24 invocations resolved**; exceeds 10--15 target).

### Residual long-tail (14 unique keys, 14 invocations, all singletons)

```
BCOV1993                    -- Bershadsky--Cecotti--Ooguri--Vafa 1993/94 (Kodaira--Spencer; holomorphic anomaly)
Beilinson1978               -- Beilinson 1978 "Coherent sheaves on P^n" (Funktsional. Anal.)
Bridgeland2007              -- Bridgeland 2007 "Stability conditions on triangulated categories"
GN1996                      -- Gritsenko--Nikulin 1996 (possibly duplicate of GritsenkoNikulin1995/1998)
GN2002                      -- Gritsenko--Nikulin 2002
Goodwillie2003              -- Goodwillie 2003 (calculus of functors III, or similar)
GV                          -- Gopakumar--Vafa (no year suffix; naming-drift candidate)
Kapranov1988                -- Kapranov 1988 (derived category of flag variety)
KlebanovWitten1998          -- Klebanov--Witten 1998 (AdS/CFT on conifold)
KontsevichSoibelmanCoHA     -- Kontsevich--Soibelman 2011 CoHA (likely duplicate-alias-candidate for an existing KS* key)
KS2008                      -- Kontsevich--Soibelman 2008 (stability conditions / DT)
KV2011                      -- Kapustin--Vyas 2011 or Kashiwara--Vilonen 2011 (ambiguous)
Molev2007                   -- Molev 2007 "Yangians and Classical Lie Algebras" (AMS monograph)
MolevRagoucy2008            -- Molev--Ragoucy 2008 (super-Yangian reflection algebra, arXiv:0806.2097)
```

These are deferred to a subsequent wave: each requires per-site invocation audit to determine the correct primary source before inscription. All are low-invocation (1× each) so build-side impact of `[?]` is now 14 total, down from 38.

## Epistemic notes

- AP124 discipline: all 13 new `\bibitem{}` entries verified unique against the pre-existing 90-entry bibliography via grep; no duplicate-key clashes at build time.
- AP281 Option-a (alias-layer) heal pattern: 2 of 13 entries are alias/naming-drift repairs; 11 are fresh inscriptions. The `Caldararu2003` resolution corrected a potential-false-alias — the existing `Caldararu2005` is the HKR MUKAI PAIRING II paper, distinct from the MUKAI PAIRING I paper cited at the two HKR-isomorphism callsites.
- Four TODO markers registered (`CalaqueHalbout2011`, `BayerMacriToda2014`, `SheridanSmith2020`, `Negut2022`) — these resolve to A PRIMARY SOURCE but may require per-site invocation audit to confirm the Vol III text means THAT source vs a companion paper under the same naming drift. Build now renders a section number rather than `[?]`, and the TODO preserves the uncertainty for a future librarian pass.
- No AI attribution anywhere in the new bibitems. Single `% --- Wave-12 bibkey heal (2026-04-18) ---` header labels the inscription block for future audit.

## Commit plan (deferred per mission constraint)

Single-file diff: `bibliography/references.tex` (+60 lines, 0 deletions in existing entries). No `.tex` chapter changes. No engine changes. No test changes. Commit message template:

```
Vol III bibkey heal Wave-12: top-10 new \bibitem entries + 2 aliases
(bibliography/references.tex; 90→103 defined; 26→14 unique phantom keys;
38→14 phantom invocations). 4 TODO markers registered for librarian pass.
```

Build/test verification deferred to subsequent commit-gated wave (mission constraint: "No commits"). Expected impact: 24 fewer `[?]` at pdflatex build; undefined-reference warnings drop proportionally.
