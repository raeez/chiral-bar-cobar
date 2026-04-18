# Attack-heal: dim H^1(sl_2) at critical level — three-object conflation

Date: 2026-04-18
Author: Raeez Lorgat
Isolation: worktree agent-a1b851a2
Mission: resolve the F3 contradiction surfaced by the Casimir-convention agent between chapter canon "dim H^1(sl_2) = 3 via Whitehead" and five standalone sites advertising "H^1 doubles 4 → 8" at critical level k = -h^v.

## Diagnosis: four distinct cohomological objects share the symbol "H^1(sl_2)"

The "contradiction" is an AP312 three-way scalar value collision. Close reading of primary sources shows four DIFFERENT cohomology groups indexed by "H^1" with very different values.

### Object (A) — symmetric bar, full chiral algebra, generic level
Source: `chapters/theory/bar_construction.tex:1633`.
```
V_k(sl_2), generic k != -h^v:  dim H^1(B^{Sigma}(V_k(sl_2))) = 3 = dim sl_2.
```
Mechanism: Whitehead + augmentation-ideal identification. The three classes are
the three sl_2 current modes (J^+, J^0, J^-); higher-weight contributions are
killed by semisimplicity of the coefficient module at generic level. Consistent
with `chapters/examples/landscape_census.tex:2601` ("3 = dim sl_2").

### Object (B) — degree-2 ordered chiral homology (ordered bar restricted to V ⊗ V)
Source: `chapters/theory/ordered_associative_chiral_kd.tex:12130-12201` and
`chapters/theory/ordered_associative_chiral_kd.tex:12239`.
```
At generic k:         dim H^0_{ord,2} = 0,  dim H^1_{ord,2} = 4   (chi_{ord,2} = -4).
At critical k = -2:   dim H^0_{ord,2} = 4,  dim H^1_{ord,2} = 8   (chi_{ord,2} = -4 conserved).
```
This is a FINITE-dimensional computation on the rank-4 bicomplex supported on
V ⊗ V where V is the sl_2 fundamental. The "4 → 8" doubling is a legitimate
statement about this degree-2 slice alone: trivial critical-level monodromy
moves 4 classes from H^1 to H^0 while the Euler characteristic chi = -4 holds.
This is the content of `prop:critical-level-ordered`.

### Object (C) — genus-1 KZB rank-4 local system on E_tau \ {0}
Source: `chapters/theory/e1_modular_koszul.tex:1145-1173`.
```
generic hbar:  dim H^1(KZB_{4}) = 4   (Euler characteristic of rank-4 local system).
```
This is the genus-1 KZB monodromy at degree 2, an entirely separate object
from (A) and (B). The "4" is a coincidence of rank, not the same 4 as in (B).

### Object (D) — full symmetric bar cohomology at critical level
Source: `chapters/examples/kac_moody.tex:4300-4424`, especially `thm:oper-bar-h0`,
`prop:oper-bar-h1`, `thm:oper-bar`, and `rem:frenkel-teleman-oper`.
```
V_{-h^v}(g):  H^n(B^{Sigma}(V_{-h^v}(g))) cong Omega^n(Op_{g^v}(D))  for all n >= 0.
```
Infinite-dimensional in every cohomological degree n >= 0. Primary sources:
Feigin-Frenkel 1992, Frenkel-Teleman 2006. For sl_2: Omega^1(Op_{sl_2}(D)) is
the module of Kahler differentials of Fun(Op_{sl_2}(D)), an infinite-rank free
module over the (infinite-dim) Feigin-Frenkel centre.

### The drift: five standalones fuse (A)(B)(D)
`standalone/ordered_chiral_homology.tex:7317-7328`, `standalone/holographic_datum.tex:716-724`,
`standalone/genus1_seven_faces.tex:908-953`, `standalone/survey_modular_koszul_duality_v2.tex:1329`,
`standalone/survey_modular_koszul_duality_v2.tex:2859`,
`standalone/survey_modular_koszul_duality_v2.tex:7286`.
Each writes "H^1 doubles from 4 to 8 for sl_2" alongside "bar cohomology spreads
to Omega*(Op_{sl_2}(D))", silently conflating the finite object (B) with the
infinite object (D). A reader who checks (A) at generic level sees "3", not "4",
and loses confidence in the whole narrative. The root cause is omission of the
(ordered, degree-2) qualifier on the 4 → 8 claim.

The chapter-canon `prop:critical-level-ordered` at
`chapters/theory/ordered_associative_chiral_kd.tex:12130-12201` is honest:
it writes "degree-2 ordered chiral homology" explicitly in clause (iii) and
keeps the Omega*(Op) identification as a SEPARATE clause (iv). The five
standalones compress this into one sentence and lose the qualifier.

## Healing per AP266 (sharpened obstruction, scope discipline)

Two honest heals apply per object:

- (A) at generic level: `dim H^1(B^{Sigma}) = 3` is chapter canon. Untouched.
- (B) at critical level: `dim H^1_{ord, 2} = 8` is correct on V ⊗ V. Untouched
  on the chapter side; in the five standalones, add the explicit qualifier
  "degree-2 ordered" and acknowledge the degree-1 symmetric bar dim H^1 = 3
  (generic) is a DIFFERENT invariant. The "4 → 8 doubling" of (B) does NOT
  describe the chapter-canon H^1 = 3.
