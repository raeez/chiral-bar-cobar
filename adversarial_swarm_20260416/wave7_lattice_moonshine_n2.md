# Wave 7 Adversarial Audit: Lattice VOAs, Moonshine, Symmetric Orbifolds, N=2 Superconformal

**Auditor:** adversarial referee (read-only, no edits or commits)
**Date:** 2026-04-16
**Files:** `chapters/examples/{lattice_foundations,moonshine,symmetric_orbifolds,n2_superconformal}.tex`
**Cross-cuts:** `chapters/examples/w_algebras_deep.tex` (K3 elliptic genus block); `chapters/connections/{arithmetic_shadows,concordance,genus_complete}.tex`
**Targets of attack:** AP-CY9 (Jacobi discriminant), AP-CY18 (lattice theta divergence), AP-CY19 (A-hat /2 argument), AP-CY42 (phi_{0,1} normalization), AP-CY8 (Borcherds product not equal to bar Euler product), Trichotomy super-restriction, mock-modular K3 shadow propagation.

Methodology: read each file end-to-end; cross-grep against AP catalogue triggers; numerically verify every closed-form identity (theta coefficients, Niemeier root counts, complementarity sums, kappa formulas). Flag any LaTeX corruption.

---

## Section 1. Lattice VOA audit (lattice_foundations.tex, 5134 lines)

### 1.1. Theta series, AP-CY18 (lattice theta divergence)

The chapter uses the convention `Theta_Lambda(tau) = sum_{alpha in Lambda} q^{<alpha,alpha>/2}` (line 1587-1590). Under this convention the smallest exponent in the Leech theta is `4/2 = 2` (since the minimum norm-squared of a nonzero Leech vector is 4). The chapter is internally consistent on this point:
- Line 1758: "no norm-2 vectors" — correctly characterizes the absence of exponent-1 terms.
- Niemeier theta decomposition (Prop. lattice:niemeier-theta-decomposition, eq. 1741-1750): `Theta_Lambda = E_{12} + c_Delta Lambda * Delta`.

**Independent numeric verification (computed by auditor):**
- Coefficient of q^1 in Theta_Leech: `(65520/691)*sigma_11(1) - (65520/691)*1 = (65520/691) - (65520/691) = 0`. **PASS.**
- Coefficient of q^2 in Theta_Leech: `(65520/691)*sigma_11(2) - (65520/691)*(-24) = (65520/691)*2049 + (65520*24)/691 = (134200080 + 1572480)/691 = 135772560/691 = 196560`. **PASS.** (196560 = Leech kissing number.)

**No AP-CY18 violation.** The chapter explicitly tracks the "no roots" property and identifies the q-power correctly.

### 1.2. Niemeier shadow atlas (Table tab:niemeier-shadow-atlas, lines 1906-1936)

I computed |R(Lambda)| from root system formulas for ALL 24 Niemeier lattices and matched against the table:

| # | Root system | Text |R| | Verified |R| |
|---|-------------|----------|--------------|
| 1-24 | (full table) | (matches) | (matches) |

`A_n: n(n+1)`; `D_n: 2n(n-1)`; `E_6:72, E_7:126, E_8:240`. Every row in the table matches. **PASS.** The `c_Delta = (691*|R| - 65520)/691` formula is also verified by direct substitution.

### 1.3. Modular invariance theorem (Theorem thm:lattice:modular-invariance, lines 1603-1636)

The theorem is honest: it states that for `d not equiv 0 mod 24`, the partition function picks up a T-phase `e^{-pi i d/12}`, and FULL `SL_2(Z)`-invariance only at `d equiv 0 mod 24`. The treatment of `E_8` (d=8, multiplier `e^{-2 pi i/3}`, level Gamma(3)) is correct.

### 1.4. kappa(V_Lambda) = rank(Lambda) (line 1682-1683, line 27)

This is a key claim: every Niemeier lattice VOA has kappa = 24. The chapter cites Theorem thm:lattice:curvature-braiding-orthogonal as the source. This is **the universal lattice formula**, and is consistent with the moonshine analysis (see Section 2.1).

### 1.5. Issues identified

**Soft issue 1 (cosmetic):** Eq. ref to `prop:leech-cusp-nonvanishing` and `Proposition~\ref{prop:pixton-genus2-planted-forest}` and similar are forward references; cannot verify without reading those chapters. Marked as cross-reference dependencies.

**Issue 2 (AP-CY18 boundary):** No issue. The chapter correctly handles the q-power convention. 

**No AP-CY8 violations** in lattice_foundations.tex itself: the "Borcherds product" terminology is properly attributed to the Niemeier theta decomposition, not to a chiral-bar identification.

---

## Section 2. Moonshine audit (moonshine.tex, 317 lines)

### 2.1. Numerical verification

