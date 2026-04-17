# Theorem H attack-and-heal ledger (2026-04-18)

Target. Theorem H (chiral Hochschild concentration in degrees
`{0,1,2}`) at `chapters/theory/chiral_hochschild_koszul.tex` (Vol~I),
with companion inscription at
`chapters/theory/chiral_center_theorem.tex`.  Status entering the
session: PROVED sharp Hilbert series on the Koszul locus; critical
level `k = -h^v` excluded; Step~3 circularity resolved 2026-04-16 via
rerouting through `thm:pbw-koszulness-criterion`; three HZ-IV
decorators advertised.  Load-bearing lemma `lem:chiral-quadratic-koszul`
flagged by the mission brief as a candidate AP242 forward reference.

## Phase~1. Adversarial attack from first principles.

### A1. Is `lem:chiral-quadratic-koszul` inscribed or forward?

Finding. INSCRIBED, not forward.  The lemma has both
`\label{lem:chiral-quadratic-koszul}` at
`chiral_hochschild_koszul.tex:657` and a proof body at lines 687-727.
The prior AP242 concern is unsubstantiated at spot-check.

### A2. Does the Fresse transport actually transport?

The lemma transports Fresse's operadic quadratic Koszul dual
construction (symmetric operads over a field) to chiral operads on a
smooth curve, along the OPE-residue pairing.  The classical
construction (Fresse 2017, Prop.~7.1.3 + Thm.~7.3.1) requires the
composition pairing on `F(E)(3)` to be NON-DEGENERATE, so that the
relation-space annihilator `R^perp` defines a dual operad of the right
rank.  The pre-heal proof body asserts "the compatibility holds
because both sides are computed by the same collision-residue
formula" but does NOT address non-degeneracy.

Finding. Non-degeneracy is the load-bearing input to the transport.
Without it, `R^perp` is too large and the "chiral Koszul dual" is
ill-defined.  This is the genuine mathematical content that had to be
made explicit.  The transport is nevertheless valid: by flatness of
`E` and smoothness of `X`, the free-operad piece `F(E)(3)` is a
locally free `D_{X^3}`-module whose fibre at a generic point is the
classical `F(E_p)(3)`; the classical Fresse non-degeneracy transports
fibrewise, and propagates by coherence and semicontinuity; at
collision divisors the specialisation factors through `FM_3(C)`,
where the pairing is non-degenerate by Kontsevich formality.

### A3. Are the HZ-IV decorators vacuous (AP277)?

Finding. Test body is NOT tautological.  The file
`compute/tests/test_theorem_H_hochschild_koszul.py` wires to real
engine calls `chirhoch_heisenberg()`, `chirhoch_virasoro()`,
`chirhoch_affine_km("sl_2")` from
`compute/lib/chirhoch_dimension_engine.py`, and asserts specific
Hilbert triples (1,1,1) / (1,0,1) / (1,3,1) and totals 3 / 2 / 5.

Residual HZ-IV gap (HONEST, smaller than AP277).  The engine's
dataclass values are annotated `# VERIFIED: [DC]
chiral_center_theorem.tex lines 1780-1795` etc.  The cited "verified
against" classical sources in the decorator prose (Feigin-Fuchs 1984
Fock-BRST; Wang 1998 semi-infinite BRST; Whitehead + Kunneth for
affine sl_2) are not independently wired as engines; they are the
bibliographic provenance of the Hilbert triples, but the numerical
cross-check inside the test uses the chapter-derived engine, not an
independent Feigin-Fuchs engine.  This is the correct residual: the
decorator prose is sound, the test is not a `assert True`, but the
engine and the chapter under review share a source of truth.  The
honest label for this is: "partial HZ-IV; disjoint numerical engine
for Feigin-Fuchs / Wang not yet implemented."

### A4. Is the critical-level exclusion load-bearing?

Finding. YES.  At `k = -h^v` the Feigin-Frenkel centre
`Fun(Op_{g^v}(D))` is infinite-dimensional, `ChirHoch^0` is no longer
scalar, the Koszul hypothesis fails (PBW associated graded becomes
non-Koszul at critical level for affine Kac-Moody), and the FM-tower
collapse no longer applies.  The exclusion is inscribed with
mathematical content at
`rem:critical-level-dimensional-divergence`:1852-1897 and is not a
rhetorical scope tag.

### A5. AP255 scan of `thm:hochschild-concentration-E1` and `thm:pbw-koszulness-criterion`.

Finding. `standalone/theorem_index.tex:2380-2381` tagged both labels
with `chiral_pbw_koszulness.tex [PHANTOM FILE]`.  Direct grep of
`chapters/` shows both labels are in fact inscribed in LIVE chapters:

- `thm:pbw-koszulness-criterion` at `chiral_koszul_pairs.tex:784`,
- `thm:hochschild-concentration-E1` at `chiral_hochschild_koszul.tex:1342`.

The index pointers were stale AP255 claims, not real phantoms.

## Phase~2. Surviving core.

