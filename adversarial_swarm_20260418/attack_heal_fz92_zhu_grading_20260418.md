# Attack-and-heal: FZ92 zhu-grading usage discipline (Vol I)

Date: 2026-04-18
Target: AP284 follow-through. Verify FZ92 (Frenkel-Zhu 1992) usage scope across Vol I.
Scope: FZ92 = Zhu algebra A(V) construction for affine KM + Virasoro (no C_2-cofiniteness).
Distinct from: Zhu96 (genus-1 modular invariance + C_2-cofiniteness framework).
Author: Raeez Lorgat

## Phase 1: Enumeration

Grep for `FZ92|Frenkel-Zhu|Frenkel and Zhu|FrenkelZhu` across Vol I .tex surfaced
six files with `FZ92` citations:

1. `bibliography/references.tex:601` — canonical bibentry. Clean.
2. `chapters/theory/chiral_modules.tex:1891, 1898, 1941, 1986, 2032` — all cite FZ92
   for `A(V_k(g)) ≅ U(g)` or `A(Vir_c) ≅ C[x]`. These are exactly FZ92's theorems.
   **Clean scope.**
3. `chapters/theory/higher_genus_modular_koszul.tex:33609, 33630, 33781` — cite FZ92
   for Zhu algebra presentation + Zhu96 for modular invariance, in the genus-$1$ slot
   of `prop:verlinde-from-ordered` and in the Zhu-algebra proof of $Z_1 = k+1$ for
   $V_k(\mathfrak{sl}_2)$ (identification $A(V_k(\mathfrak{sl}_2)) \cong
   U(\mathfrak{sl}_2)/(e^{k+1}, f^{k+1})$). **Clean scope; AP284 discipline maintained.**
4. `chapters/connections/concordance.tex:9174, 9182` — cite Zhu96 + FZ92 for $A(V)$
   construction and FZ92 for $A(V_k(\fg)) \cong U(\fg)$. Zhu96 is the $V/V \circ V$
   quotient construction, FZ92 is the specific-family computation. **Clean scope.**
5. `chapters/examples/minimal_model_fusion.tex:104, 114` — `thm:wn-s-matrix` cites
   `\cite{FZ92,Arakawa17}` for the **modular S-matrix** of $W_N$ minimal models.
   **DRIFT DETECTED (AP309 primary-source-weaker).**
6. `standalone/theorem_index.tex:1594` — mirrors the drift from item 5.

## Phase 2: Scope verification per site

### Site-by-site verdict

| File | Line | Cited for | FZ92 actually proves this? | Verdict |
|------|------|-----------|-----------------------------|---------|
| `chiral_modules.tex` | 1891 | $A(\widehat{\mathfrak{g}}_k) \cong U(\mathfrak{g})$ | Yes (FZ92 Theorem) | CLEAN |
| `chiral_modules.tex` | 1898 | $A(\mathrm{Vir}_c) \cong \mathbb{C}[x]$ | Yes (FZ92 Theorem) | CLEAN |
| `chiral_modules.tex` | 1941 | $A(\widehat{\mathfrak{g}}_k) \cong U(\mathfrak{g})$ | Yes | CLEAN |
| `chiral_modules.tex` | 1986 | $A(\mathrm{Vir}_c) \cong \mathbb{C}[x]$ | Yes | CLEAN |
| `chiral_modules.tex` | 2032 | $A(V_k(\mathfrak{g})) \cong U(\mathfrak{g})$ | Yes | CLEAN |
| `higher_genus_modular_koszul.tex` | 33609 | "Zhu algebra of FZ92" for $Z_1 = k+1$ pairing | Yes (FZ92 supplies $A(V)$, Zhu96 supplies modular invariance) | CLEAN, scope-paired |
| `higher_genus_modular_koszul.tex` | 33630 | "Frenkel-Zhu presentation of Zhu algebra" | Yes | CLEAN |
| `higher_genus_modular_koszul.tex` | 33781 | $A(V_k(\mathfrak{sl}_2)) \cong U(\mathfrak{sl}_2)/(e^{k+1},f^{k+1})$ | Yes (FZ92 Theorem 3.1) | CLEAN |
| `concordance.tex` | 9174 | Zhu algebra $A(V) = V/V \circ V$ | Joint (Zhu96+FZ92); paired correctly | CLEAN |
| `concordance.tex` | 9182 | $A(V_k(\fg)) \cong U(\fg)$ | Yes | CLEAN |
| `minimal_model_fusion.tex` | 104 | **W_N modular S-matrix** | **NO** | **DRIFT — healed** |
| `minimal_model_fusion.tex` | 114 | W_N S-matrix precise formula | **NO** | **DRIFT — healed** |
| `theorem_index.tex` | 1594 | mirror of above | **NO** | **DRIFT — healed** |

