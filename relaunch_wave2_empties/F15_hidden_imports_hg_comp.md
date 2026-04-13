# F15_hidden_imports_hg_comp (current rerun)

## Findings

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:207` — PROBLEM: Definition `def:complementarity-complexes` declares a cochain involution `\sigma` on `\mathbf C_g(\cA)` and cites `thm:verdier-bar-cobar` at line `209`, but that theorem is the bar/Verdier identification at the Koszul-dual surface, not the moduli-level involution later constructed as `lem:verdier-involution-moduli` in the same chapter. The definition is using a stronger object before it is built. FIX: replace the citation by a forward reference to `lem:verdier-involution-moduli`, or state `\sigma` as additional data at the definition point and only identify it with Verdier duality after the lemma is proved.

- [CRITICAL] `chapters/theory/higher_genus_complementarity.tex:479` — PROBLEM: Step 3 of `thm:fiber-center-identification` identifies `\mathcal H^0(R\pi_{g*}\bar B^{(g)}_{\mathrm{flat}}(\cA))` with the center local system by citing `thm:obstruction-quantum`, but that theorem defines the center local system as `\mathcal H^0` of the endomorphism sheaf `\mathcal E^\bullet_{g,\mathrm{flat}}(\cA)=\mathcal End(\bar B^{(g)}_{\mathrm{flat}}(\cA))`, not of the bar pushforward itself ([higher_genus_foundations.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex:4654)). The proof is switching objects mid-argument. FIX: either insert a separate theorem identifying the bar pushforward with the derived endomorphism/center complex, or weaken the conclusion here to a provisional bar-side sheaf and stop calling it `\mathcal Z_\cA` without that comparison.

- [HIGH] `chapters/theory/higher_genus_complementarity.tex:1158` — PROBLEM: `cor:duality-bar-complexes-complete` pairs `\bar B^n(\mathcal A)` with `\bar B^n(\mathcal A^!)` using `\Omega^*_{\log}` on both sides, but the actual Verdier-duality lane in the repo pairs the `j_*` logarithmic-form surface with the `j_!` dual surface and requires the extension-exchange step. The current proof never imports that `j_*`/`j_!` exchange. FIX: rewrite the corollary in the Verdier-dual form, explicitly invoke the `j_*`/`j_!` exchange lemma before claiming a perfect pairing, and stop treating `\Omega^*_{\log}` as self-dual on both tensor factors.

## Summary

Checked: C0/C1 proof lane through `def:complementarity-complexes`, `thm:fiber-center-identification`, and `cor:duality-bar-complexes-complete` | Findings: 3 | Verdict: FAIL
