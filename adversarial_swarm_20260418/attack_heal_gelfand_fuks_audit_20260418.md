# Gelfand-Fuks vs Chiral Hochschild — Citation Discipline Audit

**Date:** 2026-04-18
**Author:** Raeez Lorgat
**Scope:** Brief verification audit; no inscription changes. Single residual misattribution flagged for follow-up.

## Verdict

Both prior-session heals landed. One residual FF84 misattribution at `chapters/theory/hochschild_cohomology.tex:288` for a rank-1 Gel'fand-Fuchs claim; flagged, not healed in this audit per AP314 (minimal inscription).

## (i) Prior-heal verification

Both sites from this session's prior report verified clean:

- `chapters/theory/hochschild_cohomology.tex:161` — `\cite{Fuks86}` for $H^*_\mathrm{cont}(L_1; \C) = \C[\Theta]$. Correct primary source (Gel'fand-Fuks classical; Fuks86 Ch. 2 is the canonical Western-language reference). Heal landed.
- `chapters/theory/conformal_anomaly_rigidity_platonic.tex:163` — `\cite{Fuks86}` for $H^2(\mathrm{Witt}; \C) = \C$. Correct. Heal landed.

The FF84 citation nearby at `conformal_anomaly_rigidity_platonic.tex:155` is on a DIFFERENT object — $\Hch^\bullet(\Virc, \Virc)$ the Ext-group on the Virasoro algebra, for which FF84 (Verma modules over Virasoro, LNM 1060, 1984) is genuinely the primary source. No conflation.

## (ii) Programme-wide FF84 audit on Witt / Vect(S^1) / continuous-Lie-algebra content

Enumeration of every `\cite{FF84}` in Vol I (scope: `chapters/**`, `standalone/**`, `appendices/**`):

| Site | Object cited | Verdict |
|---|---|---|
| `chapters/theory/conformal_anomaly_rigidity_platonic.tex:155` | $\Hch^\bullet(\Virc, \Virc)$ at generic $c$ | CORRECT (FF84 Verma/reducibility) |
| `chapters/theory/conformal_anomaly_rigidity_platonic.tex:454` | Same (Dependencies para) | CORRECT |
| `chapters/theory/chiral_modules.tex:1410` | Minimal-model values $c_{p,q} = 1 - 6(p-q)^2/pq$ | CORRECT |
| `chapters/theory/chiral_modules.tex:1397` | Generic irreducibility of Verma modules | CORRECT |
| `chapters/theory/chiral_modules.tex:3826` | Kac determinant | CORRECT (co-cited with Kac) |
| `chapters/examples/minimal_model_examples.tex:491` | Virasoro minimal model characters | CORRECT |
| `chapters/theory/hochschild_cohomology.tex:288` | **$H^*_\mathrm{cont}(\mathrm{Lie}(\Walg), \ldots; \C) = \C[\Theta_1, \ldots, \Theta_r]$ at $r = 1$** | **FLAG: misattribution** |

The `hochschild_cohomology.tex:288` site cites `FF84` as a secondary reference for the rank-1 Gel'fand-Fuchs cohomology of the Virasoro-like subalgebra. FF84 is Verma-module / Kac-determinant work; it does not establish the continuous Lie algebra cohomology of $L_1$. Canonical primary sources are Gel'fand-Fuks 1970 (original) and Fuks86 Ch. 2 (already cited alongside). The `; \cite{FF84} for r=1` clause is a residual AP1941-class misattribution from the prior healing pass.

Minimal heal (non-inscribed here, flagged for follow-up): remove the `; Feigin--Fuchs~\cite{FF84} for $r = 1$` clause, OR reattribute to Feigin 1988 (Usp. Mat. Nauk 39, "Semi-infinite homology of Lie, Kac-Moody, and Virasoro algebras") which genuinely treats the rank-1 $L_1$ continuous cohomology in a Virasoro-specific setting.

Also noted: `chapters/theory/motivic_shadow_tower.tex:513` carries inline prose `Feigin--Fuchs 1984` without `\cite{FF84}` bibkey. Mathematical content (FF84 Ext-group vanishing at weight 5) is correct; citation hygiene is non-canonical (AP281-class prose-without-bibkey). Minor.

## (iii) Gelfand-Fuks / ChirHoch cooccurrence — non-conflation check

Two sites juxtapose the two objects explicitly for DISAMBIGUATION (not conflation):

- `hochschild_cohomology.tex:156-172` (`rem:gf-vs-chirhoch`) — states verbatim `This is \emph{not} the chiral Hochschild cohomology ... the former is the cohomology of a topological Lie algebra (no curve geometry), while the latter is an Ext-group on the curve $X$'. Discipline correct.
- `hochschild_cohomology.tex:279-298` (`rem:gf-walg-vs-chirhoch`) — $W$-algebra analogue, explicit Hilbert-series contrast $1/(1-t^2)$ vs $1 + t^2$. Discipline correct.

No site was found that conflates the two objects. The ChirHoch(Vir_c) agent's contrast inscription stands.

## (iv) Godbillon-Vey

Zero programme-wide occurrences of `Godbillon` in Vol I `.tex`. The ChirHoch(Vir_c) agent's reference to `Godbillon-Vey + Euler tower' was a prose reminder of the infinite-dimensionality mechanism for $H^*_\mathrm{cont}(\mathrm{Vect}(S^1); \C)$, not an inscription. No misattribution to audit.

## Summary

- Two prior heals verified landed.
- Six FF84 citations correct; one residual misattribution at `hochschild_cohomology.tex:288` flagged (rank-1 Gel'fand-Fuchs, not FF84 territory).
- One prose-non-bibkey at `motivic_shadow_tower.tex:513` flagged (hygiene only; content correct).
- GF vs ChirHoch disambiguation discipline holds programme-wide; two explicit non-conflation remarks.
- No Godbillon-Vey inscriptions to audit.

## AP register (minimal per AP314)

No new AP inscribed. The residual misattribution at `hochschild_cohomology.tex:288` is an instance of the already-catalogued AP272 (unstated cross-lemma via folklore citation) sub-case where a bibkey is reached for reflexively under `Fuchs` attribution without verifying the specific theorem matches the source's content. No new pattern; existing AP272 discipline covers it. Flagged for a future two-line Edit (remove `; Feigin--Fuchs~\cite{FF84} for $r = 1$` clause) outside this audit's scope.
