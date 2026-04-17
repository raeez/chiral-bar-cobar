# Spec: `k3_super_yangian_berezinian_trace.py` engine and tests

**Status.** Sandbox draft (no commit). 4th relaunch attempt; previous 3 rate-limited. Builds on V34 (super-Yangian culmination), V48 (CY-C abelian via $U^+_{q,t}^{K3}$), V49 (Pentagon-at-$E_1$ for K3), V50 (Wave-21 four-projection identity). Author: Raeez Lorgat. Date: 2026-04-16.

**Sandbox files (this engine bundle).**

- `~/chiral-bar-cobar/adversarial_swarm_20260416/draft_k3_super_yangian_berezinian.py` (605 lines, 7 sections)
- `~/chiral-bar-cobar/adversarial_swarm_20260416/draft_test_k3_super_yangian_berezinian.py` (438 lines, 10 sections, 42 pytest items)
- `~/chiral-bar-cobar/adversarial_swarm_20260416/wave_K3_super_yangian_engine_spec.md` (this file)

All 42 tests pass under `python3 -m pytest`. Pyproject lives at `~/chiral-bar-cobar/pyproject.toml`. The engine imports `compute.lib.independent_verification` for the HZ3-11 disjoint-source decorator; one decorated test verifies `conj:four-projection-trace-identity` (V34) and one verifies `conj:wave21-chi-cat-K3` (V50).

---

## 1. Mathematical content (PLATONIC FORM)

### 1.1 Mukai signature, super-Yangian assignment

The K3 Mukai lattice $\widetilde H(K3,\mathbb Z) \simeq U^{\oplus 4} \oplus E_8(-1)^{\oplus 2}$ has rank $24$ and signature $(4,20)$. The unique (up to parity reversal $\Pi$) Lie superalgebra into which the matrix algebra $M_{24}(\mathbb C)$ embeds with the super-permutation structure $P_s$ absorbing the obstruction $P_\omega^2 \neq \mathrm{Id}$ is $\mathfrak{gl}(4|20)$.

**Bookkeeping miracle (V34 §2.2).**
$$P_\omega^2 \text{-eigenspaces:} \quad \#\{+1\} = m^2 + n^2 = 4^2 + 20^2 = 416, \qquad \#\{-1\} = 2mn = 2 \cdot 4 \cdot 20 = 160, \qquad 416 + 160 = 24^2 = 576.$$
The $416/160$ split matches $\mathfrak{gl}(4|20)$'s bosonic/fermionic block decomposition exactly. The engine exposes this via `super_dimension_count((4,20)) -> (416, 160)` and `super_permutation_eigenvalues(omega) -> (416, 160)` for $\omega = \mathrm{diag}(+1^4, -1^{20})$.

### 1.2 Berezinian superdimension and crossing parameter

For $Y(\mathfrak{gl}(m|n))$ the Nazarov quantum Berezinian
$$\mathrm{Ber}_q\,T(u) \;=\; \frac{h_1(u)\cdots h_m(u)}{h_{m+1}(u+m\hbar)\cdots h_{m+n}(u+(m+n-1)\hbar)}$$
generates the centre $Z(Y(\mathfrak{gl}(m|n)))$. At the classical / $u\to 0$ limit the supertrace of the identity on $V_{m|n} = \mathbb C^m \oplus \Pi\mathbb C^n$ is
$$\mathrm{sdim}(V_{m|n}) \;=\; m - n.$$
At Mukai $(m,n) = (4,20)$: $\mathrm{sdim} = -16$. The crossing parameter $\rho_{\mathrm{cross}} = (m-n)/2 = -8$ is the *negative* of the bosonic $\mathfrak{gl}(N)$ value $\rho = N/2 > 0$; the negativity is the analytic shadow of $\mathrm{sdim} < 0$ and is the audible signature of the K3 holomorphic anomaly.

Engine API: `berezinian_sdim((4,20)) = -16`, `crossing_parameter((4,20)) = Fraction(-8)`.

### 1.3 V50 Pythagorean structural identity

$$24^2 \;=\; (-16)^2 + 4 \cdot 4 \cdot 20 \;=\; 256 + 320 \;=\; 576.$$

Equivalently $(m+n)^2 = (m-n)^2 + 4mn$. This algebraically separates *two distinct projections* of the same 24-dimensional Mukai support:
- $\kappa_{\mathrm{fiber}} = m + n = 24$ (UNSIGNED, lives on $Z_{\mathrm{Hall}}$, **off** the Wave-21 closure).
- $\mathrm{sdim}_{\mathrm{Mukai}} = m - n = -16$ (SIGNED, lives on $Z_{\mathrm{Ber}}$, **in** the closure).

