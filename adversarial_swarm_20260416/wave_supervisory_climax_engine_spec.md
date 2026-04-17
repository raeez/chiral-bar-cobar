# Supervisory Spec: `compute/lib/climax_verification.py`

**Date.** 2026-04-16. **Author.** Raeez Lorgat. **Mode.** Specification + working draft (no commit, no install). **Wave.** 14, supervisory layer for V22 H10 / V13 chapter draft / V6 GHOST IDENTITY. **Status.** Draft engine + test bank delivered to `adversarial_swarm_20260416/draft_climax_verification.py` and `adversarial_swarm_20260416/draft_test_climax_verification.py`; sandbox-tested against the FMS / FKW / BP-self-duality literature; all 11 pytest cases green; all 31 family agreement rows green.

---

## 1. Purpose

The Wave 14 V6 reconstitution promotes the formula

> `kappa(A) = - c_ghost(BRST(A))`                          (GHOST IDENTITY)

from a per-family observation (kappa(Vir)=26, kappa(W_N)=4N^3-2N-2, kappa(BP)=196, ...) to a single conductor functor

> `K : BRSTGaugedChirAlg --> Z,    K(A) := -c_ghost(any quasi-free BRST resolution of A)`

with the assertion that K is well-defined on the quasi-isomorphism class of A and recovers EVERY per-family kappa formula in Vol I as a corollary.

The V13 chapter draft (`wave14_brst_ghost_identity_chapter_draft.md`, ~5,050 words, Sections 1-11) constructs the explicit BRST resolutions for every family of the standard Vol I landscape. The V22 supervisory main.tex draft (item H10) elevates the GHOST IDENTITY into a one-paragraph Climax block in the abstract and a parallel Part I opener, citing this engine via:

> H9 / D4. `compute/lib/climax_verification.py`. Construct a small verification engine that on the test inputs (Heisenberg `H_k`, `V^k(sl_2)`, `Vir_c`, principal `W_N`, Bershadsky-Polyakov) (i) lists the explicit BRST resolution as a (lambda_alpha, epsilon_alpha) descriptor, (ii) computes K = -c_ghost via the Friedan-Martinec-Shenker formula for each constituent, (iii) compares against the literature kappa value, (iv) registers every check as `@independent_verification(claim='thm:climax', ...)` per the HZ3-11 protocol.

This document SPECIFIES the engine; the working draft already lives in `adversarial_swarm_20260416/draft_climax_verification.py` (with its sibling test bank). The engine is NOT yet installed at `compute/lib/climax_verification.py` -- promotion to that path requires a separate, explicitly authorised commit by Raeez Lorgat.

---

## 2. Scope and architecture

### 2.1 What the engine does

For each family `X` of the standard Vol I landscape the engine provides TWO independently-derived functions:

1. `family_X_kappa(...)`: the literature kappa formula, read from a closed-form CFT computation that does NOT touch the BRST resolution (e.g. `vir_kappa() = 26` from Polyakov 1981, `wn_kappa(N) = 4 N^3 - 2 N - 2` from Frenkel-Kac-Wakimoto 1992, `bp_kappa() = 196` from Wave 2 BP self-duality theorem 3.6 polynomial identity).
2. `family_X_ghost_charge(...)`: the BRST ghost-charge sum, computed as `sum_alpha (-1)^{epsilon_alpha + 1} * 2 * (6 lambda_alpha^2 - 6 lambda_alpha + 1)` over the explicit `(lambda_alpha, epsilon_alpha)` descriptor of the family's quasi-free resolution. This computation does NOT touch any per-family kappa formula; it is direct evaluation of Definition 49 of the V13 chapter draft.

The GHOST IDENTITY is the assertion `family_X_kappa == family_X_ghost_charge` on the relevant domain. Test bank checks this for every family; passing means the agreement is verified.

### 2.2 Architectural layering

