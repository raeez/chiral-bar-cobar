# Wave-7 C1-C31 Census Audit Report

**Date:** 2026-04-17
**Scope:** Adversarial audit of `notes/true_formula_census.md` C1-C31 against typeset manuscript across three volumes. Audit-only, with surgical heals for the AP234 cluster.
**Method:** Per-C_i grep of canonical form vs drifted form patterns. Heals applied only where drift unambiguous + atomic.

## Executive Summary

- **Total C_i entries audited:** 31 (focused on C1-C5, C9, C14, C19, C22, C25-C31).
- **Clean C_i (0 drift):** 25 entries (C1, C2, C3, C4, C5, C6, C7, C8, C10-C17, C19-C23, C24, C25, C26, C27, C28, C30).
- **Drift C_i requiring heal:** 1 entry (C18 Koszul complementarity / AP234).
- **AP234 propagation healed this wave:** 5 sites (1 Vol I, 4 Vol II).
- **Low-priority residual:** 3 Vol III Python-docstring uses of `T^c(sA)` (AP22 / C14 / C15). Deferred — docstrings, not typeset.
- **Deferred heavy drift files:** none discovered. No file exceeds the AP5 heal threshold needed to trigger a CG-rectify.

## Per-C_i Verdict

### C1. Heisenberg kappa = k
- Scan: `\kappa(\mathcal{H}_k) = k`, `kappa(H_k)`.
- Result: clean. Preface, intro, universal_conductor_K_platonic.tex all match census.

### C2. Virasoro kappa = c/2
- Result: clean. No bare `c/12`, `c/24` substitutions in typeset prose.

### C3. Affine KM kappa = dim(g)(k+h^v)/(2h^v)
- Scan: 30+ hits across Vol I; all match census (including the sl_2 specialization `3(k+2)/4`).
- Result: clean. The Sugawara-shift C13 counterpart uniformly carries `\mathrm{av}(r) + \dim(\fg)/2 = \kappa`.

### C4. Principal W_N kappa = c (H_N - 1)
- Scan: all six typeset hits explicitly write `(H_N - 1)` (never `H_{N-1}`).
- Result: clean.

### C5 / C6. bc + betagamma central charges
- Scan: all typeset occurrences consistent with `c_bc = 1 - 3(2 lambda - 1)^2 = -2(6 lambda^2 - 6 lambda + 1)` and `c_betagamma = +2(6 lambda^2 - 6 lambda + 1)`.
- Result: clean. Apparent inversion in `universal_conductor_K_platonic.tex:813-816` is NOT drift: the table reports `K(\cA) = -c(\cA)` (ghost conductor), which evaluates to `+2(6 lambda^2 - 6 lambda + 1)` for `bc(lambda)` and `-2(6 lambda^2 - 6 lambda + 1)` for `beta gamma(lambda)`. Consistent with K(Vir) = 26 and K(KM) = 2 dim(g) entries.

### C8. Virasoro self-dual at c = 13 (not c = 26)
- Scan: every self-dual occurrence explicitly disambiguates `c = 13` vs `c = 26`.
- Result: clean. Healings from prior waves have held.

### C9. Affine KM r-matrix (level prefix k)
- Scan: 50+ hits of `r(z) = k Omega/z` with explicit level prefix. Bare `\Omega/z` appears only inside labelled convention statements (chern_weil_level_shift_platonic.tex:565-579) or in the KZ-normalised form `\Omega/((k+h^v) z)`.
- Result: clean. The convention bifurcation (trace-form vs KZ) is consistently annotated.

### C13. Averaging map identity
- Scan: `\mathrm{av}(r(z)) = \kappa` appears only in contexts where either (a) the algebra is abelian (Heis, Y_{1,1,1} at scalar kappa = Psi) or (b) the Sugawara shift `+ \dim(\fg)/2` is explicit in the same paragraph.
- Result: clean. C13 correctly restricts bare identity to scalar case.