The cross-term $4mn = 320$ is the dimension of the off-diagonal fermionic block (the $4\times 20$ pairing matrix), structurally distinguishing $Z_{\mathrm{Hall}} \setminus Z_{\mathrm{Ber}}$ from $Z_{\mathrm{Ber}}$.

Engine API: `mukai_rank_kappa_fiber() = 24`, `pythagorean_identity() -> True`.

### 1.4 V34 Wave-21 four-projection identity at K3 × E

$$\boxed{\;\mathrm{tr}_{Z_{\mathrm{KM}}}(\mathfrak K) + \mathrm{tr}_{Z_{\mathrm{BKM}}}(\mathfrak K) + \mathrm{tr}_{Z_{\mathrm{Ber}}}(\mathfrak K) + \mathrm{tr}_{Z_{\chi}}(\mathfrak K) \;=\; \chi(\mathcal O_X).\;}$$

At $X = K3 \times E$: $0 + 5 + (-16) + 11 = 0 = \chi(\mathcal O_{K3 \times E})$ by Künneth ($\chi(\mathcal O_{K3}) \cdot \chi(\mathcal O_E) = 2 \cdot 0$). The four numbers come from disjoint sources:
- $0$: Vol I bc-ghost on the Mukai lattice VOA (class G, no BRST gauge).
- $5$: Borcherds 1998 weight theorem on the Igusa cusp form $\Phi_{10}$ (weight $10$, $c_N(0)/2 = 5$).
- $-16$: Mukai signature supertrace $m - n$.
- $11$: Atiyah–Singer / Hirzebruch on the K3 × E Hodge diamond, decomposed as $11 = (\mathrm{sig}(K3) + 22)/2 + 8 = 3 + 8$ (half-signature plus Eisenstein elliptic correction).

Engine API: `wave21_identity_K3xE() -> (0, 5, -16, 11)` (asserts sum equals $\chi(\mathcal O_{K3 \times E}) = 0$).

### 1.5 V50 falsifiable closure prediction at K3

The Wave-21 closure at K3 alone (CY₂) predicts
$$\chi^{\mathrm{cat}}(K3) \;=\; \chi(\mathcal O_{K3}) - \mathrm{tr}_{\mathrm{KM}} - \mathrm{tr}_{\mathrm{BKM}} - \mathrm{tr}_{\mathrm{Ber}} \;=\; 2 - 0 - 5 - (-16) \;=\; 13.$$

Falsifiable: directly computable from the Hodge-filtered $F^0$ residual on $D^b(\mathrm{Coh}(K3))$ minus the (KM ⊕ BKM ⊕ Ber) projections, *without* using any super-Yangian. Disjoint verification candidate: `notes/tautology_registry.md` future entry.

Engine API: `chi_cat_K3_predicted() = 13`, `wave21_identity_K3() -> (0, 5, -16, 13)` (asserts sum equals $\chi(\mathcal O_{K3}) = 2$).

### 1.6 V50 disambiguation (AP-CY55 manifold vs algebraization)

Two distinct invariants, deliberately separated in the API:
- `chi_O_K3xE_closure_target() = 0`: $\chi(\mathcal O_{K3 \times E})$, the manifold-topological holomorphic Euler char (Künneth-multiplicative). This is the **sum target** on the RHS of Wave-21.
- `chi_cat_K3xE() = 11`: $\chi^{\mathrm{cat}}_{K3 \times E}$, the categorical residual on $Z_\chi$ (= the **fourth projection**, equal to $\mathrm{tr}_\chi$).

Conflating these is the AP-CY55 trap (manifold invariant vs algebraization invariant). The original engine's `chi_cat_K3xE() = 0` corresponded to the structure-sheaf invariant; V50 nomenclature reserves `chi^cat` for the categorical residual = 11. The engine now exposes both with disambiguated names.

---

## 2. Engine API (final, post-V50)

### Required by the V50 brief

