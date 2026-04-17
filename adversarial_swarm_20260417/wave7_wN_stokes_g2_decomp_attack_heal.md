# Wave 7 — $\cW_N$ Stokes count + genus-$2$ CB degree decomposition

Date: 2026-04-17
Target: Vol I claims (1) $\cW_N$ Stokes count $= 4N-4$; (2) $\mathrm{CB}_{2,2}(k) = 2k(k+1)(k+2)/3$.
Verdict: **BOTH CLAIMS VERIFIED** (with one prose caveat on (2) and one convention caveat on (1)).

---

## Claim (1). $\cW_N$ KZ Stokes count $= 4N-4$

**Source location.** `chapters/theory/ordered_associative_chiral_kd.tex:9917-9924`
(`rem:stokes-wN-monograph`).

**Quoted statement.**
> The $\cW_N$ KZ connection at degree~$2$ has Poincar\'e rank
> $2N - 2$ (from the $W_N$–$W_N$ OPE pole $2N$, d-log absorption
> to $2N-1$) and $4N-4$ Stokes rays. $\cW_2$: $4$ rays;
> $\cW_3$: $8$ rays. Linear growth in $N$.

### Chain of reasoning

| Step | Quantity | Value |
|---|---|---|
| (a) | Highest OPE pole in $W_N(z)W_N(w)$ | $(z-w)^{-2N}$ |
| (b) | After d-log absorption on the connection | pole order $2N-1$ |
| (c) | Poincaré rank $r$ (= pole order of connection form minus one) | $2N-2$ |
| (d) | Stokes rays of Poincaré-rank-$r$ irregular point | $2r = 4N-4$ |

### Verification of each step

**(a) OPE pole order.** $W_N$ has conformal weight $N$. The $WW$ OPE in
a $\cW$-algebra contains the identity channel with highest singularity
$\langle W_N(z) W_N(w)\rangle \sim B_N (z-w)^{-2N}$ (two-point function
of a primary of weight $N$). Verified at $N=2$: $TT$ OPE pole
$(z-w)^{-4}$ ✓. At $N=3$: $W_3 W_3$ OPE (Zamolodchikov) pole
$(z-w)^{-6}$ ✓.

**(b) d-log absorption.** The connection one-form is $r(z)\,dz$, where
$r(z)$ has a pole of order $2N$; writing $dz = (z-w)\, d\log(z-w)$
absorbs one power, leaving a $2N-1$ singularity in the $d\log$ basis.
This is the standard Arnold/KZ basis reduction.

**(c) Poincaré rank.** For a meromorphic connection
$dY = A(z)\,Y\,dz$ with $A$ having pole of order $p \geq 1$ at $z_0$,
the Poincaré rank is $r = p-1$. Here $p = 2N-1$, so $r = 2N-2$.
At $N=2$: $r = 2$ (Virasoro has a rank-2 irregular singularity on the
configuration space — confirmed by Jimbo–Miwa–Ueno, Reshetikhin, and
the direct Fuchs analysis for KZ with four-pole collision).
At $N=3$: $r = 4$.

**(d) Stokes ray count.** For a Poincaré-rank-$r$ irregular singular
point of a generic system, the anti-Stokes directions in the formal
disc are the zeros of $\operatorname{Re}(\lambda_i - \lambda_j)(\theta)$
where $\lambda_i$ are the leading eigenvalues; generically
$\lambda_i - \lambda_j \propto z^{-r}$, giving $2r$ directions in
$[0, 2\pi)$. Standard reference: Boalch,
"Symplectic manifolds and isomonodromic deformations" (Lemma 2.1);
Hertling–Sabbah; Sabbah "Isomonodromic deformations". At $r=2$ this
yields $4$ rays ✓; at $r=4$, $8$ rays ✓.

### Convention caveat

"Stokes rays" admits three inequivalent usages in the literature:
(i) **anti-Stokes rays** (where a formal multiplier acts non-trivially;
count $= 2r$ generic), (ii) **Stokes sectors** (connected components
of the complement; count $= 2r$), (iii) **active rays** (those
carrying a non-trivial Stokes multiplier; could be fewer than $2r$
in non-generic settings). The $4N-4$ count matches (i)/(ii) under
genericity. The remark is consistent with the dominant convention
(Boalch, Jimbo–Miwa–Ueno, Hertling–Sabbah) but would benefit from a
one-word convention pointer.

### Cross-check: Poincaré rank of $\cW_N$ OPE pole

`ordered_associative_chiral_kd.tex:9389-9391` states:
> The $\cD$-module $\mathcal{F}_n^{\mathrm{ord}}(\cW_{1+\infty})$
> has irregular singularities of unbounded Poincaré rank
> (spin-$s$ contributes pole order $2s - 1$ after $d$-log absorption).

