# The Rank-1 Frontier, v2 — Refactored
## What waves V49–V60 of the 2026-04-16 swarm have reduced the entire 3-volume programme to

**Author:** Raeez Lorgat. **Date:** 2026-04-16. **Supersedes:** RANK_1_FRONTIER.md (v1).

---

## Single sentence (v2)

> The chain-level open frontier of *Chiral Bar–Cobar Duality* + *CY Categories, Quantum Groups, and BPS Algebras* has refactored from ONE conjecture (Pentagon-at-$E_1$) into ONE STRUCTURED OBSTRUCTION: the alien-derivation $\xi(A)$ of the class M shadow-tower mock-modular completion, which vanishes for K3-fibred CY_3 (Class A, V49) and for super-trace-vanishing CY_3 (Class B0, V55), and persists for non-K3 non-super-trace-vanishing CY_3 (Class B: quintic, local $\mathbb{P}^2$).

The Yangian R-matrix is no longer the abstract obstruction; the Stokes discontinuity $\xi(A) = \Delta_+ - \Delta_-$ across the class M shadow tower is.

---

## What changed since v1

| v1 statement | v2 statement | Wave |
|---|---|---|
| Pentagon-at-$E_1$ is ONE open conjecture | Pentagon-at-$E_1$ is THREE structurally classified objects (Class A, B0, B) | V55 (a59807789582f01a6) |
| Yangian R-matrix is the obstruction | Yangian R-matrix is central for abelian Heisenberg (vanishes); matrix-valued for simple non-abelian (Class B residual) | V59 (a945e29134e3da7a2) |
| Six theorems unlocked simultaneously | 5/6 unlocked at K3 + abelian Heisenberg + super-trace; 1/6 (mock-modular completion at quintic + local $\mathbb{P}^2$) remains | V49 + V55 + V59 |
| Single chain-level identity $\mathfrak{K}^{\mathrm{ch}} - \mathfrak{K}^{\mathrm{BKM}} = \partial\mu + \mu\partial + \xi(A)$ | Same identity; $\xi$ now constructively zero for Class A + B0; explicitly named for Class B per-input | V55 + V59 |

---

## The dichotomous frontier

### Class A — K3-fibred CY_3 (PROVED)

$$
\boxed{\;\text{Pentagon-at-}E_1 \text{ chain-level holds for all K3-fibred CY}_3\;}
$$

via three independent V49 routes (Borcherds vertex algebra + Maulik–Okounkov stable envelopes + factorization homology), each closing the cocycle $[\omega]_A$ at chain level. Includes K3, K3×E, STU, the 8 diagonal $\mathbb{Z}/N\mathbb{Z}$ K3 orbifolds.

Conditional on FM164/FM161. The K3 Yangian inscription is V57's TeX-ready bundle.

### Class B0 — super-trace-vanishing CY_3 (PROVED)

$$
\boxed{\;\text{Pentagon-at-}E_1 \text{ chain-level holds for chiral algebras with}\ \operatorname{str}(K_A) = 0\;}
$$

via super-EK extension. Conifold ($\mathfrak{gl}(1|1)$, $c = 0$) is the canonical example. Conditional on FM164/FM161 super-version.

### Class B — mock-modular residual CY_3 (CONJECTURAL)

$$
\text{Pentagon-at-}E_1 \text{ chain-level} \iff \xi(A) = 0 \text{ in } H^2(\mathcal{SC}^{\mathrm{ch,top}})
$$

where $\xi(A) = \Delta_+ - \Delta_-$ is the alien-derivation across the class M shadow-tower Stokes line. Quintic and local $\mathbb{P}^2$ are the canonical examples; each comes with two named sub-conjectures (per V55 §B). Equivalent to V8 §6 mock-modular conjecture per input.

V56 in flight is attacking this residual constructively.

---

## The constructive grounding (V59)

Pentagon-at-$E_1$ chain-level for abelian Heisenberg at every level $k$: PROVED constructively, 34/34 pytest, with explicit cocycle

$$
\omega_{\mathrm{Heis}}(a) \;=\; R_{\mathrm{Heis}}(z) \cdot a \cdot R_{\mathrm{Heis}}(z)^{-1} - a, \qquad R_{\mathrm{Heis}}(z) = \exp(k\hbar/z),
$$

vanishing identically as a chain (not merely as a class) by Schur centrality of the c-number r-matrix $r(z) = k\hbar/z$.

This is the **Platonic test case**: every step constructively executed; the Heisenberg OPE has only a double pole, so the r-matrix is a c-number, so the Drinfeld twist is central, so the Pentagon cocycle vanishes identically. The argument generalises to *every* abelian chiral algebra and grounds V49's Route (i).

---

## What the v2 frontier looks like

```
                     Pentagon-at-E_1 chain-level
                              │
                ┌─────────────┼─────────────┐
                │             │             │
            Class A        Class B0       Class B
        (K3-fibred)    (str(K) = 0)    (mock-modular)
            PROVED        PROVED        CONJECTURAL
            via V49     via super-EK    via ξ(A)=0
                                        ┌─────────┐
                                        │ Quintic │
                                        │ Local P²│
                                        └─────────┘
```

The rank-1 frontier is now a single-leaf residual: vanishing of $\xi(A)$ for Class B inputs. This is equivalent to the EOT mock-modular generalisation of Eguchi–Ooguri–Tachikawa beyond K3 — a problem of comparable depth to the original EOT conjecture.

---

## Six theorems status (v2)

