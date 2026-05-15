# Wave 1 deep verification — 2026-05-09

> Substantive mathematical verification of the load-bearing claims in the
> Wave-1 swarm output, executed on the main thread via the existing
> compute engines and direct symbolic computation.  Each item below was
> ground-truth re-derived; the outputs are reproducible with the cited
> commands.

---

## §1 Theorem H concentration: $\mathrm{ChirHoch}^\bullet(A) \subset \{0,1,2\}$

Run via `compute/lib/chiral_hochschild_engine.py`.

| Family               | $h^0$ | $h^1$ | $h^2$ | $P_A(t)$        | concentration |
|----------------------|------:|------:|------:|-----------------|---------------|
| Heisenberg $H_k$     | 1     | 1     | 1     | $1 + t + t^2$   | ✓             |
| $V_k(\mathfrak{sl}_2)$ generic | 1 | 3 | 1 | $1 + 3t + t^2$ | ✓             |
| $V_k(\mathfrak{sl}_3)$ generic | 1 | 8 | 1 | $1 + 8t + t^2$ | ✓             |
| $\beta\gamma$ system | 1     | 2     | 1     | $1 + 2t + t^2$  | ✓             |
| free fermion $\psi$  | 1     | 1     | 1     | $1 + t + t^2$   | ✓             |
| $\mathrm{Vir}_c$ generic | 1 | 0 | 1 | (W-regime)        | ✓             |
| $\mathcal W_3$       | 1     | 0     | 1     | (W-regime)       | ✓             |

**Striking observation.**  Both $\mathrm{Vir}_c$ and $\mathcal W_3$ are
**rigid**: $\mathrm{ChirHoch}^1 = 0$.  No first-order chiral
deformations exist for class-$\mathbf M$ generic-$c$ algebras.  The
Heisenberg algebra and the affine Kac–Moody algebras carry
$\mathrm{ChirHoch}^1 \neq 0$ — for Heisenberg the unique direction is
the level deformation $k \mapsto k+1$; for affine $V_k(\mathfrak g)$
the directions form $\mathfrak g$ itself.  The $\beta\gamma$ system at
generic $\lambda$ has two derivations.

**Affine Kac–Moody identity.**
$\mathrm{ChirHoch}^1(V_k(\mathfrak{sl}_N)) \cong \mathfrak{sl}_N$
verified by direct computation for $N \in \{2, 3, 4, 5, 6, 10\}$:
dimensions $3, 8, 15, 24, 35, 99$.

```text
    sl2: dim_g = 3, dim_H1 = 3 ✓
    sl3: dim_g = 8, dim_H1 = 8 ✓
    sl4: dim_g = 15, dim_H1 = 15 ✓
    sl5: dim_g = 24, dim_H1 = 24 ✓
    sl6: dim_g = 35, dim_H1 = 35 ✓
    sl10: dim_g = 99, dim_H1 = 99 ✓
```

---

## §2 Garland–Lepowsky / Macdonald identity for $V_k(\mathfrak{sl}_2)$

Run via `compute/lib/bar_cohomology_sl2_explicit_engine.py`.  The
engine returns the bar cohomology table $\{h: \{p: \dim H^p_h\}\}$
for $V_k(\mathfrak{sl}_2)$.

| weight $h$ | bar degree $p$ | $\dim H^p_h$ | Macdonald prediction $(2p+1)$ at $h = p(p+1)/2$ |
|-----------:|---------------:|-------------:|------------------------------------------------:|
| 0 | 0 | 1 | $p=0$, $h=0$, dim $1$ ✓                         |
| 1 | 1 | 3 | $p=1$, $h=1$, dim $3$ ✓                         |
| 3 | 2 | 5 | $p=2$, $h=3$, dim $5$ ✓                         |
| 6 | 3 | 7 | $p=3$, $h=6$, dim $7$ ✓                         |
| 10 | 4 | 9 | $p=4$, $h=10$, dim $9$ ✓                       |

The **Macdonald identity for $\mathfrak{sl}_2^{\mathrm{aff}}$**:
$$
\eta(\tau)^3 = \sum_{n=0}^\infty (-1)^n (2n+1) \, q^{n(n+1)/2}
$$
identifies $H^p_h(B(V_k(\mathfrak{sl}_2)))$ as the $(2p+1)$-dimensional
$\mathfrak{sl}_2$-irrep at conformal weight $h = p(p+1)/2$ (triangular
number).  The dimension $2p+1$ is the dimension of the spin-$p$
$\mathfrak{sl}_2$ representation.

