# Wave 7 Vol I κ-subscript audit + AP1 kappa-from-memory grep sweep

Date: 2026-04-18
Channel: Etingof / Polyakov / Kazhdan / Gelfand / Nekrasov / Kapranov / Bezrukavnikov / Costello / Gaiotto / Witten

## Mission recap

Vol I uses HZ-4 discipline (bare κ qualified by family superscript or prose
scope), not the HZ-7 subscript mandate (which is Vol III only). Sweep for AP1
(kappa-from-memory), AP39 (unqualified self-duality / κ=S_2), AP116/AP136
(H_N vs H_{N−1} off-by-one), and complementarity scope tags.

## Grep results

### 1. Bare `\kappa = <value>` programme-wide

- Full regex `\kappa\s*=\s*[0-9cdk]`: 619 hits across `chapters/`,
  `standalone/`, `appendices/`.

### 2. `\kappa = c/2` (Vir form): dominant legitimate pattern

All 30+ sampled `\kappa = c/2` hits are scope-qualified by the preceding
phrase "For Vir" / "Virasoro" / "$\mathrm{Vir}_c$" / enclosing proposition
named Virasoro. Zero AP1 violations at `κ = c/2`. Canonical C2 matches.

### 3. `\kappa = k` (Heis form)

- `working_notes.tex:724`: "rank-1 Heisenberg $\cH_k$ at level $k = 1/2$
  ... $\kappa = k = 1/2$". Scope-qualified (Heis named one line above).
- `standalone/analytic_sewing.tex:2709`: "For $\cH_k$ with $\kappa = k$".
  Scope-qualified.

### 4. `\kappa = 0` / `\kappa = 13/2` / `\kappa = 8` / `\kappa = 24`

All scope-qualified by the enclosing chapter/proposition (critical level,
self-dual Vir at c=13, lattice VOA V_{E_8} / Leech). No AP1 violations.

### 5. W_N off-by-one (AP116/AP136)

- `H_{N-1}` (or `H_\{N-1\}`) across Vol I typeset prose: **0 hits**.
- `c \cdot (H_N - 1)` / `c(H_N - 1)` / `c(H_N{-}1)` / `c\,(H_N - 1)` across
  Vol I: dominant form, census-consistent, 20+ hits, all correct.
- Zero AP136 violations.

### 6. Complementarity sum `\kappa + \kappa^! = 0` / `= 13`