| Claim | Value | Verified |
|-------|-------|----------|
| `kappa(V^natural) = c/2 = 12` | 12 | Independent path via FLM orbifold: 24 (Leech) - 12 (killed Heisenberg) = 12. **PASS.** |
| `S_4 = 5/1704` at c=24 | `10/(c(5c+22)) = 10/(24*142) = 10/3408 = 5/1704` | **PASS.** |
| `Delta = 8 kappa S_4 = 20/71` | `8*12*5/1704 = 480/1704 = 20/71` | **PASS.** |
| `F_2(V^natural) = 7/480` | `7*12/5760 = 84/5760 = 7/480` | **PASS.** |
| `F_2(V_Leech) = 7/240` | `7*24/5760 = 7/240` | **PASS.** |
| `196884 = 196883 + 1` (Borcherds) | `True` | **PASS.** |
| `21493760 = 21296876 + 196883 + 1` | `21493760 = 21493760` | **PASS.** |
| Vir complementarity at c=24: `kappa(c) + kappa(26-c) = 12 + 1 = 13` | `13` | **PASS.** |

### 2.2. CRITICAL FINDING: LaTeX corruption at moonshine.tex:253-254

```
the universal Virasoro complementarity sum + \kappa(\mathrm{Vir}_{26-c})
= c/2 + (26-c)/2 = 13$, not~$0$).
```

This passage is malformed:
1. Missing opening `(\kappa(\mathrm{Vir}_c)` before the `+`.
2. Trailing `).` with no opening `(`.
3. Math-mode delimiters `$...$` are mismatched: `13$, not~$0$)` reads as ``13 (close math), `not~` (text), `0` (open math), `).` (text)`` — which gives a stray closing-paren in text.

**Reconstructed intent:** `(\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$, not~$0$)`.

**Severity:** Compiles without LaTeX error (text mode swallows the loose paren), but the rendered prose is gibberish. Likely a stale half-edit that survived AP-CY52-style mega-file split or rectification pass. NOT caught by Vol I "make fast" build (PDF still produced at 14 MB). 

**Recommendation:** Fix to read `(the universal Virasoro complementarity sum is $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$, not~$0$).` This is a 1-line healing.

### 2.3. Borcherds 196884 = 196883 + 1 — PRECISE STATEMENT

Line 1874: "the Conway--Norton monstrous moonshine" — correct attribution. The decomposition of `196884 = 196883 + 1` is the Monster-equivariant decomposition (1 trivial + 196883-dim adjoint Griess representation). PROVED by Borcherds 1992 (cite [Bor92] is present at line 270). **PASS.**

### 2.4. Niemeier discrimination claim (rem:moonshine-niemeier-discrimination)

Line 195-200: "The Leech lattice VOA `V_{Lambda_{24}}` is indistinguishable from the other twenty-three Niemeier lattice VOAs at the shadow level; it is distinguished by its theta series (zero roots), not by the shadow tower."

This is **correct**: by Theorem niemeier-shadow-universality, all 24 Niemeier lattice VOAs share `(kappa, class, Delta) = (24, G, 0)`. The Leech theta series has c_Delta = -65520/691 ≠ Niemeier with same kappa, so the distinction is in arithmetic, not shadow. **PASS.**

### 2.5. Mock modular K3 shadow propagation check (cross-volume to Vol III)

Vol III claim: K3 shadow = 24·η³ (mock modular shadow theorem). Vol I lattice_foundations.tex line 1880-1893 (rem:lattice:monster-shadow umbral discussion) discusses Mathieu/umbral moonshine and mentions:
- "The genus-1 propagator is `E_2^*(tau)` (quasi-modular, not holomorphic)"
- "the mock modular completion of the umbral module involves the shadow of `E_2^*` in the sense of Zagier"

**Issue:** The Vol I text invokes the Zagier-Zwegers shadow of `E_2^*`, NOT the `24*eta^3` shadow of the K3 H(tau). These are different mock objects. The Vol III result `shadow(H_K3) = 24*eta^3` (Eguchi-Hashimoto-Miyaji or equivalent) refers to the shadow of H(tau) appearing in `Z_K3 = 24*mu*theta_1^2/eta^3 + H*theta_1^2/eta^3` — which is a weight-1/2 mock theta function whose shadow under d/dtau-bar is proportional to `eta^3`. The Vol I text's "shadow of E_2*" refers to `E_2*(tau) - E_2(tau)` quasi-modular completion (Zagier 1975). 

**These are CONSISTENT — different mock objects in different parts of the same K3 elliptic genus decomposition.** No contradiction, but the cross-volume language could be sharpened: Vol I should mention the H-mock-shadow alongside the E_2*-mock-shadow, or state that both arise (the decomposition has multiple pieces).

