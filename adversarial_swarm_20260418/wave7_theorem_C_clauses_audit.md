# Wave 7 — Theorem C clauses T1–T9 attack+heal audit

Date: 2026-04-18. Auditor voice: Etingof / Polyakov / Kazhdan / Gelfand / Nekrasov /
Kapranov / Bezrukavnikov / Costello / Gaiotto / Witten, channelled Beilinson-adversarial.
Target: CLAUDE.md Vol I Theorem C row + `chapters/theory/theorem_C_refinements_platonic.tex`
(613 lines, chunked 1–250 / 251–500 / 501–613 linear).

## Inscription provenance

- `chapters/theory/theorem_C_refinements_platonic.tex` is `\input`-ed at `main.tex:1218` (AP255 clean; file exists and compiles into the monograph).
- `standalone/multi_weight_cross_channel.tex:612` anchors `prop:delta-f-cross-w3-g2`. The standalone is NOT `\input`-ed into `main.tex` (grep: zero hits outside the in-file comment at :48). AP255 phantom-file-in-consumers **mitigated** by the in-chapter duplicate `thm:delta-f-cross-w3-g2` at `chapters/theory/koszulness_vii_multiweight_platonic.tex:311`, which is the live canonical reference target. The summary at :606–608 cites `thm:delta-f-cross-w3-g2` via koszulness_vii (not the standalone), so T8 is inscribed in-monograph; the standalone is an offline duplicate.
- `standalone/theorem_index.tex:2377` registers `prop:delta-f-cross-w3-g2` → standalone path. This is a label-collision hazard with the chapter's `thm:delta-f-cross-w3-g2` (AP124 near-miss: same slug, different environment prefix `prop` vs `thm`). Not a duplicate-label violation per prefix, but a reader may follow the theorem-index path into the non-inscribed standalone.

## Per-clause table

| Clause | Advertised | Inscribed | ClaimStatus | Scope | Verdict |
|---|---|---|---|---|---|
| T1 | DOWNGRADED to `conj:derived-center-koszul-equivalence` (brace dg / E_2 Deligne–Tamarkin); `lem:naive-center-koszul-identification` unconditional | YES, :122–135 `\begin{conjecture}` + :91–105 `\begin{lemma}` with proof | Conjectured / ProvedHere | Falsification test (`rem:derived-center-sharpened-scope`) at H^2 on Heis + Vir | CLEAN. Beilinson sharp. |
| T2 | CONDITIONAL on fiber-finiteness; Heis + affine KM non-critical unconditional; class-M boundary = `conj:perfectness-boundary-class-M` | YES, :232–275 + :333–347. `cor:c0-unconditional-class-G-L` :365–378 | ProvedHere (statement) + Conjectured (two sub-conj.) | Unconditional only at **positive integer level** and **boundary admissible level** (TUY + Arakawa); **generic non-critical KM** pushed to `conj:perfectness-boundary-km-generic` | **SCOPE NARROWER THAN CLAUDE.md**. CLAUDE.md Theorem C row says "unconditional for Heis + affine KM non-critical"; inscribed chapter says unconditional for Heis + affine KM *positive-integer* or *boundary-admissible*, with generic non-critical CONJECTURAL. **AP271 reverse drift** in CLAUDE.md. |
| T3 | C_1 reflexivity unconditional via `cor:c0-unconditional-class-G-L` | YES, :365–385 | ProvedHere | Same Heis + KM integer/admissible loci as T2; conditional elsewhere | CLEAN *if* T2 framing corrected. |
| T4 | RETRACTED (non-issue) — +3 shift is misreading of -(3g-3) at g=0 | YES, :401–414 `rem:plus-three-shift-nonissue` | Remark (no proof) | g=0 collapse explained; no theorem removed | CLEAN. |
| T5 | C_2 hypotheses pinned to BV + Verdier + bar-chart lift | Inscribed **at `higher_genus_complementarity.tex:2018`** (`thm:shifted-symplectic-complementarity`), NOT in this file; the summary at :599–601 says "consistent with the inscribed theorem, no changes required" | External — ProvedElsewhere in effect | Hypotheses named at the inscription site, not here | **AP266 SHARP CHECK**: the three BV-package conditions are named by reference; a reader needs to open `higher_genus_complementarity.tex:2018` to Beilinson-falsify them. Acceptable (chapter is a refinements ledger, not a re-inscription), but the summary would benefit from a single sentence listing the three hypotheses by name for local falsifiability. |
| T6 | FOLDED into T3 (`cor:c0-unconditional-class-G-L`) | YES, :602–603 | N/A | — | CLEAN. |
| T7 | MC5 strengthening closes class-M C_2(iii) weight-completed | **Not inscribed in this file**; :604–605 says "consistent with the MC5 weight-completed inscription, no changes here" | External — MC5 chapter | Scope: **weight-completed ambient**, explicitly | **Wave-14 AP296 inheritance check**: the Wave-14 filtration-vs-exact-weight heal scope (weight-completed ≠ direct-sum ambient) is *consistent* with the T7 framing. No pre-heal language in this chapter. CLEAN. |
| T8 | Explicit δF_2^cross(W_3) = (c+204)/(16c) in `standalone/multi_weight_cross_channel.tex` | Primary inscription at `chapters/theory/koszulness_vii_multiweight_platonic.tex:311` (`thm:delta-f-cross-w3-g2`, ProvedElsewhere forwarding to `thm:multi-weight-genus-expansion(vi)`); standalone `prop:delta-f-cross-w3-g2` is duplicate offline | ProvedElsewhere | W_3 at g=2 only; general (s, g) is Conjectural per `thm:multi-weight-genus-expansion` scope | CLEAN in-monograph. Standalone is **not `\input`-ed into main.tex**; CLAUDE.md advertising the standalone location is misleading-but-not-broken (AP255 near-miss, live reference via koszulness_vii). |
| T9 | `thm:C-PTVV-alternative` mixed: (i)+(ii) PTVV+HAG-II genuinely independent; (iii) forwards to `thm:quantum-complementarity-main` | YES, :436–479 with per-clause `\ClaimStatus`: (i) ProvedElsewhere, (ii) ProvedHere, (iii) Conjectured | Mixed, correctly split | `g ≥ 2` (g=0 separated by T4; g=1 collapsed) | CLEAN per-clause. **AP289 Künneth check**: PTVV shifted-symplectic form on RMap(M̄_g, BG_A) uses CY-dim(M̄_g) = 3g-3 additively with the 0-shifted form on BG_A → -(3g-3); this is additive within a single g and does NOT claim composition at g × g' (no cross-genus Künneth asserted). AP289 N/A here. **AP287 HZ-11 cross-volume check**: clause (iii)'s forward reference `prop:ptvv-lagrangian` lives in the same volume (`higher_genus_complementarity.tex:2195`). No HZ-11 violation. |

