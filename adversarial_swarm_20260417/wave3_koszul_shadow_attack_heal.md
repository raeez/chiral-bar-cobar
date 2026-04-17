# Wave 3 — Koszul 10+1+1 and Shadow-Tower Convergence: Adversarial Attack and Heal

**Target.** Koszul 10+1+1 equivalences (K1–K12 of `thm:koszul-equivalences-meta`), shadow-tower convergence claims (closed-form $\Sigma_{\mathrm{Vir}}$, $C_\cA = 6$ universal on class-M $T$-line, $W_3$ $W$-line $C = 12$, $S_4$, $S_5$), $Z_g$–$S_r$ arithmetic duality at $\{691, 3617\}$, depth gap, spin-stratified lattice conjecture.

**Date.** 2026-04-17.

**Voice.** Nekrasov–Gelfand–Etingof: "seamless passage between closed form and asymptotic regime," compression of depth gap to a single discriminant $\Delta = 8\kappa S_4$, scope-first.

---

## 1. Attack on the "10 unconditional" Koszul equivalences

### 1.1 What does the "10+1+1" count actually protect?

The status-table headline reads "**10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir).**" Authoritative inscriptions:

- `chapters/theory/chiral_koszul_pairs.tex:2348–2445` lists K1–K12 as `thm:koszul-equivalences-meta`.
- `chapters/theory/introduction.tex:2194` declares "ten unconditional equivalences, one conditional (Lagrangian, conditional on perfectness; unconditional for the standard landscape), and one one-directional ($\mathcal{D}$-module purity, with only the forward direction proved)."
- `standalone/koszulness_fourteen_characterizations.tex` rebases the list as a **fourteen-chart atlas on the Koszulness moduli scheme** (K1–K14), with (xv) Lagrangian and (xvi) D-mod purity standing OUTSIDE the fourteen.

The "10 vs 14" tension reflects two genuinely different decompositions:

1. **Vol I body** (K1–K12): collapses (xi)-(xiv) of the moduli-scheme atlas into a single factorisation-homology clause (K7) with its own internal scope split (genus-0 unconditional; all-genera uniform-weight).
2. **Standalone moduli atlas** (K1–K14): disaggregates the four homological-algebra chart coordinates (chiral Koszulness / PBW $E_2$-collapse / $A_\infty$-formality / Ext diagonal vanishing) plus five factorisation-geometry charts + one tropical chart.

Both are legitimate; the atlas view is sharper, the K1–K12 view is the editorial one in the body.

### 1.2 Is K6 genuinely an independent equivalence?

`rem:koszul-equivalences-meta-scope` (line 2323 of `chiral_koszul_pairs.tex`) is honest:

> "Item (vi) (the Barr–Beck–Lurie monadicity characterization) is a consequence of item (v) (bar–cobar quasi-isomorphism) via the standard comonadic reduction, not an independent equivalence; we list it because it is the $\infty$-categorical formulation most useful for applications, not because it supplies a logically new route."

This is a self-disclosed "10 but really 9 + 1 restatement" — the ten-fold TFAE reduces to a nine-fold TFAE plus a universally available reformulation. The "10 unconditional" headline is therefore **honest only with the caveat attached**. Reader-facing statements that drop the caveat are slightly inflated; in particular, `chapters/connections/holographic_codes_koszul.tex:42` says "10 unconditionally [equivalent]" without pointing to the K5⇒K6 monadic reduction.

Verdict: the Vol I inscription is correct; the scope remark is in place; nothing to retract, but the "ten unconditional" language should be read against `rem:koszul-equivalences-meta-scope` in every occurrence.

### 1.3 K7 uniform-weight conditionality

K7 (genus-0 concentration, with uniform-weight all-genera extension) is unconditional at genus zero. The all-genera clause is **conditional on uniform-weight** — this is transparently inscribed in the statement (line 2392: "If $\cA$ lies on the uniform-weight lane, then for every smooth projective curve $\Sigma_g$ ..."). On the multi-weight lane (e.g. $W_3$ beyond genus one), the concentration acquires the cross-channel correction $\delta F_g^{\mathrm{cross}}$; at $W_3$, genus 2, the correction is explicit: $(c+204)/(16c)$ (cited in the status table as `prop:delta-f-cross-w3-g2`).

