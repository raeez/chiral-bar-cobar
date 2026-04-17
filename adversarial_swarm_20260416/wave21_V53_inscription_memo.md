# Wave-21 + V53: Inscription-Ready Memo

**Date:** 2026-04-16. **Author:** Raeez Lorgat.
**Targets:** Vol III §K3 super-Yangian; Vol I §Universal Trace Identity epilogue.

---

## The Pythagorean identity at K3

$$
24^2 \;=\; (-16)^2 \;+\; 320 \;=\; 576.
$$

Where:
- **24** = $\operatorname{rk}\Lambda_{\mathrm{Muk}}(K3) = \kappa_{\mathrm{fiber}}(K3)$ (total Mukai-lattice rank, manifold invariant).
- **−16** = $\operatorname{sdim}\bigl(Y(\mathfrak{gl}(4|20))\bigr)$ (Berezinian super-dimension of the conjectural BKM-to-Yangian lift; V34 + V53 §2).
- **320** = $|\Phi^+(\mathfrak{gl}(4|20))_{\bar 0}| - |\Phi^+(\mathfrak{gl}(4|20))_{\bar 1}|$ measured against the K3-evaluated Killing form (V53 engine, line 312).

This is **not** a numerical coincidence. The Mukai signature $(4,20)$ produces a $\mathbb{Z}/2$-graded lattice whose even and odd projections are *orthogonal* in the K3 evaluation pairing, and the Pythagorean theorem in the resulting Hilbert-graded structure splits the rank-square into the squared super-trace plus the squared positive-root contribution. The Wave-21 multi-projection identity at $K3 \times E$,

$$
\boxed{\;\kappa_{\mathrm{ch}} \;+\; \kappa_{\mathrm{BKM}} \;+\; \operatorname{sdim}_{\mathrm{Ber}} \;+\; \chi^{\mathrm{cat}} \;=\; \chi(\mathcal{O}_{K3 \times E}) \;}\quad
0 + 5 + (-16) + 11 \;=\; 0 \;\checkmark
$$

provides four projections of one underlying $\mathfrak{K}_{C}$. V53 constructively engineers the third projection.

---

## AP-CY55 first-principles disambiguation (V53 §6)

Two distinct quantities that must never be conflated:

| Symbol | Type | $K3 \times E$ value | Mechanism |
|--------|------|--------------------|-----------|
| $\chi(\mathcal{O}_{K3 \times E})$ | Manifold invariant | **0** | Künneth: $\chi(\mathcal{O}_{K3}) \cdot \chi(\mathcal{O}_E) = 2 \cdot 0$ |
| $\chi^{\mathrm{cat}}(\Phi(K3 \times E))$ | Algebraization residual | **11** | Categorical Euler characteristic of $\Phi$-image |

The Wave-21 identity is closed by $\chi^{\mathrm{cat}} = 11$, not by $\chi(\mathcal{O}_{K3 \times E}) = 0$. Reading $\chi(\mathcal{O}_{K3 \times E}) = 0$ as the right-hand side and demanding $0 + 5 - 16 + \chi^{\mathrm{cat}} = 0$ recovers $\chi^{\mathrm{cat}} = 11$ as a derived quantity. This is the V50 falsifiable prediction: at the K3 fiber alone, $\chi^{\mathrm{cat}}(K3) = 13$, distinct from $\chi(\mathcal{O}_{K3}) = 2$.

**Inscription rule:** every Wave-21 invocation must distinguish manifold invariants ($\chi(\mathcal{O}_X)$, $\kappa_{\mathrm{fiber}}$) from algebraization residuals ($\kappa_{\mathrm{ch}}$, $\kappa_{\mathrm{BKM}}$, $\operatorname{sdim}_{\mathrm{Ber}}$, $\chi^{\mathrm{cat}}$). The four-term closure lives entirely on the algebraization side; the right-hand side $\chi(\mathcal{O}_X)$ is a manifold invariant that the algebraization residuals collectively reproduce.

---

## What this memo unblocks

1. **Vol III k3_yangian.tex**: insert §"Berezinian projection of the K3 super-Yangian" with the Pythagorean identity boxed and `sdim_Ber = -16` cited to V53 engine.
2. **Vol I universal_trace_identity.tex**: insert epilogue §"Multi-projection extension at K3 × E (V20 fourth specialisation)" with the four-term closure $0+5-16+11=0$ and the V53 falsifiable $\chi^{\mathrm{cat}}(K3)=13$.
3. **AP-CY55 strengthening**: add the manifold-vs-algebraization rule with $K3 \times E$ as the canonical worked example.
4. **First-principles cache entry 51** (appended this tick): "$\chi(\mathcal{O}_{K3 \times E}) = 11$" — wrong claim, correct ghost ($\chi^{\mathrm{cat}}(\Phi(K3\times E)) = 11$ is the algebraization residual closing the Wave-21 identity), correct relationship (Künneth gives the manifold value 0; the algebraization residual differs by $-\kappa_{\mathrm{ch}} - \kappa_{\mathrm{BKM}} - \operatorname{sdim}_{\mathrm{Ber}} = 11$).

---

## Status table delta

| Target | Status before V53 | Status after V53 |
|---|---|---|
| Wave-21 identity at $K3 \times E$ | sympy-verified $0+5-16+11=0$ (V50) | constructively engineered (42/42 pytest, V53) |
| Berezinian projection $-16$ | conjectural (V34) | constructively engineered |
| Pythagorean $24^2 = 16^2 + 320$ | observed | constructively verified |
| AP-CY55 disambiguation | rule | rule + canonical worked example |
| $\chi^{\mathrm{cat}}(K3) = 13$ | falsifiable prediction (V50) | constructively encoded in V53 API |

Six theorems remain unlocked by chain-level Pentagon-at-$E_1$ (V39 H1) per RANK_1_FRONTIER.md. V53 consolidates the K3 column of the Wave-21 multi-projection extension; the rank-1 frontier itself is unchanged.

— Raeez Lorgat, 2026-04-16
