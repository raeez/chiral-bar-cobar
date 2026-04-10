# Ordered Drinfeld Centre Audit (Wave 14)

## (a) Most likely intended definition

The Wave 6-8 section points in one direction very clearly. At [`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1516`]( /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1516 )-1535, the text says the classical Drinfeld centre is an `E_2` invariant, but because `U_\cA` is built from the ordered bar coalgebra, the manuscript wants an `E_1` invariant and therefore makes a `"tentative identification"` with
\[
\RHom_{U_\cA \otimes U_\cA^{\mathrm{op}}}(U_\cA,U_\cA)
\]
computed on an `"ordered bar resolution"`. At [`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1552`]( /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1552 )-1558 this object is compared to the full complex `\ChirHoch^\bullet(\cA)`, not just degree zero. At [`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1584`]( /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:1584 )-1593, the “strictest case” reduction again identifies the pointwise centre with ordinary Hochschild cochains. Combined with Vol II locality rules `B^{\ord} \to B^\Sigma` and the claim that BD do not study this `E_1` notion ([`/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:36`]( /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:36 )-39), the intended object is not the monoidal Drinfeld centre of a braided category and not a BD-style chiral centre. It is the derived `E_1`-centre of an ordered `A_\infty` model.

The rigorous definition should therefore be:
\[
Z^{\ord}_{\mathrm{Dr}}(U)\;:=\;Z_{E_1}(U^{\ord}),
\]
where `U^{\ord}` is an `A_\infty` algebra model for the ordered `E_1`-chiral algebra `U`, built before the `R`-twisted `\Sigma_n`-coinvariant projection. In Lurie’s language this is the `E_1`-centre, i.e. the centralizer of `\id_U` in `\Alg_{E_1}`. Its underlying complex is
\[
C^\bullet(U^{\ord},U^{\ord})
\;\simeq\;
\RHom_{(U^{\ord})^e}(U^{\ord},U^{\ord}),
\]
with its canonical brace, hence `E_2`, structure. The adjective “ordered” means exactly: compute this on the ordered/open-colour model, not after descent to the symmetric/factorization object. One correction is unavoidable: the Wave 6-8 line `HH^0(U_\cA\text{-mod}) = RHom_{U_\cA^e}(U_\cA,U_\cA)` is not rigorous notation for a cochain complex. If the manuscript means the full derived centre, it should write `C^\bullet` or `HH^\bullet`; if it means the ordinary centre, it should write `H^0`.

## (b) Closest literature precedent

The closest precise precedent is Lurie, *Higher Algebra* (2017), `\S5.3.1`. At `Def. 5.3.1.12` he defines `Z_{\mathcal O}(A)`, and `Rem. 5.3.1.13` plus `Cor. 5.3.1.15` identify `Z_{E_k}(A)` as an `E_{k+1}`-algebra; for `k=1`, this is exactly the derived centre of an associative algebra with its `E_2` refinement. Earlier in the same section Lurie explicitly says that for `k=1` and `f=\id_A`, the construction recovers usual Hochschild cohomology of `A`.

Francis 2013, `\S3.1`, gives the closest chain-level formulation. `Def. 3.1` defines operadic Hochschild cohomology as `\Hom_{\mathrm{Mod}^O_A}(A,M)`. `Rem. 3.2` says that for associative algebras, `E_1`-Hochschild cohomology is ordinary Hochschild cohomology, and `Rem. 3.3` says that in `\Cat_\infty` these Hochschild cohomology categories are derived analogues of Drinfeld centres. This matches the Wave 6-8 oscillation between algebraic and categorical language.

BFN 2010 is the best categorical precedent I checked: the abstract states that the Drinfeld centre and Hochschild cohomology category coincide for `QC(X)`, and more generally that `E_n`-centres are higher Hochschild objects. This supports the slogan “Drinfeld-centre language becomes Hochschild language after passage to derived/categorical form.”

