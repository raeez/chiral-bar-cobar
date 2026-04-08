# Mixed Sector of SC^{ch,top} and the Brace Complex

## Hypothesis

The mixed sector of the SC^{ch,top} Koszul dual cooperad encodes the brace operations B_n(a; b_1,...,b_n) that control how bulk operators act on boundary states.

## Verdict

**Partially true, with an important disambiguation.** The hypothesis conflates two related but distinct algebraic structures that the brace dg algebra simultaneously encodes. The precise statement requires separating braces-on-cochains (the E_2 self-action of the bulk) from evaluation-on-elements (the mixed bulk-boundary coupling).

## Source Files Read

- `~/chiral-bar-cobar/chapters/theory/en_koszul_duality.tex` (Definition def:SC at line 1193; operadic center at def:operadic-center line 1452; chain-level center thm:operadic-center-hochschild line 1575; brace comparison Step 4 at line 2058; terminality thm:center-terminality line 2217; bar as SC-coalgebra thm:bar-swiss-cheese line 1219)
- `~/chiral-bar-cobar/chapters/connections/thqg_open_closed_realization.tex` (brace dg algebra thm:thqg-brace-dg-algebra line 170; derived center def:thqg-chiral-derived-center line 271; Swiss-cheese theorem thm:thqg-swiss-cheese line 323; local-global bridge thm:thqg-local-global-bridge line 418; annulus trace thm:thqg-annulus-trace line 519; open/closed MC element constr:thqg-oc-mc-element line 837; MC equation decomposition thm:thqg-oc-mc-equation line 865; projection principle thm:thqg-oc-projection line 926)
- `~/chiral-bar-cobar-vol2/chapters/connections/brace.tex` (brace operations def:brace-ops-brace line 31; geometric brace model line 63; MC-deformations thm:MC-deformations-brace line 95; bulk-cochains identification thm:bulk-CHC-brace line 116)
- `~/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex` (HCS primitive package thm:tw-hol-primitive-package line 1202)

## Part 1: The SC^{ch,top} Operad and its Three Sectors

The Swiss-cheese operad SC^{ch,top} (Definition def:SC, en_koszul_duality.tex line 1193) has two colors {ch, top} and three types of operation:

| Component | Space | Interpretation |
|-----------|-------|---------------|
| SC(ch^k; ch) = FM_k(C) | closed-to-closed | Holomorphic E_2 structure |
| SC(ch^k, top^m; top) = FM_k(C) x E_1(m) | mixed-to-open | Bulk acting on boundary |
| SC(..., top,...; ch) = empty | open-to-closed | FORBIDDEN (directionality) |

The bar complex B^ord(A) is an SC^{ch,top}-coalgebra (thm:bar-swiss-cheese): the differential d_B is the closed color (FM_k(C) collision residues) and the deconcatenation coproduct Delta is the open color (E_1 interval splitting).

## Part 2: The Operadic Center and the Chiral Hochschild Complex

The operadic center Z_SC(A) (def:operadic-center, line 1452) is the terminal closed-color algebra acting on a fixed open-color algebra A. At each arity (k,m), a center element is a map

    phi_{k,m} : FM_k(C) x E_1(m) -> Hom(A^m, A)

equivariant for the Sigma_k action on FM_k(C) and the E_1(m) action.

The center theorem (thm:operadic-center-hochschild, line 1575) proves:

    Z_SC(A) ~= C^*_ch(A, A)

as E_2-algebras. The identification at arity k is equation (center-bar-degree) at line 1664:

    Z_SC(A)_k = [Omega^*(FM_k(C), log D) tensor A^{boxtimes k} tensor A_out]^{Sigma_k}

which is exactly the chiral Hochschild cochain complex at bar degree k.

## Part 3: Dimension Analysis of the Mixed Sector

The Koszul dual cooperad SC^{ch,top,!} has mixed-sector dimension (AP87):

    dim SC^!(ch^k, top^m; top) = (k-1)! * C(k+m, m)

At the key component (k=1, m=n) -- one bulk operator acting on n boundary elements:

    dim = (1-1)! * C(1+n, n) = 1 * (n+1) = n+1

