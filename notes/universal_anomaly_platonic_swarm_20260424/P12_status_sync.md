# P12 theorem-status and cross-surface sync report

Worker: P12, theorem-status / duplicated-surface audit.

Owned file:
`notes/universal_anomaly_platonic_swarm_20260424/P12_status_sync.md`

Read-only target surface:
`standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex`
with inputs
`standalones/universal_anomaly_voa_explicit_supplement.tex` and
`standalones/universal_anomaly_local_global_arithmetic_supplement.tex`.

No target TeX files were edited. No build was run.

## Verdict

The rectified standalone has the right global direction but the status
surface is not synchronized. The correct status map is:

- Proved here: the Hodge target, if the class is defined, is
  \(H^2(X,\Omega_X^1)=H^{1,2}(X)\); for every smooth curve
  \(H^2(C,\Omega_C^1)=0\); the raw product \(K3\times E\) has a
  21-dimensional \(H^2(\Omega^1)\) target.
- Conditional: the actual construction of
  \(\alpha_X=[m_3,B^{(2)}]_X\) until a cyclic-HKR datum, cochain
  Connes convention, trace/contraction, and independence proof are
  fixed; the bridge to Positselski, factorisation, K3/Igusa, and trace
  vertices; the K3 product vanishing; hCS anomaly matching; two-loci,
  Heegner, Bridgeland, and Niemeier corollaries.
- Conjectural: the five-vertex pentagon, motivic lift, graph lift,
  universal Duflo specialization, Verdier-dual decagon, and all-higher
  closure.
- Heuristic/open: the Clemens/Strominger physical reformulation and
  the \(H\)-twisted CDO replacement until a Courant-algebroid
  construction is supplied.

The main patch should split the paper into a proved target/falsifier
core and a conditional comparison bridge. Do not let "proved
obstruction class" language survive unless P01's cyclic-HKR datum is
inserted and proved.

## Critical drift

### C1. The abstract says "proved core" where the formal surface is conditional

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:100`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:480`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:513`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:744`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:851`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1194`

Drift: the abstract and later summaries say the construction of the
class is proved, but the explicit representative, Atiyah-cup
derivation, and bridge theorem are all conditional.

Heal: either insert a definition of the cyclic-HKR datum and prove
model-independence, or rewrite all "proved class" language to "class
in the chosen cyclic-HKR datum, conditional on the stated convention".

Patch grep:

```bash
rg -n "proved core|theorem proves the obstruction|one proved Dolbeault|corrected theorem has one proved|proves the obstruction class" standalones/universal_anomaly_*.tex
```

### C2. `thm:main` mixes proved facts, conditional arrows, and stale references

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:744`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:755`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:767`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:779`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:600`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:23`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1135`

Drift: `thm:main(i)` is the Hodge target, not vanishing. But it is
cited as vanishing at lines 600 and local-global line 23. Line 1135
cites "equivalence of (i) and (iv)", but `thm:main` states no such
equivalence.

Heal: split labels:

- `thm:atiyah-connes-target` for Hodge target and curve falsifier;
- `thm:atiyah-connes-bridge` for B1--B4;
- `conj:atiyah-connes-pentagon` for equivalence of vertices.

Then update stale references to the appropriate label.

Patch grep:

```bash
rg -n -F 'Theorem~\ref{thm:main}(i)' standalones/universal_anomaly_*.tex
rg -n -F 'Theorem~\ref{thm:main}(iii)' standalones/universal_anomaly_*.tex
rg -n -F 'equivalence of (i) and (iv)' standalones/universal_anomaly_*.tex
```

### C3. The B1 obstruction target is not defined

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:769`

Drift: the theorem maps to
`\mathrm{Ob}_{\mathrm{bar\text{-}cobar}}(A_X|_C)`, but no such object
is defined. P02 gives the correct first-obstruction target:
\[
H^2(\pi_{3,0}\Defcyc^{\mathrm{mod}}(A_C)).
\]

Heal: define
`Ob^{(1)}_{bc}(A_C):=H^2(\pi_{3,0}\Defcyc^{mod}(A_C))`, identify
`sp_{\Sigma,C}(\alpha_X)` only with `o^{(0)}_3(A_C)`, and keep full
Theorem B behind a higher-obstruction closure or independent
Koszul/PBW hypothesis.

Patch grep:

```bash
rg -n -F 'Ob}_{\mathrm{bar\text{-}cobar}}' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n "first non-trivial obstruction|higher obstruction classes|all-loop obstruction closure" standalones/universal_anomaly_*.tex
```

### C4. Derived loci are claimed but not built

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:115`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:781`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:32`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:36`

Drift: the paper says "derived loci", but the base stack, obstruction
complex, section, and derived zero locus are absent. The supplement
uses an underived Kuranishi subscheme/coherent sheaf substitute.

