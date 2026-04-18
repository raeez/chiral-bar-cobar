# Wave 18 Retry: AP281 phantom bibkey `AF15`

Attribution: Raeez Lorgat

## 1. Phantom count before heal

Baseline phantom count before heal: `53` occurrences across `chapters/` and `standalone/`.

## 2. Inscribed bibkey and full BibTeX entry

Bibkey inscribed: `AF15`

```bibtex
@article{AF15,
  author  = {Ayala, David and Francis, John},
  title   = {Factorization homology of topological manifolds.},
  journal = {Journal of Topology},
  volume  = {8},
  number  = {4},
  pages   = {1045--1084},
  year    = {2015},
  eprint  = {1206.5522},
}
```

## 3. Grep verification

The bibkey is present in `standalone/references.bib`:

```text
$ rg -n '^@article\\{AF15\\}' standalone/references.bib
826:@article{AF15,
```

The manuscript still uses `AF15` in citation commands:

```text
$ rg -n '\\cite[a-zA-Z*]*\\{[^}]*AF15[^}]*\\}' chapters standalone | wc -l
41
```

Representative cite hits:

```text
$ rg -n '\\cite[a-zA-Z*]*\\{[^}]*AF15[^}]*\\}' chapters standalone | sed -n '1,8p'
chapters/examples/deformation_quantization.tex:794:Ayala--Francis \cite{AF15} develop factorization homology. The bar-cobar perspective:
standalone/theorem_index.tex:518:theorem & \detokenize{thm:fact-homology} & \detokenize{Factorization homology via configuration spaces {\cite{AF15,CG17,BD04}}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/configuration_spaces.tex:1195}\\
standalone/theorem_index.tex:598:theorem & \detokenize{thm:af-pkd} & \detokenize{Poincar\'e--Koszul duality, AF {\cite{AF15}}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/en_koszul_duality.tex:695}\\
standalone/theorem_index.tex:710:theorem & \detokenize{thm:verdier-NAP} & \detokenize{Verdier duality = NAP duality {\cite{AF15,KS90}}} & \texttt{ProvedElsewhere} & \detokenize{chapters/theory/higher_genus_foundations.tex:1426}\\
standalone/en_chiral_operadic_circle.tex:546:with $\En$ coefficients, developed by Ayala--Francis~\cite{AF15}
chapters/connections/thqg_open_closed_realization.tex:745:for factorization homology~\cite{AF15} to the boundary circle
chapters/connections/thqg_open_closed_realization.tex:774:sense of~\cite{AF15}: every finite subset of $S^1_p$ is contained
chapters/connections/thqg_open_closed_realization.tex:953:Ayala--Francis~\cite{AF15} ``$\otimes$-excision'' axiom for
```

This establishes the required two-sided resolution condition: the key `AF15` now exists in the bibliography database and is referenced by live `\cite{AF15}` sites in the manuscript surface.

## 4. Build consequence

Because `AF15` is now a concrete BibTeX entry in `standalone/references.bib` with the exact cited key, a standard bibliography pass against that database will resolve `\cite{AF15}` and will not emit `[?]` for this key.