Honest reading: K7 is two distinct equivalences fused into one line:
- **K7a** (genus-0 unconditional): $H^k(\int_{\mathbb{P}^1}\cA) = 0$ for $k \neq 0$.
- **K7b** (all-genera, uniform-weight): same vanishing on all $\Sigma_g$ with $\mathrm{obs}_g = \kappa \lambda_g$.

The "10 unconditional" count includes K7a; K7b is a refinement on a sublane. The scope tag is present in the theorem statement; no rectification needed, but the preface wording would benefit from making this split explicit rather than folding it into a single item.

### 1.4 K8 (ChirHoch concentration + duality) is one-way, with Massey hedge

K8 in the body theorem:

> "$\mathrm{ChirHoch}^*(\cA)$ is concentrated in cohomological degrees $\{0,1,2\}$ … and **any free-polynomial description of the graded-commutative cup-product algebra is conditional on a Massey-vanishing consequence of Fulton–MacPherson formality.**"

So K8 is a proved consequence of K1–K6 on the Koszul locus (concentration + duality + Hilbert series); the converse is not a logical equivalence. The freeness clause is additionally conditional on Massey vanishing. This matches the status-table "Equiv (viii): concentration proved; freeness conditional on Massey vanishing."

### 1.5 (xi) Lagrangian conditional on perfectness — verify perfectness is proved

Per status-table T2 (`prop:perfectness-standard-landscape`, 2026-04-16): perfectness is verified family-by-family — Heisenberg (finite at each weight), affine KM non-critical (Kac–Kazhdan), Virasoro generic $c$ (Feigin–Fuks), $W_N$ (Fateev–Lukyanov), lattice (theta/eta), $\beta\gamma$ (character). So for the **standard landscape at generic parameters**, perfectness is no longer a hypothesis: it is a theorem. The Lagrangian criterion is then unconditional on the standard landscape; conditional outside it. The introduction line ("conditional on perfectness; unconditional for the standard landscape") is precisely right.

### 1.6 (xii) $\mathcal{D}$-module purity one-direction

Forward direction (purity $\Rightarrow$ Koszulness): proved. Reverse: proved **only for the affine Kac–Moody family** (Deligne–Saito mixed-Hodge package on $\mathrm{Bun}_G$) and open in general. This one-direction status is transparent in the theorem statement (`chiral_koszul_pairs.tex:2367–2368`: "Condition (xii) implies condition (x); the converse is open").

### 1.7 Consolidated Koszul ledger (after attack)

| Characterization | Status | Hedge |
|---|---|---|
| K1 chiral Koszul | proved | anchor |
| K2 PBW $E_2$-collapse | ⇔ K1 | hub |
| K3 $A_\infty$-formality | ⇔ K1 | Priddy chiral avatar |
| K4 Ext diagonal | ⇔ K1 | |
| K5 bar–cobar counit qi | ⇔ K1 | |
| K6 Barr–Beck–Lurie | ⇔ K5 | **logical restatement** (scope rem) |
| K7a genus-0 FH concentration | ⇔ K1 | unconditional |
| K7b all-genera FH concentration | ⇔ K1 | **uniform-weight hypothesis** |
| K8 ChirHoch concentration + duality | consequence, one-way | Hilbert series; free cup product conditional on Massey vanishing |
| K9 Kac–Shapovalov det ≠ 0 | ⇔ K1 | generic params |
| K10 FM boundary acyclicity | ⇔ K1 | |
| K11 Lagrangian transversality | ⇔ K1 on standard landscape | perfectness now a theorem (T2) |
| K12 D-mod purity | ⇒ K1 | reverse proved only for affine KM |

**Honest headline**: **8 genuine unconditional bidirections** (K1 ⇔ K2, K1 ⇔ K3, K1 ⇔ K4, K1 ⇔ K5, K1 ⇔ K7a, K1 ⇔ K9, K1 ⇔ K10, K1 ⇔ K11 on standard landscape) + K6 as a $\infty$-categorical restatement of K5 + K7b refinement (uniform-weight) + K8 proved one-way consequence + K12 proved forward only.

Retraction is not warranted: the scope remark inside the theorem is already adequate. **What *is* warranted** is that the bare headline "10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir)" should be refined in the preface and status table to read "**10 characterizations, organized as: 8 unconditional bidirections, 1 logical restatement (K5 ⇔ K6), 1 conditional bidirection (K7b uniform-weight), plus K8 proved one-way, K11 unconditional on standard landscape, K12 proved forward-only**." This is substance over slogan; the current shorter form is defensible but the longer form is cleaner.