## Phase 3: Nature of the drift at thm:wn-s-matrix

FZ92 ("Vertex operator algebras associated to representations of affine and Virasoro
algebras", Duke 1992) constructs Zhu algebras $A(V)$ for $V = V_k(\mathfrak{g})$ and
$V = \mathrm{Vir}_c$ and identifies their categories of simple modules via the Zhu
functor. FZ92 does NOT derive the modular $S$-matrix; it has no modular-invariance
content, no character-theoretic computation, no torus partition-function framework.
The modular $S$-matrix framework is:
- Zhu96 for the general character-modular-invariance theorem on rational $V$,
- Kac-Peterson 1984 for the affine case (modular data on $\widehat{\mathfrak{g}}_k$
  characters),
- Cappelli-Itzykson-Zuber 1987 for the Virasoro minimal-model $S$-matrix,
- Arakawa Inventiones 2007 ("Representation theory of $\mathcal{W}$-algebras") for
  $\mathcal{W}$-algebra rationality input.

The cited bibkey `Arakawa17` in Vol I resolves to Arakawa's "Chiral algebras of class
$\mathcal{S}$ and Moore-Tachikawa varieties" (arXiv:1811.01577), which is unrelated
to the $W_N$ modular $S$-matrix.

This is a textbook AP309 (primary-source citation to a strictly weaker claim) with
companion AP284 residual risk (using FZ92 as a "Zhu-grading universal attribution"
that silently propagates to modular-theoretic downstream content outside its actual
scope).

## Phase 4: Heals applied

### Heal 1: `chapters/examples/minimal_model_fusion.tex:104-116`

Before:
```
\begin{theorem}[... ; \ClaimStatusProvedElsewhere{} \cite{FZ92,Arakawa17}]
  \label{thm:wn-s-matrix}
  For the Virasoro ($N=2$) minimal model $\mathcal{M}(p,q)$, the modular
  S-matrix is (Cappelli-Itzykson-Zuber):
  [formula]
  For general $W_N$ minimal models, the S-matrix involves products
  over positive roots of $\mathfrak{sl}_N$ and Weyl-orbit summation;
  we refer to Frenkel-Zhu \cite{FZ92} and Arakawa \cite{Arakawa17}
  for the precise formula.
\end{theorem}
```

After:
- Citation `\cite{FZ92,Arakawa17}` replaced with `\cite{Zhu96,Ara07}` (Zhu's
  modular-invariance theorem + Arakawa's W-algebra representation-theory paper).
- Prose rewritten to make the sourcing honest: Zhu96 supplies the genus-$1$
  modular-invariance framework; Ara07 supplies the $\mathcal{W}$-algebra
  representation-theoretic input; Cappelli-Itzykson-Zuber supplies the Virasoro
  formula; FZ92 is explicitly noted as the Zhu-algebra presentation used UPSTREAM
  (not the $S$-matrix itself).

### Heal 2: `standalone/theorem_index.tex:1594`

Theorem-index row citation field updated `\cite{FZ92,Arakawa17}` to
`\cite{Zhu96,Ara07}` to match the healed theorem.

## Phase 5: Residual & non-findings

- `thm:verlinde-from-ordered` clean (AP284 discipline maintained): FZ92 is used
  only for the genus-$1$ slot's Zhu-algebra presentation, paired with Zhu96 for the
  modular-invariance step and TUY89 for nodal factorization. Genus-$g \geq 2$
  recovery routes through `prop:conformal-blocks-bar` + TUY89 + the modular-family
  extension of Theorem $A^{\infty,2}$. No FZ92 citation at $g \geq 2$.
- Zhu-algebra-Koszul-compatibility propositions (`prop:zhu-koszul-compatibility`,
  `cor:virasoro-zhu-koszul`, `thm:w-algebra-zhu-koszul`) all cite FZ92 correctly
  for $A(V) \cong U(\mathfrak{g})$ / $\mathbb{C}[x]$; no drift.
- Concordance entry 21d cites Zhu96 for $A(V) = V/V \circ V$ and FZ92 for
  $A(V_k(\fg)) \cong U(\fg)$; correct.

## Phase 6: AP registry

Minimal per AP314: one new AP.

**AP1861 (FZ92-as-universal-Zhu-attribution drift).** A theorem cites FZ92
(Frenkel-Zhu 1992) as the primary source for a modular-theoretic result (S-matrix,
character modularity, fusion-rule closure under modular transformations) when FZ92's
actual content is restricted to the Zhu algebra construction $A(V) = V/V\circ V$
specialised to $V \in \{V_k(\mathfrak{g}),\, \mathrm{Vir}_c\}$, without any
modular-invariance content. FZ92 has no torus partition function, no $S$-matrix,
no character-modular-invariance machinery; those belong to Zhu96 (general rational
$V$), Kac-Peterson 1984 (affine), Cappelli-Itzykson-Zuber 1987 (Virasoro minimal),
Arakawa Inventiones 2007 ($\mathcal{W}$-algebras). Canonical violation:
`thm:wn-s-matrix` at `chapters/examples/minimal_model_fusion.tex:104` cited
`\cite{FZ92,Arakawa17}` for the $W_N$ modular $S$-matrix (healed 2026-04-18 to
`\cite{Zhu96,Ara07}` with explicit prose identifying FZ92 as upstream
Zhu-algebra-presentation only, not $S$-matrix source). Counter: before citing
FZ92, verify the cited content is a Zhu algebra construction on affine/Virasoro, not
a modular-invariance / $S$-matrix / character-theoretic statement. If the target
content is modular-invariance, route through Zhu96; if $\mathcal{W}$-algebra
rationality, route through Arakawa 2007 (Ara07); if Virasoro minimal $S$-matrix,
route through Cappelli-Itzykson-Zuber. Special-case of AP309 (primary-source
citation for strictly weaker claim) + AP284 scope-propagation discipline.

## Summary

- 13 FZ92 citation sites audited across 6 files.
- 12 sites clean (FZ92 cited for Zhu-algebra construction within its actual scope).
- 1 site drifted (`thm:wn-s-matrix`) with 1 mirror (`theorem_index.tex`); both
  healed by replacing `\cite{FZ92,Arakawa17}` with `\cite{Zhu96,Ara07}` and
  rewriting prose to make upstream-vs-downstream sourcing explicit.
- AP284 "FZ92 confined to Z_1 = k+1 slot" discipline is MAINTAINED in
  `prop:verlinde-from-ordered`; no genus-$g \geq 2$ site cites FZ92.
- One new AP registered (AP1861, FZ92-as-universal-Zhu-attribution drift).

## Notes on out-of-scope hook flags

PostToolUse hook flagged AP24/AP8/AP25/AP34/AP14/AP7/AP32/V2-AP26 hits at various
lines in `theorem_index.tex`. All predate this session's edit; this audit's edit
changed only the citation field of one row (`thm:wn-s-matrix`). The flagged lines
are in separate theorem rows and section-divider tables and are out of scope for
the FZ92 discipline mission. A future dedicated audit should revisit:
- Line 1655 `thm:virasoro-self-duality` row: check whether the standalone title
  carries `c=13` scope qualifier on source chapter.
- Lines 1258/1260 cobar-betagamma/fermions rows: check proof-body scope (Omega(B)
  inversion vs derived center vs Verdier dual).
- Lines 39-41 Part I/II/III hardcoded-number occurrences in the summary table.
- Lines 360/361/375 admissible-non-Koszulness rows: check whether scope qualifiers
  carry "at denominator $q \geq 3$" distinction through downstream refs.
- Lines 2435/2439 $\kappa + \kappa^! = 0$ rows: verify family scope (KM/free: 0;
  Vir: 13; AP234 discipline).
These are not drifts introduced by this session's FZ92 heal.