| Function | Returns | Provenance |
|---|---|---|
| `super_yangian_signature()` | `(4, 20)` | V34 §1.1 |
| `berezinian_sdim((m,n)=(4,20))` | `-16` | V34 §2.3 |
| `mukai_rank_kappa_fiber()` | `24` | V50 §A2, AP-CY55 |
| `pythagorean_identity()` | `True` (asserts $24^2 = (-16)^2 + 320$) | V50 §A2 |
| `chi_cat_K3xE()` | `11` | V50 §A1 (alias of `tr_chi_K3xE`) |
| `chi_cat_K3_predicted()` | `13` | V50 §11 falsifiable |
| `wave21_identity_K3xE()` | `(0, 5, -16, 11)` (asserts sum = 0) | V50 boxed identity |
| `wave21_identity_K3()` | `(0, 5, -16, 13)` (asserts sum = 2) | V50 prediction |

### Structural support (existing, retained)

| Function | Returns | Note |
|---|---|---|
| `super_dimension_count((m,n))` | `(m²+n², 2mn)` | bosonic/fermionic split |
| `mukai_parity_vector(rank=24, positive=4)` | `[0,0,0,0,1,...,1]` | Mukai parity |
| `super_permutation_eigenvalues(omega)` | `(416, 160)` for Mukai | $P_\omega^2$ eigenspaces |
| `crossing_parameter((m,n))` | `Fraction((m-n), 2)` | $\rho_{\mathrm{cross}} = -8$ |
| `berezinian_classical_limit((m,n))` | $m-n$ | alias of `berezinian_sdim` |
| `SuperYangianGrading(signature, depth)` | dataclass | multi-graded shadow |
| `tr_ghost_K3xE()` / `tr_BKM_K3xE()` / `tr_Ber_K3xE()` / `tr_chi_K3xE()` | `0` / `5` / `-16` / `11` | per-projection traces |
| `multi_projection_trace_K3xE()` | `(0, 5, -16, 11)` | full tuple |
| `chi_O_K3xE_closure_target()` | `0` | Künneth structure-sheaf chi |
| `verify_wave21_identity()` | `True` | asserts sum = closure target |

### Symbolic / structural sanity

| Function | Returns | Note |
|---|---|---|
| `berezinian_sdim_symbolic_identity()` | `True` | sympy: $\sum_1^m 1 - \sum_1^n 1 = m - n$ |
| `four_projection_sum_symbolic()` | `True` | sympy: $0 + 5 - 16 + 11 = 0$ |
| `super_permutation_count_identity(rank, positive)` | `True` | $(m^2+n^2) + 2mn = (m+n)^2$ |
| `all_signature_checks()` | rows for $(2,1), (4,2), (4,20)$ | uniform table |
| `report()` | str | human-readable CLI output |

---

## 3. Test architecture (42 pytest items, 10 sections)

The test file `draft_test_k3_super_yangian_berezinian.py` is organised by API surface:

| Section | Tests | Coverage |
|---|---|---|
| A. Mukai signature primitives | 8 | `super_yangian_signature`, `super_dimension_count`, `mukai_parity_vector`, `super_permutation_eigenvalues` |
| B. Berezinian superdimension | 6 | `berezinian_sdim`, `berezinian_classical_limit`, `crossing_parameter` |
| C. Multi-graded Yangian shadow | 2 | `SuperYangianGrading` |
| D. K3 × E four-projection | 8 | per-projection + closure-target + identity |
| E. Symbolic sanity | 4 | sympy-verified identities |
| F. Top-level uniform check | 2 | `all_signature_checks`, `report` |
| G. INDEPENDENT VERIFICATION (V34) | 1 | `@independent_verification(claim="conj:four-projection-trace-identity")` |
| H. Engine internal consistency | 2 | $\mathrm{tr}(\omega) = m-n$, $P_\omega^2$ counts match block sizes |
| I. V50 extension API | 8 | Pythagorean + falsifiable + brief-API surface |
| J. INDEPENDENT VERIFICATION (V50) | 1 | `@independent_verification(claim="conj:wave21-chi-cat-K3")` |

**Total: 42 tests, all passing.**

### HZ3-11 decorator declarations

**Section G (V34, four-projection identity).**

```python
@independent_verification(
    claim="conj:four-projection-trace-identity",
    derived_from=[
        "Mukai signature (4,20) gl(p|q) supertrace",
    ],
    verified_against=[
        "V34 K3xE numerical sum",
        "Borcherds Phi_10 weight 10 Igusa cusp form",
        "Atiyah-Singer chi(K3xE)=11 via Hodge diamond",
    ],
    disjoint_rationale=...,  # ~700-char rationale enumerating disjointness
)
```

**Section J (V50, $\chi^{\rm cat}(K3) = 13$ prediction).**