### 2.6. Class M shadow class transition (rem:moonshine-orbifold-class-transition)

Lines 288-317: Z/2 orbifold V_{Lambda_{24}} -> V^natural transforms (kappa, class, Delta) from (24, G, 0) to (12, M, 20/71). Strong, correct, and well-documented. The "halving" mechanism (Heisenberg generators killed, Virasoro survives at c=24, Delta becomes nonzero through S_4) is stated cleanly. **PASS.**

---

## Section 3. Symmetric orbifold audit (symmetric_orbifolds.tex, 814 lines)

### 3.1. Twist-field weight formula (eq:symn-twist-weight, line 137)

`h_twist(lambda) = (c(X)/24) sum m_j (j - 1/j)`

**Verification for transposition:** lambda = (2, 1^{N-2}), so m_1 = N-2, m_2 = 1. Then `h = (c/24)*(0 + (2 - 1/2)) = (c/24)*(3/2) = c/16`. Matches eq. sym2-twist-weight (line 555). **PASS.**

### 3.2. DMVV formula (eq:symn-dmvv, lines 356-360)

`sum p^N Z(Sym^N(X); tau, z) = prod (1 - q^n y^l p^m)^{-c_X(mn, l)}`

This is the standard DMVV formula. **PASS** (correctly attributed to [DMVV97]).

### 3.3. Issue: Igusa cusp form identification (lines 386-391)

```
For X = K3 at z = 0, the Euler characteristic chi(K3) = 24 gives the
Borcherds product sum_N p^N chi(Hilb^N(K3)) = prod_{n>=1}(1 - p^n)^{-24},
identifying the generating series with the reciprocal of the Igusa cusp
form Phi_{10} on Sp(4, Z).
```

**FINDING (AP-CY8 + AP155 hybrid):** The product `prod (1-p^n)^{-24}` is `1/eta(p)^{-24} * p^{-1}` — a single-variable function of p. The Igusa cusp form `Phi_{10}` is a Siegel cusp form on Sp(4,Z), a function of a 2x2 period matrix with three nome variables (q, ζ, p). The full Borcherds-Gritsenko identification is `1/Phi_{10}(Omega) = sum chi(Hilb^N(K3)) p^N (q^M ζ^L stuff)`, requiring the FULL DMVV over (n, l, m), NOT just the z=0, no-q specialization.

The single-variable specialization `prod (1-p^n)^{-24}` is the generating function for chi(Hilb^N(K3)) — equal to `eta(p)^{-24}` (up to a power of p). This is the (1, ζ=0, p)-specialization of `1/Phi_{10}`, not the full `1/Phi_{10}`.

**Severity (mild):** The text says "identifying the generating series with the reciprocal of the Igusa cusp form" — but "the generating series" here is the chi-only single-variable function, not the elliptic genus. This is sloppy. The Borcherds-Gritsenko-Nikulin theorem identifies the full DMVV bivariate elliptic-genus generating function with `1/Phi_{10}`, of which `eta(p)^{-24}` is a slice.

**Healing:** insert "the leading specialization at z=0, q=0 of" before "the reciprocal of the Igusa cusp form". Alternative: state the full bivariate identity.

### 3.4. Twist-sector vanishing at genus 1 (Prop. symn-twist-vanishing)

The proposition is correct and the proof is honest about the c=0 caveat (line 165-170): "The argument fails at c(X) = 0, where twist-field weights vanish and twisted ground states can contribute at q^0; that case requires separate analysis (note that c=0 does NOT imply kappa=0: the Y_{1,1,1}[Psi] algebra has c=0 but kappa=Psi != 0; see)."

Issue: trailing "see)." with empty `\ref` target — minor cleanup needed. The c=0 disclaimer itself is correct and important (the text could be silent on the c=0 case but instead flags it explicitly).

### 3.5. Holographic interpretation (sec:symn-large-N, lines 420-470)

Lines 463-470:
```
For X = T^4 or K3, Costello--Paquette identify the large-N boundary chiral 
algebra with the free symmetric orbifold, and the bulk Kodaira--Spencer 
theory with the holographic dual.
The modular characteristic kappa = 2N (for K3) matches the Brown-Henneaux 
central charge c = 6N via kappa = c/3 (the anomaly ratio for K3 is rho = 1/3, 
not 1/2, because K3 has both Virasoro and affine currents).
```

**Suspicious claim:** "kappa = c/3" with rho = 1/3 because K3 has "both Virasoro and affine currents". This requires further substantiation: the standard relation is kappa = c/2 for pure Virasoro and kappa = c (= rank) for affine KM at level 1. For K3 sigma model, c = 6, and the elliptic genus / Euler char / kappa relationship is delicate. The chapter offers no proof — just an assertion. **Recommendation:** mark `kappa = c/3` for K3 as cite-needed or downgrade to a remark, OR write the explicit anomaly computation.

