# Wave-12 Heal: modular_trace.tex:80 + cy_to_chiral.tex:411

## Status

Two atomic heals applied to Vol III `chapters/theory/`. No commits.

## Site 1: `modular_trace.tex:80` — AP289 mixed-route

### First-principles analysis

`prop:kappa-non-multiplicative` (lines 75-90) demonstrates that
`kappa_BKM` does not satisfy the product rules governing either
`kappa_ch` or `kappa_cat`. The proposition's purpose is
falsification-by-contrast: compute the two candidate rules, compare to
the true `kappa_BKM(K3 x E) = 5`, exhibit failure of both.

Pre-heal display wrote
```
kappa_ch(K3) * kappa_ch(E) = 2 * 1 = 2,   kappa_BKM(K3 x E) = 5.
```
This is a ROUTE-B vs ROUTE-A category collision:

- Values 2 and 1 are Heisenberg-level kappa_ch (Route B: K3 ↦
  H_{Mukai}, level 2; E ↦ H_1, level 1). Route B's combinator is
  ADDITIVE: kappa_ch(K3 x E) = kappa_ch(K3) + kappa_ch(E) = 3,
  confirmed at line 87 and line 54 of the chapter table.
- The Hodge-supertrace / categorical Euler-char invariant (Route A,
  here kappa_cat) IS multiplicative under products (Kunneth). But
  Route-A values for K3 and E are chi(O_K3) = 2, chi(O_E) = 0 (Serre
  duality: h^{0,0} - h^{0,1} = 1 - 1 = 0 for elliptic). Route-A
  product: 2 * 0 = 0.
- The pre-heal line multiplied Route-B values (1 for E, from
  Heisenberg level) with the Route-A rule (*). The product 2*1=2 has
  no mathematical meaning — it neither computes kappa_ch(K3 x E) (= 3)
  nor kappa_cat(K3 x E) (= 0) nor kappa_BKM(K3 x E) (= 5).

### Heal

Replaced the single muddled foil by TWO honest foils, one per route:

```
kappa_ch(K3) + kappa_ch(E)  = 2 + 1 = 3   (Route B, additive)
kappa_cat(K3) * kappa_cat(E) = 2 * 0 = 0   (Route A, Kunneth-multiplicative)
kappa_BKM(K3 x E)                    = 5.
```

Discrepancy text updated: `5 != 3` (Route B fails) and `5 != 0`
(Route A fails). Commented warning cites
`cy_d_kappa_stratification.tex:411-426` for the route discipline and
registers the AP289 + AP290 violations.

### Verification

- chi(O_E) = 1 - 1 = 0 by Serre duality on elliptic curve. [AP289]
- chi(O_{K3 x E}) = chi(O_K3) * chi(O_E) = 2 * 0 = 0 by Kunneth.
- kappa_ch(K3 x E) = 3 reconfirmed (line 87, Prop.~kappa-k3).
- kappa_BKM(K3 x E) = 5 = wt(Delta_5) reconfirmed.

All numerical values cross-check against the Proposition
"categorical-euler" table at lines 50-57.

## Site 2: `cy_to_chiral.tex:411` — AP290 category-jump

### First-principles analysis

`conj:enriques-kappa-spectrum` clause (iii) for S = Enriques surface
wrote:
```
kappa_cat(S x E) = kappa_ch(S) + kappa_ch(E) = 1 + 1 = 2.
```
Three simultaneous violations:

1. **AP290 (subscript type-swap).** LHS is kappa_cat (categorical
   Euler characteristic = chi(O)); RHS wrote kappa_ch (chiral-algebra
   conductor). These are distinct invariants by definition (Remark
   `categorical-vs-topological-chi`, line 70).
2. **AP289 (Kunneth-multiplicative vs additive).** kappa_cat satisfies
   chi(O_{X x Y}) = chi(O_X) * chi(O_Y) by Kunneth, NOT additively.
3. **Arithmetic wrong anyway.** Even in the erroneous Route-B reading
   "kappa_ch(S x E) = kappa_ch(S) + kappa_ch(E)", the elliptic
   contribution kappa_ch(E) = 1 via Heisenberg level uses the Route-B
   convention, but chi(O_E) = 0 via Serre duality uses Route A; mixing
   them gives a meaningless sum.

Correct computation:
- S Enriques: chi(O_S) = h^{0,0} - h^{0,1} + h^{0,2} = 1 - 0 + 0 = 1.
  (omega_S is nontrivial 2-torsion, so h^{0,2} = 0; h^{0,1} = 0 for
  Enriques.)
- E elliptic: chi(O_E) = 1 - 1 = 0.
- Kunneth: kappa_cat(S x E) = chi(O_S) * chi(O_E) = 1 * 0 = 0.

### Heal

Replaced the clause by the correct Kunneth product:
```
kappa_cat(S x E) = chi^{CY}(D^b(Coh(S x E))) = chi(O_{S x E})
                 = chi(O_S) * chi(O_E) = 1 * 0 = 0.
```
Commented warning registers AP289 + AP290 and points to
`cy_d_kappa_stratification.tex:411-426` for route discipline.

### Verification

- chi(O_{Enriques}) = 1 reconfirmed at Proposition
  `enriques-hodge` / elsewhere in the chapter.
- chi(O_E) = 0 (AP289 canonical).
- kappa_cat(S x E) = 0 is consistent with `prop:chi-O-vanishes-odd-d`
  in `modular_trace.tex:91`: S x E is CY_3, hence chi(O) = 0.

## Commit plan

Two files changed:
- `calabi-yau-quantum-groups/chapters/theory/modular_trace.tex`
  (lines 78-89).
- `calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
  (lines 411-420).

Per agent brief: NO COMMIT. User adjudicates. If accepted:
- Single Vol III commit titled "Vol III Wave-12 modular_trace +
  cy_to_chiral: AP289/AP290 mixed-route heals (atomic, 2 sites)".
- AP5 propagation: grep Vol I + Vol II for `kappa_ch(K3) \cdot
  kappa_ch(E)` and `kappa_cat.*=.*kappa_ch.*+.*kappa_ch` patterns
  (separate pass).

## Hook false positives

PostToolUse:Edit hooks flagged AP24 (Virasoro complementarity),
AP25/AP113 (bar-cobar, bare kappa) on lines OUTSIDE the edit scope
(pre-existing text at lines 170/174/280/1278/4586). The two edits
themselves were atomic to lines 78-89 and 411-420; cross-check
confirms no regression in the flagged regions.
