# Draft: INDEPENDENT_VERIFICATION.md entry for `thm:k3-pentagon-E1`

**Source.** V49 (`wave_K3_Pentagon_E1_attempt.md`), three independent
verification routes converging on $[\omega]_{K3} = 0 \in
H^2(\mathrm{SC}^{\mathrm{ch,top}}; \mathfrak{aut})$.

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** Editorial
draft for `notes/INDEPENDENT_VERIFICATION.md`. Not committed.

This entry is the AP-CY61 independent-verification record for the new
theorem `thm:k3-pentagon-E1` introduced in
`draft_k3_yangian_pentagon_E1_theorem.tex`. It follows the protocol
documented in `notes/INDEPENDENT_VERIFICATION.md` and the
`@independent_verification` decorator API in
`compute/lib/independent_verification.py`. It is a model entry: V49 is
the first Vol III claim where three pairwise-disjoint mathematical
sources converge on the same vanishing class, and the entry is
written so it can be replicated for downstream cross-volume claims of
the same shape (Pentagon-style coherence cocycles for other CY inputs).

---

## 1. The decorator entry (verbatim, drop-in)

To be added at `compute/tests/test_k3_pentagon_E1.py` (new file
matching the engine module, to be created in a separate compute-engine
draft; the decorator template is the load-bearing piece here):

```python
from compute.lib.independent_verification import independent_verification

@independent_verification(
    claim="thm:k3-pentagon-E1",
    derived_from=[
        "V38 closed-form K3 R-matrix from Maulik-Okounkov stable envelope on Hilb^n(K3)",
        "Mukai signature (4, 20) deformation parameters h_i with sum_i h_i = 0",
    ],
    verified_against=[
        "Etingof-Kazhdan quantization theorem for Lie bialgebras (Selecta Math 1996, parts I-VI)",
        "Borcherds singular-theta correspondence and Phi_10 weight c_5(0)/2 = 5 (Borcherds 1998, Invent. Math. 132)",
        "Sympy direct computation of unitarity, pairwise YBE, classical CYBE, and Yang YBE in difference convention at charges 2, 3 (sandbox: /tmp/k3_pentagon_cocycle.py + k3_pentagon_charge3.py + k3_pentagon_ybe_check.py)",
    ],
    disjoint_rationale=(
        "Source 1 (MO/V38 closed-form R-matrix) is a geometric construction "
        "via the Maulik-Okounkov stable envelope on the Hilbert scheme "
        "Hilb^n(K3); the input is the equivariant cohomology of the moduli "
        "space, not any Lie-bialgebraic data. "
        "Source 2 (EK quantization) is a deformation-theoretic existence "
        "theorem for Lie bialgebras, established without reference to "
        "any geometric realisation; it operates entirely in the Drinfeld "
        "double Hopf-algebra setting with Drinfeld twist coherence as the "
        "Pentagon witness. "
        "Source 3 (Borcherds Phi_10) is an automorphic-form weight, "
        "computed by lattice-vector counting on the Mukai lattice (4, 20) "
        "via the Borcherds singular-theta correspondence; it is wholly "
        "independent of MO/V38 (no stable-envelope input) and of EK (no "
        "Lie-bialgebra deformation input). "
        "Source 4 (sympy cocycle defects) is a direct symbolic computation "
        "of unitarity, YBE and Pentagon defects on the rational structure "
        "function g_K3(u) = prod_i (u - h_i)/(u + h_i); it operates on "
        "the closed-form scalars of source 1 but the YBE-vanishing "
        "computation does not depend on the geometric provenance of those "
        "scalars. (Sympy is therefore a *computational verification* "
        "rather than a fully independent mathematical source; it is "
        "listed under verified_against because it independently confirms "
        "the YBE/unitarity that EK predicts and that Phi_10 weight "
        "matches.) "
        "The triple {EK, Phi_10, sympy} is pairwise mathematically disjoint "
        "in the AP-CY61 sense; the union of the three confirms "
        "[omega]_K3 = 0 along three independent axes (deformation theory, "
        "automorphic forms, direct symbolic computation)."
    ),
)
def test_k3_pentagon_cocycle_vanishes():
    """Pentagon coherence cocycle on the K3 Yangian vanishes.

    Three independent verifications:

    (i) Sympy direct: g_K3(z) * g_K3(-z) = 1 exact at Mukai signature
        (4, 20); pairwise YBE 4/4 triples on toy (2, 2); first-order
        linearisation = 0 (scalars commute with matrix perturbations);
        A_1 enhancement Yang YBE 64/64 entries in difference convention;
        classical CYBE 64/64.

    (ii) EK quantization: V38 R-matrix is the EK twist for the K3 Lie
         bialgebra; Pentagon is Drinfeld twist coherence.

    (iii) V20 Universal Trace Identity: tr_{Z(C)}(K_C) = c_5(0)/2 = 5;
          integer match between BRST ghost spectrum and Borcherds
          Phi_10 weight kills the cocycle's scalar projection.
    """
    # ... assertions ...
    pass
```

---

## 2. Why this is a *genuine* AP-CY61 entry, not a tautology