## Atomic heals applied

1. **FM7 LaTeX typo, line 331**: `\end{conjecture>` → `\end{conjecture}`. Build-breaking if the compiler is strict about matched delimiters; AP7/FM7 zero-tolerance. Healed in place via Edit.

2. **AP271 reverse-drift flag (CLAUDE.md vs inscription, not healed here)**: CLAUDE.md Theorem C row writes "unconditional for Heis + affine KM non-critical"; inscribed scope is "unconditional for Heis + affine KM positive-integer or boundary-admissible; generic non-critical is Conjectural (`conj:perfectness-boundary-km-generic`)". Parent agent should rectify CLAUDE.md to match manuscript:
   > C0 and C1 H-level eigenspace proved unconditionally on Koszul locus; C0 ordinary-derived realization conditional on perfectness, unconditional for Heisenberg and affine Kac–Moody at **positive integer or boundary admissible level**; **generic non-critical KM and class-M boundary-stratum recorded as Conjectures `conj:perfectness-boundary-km-generic` and `conj:perfectness-boundary-class-M`**; C2 shifted-symplectic upgrade conditional on BV package.

## Residual open (not healed — research frontier)

- **T1 chain-level brace qi** — expected failure in raw direct-sum class M; weight-completed ambient predicted to work (parallel to MC5 Wave-14 split). Falsification test at H^2 Heis/Vir inscribed (`rem:derived-center-sharpened-scope`), computable.
- **T2 generic non-critical KM boundary-stratum** — Kac–Kazhdan determinant formula supplies smooth-fiber finiteness; nodal propagation without TUY / Arakawa unresolved.
- **T2 class-M boundary-stratum** — Arakawa C_2-cofiniteness at nodal degenerations not inscribed family-by-family on M̄_g.
- **T9 clause (iii)** — intrinsic derived-stack anti-symplectic involution needed to decouple Lagrangian complementarity from `thm:quantum-complementarity-main`; this is the genuine frontier. Clause (i)+(ii) *are* independent via PTVV+HAG-II, per AP243 disjointness audit: V1 = PTVV Thm 2.5 on M̄_g (algebraic-geometric), V2 = HAG-II 3.3.3 tangent formula (derived algebraic geometry), V3 = naive-center explicit check on Heis + Feigin–Frenkel on KM (Lie-algebraic); disjoint at the literature + machinery + working-family level. HZ-IV decorator block at :538–572 records all three paths.

## Verdict

Chapter is honest. T1–T9 per-clause inscription matches advertised status, with two caveats: (a) FM7 typo at :331 (healed), (b) AP271 reverse-drift between CLAUDE.md Theorem C row and the inscribed T2 scope (flagged for parent, not healed here because CLAUDE.md edits are programme-governance not chapter-level). No AP255 phantoms, no AP242 forward-reference lemmas, no AP287 cross-volume attribution gaps, no AP266 BV-hypothesis black-box (named at the inscription site one jump away). T8 has a near-miss AP124 label-collision (prop vs thm with same slug) that is LaTeX-legal but reader-hostile; not healed here.