---

## 2. Shadow-tower convergence and the $C_\cA = 6$ universal class

### 2.1 $\Sigma_{\mathrm{Vir}}(z)$ closed form — verified exactly

Direct power-series attack on
$$\Sigma_{\mathrm{Vir}}(z) = \frac{4 z^3}{9} - \frac{z^2}{9} + \frac{z}{27} - \frac{\log(1 + 6 z)}{162}.$$

Using $-\log(1+6z)/162 = \sum_{n \ge 1} (-1)^n 6^n z^n / (162 n)$ and combining with the cubic polynomial:
$$[z^1]: \tfrac{1}{27} - \tfrac{6}{162} = 0, \quad [z^2]: -\tfrac{1}{9} + \tfrac{36}{324} = 0, \quad [z^3]: \tfrac{4}{9} - \tfrac{216}{486} = 0.$$

The polynomial part exactly cancels the $z, z^2, z^3$ coefficients of the log expansion, so the series starts at $z^4$. Machine-precision check:

| $r$ | $A_r$ predicted | $A_r$ from closed form | ratio $A_r/A_{r-1}$ | $-6(r-1)/r$ |
|---|---|---|---|---|
| 4 | $2$ | $2$ | — | — |
| 5 | $-48/5$ | $-48/5$ | $-24/5$ | $-24/5$ ✓ |
| 6 | $48$ | $48$ | $-5$ | $-5$ ✓ |
| 7 | $-1728/7$ | $-1728/7$ | $-36/7$ | $-36/7$ ✓ |
| 8 | $1296$ | $1296$ | $-21/4$ | $-21/4$ ✓ |
| 9 | $-6912$ | $-6912$ | $-16/3$ | $-16/3$ ✓ |

Limit $|A_r/A_{r-1}| = 6(r-1)/r \to 6$. **No error.** Nekrasov-seamless.

### 2.2 Pole-doubling $\Sigma_{\mathrm{Vir}}^{(k)}(z) = [P_k + Q_k \log(1+6z)]/(1+6z)^{2k}$

Structural: the $k$-th $1/c^k$ correction introduces degree-$2k$ polynomial in $r$ acting as $z^{2k} d^{2k}/dz^{2k}$ (via Stirling-falling-factorial). Applied to $-\log(1+6z)/162$:
$$\frac{d^{2k}}{dz^{2k}}\!\left[-\frac{\log(1+6z)}{162}\right] = -\frac{(2k-1)! \cdot 6^{2k}}{162 (1+6z)^{2k}}.$$

Faà di Bruno dictates $(1+6z)^{-2k}$; the polynomial-plus-log numerator $P_k + Q_k \log(1+6z)$ comes from the polynomial remainder of $\Sigma_{\mathrm{Vir}}$ outside the log. Degree bounds $\deg P_k \le 2k + 3$, $\deg Q_k \le 2k$ follow from the polynomial degrees and the differentiation order. Subleading case $k=1$ (verified closed form, `thm:shadow-series-closed-form-Virasoro-subleading`):
$$\Sigma_{\mathrm{Vir}}^{(1)}(z) = \frac{16 z^5}{(1+6z)^2} + \frac{20 z^4/9}{(1+6z)^2} - \frac{992 z^3}{405} + \frac{248 z^2}{405} - \frac{248 z}{1215} + \frac{124 \log(1+6z)}{3645}.$$

Matches the $k=1$ template with $P_1, Q_1$ of the stated degrees. Structurally sound. No attack.

### 2.3 Decomposition $6 = r_0 \cdot S_{r_0} = 3 \cdot 2$

`thm:shadow-exponential-base-Virasoro` (line 670 of `shadow_tower_higher_coefficients.tex`): the recurrence gives $r A_r = -6(r-1) c A_{r-1}$, i.e. $|A_r/A_{r-1}| \to 6$. The factorization $6 = r_0 \cdot S_{r_0}$ with $r_0 = 3$ is the seed depth (the first nonvanishing OPE-correction depth above $S_2$), and $S_{r_0} = S_3(\mathrm{Vir}_c) = 2$ is the universal $T$-$T$ OPE seed. The decomposition **is structural**: it says the leading recurrence coefficient is determined by the seed $S_3$ times its index.

