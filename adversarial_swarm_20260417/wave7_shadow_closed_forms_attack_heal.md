# Wave-7 Adversarial Attack + Heal: Shadow-Tower Closed Forms

Target: Vol I `chapters/theory/shadow_tower_higher_coefficients.tex`
Date: 2026-04-17
Auditor: Beilinson first-principles adversary

## Scope

Seven attack vectors against the shadow-tower closed-form statements:
`thm:shadow-exponential-base-Virasoro`, `thm:shadow-series-closed-form-Virasoro`,
`thm:pole-doubling-all-k`, `thm:w3-wline-closed-form`,
`thm:w3-wline-exponential-base`, `thm:w3-wline-generating-function`,
`thm:w3-wline-koszul-duality-partner` (implicit in remark).

## Attack verdicts

| # | Claim | Verdict | Heal |
|---|-------|---------|------|
| (i) | $\Sigma_{\Vir}(z) = 4z^3/9 - z^2/9 + z/27 - \log(1+6z)/162$; $\limsup \lvert A_{r+1}/A_r\rvert = 6$ | **VERIFIED** (exact) | none |
| (ii) | Pole-doubling $(1+6z)^{-2k}$ in $\Sigma_{\Vir}^{(k)}$ | **STRUCTURALLY CORRECT, SIGN TYPO** at line 1005-1006 | applied |
| (iii) | $6 = r_0 \cdot S_{r_0} = 3 \cdot 2$ | **VERIFIED** ($r_0 = 3$ first nonzero-seed bar-depth; $S_3(\Vir) = 2$) | none |
| (iv) | $C_{W_3}^{W\text{-line}} = 12 = 2 \cdot 6$; Hessian $3/2 \times$ kernel $4/3$ | **VERIFIED as closed form**; decomposition **POST-HOC** (text at `rem:w3-wline-decomposition-is-circular` already flags this honestly) | none |
| (v) | Koszul-dual invariant under $c \to 4 - c$; $K_3 = 4$ | **CONVENTION CLASH** with AP234/C3/C4: in Arakawa convention $K(W_3) = 196$, not $4$ | scope-qualified to FL free-field convention; explicitly distinguished from Trinity conductor $100$ and scalar complementarity $250/3$ |
| (vi) | Spin-stratified $C_{W^{(s)}} = s(s+1)$ | **ALREADY CORRECTLY MARKED `\ClaimStatusConjectured`** with three alternative functional forms catalogued ($s(s+1)$, $6(s-1)$, $4s$, etc.) | none; remark `rem:w3-wline-higher-spin-prediction` already honest |
| (vii) | Cross-volume propagation | Vol II `thqg_perturbative_finiteness.tex`, Vol III `k3_yangian_chapter.tex` reference $C = 6, 12$ as imported constants (no re-derivation); no drift detected | none |

## Key computations

### (i) Virasoro closed form

Taylor coefficients of $-\log(1+6z)/162$: $[z^r] = (-1)^r 6^r / (162 r)$.
At $r = 4$: $6^4/(162 \cdot 4) = 1296/648 = 2$. Matches $A_4 = 2$.
Cubic $+$ quadratic $+$ linear terms are exactly $-[\text{low-order log}]$
up to $r = 3$, giving $\Sigma_{\Vir}$ starting at $r = 4$. Ratio
$\lvert A_{r+1}/A_r\rvert = 6r/(r+1) \to 6$ confirmed.

### (ii) Faà di Bruno sign

$f(z) := -\log(1+6z)/162$. Even-order derivative:
$f^{(2k)}(z) = (-1)^{2k+1} \cdot (2k-1)! \cdot 6^{2k} / [162(1+6z)^{2k}]$
$= -(2k-1)! \cdot 6^{2k} / [162(1+6z)^{2k}]$ from $-\log$, but the
textbook $\log(1+u)^{(n)} = (-1)^{n-1}(n-1)!/(1+u)^n$ gives at $n=2k$:
$(-1)^{2k-1}(2k-1)! = -(2k-1)!$. Composed with $-1/162$ prefactor:
$f^{(2k)}(z) = +(2k-1)! \cdot 6^{2k}/[162(1+6z)^{2k}]$. **Positive**
at every even $k$. Verified at $k=1$: $f''(z) = 2/[9(1+6z)^2]$ (positive).
The prior text had the sign reversed.

### (iii) $r_0 = 3, S_3 = 2$