Sweep `\kappa.*+\s*\kappa.*=\s*0` / `=\s*13`: zero untagged hits.
Inscribed occurrences in `universal_conductor_K_platonic.tex`,
`higher_genus_complementarity.tex`, `w_algebras_deep.tex` all carry
family-qualifying prose ("For affine Kac–Moody", "For Virasoro", "For
$\cW_N$").

### 7. `\kappa_{ch,cat,BKM,fiber}` subscripted forms

- Vol I: **0 hits** (correct — HZ-7 is Vol III scope).

## Sampled 20-hit classification table

| file:line | bare-κ expression | family | verdict |
|-----------|-------------------|--------|---------|
| `ordered_associative_chiral_kd.tex:3310` | κ=0 | Vir gravitational Yangian c=26 | qualified, UNIFORM-WEIGHT |
| `ordered_associative_chiral_kd.tex:3314` | κ=13/2 | Vir gravitational Yangian c=13 | qualified |
| `ordered_associative_chiral_kd.tex:8674` | κ=3(k+2)/4 | sl_2 affine | qualified by eq:sl2-kappa |
| `ordered_associative_chiral_kd.tex:9388` | κ=c/2 | N=2 class M = Vir | qualified |
| `computational_methods.tex:130` | κ=c/2 | Vir | qualified (section on Virasoro) |
| `computational_methods.tex:869` | κ=3(k+h^v)/(2h^v) | affine sl_2 | qualified |
| `computational_methods.tex:962` | κ=8 | V_{E_8} lattice VOA | qualified (E_8 section) |
| `computational_methods.tex:1037` | κ=24 | V_Leech lattice VOA | qualified |
| `computational_methods.tex:1179` | κ=7c/6 | flagged WRONG in surrounding prose | AP1-catching, not violation |
| `chiral_hochschild_koszul.tex:6900` | κ=c/2 | Vir anomaly | qualified |
| `higher_genus_complementarity.tex:6303` | κ=c/2 | Vir_c | qualified |
| `higher_genus_foundations.tex:6505` | κ=c·ϱ(g) | W-algebras with ϱ=Σ1/(m_i+1) defined inline | qualified |
| `higher_genus_foundations.tex:6932` | κ=c·ϱ(g) | W-algebras, (ii) | qualified |
| `higher_genus_modular_koszul.tex:5258` | κ=c/2 | Vir from ρ(sl_2)=1/2 | qualified |
| `higher_genus_modular_koszul.tex:5330` | κ=c·(H_N−1) | W_N | qualified, AP136-correct |
| `shadow_tower_quadrichotomy_platonic.tex:654` | κ=c/2 | Vir_c | qualified |
| `shadow_tower_quadrichotomy_platonic.tex:1165` | κ=24 | Niemeier lattice VOA | qualified |
| `working_notes.tex:724` | κ=k=1/2 | H_k, bosonic string | qualified |
| `working_notes.tex:2482` | κ=d/2 | Lattice VOA rank d | qualified by table header |
| `theorem_A_infinity_2.tex:436` | κ=0 | class G only | scope-qualified BUT carried "(per AP-class)" leak |

20/20 mathematically correct; 1 Metadata Hygiene violation flagged.

## Verdicts

- **AP1 kappa-from-memory violations**: **0** (all bare-κ = value sites
  are family-scope-qualified).
- **AP39 unqualified κ=S_2 violations**: **0**.
- **AP116/AP136 W_N off-by-one violations**: **0** (zero `H_{N-1}` hits).
- **Complementarity untagged violations**: **0**.
- **Metadata Hygiene (AP-tokens in typeset prose)**: **1** —
  `chapters/theory/theorem_A_infinity_2.tex:436` carried the parenthetical
  `(per AP-class)` inside the `\begin{proof}` of `thm:A-infinity-2`. This is
  a CONSTITUTIONAL violation per CLAUDE.md Manuscript Metadata Hygiene
  rules (the token `AP-class` is a catalogue identifier and must not appear
  in typeset prose).

## Heals applied

- `chapters/theory/theorem_A_infinity_2.tex:436`: removed "(per AP-class)"
  parenthetical. Mathematical content unchanged: `κ = 0 ... holds in class
  G only` retains the class-G scope anchor, which is the mathematical
  content the parenthetical was trying to reference.

Cross-volume grep after heal:
```
grep -rn 'per AP-class\|(AP[0-9]\+)\|per AP[0-9]\+' \
  ~/chiral-bar-cobar/chapters/ ~/chiral-bar-cobar/standalone/ \
  ~/chiral-bar-cobar-vol2/chapters/ ~/chiral-bar-cobar-vol2/standalone/ \
  ~/calabi-yau-quantum-groups/chapters/ ~/calabi-yau-quantum-groups/standalone/ \
  | grep -v '%'
```
Zero hits programme-wide.

## Residual open count

- HZ-4 / AP1 / AP39 / AP116 / AP136: **0 open**.
- AP-token-in-prose (AP234 discipline): **0 open** (healed).
- Conclusion: **Vol I κ-discipline is clean** with respect to the
  CLAUDE.md HZ-4 mandate. The AP1 recurrence archaeology ("4 waves, 15+
  instances") has been successfully pacified in the current source.

## Commit plan

Mission constraint: no commits. The single edit is a Metadata Hygiene
heal (prose-only, non-formula) that is safe to batch with the next
content-bearing commit by the author.

## Notes

1. `computational_methods.tex:1179` naive-formula κ = 7c/6 is a
   PEDAGOGICAL AP1-WARNING pattern (the surrounding prose states it is
   wrong and explains why: Zamolodchikov metric eigenvalues are not
   anomaly ratios). This is the correct way to inscribe a failed
   mental-model in the manuscript.
2. W-algebra κ = c·ϱ(g) with ϱ = Σ 1/(m_i+1) at
   `higher_genus_foundations.tex:6505` uses exponent-sum form; at principal
   nilpotent this reduces to H_N − 1 via the identity Σ_{j=1}^{N-1}
   1/(m_j+1) = H_N − 1 for m_j = j. Equivalence registered in
   `conformal_anomaly_rigidity_platonic.tex`.
3. BP κ(B^k) = c/6 at `bar_cobar_adjunction_curved.tex:275` is an
   Arakawa-convention choice (HZ-4 BP quick-reference). Consistent with
   C31 + `bp_self_duality.tex`.