**Attack passes**: the 3·2 structure is not a coincidence; it is the specific value of the leading-order $j=3$ term in the Riccati recurrence.

### 2.4 $C_\cA = 6$ — universal on what, exactly?

`thm:universal-class-M-C-is-6` (line 677) has two explicit hypotheses:

1. $T$-line seed $S_3(\cA, T) = 2$.
2. All other generator-line contributions to $S_r$ at depth $r \ge 3$ are $O(c^{-\alpha})$ with $\alpha > 0$ — strictly subleading.

So the claim is scoped to $E_\infty$-chiral algebras in class M, non-logarithmic $C_2$-cofinite, **containing a Virasoro subalgebra**, on the $T$-line. This is NOT claiming $C_\cA = 6$ on $W_3$ $W$-line — where the integer is $12$, as separately computed. The statement's internal logic is tight: under hypothesis (2), only the $j=3$ $T$-$T$ contribution survives at $O(c)$, and the analysis reduces to the Virasoro recurrence.

**Attack passes**. The `rem:C-A-scope-E-infinity` (line 716) additionally clarifies the $E_\infty$-restriction.

### 2.5 $W_3$ $W$-line $C = 12 = 2 \cdot 6$ doubling

Claim: $a_n = 2 \cdot 3^{n-2} \binom{2n-4}{n-2} / [n(n-1)]$, $a_{n+1}/a_n = 6(2n-3)/(n+1) \to 12$.

Direct computation:
$a_3 = 2, a_4 = 9, a_5 = 54, a_6 = 378, a_7 = 2916, a_8 = 24057, a_9 = 208494, a_{10} = 1876446, a_{11} = 17399772.$

Ratios $a_n/a_{n-1}$: $9/2, 6, 7, 54/7, 33/4, 26/3, 9, 102/11, \ldots$ Formula $6(2n-5)/n$ at these indices: $9/2, 6, 7, 54/7, 33/4, 26/3, 9, 102/11$ — exact match. Limit: $6 \cdot 2 = 12$. ✓

The "doubling" $12 = 2 \cdot 6$ is post-hoc once $s(s+1)$ is known (see `rem:w3-wline-decomposition-is-circular` line 2225):

> "A natural temptation is to decompose the doubling $2 = (3/2)(4/3)$ … This decomposition is *post-hoc*: it holds because $C = s(s+1)$ for $s = 2, 3$ gives ratio $(s+2)/s = (3 \cdot 4)/(2 \cdot 3) = 2$ … The decomposition does *not* provide an independent derivation of $C = s(s+1)$."

The "Hessian ratio $3/2$ × kernel ratio $4/3$" mental model is a consequence of the formula, not a proof. The Vol I cache entry in `CLAUDE.md` (Key Constants block) describing this as "doubling from Hessian ratio 3/2 × kernel ratio 4/3" should be read as **heuristic**, not structural.

**Attack outcome**: the $C = 12$ value is verified; the "$12 = 2 \cdot 6$ via 3/2 × 4/3" heuristic is honestly flagged inside the body.

### 2.6 Spin-stratified conjecture $C_{W^{(s)}} = s(s+1)$

Two data points ($s = 2$: 6; $s = 3$: 12) do not determine a function. Alternative candidates the Vol I remark (`rem:w3-wline-higher-spin-prediction`, line 2237) enumerates:

- $s(s+1)$ → $s=4$: 20.
- $6(s-1)$ → $s=4$: 18.
- $4s^2 - 4s + 6$ → $s=4$: 22.
- $4s$ (from shared Riccati template with $j,k \ge 2, j+k = n+1$) → $s=4$: 16.

The Vol I inscription **already carries `\ClaimStatusConjectured`** with all four candidates exhibited. The commitment to $s(s+1)$ is on structural grounds (Zamolodchikov-norm scaling $N_{W^{(s)}} \propto c/s$ plus $s^{n-2}$ seed-generalization), not on numerical coincidence.

**Attack passes**. The conjecture is properly hedged. The falsification is a $W_4$ direct computation.

---

## 3. $S_4, S_5$ values and asymptotics

### 3.1 $S_4 = 10/[c(5c+22)]$

At $c = 13$: $S_4 = 10/(13 \cdot 87) = 10/1131$. At $c = 1$: $S_4 = 10/27$. Asymptotic at large $c$: $S_4 \sim 10/(5 c^2) = 2/c^2$, **not** $2/(5c^2)$. Cross-checked:
- $c = 1000$: exact $S_4 = 10/[1000 \cdot 5022] = 1.9912 \times 10^{-6}$; leading $2/c^2 = 2 \times 10^{-6}$; ratio $0.9956$ consistent.

