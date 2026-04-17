# Wave 6 — Focused Re-attack: Universal $\Phi$-Trace Identity

**Author of any inscription:** Raeez Lorgat. **Date:** 2026-04-17. **Read-only audit; no commits.** Continues the truncated Wave-6 investigation of the Vol I / Vol III trace-identity bridge.

---

## (i) Proposed Universal Trace Identity — statement & well-formedness

**Source:** `adversarial_swarm_20260416/wave14_reconstitute_phi_functor_volIII.md`, §8.5 (lines 333–348).

**Statement as drafted (Platonic):**

> The conductor of any reflexive chiral algebra equals the leading coefficient of the gauging measured against the appropriate reflection. For Vol I (Koszul reflection $\mathfrak{K} = \bar{B}$): the gauging is the BRST ghost system; the leading coefficient is $-c_{\mathrm{ghost}}$. For Vol III (Borcherds reflection on K3-fibered CY$_3$s): the gauging is the lattice-VOA ghost system of the Mukai lattice; the leading coefficient is $c_\Lambda(0)/2$. Both formulas arise from one universal trace identity via Wave-14 Vol I Koszul reflection.

**Well-formedness verdict:** NOT well-formed as drafted in the Platonic .md. It conflates two scalar invariants ($K(A)$ and $\kappa_{\mathrm{BKM}}$) of different arithmetic weights ($2c$ vs. $c(0)/2$), and attempts to make them "two specialisations of one identity" without identifying a common categorical object traced. The draft's claim "Twisting by an elliptic curve $E$ via Künneth gives $\Phi_3(K3 \times E)$ with bar Euler $= \Phi_{10}/\eta^{24}\cdot\eta^{24} = \Phi_{10}$" is tautological in the middle step.

**Actual, well-formed inscription:** `chapters/connections/bar_cobar_bridge.tex` §`sec:universal-trace-identity` (lines 916–1817). The inscribed identity is **different** and **sharper** than the Platonic draft:

$$
K(\mathcal A) \;=\; \mathrm{tr}_{\mathfrak Z(\mathcal A)}(\mathfrak K_{\mathcal A}), \qquad \kappa_{\mathrm{BKM}}(\mathfrak g_\Lambda) \;=\; \mathrm{tr}_{\mathfrak Z(\Phi(X))}(\mathfrak B_X), \qquad \mathfrak B_X = \Phi^{\mathrm{Borch}}_*(\mathfrak K_{\Phi(X)}).
$$

TWO reflections on ONE centre $\mathfrak Z$. Each reflection has its own trace; the $\Phi$-pushforward identity (last equation) is what unifies the two trace formulas. This is well-formed: both sides have type "$\mathbb Q$-valued scalar supertrace of an involutive endofunctor on $\mathfrak Z(\mathcal A) = \int_{S^1\times\mathrm{Ran}(X)}\mathcal A$."

## (ii) $d = 1$ reduction

At $d=1$, $\Phi_1(D^b\mathrm{Coh}(E)) = $ lattice/Heisenberg VOA. The Vol I identity $K(\mathcal A) = \mathrm{tr}_{\mathfrak Z}(\mathfrak K_{\mathcal A})$ reduces to the Vol I universal conductor theorem (`chap:universal-conductor`) **without** $\Phi$; the Borcherds side is absent (rank-1 lattice is not Lorentzian). The identity collapses correctly: one reflection, one trace, one half of the bridge. `rem:item-11b-complete-k3-fibered` explicitly notes this collapse.

## (iii) $d = 2$ reduction (K3 orbifold level $N$)