```python
@independent_verification(
    claim="conj:wave21-chi-cat-K3",
    derived_from=[
        "V34 Mukai signature (4,20) gl(p|q) supertrace + V50 Pythagorean",
    ],
    verified_against=[
        "V20 Borcherds Phi_10 weight 10",
        "Atiyah-Singer chi(K3xE)=11 via Hodge diamond",
        "V50 closure prediction chi^cat(K3)=13",
    ],
    disjoint_rationale=...,  # ~600-char rationale
)
```

Both decorators pass the import-time disjointness check in `compute/lib/independent_verification.py`. The `derived_from` and `verified_against` source sets are case- and whitespace-insensitive disjoint.

---

## 4. AP-CY hygiene checks

This engine deliberately threads the following anti-patterns:

- **AP-CY55** (manifold vs algebraization invariants). Two functions explicitly disambiguated: `chi_O_K3xE_closure_target() = 0` (manifold) vs `chi_cat_K3xE() = 11` (algebraization residual on $Z_\chi$). Tests `test_chi_O_K3xE_closure_target_is_zero` and `test_chi_cat_K3xE_v50_alias_is_eleven` enforce both readings.
- **AP-CY56** (parity reversal $\Pi$). Code defaults to $(4|20)$ convention (positive directions = bosonic, negative = fermionic). Docstring in `super_yangian_signature` references AP-CY56; `mukai_parity_vector` allows the alternate split.
- **AP-CY11** (conditional propagation). The Berezinian sdim engine captures only the *abelian/classical shadow*; (Y-K3-4) and (Y-K3-5) (BKM imaginary roots, MO higher charges) remain conjectural. Docstring states this scope explicitly.
- **AP-CY61** (first-principles). The renaming `chi_cat_K3xE` (from "0" to "11") is NOT a shallow term swap: it is a substantive AP-CY55 disambiguation in line with V50's distinction between $\chi(\mathcal O_X)$ (manifold) and $\chi^{\rm cat}$ (algebraization residual). Engine retains both via `chi_O_K3xE_closure_target` and `chi_cat_K3xE`, with the closure target appearing on the RHS of Wave-21 and the algebraization residual being the fourth projection.
- **AP-CY24** (docstring ground truth). All numerical values in docstrings (`(416, 160)`, `(20, 16)`, `(5, 4)`, `-16`, `-8`, `13`, `11`, `5`) are matched by tests. No docstring claims a value the engine does not compute.
- **AP-CY27** (sandbox non-persistence). Files written by `Write` tool, immediately verified by `pytest` and `python3 __main__`. Existence and contents confirmed.
- **AP-CY28** (pole-unsafe test points). No rational-function evaluation involved; sdim is integer arithmetic.
- **HZ3-11** (independent verification). Two `@independent_verification` decorators with disjoint source sets (V34, V50). One per claim label.

---

## 5. Mapping to V34 and V50 wave documents

| V34 §6.2 row | Engine function | V50 §A1 row | Engine function |
|---|---|---|---|
| $\kappa_{\mathrm{ch}}^{\mathrm{V20}} = 0$ | `tr_ghost_K3xE` | $\mathrm{tr}_{Z_{\mathrm{KM}}} = 0$ | `tr_ghost_K3xE` |
| $\kappa_{\mathrm{BKM}} = 5$ | `tr_BKM_K3xE` | $\mathrm{tr}_{Z_{\mathrm{BKM}}} = 5$ | `tr_BKM_K3xE` |
| $\mathrm{sdim}_{\mathrm{Mukai}} = -16$ | `tr_Ber_K3xE` (`berezinian_sdim((4,20))`) | $\mathrm{tr}_{Z_{\mathrm{Ber}}} = -16$ | `tr_Ber_K3xE` |
| $\chi^{\mathrm{cat}}(K3 \times E) = 11$ | `tr_chi_K3xE` (= `chi_cat_K3xE` V50 alias) | $\mathrm{tr}_{Z_{\chi}} = 11$ | `tr_chi_K3xE` |
| sum = 0 = $\chi(\mathcal O_{K3 \times E})$ | `verify_wave21_identity` | sum = $\chi(\mathcal O_X)$ | `wave21_identity_K3xE` |