BD 2004 is the correct source for chiral algebras and chiral homology, but I did **not** verify a section there that defines an ordered or `E_1` centre. Attribution of a specific “chiral centre” construction to BD is therefore uncertain. Likewise, KS09 is the right `A_\infty` deformation-theory background, but I did not verify in that text the exact brace/`E_2` statement; that attribution is safer to place on the Deligne-conjecture literature.

## (c) Does this make `Z(U_\cA) \simeq \ChirHoch^\bullet(\cA)` tractable?

Yes, as a **tractable conjectural comparison**, not as a theorem available from the cited literature alone. Under the definition above, the conjecture becomes:
\[
Z^{\ord}_{\mathrm{Dr}}(U_\cA)\;\simeq\;\ChirHoch^\bullet(\cA).
\]
That is now a comparison of two Hochschild-type complexes with brace/`E_2` structure. The right-hand side already has such a model in the manuscript: [`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:570`]( /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/hochschild.tex:570 )-704 constructs chiral Hochschild cochains as a brace algebra on `\FM(\C)\times\Conf(\R)`, and the associated graded splits into BD-chiral and `E_1` Hochschild pieces. So the conjecture stops being undefined and becomes a concrete Hochschild-vs-Hochschild statement.

But it is not presently proved internally, for the same reason already admitted at [`/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1369`]( /Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ordered_associative_chiral_kd_core.tex:1369 ): the double `U_\cA` itself is “not yet constructed at the bar-complex level.” Until `U_\cA^{\ord}` exists as an actual `A_\infty` algebra or monoidal dg category, its Hochschild cochains are only formal notation.

## (d) What new construction is required?

Two genuinely new constructions are required.

First, an actual ordered `E_1`-chiral Drinfeld double `U_\cA^{\ord}` as an `A_\infty` algebra, or equivalently a monoidal dg category of ordered line operators presenting it. Vol II itself says `E_1`-chiral algebra in this sense is new ([`/Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:38`]( /Users/raeez/chiral-bar-cobar-vol2/CLAUDE.md:38 )-39), so this is not something the literature already supplies.

Second, an ordered-to-bulk comparison theorem: either a Morita statement identifying `Z_{E_1}(U_\cA^{\ord})` with the derived centre of the line-operator category, or a direct factorization-homology map from ordered Hochschild cochains of the double to `\ChirHoch^\bullet(\cA)`. That bridge is not in Lurie, Francis, BFN, or BD in the exact manuscript sense.

## (e) Recommended wording for `hochschild.tex`

If the manuscript wants to keep the phrase “ordered Drinfeld centre”, the safest installation is:

```latex
\begin{definition}[Ordered Drinfeld centre]
Let $U$ be an ordered $E_1$-chiral algebra, and let $U^{\ord}$ denote an
$A_\infty$ model built from the ordered/open-colour presentation
\textup{(}equivalently, before the $R$-twisted $\Sigma_n$-coinvariant
descent $B^{\ord}\to B^\Sigma$\textup{)}.  The ordered Drinfeld centre of
$U$ is the $E_1$-center
\[
Z_{\Dr}^{\ord}(U)\;:=\; Z_{E_1}(U^{\ord}),
\]
namely the center of $U^{\ord}$ in the sense of Lurie,
\emph{Higher Algebra}, \S5.3.  Its underlying cochain complex is
\[
Z_{\Dr}^{\ord}(U)
\;\simeq\;
C^\bullet(U^{\ord},U^{\ord})
\;\simeq\;
\RHom_{(U^{\ord})^e}(U^{\ord},U^{\ord}),
\]
equipped with the canonical brace, hence $E_2$, structure.
\end{definition}

\begin{remark}
This is not, by definition, the ordinary monoidal Drinfeld centre of a
braided category.  It is the ordered $E_1$-center of the ordered
$A_\infty$ model.  If $\Mod(U^{\ord})$ is compactly generated, Morita
invariance identifies $Z_{\Dr}^{\ord}(U)$ with the derived center of the
dg-category $\Mod(U^{\ord})$.
\end{remark}
```

If nomenclature is flexible, “ordered derived centre” is safer than “ordered Drinfeld centre”; the latter is defensible only after the definition above is installed.