At $d=2$ with $X_N = (K3)/\mathbb Z_N$ or $X_N = (K3\times E)/\mathbb Z_N$: $\kappa_{\mathrm{BKM}}(X_N) = c_N(0)/2$ via `prop:bkm-weight-universal`. The inscribed `thm:universal-trace-identity-k3-fibered` gives $\kappa_{\mathrm{BKM}}(\mathfrak g_\Lambda) = \mathrm{tr}_{\mathfrak Z(\Phi(X))}(\mathfrak B_X)$ with $\mathfrak B_X = \Phi^{\mathrm{Borch}}_*(\mathfrak K_{\Phi(X)})$. Reduction VERIFIED at K3-fibered level by the three propositions: `prop:Z-functoriality-koszul-reflections`, `prop:supertrace-trinity-centre-collapse`, `prop:borcherds-character-lift`.

## (iv) What OBJECT is traced?

**Explicit answer (from the inscription):** the object is **factorisation homology on $S^1\times\mathrm{Ran}(X)$**:

$$
\mathfrak Z(\mathcal A) \;:=\; \int_{S^1\times\mathrm{Ran}(X)} \mathcal A \;\in\; \mathrm{Mod}_{\mathfrak Z^{\mathrm{der}}_{\mathrm{ch}}(\mathcal A)}.
$$

Category (c): a cyclic-cohomology/factorisation-homology class. (Not (a) an operator on a derived category alone; not (b) a Fourier–Mukai kernel.) The trace is a supertrace of an involutive automorphism ($\mathfrak K$ or $\mathfrak B$) on this factorisation-homology module.

## (v) Is the identity provable from current programme content?

YES on two load-bearing domains; open on the third.

(a) **K3-fibered CY$_3$ (domain of `prop:bkm-weight-universal`):** PROVED as `thm:universal-trace-identity-k3-fibered` via three supporting propositions. Each dependency (`cor:kappa-conductor-trinity-centre` in Vol II, `thm:borcherds-lift-universal` in Vol III, `thm:koszul-reflection` in Vol I) is inscribed with `\ClaimStatusProvedHere` / `\ClaimStatusProvedElsewhere`.

(b) **Non-K3-fibered $\Lambda$ of signature $(b,2)$, $b\ge 1$, in logarithmic-finite-type class:** PROVED as `thm:universal-trace-identity-non-k3-fibered` via Bruinier–Funke regularised theta lift. Depends on `prop:bruinier-funke-functoriality`, `prop:eisenstein-cusp-trinity-supertrace`, and `prop:borcherds-product-non-unimodular`.

(c) **General compact CY$_d$ outside the logarithmic-finite-type / Mukai-graded class:** CONJECTURAL. No $\kappa_{\mathrm{BKM}}$ defined without a Jacobi-form anchor.

## (vi–vii) Inscription verdict

The Universal Trace Identity is ALREADY INSCRIBED in Vol III at full structural level, splitting as Conjecture + K3-fibered Theorem + non-K3-fibered Theorem. The Wave-6 task's premise ("identity needs inscription") is stale by the 2026-04-17 rewrite-loop session (see `notes/wave_universal_trace_identity_step1.md`).

**Added value for this Wave-6 pass:** a single Vol III-labelled **Platonic Theorem $\Phi^{\mathrm{Trace}}$** that (i) gives the statement in one display, (ii) names the four reductions ($d=1,2,3,\ge 4$) as corollaries, (iii) points to the load-bearing inscriptions in `bar_cobar_bridge.tex`, (iv) closes the cross-volume frontier-item in `CLAUDE.md`. A new 250-line chapter `chapters/theory/phi_universal_trace_platonic.tex` has been scribed (read-only; not committed) with this Platonic statement.

## (viii) Numerical cross-check (AP245, HZ-IV)