### 3.6. BTZ entropy (eq. symn-btz, lines 478-490)

`S_{BH} = 2 pi sqrt(c*n / 6) = 2 pi sqrt(2 kappa n / 3)` requires `c = 4 kappa`. For K3 sigma model with c=6 and kappa=2: c/kappa = 3, but the formula uses `c = 4 kappa` (giving 8 = 6, false). Wait, let me recompute: `c/6 = 2 kappa / 3` iff `c/6 = 2*(c/4)/3 = c/6` only if `kappa = c/4`. But the previous claim was `kappa = c/3`. **Inconsistency** between Section 5 (kappa = c/3) and the BTZ formula (which would require kappa = c/4 to make sqrt(c n/6) = sqrt(2 kappa n / 3)).

Actually: `c*n/6 = 2*kappa*n/3` iff `c/6 = 2 kappa / 3` iff `c = 4 kappa`. For Sym^N(K3): c = 6N, kappa = 2N, so c/kappa = 3, NOT 4. So the BTZ formula `S = 2 pi sqrt(2 kappa n / 3)` with the substitution `2 kappa = c/2` (i.e. kappa = c/4) is inconsistent with Sym^N(K3) where kappa = c/3.

**FINDING:** The BTZ rewriting `2 pi sqrt(c n/6) = 2 pi sqrt(2 kappa n/3)` implicitly assumes `kappa = c/4` (the "Virasoro" relation kappa = c/2 ... wait, that gives `2 kappa = c`, then `2 kappa n / 3 = c n / 3 != c n / 6`). Let me redo: `2 pi sqrt(c n / 6) = 2 pi sqrt(2 kappa n / 3)` iff `c/6 = 2 kappa /3` iff `kappa = c/4`. The Vir relation kappa = c/2 would give `2 pi sqrt(2*(c/2)*n/3) = 2 pi sqrt(c n / 3)`, NOT `c n / 6`. So the BTZ formula is **inconsistent with both K3 (kappa=c/3) and pure Virasoro (kappa=c/2)**. 

**This is a genuine bug.** Either:
(a) the formula should read `2 pi sqrt(c n / 6)` AND drop the `2 kappa n / 3` rewriting, OR
(b) the formula should read `S = 2 pi sqrt(2 kappa n / 3)` with kappa = c/4 (which is neither K3 nor Vir), OR
(c) the rewriting introduces a wrong factor.

The standard Cardy formula is `S = 2 pi sqrt(c n / 6)` (no kappa). The text's rewriting is erroneous. **Recommend:** verify the kappa-rewriting or remove it.

### 3.7. Hecke proof (Prop. symn-hecke-kappa, lines 644-673)

The proof says: "The vacuum contribution of T_N at q^0 is `sum_{ad=N} c_X(0,0) = sigma_0(N)*c_X(0,0)`, where sigma_0(N) is the number of divisors. However, the connected amplitude at order p^N is `N*kappa(X)/24` ... The divisor sum arises from the generating-function packaging and cancels in the connected extraction."

**Concern:** The "cancellation" is asserted, not computed. The Hecke generating function and the connected genus-1 extraction would benefit from an explicit example (e.g., N=2, N=3, N=6) showing the divisor-sum -> N collapse. Without the explicit cancellation, the proof is hand-wavy. **Mild AP14 / AP-CY24 risk:** docstring/proof gives a true CONCLUSION via UNVERIFIED INTERMEDIATE STEPS.

---

## Section 4. N=2 Superconformal audit (n2_superconformal.tex, 449 lines)

### 4.1. Numerical verification

| Claim | Value | Verified |
|-------|-------|----------|
| `kappa(N=2 SCA) = (k+4)/4` from Kazama-Suzuki | `3(k+2)/4 + 1/2 - (k/2+1) = (3k+6+2-2k-4)/4 = (k+4)/4` | **PASS** |
| `kappa = (6-c)/(2(3-c))` with c = 3k/(k+2) | substitute, gives `(k+4)/4` | **PASS** (sympy verified) |
| Complementarity `kappa(c) + kappa(6-c) = 1` | `(6-c)/(2(3-c)) + c/(2(c-3)) = 1` | **PASS** (sympy verified) |
| N=1 SVir complementarity sum = 41/4 | sympy verified | **PASS** |
| N=4 small SCA complementarity sum = -8 | sympy verified | **PASS** |

### 4.2. Comparison hierarchy table (rem:n2-susy-hierarchy, lines 425-449)

```
N | c       | kappa     | c'     | kappa+kappa' | self-dual
0 | c       | c/2       | 26-c   | 13           | c=13
1 | c       | (3c-2)/4  | 15-c   | 41/4         | c=15/2
2 | 3k/(k+2)| (k+4)/4   | 6-c    | 1            | c=3
4 | 6k      | 2k        | -c-24  | -8           | c=-12
```

