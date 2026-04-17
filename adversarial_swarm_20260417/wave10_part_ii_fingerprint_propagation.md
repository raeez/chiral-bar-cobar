# Wave-10 Part II Fingerprint Propagation (F2: p_max vs r_max separator)

**Date**: 2026-04-17
**Scope**: Cross-volume propagation of Wave-9 #59 Part II heal F2 (κ-isospectral
example: separator is `r_max`, not `p_max`). Excludes F1 (V^♮ Monster
fingerprint — delegated to parallel agent).
**Verdict**: NO propagation edits required. Vol I was already consistent
away from the single healed site.

## F2 heal recap

Wave-9 #59 healed the κ-isospectral example in
`chapters/frame/part_ii_platonic_introduction.tex` (lines 132-144):
- Used disjoint level symbols: `H_ℓ` (Heisenberg, level ℓ), `V_k(sl_2)`
  (affine KM, level k), tuned at `k = (4/3)ℓ - 2` to share `κ = ℓ`.
- Confirms `p_max(H_ℓ) = p_max(V_k(sl_2)) = 2` (not a separator).
- Uses `r_max` as the separator: `r_max(H_ℓ) = 2 ∈ G` vs
  `r_max(V_k(sl_2)) = 3 ∈ L`.

## Audit scope

Grep triggers applied across all three volumes:
- `p_{\max}(H` within 200 chars of `p_{\max}(V_k(`
- `isospectral` / `κ-isospectral` / `kappa-isospectral` / `κ-degenerate`
- `tuning.*kappa` / `non-isomorphic.*identical.*kappa`
- `(4/3)ℓ` tuning formula
- Fingerprint tuples `(1,4)`, `(2,2)`, `(2,3)`, `(4,∞)`

## Findings

### Vol I

1. `chapters/frame/part_ii_platonic_introduction.tex`: already healed
   (Wave-9 #59). NOT re-edited per skip-list.
2. `chapters/frame/preface.tex`: clean — uses `r_max` uniformly as
   the separator slot of the five-slot fingerprint. No isospectral drift.
3. `chapters/frame/programme_overview_platonic.tex`: clean — six-slot
   `φ'(A) = (p_max, r_max, χ, n_strong, coset, κ_ch)` canonical.
4. `chapters/frame/part_iii_platonic_introduction.tex`: clean — every
   occurrence of `p_max` / `r_max` consistent; atlas completeness uses
   `(i, j)` pairs with correct non-degeneracy.
5. `chapters/theory/three_invariants.tex`: canonical table
   (β γ (1,0,4), Heis (2,1,2), affine sl_N (2,1,3), Vir (4,3,∞),
   V_{-h^v}(g) (2,1,∞ FF), W_N (2N,2N-1,∞)). Explicit
   `k_max = p_max − 1` relation.
6. `chapters/theory/infinite_fingerprint_classification.tex`: canonical
   five-slot fingerprint; `thm:pole-depth-independence` exhibits exactly
   the Wave-9 canonical table. Also contains the `d_alg = r_max − 2`
   bijection (closes FM110).
7. `standalone/classification_trichotomy.tex` (lines 217-233):
   canonical witnesses (1,4)/(2,2)/(2,3)/(4,∞)/(2N,∞) in
   `prop:independence`.
8. `standalone/survey_modular_koszul_duality.tex` and `_v2.tex`: `r_max`
   used throughout; no isospectral / p_max-separator claim.
9. `standalone/N6_shadow_formality.tex`: canonical table
   `Heis (2,0,2)` — G, `affine (2,1,3)` — L, `β γ (1,0,4)` — C,
   `Vir (4,3,∞)` — M.
10. `standalone/gaudin_from_collision.tex`, `garland_lepowsky.tex`: each
    r_max value tied to the correct family; no drift.
11. `worldview_synthesis_2026_04_17.tex` (lines 225-229): Virasoro
    κ = c/2 at c=13 self-dual; W_N κ = c(H_N − 1); BP κ + κ^! = 98/3.
    No isospectral claim; clean.
12. `working_notes.tex`: r_max-based classification table (lines
    948-962, 1464-1473, 4112-4127); internally consistent.
13. `main.tex`: sole hit was "fine-tuning" in a comment line — not a
    math claim.

### Vol II

- No `κ-isospectral` occurrences.
- No `p_max(H)` vs `p_max(V_k)` separator claim.
- Sole `isospectral` hit: Moser 1975 bibliography reference
  (`main.tex:2596`) — benign.

### Vol III

- No `κ-isospectral` or related drift.
- No `p_max`-separator claim contrasting `H_k` and `V_k(sl_2)`.

## Fingerprint-table sanity check (non-Monster)

Across Vol I and standalones, the canonical tuple values are
uniformly present with no drift:

- `H_k`: `(p_max, r_max) = (2, 2)`, class G.
- `V_k(sl_N)` at generic level: `(2, 3)`, class L.
- `β γ`: `(1, 4)`, class C (note `p_max = 1` is the archetypal witness).
- `Vir_c`: `(4, ∞)`, class M.
- `W_N`: `(2N, ∞)`, class M.
- `V_{-h^v}(g)` critical: `(2, ∞)`, class FF (companion).

## AP5 atomicity

No half-propagation: the single drifted site (part_ii) was healed atomically
in Wave-9 #59, and all downstream uses across both the frame chapters, theory
chapters, standalones, and cross-volume files were already consistent with
that heal before the current audit began.

## Constitutional hygiene

No typeset-prose AP references introduced. No edits to the skip-list files.
No commits (per task instructions).

## Conclusion

Wave-10 F2 propagation: **no edits required**. The κ-isospectral example
was a localised bug in part_ii_platonic_introduction.tex that did not
propagate to any other file in the three-volume programme. The canonical
`r_max`-as-separator convention was already uniform across Vol I framing,
Vol I theory, Vol I standalones, Vol II, and Vol III.
