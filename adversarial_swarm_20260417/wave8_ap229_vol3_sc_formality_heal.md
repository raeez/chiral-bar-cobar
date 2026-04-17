# Wave 8 — AP229 Vol III SC-formality Propagation Heal

**Date**: 2026-04-17
**Target**: AP229 "SC-formality propagation debt (Vol III stale)"
**Scope**: Vol III `~/calabi-yau-quantum-groups`
**Status**: HEALED (2 manuscript sites)

## Canonical Statement (Vol I anchor)

Per `chapters/theory/ftm_seven_fold_tfae_platonic.tex` lines 415-433:

- `prop:sc-formal-iff-class-g`: on the standard landscape, SC-formality is equivalent to class~$G$.
- `rem:sc-formal-parametrised-scope`: the unparametrised bidirection `SC-formal ⇔ PBW E_2-collapse` is FALSE as stated; class~$L$, class~$C$, class~$M$ standard-landscape members are Koszul but NOT SC-formal. The hub-and-spoke seventh equivalence is class-$G$-scoped.
- `prop:swiss-cheese-nonformality-by-class`: witnesses non-formality off class~$G$.

Definition: SC-formal means $m_k^{\mathrm{SC}} = 0$ for $k \geq 3$ (AP14).

## Vol III Grep Audit

**Manuscript sites (`chapters/**/*.tex`, `standalone/**/*.tex`)**: exactly 2 loci.

### Site 1: `chapters/connections/modular_koszul_bridge.tex:380`

Before:

> ...while SC-formality (which class~$G$ alone satisfies) is the stronger operadic condition that controls shadow-tower vanishing.

**Audit gates**:

- (a) Scope to class~$G$: present but thin.
- (b) Distinction from Koszulness (AP14): explicit and correct.
- (c) Metric-family distinction (AP218): not claimed metric, no drift.
- (d) Dioperad language: N/A here.
- (e) Vol I citation: **MISSING** (the AP229 propagation debt).

**Heal**: definition of SC-formality made explicit ($m_k^{\mathrm{SC}} = 0$, $k \geq 3$); added `Vol~I, Proposition~\ref{prop:sc-formal-iff-class-g}` and `prop:swiss-cheese-nonformality-by-class` + `rem:sc-formal-parametrised-scope`.

### Site 2: `chapters/theory/m3_b2_saga.tex:1149-1160`

Before:

> ...\emph{SC-formality} (vanishing of all higher $\Ainf$ operations $\mu_k$ for $k \geq 3$ on the Swiss-cheese complex, Chapter~\ref{ch:en-factorization}) are \emph{distinct} stratifications... only class~G is SC-formal.

**Audit gates**:

- (a) Scope to class~$G$: present.
- (b) Distinction from Koszulness: explicit.
- (c) Metric-family: not claimed.
- (d) Dioperad: N/A.
- (e) Vol I citation: **MISSING**.
- Minor convention: notation was $\mu_k$ for Swiss-cheese higher ops; Vol I canonical is $m_k^{\mathrm{SC}}$. Unified to $m_k^{\mathrm{SC}}$.

**Heal**: notation unified to Vol I canonical $m_k^{\mathrm{SC}}$; added Vol I citation.

## Cross-References Added

Both sites now cite `prop:sc-formal-iff-class-g` and `rem:sc-formal-parametrised-scope` from Vol~I (labels resolved via shared namespace, per Vol III convention for cross-volume references as in `k3e_cy3_programme.tex`).

## Side Observation (NOT healed; separate question)

`modular_koszul_bridge.tex:370,380` states `\cW_{1+\infty}` at $c=1$ is **class~M** (infinite shadow depth, MacMahon Euler product).
`m3_b2_saga.tex:1146-1147` states for $\C^3$, $S_3 = 0$ (**class~G**).

Both refer to the same CY object (C³ → `\cW_{1+\infty}` at c=1). These are internally inconsistent. This is orthogonal to AP229 (it's a shadow-stratification question, not an SC-formality propagation question) and is flagged for a future wave.

## Vol III CLAUDE.md Check

No SC-formality status-table entries in Vol III CLAUDE.md — nothing to sync.

## Compute / test hygiene

`compute/lib/swiss_cheese_cy3_e1.py`, `compute/lib/cross_volume_shadow_bridge.py`, and their tests already state "only class G is SC-formal" and "AP14: SC-formality ≠ chirally Koszul" correctly. No healing needed.

## AP5 Cross-Volume Propagation

Grep across all three volumes for `SC-formal|Swiss-cheese formal|SC-formality`: Vol~I canonical statements (ftm_seven_fold_tfae_platonic), Vol~II (compute/skill/test matches only, no stale status), Vol~III (2 manuscript sites now healed). No half-renamed inconsistencies.

## Files touched

1. `~/calabi-yau-quantum-groups/chapters/connections/modular_koszul_bridge.tex` (line 380 remark)
2. `~/calabi-yau-quantum-groups/chapters/theory/m3_b2_saga.tex` (lines 1149-1160 remark)

## Not committed

Per instructions.