I verified each row independently: sums and self-dual values are correct.

**Self-dual check for N=4:** complementarity `kappa(c) + kappa(-c-24) = -8` self-dual at `c = -c - 24`, i.e. `c = -12`. **PASS.**
**Self-dual for N=2:** `c = 6 - c` gives `c = 3`. At `c = 3`: `kappa = (6-3)/(2*0) = infty`. The text labels this as the self-dual point, BUT the value of kappa diverges — this needs a note. The text writes "Self-dual c=3" without acknowledging that the symmetric point is the FREE-FIELD limit where the algebra degenerates (kappa diverges). Mild ambiguity.

**Self-dual for N=1 SVir:** `c = 15 - c` gives `c = 15/2`. At c=15/2: kappa = (3*15/2 - 2)/4 = (45/2 - 2)/4 = (41/2)/4 = 41/8. The text claims kappa+kappa' = 41/4, which equals 2*(41/8). **PASS** (self-dual gives kappa = 41/8).

### 4.3. OPE convention check (Sec. 1, lines 117-161)

The OPE is in OPE-mode convention `a_{(n)}b = coefficient of (z-w)^{-(n+1)}` (line 130-131). Then `T_{(3)}T = c/2` corresponds to `T(z)T(w) ~ (c/2)/(z-w)^4 + ...`. **Standard.** Matches `T(z)T(w) ~ c/(2(z-w)^4) + 2T/(z-w)^2 + dT/(z-w)`.

`G^+_{(2)}G^- = c/3` corresponds to coefficient of `(z-w)^{-3}` in `G^+ G^-` OPE. **Convention-dependent:** in some conventions the leading coefficient is `2c/3` (e.g., Schwimmer-Seiberg, Kiritsis), in others `c/3` (depends on G normalization). The chapter is internally consistent: `J_{(1)}J = c/3` matches the U(1) at level c/3, and the spectral-flow shift `J -> J + (c/3) theta` (eq. 33) is consistent with the U(1) level.

**No bug found, but caution:** if the reader uses the Kac-Schoutens or Boucher-Friedan-Kent OPE conventions, `G^+_{(2)}G^- = 2c/3`. Recommend explicit "level" footnote.

### 4.4. Spectral flow notation (eq. n2-spectral-flow, lines 395-401)

```
sigma_theta(T) = T + theta*J + (c/6) theta^2,
sigma_theta(J) = J + (c/3) theta,
sigma_theta(G^pm) = G^pm_{pm theta}.
```

**Notation issue:** The standard spectral flow on modes is `L_n -> L_n + theta J_n + theta^2 (c/6) delta_{n,0}` and `J_n -> J_n + (c/3) theta delta_{n,0}`. As field equations, this is:
- `T(z) -> T(z) + (theta/z) J(z) + (theta^2 c/6) z^{-2}` (or equivalent forms with derivatives)
- `J(z) -> J(z) + (theta c/3) / z`

The text drops the `1/z` factors. This is "informal field-equation" shorthand — readable to experts but technically inexact. **Severity: cosmetic.** A footnote "schematic; precise mode-level statement..." would heal.

### 4.5. CE vs chiral bar gap claim (Prop. n2-koszulness, rem:n2-ce-chiral-gap, lines 281-332)

This is the chapter's main mathematical claim: at generic c, the N=2 SCA has `H^2_CE != 0` at conformal weight 3 (CE complex), but `H^2_bar = 0` (chiral bar complex Koszul). The proof invokes `Adamovic 1999` for free strong generation and PBW universality (Proposition pbw-universality) for the collapse. **Plausible, well-cited, but cannot independently verify without access to Adamovic.** Mark as cross-reference dependent.

### 4.6. Critical level k = -2 (line 75)

The chapter correctly notes `k = -2` is excluded (Sugawara undefined). **PASS.**

### 4.7. Trichotomy super-restriction (cross-volume from wave 5)

The chapter claims (lines 19-23): "The Virasoro subalgebra places it in class M (r_max = infty), while the U(1) current gives a class G channel (r_max = 2) and the fermionic G^+G^- pairing gives a class L channel (r_max = 3). The overall class is M, governed by the deepest channel."

**Cross-check against trichotomy:** if the trichotomy theorem (proved in earlier chapters) is bosonic-integer-weight-only (per the wave 5 BV finding), then applying it to fermionic channels via the G^+G^- pairing requires justification. The chapter labels the G-channel as "class L" — does the trichotomy classification (G/L/C/M) extend to fermionic generators? The chapter SHOULD have a remark explaining whether the trichotomy applies to mixed-statistics algebras.

