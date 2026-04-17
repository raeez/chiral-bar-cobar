# Wave-12 Heal: Vol III Part V Front-Matter Per-d Family Enumeration

**Wave-11 finding #77:** Vol III Part V front-matter (`~/calabi-yau-quantum-groups/main.tex:983-1070`) lacked per-d family enumeration. Only toric CY_3 was explicitly tabulated; the reader was forced to chase to Chapter~23 (`cy_d_kappa_stratification`) for the dimension stratification.

**Status:** VALID finding. Front-matter opened on the CY-D tri-stratum (holonomy classification) then jumped straight to the toric CY_3 landscape, skipping the per-d CY family table.

## Heal

Inscribed a new paragraph **"Per-dimension family enumeration"** immediately after the tri-stratum and before the toric CY_3 block, carrying one row per CY dimension $d \in \{1,2,3,4,5\}$.

### Table inscribed

| d | family | kappa_ch | target | note / physics |
|---|--------|----------|--------|----------------|
| 1 | E (elliptic curve) | 0 | E_1^ch | 1-loop string; Hodge (1,1) |
| 2 | K3 | 2 | E_2 | Heterotic on T^4; mock-modular theorem |
| 2 | abelian surface | 0 | E_2 | Hodge (1,4,1) |
| 2 | bielliptic | 0 | E_2 | étale Z/n quotient of E x E |
| 2 | Enriques | 0 | E_2 | double cover of K3 by Z/2 |
| 3 | quintic | 0 | E_1 | type IIA/B on Q_5 in P^4 |
| 3 | K3 x E | 0 | E_1 | duality web; kappa_BKM = c_N(0)/2 |
| 3 | E^3 | 0 | E_1 | abelian, maximal Aut |
| 3 | local P^2 | 3/2 | E_1 | non-compact; class M (NOT L) |
| 3 | conifold T*S^3 | 1 | E_1 | direct McKay; NOT local surface |
| 4 | CY_4 sextic | 2 | E_1 | M-theory compactification |
| 4 | K3 x K3 | 0 | E_1 | p_1-twisted; cascade terminates at E_3 |
| 4 | T^8 | 0 | E_1 | maximal abelian; trivial Yukawa |
| 5 | CY_5 generic | 0 | E_1 | F-theory; h^{p,q} = delta_{pq} generic |

### Honest-scope qualifiers inscribed

(a) **Conifold caveat**: NOT a local surface, so `kappa_ch = chi(S)/2` FAILS at T*S^3; direct McKay gives 1 (Cor. `cor:conifold-non-local-surface`, AP-CY34/AP-CY44).
(b) **K3 x K3 obstruction**: p_1(T_X) != 0 breaks the naive cascade to E_4; operad depth terminates at E_3 (pi_4(BU)=Z obstruction GROUP, not guarantee -- AP185).
(c) **CY_5 genericity**: h^{p,q}(X) = delta_{pq} is a generic statement; isolated loci in moduli carry extra Hodge classes.

### Russian-school voice anchors

- Bondal--Orlov (derived-category classification of CY manifolds).
- Kontsevich--Soibelman motivic Hall algebra (wall-crossing voice).
- Beauville--Bogomolov holonomy trichotomy (strict-CY vs holomorphic-symplectic).
- Physics register by dimension: d=1 1-loop string, d=2 Heterotic on T^4 (K3), d=3 IIA/B compactification (quintic), d=4 M-theory, d=5 F-theory.

### Discipline

- **HZ-7 (Vol III kappa subscript):** every kappa in the inscribed block is written `\kappa_{\mathrm{ch}}` or `\kappa_{\mathrm{BKM}}`. No bare kappa.
- **AP247 {Phi_d}:** the functor is written `\{\Phi_d\}_{d \ge 1}` (already the convention in surrounding front-matter).
- **AP236 metadata hygiene:** initial draft carried `FM43` as a scope tag for the n(d) recall; removed in follow-up edit -- no blacklist slug leaked into typeset prose. Replaced with "scope qualifier as stated in the introduction".
- **Edit scope:** strictly within Part V front-matter (main.tex ~1002-1050); no chapter body touched.

## Files touched

- `~/calabi-yau-quantum-groups/main.tex:1002-1050` (front-matter inscription).

## Open downstream

None surfaced by this heal. The framing chapter (Ch 23 `cy_d_kappa_stratification`) already carries the proof; this inscription lifts the reader-facing enumeration to the Part frontispiece.
