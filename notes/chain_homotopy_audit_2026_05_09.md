# Chain-homotopy denominator audit — 2026-05-09

## Finding

The symbol "$\kappa + \kappa^!$" denotes **two different scalars** in two
load-bearing places, and they only coincide on Class B.

### The two scalars

**(i) Master concordance $K^\kappa(\mathcal{A}) := \kappa(\mathcal{A}) +
\kappa(\mathcal{A}^!)$.**
Definition: `chapters/connections/master_concordance.tex:449–497` — the
*scalar Verdier sum* on a chosen Verdier-partner pair of chiral algebras,
taken at the **algebra level**.  For each archetype:

| Family                                | Verdier partner                    | $K^\kappa$ |
|---------------------------------------|------------------------------------|-----------:|
| Heisenberg $\mathcal H_k$             | curved $\mathrm{Sym}^{\mathrm{ch}}$| $0$        |
| Affine $V_k(\mathfrak g)$             | Feigin–Frenkel $-k-2h^\vee$        | $0$        |
| $\beta\gamma_\lambda$                 | $bc_\lambda$                       | $0$        |
| Virasoro $\mathrm{Vir}_c$             | $\mathrm{Vir}_{26-c}$              | $13$       |
| Mukai-K3 Heisenberg                   | Vol III B-row                      | $8$        |

This is the **level-5 complementarity ceiling** that enters Theorem C.

**(ii) Chain-homotopy proposition denominator.**
Definition: `chapters/theory/theorem_A_infinity_2.tex:783–871`
(`prop:A-universal-chain-homotopy`, inscribed by Wave-1 agent B12).  The
formula
$$
h_{A_b} \;=\; \frac{h_{\mathrm{LV}}}{\kappa(A_b) + \kappa(A_b^!)}
$$
uses a $\kappa^!$ obtained by "applying $\mathbb D_{\mathrm{Ran}}$ to the
**bar coalgebra** $B(A_b)$ and recomputing the trace form on the dual."
The witness table:

| Archetype                    | "$\kappa + \kappa^!$" (chain-homotopy) | $h_{A_b}$              |
|------------------------------|---------------------------------------:|------------------------|
| $\mathsf G$ (Heis.)          | $1$ (free)                             | $h_{\mathrm{LV}}$      |
| $\mathsf L$ ($V_k(\fg)$)     | $2(k+h^\vee)$                          | $h_{\mathrm{LV}}/[2(k+h^\vee)]$ |
| $\mathsf C$ ($\beta\gamma_\lambda$) | $1$ (free)                      | $h_{\mathrm{LV}}$      |
| $\mathsf M$ ($\mathrm{Vir}_c$) | $c(5c+22)/10$                        | $10 h_{\mathrm{LV}}/[c(5c+22)]$ |
| $\mathsf B$ (Mukai-K3)       | $8$                                    | $h_{\mathrm{LV}}/8$    |

The class-$\mathsf M$ value $c(5c+22)/10$ is the **Zamolodchikov norm**
$\langle\Lambda|\Lambda\rangle$ of the level-4 quasi-primary
$\Lambda = {:}TT{:} - (3/10)\partial^2 T$; it is the inverse of $S_4$.

### Numerical comparison

```
Class | K^κ (concordance) | "κ+κ^!" (chain-homotopy) | Agree?
G     | 0                 | 1                          | ✗
L     | 0                 | 2(k+h^∨)                   | ✗
C     | 0                 | 1                          | ✗
M     | 13                | c(5c+22)/10                | ✗
B     | 8                 | 8                          | ✓ (Mukai)
```

The two columns coincide only on class B (Mukai conductor accident).

## Why they differ

The Verdier dual is applied at different levels of the Beilinson tower:

- **Concordance $K^\kappa$.**  Verdier duality on the **chiral algebra**
  $\mathcal A$: a level-1 ↔ level-1 functor giving $\mathcal A^!$ a chiral
  algebra. For class L, this is Feigin–Frenkel level shift; for class M,
  $c \mapsto 26-c$.
- **Chain-homotopy $\kappa^!$.**  Verdier–Ran duality on the **bar coalgebra**
  $B(\mathcal A)$: a level-2 ↔ level-2 functor.  $\kappa$ recomputed on the
  dual coalgebra is generically a different rational function of the
  trace-form data.

Both conventions are mathematically legitimate.  The notation collision is
the issue.

## Remediation paths

### Option A — distinguish notation (recommended)

Rename the chain-homotopy denominator to a non-clashing symbol:
- $\kappa(A_b) + \kappa^!_{\mathrm{LV}}(A_b)$ where $\kappa^!_{\mathrm{LV}}$
  flags the Loday–Vallette / bar-coalgebra-Verdier construction; or
- a single name $\mathcal{N}(A_b)$ for "the convolution-pairing norm",
  with a per-archetype table.

Then $K^\kappa$ keeps its concordance meaning.

### Option B — heal the chain-homotopy formula

State $h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ where $\mathcal N$ is
the family-dependent shadow-pairing norm read off from the convolution
$L_\infty$-algebra inner product.  Provide the per-archetype table as the
*definition*, not as evidence for an a priori formula.

### Option C — reconcile algebraically (open)

Find a shared definition of $\kappa^!$ that gives both the concordance and
the chain-homotopy values simultaneously.  Likely requires distinguishing
the *level* at which Verdier is applied (1, 2, 3) and writing
$\kappa^!_{(\ell)}$ at each level.  Class B's coincidence at $8$ on the
Mukai-K3 row would then be read as the level-1 ↔ level-2 Verdier match
through the Mukai involution — a structural statement to verify.

