# Wave 2 — Bershadsky--Polyakov self-duality (`bp_self_duality.tex`)

**Adversarial referee report.** Date: 2026-04-16. Target: `~/chiral-bar-cobar/standalone/bp_self_duality.tex` (668 lines), with cross-references into `five_theorems_modular_koszul.tex` (L2532--2554, L2260--2266) and `koszulness_fourteen_characterizations.tex` (L1290--1316).

The wave-1 alarm was that the value `kappa(BP_{-3}) = 49/3` is asserted at the fixed point of the Feigin--Frenkel involution `k -> -k-6`, which **coincides with the critical level** `k=-h^v=-3`, where `c(BP_k)` has a simple pole. The alarm is correct, the value 49/3 is **not** the limit of `kappa(BP_k)` as `k -> -3`, and the manuscript itself acknowledges this in `bp_self_duality.tex` Prop. 4.7 (L598--619). The cross-volume cross-reference text (`five_theorems_modular_koszul.tex` L2551--2552) **does not** acknowledge it and is the active misclaim. Below: verdict, ghost theorem, AP audit, three concrete upgrade paths, and a punch list.

---

## Section 1. Verdict on the `BP_{-3}` value

**The value `kappa(BP_{-3}) = 49/3` is wrong as a value of `kappa` at a real level. It is a formal symmetric mean.** Numerical verification:

```
c(k) = 2 - 24(k+1)^2/(k+3)
c(-3 + 1/1000)  ~  -95902.024
c(-3 - 1/1000)  ~  +96098.024
c(-3 + 1/100)   ~  -9502.24
c(-3 - 1/100)   ~  +9698.24
```

`c(k)` does not have a removable singularity at `k=-3`: the residue of the simple pole is `lim_{k->-3} (k+3) * c(k) = -24 * (-2)^2 = -96`, with a constant offset (the `2`) and a regular-on-the-other-side asymptotic from the `(k+1)^2` numerator. Concretely `c(k) = -24(k+1)^2/(k+3) + 2`, and at `k = -3 + eps` we have `(k+1)^2 = (-2+eps)^2 = 4 - 4eps + eps^2`, so `c = -24(4 - 4eps + ...)/eps + 2 = -96/eps + 96 - 24 eps + 2 = -96/eps + 98 + O(eps)`. Symmetrically at `k = -3 - eps` we get `+96/eps + 98 + O(eps)`.

Two consequences:

1. The **divergent** parts cancel under the involution. The constant residue (`98`) is the **finite remainder of the symmetric average** `(c(k) + c(-k-6))/2 = K/2 = 98`, and is *visible from either side* of `k=-3`.
2. The **value** of `c(-3)` itself, or `kappa(-3) = c(-3)/6`, is genuinely undefined: a left-sided limit is `+infty`, a right-sided limit is `-infty`. The "self-dual value" `c=98` is **not** `c(-3)`; it is `lim_{eps->0} (c(-3+eps) + c(-3-eps))/2 = 98` (the principal value), or equivalently the *value of `c+c'` divided by 2*.

`bp_self_duality.tex` itself explicitly states this in Prop. 4.7 (L598--619): "The roots `k = -3 +/- 2i` are complex" and "the formal self-dual point `k = k' = -3` is the critical level, where the DS reduction degenerates." So *that* file is technically self-consistent. The alarm is real for two derived statements:

- **`five_theorems_modular_koszul.tex` L2551--2552**: "The self-dual level is `k = -3`, at which `kappa(BP_{-3}) = 49/3`." This **drops the warning** and presents `49/3` as a value, not a principal-value mean. **Wrong as written.**
- **`koszulness_fourteen_characterizations.tex` L1315--1316**: "The self-dual level is `k = -3`, at which `kappa = 49/3`." **Same error.**

So: the wave-1 finding propagates into both cross-reference files, but the standalone `bp_self_duality.tex` is correct on this specific point (with caveats below).

---

## Section 2. First-principles investigation

### What the claim gets RIGHT (the ghost theorem)

There is a **real, level-independent, polynomial identity** lurking here. Symbolic computation confirms (Section 1 of the original `bp_koszul_conductor_engine.py`):