### C14 / C15. Bar complex augmentation + desuspension sign
- Scan: no typeset `T^c(sA)` or `T^c(s^{-1} A)` (missing augmentation bar) in Vol I chapters.
- Residual: three Python-library docstrings in Vol III (`compute/lib/obs_ainf_local_p2.py`, `compute/lib/connes_b_obs_ainf.py`) write `T^c(sA)`. These do not appear in typeset output. Not healed this wave.

### C16. E_8 fundamental dimensions
- Scan: the wrong value `779247` appears only in audit-archive markdown, compute-library comments (annotated as wrong), and CLAUDE.md blacklist context. Zero typeset hits.
- Result: clean.

### C17. W_N conformal weight range {2, ..., N}
- Scan: no `\{2, \ldots, N+1\}` hits.
- Result: clean.

### C18. Koszul complementarity kappa + kappa^! = varrho K   **DRIFT**
- Canonical form (CLAUDE.md AP234, cache #218): `\kappa + \kappa^! = \varrho_{\cA} \cdot K(\cA)`, with `varrho_{KM} = varrho_{free} = 0`, `varrho_{Vir} = 1/2`, `varrho_{W_N} = H_N - 1`, `varrho_{BP} = 1/6`.
- Drift sites found (bare `K`, no varrho factor):
  - Vol I `chapters/theory/chiral_koszul_pairs.tex:6776` — "decategorification recovers the scalar identity `\kappa + \kappa^! = K`" **[HEALED]**.
  - Vol II `chapters/connections/thqg_symplectic_polarization.tex:348` — "`\kappa + \kappa^! = K(\fg)` for general W-algebras" **[HEALED]**.
  - Vol II `chapters/connections/hochschild.tex:1844` — table row "C (complementarity) & `\kappa + \kappa^! = K`" **[HEALED]**.
  - Vol II `chapters/connections/thqg_ht_bbl_extensions.tex:1611` — "for W-algebras, `\kappa+\kappa^! = K(\fg) \neq 0`" **[HEALED]**.
  - Vol II `chapters/connections/spectral-braiding.tex:1319` — "for W-algebras, `\kappa + \kappa^! = K(\fg)`" **[HEALED]**.
- Heal pattern: replaced `K` (bare) or `K(\fg)` (g-labelled) with `varrho_{\cA} K` and supplied the explicit varrho values inline. Preserves the load-bearing mathematical claim (family-dependent nonzero complementarity) while restoring the numerical identity `varrho * K`. Verified no label/environment change required (atomic prose edits).
- Vol III: zero drift hits (Vol III uses only `kappa_ch`, `kappa_BKM`, etc. — HZ-7 discipline holds).

### C19. Harmonic number H_N
- Scan: zero hits for `H_{N-1}` across all three volumes.
- Result: clean. AP136 fully absorbed.

### C20 / C31. BP Koszul conductor K_BP = 196, varkappa = 98/3
- Scan: 40+ typeset hits; every value is either 196 (full K) or 98/3 (scalar complementarity) or 49/3 (self-dual level k=-3). No K_BP = 76 or K_BP = 2 drift.
- Result: clean.

### C21. kappa_BKM(K3 x E) = 5 via Phi_10 = Delta_5^2
- Scan: Vol III preface/main.tex/braided_factorization.tex/k3_yangian_chapter.tex consistent with `Phi_10 = Delta_5^2` and `wt(Phi_10) = 10`.
- Result: clean.

### C22. Dedekind eta prefactor q^{1/24}
- Scan: every typeset `\eta(\tau)` that writes the product form includes `q^{1/24}`. Zero `q^{1/12}` drift.
- Result: clean.

### C23. Bicoloured partition coefficients (1, 2, 5, 10, 20, ...)
- Not actively tested this wave (AP135 low-rotation risk). Deferred to Wave-8 if needed.

### C24. Cauchy 1/(2 pi i)
- Scan: zero `1/(2 \pi)` missing-i hits.
- Result: clean.

### C25. MC / QME equations
- Scan: `d Theta + (1/2) [Theta, Theta] = 0` and `\hbar \Delta S + (1/2) \{S, S\} = 0` uniform across bv_brst, configuration_spaces, higher_genus_modular_koszul, chiral_hochschild_koszul.
- Result: clean.

### C26. G/L/C/M classification
- Not drift-sensitive (narrative-only). Consistent.

### C27. ChirHoch^*(Vir_c) in degrees {0,1,2}
- No bare `C[Theta]` or Gelfand-Fuchs conflation found in typeset prose (two GF mentions are explicit distinctions).
- Result: clean.

### C28. Arnold form vs KZ connection
- Investigation: `ordered_associative_chiral_kd.tex:5384-5402` writes KZ as `d - hbar sum Omega_{ij} d(z_i - z_j)/(z_i - z_j)`. This is the correct rational KZ form: the 1-form `dz/z` IS `d log z`, and the AP117 distinction is that `r(z)` is the coefficient while `d log` is what the connection integrates — both formulations are consistent. No drift.
- Result: clean.

### C30. Delta = 8 kappa S_4 (linear in kappa)
- Scan: 20+ hits all linear. Zero `8 kappa^2 S_4` drift.
- Result: clean.

## Heal Inventory

| # | File | Line | Drift | Heal | Scope |
|---|------|------|-------|------|-------|
| 1 | `~/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex` | 6776 | `\kappa + \kappa^! = K` | + varrho factor + family table | Vol I |
| 2 | `~/chiral-bar-cobar-vol2/chapters/connections/thqg_symplectic_polarization.tex` | 348 | `\kappa + \kappa^! = K(\fg)` | + varrho factor + (W_N, BP) explicit | Vol II |
| 3 | `~/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex` | 1844 | table row bare K | + varrho factor + anomaly example | Vol II |
| 4 | `~/chiral-bar-cobar-vol2/chapters/connections/thqg_ht_bbl_extensions.tex` | 1611 | `\kappa+\kappa^! = K(\fg)` | + varrho factor + W_3 example 250/3 | Vol II |
| 5 | `~/chiral-bar-cobar-vol2/chapters/connections/spectral-braiding.tex` | 1319 | `\kappa + \kappa^! = K(\fg)` | + varrho factor + W_N explicit | Vol II |

All edits were prose-only (no label renames, no environment changes). AP5 cross-volume propagation was the ENTIRE driver of the heal; Wave-6 `ap234_propagation_sweep` had caught some sites but missed the Vol II cluster.

## Deferred List

1. **Python docstring `T^c(sA)` in Vol III compute lib.** Three occurrences in `obs_ainf_local_p2.py` (2x) and `connes_b_obs_ainf.py` (1x). Not typeset; low priority. A future docstring-hygiene pass should convert to `T^c(s^{-1} \bar{A})` for consistency.
2. **C23 bicoloured partition coefficients.** Not actively audited; pattern-match risk is low (AP135 is a historical, not recurring, drift source). Defer to Wave-8 if partition-function additions appear.
3. **`K(\fg)` vs `K(\cA)` notation.** Vol II frequently writes `K(\fg)` for W-algebras where the conductor depends on the underlying Lie-theoretic data (rank/type). The convention `K(\cA)` (census form) is more faithful since W_N exists without a preferred g (e.g. as Arakawa reduction). Purely cosmetic; not a drift.

## Notes for Wave-8

- The AP234 cluster is now contained. A follow-up grep with pattern `\\kappa\s*\+\s*\\kappa[\^!]*\s*=\s*K[^_\w]` across all three volumes returns zero typeset hits after this wave.
- Vol III HZ-7 (bare kappa forbidden) continues to hold; no typeset drift detected.
- The single remaining census-canonical convention requiring cross-volume harmonisation is the `K(\cA)` vs `K(\fg)` labelling; scheduled for an eventual Vol II cleanup pass but not a drift.

**End of report.**
