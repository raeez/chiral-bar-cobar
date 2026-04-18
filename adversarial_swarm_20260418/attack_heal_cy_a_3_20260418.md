# Attack-and-heal: CY-A_3 inf-cat claim + Obs_Ainf = 0 UNIVERSALLY

Date: 2026-04-18
Target: Vol III `/Users/raeez/calabi-yau-quantum-groups/`
AP block reserved: AP961-AP980 (only three used; rest released per AP306 discipline)
Scope: the CY-A_3 proved-via-inf-cat-framework claim and the accompanying
`Obs_Ainf = 0 UNIVERSALLY` (via Costello open-closed TCFT) claim. Status
declared in Vol III `CLAUDE.md` row lines 101 and 109 and Vol I `CLAUDE.md`
line "CY-A_3 PROVED in inf-categorical framework; chain-level
[m_3,B^{(2)}]!=0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via Costello
TCFT." Primary inscriptions: `chapters/theory/m3_b2_saga.tex`,
`chapters/theory/cy_to_chiral.tex`, `chapters/theory/cyclic_ainf.tex`.

## Summary verdict

The Vol III chapter inscriptions are SUBSTANTIALLY BETTER than the CLAUDE.md
headline suggests. The acute pattern AP278 (moduli-space boundary
classification asserted without construction) is PRESENT but is already
inscribed with an explicit in-text scope remark identifying it as the open
frontier, and the AP-CY34 (individual-vs-total cancellation) distinction is
honestly inscribed at three locations. However: the row labels `PROVED`
and `UNIVERSALLY` are stronger than the proof bodies support, and a
chain-level identification gap (`B^{(2)}_{TCFT} vs B^{(2)}_{naive}`) that is
inscribed at remark-level in `m3_b2_saga.tex` is not reflected in the
CLAUDE.md headline. This is an AP305 (pessimistic-or-optimistic CLAUDE.md
drift) and AP286 (tactical phantomsection vs semantic heal) composite with
AP269 (SDR-formula fabrication mild-variant: the "total sum = 0 by
Costello's TCFT" is OPERADIC-LEVEL proved; CHAIN-LEVEL on the bar complex is
inscribed as conjectural in the same chapter at `rem:tcft-vs-naive-b2`).
AP281 (bibkey phantom): `Goodwillie2003` used in `m3_b2_saga.tex:751` has
zero matching `\bibitem{Goodwillie2003}` in `bibliography/references.tex`
(the entry `ChingHarper2019` exists at `:66-67` but the `Goodwillie2003`
citation is itself phantom).

The headline "CY-A_3 PROVED in inf-categorical framework" is accurate at
the level of the sharpened theorem (`thm:derived-framing-m3b2` +
`thm:cy-to-chiral-d3`), PROVIDED the reader understands this is a
NON-OBSTRUCTION theorem (HH^{-2}_{E_1}(A,A) = 0 via unit-connectedness +
Francis-Gaitsgory connectivity), not a construction of `Phi_3(X)` for a
specific compact CY_3. The Vol III CLAUDE.md line 18 acknowledges this
explicitly: "CY-A_3 inf-cat resolution is a NON-OBSTRUCTION theorem
(HH^{-2}=0 proves no obstruction), NOT a construction of Φ(X) for specific
compact CY_3." The Vol I CLAUDE.md HOT ZONE entry does not carry this
qualifier. This is a Vol I CLAUDE.md row alignment gap, not a Vol III
inscription gap.

## Findings (seven items)

### F1. Infinity-categorical model is implicit, not named

The proof of `thm:derived-framing-m3b2`
(`chapters/theory/m3_b2_saga.tex:697-765`) cites Dunn additivity
`\cite{Dunn1988}`, Francis `\cite{Francis2013}`,
Francis-Gaitsgory `\cite{FrancisGaitsgory2012}`, and `\cite{Goodwillie2003}`
but does NOT specify an (infinity,1)-categorical model — Lurie
quasi-categories, Joyal quasi-categories, complete Segal spaces, or a model
category presentation. For a theorem whose load-bearing step is "the space
of E_3-structures compatible with the given E_2-structure is contractible"
(clause (iv)), the ambient (infinity,1)-category is not optional: the
contractibility is a statement about a mapping SPACE, not a mapping SET.