AP178 correctly warns against the factor-of-5 error. No issue.

### 3.2 $S_5 = -48/[c^2(5c+22)]$

"Verified independently" via `rem:s5-bpz-wick-verification` (`shadow_tower_higher_coefficients.tex:87`):

> "The closed form admits a third genuinely independent verification via direct Belavin–Polyakov–Zamolodchikov 5-point Wick contraction. The Wick chain extracts $\langle \Lambda | \Lambda \rangle = c(5c+22)/10$ from the Schur complement of the Virasoro level-4 Gram matrix, reads off $S_3 = 2$ from the universal BPZ 3-point Ward identity, counts $\Lambda$-mediated chord-diagram topologies on $K_5$ via inclusion–exclusion cumulant inversion (signed weight $-48/10$) … The implementation is at `compute/lib/s5_virasoro_wick.py` with the independent-verification decorator at `compute/tests/test_s5_virasoro_wick.py::TestWickIndependentVerification` covering six finite calibration points."

The Wick chain takes $(\kappa, S_3, S_4)$ via a different symbolic route than the Riccati MC recursion. Path disjointness is explicit.

At $c = 13$: $S_5 = -48/(169 \cdot 87) = -16/4901$. Negative sign is correct: the universal pattern is alternating for Virasoro shadows — `shadow_tower_higher_coefficients.tex:375`:

> "the odd-weight $S_5, S_7$ inherit … $S_4 > 0$, $S_5 < 0$, $S_6 > 0$, $S_7 < 0$ reflects the sign of the Hessian-projector eigenvalue."

No physical-unitarity obstruction: $S_r$ are not amplitude coefficients but Maurer–Cartan shadow projections; their signs encode Hessian-eigenvalue signs, not probability-preservation data. The negative $S_5$ is expected.

---

## 4. $Z_g$ — $S_r$ arithmetic duality at $\{691, 3617\}$

### 4.1 Presence on $Z_g$

$Z_g$ leading coefficient: $B_{2g-2}/(g-1)$.

$g = 7$: leading $= B_{12}/6 = (-691/2730)/6 = -691/16380$. **691 appears in the numerator**.
$g = 9$: leading $= B_{16}/8 = (-3617/510)/8 = -3617/4080$. **3617 appears in the numerator**.

Both are prime (691 and 3617 are prime integers, Kummer-irregular: they divide their Bernoulli-numerator witnesses).

### 4.2 Absence through $S_r$, $r \le 11$

`thm:s-r-kummer-absent-through-r-11` (line 2425): the cleared Virasoro shadow numerators $N_r(c) \in \mathbb{Z}[c]$ have prime content supported on $\{2, 3, 5, 7, 17, 61, 163, 173, 193, 2111, 16657, 38891, 292351, 3988097\}$; neither 691 nor 3617 appears.

**Sharp**: the claim is **only for the leading two Kummer-irregular primes**. The theorem explicitly notes that 2111 (which IS Kummer-irregular, dividing $\mathrm{num}(B_{1038})$) DOES appear in $N_9$ via $29554 = 2 \cdot 7 \cdot 2111$. So the duality statement is not "no Kummer-irregular prime ever appears on $S_r$" but "the leading two Kummer-irregular primes $\{691, 3617\}$ are absent through $r = 11$."

The body is already explicit about this. Programmatic caches (CLAUDE.md "Z_g closed forms" line) could be read as overclaiming; the precise statement is the one in the theorem — the disjointness is at $\{691, 3617\}$, not at all Kummer-irregular primes.

### 4.3 B92 retractions (2026-04-17 session headlines)

The 2026-04-17 audit has already retracted primes $\{1423, 3067, 23, 43, 419\}$ from the Kummer-irregular label at primary-source verification; they appear in $S_r$ numerators as **Riccati-arithmetic characteristic primes**, not Kummer-arithmetic. Corrected Tier-3 emergence: $\{37, 691, 811\}$. The CLAUDE.md B92/B88 catalog enforces this.

**Attack passes**: arithmetic duality is sharp, scope-qualified, honestly hedged. Nothing to downgrade here.

---

