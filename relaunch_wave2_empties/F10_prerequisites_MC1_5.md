# F10_prerequisites_MC1_5 (current rerun)

## DAG

- `MC1` (`thm:master-pbw`) is the PBW lane. On the live surface it is supplied by the all-genera family PBW theorems in [higher_genus_modular_koszul.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_modular_koszul.tex:1367) and the propagation package around `thm:pbw-universal-semisimple`. Status: `PROVED`.
- `MC2` (`thm:universal-theta`) is the universal MC lane. It is fed by `thm:mc2-bar-intrinsic`, `prop:geometric-modular-operadic-mc`, `prop:mc2-reduction-principle`, and `thm:tautological-line-support`. Status: `PROVED`, with one live statement-level cycle noted below.
- `MC3` is cited through the Yangian/DK lane and is downstream of the local MC2 package rather than upstream of it on this surface. Status: `CITED/PROVED ELSEWHERE ON THE LIVE SURFACE`.
- `MC4` is the completion lane, anchored at `thm:completed-bar-cobar-strong` and the derived MC4 criteria in [bar_cobar_adjunction_curved.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/bar_cobar_adjunction_curved.tex:952). Status: `PROVED`.
- `MC5` splits on the live surface:
  analytic sewing (`thm:general-hs-sewing`) is `PROVED`;
  chain-level BV/BRST/bar identification remains conjectural on the cited surface.

## Findings

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:2336` — PROBLEM: `thm:three-tier-architecture` says each tier follows from its stated input alone, but Tier 0 still states “Theorem D ... holds unconditionally” at lines `2366-2368`, while concordance restricts the all-genera scalar formula to the proved uniform-weight lane and keeps genus `1` universal only ([concordance.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:59)). The same theorem also says HS-sewing is “automatic” from PBW alone at lines `2434-2437`, but `thm:general-hs-sewing` explicitly assumes both polynomial OPE growth and subexponential sector growth ([genus_complete.tex](/Users/raeez/chiral-bar-cobar/chapters/connections/genus_complete.tex:1389)). FIX: rewrite Tier 0 item `(0.4)` to “genus `1` universal; all genera on the proved uniform-weight lane; multi-weight `g>=2` via `thm:multi-weight-genus-expansion`,” and rewrite the Tier 2 conclusion to say HS-sewing is automatic only after adding the subexponential sector-growth hypothesis or after routing through the standard-landscape corollary.

- [CRITICAL] `chapters/theory/higher_genus_modular_koszul.tex:5673` — PROBLEM: `prop:mc2-reduction-principle` chooses the coefficient spaces `W_g` “for the modular-operadic package of Theorem~\ref{thm:universal-theta}`” at lines `5676-5680`, but the proposition is then used in the MC2 completion lane that feeds back into `thm:universal-theta` (see lines `8150-8157` and `8281-8296`). That is a live local cycle in the MC2 statement DAG. FIX: replace the reference to `thm:universal-theta` in the proposition statement by an intrinsic source of the coefficient spaces, e.g. `\Gmod` or the modular graph coefficient algebra from `prop:geometric-modular-operadic-mc`, so the reduction principle no longer depends on the theorem it helps recover.

## Summary

Checked: MC1-MC5 dependency lane in `higher_genus_modular_koszul.tex` plus directly cited support theorems | Findings: 2 | Verdict: FAIL