Counter: in the Francis-Gaitsgory GR17 framework (the nearest canonical
reference for the E_3/E_1 additivity spectral machinery), the ambient is
Lurie quasi-categories. The proof body does not distinguish (a) the
Goodwillie calculus of functors (Goodwillie's own paper) from (b) the
Goodwillie-Ching-Harper structured-ring-spectra derived Koszul duality
(`ChingHarper2019`, inscribed in the bib at line 66-67); these are distinct
frameworks and the obstruction-group identification
`fib(T Mod_{E_3} -> T Mod_{E_2}) ~ HH^*_{E_1}(A,A)[-2]` proceeds through
(a), not (b). AP251 (attribution-density floor): the proof cites four
papers, none of which states the specific obstruction-group identification
in its own notation. AP272 (unstated cross-lemma via folklore citation).

### F2. AP281: phantom bibkey `Goodwillie2003`

Grep confirms: `\cite{Goodwillie2003}` at `m3_b2_saga.tex:751`; zero
`\bibitem{Goodwillie2003}` hits in `bibliography/references.tex`. The
`Goodwillie tower` language identifies this as the 2003 paper "Calculus
III" (*Geometry & Topology*); the closest match in the Vol III bib is
`ChingHarper2019` (derived Koszul duality and TQ-homology), which is the
STRUCTURED-RING-SPECTRA generalisation, not the original Goodwillie 2003
paper. At build time the `\cite{Goodwillie2003}` renders `[?]`. AP281
variant: single-paper drift (the citation resolves in the AUTHOR's mental
model, not in the bib).

Healing: inscribe `\bibitem{Goodwillie2003}` for Goodwillie, "Calculus III.
Taylor series", Geom. Topol. 7 (2003) 645-711, arXiv:math/0310481. Or
replace the `\cite{Goodwillie2003}` with `\cite{ChingHarper2019}` and
verify the Goodwillie-layer vanishing bound proved in Ching-Harper 2019
suffices (it does, via the TQ-homology tower; see their Theorem 1.4).

### F3. AP278 is PRESENT but inscribed transparently as frontier

The headline cancellation proof of `thm:total-ainf-compat`
(`m3_b2_saga.tex:547-617`) asserts: "the only boundary components of
$\overline{\cM}_{b, B^{(2)}}$ are $b \circ B^{(2)}$ and $B^{(2)} \circ b$.
No other Connes-hierarchy operations ($B^{(0)}, B^{(1)}, B^{(3)}$) appear
as boundary types: the surface types producing $B^{(i)}$ for $i \neq 2$
involve different topological operations (rotation, interior contraction,
cap product) that cannot arise as degenerations of the strip-plus-node
family." This is a compact 1-dimensional moduli-space boundary
classification. It is NOT constructed: no Deligne-Mumford-type
compactification is described, no Kuranishi-chart decomposition, no
explicit primary-source citation to a specific Costello theorem
enumerating the boundary strata of $\overline{\cM}_{b, B^{(2)}}$.

This is the canonical AP278 pattern. What makes the Vol III inscription
distinct from pure-violation cases: `rem:tcft-vs-naive-b2`
(`m3_b2_saga.tex:632-683`) inscribes the chain-level discrepancy honestly:

> "The chain-level identification $B^{(2)}_{TCFT} \overset{?}{\simeq}
> B^{(2)}_{naive}$ is therefore the open chain-level frontier of CY-A_3 for
> non-formal A-infinity algebras: Theorem ref{thm:total-ainf-compat}
> resolves the operadic-TCFT identity at the moduli-operad level, but
> lifting this to a strict chain-level identity on the bar complex
> requires either (a) a chain-level rectification of the cyclic
> A-infinity-structure that strictifies the cross-arity terms, or (b) an
> explicit chain homotopy
> $h: C_\bullet(A) \to C_\bullet(A)[+1]$ realising
> $B^{(2)}_{TCFT} - B^{(2)}_{naive} = [d_{tot}, h]$."

AP-CY34 engine `chain_level_m2_b2_cancellation.py:630-647` verifies that
the NAIVE pairwise-contraction $B^{(2)}_{naive}$ maps different arities
to different arities and CANNOT cancel by direct sum: arity 5 to arity 2
for $\{b_2, B^{(2)}\}$ vs arity 5 to arity 1 for $\{b_3, B^{(2)}\}$.

Conclusion: the Vol III chapter has the correct discipline. The issue is
not the inscription but the CLAUDE.md headline, which says "Obs_Ainf=0
UNIVERSALLY" without the chain-level caveat.

### F4. "UNIVERSAL" scope: three distinct objects conflated

`Obs_Ainf = 0 UNIVERSALLY` is true at THREE distinct ambient levels, with
sharply different strengths:

(L1) **Operadic / TCFT level**: $\{b, B^{(2)}_{TCFT}\} = 0$ universally,
for all cyclic A-infinity algebras of CY dimension $d$. This is the
content of `thm:total-ainf-compat`, PROVED conditional on the unconstructed
boundary classification of $\overline{\cM}_{b, B^{(2)}}$ (F3).

(L2) **Infinity-categorical level**: the obstruction class
$[\mathrm{Obs}_{\Ainf}] \in \HH^{-2}_{E_1}(A, A)$ vanishes, and the space
of $E_3$-liftings is contractible, for any smooth proper CY_3 category
with $\HH^0(\cC) = k$. This is `thm:derived-framing-m3b2`, PROVED
conditional on the unspecified infinity-categorical model and the
Goodwillie-tower vanishing via connectivity (F1).

(L3) **Chain level on the bar complex**:
$\{b_k, B^{(2)}_{naive}\} \neq 0$ strictly for $k \geq 3$, and the sum does
NOT vanish without a chain-level rectification (F3). This is
INSCRIBED AS OPEN at `rem:tcft-vs-naive-b2` and
`m3_b2_saga.tex:779-801` ("Level 1: Strict chain-level. Answer: NO for
non-formal algebras").

The Vol III CLAUDE.md row line 101 says "Obs_Ainf=0 UNIVERSALLY"; Vol I
CLAUDE.md says "Obs_Ainf=0 UNIVERSALLY via Costello TCFT". Both readings
mix L1 and L2 under one "UNIVERSAL" umbrella and elide L3. AP234 (two
objects under one symbol) / AP311 (two invariants under one banner).

### F5. AP-CY34 engine chain-level evidence contradicts naive headline

Per AP-CY34: "individual $\{b_k, B^{(2)}\} \neq 0$ but total sum via
Costello TCFT gives 0." This is correct at level L1 (operadic TCFT) where
"total sum" means the image under the TCFT identification
$B^{(2)}_{TCFT}$. It is FALSE at level L3 (chain-level on the bar complex
with $B^{(2)}_{naive}$): the two terms land in different bar-arity graded
pieces, per `chain_level_m2_b2_cancellation.py:630-647`, and cannot
cancel by direct sum. The Vol III manuscript inscribes this correctly at
`rem:tcft-vs-naive-b2`. The CLAUDE.md gloss "total sum via Costello TCFT
gives 0" is ACCURATE for $B^{(2)}_{TCFT}$ but AMBIGUOUS for $B^{(2)}_{naive}$.

### F6. AP251 attribution-density floor: proof attributes to Costello 2005 + 2007

`thm:total-ainf-compat` proof body cites `\cite{Costello2005TCFT}` (Theorem
A; arXiv:math/0412149) and `\cite{Costello2007Ainfty}` (arXiv:0706.1959).
These exist in the bib and resolve. The proof sketch identifies
(i) $b$ with codim-1 boundary strata (strip-like degenerations),
(ii) $B^{(2)}$ with the genus-change operation, and
(iii) the 1-manifold boundary count $\partial^2 = 0$ as the content.

Costello 2005 Theorem A establishes the equivalence
(cyclic A-infinity of dim $d$) $\simeq$ (open TCFT with $d$-shifted
framing). Costello 2007 extends to open-closed. Neither paper
explicitly enumerates the boundary strata of $\overline{\cM}_{b, B^{(2)}}$
as a 1-dimensional moduli space. The Vol III proof treats this boundary
enumeration as a structural consequence of the equivalence, not as a
separately inscribed lemma. AP272 (unstated cross-lemma via folklore
citation): the boundary enumeration is used but never proved locally or
cited to a specific theorem / proposition in Costello 2005, 2007.

### F7. Vol I vs Vol III CLAUDE.md alignment

- Vol III CLAUDE.md line 18: explicit "NON-OBSTRUCTION theorem
  (HH^{-2}=0), NOT a construction of Phi(X) for specific compact CY_3."
  This is the correct scope.
- Vol III CLAUDE.md line 101 (row Cyclic A_inf framing compat): "Obs_Ainf=0
  UNIVERSALLY" without chain-level caveat.
- Vol III CLAUDE.md line 109 (row CY-A_3 inf-categorical): "PROVED" without
  chain-level caveat.
- Vol I CLAUDE.md "CY-A_3 PROVED in inf-categorical framework; chain-level
  [m_3,B^{(2)}]!=0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via Costello
  TCFT." acknowledges the chain-level individual non-vanishing (that's
  correct) but DOES NOT acknowledge the L1-vs-L3 distinction for the
  TOTAL sum on the bar complex.

AP305 (pessimistic/optimistic drift) here manifests in the OPTIMISTIC
direction: CLAUDE.md is more optimistic than the honestly inscribed
`rem:tcft-vs-naive-b2`. AP271 (reverse drift: CLAUDE.md lags behind
manuscript retraction) applies in the inverse direction: the Vol III
chapter inscribed the chain-level frontier caveat at
`rem:tcft-vs-naive-b2` and the CLAUDE.md rows 101 / 109 never propagated
the caveat. A reader of the CLAUDE.md rows who never opens
`m3_b2_saga.tex` will believe "UNIVERSALLY" applies at all three levels.

## Healing recommendations (not applied in this pass; audit only)

### H1 (AP278+AP272, primary). Inscribe a bridge lemma for the boundary classification of $\overline{\cM}_{b, B^{(2)}}$

Add a `\begin{lemma}[Boundary stratification of the $(b, B^{(2)})$
moduli]` to `m3_b2_saga.tex` before `thm:total-ainf-compat`, stating
explicitly:

> "The compact 1-dimensional moduli space $\overline{\cM}_{b, B^{(2)}}$
> parametrising surfaces with one strip-degeneration and one
> genus-change-node has boundary stratification
> $\partial \overline{\cM}_{b, B^{(2)}} = (b \circ B^{(2)}) \sqcup (B^{(2)}
> \circ b)$."

Status tag: `\ClaimStatusProvedElsewhere` attributing the boundary
enumeration to Costello 2007, Section 5 (open-closed moduli) + Harrelson-
Voronov-Zuniga 2006 (moduli of Riemann surfaces with open-closed marked
points). If the Costello references do not explicitly state this
stratification, downgrade to `\ClaimStatusConditional` with an honest
frontier remark naming the missing ingredient.

### H2 (AP281). Inscribe `\bibitem{Goodwillie2003}` or retarget to `ChingHarper2019`

Either add a `\bibitem{Goodwillie2003}` to `bibliography/references.tex`
for Goodwillie, Calculus III, Geom. Topol. 7 (2003) arXiv:math/0310481,
or replace `\cite{Goodwillie2003}` at `m3_b2_saga.tex:751` with
`\cite{ChingHarper2019}` if the connectivity bound used is the
Ching-Harper TQ-homology bound (which gives the same vanishing).

### H3 (AP305+AP4+AP40). Rewrite Vol III CLAUDE.md rows 101 and 109 with chain-level caveat

Current row 101:

> "| **Cyclic A_inf framing compat** | PROVED (corrected) |
> prop:cyclic-ainf-framing-compat. [...] Obs_Ainf=0 UNIVERSALLY. |"

Healed row 101:

> "| **Cyclic A_inf framing compat** | PROVED operadic-TCFT-level;
> chain-level frontier inscribed at rem:tcft-vs-naive-b2 |
> prop:cyclic-ainf-framing-compat. Individual {b_k, B^{(2)}_naive} != 0
> for k >= 3 (obs_ainf_local_p2, 54 tests; chain_level_m2_b2_cancellation
> verifies different-arity cancellation is impossible). Costello TCFT
> gives {b, B^{(2)}_TCFT} = 0 via partial^2 = 0 on moduli chain complex
> C_*(overline{cM}_{0,n}^{open}). Chain-level identification
> B^{(2)}_TCFT =?= B^{(2)}_naive is open for non-formal algebras
> (conj:b2-tcft-naive-identification to inscribe; Tradler 0108027 gives
> the formal case). |"

Similar row 109 rewrite: "PROVED as NON-OBSTRUCTION theorem
(HH^{-2}_{E_1}(A,A) = 0 by unit-connectedness; space of E_3-liftings
contractible); chain-level construction of Phi_3(X) for compact
non-formal CY_3 is Step 2 (Cech-HTT + Borel summability) not Step 1."

### H4 (AP287 cross-volume propagation). Update Vol I CLAUDE.md

Vol I CLAUDE.md line "CY-A_3 PROVED in inf-categorical framework; chain-
level [m_3,B^{(2)}]!=0 is NOT obstruction; Obs_Ainf=0 UNIVERSALLY via
Costello TCFT." needs a one-phrase caveat: replace "UNIVERSALLY" with
"UNIVERSALLY at operadic-TCFT level (L1); chain-level identification
B^{(2)}_TCFT =?= B^{(2)}_naive open, rem:tcft-vs-naive-b2 in Vol III
m3_b2_saga.tex".

### H5 (AP266 sharpened obstruction). Inscribe explicit obstruction class

Per AP266 healing discipline: when a deep-math attempt genuinely FAILS at
chain level, inscribe the obstruction as an explicit cohomology class
with a falsification test. Here: `conj:b2-tcft-naive-identification` can
be sharpened by noting that the obstruction to the chain-level homotopy
$h$ satisfying $B^{(2)}_{TCFT} - B^{(2)}_{naive} = [d_{tot}, h]$ is a
class in $H^{-1}(\RHom_{C_*(A)}(C_*(A), C_*(A)))$ with nonzero
components in bidegree $(5, 2)$ and $(5, 1)$ per the engine verification.
Any claimed strictification (e.g. extension of Tradler 2001 to
non-formal algebras) must produce such an $h$ with vanishing class,
providing a Beilinson falsification test.

## Dependency propagation sweep (AP149)

CLAUDE.md cross-volume consumers of "Obs_Ainf=0 UNIVERSALLY":

- Vol I CLAUDE.md HOT ZONE summary line (AP271 lag).
- Vol III CLAUDE.md rows 101, 109, 136 ("CY-B push at d=3 conditional on
  chain-level data"), 757 ("CY-A: d=2 PROVED, d=3 PROVED (inf-cat)").
- Vol III `cy_to_chiral.tex` line 1977, 1989, 2023-2072, 2182, 3671-3677
  (explicit cascade through `thm:cy-to-chiral-d3` Step 1).
- Vol III `cyclic_ainf.tex:174, 219, 238` (routes via CY-A_3 Theorem).
- Tests: `cya3_stress_test.py`, `operadic_tcft_mk_b2_engine.py`,
  `obs_ainf_local_p2.py`, `chain_level_m2_b2_cancellation.py`,
  `stasheff_cancellation_obs_ainf.py`, `derived_framing_obstruction.py`,
  `connes_b_obs_ainf.py`, `spectral_seq_obs_ainf.py`.

H3 + H4 applied atomically would close the AP149 propagation loop. Each
downstream "conditional on CY-A_3" consumer is already honestly scoped;
they inherit the chain-level caveat automatically once H3 is applied.

## Outcome

Four PRESENT anti-patterns, all with existing in-chapter discipline:
AP278 (inscribed but as operadic-level claim, with chain-level frontier
acknowledged at `rem:tcft-vs-naive-b2`), AP281 (phantom
`Goodwillie2003`), AP272 (unstated Costello boundary-enumeration
lemma), AP305/AP271 (CLAUDE.md rows lag behind the honest
`rem:tcft-vs-naive-b2` inscription).

The mathematical content is NOT broken. The acute claim
"Obs_Ainf = 0 UNIVERSALLY" is correct at levels L1 (operadic TCFT) and L2
(infinity-categorical non-obstruction); it is open at level L3 (chain-
level on the bar complex with the naive Connes-hierarchy $B^{(2)}$) and
this is honestly inscribed in Vol III. The Vol I CLAUDE.md row should
inherit the L1/L2/L3 stratification.

AP961 (Vol III / Vol I CLAUDE.md row asymmetry): when a Vol III chapter
inscribes an honest frontier remark (here `rem:tcft-vs-naive-b2`)
downgrading the strength of a "UNIVERSALLY" claim, the Vol I CLAUDE.md row
that mirrors the advertised claim must carry the same downgrade within
the same session. Current state: the Vol III frontier remark was
inscribed with the proposition; the Vol I CLAUDE.md row was not updated
to reflect the chain-level open-frontier caveat. AP271 at cross-volume
level, specialised to the case where the downgrade is inside a single
chapter's Remark rather than a separate retraction file.

AP962 (AP278 variant: boundary classification inscribed transparently as
structural-expectation, not constructed). Where the standard AP278 fires
on "asserted without construction", this variant fires on "asserted with
a companion remark admitting the chain-level identification is open"
— the moduli-operad identity is claimed and is partially justified by
Costello 2005+2007, but the 1-manifold boundary stratification
$\partial \overline{\cM}_{b, B^{(2)}} = (b \circ B^{(2)}) \sqcup (B^{(2)}
\circ b)$ (no other strata) is asserted without primary-source
enumeration. The honest Vol III scope is the operadic-TCFT identity on
$B^{(2)}_{TCFT}$, not on $B^{(2)}_{naive}$; this transparency does not
dissolve the AP278 pattern, it only scope-qualifies it. The variant
deserves its own register because a future agent auditing
`thm:total-ainf-compat` in isolation (without the nearby
`rem:tcft-vs-naive-b2`) will not see the chain-level caveat and may
propagate the "UNIVERSALLY" headline.

AP963 (three-level ambient conflation under one "UNIVERSAL" banner).
When a claim "X = 0 universally" is made, the ambient level (operadic,
infinity-categorical, chain-level on the bar complex) at which the
vanishing holds must be stated. Canonical violation: CLAUDE.md rows
asserting $\mathrm{Obs}_{\Ainf} = 0$ UNIVERSALLY without L1/L2/L3
stratification. Related AP311 (two invariants under one banner) and
AP234 (two Koszul conductors under letter $K$); AP963 is the ambient-
level-discipline sibling, applied to vanishing claims in A-infinity /
cyclic / TCFT ambient hierarchies.

## Action items (not applied)

Recommended for next session. No edits made this session; no commits.

1. H1: inscribe boundary-stratification lemma in `m3_b2_saga.tex` before
   `thm:total-ainf-compat`, with `\ClaimStatusProvedElsewhere` or
   `\ClaimStatusConditional` per primary-source verification.
2. H2: resolve `\cite{Goodwillie2003}` phantom (5-minute bib edit).
3. H3: rewrite Vol III CLAUDE.md rows 101 and 109 with chain-level
   caveat.
4. H4: Vol I CLAUDE.md HOT ZONE entry aligns to Vol III.
5. H5: inscribe `conj:b2-tcft-naive-identification` with explicit
   obstruction-class statement + Beilinson falsification test, per AP266.

## Primary sources (absolute paths)

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/m3_b2_saga.tex`
  lines 547-617 (`thm:total-ainf-compat`), 632-683
  (`rem:tcft-vs-naive-b2`), 697-765 (`thm:derived-framing-m3b2`),
  779-801 (three levels of truth).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
  lines 1970-1990 (obstruction decomposition), 1993-2021
  (`prop:cyclic-ainf-framing-compat`), 2024-2050
  (`rem:cyclic-ainf-framing-audit`), 2052-2073
  (`rem:hopf-reduction`), 2076-2114 (`thm:derived-framing-obstruction`),
  3622-3683 (`thm:cy-to-chiral-d3` statement and proof), 3685-3738
  (`rem:cy-to-chiral-d3-evidence` E1-E10 + O1-O5).
- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cyclic_ainf.tex`
  lines 216-239 (`conj:cyclic-ainf-kappa-cat-d3`, `rem:costello-operadic`).
- `/Users/raeez/calabi-yau-quantum-groups/bibliography/references.tex`
  lines 69 (`Costello2007`), 79 (`Costello2005TCFT`),
  83 (`Costello2007Ainfty`), 111 (`Dunn1988`),
  123 (`Francis2013`), 126 (`FrancisGaitsgory2012`),
  66-67 (`ChingHarper2019`). No `\bibitem{Goodwillie2003}`.
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/operadic_tcft_mk_b2_engine.py`
  docstring lines 1-80 (AP-CY34 resolution narrative).
- `/Users/raeez/calabi-yau-quantum-groups/compute/lib/chain_level_m2_b2_cancellation.py`
  lines 630-647 (arity mismatch: $\{b_2, B^{(2)}\}$ maps arity 5 to 2;
  $\{b_3, B^{(2)}\}$ maps arity 5 to 1).
- `/Users/raeez/calabi-yau-quantum-groups/CLAUDE.md`
  lines 18 (NON-OBSTRUCTION qualifier), 101 (row Cyclic A_inf framing
  compat), 109 (row CY-A_3 inf-categorical), 136 (CY-B at d=3), 226,
  264, 269, 757, 825 (downstream conditional-on-CY-A_3 consumers).

End of report. Raeez Lorgat, 2026-04-18. No AI attribution; no commits.