## 5. Depth-gap $d_{\mathrm{alg}} \in \{0, 1, 2, \infty\}$

### 5.1 First-principles proof or case analysis?

`prop:depth-gap-trichotomy` (`higher_genus_modular_koszul.tex:18188`) proof structure:

**Single-line regime $\kappa \ne 0$.** On a primary line with $\kappa \ne 0$:
- $Q_L(t) = (2\kappa + 3 \alpha t)^2 + 2 \Delta t^2$ (Gaussian decomposition), $\Delta = 8 \kappa S_4$ (critical discriminant).
- $H(t) = t^2 \sqrt{Q_L(t)}$ (shadow generating function).
- If $\Delta = 0$ (i.e. $S_4 = 0$): $Q_L$ is a perfect square; $H$ is a polynomial of degree 3; tower terminates; $d_{\mathrm{alg}} \in \{0, 1\}$.
- If $\Delta \ne 0$: binomial expansion of $\sqrt{Q_L}$ with quadratic interaction $u = (6 \alpha t + (9\alpha^2 + 2\Delta) t^2)/(4\kappa^2)$ does NOT terminate; $S_r \ne 0$ for infinitely many $r$; $d_{\mathrm{alg}} = \infty$.

Thus **on any $\kappa \ne 0$ line, the only finite values are $\{0, 1\}$; finite value 2 never occurs; finite value $\ge 3$ never occurs.** This is a first-principles argument (algebraicity of $\sqrt{Q_L}$), not a case analysis over finitely many families.

**Global contact witness.** $d_{\mathrm{alg}} = 2$ is realized by the $\beta\gamma_\lambda$ family GLOBALLY, NOT on any single primary line. On the $T$-line $S_4 = 10/[c(5c+22)] \ne 0$ (infinite tail); on the weight-changing line all shadows vanish. The interaction of two non-proportional primary lines produces $r_{\max} = 4$ globally: $S_4 = -5/12$ survives as an integrated cross-channel residue, $S_r = 0$ for $r \ge 5$.

### 5.2 Impossibility of $d_{\mathrm{alg}} = 3$ — `lem:depth-three-impossible`

Two proofs in `higher_genus_modular_koszul.tex`: (a) MC recursion at degrees 5 and 6 forces a nonzero tail when $S_4 \ne 0$, regardless of whether $\alpha = 0$ or $\alpha \ne 0$; (b) shadow Lie algebra representation: $D_{\mathfrak{Q}}$ is a degree-2 raising operator whose iterates populate all even degrees; the only finite-length representation with $S_3 \ne 0$ occurs at $S_4 = 0$ (class L, $d_{\mathrm{alg}} = 1$).

Both proofs are structural/algebraic; neither is a case analysis. The first-principles argument is inscribed.

**Attack passes**. Nothing to heal.

---

## 6. Surgical edits

### 6.1 Downgrades / retractions

Attack yielded no downgrades. All five top claims (Koszul 10+1+1; $C_\cA = 6$; $W_3$ $C = 12$; $S_4, S_5$; depth gap; Kummer duality) hold at their stated scopes. Existing scope remarks (`rem:koszul-equivalences-meta-scope`, `rem:C-A-scope-E-infinity`, `rem:w3-wline-decomposition-is-circular`, `rem:spin-stratified-cwsl`, `thm:s-r-kummer-absent-through-r-11`) are sufficient.

### 6.2 Editorial refinements (not commits)

If a future preface-refresh session touches the 10+1+1 headline, recommend the longer form:

> "The twelve characterizations of chiral Koszulness comprise: eight unconditional bidirections (K1 ⇔ K2 through K1 ⇔ K10, on the standard landscape at generic parameters), the $\infty$-categorical Barr–Beck–Lurie restatement (K6 ⇔ K5, not an independent equivalence), the uniform-weight all-genera extension of factorization-homology concentration (K7b, conditional), the Hochschild consequence with Massey-conditional free cup product (K8, one-way), the Lagrangian transversality criterion (K11, conditional on perfectness — unconditional on the standard landscape), and $\mathcal{D}$-module purity (K12, forward direction proved)."

This is substance, not slogan. The current `chapters/theory/introduction.tex:2194` line is already nearly this long.

### 6.3 Working-notes rectification