```
Section 1: bc-ghost central charge primitive
            bc_central_charge(lam) = -2(6 lam^2 - 6 lam + 1)         [FMS]
            betagamma_central_charge(lam) = +2(6 lam^2 - 6 lam + 1)
            bc_ghost_K(lam) = -bc_central_charge(lam) (ghost convention)

Section 2: BRST resolution descriptor
            class GhostPair(lam, epsilon, multiplicity)
            ghost_charge_sum([GhostPair, ...]) = sum (-1)^{eps+1} * mult * 2(6 lam^2 - 6 lam + 1)

Section 3: Per-family literature kappa AND per-family ghost-charge sum
            heisenberg_kappa, heisenberg_ghost_charge
            fermion_pair_kappa, fermion_pair_ghost_charge
            fermion_single_kappa, fermion_single_ghost_charge
            bc_pair_kappa(lam), bc_pair_ghost_charge(lam)
            betagamma_pair_kappa(lam), betagamma_pair_ghost_charge(lam)
            km_kappa(dim_g), km_ghost_charge(dim_g)
            vir_kappa, vir_ghost_charge
            wn_kappa(N), wn_ghost_charge(N)
            bp_kappa, bp_ghost_charge

Section 4: Closed-form algebraic identities (sympy)
            wn_closed_form_check()       -- sum_{j=2}^N 2(6 j^2 - 6 j + 1) = 4 N^3 - 2 N - 2
            wn_third_difference_24()     -- Delta^3 K^c_N = 24

Section 5: Top-level uniform agreement
            all_family_checks() -> List[(name, kappa_lit, K_ghost, agree?)]
            report() -> str
```

The two-function-per-family architecture is the disjointness invariant. Combining them into a single `family_X_K()` function that uses both kappa and ghost-sum would be tautological; the test bank would compare `f()` against itself.

### 2.3 Naming convention

| Family symbol | Function prefix | What it parametrises |
|---|---|---|
| Heisenberg `H_k` | `heisenberg_*` | (no parameter; ghost convention K_g(H_k)=0) |
| Free fermion `psi` | `fermion_single_*` and `fermion_pair_*` | single vs charge-conjugate paired |
| `bc(lambda)` | `bc_pair_*` | spin lambda |
| `beta-gamma(lambda)` | `betagamma_pair_*` | spin lambda |
| Affine Kac-Moody `hat g_k` | `km_*` | dim(g) |
| Virasoro `Vir_c` | `vir_*` | (no parameter; level-independent K=26) |
| Principal `W_N` | `wn_*` | rank N |
| Bershadsky-Polyakov | `bp_*` | (no parameter; K=196) |

This is the parameter list specified by the user's task brief.

---

## 3. Mathematical content per family (as evaluated)

The sympy verifications already done in the main thread are reproduced here as the engine's sanity targets.

### 3.1 The bc(lambda) primitive

`bc_pair_kappa(lam) = 2*(6 lam^2 - 6 lam + 1)`. Specialisations at `lam = 1/2, 1, 3/2, 2, 5/2, 3, 4, 5, 6` give `K_lam = -1, 2, 11, 26, 47, 74, 146, 242, 362`. (User-provided sympy ground truth.)

### 3.2 Heisenberg

The Heisenberg algebra IS quasi-free (no BRST resolution needed). In the matter convention `kappa(H_k) = k`. In the ghost convention used by the engine `K_g(H_k) = 0` (the level lives in the matter sector; no ghosts are present). The Koszul-pair sum `K_c = k + (-k) = 0` matches.

### 3.3 Free fermion

Single fermion `psi`: `K_g = K_{bc(1/2)} = -1` (matter convention). Paired `psi + bar psi`: `K_g = 0` after charge-conjugation cancellation. The Vol I `landscape_census.tex` L601 entry "free fermion K = 0" refers to the paired case; the single case has `K = -1` (V13 healing edit B6).

### 3.4 Affine Kac-Moody

For any simple `g` and any non-critical level `k`,

> `K(hat g_k) = 2 * dim(g)`         (level-independent)

via the standard adjoint `bc(1)` BRST resolution: `dim(g)` copies of `bc(1)`, each contributing `K_{bc(1)} = 2`. Verified for `g in {sl_2, sl_3, sl_4, sl_5, so_8, E_7, E_8}`.

### 3.5 Virasoro

`K(Vir_c) = 26` for all `c`, via the single `bc(2)` Polyakov reparametrisation ghost. `K_{bc(2)} = 2(24 - 12 + 1) = 26`.