The n+1 generators correspond to the n+1 positions at which 1 closed leaf can be inserted among n ordered open leaves:

    Position 0: c | o_1 o_2 ... o_n
    Position i: o_1 ... o_i | c | o_{i+1} ... o_n
    Position n: o_1 o_2 ... o_n | c

This is the combinatorial content of the brace evaluation: a degree-p cochain f in Hom(A^p, A) can be evaluated on algebra elements at each of these insertion positions.

## Part 4: The Critical Disambiguation

The brace.tex file (Vol II) defines TWO distinct algebraic operations:

**(A) Braces of cochains on cochains** (def:brace-ops-brace, line 31):

    {f}{g_1,...,g_m} : C^*_ch(A,A) tensor C^*_ch(A,A)^{tensor m} -> C^*_ch(A,A)

These are the E_2/Gerstenhaber operations on the BULK algebra itself. They encode the self-interaction of bulk operators (closed-on-closed).

**(B) Mixed operations / evaluation** (thm:thqg-swiss-cheese, line 323):

    mu_{p;q}^univ : C^*_ch(A,A)^{tensor p} tensor A^{tensor q} -> A

These take p bulk cochains and q boundary algebra elements and produce a boundary element (closed-to-open).

These are DIFFERENT operations on DIFFERENT spaces. The brace (A) maps cochains to cochains; the mixed operation (B) maps cochains + elements to elements.

**They are related by evaluation.** A cochain f in C^n_ch(A,A) = Hom(A^n, A) can be evaluated on algebra elements. The mixed operation at (k=1, m=n) is exactly this evaluation:

    mu_{1;n}(f; a_1,...,a_n) = f(a_1,...,a_n)

This is established in the proof of thm:thqg-swiss-cheese (line 355-384): the morphism Phi: B -> C^*_ch(A,A) is defined by Phi(b)_n(a_1,...,a_n) = mu_{1;n}(b; a_1,...,a_n).

## Part 5: The Correct Statement

**The brace dg algebra (C^*_ch(A,A), {-}{-,...,-}) is the total algebraic structure that governs BOTH:**

1. The E_2 self-action of the bulk (brace of cochains on cochains = closed sector operations)
2. The mixed bulk-boundary coupling (evaluation of cochains on algebra elements = mixed sector operations)
3. The compatibility of (1) and (2) via the Leibniz/higher pre-Lie identities

**The Swiss-cheese theorem (thm:thqg-swiss-cheese) is the precise unification:** U(A) = (C^*_ch(A,A), A) is the TERMINAL local chiral open/closed pair. Every bulk algebra B acting on the boundary A factors uniquely through C^*_ch(A,A). The factoring map is exactly "evaluate cochains on algebra elements."

**What the mixed sector IS:** The (k,m) component of the open/closed convolution algebra g^oc decomposes into four sectors (thm:thqg-oc-mc-equation, line 877):

| Sector | Range | Content |
|--------|-------|---------|
| Pure closed | k >= 1, m = 0 | Bar complex / Theta_A |
| Pure open | k = 0, m >= 1 | A_infty module operations |
| Mixed | k >= 1, m >= 1 | Bulk-boundary couplings = cochain evaluation |
| Clutching | hbar*Delta | Modular sewing (genus raising) |

The mixed sector at (k,m) encodes how k bulk operators simultaneously act on m boundary elements. At (k=1, m=n) this is the single-bulk-operator action; at (k >= 2, m >= 1) this is iterated bulk action, encoding the E_2-module axioms for A as a module over C^*_ch(A,A).

## Part 6: Heisenberg Computation at (k=1, m=1)

For the Heisenberg VOA H_k (single generator J of weight 1, OPE J(z)J(w) ~ k/(z-w)^2):

The mixed MC equation at (1,1) in the open/closed convolution algebra requires consistency of the bulk-boundary action:

    delta(mu_{1;1}) + [m_2, mu_{1;1}] = 0

where m_2 is the binary chiral product. This encodes: the action of the composite (a *_ch b) on a boundary state m equals the iterated action a(b(m)).