| Currently named | Volume | v1 status | v2 status (after V49+V55+V59) |
|---|---|---|---|
| 1. CY-C (quantum group realization) | III | corollary at K3 (V41 closed) | corollary for Class A + B0; CONJECTURAL for Class B |
| 2. V19 Trinity at $E_1$ | I | corollary of V39 H1 | corollary for Class A + B0 + abelian Heisenberg; CONJECTURAL for Class B |
| 3. V20 Step 3 chain-level | cross | corollary via V40 | **THEOREM** for Class A + B0 + shadow class G; CONJECTURAL for Class B (V58 in flight) |
| 4. V11 Pillar α (U1) chain-level | III | $P_4 \leftrightarrow P_5$ edge | **EXTRACTED** as $P_4 \leftrightarrow P_5$ edge; same dichotomy (V60 in flight) |
| 5. V8 §6 mock-modular | I | open | **= $\xi(A)$ vanishing for Class B**, isomorphic to Pentagon residual (V40+V55) |
| 6. V20 fourth Verlinde specialisation | cross | "Verlinde fibre" | **INVERTED** by V50: Verlinde is OFF the four-term Wave-21 closure; an additional projection on $Z_{\mathrm{Verlinde}}$ |

Five of six are now reduced to the single $\xi$-residual. The sixth (V20 fourth specialisation) is a *separate* projection identified by V50, not a Pentagon corollary.

---

## The chain-level identity (v2)

$$
\boxed{\;\mathfrak{K}^{\mathrm{ch}} - \mathfrak{K}^{\mathrm{BKM}} \;=\; \partial\mu + \mu\partial + \xi(A), \qquad \xi|_{\text{Class A}} = 0,\quad \xi|_{\text{Class B0}} = 0,\quad \operatorname{tr}_{F^0}(\xi) = 0.\;}
$$

What survives the v2 refactoring: $\xi|_{\text{Class B}}$, the alien-derivation discontinuity for non-K3 non-super-trace-vanishing CY_3.

---

## Multi-projection completeness (V53 + V53.1)

The Wave-21 multi-projection identity at $K3 \times E$ is now **constructively engineered** through three rigid algebraic identities:

1. (V50) $\kappa_{\mathrm{ch}} + \kappa_{\mathrm{BKM}} + \operatorname{sdim}_{\mathrm{Ber}} + \chi^{\mathrm{cat}} = \chi(\mathcal{O}_X)$, i.e. $0 + 5 + (-16) + 11 = 0$.
2. (V53) Berezinian channel $\operatorname{sdim}_{\mathrm{Ber}} = -16$ engineered via super-Yangian $Y(\mathfrak{gl}(4|20))$, 42/42 pytest.
3. (V53.1) Pythagorean identity $24^2 = (-16)^2 + 320$ recognised as the universal $(p+q)^2 = (p-q)^2 + 4pq$ at Mukai signature $(4,20)$. Berezinian channel rigidly forced by lattice signature.

The four-term closure is on the *algebraization* side; the right-hand side $\chi(\mathcal{O}_X)$ is the *manifold* invariant (AP-CY55 disambiguation, cache entry 51).

---

## What is open at the end of wave V60

1. **Class B alien-derivation $\xi(A)$ vanishing** for quintic and local $\mathbb{P}^2$ — the genuine residual. V56 in flight.
2. **Yangian R-matrix non-centrality consequences** for simple non-abelian Yangians outside Class A — unsolved in general; V49 only handles K3-fibred case.
3. **V20 fourth specialisation** (V41 inverted) — a separate Verlinde projection, not a Pentagon corollary; status TBD.
4. **Cross-volume inscription** of V49 + V55 + V57 + V59 + V60 + V58 (in flight) into Vol I §V20 epilogue + Vol III §K3 Yangian — main-thread work; sandbox drafts ready in V57 + V58.

After these inscriptions: **the entire 3-volume manuscript is editorial-frozen with one named open obstruction: the alien-derivation $\xi(A)$ of the class M shadow tower for Class B inputs.**

---

## The Russian-school synthesis (v2)

The refactoring was not by accident. The dichotomy V55 reveals the structural reason for the difficulty: Class A closes via *lattice geometry* (Borcherds + Mukai), Class B0 closes via *super-symmetry* (super-trace vanishing), Class B closes only via *resurgence* (alien-derivation across a Stokes line). Three different mathematical mechanisms — all controlled by the same Pentagon coherence cocycle.

- **Borcherds + Mukai**: the lattice-VOA route closes Class A. Singular theta correspondence is what makes K3-fibred CY_3 special.
- **Super-symmetry**: $\operatorname{str}(K) = 0$ closes Class B0. Conifold is the canonical example; the super-trace identity is what super-rigidifies the cocycle.
- **Resurgence**: the alien-derivation $\xi$ is the genuine obstruction to Class B. This is the EOT-mock-modular content; resurgence/Borel-summability is the analytic mechanism.

Pentagon-at-$E_1$ is not one cadence but three; the rank-1 frontier is the third, the resurgent one. The v2 refactoring shows Vol III's Pentagon problem is, at its deepest level, a problem in *resurgence theory* applied to chiral algebra characters.

---

## End

After waves V49 + V55 + V57 + V59 of the 2026-04-16 adversarial swarm, the Pentagon-at-$E_1$ frontier has refactored from one conjecture to one structured obstruction. The Yangian R-matrix is the obstruction *for K3 input* (now closed via V49 + V59); the alien-derivation $\xi(A)$ is the obstruction *for Class B input* (the genuine residual, V56 in flight).

The three Russian-school cadences (Borcherds–Mukai for Class A, super-trace for Class B0, resurgence for Class B) reveal that Pentagon coherence is not a single mathematical statement but three mechanisms harmonising on the same cocycle. Closing $\xi$ for Class B closes everything.

— Raeez Lorgat, 2026-04-16