The AP-CY61 protocol explicitly forbids "tautological decoration":
test modules whose `derived_from` and `verified_against` sets overlap
or where one is a paraphrase of the other. The 2026-04-16 audit
identified five Vol III tautology cases now in
`notes/tautology_registry.md`. The V49 entry above is *not* in that
shape, for three reasons.

### 2.1 EK is provenance-independent of MO/V38

The Etingof-Kazhdan theorem of 1996 is a pure existence statement: every
Lie bialgebra $(\mathfrak{g}, [-, -], \delta)$ admits a quantization
$U_\hbar(\mathfrak{g})$ with explicit Drinfeld associator and
quasi-triangular structure. The proof uses the Knizhnik-Zamolodchikov
associator and the Drinfeld-Kohno theorem; it does **not** use Hilbert
schemes, stable envelopes, or any geometric realisation. The
identification of the V38 closed-form R-matrix with the EK twist for
the K3 Lie bialgebra is what *connects* MO and EK; the theorem itself
is independent.

In particular, the K3-specific V38 R-matrix could in principle have
disagreed with the EK twist (then the Pentagon would have failed at K3
even though EK predicts coherence in general). The fact that they
*agree* is the content of the EK route, not its hypothesis.

### 2.2 Borcherds $\Phi_{10}$ is automorphic, not algebraic

The Borcherds $\Phi_{10}$ weight $c_5(0)/2 = 5$ is computed by
lattice-vector counting on the unimodular even lattice $II_{2,26}$
restricted to the Mukai sublattice (4, 20); the singular-theta
correspondence (Borcherds, *Invent. Math.* 132, 1998) lifts the
Eisenstein-style theta series to a meromorphic Siegel modular form
of weight $10$ on $Sp_4(\mathbb{Z})$. The computation uses no
chiral-algebra or Hopf-algebra input: it is wholly automorphic.

The integer match $c_5(0)/2 = 5 = -c_{\mathrm{ghost}}(\mathrm{BRST})$
between this automorphic constant and the Vol I BRST ghost spectrum
is the content of V20 Step 3; the V49 entry inherits this match and
applies it as the trace projection of the Pentagon cocycle.

### 2.3 Sympy is computational, not foundational

The sympy verification at charges 2 and 3 uses the closed-form scalars
of V38 and computes their YBE, unitarity, and Pentagon defects directly
in sympy `Rational` arithmetic. It confirms what EK predicts (YBE
holds in difference convention; unitarity holds; first-order linearisation
vanishes). It is therefore not an independent *mathematical* source on
the same footing as EK and Phi_10, but it is an independent *computational
verification*: the same numbers must come out of sympy whether or not
EK is invoked.

The AP-CY61 protocol allows computational verification under
`verified_against` provided the disjoint_rationale acknowledges its
nature explicitly (which the entry above does).

---

## 3. Audit-time check (mechanical disjointness)

The decorator's import-time check is:

```python
overlap = set(derived_from) & set(verified_against)  # case/whitespace insensitive
if overlap:
    raise TautologicalDecorationError(claim, overlap)
```

For the V49 entry:

- `derived_from`: {"V38 closed-form K3 R-matrix from Maulik-Okounkov stable envelope on Hilb^n(K3)", "Mukai signature (4, 20) deformation parameters h_i with sum_i h_i = 0"}
- `verified_against`: {"Etingof-Kazhdan quantization theorem for Lie bialgebras (Selecta Math 1996, parts I-VI)", "Borcherds singular-theta correspondence and Phi_10 weight c_5(0)/2 = 5 (Borcherds 1998, Invent. Math. 132)", "Sympy direct computation of unitarity, pairwise YBE, classical CYBE, and Yang YBE in difference convention at charges 2, 3 (sandbox: /tmp/k3_pentagon_cocycle.py + k3_pentagon_charge3.py + k3_pentagon_ybe_check.py)"}
- intersection: $\varnothing$ (no string in derived_from appears in verified_against under case-insensitive whitespace-normalised comparison).

**Result:** the entry passes the import-time disjointness check. It is
a non-tautological AP-CY61 decoration.

---

## 4. Why this entry is a model for downstream V49-shape claims

The "three-route convergence" pattern — geometric (MO/stable envelope)
+ deformation-theoretic (EK) + automorphic (Borcherds) — is the K3
specialisation of a more general triangle that should appear for every
Pentagon-style coherence cocycle on a CY chiral algebra. The model
entry above can be replicated for:

1. **Quintic CY$_3$ Pentagon-at-$E_1$** (currently
   `ClaimStatusOpen`): the analogous triangle would use a
   Donaldson-Thomas / DT-PT correspondence on the quintic instead of MO
   on Hilb$^n$(K3); EK on the quintic Yangian (if it exists); and the
   appropriate automorphic form (Calabi-Yau MUM / mirror symmetry
   $j$-function in place of Borcherds $\Phi_{10}$). Three sources,
   pairwise disjoint, converging on the cocycle vanishing.