> **Theorem (BP central-charge conductor).** With `c(k) = 2 - 24(k+1)^2/(k+3)` and the involution `k' = -k-6`,
>     `c(k) + c(k') = 196` *as a polynomial identity in `k`*, valid for all `k != -3` (where both sides are finite).

This is **stronger than a value at a single point**: it is a *globally constant* function on the moduli line minus `{-3}`. The verification:
```
c(k) + c(-k-6)
  = [2 - 24(k+1)^2/(k+3)] + [2 - 24(-k-5)^2/(-k-3)]
  = 4 - 24(k+1)^2/(k+3) + 24(k+5)^2/(k+3)
  = 4 + 24[(k+5)^2 - (k+1)^2]/(k+3)
  = 4 + 24*(8k+24)/(k+3)
  = 4 + 192*(k+3)/(k+3)
  = 196.
```

This is a **theorem at every regular level**, not at the fixed point. It is the *ghost* whose narration as "value at `k=-3`" is the error. The ghost theorem extends naturally:

> **Conjecture (hook-type uniform conductor).** For every odd `N = 2m+1` and self-transpose hook partition `lambda = (m+1, 1^m)`, the central-charge conductor `K_lambda = c(W_k(sl_N, f_lambda)) + c(W_{-k-2N}(sl_N, f_lambda))` is a level-independent constant.