For the Fock module F_k at level k: J_n acts as p * delta_{n,0} on momentum eigenstate |p>. The zero-mode J_{(0)} acts as a scalar (the momentum), so the mixed MC equation at (1,1) is automatically satisfied: J_{(0)}(J_{(0)}m) = J_{(0)}^2 m = p^2 m.

## Part 7: HCS Physical Verification (Affine KM Boundary)

For 3d holomorphic Chern-Simons with gauge algebra g at level k (thm:tw-hol-primitive-package, examples-worked.tex line 1202):

- Boundary algebra: A = V_k(g) (affine Kac-Moody)
- Bulk: Z^der_ch(A) = C^*_ch(V_k(g), V_k(g))
- Collision residue: r(z) = Omega_g / z (classical r-matrix)

The mixed MC equation at (1,1) with two KM currents J^a, J^b and a module element m:

    mu_{1;1}(J^a *_ch J^b; m) = mu_{1;1}(J^a; mu_{1;1}(J^b; m))

The left side: mu_{1;1}(f^{ab}_c J^c; m) = f^{ab}_c J^c_{(0)} m.
The right side: J^a_{(0)}(J^b_{(0)} m).

The mixed MC equation becomes:

    f^{ab}_c J^c_{(0)} m = [J^a_{(0)}, J^b_{(0)}] m

This is the statement that J_{(0)} furnishes a Lie algebra representation of g on the module M. This is the classical content of the KM module axioms.

At higher mixed components (1,n): the mixed MC equation reproduces the n-point bulk-boundary Ward identity.

## Part 8: Deligne Conjecture Connection

The (k >= 2, m >= 1) components of the mixed sector are the HIGHER mixed operations. At (k=2, m=1), dim = C(3,1) = 3, corresponding to 3 ways to place 2 closed and 1 open leaf: (cco, coc, occ). These encode how the Gerstenhaber bracket [f,g] acts on boundary elements, plus A_infty corrections.

The full mixed sector at all (k,m) is exactly the data of an E_2-module structure on A over C^*_ch(A,A). This is the chiral analogue of the Deligne conjecture: the operadic center Z_SC(A) = C^*_ch(A,A) acts on A via the E_2 module structure, and the braces are the coordinate expression of this action.

The comparison theorem (thm:operadic-brace-comparison, en_koszul_duality.tex line 2140) proves the three models agree as E_2-algebras:

1. Operadic center Z_SC(A)
2. Chiral Hochschild cochains C^*_ch(A,A) with braces
3. Derived endomorphism algebra REnd_{A^e}(A)

## Conclusions

1. The hypothesis "mixed sector of SC^{ch,top,!} = brace complex" is **partially true**: the mixed sector encodes the evaluation of cochains on algebra elements, which is the MODULE structure defined by the braces. It is NOT the brace self-composition (which is the E_2 closed-sector structure).

2. The brace dg algebra is the **unifying algebraic structure** that simultaneously governs both the closed-sector E_2 self-action and the mixed-sector bulk-boundary coupling. The Swiss-cheese theorem (thm:thqg-swiss-cheese) is the precise formulation.

3. The dimension (k-1)! * C(k+m,m) of the mixed cooperad component counts insertion positions for closed leaves among ordered open leaves. At (1,n) this gives n+1, matching the number of positions at which a single bulk operator can be inserted into a boundary sequence.

4. The mixed MC equation at (1,1) for HCS reproduces the Lie algebra action of g on modules (zero-mode algebra = g). At (1,n) it gives the n-point Ward identity.

5. **No new errors found in the manuscript.** The existing treatment in thqg_open_closed_realization.tex correctly distinguishes the four sectors of the MC equation, correctly identifies the mixed projection with the Swiss-cheese coupling, and correctly states the terminality of U(A).

6. **Potential improvement:** Neither volume currently contains a proposition explicitly stating "the (1,n) mixed sector of g^oc is the brace evaluation B_n(f; a_1,...,a_n) = f(a_1,...,a_n)." This is implicit in the proof of thm:thqg-swiss-cheese (the map Phi is defined by evaluation) but not isolated as a standalone result. Adding such a proposition would make the mixed-sector = brace-evaluation identification explicit.