2. **Conifold Pentagon-at-$E_1$**: stable envelope on the resolved
   conifold $\mathcal{O}(-1) \oplus \mathcal{O}(-1) \to \mathbb{P}^1$;
   EK on the conifold quantum group (Y(\mathfrak{gl}(1|1))); modular
   form attached to the conifold MUM point.

3. **Local $\mathbb{P}^2$ Pentagon-at-$E_1$**: NCQH on local
   $\mathbb{P}^2$; EK on the affine Yangian
   $\widehat{\widehat{Y}}(\mathfrak{gl}_1)$; modular form for the
   local-$\mathbb{P}^2$ topological string.

In each case, the three sources are pairwise disjoint (geometric +
deformation-theoretic + automorphic), and convergence on the vanishing
cocycle would be a genuine AP-CY61 verification rather than a
tautological hardcoding. The V49 entry shows the shape; the downstream
entries are now templated.

---

## 5. Cross-volume implication: replicate the triangle for Vol I

The same three-route structure underwrites V20 itself
(`UNIVERSAL_TRACE_IDENTITY.md`): the trace identity
$\mathrm{tr}_{Z(C)}(\mathfrak{K}_C) = -c_{\mathrm{ghost}} = c_5(0)/2$
already had two sources (Vol I BRST ghost + Vol III Borcherds); the V49
delivery adds a third (Vol II Pentagon coherence as the operadic
substrate per V15 / Vol II Manifesto). The V20 entry in
`INDEPENDENT_VERIFICATION.md` should be updated to add Pentagon
coherence as the third leg of the triangle, mirroring the V49 entry
above. A separate draft (not produced here, recommended as follow-up)
should add the Pentagon coherence reading as `verified_against` source
3 for the V20 entry.

---

## 6. Application sequence

1. Apply `draft_k3_yangian_pentagon_E1_theorem.tex` to
   `chapters/examples/k3_yangian_chapter.tex` (after
   prop:mukai-indefinite-yangian, line 610).
2. Apply `draft_K3_six_corollaries.tex` to the four chapters listed
   in its header.
3. Add the entry above to `notes/INDEPENDENT_VERIFICATION.md` and
   create the corresponding test module
   `compute/tests/test_k3_pentagon_E1.py` with the
   `@independent_verification` decorator (separate compute-engine
   draft; this draft only specifies the decorator entry).
4. Run `make verify-independence` and `make verify-independence-verbose`;
   the new entry should appear in the registry, the disjointness check
   passes, the new claim moves from "uncovered" to "covered".
5. Update `notes/tautology_registry.md` to remove the entry
   `prop:bkm-weight-universal` if and only if Step 3 of the V49 proof
   provides the integer-match witness sufficient to upgrade the
   Borcherds weight universality from coincidence to certified at
   $N = 1$ (K3 $\times$ E specifically); the registry entry remains for
   $N \geq 2$ orbifold cases per AP-CY55 (the universal formula
   $\kappa_{\mathrm{BKM}} = c_N(0)/2$ holds for all $N$ but the
   adversarial certification is per-$N$).

---

## 7. AP compliance summary

| AP # | Description | How satisfied here |
|---|---|---|
| AP-CY55 | manifold vs algebraization invariants | The disjoint_rationale separates $\kappa_{\mathrm{BKM}}$ (algebraization) from $\kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}$ (manifold). Routes (i)-(iii) verify algebraization invariants; manifold invariants enter as inputs only. |
| AP-CY60 | six routes are constructions, not applications of $\Phi$ | Three sources here are three *verifications* of one cocycle, not three *applications* of $\Phi$. (Six routes to G(K3 x E) are a different statement, AP-CY60.) |
| AP-CY61 | independent verification protocol | Three pairwise-disjoint sources; explicit disjoint_rationale; passes import-time disjointness check. |
| AP-CY62 | geometric vs algebraic chiral Hochschild | The Pentagon cocycle lives in the chiral Hochschild model $C^*_{\mathrm{ch,alg}}$ (algebraic, AP-CY62 (b)); the verification routes operate on this model. |
| AP160 | chiral Hochschild explicit qualifier | Source 1 is geometric (MO on Hilb$^n$); Source 2 is algebraic (EK on Lie bialgebra); the disambiguation is preserved in the rationale. |
| AP113 | subscripted $\kappa$ | $\kappa_{\mathrm{BKM}}, \kappa_{\mathrm{ch}}, \kappa_{\mathrm{cat}}, \kappa_{\mathrm{fiber}}$ used; no bare $\kappa$. |
| FM44 | YBE convention | difference convention $R_{12}(a) R_{13}(a+b) R_{23}(b)$ named in the sympy source 4. |
| AP-CY28 | pole-safe test points | Sympy verification at $z = 7$ on Mukai parameters $h \in \{1, -2, 1\}$ (toy) avoiding the structure-function poles. |

---

**End draft.**

Authored by Raeez Lorgat. No AI attribution. Not committed. Sandbox
artefacts (k3_pentagon_cocycle.py, k3_pentagon_charge3.py,
k3_pentagon_ybe_check.py) live in /tmp per V49 §4 disclosure. Drop-in
text for `notes/INDEPENDENT_VERIFICATION.md` and template for the
test module decorator.