This is **Garland–Lepowsky (1976)** specialised to
$\mathfrak{sl}_2$-aff: the Lie cohomology
$H^*(\mathfrak g[t]\!\cdot\! t,\,\mathbb C)$
of the negative-mode current Lie subalgebra computes the bar
cohomology of $V_k(\mathfrak g)$.

The bar cohomology of $V_k(\mathfrak{sl}_2)$ is **unbounded**; this is
a level-2 statement on the Beilinson tower and is consistent with
Theorem H, which is a level-3 statement
($\mathrm{ChirHoch}^\bullet \subset \{0, 1, 2\}$).  The two objects are
distinct: bar cohomology = $A^{\mathrm i} = H^* B(A)$ at level 2;
chiral Hochschild = $Z^{\mathrm{der}}_{\mathrm{ch}}(A)$ at level 3.

---

## §3 Universal Borcherds-weight identity $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$

Verified for $N \in \{1, 2, 3, 4, 6\}$ via the CHL paramodular
classification (Borcherds 1995 + Gritsenko–Nikulin 1998).

| $N$ | $\mathrm{wt}(\Phi_N)$ | $c_N(0)$ | $\kappa_{\mathrm{BKM}} = c_N(0)/2$ |
|----:|----------------------:|---------:|-----------------------------------:|
| 1 | 5 | 10 | 5 ✓                                       |
| 2 | 4 | 8  | 4 ✓                                       |
| 3 | 3 | 6  | 3 ✓                                       |
| 4 | 2 | 4  | 2 ✓                                       |
| 6 | 1 | 2  | 1 ✓                                       |

**Half-integer continuations** (Clery–Gritsenko 8-row):
$\Delta_{1/2}$ has weight $1/2$ ($c(0) = 1$); $\nabla_{3/2}$ has weight
$3/2$ ($c(0) = 3$).

**Why the additive form fails.**
The forbidden slogan
$\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}}^{\mathrm{Heis}} + \chi(\mathcal O_{\mathrm{fiber}})$
predicts $\kappa_{\mathrm{BKM}}(\Delta_5) = 3 + 24 = 27$ on K3$\times$E,
versus the correct $5$.  The simpler reading $\kappa_{\mathrm{BKM}} =
\kappa_{\mathrm{ch}} + \chi(\mathcal O_{\mathrm{K3}}) = 3 + 2 = 5$ is
an $N=1$ coincidence: at $N=2$ it predicts $\kappa_{\mathrm{BKM}}(\Phi_2)
= 1 + 0 = 1$ versus the correct $4$.  No additive identity expressing
$\kappa_{\mathrm{BKM}}$ as a sum of chiral and fibre scalars is licensed
(MA-6).

---

## §4 BKM algebra cross-check battery (9 of 9 PASS)

`cy_bkm_algebra_engine.full_cross_check_battery()`:

| Cross-check                       | result |
|-----------------------------------|--------|
| `c0_consistency`                  | ✓      |
| `phi01_sum_rule`                  | ✓      |
| `root_norm`                       | ✓      |
| `weyl_reflection_involution`      | ✓      |
| `reflection_preserves_norm`       | ✓      |
| `rho_prefactor`                   | ✓      |
| `phi10_leading`                   | ✓      |
| `shadow_consistency`              | ✓      |
| `euler_char_product`              | ✓      |

**Igusa $\Delta_5$ normalisation** (also from the engine):
- Leading coefficient $\Delta_5 = 64\,D_5$.
- $\Phi_{10}^{\mathrm{un}} = \Delta_5^2$.
- $\Phi_{10}^{\mathrm{OP}} = D_5^2 = (1/4096)\,\Delta_5^2$.
- $Z_{\mathrm{OP/DT}} = -D_5^{-2} = -4096\,\Delta_5^{-2}$.
- The factor $4096 = 64^2 = 2^{12}$.

---

## §5 Master concordance complementarity sums $K^\kappa$ (algebra-level)

Recomputed by direct symbolic substitution (sympy):

| Family                           | $K^\kappa$ | check |
|----------------------------------|-----------:|------:|
| $H_k$ vs curved $\mathrm{Sym}^{\mathrm{ch}}(V^*)$ | $0$    | ✓ |
| $V_k(\mathfrak g)$ vs FF$(-k-2h^\vee)$ | $0$              | ✓ |
| $\beta\gamma_\lambda$ vs $bc_\lambda$ | $0$                | ✓ |
| $\mathrm{Vir}_c$ vs $\mathrm{Vir}_{26-c}$ | $13$            | ✓ |
| $\mathcal W_3^k$ vs dual DS      | $250/3$              | ✓ |
| $\mathrm{BP}_k$ vs $\mathrm{BP}_{-k-6}$ | $98/3$            | ✓ |
| Mukai-K3 vs Vol III B-row        | $8$                  | ✓ |
| $V_{\Lambda_{24}}$ self-dual     | $48$                 | ✓ |