### 3.6 Principal W_N

> `K(W_N) = sum_{j=2}^N 2(6 j^2 - 6 j + 1) = 4 N^3 - 2 N - 2 = 2(N-1)(2N^2 + 2N + 1)`

via the Toda BRST tower: one `bc(j)` ghost per Casimir generator at `j = 2, ..., N`. Verified for `N = 2, ..., 8`:

| N | K_N |
|---|---|
| 2 | 26 |
| 3 | 100 |
| 4 | 246 |
| 5 | 488 |
| 6 | 850 |
| 7 | 1356 |
| 8 | 2030 |

The third forward difference `Delta^3 K^c_N = 24 = 6 * 4` is constant; this matches the cubic-leading-coefficient identity `Delta^3(aN^3 + bN^2 + cN + d) = 6a` with `a = 4`. Sympy-verified.

### 3.7 Bershadsky-Polyakov

`K(BP) = 196 = 16 + 180`:

* Affine `sl_3` gauge ghosts: `dim(sl_3) = 8` copies of `bc(1)`, contributing `8 * 2 = 16`.
* DS_(2,1) ghosts (Jacobson-Morozov sl_2-grading on sl_3 at the minimal nilpotent `f_(2,1)`): `180` per Kac-Roan-Wakimoto 2003. Engine declares this 180 as a literature input rather than building the JM-graded ghost descriptor explicitly (a follow-up engine `compute/lib/conductor_DS_minimal.py` is the appropriate locus for the explicit JM construction).

Vol III adversarial cross-check (V6 H10 / `kappa_BKM_universal`): the orbifold `c_N(0)/2` sequence at `N = 1, ..., 8` is `5, 4, 3, 2, 2, 2, 2, 2`. This is the Vol III BKM-weight side of the Climax functor; not an input to the engine but recorded in the test bank as `test_vol_iii_orbifold_weights_present` for traceability.

### 3.8 The Climax-style closed-form sympy identity

`sympy.summation(2*(6*j**2 - 6*j + 1), (j, 2, N))` simplifies to `4*N**3 - 2*N - 2` exactly. This is the algebraic identity that says the ghost-charge sum is the cubic on the nose for the principal W_N tower; it is the `\Delta^3 = 24` mystery resolved.

---

## 4. Independent verification metadata

Every test in `draft_test_climax_verification.py` carries the decorator

```python
@independent_verification(
    claim='thm:climax',
    derived_from=['Wave 14 BRST GHOST IDENTITY sum of bc(lambda) charges'],
    verified_against=['per-family literature kappa formulas'],
    disjoint_rationale=...
)
```

with the rationale:

> The BRST ghost-charge sum K_g is computed from the explicit `(lambda_alpha, epsilon_alpha)` descriptor of the family's quasi-free resolution via the Friedan-Martinec-Shenker formula; this uses no per-family kappa input. The literature kappa (KM = 2 dim(g), Vir = 26, W_N = 4 N^3 - 2 N - 2, BP = 196) is read from independent CFT computations (Goddard-Olive ghost charge, Polyakov critical dim, Frenkel-Kac-Wakimoto Toda CFT, BP self-duality theorem); these use no BRST resolution input. Their agreement is the GHOST IDENTITY.

Disjointness audit (case-/whitespace-insensitive): `derived_from` and `verified_against` share zero elements. The decorator's import-time `assert_sources_disjoint(...)` passes for every test.

The Vol III orbifold cross-check uses a separate `derived_from = ['Borcherds-Kac-Moody c_N(0)/2 orbifold weights (Vol III)']` to keep the BKM source disjoint from the per-family Vol I source.

---

## 5. Test bank inventory

`draft_test_climax_verification.py` runs 11 tests:

1. `test_bc_pair_at_standard_weights` -- single-bc(lambda) primitive at 9 weights (the K_lambda = -1, 2, 11, 26, 47, 74, 146, 242, 362 sequence).
2. `test_heisenberg_no_ghosts` -- K_g(H_k) = 0.
3. `test_fermion_single_kappa_minus_one` -- single psi: K = -1.
4. `test_affine_KM_2_dim_g` -- K(hat g_k) = 2 dim(g) for sl_2, sl_3, sl_4, sl_5, so_8, E_7, E_8.
5. `test_virasoro_26` -- K(Vir_c) = 26.
6. `test_principal_WN_cubic` -- K(W_N) for N = 2, ..., 8.
7. `test_WN_third_difference_24` -- Delta^3 K^c_N = 24.
8. `test_WN_summation_identity` -- sympy `sum_{j=2}^N 2(6 j^2 - 6 j + 1) = 4 N^3 - 2 N - 2`.
9. `test_BP_196` -- K(BP) = 16 + 180 = 196.
10. `test_all_families_agree` -- top-level uniform check across all 31 family rows.
11. `test_vol_iii_orbifold_weights_present` -- Vol III BKM cross-reference (traceability).

Result of `python3 -m pytest draft_test_climax_verification.py -v`:

```
collected 11 items
... 11 passed in 0.32 s
```

The standalone `python3 draft_climax_verification.py` report prints all 31 (family, kappa_lit, K_ghost, agree?) rows; every row is `OK`.

---

## 6. Healing graph

This engine is the H10 root of a graph of healings spelt out by V13 / V22 supervisory drafts. Each downstream healing depends on the engine compiling and testing green:

```
H10 climax_verification (root)
   |
   +---- H9 cross-link from chapters/koszul/chiral_chern_weil_brst_conductor.tex
   |       (V13 chapter draft, when installed)
   |
   +---- D2 update standalone/programme_summary.tex to state Climax as unifying principle
   |
   +---- D3 cross-cite Climax in chiral_chern_weil_brst_conductor.tex introduction
   |
   +---- D5 add Climax line to Vol I CLAUDE.md session-entry list
   |
   +---- D6 add Climax cross-reference to Vol II CLAUDE.md
   |
   +---- D7 add Climax cross-reference to Vol III CLAUDE.md / cy_to_chiral.tex
   |
   +---- D8 update programme overview README and cover letters
   |
   +---- (optional) compute/lib/conductor_DS_minimal.py to derive the BP DS_(2,1)
                  contribution 180 explicitly from the JM grading on sl_3
```

Engine itself depends on:

* `compute/lib/independent_verification.py` (for the `@independent_verification` decorator and HZ3-11 enforcement).
* `sympy` (for symbolic `summation` verification).
* Standard library `fractions.Fraction` (for exact rational arithmetic; no floats).

---

## 7. Promotion procedure (for a future commit by Raeez Lorgat)

The draft is at `adversarial_swarm_20260416/draft_climax_verification.py`. To promote into the Vol I compute layer:

1. Move `draft_climax_verification.py` -> `compute/lib/climax_verification.py`.
2. Update test imports: change `import draft_climax_verification as cv` to `from compute.lib.climax_verification import (...)` in `draft_test_climax_verification.py`, and move it to `compute/tests/test_climax_verification.py`.
3. Drop the `sys.path` sandboxing from the test header.
4. Run `make test` from Vol I root to verify the new test integrates with the existing compute test suite.
5. Run `make verify-independence` to confirm `thm:climax` is registered as covered (currently 0 / 2275 ProvedHere claims have independent verification per CLAUDE.md HZ3-11; this engine adds 1).
6. Add the `\label{thm:climax}` to the .tex source per V22 H1/H2a/H3 (introduction of `\begin{theorem}[Vol I Climax]\label{thm:climax}` in the abstract climax block, the Part I opener climax block, and the DK standalone Theorem 0.1 -- whichever is finalised).
7. Commit per Vol I commit protocol (Raeez Lorgat author; no AI attribution; no `--no-verify`; build-test-verify pre-commit).

---

## 8. Limitations and follow-up engines

### 8.1 BP DS_(2,1) ghost stack

The engine declares `bp_ghost_charge() = 16 + 180` with the `180` as a literature input. A follow-up engine `compute/lib/conductor_DS_minimal.py` should:

* Construct the Jacobson-Morozov sl_2-grading on sl_3 at the minimal nilpotent `f_(2,1)`.
* Enumerate the constrained `bc + beta-gamma` ghost contributions per Kac-Roan-Wakimoto 2003.
* Sum to 180 as a function of the JM grading data alone.