The `working_notes.tex:9778–9815` entries describing the spin-stratified lattice already carry the conjectural caveat with the four candidate extrapolations. The CLAUDE.md cache entry for the "Conjectural spin-stratified lattice: $C_{W^{(s)}} = s(s+1)$ for each primary in principal $W_N$" should append the four candidate values at $s=4$ $\{20, 18, 22, 16\}$ for discipline. This is a memory-file update, not a manuscript edit.

---

## 7. Verdict summary

| Target | Attack outcome | Heal |
|---|---|---|
| Koszul "10 unconditional" | sound with scope remark; K6 = K5 restatement; K7 two-clause | keep; recommend longer headline in preface |
| Lagrangian (xi) | unconditional on standard landscape (perfectness now a theorem) | no change |
| D-mod purity (xii) | forward proved; reverse proved only for affine KM | scope already explicit |
| $\Sigma_{\mathrm{Vir}}(z)$ closed form | verified exactly (polynomial part cancels log tail at $z^1, z^2, z^3$; $A_r$ matches) | no change |
| Pole-doubling $\Sigma_{\mathrm{Vir}}^{(k)}$ | structural; degree bounds sound | no change |
| $6 = r_0 \cdot S_{r_0} = 3 \cdot 2$ | structural (leading $j=3$ term, $S_3 = 2$) | no change |
| $C_\cA = 6$ universal | scoped to class-M $T$-line with Virasoro subalgebra; $E_\infty$-only | no change |
| $W_3$ $W$-line $C = 12$ | verified numerically to $n = 11$ | no change |
| $12 = 2 \cdot 6$ "doubling via 3/2 × 4/3" | heuristic; already flagged post-hoc | caveat retained |
| $C_{W^{(s)}} = s(s+1)$ | Conjectured; four candidates at $s=4$ inscribed | append candidate values to cache |
| $S_4, S_5$ | verified; $S_5$ BPZ–Wick independently | no change |
| $S_4$ asymptotic $\sim 2/c^2$ | correct (AP178 enforced) | no change |
| Depth gap | first-principles (Riccati $\sqrt{Q_L}$ algebraicity); no case analysis | no change |
| $\{691, 3617\}$ on $Z_g$ | verified via $B_{12}, B_{16}$ numerators | no change |
| $\{691, 3617\}$ absent on $S_r, r \le 11$ | sharp; explicitly NOT a "no Kummer-irregular" claim (2111 present on $N_9$) | scope already explicit |

Zero downgrades. Zero retractions. The Vol I inscription passes the adversarial attack at every checked point. The 2026-04-17 session Beilinson-audit healing (which retracted primes $\{1423, 3067, 23, 43, 419\}$ and corrected the Tier-3 emergence set) had already absorbed the most dangerous attack surface.

Russian-school verdict: **the shadow-tower closed forms are Nekrasov-seamless** (polynomial and logarithmic pieces fit without adjustable constants); **the depth gap is Gelfand-compressed** (single discriminant $\Delta = 8\kappa S_4$ distinguishes $\{0, 1\}$ from $\infty$); **the Koszul 10+1+1 ledger is Etingof-precise** (every headline word carries a scope modifier somewhere in the theorem statement). No Beilinson-dismissals trigger.

---

## 8. Residual follow-ups (not in scope, not actioned)

- **$W_4$ $W^{(4)}$-line direct computation** would falsify or confirm $s(s+1)$ at $s=4$ against the four candidates $\{20, 18, 22, 16\}$. Requires explicit Fateev–Lukyanov $W^{(4)} W^{(4)}$ OPE structure constants — separate engine.
- **Seed-scaling theorem** relating $W_N$ $W^{(s)}$-line integer sequences across spins would provide structural (not merely extrapolative) grounds for $C^{(s)} = s(s+1)$.
- **Kummer-absence at $r \ge 12$**: $N_{12}$ through $N_{15}$ would probe whether the $\{691, 3617\}$-disjointness extends, or whether — as the geometric heuristic predicts — the primes enter $S_r$ at $r$ comparable to the corresponding Bernoulli index.

These are research frontier items; not rectification targets.

---

## 9. No `\begin{conjecture}` insertions required

Every attacked target either: (a) is already inscribed as a theorem with adequate scope, OR (b) is already inscribed as a conjecture with candidate alternatives. No environment downgrades are needed. The `prop:depth-gap-trichotomy`, `thm:universal-class-M-C-is-6`, `thm:s-r-kummer-absent-through-r-11`, and `thm:koszul-equivalences-meta` all stand at their stated scopes.