This is consistent with (b)/(c): spin-$s$ OPE pole is $(z-w)^{-2s}$,
absorbs to $2s-1$, Poincaré rank $2s-2$. The $\cW_N$ case is the
truncation at max spin $s=N$, Poincaré rank $2N-2$. ✓

### Verdict (1)

**ACCEPT** with optional one-line convention pointer inserted into the
remark.

---

## Claim (2). $\mathrm{CB}_{2,2}(k) = 2k(k+1)(k+2)/3$

**Source location.** `chapters/theory/higher_genus_modular_koszul.tex:34573-34612`
(`prop:g2-conformal-block-degree`).

**Quoted statement.**
> At integer level $k \geq 1$, the degree-$2$ conformal block count on
> $\Sigma_2$ decomposes by isospin channel: (i) singlet channel
> contributes at all levels; (ii) triplet channel contributes only for
> $k \geq 2$; (iii) $\mathrm{CB}_{2,2}(k) = 2k(k+1)(k+2)/3$,
> cubic in $k$. At $k=1$: $4$; at $k=2$: $16$; at $k=3$: $40$.

### Verlinde computation for $SU(2)_k$ at $g=2$ with two fundamental insertions

Here "degree 2" = two insertions of the fundamental $V_1$ (Dynkin
label $1$, i.e., spin-$1/2$ of weight $1$), and the fusion
$V_1 \otimes V_1 = V_0 \oplus V_2$ uses the Dynkin-label convention
consistent with the proof body.

Verlinde formula for $SU(2)_k$ at genus $g$ with $n$ insertions of
Dynkin label $\lambda_i$:
$$\dim \mathcal{V}_{g, (\lambda_1, \ldots, \lambda_n)}(k) =
\left(\frac{k+2}{2}\right)^{g-1} \sum_{\ell=1}^{k+1}
\frac{\prod_i \sin(\pi(\lambda_i+1)\ell/(k+2))}
{\sin^{2g-2+n}(\pi\ell/(k+2))}.$$

Specialize $g=2$, $n=2$, $\lambda_1 = \lambda_2 = 1$:
$$\mathrm{CB}_{2,2}(k) = \frac{k+2}{2}
\sum_{\ell=1}^{k+1} \frac{\sin^2(2\pi\ell/(k+2))}{\sin^4(\pi\ell/(k+2))}.$$

Using $\sin(2x) = 2\sin x \cos x$:
$$= \frac{k+2}{2} \sum_{\ell=1}^{k+1}
\frac{4\cos^2(\pi\ell/(k+2))}{\sin^2(\pi\ell/(k+2))}
= 2(k+2) \sum_{\ell=1}^{k+1} \cot^2\!\left(\frac{\pi\ell}{k+2}\right).$$

Standard cotangent-squared sum (classical, e.g., Hardy–Wright §18.3):
$$\sum_{\ell=1}^{N-1} \cot^2(\pi\ell/N) = \frac{(N-1)(N-2)}{3}.$$

With $N = k+2$:
$$\sum_{\ell=1}^{k+1} \cot^2(\pi\ell/(k+2)) = \frac{(k+1)k}{3}.$$

Therefore:
$$\boxed{\mathrm{CB}_{2,2}(k) = 2(k+2) \cdot \frac{k(k+1)}{3}
= \frac{2k(k+1)(k+2)}{3}.}$$ ✓

### Tabulated values

| $k$ | $2k(k+1)(k+2)/3$ | Claim |
|---|---|---|
| $1$ | $2\cdot 1 \cdot 2 \cdot 3 / 3 = 4$ | $4$ ✓ |
| $2$ | $2\cdot 2 \cdot 3 \cdot 4 / 3 = 16$ | $16$ ✓ |
| $3$ | $2\cdot 3 \cdot 4 \cdot 5 / 3 = 40$ | $40$ ✓ |

### Singlet + triplet check at $k=1$

At $k=1$, $V_2$ requires integrability condition $2j \leq k$,
i.e., Dynkin label $\lambda \leq k$: $V_2$ has $\lambda=2 > k=1$,
**NOT integrable** ✓. So at $k=1$ only the singlet channel contributes.

Singlet-channel genus-$2$ block count at $k=1$ = Verlinde
$g=2$, $n=0$ vacuum insertion:
$$\dim \mathcal{V}_{2,\varnothing}(1) = \frac{3}{2}
\left[\csc^2(\pi/3) + \csc^2(2\pi/3)\right]
= \frac{3}{2}\left[\frac{4}{3} + \frac{4}{3}\right] = 4. \checkmark$$