Heal: insert P05's machinery:
\[
\mathcal B,\quad \mathbb E_{AC}=R\pi_*\Omega^1_{\mathcal X/\mathcal B}[2],
\quad \alpha_{AC}\in\Gamma(\mathcal B,\mathbb E_{AC}),\quad
\mathbf Z_\alpha=\mathbf Z(\alpha_{AC}).
\]
Only after that may `QCoh`/`IndCoh` or `Pr^L_k` appear as a corollary.

Patch grep:

```bash
rg -n "derived loci|zero locus|subscheme|coherent sheaf|Pr\\^\\{\\\\mathrm\\{L\\}\\}|Pr\\^L" standalones/universal_anomaly_*.tex
```

### C5. K3/Mukai/Igusa/trace input is stronger than P04 permits

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:355`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:361`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:390`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:396`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:227`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:247`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:591`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:674`

Drift: stable constants survive,
\(c_+(\operatorname{Muk}(K3))=4\), \(K=8\), \(\hbar^2=-1/8\), and
\(\Delta_5^2=\Phi_{10}\). But the compact \(K3\times E\) realization,
canonical arithmetic VOAs, and Bruinier-implies-\(K=8\) language remain
too strong.

Heal: split a proved/elsewhere constant package from conditional
realization hypotheses B3/B4. Replace "Bruinier forces \(K=8\)" by
"Bruinier supplies the Heegner Chern-class input; Mukai signature plus
the conductor normalization gives \(K=8\)."

Patch grep:

```bash
rg -n "Bruinier.*forces|reduces to.*Bruinier|canonical arithmetic VOA|survive Bruinier|K = 2c_\\+|hbar\\^2 = -1/8" standalones/universal_anomaly_*.tex
```

### C6. Clemens/Strominger is marked proved elsewhere but is open/heuristic

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1023`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1028`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1030`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1047`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1188`

Drift: the corollary claims a proved-elsewhere Strominger
reformulation and says the four statements lift verbatim. Later the
open question correctly says the CDO construction remains open.

Heal: demote `cor:strominger` to `ClaimStatusConditional` or
`ClaimStatusHeuristic`, remove "lifts verbatim", and make the open
question the controlling surface.

Patch grep:

```bash
rg -n "cor:strominger|lifts verbatim|every Courant algebroid has a CDO|four climaxes reduce|H-twisted cocycle" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

## Serious drift

### S1. The setup asserts the cyclic-HKR operator before its conditional datum exists

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:223`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:248`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:461`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:473`

Drift: these paragraphs assert that \(B^{(2)}\) is a cochain operator,
that the commutator is defined, and that HKR lands in
\(H^2(\Omega^1)\). P01 shows this is conditional until the negative
cyclic complex, total grading, trace/contraction, and projection
through \(H^2(\wedge^2T_X)\) are fixed.

Heal: insert a "Cyclic-HKR datum" definition before line 223 and route
the target as
\[
\HH^4(X)\to H^2(X,\wedge^2T_X)\xrightarrow{\iota_{(-)}\Omega_X}
H^2(X,\Omega^1_X).
\]

Patch grep:

```bash
rg -n "B\\^\\{\\(2\\)\\}.*HH\\^2|commutator.*defined|descends to a class|maps, under HKR|HC\\^\\{-,2\\}" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### S2. Conditional/conjectural environments still contain proof-shaped assertions

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:568`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:577`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:624`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:633`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:603`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:608`

Drift: conjectures/provisional comparisons are followed by full proof
environments giving exact graph weights, motivic representatives, or
strictification implications. That reads as proved surface.

Heal: rename these `proof` blocks to "Evidence" or "Expected
construction", or strengthen the statements only after a real proof is
available.

Patch grep:

```bash
rg -n "\\\\ClaimStatusConjectured]|\\\\ClaimStatusConditional]" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
rg -n "\\\\begin\\{proof\\}" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### S3. Formality block imports false all-higher strictness

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:590`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:596`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:600`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:603`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:609`

Drift: vanishing of a second Taylor coefficient is used to claim strict
\(E_3\)-formality and to cite `thm:main(i)` for vanishing. P03/P06 say
this is only a frontier bridge with all-higher closure.

Heal: state only a conditional identification of \(U^3_{2,X}\) with
the obstruction class under the cyclic-HKR convention; move strictness
to a conjecture with an explicit all-higher obstruction hypothesis.

Patch grep:

```bash
rg -n "strict isomorphism|second Taylor coefficient vanishes|Theorem~\\\\ref\\{thm:main\\}\\(i\\)|formality morphism is a strict" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### S4. hCS/Adler-Bardeen slips from hypothesis to assertion

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:810`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:823`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:841`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:846`

Drift: the theorem begins conditionally, but item 823 and the following
remark assert that descent produces exactly \([m_3,B^{(2)}]\). The
compactness/all-loop sentence is also stronger than P03's bridge
surface.

Heal: keep all hCS comparison as a named B2 hypothesis unless the local
BRST anomaly complex and HKR comparison are constructed. Replace
"produces ... and this class is" by "would produce ... if the B2
comparison is proved".