**Mild concern (AP153/AP-CY46-style):** scope inflation if the trichotomy was proved bosonic and is applied here without a super-extension theorem.

---

## Section 5. AP-CY9/18/19/42 audit table

| AP | Trigger | Found in audited chapters? | Verdict |
|----|---------|----------------------------|---------|
| AP-CY9 | Jacobi discriminant constraint, c(-1) value, sequential D-fill | The K3 elliptic genus block in w_algebras_deep.tex line 5418 expands `2*phi_{0,1} = 2(y+10+y^-1) + (20 y^2 + 216 y + ...)q + ...` — discriminants implicit, not enumerated; phi_{0,1}(tau,0) constancy verified (sum_l c(1,l) = 0). Conclusion: c(D=-1) for `phi_{0,1}` = 1, for `2*phi_{0,1}` (= K3 elliptic genus) = 2. **Both consistent with AP-CY9.** | PASS |
| AP-CY18 | Lattice theta divergence; q^1 vs q^2 first correction | Leech theta correctly states "no norm-2 vectors" (line 1758). Numerically verified: q^1 coeff = 0, q^2 coeff = 196560 (Leech kissing number). | PASS |
| AP-CY19 | A-hat genus argument; (x/2)/sinh(x/2) vs x/sinh(x) | Searched all four files; no A-hat genus appears. | N/A |
| AP-CY42 | phi_{0,1} normalization c(-1)=1 vs c(-1)=2 | The text uses BOTH conventions correctly: phi_{0,1} alone (c(-1)=1) vs `2*phi_{0,1}` for K3 (c(-1)=2). Explicit factor-of-2 documented in w_algebras_deep.tex line 5413. | PASS |

---

## Section 6. Within-volume consistency

Cross-grep for kappa/eta^3/Mathieu/24*eta^3:
- lattice_foundations.tex line 1880-1893: invokes Zagier shadow of E_2* for Mathieu/umbral
- moonshine.tex: c=24 V^natural, kappa = 12, no mock-modular shadow claim
- symmetric_orbifolds.tex line 386-391: `prod(1-p^n)^{-24}` for Hilb^N(K3) generating series, identified with `1/Phi_{10}` (problematic, see 3.3)
- n2_superconformal.tex: no mock-modular content
- w_algebras_deep.tex line 5408-5427: K3 elliptic genus = `2*phi_{0,1}`, Mathieu coefficients `45+45'`, `231+231'`, mock modular form `H(tau) = sum A_n q^{n - 1/8}`

**Internal consistency:**
- The K3 mock-modular shadow `H(tau) = -2*q^{-1/8}*(1 - 45q - 231q^2 - ...)` from EOT 2010 is mentioned in w_algebras_deep.tex but NOT explicitly in lattice_foundations.tex's umbral discussion. The umbral discussion focuses on the QUASIMODULAR `E_2*` shadow.
- These are two DIFFERENT mock components: `H` is a weight-1/2 mock theta, while `E_2*` is a weight-2 quasimodular completion. Both arise in the K3 elliptic genus decomposition. The chapters could be tied together with a brief remark.

**No outright contradictions** detected. Mild incompleteness in the cross-references between mock components.

---

## Section 7. First-Principles Investigation Protocol (AP-CY61)

For each suspect claim in the audit, I asked: what is the GHOST OF A TRUE THEOREM behind it?

### 7.1. Ghost behind "kappa(K3 sigma) = c/3"

Literal claim in symmetric_orbifolds.tex line 469: "anomaly ratio for K3 is rho = 1/3, not 1/2, because K3 has both Virasoro and affine currents".

**True theorem this approximates:** the K3 sigma model has c = 6, but only TWO of the central charge units come from a "Virasoro c/2 channel" (the modular characteristic kappa = 2 = chi(O_K3) by Vol III thm:phi-k3-explicit). The other 4 units come from the rest of the Mukai-rank-24 structure that does NOT contribute to kappa via the c/2 mechanism. 

**Correct relationship:** kappa_ch(K3) = 2 (PROVED Vol III); c(K3 sigma) = 6 (standard). Ratio: kappa/c = 1/3, NOT a "rho = 1/3 anomaly ratio" but a CONSEQUENCE of `kappa_ch = chi(O)` for K3 (Vol III CY-D at d=2). 

**Healing:** rewrite line 469 as: "The modular characteristic kappa = 2N matches `kappa_ch(K3) = chi(O_{K3}) = 2` (Vol III thm:phi-k3-explicit) scaled by N for the symmetric product. The ratio kappa/c = 1/3 is NOT an independent anomaly coefficient but a consequence of the d=2 CY-D identity."

### 7.2. Ghost behind "BTZ entropy with kappa rewriting"