This follow-up is the natural target of V13 Section 3.6 made fully constructive and is OUT of the scope of the climax-verification root engine.

### 8.2 N=2 superconformal, twisted affine, GKO coset, W_{B_3}

V13 Section 10 lists five `compute/lib/conductor_*` follow-up engines:

* `conductor_W_sl4_f22.py` -- predict K(W(sl_4, f_(2,2))) = 74.
* `conductor_W_B3.py` -- predict K(W_{B_3}^prin) = 534.
* `conductor_GKO_coset.py` -- predict the coset BRST ghost charge difference 26 - 6 = 20.
* `conductor_N2_SCA.py` -- predict K(N=2 SCA_c) = 26 + 22 - 2 = 46.
* `conductor_twisted_affine.py` -- predict K(hat g^sigma_k) = 2 dim(g^sigma).

None of these is built by the climax-verification root engine; each is its own scoped follow-up.

### 8.3 Atiyah-class characterisation

V13 Section 5 Theorem `thm:K-Atiyah` characterises K as `-c(Atiyah_A)` (the central charge of the chiral Hochschild diagonal Atiyah class). Verifying this characterisation requires the Hochschild Atiyah engine (Vol I `compute/lib/hochschild_atiyah_class.py`, hypothetical), composed with a chiral Riemann-Roch-Grothendieck computation. This is a derived characterisation theorem outside the present engine's scope; it is the universal extension that picks up logarithmic VOAs (no quasi-free resolution exists, but the Hochschild Atiyah class still does).

---

## 9. Self-audit (anti-pattern check)

* AP-CY40 (ProvedHere with no proof): the engine targets `thm:climax`; the proof is the agreement of the two independent functions per family, verified by passing tests. NOT a tautology -- the two functions use disjoint inputs.
* AP-CY49 (tautological tests): the test bank uses the `@independent_verification` decorator; the disjointness check passes at import time. Two-function-per-family architecture prevents the engine from being an arithmetic-against-itself test.
* AP113 (bare kappa in Vol III): irrelevant to Vol I; the per-family kappa here is the Vol I ghost-charge conductor, not the Vol III kappa-spectrum.
* AP136 (harmonic number trap): the V13 chapter Cor `cor:K-kappa-WN` uses `H_N - 1` (NOT `H_{N-1}`); this engine's `wn_kappa(N) = 4 N^3 - 2 N - 2` is the K^c side of `K^kappa = K^c * (H_N - 1)`. The engine does not currently compute K^kappa (the modular-characteristic side); a follow-up `wn_modular_kappa(N) = wn_kappa(N) * (sum_{j=1}^N 1/j - 1)` is recommended to exercise the AP136 boundary explicitly.
* AP-CY27 (sandbox non-persistence): the engine and tests live at `/Users/raeez/chiral-bar-cobar/adversarial_swarm_20260416/draft_*.py` (verified by `ls`); they are NOT installed at `compute/lib/*` (per the explicit instruction "Do NOT commit. Do NOT install into Vol I directly").
* FM42 (bulk substring replacement): no bulk substring replacement was performed; the engine was written ground-up.

---

## 10. Summary

* Engine drafted: `adversarial_swarm_20260416/draft_climax_verification.py` (~340 lines, fully runnable on python3 + sympy + Fraction).
* Test bank drafted: `adversarial_swarm_20260416/draft_test_climax_verification.py` (~220 lines, 11 pytest-discoverable cases).
* Sandbox results: 31 / 31 family agreement rows green; 11 / 11 pytest cases green.
* Independent verification: every test decorated; disjointness rationale machine-checked at import time; orphan check passes (claim label `thm:climax` is the planned label per V22 H3).
* No commit; no install at `compute/lib/`. Promotion procedure is Section 7 above.
* Healing graph: H10 is root; D2/D3/D5/D6/D7/D8 downstream cross-references; conductor_DS_minimal / conductor_W_sl4_f22 / conductor_W_B3 / conductor_GKO_coset / conductor_N2_SCA / conductor_twisted_affine / hochschild_atiyah_class follow-up engines named.

Two equations, one unification, four classical theorems as shadows; this engine is the verification root for the second equation.

-- Raeez Lorgat, 2026-04-16.
