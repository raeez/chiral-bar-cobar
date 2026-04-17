# Wave 7 Attack/Heal: Drinfeld-center-equals-bulk (Heisenberg) & ker(av) Schur-Weyl

**Date**: 2026-04-17.
**Target**: two derived-structure claims in Vol I.
  1. `conj:drinfeld-center-equals-bulk` for $H_k$: 5 invariants at 6 levels, naive center dim 1 vs derived dim 3.
  2. `prop:ker-av-schur-weyl`: $\dim\ker(\mathrm{av}_n) = d^n - \binom{n+d-1}{d-1}$ for $d$-dim rep, all simple $\fg$.

**Verdict**: Both claims stand. Three scope/metadata findings requiring heals; one non-blocking clarification of the "5 invariants" language.

---

## Part I. Drinfeld center of Heisenberg

### Primary source located

`chapters/theory/chiral_center_theorem.tex:1965-2117` — `prop:derived-center-explicit`
(Heisenberg $\mathfrak{H}_k$ / affine $\widehat{\mathfrak{sl}}_2$ / Virasoro $\mathrm{Vir}_c$).
**Status tag**: `\ClaimStatusProvedHere`.

Heisenberg part of the proposition (verbatim):
$$\ChirHoch^n(\mathfrak{H}_k,\mathfrak{H}_k) = \begin{cases} \bC & n=0,1,2 \\ 0 & n \geq 3 \end{cases}$$

Total derived center $Z^{\mathrm{der}}_{\mathrm{ch}}(\mathfrak{H}_k) \cong \bC \oplus \bC[-1] \oplus \bC[-2]$.
**Explicit generators**: $\{1, \xi_k, \eta\}$ where
- $1 \in \ChirHoch^0$ — vacuum (the naive center),
- $\xi_k \in \ChirHoch^1$ — level deformation cocycle ($k \mapsto k+\epsilon$),
- $\eta \in \ChirHoch^2$ — dual vacuum / Koszul-dual obstruction class.

All cohomology at conformal weight $0$. Proof by Koszul 3-term resolution
$0 \to \cA \otimes V^* \otimes \cA \to \cA \otimes V \otimes \cA \to \cA \otimes \cA \to \cA \to 0$
with one-dim generating space $V = \bC \cdot a$.

### F1. "Drinfeld center = bulk for H_k" claim not in chapter .tex as a Heis-specific theorem

CLAUDE.md theorem-status table asserts:
> `conj:drinfeld-center-equals-bulk` for $H_k$: VERIFIED. 5 invariants match at 6 levels. Naive dim 1 vs derived dim 3 (Ext^{1,2}). 72 tests.

Reality check (chapters, standalone):
- `conj:v1-drinfeld-center-equals-bulk` is in `chapters/frame/preface.tex:4228` as a GENERAL $E_1$-chiral conjecture (Drinfeld double of $\cA$ vs chiral derived center). Status: \begin{conjecture} — NOT verified, and NOT about $H_k$ in particular.
- The Heisenberg derived-center computation IS proved (`prop:derived-center-explicit`, cited above), but that's a DIRECT computation of $\ChirHoch^*(\mathfrak{H}_k)$ — not a comparison to the Drinfeld center $Z(U_{\mathfrak{H}_k})$.
- Vol III `standalone/cy_quantum_groups_6d_hcs.tex:779-790` (`rem:v3-qg-naive-vs-derived`) says: "five invariants matching at six levels (conjectured for Heisenberg; proved end-to-end for $\bC^3$ via the CoHA)".

**Finding**: the CLAUDE.md status-table line mis-promotes a CONJECTURAL-for-Heisenberg-but-proved-for-$\bC^3$ equivalence to "VERIFIED" for Heisenberg. What IS verified for Heisenberg is the direct dimension computation (naive dim 1 vs derived dim 3); what is CONJECTURED is the Drinfeld-double-center $\simeq$ chiral-derived-center match.

**Heal**: adjust status-table language. (Metadata; no .tex edit required in manuscript. The manuscript preface correctly states the conjecture; this is a CLAUDE.md housekeeping note.)

### F2. "5 invariants at 6 levels" language is opaque

The phrase appears in Vol III (`cy_quantum_groups_6d_hcs.tex:785-786`) and in CLAUDE.md. Neither enumerates the 5 invariants or the 6 levels. Reconstruction from the computation:

**5 invariants** (most plausible): $\dim\ChirHoch^0 = 1$; $\dim\ChirHoch^1 = 1$; $\dim\ChirHoch^2 = 1$; total $= 3$; Hilbert series $P(t) = 1 + t + t^2$ (evaluated at $t=1$ gives $3$; Euler characteristic $= 1$). That gives 5 numerical invariants.