Literal claim in symmetric_orbifolds.tex line 482-484: `S_BH = 2 pi sqrt(c n / 6) = 2 pi sqrt(2 kappa n / 3)`.

**True theorem:** the Cardy formula `S_BH = 2 pi sqrt(c n / 6)` is correct. The kappa-rewriting `2 pi sqrt(2 kappa n / 3)` is FALSE for K3 (kappa = c/3) and FALSE for Vir (kappa = c/2). It would only hold for kappa = c/4 — a non-standard value.

**Correct relationship:** drop the kappa-rewriting OR insert the explicit ratio: `S_BH = 2 pi sqrt(c n / 6) = 2 pi sqrt((c/kappa) * kappa * n / 6)`. For K3 (c/kappa = 3): `S_BH = 2 pi sqrt(kappa n / 2)`. For Vir (c/kappa = 2): `S_BH = 2 pi sqrt(kappa n / 3)`.

### 7.3. Ghost behind "Phi_10 = 1/(prod (1-p^n)^{24})"

Literal claim in symmetric_orbifolds.tex line 386-391.

**True theorem:** Borcherds-Gritsenko-Nikulin: `1/Phi_{10}(tau, ω, z) = sum_{N,M,L} chi(M_{L,N,M}) e^{2 pi i (N tau + M ω + L z)}` where the LHS is the FULL Siegel cusp form and the RHS is the bivariate elliptic-genus generating series. The product `prod(1-p^n)^{-24}` = `eta(p)^{-24} * p^{-1}` is a SPECIALIZATION (z=0, q=0).

**Correct relationship:** `eta(p)^{-24} = (z=0, q=0)-section of 1/Phi_{10}`. Healing: explicitly state that this is a specialization, or write the full DMVV-Borcherds product.

### 7.4. Ghost behind "moonshine.tex:253-254 garbled"

Literal claim: `the universal Virasoro complementarity sum + \kappa(\mathrm{Vir}_{26-c}) = c/2 + (26-c)/2 = 13$, not~$0$).`

**True theorem:** the Virasoro complementarity `kappa(Vir_c) + kappa(Vir_{26-c}) = c/2 + (26-c)/2 = 13` is correct (Theorem complementarity). The text intended to point out that the SUM is 13, NOT 0 (contrasting with affine KM where the sum is 0 — the lattice-type complementarity).

**Healing:** restore the missing `(\kappa(\mathrm{Vir}_c)` opening clause and balance parens/dollars.

---

## Section 8. Three upgrade paths (steelmanned)

### 8.1. Strengthen moonshine via independent verification (AP-CY61 + Vol III protocol)

The 5 main theorems for V^natural (Table tab:moonshine-five-theorems) are all "Proved" or "Open". The chapter would benefit from a Vol III-style independent verification block: each theorem cited with `derived_from` and `verified_against` pointing to BOTH the bar-complex computation AND the direct moonshine reference (Borcherds, FLM, Conway-Norton). This converts the implicit cross-checks into a machine-checkable invariant per the Vol III independent_verification protocol.

### 8.2. Promote Niemeier shadow universality to a cleaner form

Theorem niemeier-shadow-universality is well-proved but the statement could be SHARPENED: state that the modular characteristic, shadow class, and critical discriminant collectively form a TOPOLOGICAL invariant (independent of the cocycle eps), with the only DISTINGUISHING data being the Niemeier theta-decomposition coefficient c_Delta. This unifies the Niemeier-vs-Monster discrimination story.

### 8.3. Convert the symmetric orbifold "BTZ" sloppiness into a precise theorem

Currently lines 478-490 give Cardy with a wrong kappa-rewriting. The strongest possible claim:
`S_BH = 2 pi sqrt(c n / 6); for K3-type symmetric orbifolds with c = 6N and kappa = 2N, this becomes S_BH = 2 pi sqrt(N n)` (a clean N-dependence, manifestly the AdS_3/CFT_2 holographic entropy).

This UPGRADES the existing weak claim into a precise large-N statement matching the AdS_3 Bekenstein-Hawking area law.

---

## Section 9. Punch list (prioritized for HEALING, not downgrade)

### Priority 1 (typographic/syntax bugs)

1. **moonshine.tex:253-254 LaTeX corruption.** Restore opening `(\kappa(\mathrm{Vir}_c)` and balance dollar-signs/parens. ESTIMATED COST: 1-line edit. (HIGH severity for prose readability, LOW for build correctness — currently passes build but renders gibberish.)

2. **symmetric_orbifolds.tex:170 trailing "see)."** with empty cross-reference. Add the intended reference or remove.

### Priority 2 (mathematical sloppiness — corrections-in-place, no theorem downgrades)