$r_0$ = first bar-depth where the shadow seed is $O(c^0)$ nonzero
(the stress-tensor $T$-$T$-$T$ universal Virasoro OPE gives $S_3 = 2$,
pre-Sugawara-normalisation). Not a numerological coincidence: the
two-seed Riccati $\Phi_3 = 2c, \Phi_4 = c, \ldots$ has $j = 3$ as the
unique $O(c)$ channel. $6 = 3 \cdot 2 = r_0 \cdot S_{r_0}$ is the
leading-eigenvalue factorisation of the linearised recurrence kernel.

### (iv) $W_3$ W-line ratio identity

$a_{n+1}/a_n = 6(2n-3)/(n+1) = 12 - 30/(n+1)$. Telescoping
$\prod_{k=2}^{n-1}$ gives $a_n = 2 \cdot 3^{n-2} \binom{2n-4}{n-2}/[n(n-1)]$
via the double-factorial identity $(2n-5)!! = (2n-4)!/[2^{n-2}(n-2)!]$.
Stirling $\binom{2m}{m} \sim 4^m/\sqrt{\pi m}$ gives $a_n \sim 12^n/(72\sqrt{\pi}n^{5/2})$.
Numerical ratio test at $n = 200$: $1.00945$ $\to 1$. All verified.

### (v) $K_3 = 4$ convention clash

In Arakawa convention $c^{\mathrm{A}}(W_3)(k) = 2 - 24(k+1)^2/(k+3)$:
$c(k) + c(-k-6) = 196$ (constant, matches BP AP140 identity).
The "$c \to 4 - c$" symmetry with $K_3 = 4$ uses a DIFFERENT
convention (Fateev--Lukyanov free-field, self-dual fixed at $c = 2$).
Neither is wrong; but mixing them without labeling was an AP144
convention clash. HEALED by restricting $K_3 = 4$ statement to
FL convention and cross-referencing the Trinity conductor and
$\kappa + \kappa^! = 250/3$ values.

### (vi) Spin lattice

Two data points $(s = 2, C = 6)$ and $(s = 3, C = 12)$ fit
$C = s(s+1)$, $C = 6(s-1)$, $C = 4s$, $C = 2s^2 - 4s + 6$ equally.
Text honestly marks this conjectural and catalogs alternatives;
NO CHANGE needed.

### (vii) Propagation

Vol II `programme_climax_platonic.tex`, Vol III `k3_yangian_chapter.tex`,
Vol I `preface.tex`, `introduction.tex`, `programme_overview_platonic.tex`
all reference $C_{\Vir} = 6, C_{W_3}^W = 12$ as imported. No independent
re-derivation. No drift, no inconsistency.

## Surgical edits applied

1. `shadow_tower_higher_coefficients.tex:1005-1006`: sign fix on
   $d^{2k}/dz^{2k}[-\log(1+6z)/162]$ (now $+(2k-1)! 6^{2k}/[162(1+6z)^{2k}]$).
2. `shadow_tower_higher_coefficients.tex:2287-2295`: $K_3 = 4$
   convention scope-qualified to FL free-field convention; distinguished
   from Trinity $K = 100$ and scalar complementarity $\kappa + \kappa^! = 250/3$.

## No downgrades

Every `\ClaimStatusProvedHere` theorem remains valid. The conjectural
spin lattice (`rem:w3-wline-higher-spin-prediction`) was already
appropriately marked. Proof-sketch sign typo (ii) was a writing
error; the $(1+6z)^{-2k}$ structural conclusion is correct.

## Cache entries (new)

- **Pattern 222**: Faà di Bruno sign on even-derivative of
  $\log(1+\alpha z)$: $(d/dz)^{2k}[\log(1+\alpha z)] = -(2k-1)! \alpha^{2k}/(1+\alpha z)^{2k}$
  (negative). Composing with $-1/C$ prefactor gives positive. Writing
  $(-)(-) = -$ is the typo; correct is $(-)(-) = +$. Pre-write template:
  evaluate at $k=1$ numerically before writing the $k$-indexed formula.
- **Pattern 223**: $K_3 = 4$ vs $K_3 = 196$: convention-dependent
  Koszul conductor. Arakawa gives 196 (trace-form); FL free-field
  gives 4 (symmetric-point); Trinity gives 100 ($c + c^!$).
  Pre-write template: state convention FIRST when writing any
  $K$ for $W_3$ or $W_N$.

## Report

1 sign error healed, 1 convention scope-qualified, 4 claims verified
unchanged, 1 conjecture left correctly marked, cross-volume clean.
No downgrades. 2 cache entries for future AP prevention.