## Wave-2 actionables

1. Update `theorem_A_infinity_2.tex:783–912` to use distinguished notation
   (Option A or B above); add a cross-reference clarifying that the
   chain-homotopy "$\kappa+\kappa^!$" is **not** the master-concordance
   $K^\kappa$.
2. Add a convention block in `chapters/connections/master_concordance.tex`
   distinguishing $K^\kappa$ from the chain-homotopy norm.
3. Update `CLAUDE.md` essential-constants line for the universal
   chain-homotopy: write
   $h_{A_b} = h_{\mathrm{LV}} / \mathcal N(A_b)$ with a table of
   archetype norms; reserve "$\kappa+\kappa^!$" for the concordance
   level-5 sum.
4. Audit `master_reconstruction.tex` (Wave-1 agent A1) for any place that
   conflates the two — A1's chapter cites
   $h_{A_b} = h_{\mathrm{LV}}/(\kappa+\kappa^!)$ as the universal
   chain-homotopy; verify which $\kappa+\kappa^!$ A1 means.

## Discovery context

Found 2026-05-09 during the Wave-1 manuscript reconstitution swarm
integration phase.  Verified via `sympy` recomputation:
- Class L: $\kappa(V_k) + \kappa(V_{-k-2h^\vee}) = 0$ (Feigin–Frenkel).
- Class L: chain-homotopy denominator = $2(k+h^\vee)$.
- Class M: $\kappa(\mathrm{Vir}_c) + \kappa(\mathrm{Vir}_{26-c}) = 13$.
- Class M: chain-homotopy denominator = $c(5c+22)/10$.

The mismatch is a notation collision, not a mathematical error in either
inscription.  Both formulas are individually correct; the symbol re-use
is the bug.

---

## Companion finding — 5×5 column assignment disagreement

Cluster C / B7 inscriptions of the $5{\times}5$ $\kappa$-stratification
matrix disagree on which column carries the modular characteristic $\kappa$
for non-CY archetypes.

**Per-agent column for $\kappa(\mathcal{A})$:**

| Agent | Family            | Column carrying $\kappa$            |
|-------|-------------------|-------------------------------------|
| C-G   | Heisenberg $H_k$  | $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ ($= k$) |
| C-L   | $V_k(\fg)$        | $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ ($= d(k+h^\vee)/(2h^\vee)$) |
| C-C   | $\beta\gamma_\lambda$ | $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$ ($= c/2$) |
| C-M   | $\mathrm{Vir}_c$, $\mathcal W_N$ | $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$ ($= c/2$, $c(H_N-1)$) |
| C-B   | Mukai-K3 $\times$ E | $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ ($= 3$, Mukai rank) |
| B7    | landscape census table | $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ for all rows |

C-G and C-B treat $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ as the
**Heisenberg / lattice subVOA rank** (semantically correct: H_k has rank
$k$, K3$\times$E has Mukai rank 3). C-L extends this to "the trace-form
Casimir scalar", which agrees with $\kappa$ for $V_k(\fg)$ but is not the
same definition. C-C and C-M instead place $\kappa$ in
$\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$, treating it as a chiral Hodge
characteristic.

The columns of the $5{\times}5$ matrix need precise, family-independent
definitions before the table is canonical.  Candidate definitions:

- $\kappa_{\mathrm{cat}}$: categorical Calabi–Yau dimension shift (e.g.\
  $\chi(\mathcal O_X) \cdot \chi(\mathcal O_E)$ for K3$\times$E); zero for
  chart-only families with no CY host.
- $\kappa^{\mathrm{Hodge}}_{\mathrm{ch}}$: chiral Hodge supertrace
  $\Xi(\mathcal A) = \sum_{p,q}(-1)^{p+q}h^{p,q}$ at the level-0 stratum.
  For K3$\times$E, $\Xi = 0$ since $h^{0,1}(E) = 1$ enters with a sign.
- $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$: rank of the canonical Heisenberg
  / lattice subVOA. For $V_k(\fg)$, this is $\mathrm{rank}(\fg)$, **not**
  $\dim(\fg)(k+h^\vee)/(2h^\vee)$.
- $\kappa_{\mathrm{BKM}}(\Phi_N) = c_N(0)/2$ from the universal
  Borcherds-weight identity; defined only on rows with an attached
  paramodular form.
- $\kappa_{\mathrm{fiber}}$: $\chi_{\mathrm{top}}$ of the CY fiber where a
  fiber is attached.

Under this canonical reading, C-L's value
$d(k+h^\vee)/(2h^\vee)$ should sit in a **separate column**
$\kappa_{\mathrm{mod}}$ (the modular characteristic), or the $5{\times}5$
should be expanded to $5{\times}6$ with $\kappa$ as its own column.

## Wave-2 actionable for the column-assignment finding

5. Pin canonical column definitions in `chapters/examples/landscape_census.tex`
   (alongside the new $5{\times}5$ table inscribed by B7) and propagate to
   `compute/tests/test_kappa_stratification_*.py` so Cluster C tests use a
   shared schema.  Likely outcome: rename C-L's
   $\kappa^{\mathrm{Heis}}_{\mathrm{ch}}$ entry to
   $\kappa_{\mathrm{mod}}$, leaving $\kappa^{\mathrm{Heis}}_{\mathrm{ch}} =
   \mathrm{rank}(\fg)$.