`bp_self_duality.tex` Thm 4.4 (L485--503) attempts this but **mis-states the involution** as `k' = -k - N` instead of `k' = -k - 2h^v = -k - 2N` (Warning 4.5, L505--511, *acknowledges* the error in the proof but doesn't fix the theorem statement). See AP audit below.

### What the claim gets WRONG (precise conflation)

Three layered conflations:

**(A) Conflation of "value at fixed point" with "principal-value mean across pole".**
`kappa(BP_{-3}) = 49/3` reads as a function value. It is in fact `(K/2)/6 = 196/12 = 49/3` (or `K_kappa/2 = (98/3)/2 = 49/3`), which is the principal value `lim_{eps->0+} (kappa(-3+eps) + kappa(-3-eps))/2`. Both sides individually diverge; only the symmetric sum is finite, with mean `49/3`.

**(B) Conflation of "self-dual point of the involution" with "Koszul self-dual point of the algebra".**
The involution `k -> -k-6` has a unique fixed point at `k = -3`. But the *Koszul self-dual* condition `c(k) = c(-k-6)`, i.e., the algebra is Koszul-isomorphic to its own dual, has solutions where `c = K/2 = 98` — and Prop. 4.7 correctly observes that *no real `k` satisfies this*: the equation `c(k) = 98` has only complex roots `k = -3 +/- 2i`. The *involution-fixed point* and the *charge-fixed point* genuinely disagree, and `k = -3` is not a Koszul self-dual point in the algebra-as-VOA sense — it's the critical level.

**(C) Conflation of "BP at critical level" with "a VOA".**
At `k = -h^v = -3`, the affine Sugawara term diverges; `V_{-3}(sl_3)` admits the *Feigin--Frenkel center* (commutative VOA with no stress tensor on the algebra of singular vectors). DS reduction at the critical level gives a degenerate limit: the Bershadsky--Polyakov VOA at `k=-3` is **not** an ordinary VOA — it is a degenerate object (commutative chiral algebra with the Feigin--Frenkel center as the "center"), and `c` is genuinely meaningless. (This is the same phenomenon that makes the geometric Langlands programme *interesting* at the critical level for the principal `W`-algebra.)

### The CORRECT statement

Replacing the wrong narration with the right theorem:

> **Theorem (BP charge conductor, corrected).** Let `c_BP(k) = 2 - 24(k+1)^2/(k+3)`. The Feigin--Frenkel involution `k -> -k - 6` (where `2h^v(sl_3) = 6`) descends from `V_k(sl_3)` to `BP_k = W_k(sl_3, f_{(2,1)})` for every `k != -3`. The map `k -> -k-6` has a unique fixed point at `k=-3`, which **coincides with the critical level** `k = -h^v(sl_3) = -3`. At every regular level the **charge conductor** `K_central(BP) := c_BP(k) + c_BP(-k-6) = 196` is a polynomial identity (level-independent constant). At the critical level `k=-3`, the BP VOA degenerates; `c` is undefined (simple pole), and the formal symmetric mean `(c(k)+c(-k-6))/2 = 98` is the principal-value of `c` across the pole. **No real level realises a self-dual value `c = K/2 = 98`**: the equation `c(k) = 98` has only complex solutions `k = -3 +/- 2i`.

> **Corollary.** The "self-dual point at `k=-3`" is the *critical level*, not a finite-charge point. The conjectured Koszul self-duality of `BP_k` at `k != -3` is a duality between *distinct VOAs at distinct levels*, joined by an involution with a degenerate fixed point. There is no honest "self-dual VOA" at finite real `k`.

This is *stronger than the original* claim: it says the universal sum is constant 196, valid at every regular level, gives a clean conceptual reason why the fixed point is degenerate, and identifies the critical level as the unavoidable obstruction to a finite self-dual point.

---

## Section 3. AP audit of `bp_self_duality.tex`

### AP8: "self-dual" qualified?

**AP8** (CLAUDE.md L703): "NEVER 'self-dual' unqualified. Specify which duality, which c. Virasoro self-dual at c=13."

- **Title** (L56--57): "Bershadsky--Polyakov Koszul self-duality". *Qualified* by "Koszul" in the title — OK.
- **Abstract** (L68--84): says "Koszul self-dual under the hook-transpose involution" and gives `c(k) + c(k') = 196`. *Qualified* — OK.
- **L72--74**: Adds "for `k != -3` (away from the critical level)" — this is the key wave-1 fix; PRESENT in the standalone, MISSING in cross-reference files.
- **Prop 4.7** (L598--607): Title "BP self-dual point" — does *not* specify "Koszul". The body explicitly notes the singularity, but the heading is bare. **Mild violation.**

Verdict: **Mostly compliant**, with one improvable heading.

### AP39: kappa formula family-specificity

**AP39** (L933): "kappa != S_2 for non-Virasoro. Coincide only rank-1. Lookup: Heis_k: kappa=k (NOT k/2). Vir_c: kappa=c/2 (ONLY family where kappa=S_2/2). KM: kappa=dim(g)(k+h^v)/(2h^v)."

- **`bp_self_duality.tex` Eq. 3.5 anomaly ratio** (L322--329): claims `rho_B = 1/1 - 2/(3/2) - 2/(3/2) + 1/2 = 1 - 4/3 - 4/3 + 1/2 = 1/6`.
   **Direct arithmetic: `1 - 4/3 - 4/3 + 1/2 = 6/6 - 8/6 - 8/6 + 3/6 = -7/6`, NOT `1/6`.** This is a hard arithmetic error. The claimed answer `1/6` matches `kappa = c/6` (used elsewhere in the file and across `koszulness_fourteen_characterizations.tex` and `five_theorems_modular_koszul.tex`), but the *derivation* presented does not give it. **Critical violation.**
- **L389--394**: `kappa = c/2` is used on the `T`-line in the proof of Thm 3.6, claiming this is the "Virasoro self-OPE". This is consistent with AP39 (Vir line gets c/2), but **inconsistent with the rest of the file** which states `kappa(BP_k) = c/6` (used implicitly in the conductor narration) and with `five_theorems_modular_koszul.tex` L2542 which states `kappa(BP_k) = c/6`. **Internal contradiction within the standalone:** Prop. 3.5 (L331--345) writes `kappa_T(k) + kappa_T(k') = c(k)/2 + c(k')/2 = K/2 = 98`, which is `kappa = c/2`; but the abstract and Eq. 3.5 use `rho = 1/6` implying `kappa = c/6`. Both formulas appear in the *same paper*; the standalone file has not internally chosen one. **Critical violation.**
- **`koszulness_fourteen_characterizations.tex` L1298**: states `c = (k-1)(6k+1)/(k+3)` for BP. **This is a wholly different formula** from the FKR formula `c = 2 - 24(k+1)^2/(k+3)` used in `bp_self_duality.tex`. At `k = -3/2`: FKR gives `c = -2` (matches triplet), the koszulness_14 formula gives `c = 40/3`. The koszulness_14 formula is **wrong** (not the BP central charge in any standard convention I can locate).

So we have **two distinct AP39 violations**:
1. Two different `kappa` prefactors (`c/2` vs `c/6`) used in the same standalone, with the published anomaly-ratio derivation giving neither.
2. Two different `c(k)` formulas used in different standalone papers under the same author.

Note: the alternative formula `c = (k-1)(6k+1)/(k+3)` can be excluded by the simplest admissible-level test (`k = -3/2` should give `c = -2`, the triplet value).

### AP136: harmonic-number trap

The `W_N` formula in `five_theorems_modular_koszul.tex` L2512 reads `kappa(W_N) = c (H_N - 1)`. At `N=3`: `H_3 - 1 = 1/2 + 1/3 = 5/6`, `kappa(W_3) = 5c/6` (L2520). This is **correct**. Conductor for `W_3`: from the L2247 table, `K(W_3) = 250/3`. Sanity check: the central-charge conductor for principal `W_3` from `KRW` is `c + c' = 2 * dim(sl_3) * (something)`. Not directly verified here, but the *form* `K_kappa(W_3) = (5/6) * K_central(W_3)` would give a clean cross-check.

### Other issues caught by audit

- **Warning 4.5 (L505--511)** is itself a recovered AP. The proof of Thm 4.4 writes `k' = -k - N` then immediately a parenthetical "but `h^v(sl_N) = N`, so `k' = -k - 2N`". The **theorem statement still reads `k' = -k - N`**, which is wrong. The narrator catches the error mid-proof but **never patches the theorem statement**. The theorem as displayed is internally inconsistent.
- **Eq. 3.4 (L260--268)** computation is correct, BUT the appeal to "Fehily--Kawasetsu--Ridout convention" (L271 onward) inside Warning 3.7 reveals there are *two* central-charge formulas in the compute layer (`c1 = 2 - 24(k+1)^2/(k+3)` vs `c2 = 2 - 3(2k+3)^2/(k+3)`). At `k=-3/2`: `c1 = -2` ✓ (matches triplet), `c2 = +2` ✗ (wrong sign). The warning correctly identifies `c1` as authoritative, but the discussion of "different formulas" is misleading — `c2` is *wrong*, not just a "different convention". The compute module's `K=76` is a consequence of using `c2`, which is incorrect.

---

## Section 4. Three concrete upgrade paths

### Upgrade path 1 (strongest): "Charge conductor as a polynomial identity"

Replace the soft narration "the Koszul conductor is `K = 196`" with the hard polynomial statement:

> **Theorem (BP charge conductor, polynomial form).** As elements of the rational function field `Q(k)`,
> `c_BP(k) + c_BP(-k-6) = 196`.
> Equivalently, `c_BP(k) - 98` is an *odd* function of `(k+3)` under the involution `k -> -k-6`.

The *odd-function* reformulation is the conceptual content: it says `c(k) - K/2` transforms as `phi(eps) -> -phi(-eps)` where `eps = k+3`, so the principal value at `eps=0` is exactly `K/2`. This is much sharper than the bare `c+c'=196`.

This is `Annals`-grade if combined with:

> **Conjecture (hook-uniform conductor).** For every odd `N = 2m+1` and self-transpose hook `lambda = (m+1, 1^m)`, the conductor `K_lambda := c(W_k(sl_N, f_lambda)) + c(W_{-k-2N}(sl_N, f_lambda))` is in `Q(k) ∩ Q = Q` (level-independent), and `c(W_k) - K_lambda/2` is an odd function of `k + h^v(sl_N) = k + N`.

This converts the "self-dual point at `k=-3`" claim into a *structural symmetry* of the *whole moduli line*, with the critical level appearing as the unique fixed point where the symmetry forces a divergence. No retraction; *strict generalisation*.

### Upgrade path 2: "BP self-duality as a derived equivalence"

The current Prop 3.4 (L228--244) asserts an isomorphism `(BP^k)^! ~~ BP^{k'}` of chiral algebras and proves it by appeal to CLNS24 Thm 4.4 + Feigin--Frenkel. This is a strong claim — but it's stated as a *VOA isomorphism* without specifying which derived/chiral category the equivalence lives in.

**Stronger formulation:**

> **Theorem (BP Koszul self-duality, derived).** For every `k in C \ {-3}`, the bar-cobar adjunction induces a derived equivalence `D^b(BP^k\text{-mod}) ≃ D^b(BP^{-k-6}\text{-mod})` of triangulated categories, intertwining (a) the modular characteristic on the `T`-line by `kappa_T -> 98 - kappa_T` and (b) the shadow obstruction tower by `S_r(c) <-> S_r(K - c)`. The equivalence is *self-dual* (its inverse is itself, twisted by the involution). At the critical level `k=-3` the derived category degenerates: `BP^{-3}` is no longer an honest VOA, and the equivalence becomes a self-equivalence of the derived category of the Feigin--Frenkel centre.

This adds derived-categorical structure to the bare "Koszul self-dual" assertion, gives a *transformation rule* for kappa under the involution (which the current paper writes as the *value* `kappa + kappa' = 98` only — the transformation rule `kappa -> 98 - kappa` is stronger), and explains the critical-level behaviour conceptually instead of phenomenologically.

### Upgrade path 3: "Mixed shadow class as a new invariant"

The most genuinely original mathematical claim in `bp_self_duality.tex` is Remark 5.3 (L423--434): BP exhibits *different shadow classes on different generator lines* (M on `T`, G on `J`). This is presented as an observation. Upgrade it to a definition + theorem:

> **Definition (per-line shadow signature).** For a chiral algebra `A` with strong generators `{g_i}_{i ∈ I}`, the *per-line shadow signature* is the function `sigsh: I -> {G, L, C, M, fermionic}` assigning to each generator `g_i` the shadow class of the obstruction tower restricted to the primary slice spanned by `g_i`.

> **Theorem (BP signature, corrected).** The BP algebra has signature `sigsh(BP) = (T: M, J: G, G^+: fermionic, G^-: fermionic)`. The global shadow class of `BP` is the maximum over `i in I`, namely `M`.

> **Conjecture.** For every `W`-algebra `W_k(sl_N, f_lambda)`, the per-line signature is determined by the partition `lambda` and the dual Coxeter number `h^v` via the partition-of-generator-weights into "Heisenberg-like" (G), "free-fermion-like" (G), "Virasoro-like" (M), and "ghost-like" (fermionic).

This converts the BP "first non-principal mixed example" observation into a **classification programme**: the mixed signature is not an oddity but the generic phenomenon for non-principal `W`-algebras, with the principal `W`-algebras being the degenerate case where all lines agree.

The critical level `k=-3` reappears in this language as the level where the `J`-line residual level `k_res = k + 1/2` collides with `-5/2` (and the `T`-line central charge diverges) — the per-line signature *itself* degenerates at `k=-3`, predicting an obstruction at the critical level visible from the signature point of view alone.

---

## Section 5. Punch list (ordered by criticality)

**P0 — Critical, must fix before submission**

1. **`bp_self_duality.tex` Eq. 3.5 (L322--329)**: arithmetic error. `1 - 4/3 - 4/3 + 1/2 = -7/6`, **not** `1/6`. Either the claimed `rho = 1/6` is right and the derivation is wrong (most likely — recompute the DS-reduction signed sum: e.g., maybe `+2/(3/2)` not `-2/(3/2)` for `G^pm`, or different weight assignments), or the answer is wrong. **Either way, this paragraph as written is mathematically false.** This is the single most embarrassing item.

2. **`bp_self_duality.tex` `kappa` prefactor inconsistency**: the file uses `kappa_T = c/2` (Prop. 3.5, L331--345) and *implicitly* `kappa = c/6` (the abstract's "anomaly ratio = 1/6" implies `kappa = c/6`). These are incompatible. Pick one and propagate. AP39 says they're family-specific, so the BP-specific value (`c/6` per `koszulness_fourteen_characterizations.tex` and `five_theorems_modular_koszul.tex`) is the right one for the *full* algebra, while `c/2` is the right one for the *T-line restriction*. The paper should distinguish `kappa^{full}_BP = c/6` from `kappa^T_BP = c/2`.

3. **`koszulness_fourteen_characterizations.tex` L1298**: `c = (k-1)(6k+1)/(k+3)` is the **wrong central-charge formula** for BP. At `k=-3/2`: gives `c = 40/3`, but the triplet value is `c = -2`. Replace with `c = 2 - 24(k+1)^2/(k+3)`.

4. **`five_theorems_modular_koszul.tex` L2551--2552**: presents `kappa(BP_{-3}) = 49/3` as a **value at a level**. It is not — both `c(-3 + eps)` and `c(-3 - eps)` diverge in opposite directions. Replace with: "The fixed point of the involution `k = -k - 6` is `k = -3`, which coincides with the critical level `k = -h^v(sl_3)`. At this point the BP VOA degenerates and `c` is undefined; the principal-value mean is `(c+c')/2 = 98`, equivalently `kappa^{full} = 49/3`." Same fix in `koszulness_fourteen_characterizations.tex` L1315--1316.

5. **`bp_self_duality.tex` Thm 4.4 (L485--503)**: theorem statement says `k' = -k - N`, the proof acknowledges this is wrong (`-k - 2N`), but the displayed equation in the theorem is never patched. Fix the theorem.

**P1 — Important, should fix in next revision**

6. **`bp_self_duality.tex` Prop. 4.7 heading (L598)**: rename "BP self-dual point" -> "BP involution fixed point and the critical level" (AP8: avoid bare "self-dual").

7. **`bp_self_duality.tex` Thm 3.4 (L253--269)**: upgrade to *polynomial identity* form per Upgrade Path 1. Replace `K_B = 196` with `c_BP(k) + c_BP(-k-6) = 196 in Q[k][1/(k+3)]`.

8. **Warning 3.7 (L271--292)**: clarify that the `c2` formula is **wrong**, not "a different convention". The compute module `bp_shadow_tower.py` agrees this is an AP1/AP3 correction (lines 17--19, 51--53), so the warning should *cite the resolution* and not present it as a parallel convention.

**P2 — Strengthening, optional but recommended**

9. **Add a "transformation rule" remark**: under `k -> -k-6`, `c -> 196 - c` and `kappa^{full} -> 196/6 - kappa^{full} = 98/3 - kappa^{full}`. This is the clean form of the conductor.

10. **Add a "principal value" remark** to Prop. 4.7: the value `c = K/2 = 98` is the principal value of `c` across the pole at `k=-3`, not the value of `c` at any real `k`. Make explicit that `c(k) - 98` is an *odd function* of `k+3`.

11. **Add per-line signature definition** (Upgrade Path 3): elevate Remark 5.3 to a definition + theorem with a conjectural classification, so the "first non-principal mixed example" observation becomes a structural result.

12. **Independent verification protocol** (per CLAUDE.md HZ3-11 / AP-CY10 protocol): the conductor `K=196` is currently verified via `c+c'` algebraic computation only. Add an *independent* verification path: e.g., (a) bar-Euler-product computation, (b) Hilbert polynomial cross-check, (c) Hochschild dimension computation. The 63 tests in `bp_shadow_tower.py + bershadsky_polyakov_bar.py` should be partitioned into `derived_from = {FKR central charge}` and `verified_against = {something else}` per the `@independent_verification` decorator.

---

## Summary

The wave-1 alarm ("`kappa(BP_{-3}) = 49/3` is suspicious because `c` has a pole at `k=-3`") is **confirmed**. The standalone `bp_self_duality.tex` itself acknowledges the singularity in Prop. 4.7, but the cross-reference files (`five_theorems_modular_koszul.tex`, `koszulness_fourteen_characterizations.tex`) drop the warning and present `49/3` as a value. The deeper issues are (a) an arithmetic error in the anomaly-ratio derivation Eq. 3.5 (`1 - 4/3 - 4/3 + 1/2 = -7/6`, not `1/6`), (b) an internal `kappa = c/2` vs `kappa = c/6` inconsistency in `bp_self_duality.tex`, (c) a wholly different (and wrong) central-charge formula in `koszulness_fourteen_characterizations.tex`, and (d) Thm 4.4's `k' = -k - N` typo (should be `-k - 2N`).

The strongest correct upgrade: state the conductor `K = 196` as a *polynomial identity* `c(k) + c(-k-6) = 196` valid on `Q(k)`, observe that `c(k) - 98` is an *odd function* of `k+3`, identify `k=-3` as the unique zero of the odd part *and* the critical level *and* the involution fixed point, and conclude that the formal "self-dual value" `c = 98` is the principal-value of `c` across the pole — never realised at a finite real level. This is sharper than any value-at-a-point claim and removes the degeneracy/divergence ambiguity entirely.

The genuinely novel mathematical content (Remark 5.3: BP exhibits mixed shadow class on different generator lines) deserves promotion from observation to definition and conjecture; this is the most original contribution of the standalone and should not be hidden in a remark.
