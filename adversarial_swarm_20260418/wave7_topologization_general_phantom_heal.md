# Wave 7: `conj:topologization-general` phantom heal — FALSE-POSITIVE VERDICT

Date: 2026-04-18
Scope: Vol I + Vol II + Vol III
Trigger: Wave-6 AP255 phantom-label programme sweep flagged `conj:topologization-general` as the TOP-PRIORITY Tier-1 mass-consumer phantom (37 refs, ABSENT in Vol II).

## Verdict

**NO INSCRIPTION ACTION REQUIRED.** The Wave-6 finding was a STALE false-positive.

The label `\label{conj:topologization-general}` IS inscribed in Vol I at
`chapters/theory/en_koszul_duality.tex:3392`, inside a properly-tagged
`\begin{conjecture}[Chain-level topologization for general chiral
algebras]` environment carrying `\ClaimStatusConjectured`. The metadata
index confirms (`metadata/claims.jsonl:2081`; `metadata/label_index.json:2682`;
`metadata/dependency_graph.dot:2169`). The inscription was healed in an
earlier wave (consistent with the archival markdown trail under
`rectification_20260412_233715/`, `relaunch_20260413_111534/`,
`healing_20260413_132214/`); the Wave-6 phantom detector missed it,
likely because the `\begin{conjecture}[...]` header and `\label{...}`
sit on separate lines and the detector's regex assumed same-line
co-location.

## Phantom verification (grep evidence)

Direct label grep:
```
grep -rn '\\label{conj:topologization-general}' chapters/ standalone/ appendices/
chapters/theory/en_koszul_duality.tex:3392:\label{conj:topologization-general}
```
One hit in Vol I live source. Zero hits in Vol II `.tex` sources (sc_chtop_heptagon.tex:1216 is a `\ref` consumer, not a `\label`). Zero hits in Vol III live sources.

## Consumer enumeration (live `.tex` only, archival notes excluded)

**Vol I** (9 prose consumers + 1 table + 1 metadata index = 11):
- `chapters/theory/introduction.tex:1746, 1898, 2391`
- `chapters/theory/en_koszul_duality.tex:3139, 3329, 3386, 3874, 4896, 5074`
- `chapters/frame/preface.tex:4176`
- `chapters/connections/concordance.tex:7344`
- `standalone/theorem_index.tex:619` (metadata row, resolves)

**Vol II** (1):
- `chapters/theory/sc_chtop_heptagon.tex:1216`

**Vol III**: zero live `.tex` consumers. (`AGENTS.md` mention is prose, not `\ref`.)

Total live consumers: ~12 (not 37). The 37-count in the Wave-6 sweep was inflated by archival markdown notes under `relaunch_*`, `rectification_*`, `healing_*`, `opus_audit_*`, `wave2_audit_*`, and worktree duplicates — session ledgers that do not affect the build and do not render `[?]`.

## Inscribed body audit (against drafted heal template)

The inscribed conjecture at `en_koszul_duality.tex:3391-3414` reads:

```
\begin{conjecture}[Chain-level topologization for general chiral algebras]
\label{conj:topologization-general}
\ClaimStatusConjectured
Let A be a chiral algebra with conformal vector T(z) at non-critical
parameters, and suppose the corresponding 3d holomorphic-topological
bulk theory admits a BRST complex in which holomorphic translations
are Q-exact by an antighost contraction. Then the analogue of
Theorem [thm:topologization] holds:
(i) BRST cohomology H_Q^*(Z^der_ch(A)) carries an E_3^top structure;
(ii) the cohomology complex gives a chain-level E_3^top model on a
    quasi-isomorphic complex;
(iii) the original complex Z^der_ch(A) carries a chain-level E_3^top
    structure whenever the corresponding A_infinity-coherence tower
    trivializing holomorphic translation vanishes.
\end{conjecture}
```

This is STRONGER than the template prepared for heal option (a): the
inscribed statement has three explicit clauses separating BRST-
cohomological, chain-level-on-quasi-iso, and chain-level-on-original
cases — matching exactly the HZ granularity demanded by AP-TOPOLOGIZATION
and AP258 (cohomological-vs-chain status drift). Accompanying
`rem:topologization-evidence` at :3416 then provides the honest
obstruction-map: for affine KM the (i) and (ii) clauses are
unconditional (via `thm:topologization`), clause (iii) is the gap;
for class M the shadow tower's infinite-degree operations may obstruct
chain-level E_3 on the original complex.

The inscribed body ALREADY satisfies the heal discipline. No rewrite
indicated.

## CLAUDE.md consistency (AP271 reverse-drift check)

Vol I CLAUDE.md entries cross-checked:
- AP-TOPOLOGIZATION (merged): says "PROVED for affine KM V_k(g) at
  non-critical level k != -h^v; CONJECTURAL for general chiral
  algebras with conformal vector (conj:topologization-general). Proof
  COHOMOLOGICAL (Q-cohomology), not chain-level; for class M chain-
  level E_3 may fail." MATCHES inscribed body.
- Topologization row of theorem-status table: scopes class-L strict
  chain-level explicitly as a FRONTIER item, naming the draft
  candidate antighost-contact formulas as retracted pending
  independent verification. MATCHES.
- E_3 identification row: scopes affine KM Sugawara-unconditional vs
  general conjectural via `conj:topologization-general` pointer.
  MATCHES.

No AP271 drift detected. CLAUDE.md does not overclaim against the
inscribed conjecture.

## Wave-6 sweep detection-gap — recommendation

The Wave-6 phantom detector missed a real label that sits below its
`\begin{conjecture}[...]` header. Two improvements for future sweeps:

1. Phantom-label detector should parse multi-line environments: after
   matching `\begin{conjecture}[...]`, scan the next 3 lines for a
   `\label{...}` before declaring phantom.

2. Cross-check against `metadata/claims.jsonl` and
   `metadata/label_index.json` when an index exists: a label present in
   the claims jsonl but reported phantom by the text sweep is a
   DETECTION GAP, not a missing inscription. Raise as diagnostic, not
   as heal priority.

## Operational outcome

No commit to produce. The Wave-6 phantom list should be updated to
reclassify `conj:topologization-general` from Tier-1 phantom to
"INSCRIBED — sweep false-positive (multi-line header/label)". The
remaining Wave-6 Tier-1 candidates should be re-verified with the
improved detector before inscription effort is spent.

Note also: the related Vol II inscription
`conj:e-infinity-specialisation-Winfty` at
`e_infinity_topologization.tex:679` is a distinct, separately-
inscribed conjecture covering the W_inf endpoint of the E_infinity
topologization ladder; it is not a candidate retarget for
`conj:topologization-general` (different scope — iterated-Sugawara
depth-N endpoint vs existence of Q-exact antighost on a general
chiral algebra with conformal vector).

## Author

Raeez Lorgat
