# Wave-1 F1.c closure: K(W_N) for N ≥ 4

Date: 2026-04-18
Author: Raeez Lorgat
Mission: Retract the stale CLAUDE.md Wave-1 F1.c open-frontier bullet claiming "K(W_N) for N ≥ 4 — Vol I census carries no entry".

## Finding

The F1.c bullet is stale. The closed form for the Koszul conductor of principal W_N
is already inscribed in Vol I with a proof body:

- Primary inscription: `chapters/theory/universal_conductor_K_platonic.tex:641-688`,
  `cor:uc-K-WN` (ProvedHere):
  ```
  K(W_N) = sum_{j=2}^{N} 2(6 j^2 - 6 j + 1)
         = 4 N^3 - 2 N - 2
         = 2(N - 1)(2 N^2 + 2 N + 1).
  ```
  Third forward difference Delta^3 K(W_N) = 24 constant.
  Proof mechanism: Toda BRST spin-tower of bc(j)-ghost generators
  at Casimir spins j in {2, ..., N} (principal Drinfeld-Sokolov),
  applying the per-spin uc-K-g formula.

- Tabulated values: K(W_2) = K(Vir) = 26, K(W_3) = 100, K(W_4) = 246,
  K(W_5) = 488, K(W_6) = 850. Cross-referenced at `chapters/examples/landscape_census.tex`
  L199 (additional tabulations at lines 938 and 1520).

- Modular-characteristic identity: `rem:uc-harmonic-density-WN`:690-699,
  K^kappa(W_N) = kappa(W_N) + kappa(W_N^!) = K(W_N) * (H_N - 1)
               = 2(N-1)(2N^2+2N+1)(H_N - 1),
  closing the varrho_A * K(A) identity for principal W_N for all N >= 2.

## Heals applied to CLAUDE.md

1. Line 1370 (Beilinson-rectified open frontiers list):
   The F1.c bullet rewritten as CLOSED 2026-04-18, citing the inscribed closed form,
   proof mechanism, tabulated values, and the modular-characteristic identity.
   varrho_BP structural-origin bullet (F1.b) explicitly preserved as genuinely open.

2. Line 497 (Wrong Formulas Blacklist B93):
   The "UNTESTED N>=4 (K_{W_N} not in census)" scope claim replaced with
   a citation of the inscribed closed form at cor:uc-K-WN.

No other CLAUDE.md loci referenced "K_{W_N} not in census" or equivalents
(grep-verified across CLAUDE.md).

## AP registration

No new AP needed. The finding is a garden-variety AP271 instance
(reverse drift: CLAUDE.md lagging behind the manuscript; manuscript is
authoritative per the Beilinson epistemic hierarchy). Per AP314
(inscription-rate throttle) the closure is recorded as a status-table
and blacklist update without inscribing a fresh AP number in the
AP1961-AP1980 reserved range. The pre-authored range remains available.

## Epistemic scope of the closure

The closure is tight:

- Scope: principal W_N = W_N^k(sl_N) at non-critical level (the universal_conductor_K_platonic.tex
  Toda BRST derivation is principal-only; non-principal nilpotents require
  Jacobson-Morozov decomposition and are NOT covered by cor:uc-K-WN).
- Convention: the K(W_N) values are in the same central-charge convention
  as K(Vir) = 26 (Arakawa-compatible). The Fateev-Lukyanov convention,
  which gives a different numerical value for K_BP (AP268 polynomial-constant
  in both conventions), would rescale these values by the convention
  conversion factor; the closed-form cubic structure is
  convention-independent (the leading cubic coefficient 4 descends from
  6 * 2 = 12 of the per-spin uc-K-g formula).
- Verification path for varrho_A * K(A) at N >= 4: the modular-characteristic
  identity K^kappa(W_N) = K(W_N) * (H_N - 1) is now computable at every N;
  the prior B93 scope caveat "UNTESTED N >= 4" is superseded.

## Non-scope

- F1.b (varrho_BP = 1/6 structural origin) is NOT closed. Whether
  1/6 is a Hessian-determinant-of-DS-Lagrangian, a coset central-charge
  ratio, or a Berezinian shift remains open.
- The identity varrho_A * K(A) at N >= 4 is now computable (F1.c closed)
  but has not been numerically verified against first-principles kappa(W_N)
  + kappa(W_N^!) evaluations at N = 4, 5, 6; that verification is a
  follow-on task (not a frontier, just unrun arithmetic).

## Files touched

- `/Users/raeez/chiral-bar-cobar/CLAUDE.md` (two edits, lines 497 and 1370).

No other files modified.
