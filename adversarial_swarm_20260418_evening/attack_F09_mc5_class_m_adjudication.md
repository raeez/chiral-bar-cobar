# F09 Attack: MC5 class M direct-sum vs pro-ambient
## Two framings

1. Raw direct-sum falsity in Vol I [chapters/theory/theorem_B_scope_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:381):

> "Let $\cA \in \{\mathrm{Vir}_c, W_N\text{-algebras}, V_{-h^\vee}(\mathfrak{g})\}$ be a class-M chiral algebra, and let $C = \bar{B}^{\mathrm{ch}}(\cA)$ be its raw (non-completed) chiral bar coalgebra with the direct-sum conformal-weight grading. Then $C$ is not conilpotent, the chiral co-contra correspondence ... does not apply directly to $C$, and no strengthening of the coderived framework recovers the equivalence ... on the raw direct sum."

L_0 witness, same file [lines 397-407](/Users/raeez/chiral-bar-cobar/chapters/theory/theorem_B_scope_platonic.tex:397):

> "the element $L_0 \in \bar{B}^1(\mathrm{Vir})$ has $\bar{\Delta}^{(N)}(L_0) \neq 0$ for every $N \geq 1$ because the infinite sum over the Cartan modes never terminates in the raw direct sum."

2. Pro-ambient chain-level theorem in Vol I [chapters/theory/mc5_class_m_chain_level_platonic.tex](/Users/raeez/chiral-bar-cobar/chapters/theory/mc5_class_m_chain_level_platonic.tex:229):

> "Let $\cA$ be a class-$\mathsf{M}$ chiral algebra ... let $f_g := \{f_g^{(\leq N)}\}_{N \geq 0} \in \mathrm{Mor}(\mathrm{pro}\text{-}\mathrm{Ch}(\mathrm{Vect}))$ be the induced morphism of pro-objects. Then $f_g$ is a chain-level quasi-isomorphism in $\mathrm{pro}\text{-}\mathrm{Ch}(\mathrm{Vect})$: at each weight-truncation stage $N$, the finite-stage map $f_g^{(\leq N)}$ is a strict chain-level quasi-isomorphism ... and the tower satisfies the Mittag--Leffler condition ..."

## Compatibility check

These are complementary, not contradictory.

- The proposition is explicitly about the raw non-completed bar coalgebra with the direct-sum conformal-weight grading in bounded `Ch(Vect)`.
- The theorem is explicitly about the inverse system of finite-weight truncations in `pro-Ch(Vect)`.
- Vol I already resolves the relation in prose [mc5_class_m_chain_level_platonic.tex:198-220](/Users/raeez/chiral-bar-cobar/chapters/theory/mc5_class_m_chain_level_platonic.tex:198):

> "The statement `genuinely false' is restricted to the bounded-direct-sum ambient $\mathrm{Ch}(\mathrm{Vect})$, which is not the ambient of the original bar complex once its weight filtration is retained."

So the direct-sum failure is genuine inside the naive ambient, but it does not negate the pro / completed theorem.

## Headline framing

`CLAUDE.md` does not support a global headline "MC5 class M false" without an ambient qualifier.

- The detailed status row at [CLAUDE.md:586](/Users/raeez/chiral-bar-cobar/CLAUDE.md:586) headlines: `PROVED at coderived level weight-completed only`, then separately says `Raw class-M direct-sum level: GENUINELY FALSE`.
- The reconstitution line at [CLAUDE.md:1378](/Users/raeez/chiral-bar-cobar/CLAUDE.md:1378) says: `MC5 chain-level class M — CLOSED weight-completed ... direct-sum class M genuinely false, correct scope`.
- The shorter line at [CLAUDE.md:1374](/Users/raeez/chiral-bar-cobar/CLAUDE.md:1374), `MC5 chain-level (class M false)`, is therefore shorthand and ambient-ambiguous if read in isolation.
- The concordance gives the clean canonical headline at [chapters/connections/concordance.tex:1980](/Users/raeez/chiral-bar-cobar/chapters/connections/concordance.tex:1980): `analytic, coderived, and canonical-ambient chain-level proved`, with bounded direct-sum failure marked as the naive-ambient exception.

## Verdict

VERDICT: both labels are true, but at different scopes.

`GENUINELY FALSE` is correct for the raw bounded direct-sum ambient `Ch(Vect)`; the `L_0` witness and the nonzero `S_4(\mathrm{Vir}_c)` obstruction make that a real mathematical failure, not a proof-gap artefact.

As a headline for MC5 class M itself, however, "direct-sum false" is an ambient-choice artefact. The canonical repository framing is: chain-level MC5 for class M is proved in the pro-object / `J`-adic / filtered-completed ambient, and fails only after one forgets that retained filtration/topology and insists on the naive bounded direct-sum ambient.