Patch grep:

```bash
rg -n "Adler--Bardeen|hCS anomaly|produces a Dolbeault|this class is the cocycle|all loop orders|Costello 2011 Theorem~13.4.1" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### S5. The quintic is a falsifier of universality, not yet a nonzero obstruction computation

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:104`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:868`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:890`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1220`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1343`

Drift: the proposition correctly says non-vanishing of
\(\alpha_{Q_5}\) is conditional, but summaries and the hand-table still
read as "no" for \([m_3,B^{(2)}]\).

Heal: replace table entry with "unknown/conditional; target 101-dim";
say the quintic falsifies an unconditional K3/Igusa locus claim, not
the obstruction itself until the Yukawa-to-cyclic-projection bridge is
proved.

Patch grep:

```bash
rg -n "Q_5.*falsifier|quintic falsifies|\\$Q_5\\$.*no \\(\\$101\\$-dim\\)|non-zero Yukawa.*universal" standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### S6. Toy VOA examples overclaim bridge vertices

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1264`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1307`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:473`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:724`

Drift: Heisenberg and \(V_1(\mathfrak{sl}_2)\) prove small algebraic
vanishing mechanisms and curve-side Theorem B examples. They do not
degenerate the K3/Igusa vertex or supply all five Koszul duals.

Heal: restrict these examples to algebraic vanishing and Theorem B toy
models. Keep the five-dual/decagon section explicitly conjectural at
every item, not only in its final sentence.

Patch grep:

```bash
rg -n "toy analogues|four climaxes specialise|five Koszul duals|degenerates to|trace identity.*gives" standalones/universal_anomaly_*.tex
```

### S7. Arithmetic supplement contradicts its own conditional list

Anchors:

- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:54`
- `standalones/universal_anomaly_local_global_arithmetic_supplement.tex:58`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:591`
- `standalones/universal_anomaly_voa_explicit_supplement.tex:709`

Drift: the local-global supplement correctly says the nine-element
replacement is conditional, but the VOA supplement says each of the
nine carries a canonical arithmetic VOA.

Heal: every occurrence of the nine-list must be prefaced by
"conditional Bruinier/Chenevier list"; canonical arithmetic VOAs should
be "candidate VOAs" until the coefficient/sign computation is supplied.

Patch grep:

```bash
rg -n "nine Heegner|nine discriminants|canonical arithmetic VOA|survive Bruinier|conditional arithmetic refinement" standalones/universal_anomaly_*.tex
```

## Moderate drift

### M1. Old "climax" and "pentagon" language remains in theorem labels and titles

Anchors:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:286`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:298`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:312`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:387`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:801`
- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1362`

Heal: rename manuscript-facing surfaces to "comparison targets",
"conditional bridge", and "conjectural pentagon". Keep old labels only
as internal labels if changing references is too wide.

Patch grep:

```bash
rg -n "climax|climaxes|four-climax|five-vertex pentagon|pentagon" standalones/universal_anomaly_*.tex
```

### M2. Supplements interrupt the status ladder

Anchor:

- `standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex:1138`

Heal: move supplements after open questions under `\appendix`, or
convert their top-level `\section`s to appendix sections. This is
architectural, but it affects status because the supplements currently
look like mid-proof support for the bridge.

Patch grep:

```bash
rg -n -F '\input{universal_anomaly_' standalones/universal_anomaly_four_climax_simultaneously_2026_04_22.tex
```

### M3. Metadata does not currently guard this standalone

Anchor:

- `metadata/theorem_registry.md:1`

Observation: the registry is generated from the main TeX tree; this
standalone and its supplements are not represented in `metadata/claims.jsonl`.
If this standalone is to become a canonical paper, add it to the
metadata extraction surface or keep a separate standalone claim map.

Patch grep:

```bash
rg -n "universal_anomaly_four_climax|atiyah-connes|thm:main|conj:atiyah-connes-pentagon" metadata/*.json* metadata/*.md
```

## Minimal patch order

1. Rewrite abstract/status summary: no "proved construction" unless
   the cyclic-HKR datum is inserted.
2. Split `thm:main` into proved target/falsifier theorem and
   conditional bridge theorem; update stale references to
   `thm:main(i)`, `(iii)`, `(iv)`, `(v)`.
3. Define B1's obstruction target using P02's
   \(\Defcyc^{\mathrm{mod}}\) receptacle.
4. Insert P05 derived-loci base/zero-locus definitions before the
   bridge, or remove derived-loci language.
5. Fence K3/trace input by P04's stable constants plus conditional
   compact-realization hypotheses.
6. Demote the Clemens/Strominger corollary to conditional/open and
   make the open question the controlling surface.
7. Clean "climax" language and move supplements to appendices.

Residual risk after those patches: the class itself still remains
conditional until P01's cyclic-HKR datum and independence proof are
inscribed. That is the decisive proof obligation for making the paper a
new theorem rather than a serious frontier architecture.
