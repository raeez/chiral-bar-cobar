# Chiral Koszul Duality — definitive reconstruction source

This bundle contains the complete LaTeX source of the normative reconstruction, its bibliography, the independent finite-window verification harness, generated verification outputs, the archive-separator generator, and integrity manifests.

## Build the normative PDF

From `src/` run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document uses standard TeX Live packages. The source is split into:

- `frontmatter.tex`
- `part1_foundations.tex`
- `part2_duality.tex`
- `part3_examples.tex`
- `part4_physics.tex`
- `part5_audit.tex`
- `appendices.tex`
- `references.bib`

## Reproduce the finite-window checks

```bash
python computations/verify_bar_models.py
```

This regenerates `verified_results.json` and `verification_report.txt`. The harness uses exact rational arithmetic and explicit normalized-bar matrices; it does not infer homology dimensions from chain-space counts.

## Claim-status discipline

The normative PDF distinguishes:

- proved in the displayed hypotheses;
- computationally verified in a stated finite window;
- standard theorem with an explicit citation;
- conditional construction requiring named geometric or analytic inputs;
- conjectural frontier.

The source witnesses in the collected archive are preserved verbatim, but the normative reconstruction governs how incompatible claims are resolved.