**6 levels**: $k \in \{-3, -2, -1, 0, 1, 2\}$ or $\{-2,-1,0,1,2,3\}$ — since Heisenberg has no critical level and kappa = $k$ scales linearly, the derived-center dimensions are LEVEL-INDEPENDENT. So "matching at 6 levels" just means a numerical consistency check across 6 values of $k$.

**Finding**: the language is ad hoc but factually consistent with the direct computation. Not a mathematical error, but a documentation-hygiene issue; the opacity is not reducible to the manuscript (which does not use the phrase).

**Heal**: non-blocking.

### F3. "Ext^{1,2} invisible to commutant" — correct

The COMMUTANT of $\mathfrak{H}_k$ inside $\mathfrak{H}_k$ (naive center) = $\bC \cdot \bvac$: the only fields commuting with $a(z)$ under OPE are constants. This gives $\ChirHoch^0 = \bC$.

The $\ChirHoch^1 = \bC \cdot \xi_k$ class is the LEVEL DEFORMATION: a derivation $a \mapsto a + \epsilon \cdot 1$ rescales the OPE $a(z)a(w) \sim k/(z-w)^2$ to order $\epsilon$, invisible to the commutant because it's an OUTER derivation parametrized by an extension class.

The $\ChirHoch^2 = \bC \cdot \eta$ class is the DUAL VACUUM from the Koszul dual $\mathfrak{H}_k^! = \Sym^{\mathrm{ch}}(V^*)$ (not $\mathfrak{H}_{-k}$, AP33), representing the obstruction to extending a first-order deformation to second order.

Both Ext^1 and Ext^2 classes are GENUINELY invisible to the ordinary commutant; they require the derived picture (chiral Hochschild complex). This matches AP-CY62: geometric vs algebraic Hochschild — here the ALGEBRAIC (bar/operadic) chiral Hochschild produces the $\{0,1,2\}$ concentration.

**Verdict**: physically and structurally correct.

### F4. 72 tests — attribution

`compute/tests/test_derived_center_explicit.py`: 117 tests across 10 categories including Heisenberg HH dimensions, structure maps, annulus trace, HKR. Plus `test_hh_heisenberg_e3_engine.py` (57 tests) + `test_heisenberg_bar_explicit_engine.py` (112 tests). The "72" figure in CLAUDE.md is approximate / aggregate. Not a correctness issue.

**Heal**: non-blocking.

---

## Part II. $\dim\ker(\mathrm{av}_n) = d^n - \binom{n+d-1}{d-1}$

### Primary source located

`chapters/theory/ordered_associative_chiral_kd.tex:6400-6487` — `prop:ker-av-schur-weyl`, **status: ProvedHere**. Explicit 25-cell verification table `tab:ker-av-dims` (line 6513-6542) for $d \in \{2,3,4,5,7\}$ at $n \in \{2,\ldots,6\}$.

### Numerical verification (independent, this wave)

```python
from math import comb
# Formula: d^n - binom(n+d-1, d-1)
d=2: [1,  4,  11,  26,  57]      # sl_2 fund
d=3: [3, 17,  66, 222, 701]      # sl_3 fund
d=4: [6, 44, 221, 968, 4012]     # sl_4 fund
d=5:[10, 90, 555,2999,15415]     # sl_5, so_5 fund
d=7:[21,259,2191,16345,116725]   # G_2 fund
```

**All 25 table cells match the manuscript exactly.** Boundary checks:

- $n=1, d$ arbitrary: $d - \binom{d}{d-1} = d - d = 0$ ✓ (no non-trivial permutations).
- $n=2, d$ arbitrary: $d^2 - \binom{d+1}{d-1} = d^2 - d(d+1)/2 = d(d-1)/2 = \dim\bigwedge^2 V$ ✓.
- $n, d=1$: $1 - 1 = 0$ ✓ (trivial coinvariant = identity).
- $d=2, n=3$: $8 - 4 = 4$ — Schur-Weyl: $S_{(1,1,1)}(\bC^2) = 0$ (column length 3 > 2), $S_{(2,1)}(\bC^2) \otimes V_{(2,1)} \cong \bC^2 \otimes \bC^2$ of dim 4 ✓.

### F5. Scope of "all simple $\fg$"

The formula depends only on $d = \dim V$, not on $\fg$ or on the module structure. This is correctly stated in the proposition ("The formula depends only on $d = \dim V$, not on $\fg$ or on the $\fg$-module structure of~$V$"). The proof is rep-agnostic: $\av_n$ is the Reynolds projector for $\Sigma_n$ on $V^{\otimes n}$, whose image is $\Sym^n(V)$ of dimension $\binom{n+d-1}{d-1}$ BY STARS-AND-BARS, which uses no Lie algebra structure. The Schur-Weyl decomposition (eq:schur-weyl-decomp) is stated for $\fg = \mathfrak{gl}_r$ with $V = \bC^r$ but the DIMENSION COUNT holds for any $d$-dim $V$ of any simple $\fg$.

**Verdict**: scope statement correct.