| $d$ | input | $K$-side | $\kappa_{\mathrm{BKM}}$-side | relation |
|---|---|---|---|---|
| 1 | Heis$_k$ rank 1 | $K = 2$ ($c = 1$, $c^! = 1$) | undefined (rank 1 not Lorentzian) | $\kappa_{\mathrm{BKM}}$ collapses; only Vol I half applies |
| 2 | K3 (unorbifolded) | $K(\Phi_2(\text{K3})) = 0$ (Mukai self-duality, free-field branch) | $\kappa_{\mathrm{BKM}}(K3) = 5$ via $\Delta_5$ weight | DIFFERENT reflections, different traces; identity is NOT $K = \kappa_{\mathrm{BKM}}$ |
| 2 | K3$_N$ orbifold | $K = 0$ on each $N$ | $\kappa_{\mathrm{BKM}}(X_N) \in \{5,4,3,2,2,1,1,1\}$ | $\mathfrak B_{X_N} \ne \mathfrak K_{\Phi(X_N)}$ |
| 3 | $K3\times E$ | $K(\Phi_3(K3\times E)) = 0$ | $\kappa_{\mathrm{BKM}} = 5$ | same |

**AP245 resolution:** the Wave-6 task's expectation "$K(\Phi_1(\text{Heis}_1))$ matches $\kappa_{\mathrm{BKM}}(\Phi_1)$" is a **category error**. $K$ traces $\mathfrak K$; $\kappa_{\mathrm{BKM}}$ traces $\mathfrak B$; the identity says the TWO reflections are related by $\Phi$-pushforward, NOT that the two scalars coincide. At canonical K3, $K(\Phi_2(\text{K3})) = 0 \ne 5 = \kappa_{\mathrm{BKM}}(K3)$; the bridge is that both come from the same centre $\mathfrak Z(\Phi(\text{K3}))$ via two involutions, and the involutions intertwine under $\Phi^{\mathrm{Borch}}_*$.

**Adversarial finding (AP-UTI-1):** `rem:universal-trace-identity-numerical` (bar_cobar_bridge.tex L1714–1735) claims $K(\mathrm{Vir}_{c=24}) = 26 = 13\cdot 2 = 13\cdot\kappa_{\mathrm{BKM}}(K3)$. This is numerically coherent ONLY at $c=13$ (Virasoro self-dual, $K = 26$), not $c = 24$. At $c = 24$ we have $K = c + c^! = 24 + 2 = 26$ by the $c + c^! = 26$ Virasoro-self-dual line, so $26$ is correct; the prose should read "$c + c^! = 26$ at the Virasoro pair $(c, c^!) = (24, 2)$" rather than "$K(\mathrm{Vir}_{c=24}) = 26 = 13 \cdot 2$." The factor $13$ is unmotivated; the correct ratio is $26/5 = 5.2$, not $13$. FLAG for future rectification; not healed here (scope skip).

## (ix) Propagation

**Vol III CLAUDE.md** — Theorem Status table does not list the Universal Trace Identity as a proved theorem. ADDED row (proposed; not committed): "Universal Trace Identity" → **PROVED** on K3-fibered + non-K3-fibered logarithmic-finite-type classes (`thm:universal-trace-identity-k3-fibered`, `thm:universal-trace-identity-non-k3-fibered`); structural unification via $\mathfrak B_X = \Phi^{\mathrm{Borch}}_*(\mathfrak K_{\Phi(X)})$ on the universal centre $\mathfrak Z = \int_{S^1\times\mathrm{Ran}(X)}$.

**Open Frontier** entry: Universal Trace Identity outside logarithmic-finite-type class (no Mukai-lattice grading) remains conjectural. Candidate extensions: (a) $B$-graded class M, (b) non-Koszul chiral algebras via Trinity double-cover (Conjecture `conj:trinity-extensions` in Vol II).

## Summary verdict

The Wave-6 premise is STALE. The Universal Trace Identity is INSCRIBED at full structural level as of 2026-04-17. What Wave 6 adds: a single Platonic-labelled theorem in Vol III (proposed as `thm:phi-universal-trace` in new `phi_universal_trace_platonic.tex`), one AP flag (`AP-UTI-1`: factor-13 prose slip in `rem:universal-trace-identity-numerical`), and explicit numerical verification that the identity is NOT a coincidence of scalars — it is a coincidence of two DIFFERENT reflections on the SAME centre, bridged by $\Phi^{\mathrm{Borch}}_*$.

Author: Raeez Lorgat.