Theorem H's concentration statement in `{0,1,2}` and the sharp bigraded
Hilbert series

```
P_A(t,q) = HS_{Z(A)}(q) + HS_{ChirHoch^1(A)}(q) t + HS_{Z(A^!)}(q) t^2
```

survive.  The proof routes: (i) PBW criterion
`thm:pbw-koszulness-criterion` supplies chiral Koszulness from
classical Koszulness of the associated graded; (ii) Shelton-Yuzvinsky
1997 supplies Koszulity of the pure-braid Orlik-Solomon algebra,
transported through the Fresse chain map `sigma` of
`lem:chiral-quadratic-koszul`; (iii) the FM-formality spectral
sequence of `prop:fm-tower-collapse` collapses the configuration tower
to the curve-level `D_X`-Ext, whose amplitude is `[0, 2 dim_C X] = [0,2]`
on a smooth curve; (iv) Koszul duality `thm:main-koszul-hoch` gives
`dim ChirHoch^2(A) = dim Z(A^!)`.

Scope qualifiers that survive unchanged: quadratic on the Koszul
locus; critical level `k = -h^v` excluded with explicit divergence
mechanism recorded.

The ordered-bar E_1-variant `thm:hochschild-concentration-E1` survives
as inscribed, with the honest scope remark that its subscript "E_1"
denotes the first page of the collision-depth spectral sequence on
ordered FM, not E_1-chiral input (Yangian); the hypothesis is the
PBW criterion, an E_∞-chiral condition.

## Phase~3. Heal.

H1.  Rewrote proof of `lem:chiral-quadratic-koszul` at
`chiral_hochschild_koszul.tex:687-727` with Step~1 (non-degeneracy of
OPE-residue pairing via fibrewise reduction to classical Fresse +
coherence propagation + Kontsevich formality at collision divisors)
and Step~2 (Fresse transport) explicit.  The transport step now
depends on a named input that can be falsified rather than an
asserted compatibility.

H2.  Corrected stale AP255 rows in `standalone/theorem_index.tex`:
`thm:pbw-koszulness-criterion` relocated to
`chiral_koszul_pairs.tex`; `thm:hochschild-concentration-E1` relocated
to `chiral_hochschild_koszul.tex`; `[PHANTOM]` tags removed.

H3.  No HZ-IV decorator rewrite: the test body is genuine.  The
residual disjointness gap (engine shares a source with the chapter)
is recorded in the Theorem H row of CLAUDE.md as an AP277 residual
rather than silently passed over.

H4.  No downgrade.  The theorem's proof chain is load-bearing
complete under the standard hypotheses and the now-explicit
non-degeneracy of the OPE-residue pairing.

## Phase~4. Inscription.

See the diff at `chiral_hochschild_koszul.tex:687-747` (the proof body
replacement) and `standalone/theorem_index.tex:2380-2381` (the index
row correction).  Prose follows the manuscript's established register
(subject-led sentences, no hedging, no em-dashes, no catalogue
labels).  `\ClaimStatusProvedHere` tags are preserved for both the
lemma and the two theorems.

## Phase~5. Propagate.

P1.  Grep across Vol~I chapters / standalone / appendices for
`\ref{thm:hochschild-concentration-E1}` returns hits in
`chiral_hochschild_koszul.tex` (self-references), one external in
`theorem_h_off_koszul_platonic.tex:43`, one cross-file in
`five_theorems_modular_koszul.tex:3057`, and the now-corrected index
row.  No broken references.

P2.  Grep for `\ref{lem:chiral-quadratic-koszul}` returns only
self-references inside `chiral_hochschild_koszul.tex`; the lemma is
used locally in the proofs of `prop:fm-tower-collapse`,
`lem:chiral-homotopy-transport`, `thm:hochschild-concentration-E1`,
and `rem:sigma-inverse-chain-level`.

P3.  Grep for `\ref{thm:pbw-koszulness-criterion}` returns hits across
preface, several theory chapters, and the theorem index.  All pointers
resolve to the inscribed label at `chiral_koszul_pairs.tex:784`.

P4.  Updated `CLAUDE.md` Theorem H row with the non-degeneracy step
now explicit, the AP242 / AP255 / AP277 audit outcomes, and file-line
pointers for future audits.

P5.  Vol~II / Vol~III grep not performed in-session; no direct
consumers outside Vol~I are known from the mission brief.

## Verdict.

Theorem H (sharp Hilbert series, concentration in `{0,1,2}`, Koszul
locus) and its E_1-variant via ordered FM remain PROVED at their
stated scopes.  One genuine gap in the Fresse transport
(non-degeneracy of OPE-residue pairing) has been closed by making the
fibrewise reduction explicit.  One AP255 phantom-file flag in the
index was stale and has been corrected.  The HZ-IV decorators are
sound at the prose level and the test body is genuine; the residual
disjointness gap has been recorded honestly in CLAUDE.md as an AP277
residual.  No downgrade is warranted.

Raeez Lorgat, 2026-04-18.
