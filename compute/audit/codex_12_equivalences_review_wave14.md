**(a) Per-condition verdicts**

- (i) **PRECISE**. The theorem points to the canonical notion of chirally Koszul for the fixed PBW-filtered bar datum (L1904-1916; Definition at L234-246).
- (ii) **PRECISE**. This is the right PBW-degree concentration condition and respects CLAUDE AP75, which forbids replacing PBW degree by conformal-weight concentration (L1917-1919; `CLAUDE.md` AP75 at L302).
- (iii) **PRECISE**. The chapter separates bar-side `A_\infty` formality from Swiss-cheese formality, so AP14 is handled correctly (L1920-1923, L1120-1129, L2247; `CLAUDE.md` AP14 at L228).
- (iv) **PRECISE**. The Ext bigrading is defined earlier by cohomological degree and conformal weight, so `p != q` is well-scoped (L1924-1926; L1260-1265).
- (v) **PRECISE**. The counit quasi-isomorphism is a clean standalone condition and matches the inversion theorem’s statement (L1927-1930; `bar_cobar_adjunction_inversion.tex` L1618-1624).
- (vi) **PRECISE**. The BBL condition is technical but locally well-defined through the comparison functor on the fiber over the bar coalgebra (L1931-1933; `bar_cobar_adjunction_inversion.tex` L2310-2323).
- (vii) **PRECISE**. The quantifier “for all `g`” is explicit; it is stronger than what the reverse implication uses, but it is not ill-posed (L1934-1936, L2053-2060; `bar_cobar_adjunction_inversion.tex` L2383-2391).
- (viii) **WRONG**. The cited Hochschild theorems prove concentration and a polynomial Hilbert series, not that `\ChirHoch^*(\cA)` is a polynomial algebra with generators in degrees `{0,1,2}` (L1937-1940; `chiral_hochschild_koszul.tex` L538-567, L649-697).
- (ix) **IMPRECISE**. The supporting theorem only treats conformal vertex algebras with a Shapovalov form, so the meta-theorem overstates scope on arbitrary chiral algebras, including critical affine KM (L1941-1943; L1348-1352).
- (x) **IMPRECISE**. The variable `n` is free in the statement, violating the repo’s AP139 quantifier discipline; the supporting FM theorem correctly says “for all `n >= 2`” (L1944-1946; `bar_cobar_adjunction_inversion.tex` L2443-2449; `CLAUDE.md` AP139 at L713).
- (xi) **IMPRECISE**. The theorem-level caveat mentions perfectness and non-degeneracy, but the supporting Lagrangian theorem also assumes isotropic embeddings and later lists finiteness of the modular envelope as part of the conditional package (L1907-1908, L1952-1954; `bar_cobar_adjunction_inversion.tex` L2550-2557, L2588-2594).
- (xii) **PRECISE**. In the target theorem it is stated only as a one-way refinement, which matches the local caveat; the drift occurs later in concordance, not in the theorem statement itself (L1909-1910, L1955-1957, L2204-2215).

**(b) Proof circuit status**

**INCOMPLETE**. The satellite arrows `(i)↔(iv),(vi),(vii),(ix),(x)` each have either a theorem-sized local argument or a clean citation target. The core circuit does not. The line `(i)↔(ii)` is mis-cited to `thm:pbw-koszulness-criterion`, which is a one-way PBW deformation theorem under flatness and classical-Koszul hypotheses, not a general “Koszul iff `E_2` collapse” result (L1968-1972; L682-706). The line `(v)↔(viii)` is weaker still: `(v)->(viii)` cites a theorem proving Hochschild duality/concentration, while `(viii)->(v)` uses a ring-structure statement that is not locally proved (L1989-2008; `chiral_hochschild_koszul.tex` L649-697). I do not see strict circularity: the forward reference to `(iv)->(i)` at L2006-2007 is later discharged independently at L2155-2169.

**(c) Classical vs new**

Classical or standard lifts: (ii) Priddy-style bar purity, (iv) BGS Ext diagonality, (iii) Kadeishvili/Loday-Vallette formality, (v) bar-cobar inversion, and much of (vi) via Positselski plus Barr-Beck-Lurie. Programme-specific: (vii) factorization-homology concentration, (viii) Hochschild concentration/polynomiality on the chiral side, (ix) Kac-Shapovalov in bar-relevant range, (x) FM boundary acyclicity, (xi) shifted-symplectic Lagrangian transversality, and (xii) mixed-Hodge purity. No pair is literally duplicate, but (vi) is a categorical repackaging of (v), and (vii) is stronger than needed since the converse only uses `g=0`.

**(d) Top 3 gaps**

1. **Condition (viii) is overstated.** The theorem surface says “polynomial algebra with generators in degrees `{0,1,2}`”, but the cited Hochschild results prove only concentration and a polynomial Hilbert series. This breaks the most modern node of the core circuit (L1937-1940; `chiral_hochschild_koszul.tex` L649-697).
2. **The `(i)↔(ii)` backbone is not proved at stated generality.** The cited PBW theorem is one-directional and hypothesis-heavy. Unless another theorem is intended, the meta-proof lacks a general argument from chirally Koszul to PBW `E_2` collapse (L1968-1972; L682-706).
3. **Critical-level affine KM is not handled consistently.** I do not see the earlier `k=0` versus `k=-h^\vee` semantic slip inside the target block itself, but the theorem surface still fails the critical test: universal affine KM is declared Koszul at all levels including critical (L2608-2609, L2717-2719), condition (ix) is only defined for conformal algebras (L1348-1352), and the landscape table later says the critical affine spectral sequence does not collapse at `E_2` (`landscape_census.tex` L3799-3801, L3835-3838). I found no `c=1` bug; higher-rank `\mathcal W` determinant divisors are present only in example chapters (`w_algebras.tex` L2030-2072), not at theorem level.

**(e) Overall confidence**

**LOW**. Several satellite equivalences look salvageable, but the current load-bearing theorem surface has one wrong condition, one mis-cited backbone arrow, and unresolved critical-level scope drift. That is too unstable for the flagship “12 equivalences” claim.

**(f) Specific flagged lines**

`chiral_koszul_pairs.tex`: L1904-1910, L1937-1946, L1968-2008, L2172-2200, L2204-2215, L2346-2406, L2608-2609, L2717-2719.  
`bar_cobar_adjunction_inversion.tex`: L2443-2449, L2550-2557, L2588-2594.  
`concordance.tex`: L2367-2370.  
`landscape_census.tex`: L1078-1080, L1146-1149, L3799-3801, L3835-3838.  
`w_algebras.tex`: L2030-2072.
