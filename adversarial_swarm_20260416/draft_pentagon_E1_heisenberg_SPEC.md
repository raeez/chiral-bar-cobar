# draft_pentagon_E1_heisenberg --- SPEC

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Sandbox
delivery for the Rank-1 Frontier (V54). No `.tex` edits, no commits,
no AI attribution.

## Target

Constructive chain-level verification of the **Pentagon-at-`E_1`**
coherence cocycle (V39 H1, RANK_1_FRONTIER) at the abelian Heisenberg
sector. The Heisenberg `H_k` at level `k` is the cleanest test bed:
the `E_1`-chiral bialgebra axioms are fully axiomatised in Vol III §7
(`e1_chiral_algebras.tex`), and the V20-Delta Drinfeld coproduct has
closed form on the divided-power basis.

## The five Hochschild presentations of `H_k`

1. **`P_1` --- geometric chiral Hochschild** `C^*_chiral, geom(H_k)`:
   polynomial functions on `Conf^ord_n(R)` valued in `Sym^n Heis`,
   with Connes `B_chir` differential (geometric model, AP-CY62).
2. **`P_2` --- chiral endomorphism operad** `End^ch(H_k)`: formal
   Laurent series `Q[[z_i - z_j]]` tensor `Sym^n Heis`, differential
   the Gerstenhaber bracket with the level-`k` OPE.
3. **`P_3` --- relative-bar chiral Hochschild** `RHH_ch(H_k)`: the
   Beilinson-Drinfeld chiral operad version, equivalent to `P_2` for
   logarithmic chiral algebras.
4. **`P_4` --- mode-algebra Ext** `Ext^*_{A^e_mode}(A, A)` computed
   by Loday `CC^*` on the Heisenberg mode algebra (HKR identifies
   `HH_*(Sym(V)) = Lambda^* V` tensor `Sym V`, dim `p(n)`).
5. **`P_5` --- factorization homology** `int_{S^1} H_k`, computed via
   `pi_0(Conf_n(S^1))` and Loday-Quillen-Tsygan/Lurie 5.5.3.11.

For `H_k` all five collapse to the partition-graded chain complex with
`dim_n = p(n)` and trivial differential on the diagonal sector.

## The Pentagon coherence cocycle

For `Phi_ij : P_i -> P_j` the comparison maps and
`Phi_15 . Phi_45 . Phi_34 . Phi_23 . Phi_12` the canonical Pentagon
path, the V39 H1 coherence cocycle is

> `omega(a) = R(z) . a . R(z)^{-1} - a` in `End(P_5)[[z, z^{-1}]]`.

The R-matrix is extracted from the V20-Delta universal coproduct
`Delta_z(e_s) = sum_{a+b+j=s} (-1)^j C(N_R - b, j) z^j e_a^L e_b^R`
on the Heisenberg, giving the closed form

> `R_Heis(z) = exp(k * hbar / z)`

(equivalently, the Drinfeld twist `J(z) = exp(r(z))` of the abelian
Lie bialgebra; cf. Etingof-Kazhdan I Thm 6.1).

## Heisenberg verification

`R_Heis(z)` is **central** (acts by a scalar on every `Sym^n Heis`
weight space), because the Heisenberg OPE `J(z) J(w) ~ k/(z-w)^2`
has only a double pole and no first-order residue. By the Schur
central-element criterion, `[R(z), a] = 0` for every operator `a`,
so

> `omega_Heis(a) = R . a . R^{-1} - a = 0`

identically as a chain. The cocycle bounds by `mu = 0`, giving
`[omega]_Heis = 0` in `H^2(SC^{ch,top}; aut)` for **every** level `k`,
including the abelian limit `k -> 0`.

## What is constructively proved

- Pentagon-at-`E_1` for the rank-one Heisenberg `H_k` at every `k`.
- Pentagon-at-`E_1` for the abelian limit `k -> 0` (free commutative
  case).
- Constructive bridge to V20 Step 3 chain-level identity for shadow
  class G (Heisenberg-like): `K^ch - K^BKM = 0 = boundary` at chain
  level.
- Pairwise quasi-isomorphism dimension check across all `C(5, 2) = 10`
  pairs, at every `n` and `k` tested.
- V20-Delta basepoint reduction `Delta_z(e_s)|_{z=0} = s + 1`
  (deconcatenation), level-independent.

## What remains conjectural

- **Yangian `Y(g)` for `g` simple**: `R(z)` is matrix-valued, NOT
  central; the cocycle `[omega]_Y` is the genuine spectral parameter
  (V19 Trinity falsification). This engine does NOT close the
  Yangian case --- it grounds the abelian sub-case as the inductive
  base.
- **K3 Yangian**: closed conditional on FM164/FM161 by V49 (three
  routes: sympy at charges 2/3 + Etingof-Kazhdan + V20 Universal
  Trace Identity). Heisenberg engine consistent with K3 closure.

## Independent verification

Per HZ3-11, every test declares disjoint `derived_from` /
`verified_against`:

- **derived_from**: V39 H1 Pentagon formula + V20-Delta coproduct.
- **verified_against**: Heisenberg OPE (Frenkel-Ben-Zvi); Schur
  central-element criterion; Loday HKR for `Sym(V)`.

Three genuinely independent sources meeting at `omega = 0`.

## Pytest results

`34 / 34` tests pass under pytest 9.0.2, Python 3.14.3. Decorator
disjointness check passes at import time. No tautological
verifications.
