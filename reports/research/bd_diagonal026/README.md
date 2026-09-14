# Ternary collision comparison

The integration includes, in order, are `research-candidates/bd_diagonal026/ternary-comparison-body.tex` and `research-candidates/bd_diagonal026/polynomial-ternary-body.tex`. Together they are a self-contained mathematical module. The second chapter completes the global polynomial extension identified by the first chapter.

The only style dependencies are the canonical mathematical theorem environments and standard mathematical packages. The chapter provides the macros HH and pp only when they are absent. All mathematical labels use the prefix `bd26-`. The bibliography key `BDdiagonal` is defined in the standalone wrapper. The integration owner can use that same entry in the combined bibliography.

The final result is a polynomial ternary cochain map into the actual Chevalley–Cousin complex of W on all 18 global source summands, retaining the prescribed mixed intermediate images and arbitrary finite inner poles. Weighted edge integrals supply the required positive-degree unmerged components. The note gives an equivariant average and a complete source for a right differential module comparison. At level zero, the map projects to the unextended native chiral algebra and sends an explicit source cycle to a nonzero cohomology class.

The Koszul target at nonzero level is contractible. Independent outer-pole localization is a different coefficient domain and retains the cubic obstruction. No Heisenberg state equivalence or all-arity comparison is claimed. Exact residuals are in proof-and-scope.md.

From this worktree:

```sh
/opt/homebrew/bin/python3 reports/research/bd_diagonal026/check_exact.py
python3 reports/research/bd_diagonal026/build.py
pdftoppm -r 100 -png reports/research/bd_diagonal026/build/ternary-comparison.pdf reports/research/bd_diagonal026/render/page
```

The standalone PDF is a local verification artifact. Only the main integration owner updates the combined reader PDF. Independent exact-candidate acceptance remains required.