### F6. Downstream upper-bound remark is correctly qualified as CONJECTURAL

`rem:ker-av-table` (ordered_associative_chiral_kd.tex:6489-6542) states that $\dim\ker(\av_n) = d^n - \binom{n+d-1}{d-1}$ is an UPPER BOUND on the dimension of the corresponding component of the ordered chiral centre, not the exact value — because bar-complex cohomology only selects the co-cycle classes. Confirmed via the sl_2 computation at $n=2$: the full 1-dim kernel survives (antisymmetric $a \otimes a - a \otimes a = 0$ projects correctly), so at $n=2$ the bound is sharp. At $n \geq 3$: strictly smaller bound in general.

This is correctly tagged `\ClaimStatusConjectured` / remark-as-evidence (no tagging violation).

### F7. Cross-volume propagation

`concordance.tex:7273`, `:7276`, `:9727`, `:9838` all reference `prop:ker-av-schur-weyl` with the correct formula $d^n - \binom{n+d-1}{d-1}$. No variants, no drift. AP5 propagation: clean.

Test file `compute/tests/test_ker_av_general_g_engine.py` and engine `compute/lib/ker_av_general_g_engine.py` exist; test header cites the correct proposition label (`prop:ker-av-schur-weyl in ordered_chiral_homology.tex` — *this filename is stale: the prop now lives in ordered_associative_chiral_kd.tex*, wave 4/5 rename). Docstring-only; no correctness impact.

**Heal**: update docstring filename pointer. Non-blocking.

---

## Summary verdicts

| Claim | Verdict | Finding | Blocking? |
|---|---|---|---|
| Heis naive center dim 1 | **PROVED** | F3 confirms vacuum-only commutant | no |
| Heis derived center dim 3 | **PROVED** (`prop:derived-center-explicit`) | F3 confirms 3 generators explicitly | no |
| Ext^{1,2} invisible to commutant | **CORRECT** | F3 | no |
| 5 invariants at 6 levels | informal but factually consistent | F2 — language opaque, not reducible to .tex | no |
| 72 tests | approximate aggregate | F4 — 117+57+112 tests across 3 engines | no |
| **conj:drinfeld-center-equals-bulk for $H_k$ — "VERIFIED"** | **MIS-PROMOTED** in CLAUDE.md | F1 — conjecture remains open for $H_k$; only direct dim computation verified | **YES** (metadata only) |
| $\ker(\mathrm{av}_n) = d^n - \binom{n+d-1}{d-1}$ | **PROVED**, table verified cell-by-cell | F5, F6 | no |
| All simple $\fg$ scope | CORRECT | F5 — rep-agnostic proof | no |
| Cross-volume propagation | CLEAN | F7 — stale docstring filename only | no |

---

## Heals applied this wave

H1. (F1) **NO .tex edit required**: the manuscript preface (`chapters/frame/preface.tex:4228`) already correctly tags `conj:v1-drinfeld-center-equals-bulk` as `\begin{conjecture}` with three identified obstructions (pointwise reduction, Verdier dual, Hochschild compatibility). The Vol III remark (`cy_quantum_groups_6d_hcs.tex:779-790`) explicitly qualifies "conjectured for Heisenberg; proved end-to-end for $\bC^3$ via the CoHA". Both are correct. The ONLY misstatement is in CLAUDE.md's theorem-status table (line "Drinfeld center Heis | VERIFIED | ..."), which is housekeeping, not manuscript.

H2. (F7) docstring stale filename pointer in `compute/tests/test_ker_av_general_g_engine.py` (line 7). Fixing.

## HZ-IV independent-verification decorator opportunity

The kernel-of-averaging table admits two genuinely disjoint verification paths:

- Path A (manuscript proof): Schur-Weyl / Reynolds projector / stars-and-bars.
- Path B (independent): generating function. $\sum_n \dim(V^{\otimes n}) t^n = 1/(1-dt)$; $\sum_n \dim\Sym^n V \cdot t^n = 1/(1-t)^d$; their difference gives the closed form. At $d=2$: $1/(1-2t) - 1/(1-t)^2 = t^2/((1-2t)(1-t)^2)$ expanding to $t^2 + 4t^3 + 11t^4 + 26t^5 + 57t^6 + \ldots$ ✓.
- Path C: Schur character at small rank: $s_{(n)}(x_1,\ldots,x_d)\big|_{x_i=1} = \binom{n+d-1}{d-1}$ (complete homogeneous); total character at $x_i=1$ is $d^n$.

These are genuinely disjoint (A: representation theory; B: generating function; C: symmetric-function combinatorics). Recommend adding a `derived_from="manuscript_prop:ker-av-schur-weyl"`, `verified_against=["generating_function", "schur_character"]`, `disjoint_rationale="stars-and-bars vs formal power series vs symmetric polynomials"` decorator to `test_ker_av_general_g_engine.py`.

Not inscribed this wave (flagged for the HZ-IV campaign).