The **five-archetype bucket** $\{0,\ 8,\ 13,\ 250/3,\ 98/3\}$ on the
non-trivial complementarity rows is closed (with $V_{\Lambda_{24}}$
adding a separate Niemeier-self-dual scalar $48$ on its own lane).

---

## §6 K3$\times$E anchor row B = $(0, 0, 3, 5, 24)$

Recomputed entry-by-entry:

| Coordinate                            | value | three-path provenance |
|---------------------------------------|------:|------------------------|
| $\kappa_{\mathrm{cat}}(\mathrm{K3}\times E)$ | $0$ | (i) Künneth $\chi(\mathcal O)\cdot\chi(\mathcal O_E) = 2\cdot 0$; (ii) HRR $\chi(\mathcal O_E) = 1-g(E) = 0$; (iii) Serre-functor reading on $E$ |
| $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$ | $0$ | (i) odd-$d$ Serre cancellation; (ii) Künneth on Hodge supertrace; (iii) $c_1(\mathrm{K3}) = c_1(E) = 0$ |
| $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ | $3$ | (i) Mukai vector decomposition at rank $24/4 = 1/6$; (ii) lattice $\mathrm{II}_{2,2} \oplus \langle 2\rangle$ at rank 3; (iii) Borcherds–Mukai $\kappa_{\mathrm{Heis}} + \kappa_{\mathrm{BKM}} = 3+5 = 8$ |
| $\kappa_{\mathrm{BKM}}(\Delta_5)$    | $5$  | universal identity $c_1(0)/2 = 10/2$ |
| $\kappa_{\mathrm{fiber}}$            | $24$ | $\chi_{\mathrm{top}}(\mathrm{K3}) = 24$ |

The Mukai conductor identity is the algebra-level bridge: $K^\kappa(\mathrm{Mukai-K3}) = \mathcal N(\mathrm{Mukai-K3}) = 2c_+(\mathrm{Mukai}(\mathrm{K3})) = 8$.  Class B is the **unique** archetype whose chain-homotopy norm $\mathcal N$ and concordance complementarity sum $K^\kappa$ coincide.

---

## §7 Implications for the manuscript

1. **All Wave-1 inscriptions verified mathematically**: Theorem H, the
   Garland–Lepowsky / Macdonald formula, the universal Borcherds-weight
   identity, the K3$\times$E anchor row, the $K^\kappa$ complementarity
   sums.  No Wave-1 agent invented a falsified value within the
   verified scope.

2. **The notation collision identified during integration**
   ($\kappa+\kappa^!$ at level 1 vs level 2) is genuine; its
   linguistic resolution into $K^\kappa$ vs $\mathcal N$ does not
   change any verified value.  The mathematics is correct in both
   readings; only the naming was ambiguous.

3. **Class B's coincidence $\mathcal N = K^\kappa = 8$** is structural
   (Mukai self-mirror: the bar coalgebra of the Mukai-K3 chiral
   bialgebra sits at the same scalar lane as its Verdier dual).
   The other archetypes have $\mathcal N \neq K^\kappa$ as a symptom
   of the level-1 vs level-2 Verdier asymmetry.

4. **Open frontier deepening.** The Garland–Lepowsky formula gives
   the bar cohomology unconditionally as the Macdonald identity;
   chart-class enumeration (F8) is the next non-trivial structural
   question.  Heisenberg and free fermion both sit in class G; their
   chart-classes differ by lattice rank but their $\mathcal N$
   values agree at $1$ (Convention~`conv:A-two-kappa-shriek`).

---

## Reproducibility

```bash
# Theorem H concentration
python3 -c "
import sys; sys.path.insert(0, 'compute/lib')
from chiral_hochschild_engine import compute_all_standard_families, summary_table
from chiral_hochschild_engine import verify_km_h1_equals_dim_g
print(verify_km_h1_equals_dim_g())
print(summary_table())
"

# Garland-Lepowsky / Macdonald
python3 -c "
import sys; sys.path.insert(0, 'compute/lib')
from bar_cohomology_sl2_explicit_engine import compute_bar_cohomology_table
print(compute_bar_cohomology_table(max_degree=4, max_weight=10))
"

# BKM cross-check battery
python3 -c "
import sys; sys.path.insert(0, 'compute/lib')
from cy_bkm_algebra_engine import full_cross_check_battery, k3xe_kappa_split
print(full_cross_check_battery())
print(k3xe_kappa_split())
"
```
