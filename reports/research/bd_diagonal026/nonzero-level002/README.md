# Native nonzero-level source extension

The mathematical include is `research-candidates/bd_diagonal026/nonzero-level002/nonadjacent-source-body.tex`. It is self-contained. Its wrapper uses the canonical shared style and bibliography key `BDnonadjacent`. Every new label begins with `bdnz-`.

The two accepted 026 modules remain byte-identical. This successor does not repeat their polynomial map into W. It fixes a numerical level k in C minus zero and uses the unextended native Heisenberg chiral complex throughout.

## Proof package

The support theorem restricts to U = X^3 minus (Delta12 union Delta23). The only remaining collision is Delta13. Its constant-word output is -k[1 delta13 partial_t | J2], with t = z1-z3. Adjacent-supported outputs vanish on this open set and cannot cancel it. The target has no proper-diagonal degree-minus-three states, so an output correction to the degree-minus-three word itself is also unavailable.

The minimal regular-function source carrier is N = R nu = R/(t^2), concentrated in degree minus two. The generator maps to the actual double-pole coefficient. The first normal multiple t nu is nonzero, and t^2 nu is zero. A source delta line R/(t) cannot represent this operation. Minimality means the cyclic image with this specified generator, not an assertion about all possible operadic source models.

For the selected word, beta(fe123) = -f(123)nu. It is zero on every other coefficient degree and word. The extension O+ = O directsum N has differential (bx,beta x), and fits the short exact sequence 0 -> N -> O+ -> O -> 0. This is a cochain-complex extension over R. It is not asserted to be a bar coalgebra or a product on the original state algebra.

The source's lowest cohomology is computed globally from the actual compatible families. Every ordered sector has basis z_sigma, m_sigma, n_sigma, where z_sigma = t_ij t_jk e_sigma + t_jk q_ij m_sigma + t_ij q_jk n_sigma. Closedness on the full simplex makes the unmerged coefficient an element of R. Restriction to each actual adjacent edge forces divisibility by the corresponding normal difference. Their coprimality forces the product. This proves the full H^-3 calculation without assuming a global coefficient formality theorem.

Write s = z2-z3 and p = s(t-s). The selected connecting map sends z123 to -p nu. Multiplication by p is injective on R/(t^2). Thus the H^-3 projection replaces R z123 by t^2 R z123, while all other basis components remain unchanged. In degree minus two, the exact sequence adds R/(t^2,p) as a submodule. It has transverse length four and basis 1,s,t,st over C[y]. The cohomology extension is not asserted to split.

After localizing at p, the small-diagonal quotient vanishes and beta is surjective. The actual closed ordered source e' = e123 + q12/t12 m12|3 + q23/t23 n1|23 has beta(e') = -nu. It has no closed lift. The native comparison sends the selected separated insertion to its actual three-current state and the new module identically to the native collision summand. It kills old mixed words and other source sectors. No quasi-isomorphic replacement preserving that projected source morphism can remove the obstruction: the two-term target connecting map is already nonzero on [e'].

An all-word variant uses the same single module N. Define beta_all(fe_sigma) = -sgn(sigma) f(sigma)nu. This gives a native comparison on U for all six separated ordered current insertions; all old mixed images are explicitly zero. The six global connecting coefficients, in order 123,132,213,231,312,321, are s^2-st, -st, st, st, -st, st-s^2 modulo t^2. Their image ideal is (s^2,st) in R/(t^2). The degree-minus-two small-diagonal quotient is consequently R/(t^2,s^2,st), with basis 1,s,t and transverse length three. The kernel of the lowest cohomology map is given by the displayed six-coefficient linear congruence. This all-word extension and the selected-word extension are distinct constructions; both remain in the source.

The new carrier's minimal right differential closure has the exact cyclic presentation D_R / (t^2 D_R + (t partial_t - 1)D_R + (partial_y - partial_s)D_R). Its independent images are finite normal derivatives of the vacuum tensored with T^n J. Normal ordering and T^n J = n! x_(n+1) prove that the listed relations are complete. Both native comparison variants extend after inducing the old source to right differential modules and using this quotient for the new carrier.

The binary connection proposition is a further deciding obstruction. A regular coefficient-compatible normal connection commuting with the unchanged binary bar differential would preserve the closed module R(te+uh) plus Rh. The e coefficient of the covariant derivative of te+uh, evaluated at u=0, is 1+tA(0). It cannot be divisible by t. Thus such a connection does not exist, at any level. This excludes the stated natural descent requirements; it does not classify every possible enlarged or altered state-translation source.

## Failed routes and exact residuals

An adjacent-only output correction fails on Delta13 intersect U, before any small-diagonal calculation. A simple delta source fails because the native image has two normal jets. An acyclic source replacement preserving the projected insertion fails because its derived connecting map is nonzero. Replacing the two-jet generator by a free right differential module without the displayed relations would enlarge the source unnecessarily and leave the new carrier's translation law unspecified.

The source extensions change cohomology. The length-four and length-three small-diagonal terms are explicit costs, not equivalences. The native map is defined on U, where both adjacent diagonals have been removed. A global current comparison with old mixed images retained is not proved. Relabeling produces each ordered open-domain comparison, but their compatibility and extension over the removed diagonals need new equations.

The old ordered source has only been induced to differential modules. The new collision carrier has exact descent relations, while a connection on the original symbols remains absent. The binary no-go proves that the regular coefficient-compatible prescription cannot supply it. Any replacement must state its changed coefficient action or extra source states and check the resulting relations against the comparison map.

No ordered-surjection, deconcatenation, associativity, or four-input compatibility has been constructed. No level was changed, no vacuum primitive was adjoined to V_k, and no acyclic state extension was identified with V_k.

## Verification

Run from the assigned worktree:

```sh
/opt/homebrew/bin/python3 reports/research/bd_diagonal026/nonzero-level002/check_exact.py
python3 reports/research/bd_diagonal026/nonzero-level002/build.py
```

The independent symbolic calculations retain the exact two-jet action, the normal Weyl relation, the global connecting matrix with determinant s^4, both finite small-diagonal quotients, and all six signed connecting coefficients. They also check the global cycle boundary coefficients and the deciding regular-connection endpoint. The general proofs remain in the source. No formal proof assistant was used.

The primary carrier citation was checked against the author-hosted Beilinson–Drinfeld Chapter 3, Section 3.4.11, equation (3.4.11.1), printed pages 182–183. The original primary PDF and its hash remain in the preserved 026 input closure. No novelty claim is made.

The build uses the canonical style through TEXINPUTS and writes only within this new report scope. Independent mathematical review of this new freeze remains required. Required mathematical controls remain gpt-6-astra and ultra; independently observed metadata remains unverified.
