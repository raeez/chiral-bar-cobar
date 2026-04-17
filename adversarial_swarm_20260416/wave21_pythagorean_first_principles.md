# The Pythagorean identity 24² = (−16)² + 320 is the (p,q) ↦ (p+q)²−(p−q)² identity

**Date:** 2026-04-16. **Author:** Raeez Lorgat. **Wave:** post-V53.

## Statement

For any super-signature $(p,q) \in \mathbb{Z}_{\geq 0}^2$:

$$
\boxed{\;(p+q)^2 \;=\; (p-q)^2 \;+\; 4pq\;}
$$

Specialising to the Mukai signature $(p,q) = (4,20)$ of $H^*(K3,\mathbb{Z})$:

- $\operatorname{rk} = p+q = 24 = \kappa_{\mathrm{fiber}}(K3)$
- $\operatorname{sdim}_{\mathrm{Ber}} = p-q = -16$ (the Berezinian super-trace of $\mathbb{1} \in Y(\mathfrak{gl}(4|20))$)
- $4pq = 320$

Yields:
$$
24^2 \;=\; 576 \;=\; 256 + 320 \;=\; (-16)^2 + 4 \cdot 4 \cdot 20.
$$

## Why this matters

V53 reported $24^2 = (-16)^2 + 320$ as a "Pythagorean identity orthogonally decomposing the squared Mukai rank into the squared Berezinian super-trace and the squared positive-root contribution." The first-principles reduction sharpens this: the identity is **universal in $(p,q)$**; the K3 case $(4,20)$ is one instance. Three corollaries:

1. **Rigidity of the Berezinian channel.** For a super-Yangian $Y(\mathfrak{gl}(p|q))$, the Wave-21 Berezinian projection is $\operatorname{sdim}_{\mathrm{Ber}} = p-q$, *forced* by the lattice signature. It is not a free parameter to be tuned.

2. **The $4pq$ term has off-diagonal interpretation.** $4pq$ is twice the dimension of the off-diagonal super-blocks $M_{p\times q} \oplus M_{q\times p}$ (each of dimension $pq$), summed over positive and negative odd-root contributions. Equivalently, $4pq$ counts the *odd-root pairing data* of the super Lie algebra.

3. **Wave-21 multi-projection at any K3-fibered super-Yangian source.** For a CY3 with K3 fiber and Mukai signature $(4,20)$ in the fiber: the Berezinian channel contributes $-16$, and the Wave-21 four-term identity reads
$$
\kappa_{\mathrm{ch}} \;+\; \kappa_{\mathrm{BKM}} \;+\; (-16) \;+\; \chi^{\mathrm{cat}} \;=\; \chi(\mathcal{O}_X).
$$
The $-16$ is rigidly K3-derived; only $\kappa_{\mathrm{ch}}, \kappa_{\mathrm{BKM}}, \chi^{\mathrm{cat}}$ depend on the global geometry and the chiral algebraization.

## Generalisation: the K3-fibered super-Yangian Pythagorean ladder

For each $(p,q)$ with $p+q = 24$ (K3 lattice rank constraint):

| $(p,q)$ | sdim | $4pq$ | Identity |
|---------|------|-------|----------|
| $(0,24)$ | $-24$ | $0$ | $24^2 = 24^2 + 0$ (purely odd; Berezinian degenerate) |
| $(1,23)$ | $-22$ | $92$ | $576 = 484 + 92$ |
| $(4,20)$ | $-16$ | $320$ | $576 = 256 + 320$ — **Mukai signature** |
| $(8,16)$ | $-8$ | $512$ | $576 = 64 + 512$ |
| $(12,12)$ | $0$ | $576$ | $576 = 0 + 576$ (sdim degenerate; purely off-diagonal) |
| $(16,8)$ | $+8$ | $512$ | $576 = 64 + 512$ |
| $(24,0)$ | $+24$ | $0$ | $576 = 576 + 0$ (purely even; Berezinian = full rank) |

The Mukai signature $(4,20)$ is **distinguished** in this ladder by the Hodge-theoretic fact that the K3 Mukai lattice has positive part $H^0 \oplus H^4 \oplus H^{1,1}_{\mathrm{pos}}$ of rank 4 and negative part of rank 20. The Pythagorean entry $(4,20)$ is the unique one consistent with the K3 period domain.

## What this unblocks

- **V53 engine update** (low priority): factor `pythagorean_identity()` into a generic helper `pythagorean_super(p, q) → (rk², sdim², 4pq)` valid for all $(p,q)$, with the K3 specialisation as one test among the ladder.
- **Vol III k3_yangian.tex** insertion: Box this identity as Proposition (universal-in-$(p,q)$), then specialise to $(4,20)$. Frame the V50 Wave-21 right-hand side closure $0 + 5 + (-16) + 11 = 0$ as the geometric content, and the identity above as the algebraic content.
- **Falsifiability**: any K3-fibered CY3 with super-Yangian source MUST have Berezinian projection $p - q$ where $(p,q)$ is the K3 fiber Mukai signature. A computed value contradicting $p-q$ would falsify the conjectural BKM-to-Yangian lift.

## Status delta

| Quantity | Before this memo | After this memo |
|---|---|---|
| $24^2 = (-16)^2 + 320$ | Pythagorean coincidence | universal-in-$(p,q)$ identity, K3 specialisation |
| Berezinian channel value | reported $-16$ for K3 | rigidly forced by Mukai signature for any K3-fibered source |
| Wave-21 closure mechanism | four arithmetic projections sum to $\chi(\mathcal{O}_X)$ | three algebraization residuals + one rigid lattice invariant ($\operatorname{sdim} = p-q$) |

— Raeez Lorgat, 2026-04-16