- (D) at critical level: bar cohomology IS infinite-dimensional, not 8.
  "Bar H^* spreads to Omega*(Op)" is correct; "H^1 is 8-dimensional" is false
  for the full symmetric bar (true only for the degree-2 ordered slice).

The fix preserves the chapter canon untouched and inserts scope qualifiers into
the five standalones. The (ordered, degree-2) qualifier converts the conflation
into two honest statements.

## CLAUDE.md line 623 rectification

Old: `At k=-h^v: kappa=0, monodromy trivial, H^1 doubles (4→8), Koszulness fails, bar H* = Omega*(Op_g^v(D)).`

New: `At k=-h^v: kappa=0, monodromy trivial, degree-2 ordered chiral homology H^1_{ord,2} doubles 4 -> 8 (finite, on V⊗V), FULL bar cohomology H^n(B^Sigma) = Omega^n(Op_{g^v}(D)) (infinite-dim, Frenkel-Teleman 2006), Koszulness fails. 72 tests.`

This separates object (B) from object (D) at the metacognitive layer and
prevents the drift the five standalones exhibit.

## Edits applied (this worktree)

1. `standalone/ordered_chiral_homology.tex:7322` — add "degree-2 ordered" qualifier.
2. `standalone/holographic_datum.tex:718` — add "degree-2 ordered" qualifier.
3. `standalone/genus1_seven_faces.tex:916,952` — add "(degree-2 ordered chiral homology on V⊗V)" qualifier; separate the bar-cohomology-is-Omega*(Op) clause into its own sentence with "infinite-dimensional" noted.
4. `standalone/survey_modular_koszul_duality_v2.tex:1329-1331, 2859-2861, 7286-7287` — add qualifier; clarify the Feigin-Frenkel Omega* identification is infinite-dimensional.
5. `CLAUDE.md:623` — separate object (B) and object (D) at the status-table level.

The primary chapter canon (bar_construction.tex, kac_moody.tex, ordered_associative_chiral_kd.tex, e1_modular_koszul.tex, landscape_census.tex) is NOT edited; the canon is already honest.

## Anti-patterns registered (AP2041-AP2043, minimal per AP314)

**AP2041 (Same symbol "H^1(A)" across three cohomological objects without scope qualifier).** When "H^1" refers to different graded pieces (full symmetric bar vs degree-n ordered slice vs KZB local system) in adjacent paragraphs, a reader loses the ability to tell finite from infinite. Counter: every "dim H^1 = N" statement carries (a) which complex (ordered vs symmetric; full vs degree-k), (b) which parameter locus (generic vs critical), (c) finite-dim vs infinite-dim scope. Canonical violation: the five standalones listed above fused degree-2 ordered (finite, doubles 4 -> 8) with full symmetric bar at critical (infinite, Omega*(Op)). Healing: add explicit "(ordered, degree-2 slice)" or "(full symmetric bar)" qualifier. Related: AP312 (three-way cross-file scalar-value contradiction) at the meta-object level; AP290 (subscript type-swap) at the kappa level.

**AP2042 (Degree-2 ordered homology "4 → 8 doubling" fused with full symmetric "spreads to Omega*(Op)" picture).** A text writes two sentences back-to-back where the first names a finite invariant and the second invokes an infinite-dimensional structure identifying the same invariant with an oper-space de Rham complex. If "H^1 = 8" and "H^1 = Omega^1(Op)" appear in the same paragraph without explicit "these are two different H^1" acknowledgement, the reader is trained to believe Omega^1(Op) is 8-dim. Counter: separate the two statements into distinct sentences and explicitly note they concern different bar complexes (ordered degree-2 vs full symmetric). Healing applied in this heal: restructure each of the five standalone sites so that the degree-2 ordered computation and the full symmetric critical-level identification are visibly distinct.

**AP2043 (Status-table "H^1 doubles 4 → 8" without object specifier).** CLAUDE.md line 623 inherits AP2042 at the metacognitive layer. A reader of the status table cannot tell which H^1 is advertised. Counter: status rows referring to a scalar invariant must specify the complex, the degree-slice, and the ambient. Healed by separating object (B) (finite, ordered degree-2) from object (D) (infinite, Frenkel-Teleman) in the same row.

## Primary-source citations (not fabricated)

- **Feigin-Frenkel 1992**: "Affine Kac-Moody algebras at the critical level and Gelfand-Dikii algebras." Int. J. Mod. Phys. A, Vol. 7, Supp. 1A. Gives Z(V_{-h^v}(g)) cong Fun(Op_{g^v}(D)).
- **Frenkel-Teleman 2006**: "Self-extensions of Verma modules and differential forms on opers." Compositio Math. 142(2), 477-500. Gives Ext^n(V_crit, V_crit) cong Omega^n(Op_{g^v}(D)) for all n >= 0.
- **Frenkel 2007**: "Langlands Correspondence for Loop Groups," Cambridge University Press. Theorem 4.3.2 and Ch. 10 synthesise the critical-level oper identification.

Each of these gives an INFINITE-dimensional object; none gives 8.

## Patch (worktree → main apply)

```
cd /Users/raeez/chiral-bar-cobar
git apply adversarial_swarm_20260418/patches/h1_sl2_critical_level.patch
```

Patch file at `adversarial_swarm_20260418/patches/h1_sl2_critical_level.patch` in main repo after commit (per AP316 delivery discipline).