3. **symmetric_orbifolds.tex:482-484 BTZ kappa-rewriting**: the equation `2 pi sqrt(c n / 6) = 2 pi sqrt(2 kappa n / 3)` is dimensionally wrong (requires kappa = c/4, neither Vir nor K3 value). Replace with `2 pi sqrt(c n / 6)` and add corollary `for K3 Sym^N: S_BH = 2 pi sqrt(N n)`.

4. **symmetric_orbifolds.tex:386-391 Igusa Phi_{10} identification**: insert "the (q=0, z=0)-specialization of" before "the reciprocal of the Igusa cusp form Phi_{10}", OR write the full Borcherds-Gritsenko bivariate product to honestly identify with 1/Phi_{10}.

5. **symmetric_orbifolds.tex:469 "kappa = c/3" for K3**: substantiate with cite to Vol III thm:phi-k3-explicit or rederive as a consequence of `kappa_ch(K3) = chi(O_K3) = 2`.

### Priority 3 (presentation upgrades)

6. **n2_superconformal.tex:425-449 hierarchy table self-dual N=2 row**: add footnote noting that the c=3 self-dual point is the free-field limit where kappa diverges.

7. **n2_superconformal.tex:395-401 spectral flow as field eqs**: add footnote "schematic; precise statement is the mode-level shift L_n -> L_n + theta J_n + (c/6) theta^2 delta_{n,0}".

8. **lattice_foundations.tex:1880-1893 umbral remark**: cross-reference the Vol III Mathieu mock-shadow result `shadow(H_K3) = 24 eta^3` for completeness alongside the E_2* shadow.

### Priority 4 (independent verification protocol, per AP-CY61 / Vol III)

9. Apply the `@independent_verification` decorator pattern to the moonshine and N=2 SCA `@ClaimStatusProvedHere` theorems. The simplest entries: `prop:moonshine-kappa` (verify via FLM orbifold construction AND Niemeier discrimination AND Vir formula — three paths already in the proof), `prop:n2-kappa` (verify via Kazama-Suzuki AND direct OPE calculation AND the `kappa(c) + kappa(6-c) = 1` constraint).

### NO downgrades recommended

All `\ClaimStatusProvedHere` tags that I checked have proofs that survive scrutiny. The numerical content (Niemeier table, Monster decomposition, complementarity sums, Kazama-Suzuki coset arithmetic) is correct on every line I verified. The bugs found are typographic, dimensional rewriting, and identification scope — all healable IN PLACE.

---

## Sign-off

- **Numerical claims verified**: 14/14 (Leech theta, Niemeier root counts, Monster decomposition, complementarity sums for N=0,1,2,4 SCA, F_g amplitudes).
- **LaTeX corruption found**: 1 (moonshine.tex:253-254).
- **Mathematical sloppiness found**: 3 (BTZ kappa-rewriting, Phi_10 specialization, K3 c/3 ratio).
- **Trailing reference bug**: 1 (symmetric_orbifolds.tex:170).
- **AP-CY9, AP-CY18, AP-CY19, AP-CY42**: all PASS in the audited files.
- **Trichotomy super-restriction concern**: 1 (mild, n2_superconformal.tex G-channel class L assertion).
- **Recommendations**: 9 (8 healings, 1 protocol install). Zero downgrades.

The four chapters are LOAD-BEARING: the lattice/Niemeier/Monster discrimination is a foundation-stone of the Volume I shadow-classification programme, and the N=2 SCA is the showcase example of CE-vs-bar-Koszul gap. They should be repaired (Priority 1+2) and upgraded (Priority 3+4) BEFORE any further structural rectification.

## Cache write-back (per memory/feedback_cache_write_back.md)

If this audit becomes part of the cross-volume cache `appendices/first_principles_cache.md`:

| Wrong claim | Ghost theorem | Correct relationship | Type |
|-------------|---------------|---------------------|------|
| "BTZ S = 2 pi sqrt(c n / 6) = 2 pi sqrt(2 kappa n /3)" (sym_orb 482) | Cardy formula correct as-is; rewriting wrong | Rewriting requires kappa = c/4; K3 has kappa = c/3, Vir has kappa = c/2 | mechanism error |
| "prod(1-p^n)^{-24} = 1/Phi_{10}" (sym_orb 391) | Borcherds-Gritsenko-Nikulin: 1/Phi_{10} is bivariate; LHS is (q=0,z=0)-slice | Single-variable specialization, NOT the full Siegel form | scope/specialization |
| "kappa = c/3 for K3 because affine + Virasoro" (sym_orb 469) | kappa_ch(K3) = chi(O) = 2 (Vol III); c = 6; ratio is consequence | NOT an independent anomaly coefficient; follows from CY-D at d=2 | construction/narration |
| "moonshine.tex:253 garbled prose" | Vir complementarity: kappa(c)+kappa(26-c) = 13 | LaTeX syntax broken, mathematical content correct | typographic |