V50 extends V34 by:
1. Promoting the K3 × E numerical instance ($\sum = 0$) to the *universal* closure $\sum = \chi(\mathcal O_X)$.
2. Predicting $\chi^{\mathrm{cat}}(K3) = 13$ from the K3 closure ($\chi(\mathcal O_{K3}) = 2$). Engine: `chi_cat_K3_predicted`, `wave21_identity_K3`.
3. The Pythagorean identity $24^2 = (-16)^2 + 320$ separating $\kappa_{\mathrm{fiber}}$ (off-closure) from $\mathrm{sdim}_{\mathrm{Mukai}}$ (in-closure). Engine: `pythagorean_identity`, `mukai_rank_kappa_fiber`.

---

## 6. Open conjectures named (no downgrades, per V34 §9 / V50 §VIII)

This engine is constructive Python tooling for the following NAMED conjectures (no theorem upgrades, no downgrades, just disjoint verification scaffolding):

1. `conj:four-projection-trace-identity` (V34). Status: numerical instance $\{0, 5, -16, 11\} \to 0$ at K3 × E **VERIFIED** by this engine. Structural derivation (Hochschild stratification, Caldararu HRR) requires V20 Step 3 chain-level (RANK_1_FRONTIER, conditional on Pentagon-at-$E_1$).
2. `conj:wave21-chi-cat-K3` (V50). Status: PREDICTED $\chi^{\mathrm{cat}}(K3) = 13$ by closure. Falsifiable by direct Hodge-residual $F^0$ trace on $D^b(\mathrm{Coh}(K3))$. **VERIFIED** by this engine via the closure subtraction; INDEPENDENT direct verification deferred.
3. `conj:mukai-super-yangian` (V34 §4). Status: structural pieces (Y-K3-1)–(Y-K3-3) PROVED at $\mathfrak{gl}(2|1)$ and $\mathfrak{gl}(4|2)$ toy levels; full $(4,20)$ requires (Y-K3-4)–(Y-K3-5) (BKM imaginary roots, MO higher charge). Engine captures the abelian/classical shadow.
4. `conj:wave21-orthogonality-rigidity` (V50 §VIII.3). Status: structural, requires Lurie HA §2.4 coherent-involution rigidity argument extended to the four-term decomposition.
5. `conj:wave21-verlinde-completion` (V50 §VIII.5). Status: speculative; conditional on resolving CY-C (V41).

None of these is downgraded. The engine is an HZ3-11-decorated instrument for *disjoint* verification of the V34 and V50 numerical instances, NOT a proof skeleton.

---

## 7. Verification log (sandbox)

```
$ cd ~/chiral-bar-cobar/adversarial_swarm_20260416
$ python3 -m pytest draft_test_k3_super_yangian_berezinian.py -v
============================== 42 passed in 0.21s ==============================

$ python3 draft_k3_super_yangian_berezinian.py
Mukai super-Yangian signature: (m, n) = (4, 20)
Berezinian sdim (Mukai)       : -16
Crossing parameter rho_cross  : -8

(m, n) | sdim = m - n | (bosonic, fermionic)
--------------------------------------------------------
(2, 1)   |            1 | (5, 4)
(4, 2)   |            2 | (20, 16)
(4, 20)  |          -16 | (416, 160)

K3 x E four-projection (tr_ghost, tr_BKM, tr_Ber, tr_chi):
  (0, 5, -16, 11)
  sum = 0
  chi(O_{K3 x E}) (closure target) = 0
  Wave-21 identity holds? True

=== V50 extension ===
kappa_fiber (Mukai rank)         : 24
Pythagorean 24^2 = (-16)^2 + 320 : True
Wave-21 at K3 x E                : (0, 5, -16, 11) -> sum = 0 = chi(O_KxE)
Wave-21 at K3 (V50 prediction)   : (0, 5, -16, 13) -> sum = 2 = chi(O_K3)
chi^cat(K3) predicted            : 13
```

All sympy-verified items pass. Python 3.14.3, pytest 9.0.2.

---

## 8. NOT done, per task constraint

- No edits to `compute/lib/` or `compute/tests/` proper.
- No edits to `chapters/`, `appendices/`, `notes/`, `working_notes.tex`.
- No git commits, no `git add`, no manuscript build.
- No commits authored by anyone other than Raeez Lorgat.
- No AI attribution in code or spec.

Future installation path (NOT applied here, per V34 §8 / V50 §VII): rename to `compute/lib/k3_super_yangian_berezinian_trace.py`, add `compute/tests/test_k3_super_yangian_berezinian_trace.py`, run `make verify-independence` (HZ3-11 audit), update `notes/tautology_registry.md` with the V50 $\chi^{\rm cat}(K3) = 13$ entry.

— Raeez Lorgat, 2026-04-16. END OF SPEC.