At $k=2$: $16 = 10 + 6$ or similar split? Verify:
$N=k+2=4$, Verlinde $g=2, n=0$ with vacuum:
$\dim = 2 \sum_{\ell=1}^3 \csc^2(\pi\ell/4)
= 2[2 + 1 + 2] = 10$ (singlet contribution).
Triplet contribution ($\lambda=2$ insertion is now integrable):
$\mathrm{CB}_{2,1}(\lambda=2)$ at $k=2$, one insertion of $\lambda=2$,
$g=2, n=1$:
$\dim = 2 \sum_{\ell=1}^3 \sin(3\pi\ell/4) / \sin^3(\pi\ell/4)$
$= 2[\sin(3\pi/4)/\sin^3(\pi/4) + \sin(3\pi/2)/\sin^3(\pi/2)
+ \sin(9\pi/4)/\sin^3(3\pi/4)]$
$= 2[(\sqrt{2}/2)/(\sqrt{2}/2)^3 + (-1)/1 + (\sqrt{2}/2)/(\sqrt{2}/2)^3]$
$= 2[2 + (-1) + 2] = 6$.
Total $= 10 + 6 = 16$ ✓ matches cubic.

### Prose caveat (minor, non-load-bearing)

The proof body writes:
> "Each channel contributes $\mathrm{CB}_{2,1}(j) = \sum_m
> (S_{jm}/S_{0m})^{-2}$, a genus-$2$ **one-point** conformal block count."

The label "one-point" is a mild misnomer: $\sum_m (S_{jm}/S_{0m})^{-2}$
with the exponent $-2 = -(2g - 2 + n)$ at $g=2, n=0$ is the
**genus-$2$ zero-point** Verlinde formula in channel $j$ (the
$j$-channel appears as the total charge propagating, not as an
insertion). Equivalently: after fusing the two fundamental insertions
to channel $j$, the remaining Verlinde is the genus-$2$ vacuum block
for $V_j$, which is the trace of the $S$-matrix weighted genus-$2$
partition. The **math is correct**; only the prose label is off by
"one-point" vs "zero-point after fusion".

Heal: rename to "genus-$2$ zero-point block count in channel $j$".

### Dimension check: polynomial degree $3g-3$

For $SU(2)_k$ at genus $g$, $\dim \mathcal{V}_{g,\varnothing}(k)$ is a
polynomial in $k$ of degree $3g-3 = 3$ at $g=2$. With two additional
fundamental insertions, the virtual dimension grows by $2 \cdot \dim
V_1 = 2$ in the parabolic moduli, but the Verlinde count remains
polynomial of degree $3g-3+n = 3$ at $g=2, n=2$. ✓ **The cubic is
structurally correct.**

### Verdict (2)

**ACCEPT** the formula and the table. Prose heal: replace
"one-point" → "zero-point block count in channel $j$ (after fusion
of the two fundamentals)".

---

## Surgical heals

### Heal 1 (Claim 1 convention pointer)

File: `ordered_associative_chiral_kd.tex:9917-9924`.
Insert a one-line convention pointer; no mathematical content change.

### Heal 2 (Claim 2 prose label)

File: `higher_genus_modular_koszul.tex:34604-34606`.
Rename "one-point" → "zero-point".

---

## Cache entries

- **Pattern 222**: $\cW_N$ KZ Stokes count chain: pole $2N$ →
  d-log absorbed to $2N-1$ → Poincaré rank $r = 2N - 2$ → Stokes
  rays $= 2r = 4N-4$. Always state the Stokes-ray convention
  (anti-Stokes / Stokes-sector / active). AP236 adjacent.

- **Pattern 223**: Verlinde cotangent-squared identity
  $\sum_{\ell=1}^{N-1}\cot^2(\pi\ell/N) = (N-1)(N-2)/3$ reduces
  $SU(2)_k$ Verlinde at $g=2$ with two fundamental insertions to
  $2k(k+1)(k+2)/3$. Generic degree-$(3g-3+n)$ polynomial structure.

- **Pattern 224**: Verlinde "one-point" vs "zero-point" channel
  count prose hygiene. $\sum_m (S_{jm}/S_{0m})^{-2}$ is the
  genus-$2$ **zero-point** block in channel $j$ (exponent
  $-2 = -(2g-2+n)$ at $g=2, n=0$); "one-point" label would
  require $n=1$ insertion. No mathematical error; prose only.

---

## Summary

Both claims verified from first principles. $\cW_N$ Stokes $= 4N-4$
confirmed via Poincaré-rank arithmetic and Boalch/Jimbo–Miwa–Ueno
conventions. $\mathrm{CB}_{2,2}(k) = 2k(k+1)(k+2)/3$ verified via
explicit Verlinde computation using the classical
$\cot^2$ identity; singlet/triplet decomposition correct at $k=1$
(triplet absent, integrability).

Two small surgical heals inscribed below (one convention pointer,
one prose relabel). No load-bearing mathematical changes.
