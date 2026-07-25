"""Source-level guards for derived centres and Theorem C surfaces."""

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
THQG_OPEN_CLOSED_TEX = (
    REPO_ROOT / "chapters/connections/thqg_open_closed_realization.tex"
)
EN_KOSZUL_DUALITY_TEX = REPO_ROOT / "chapters/theory/en_koszul_duality.tex"
THREE_HOCHSCHILD_TEX = (
    REPO_ROOT / "chapters/theory/three_hochschild_unification_platonic.tex"
)
HIGHER_GENUS_COMPLEMENTARITY_TEX = (
    REPO_ROOT / "chapters/theory/higher_genus_complementarity.tex"
)
CHIRAL_HOCHSCHILD_KOSZUL_TEX = (
    REPO_ROOT / "chapters/theory/chiral_hochschild_koszul.tex"
)


def _source(path: Path) -> str:
    return path.read_text()


def _block(source: str, label: str, env: str) -> str:
    label_pos = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{env}}}", 0, label_pos)
    end = source.index(rf"\end{{{env}}}", start)
    return " ".join(source[start:end].split())


def test_chiral_derived_centre_oca_and_swiss_cheese_output_are_typed():
    """The closed colour is the cochain centre; OCA is extra data."""
    source = _source(THQG_OPEN_CLOSED_TEX)

    centre = _block(source, "def:thqg-chiral-derived-center", "definition")
    genus = _block(source, "def:genus-g-derived-center", "definition")
    oca = _block(source, "def:thqg-oca-datum", "definition")
    swiss = _block(source, "thm:thqg-swiss-cheese", "theorem")
    comparison = _block(
        source, "prop:thqg-universal-action-not-reconstruction", "proposition"
    )

    for required in (
        r"\ClaimStatusDefinitional",
        r"R\!\operatorname{Hom}^{\mathrm{act}}_{\mathsf{Fact}_{\cA-\cA}}",
        r"\mathcal{C}^{\bullet}_{\mathrm{ch}}(\cA,\cA)",
            "brace dg algebra",
            "Deligne--Tamarkin rectification",
            "OCA datum",
            r"H_H(\cA;S)",
            "Critical, minimal/admissible, and $E_1$-chiral families carry their own support data",
    ):
        assert required in centre

    for required in (
        r"\ClaimStatusDefinitional",
        r"\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)^{(g)}",
        r"\Dg{g} \;=\; \dfib + \nabla^{\mathrm{GM}}",
        r"\Dg{g}^{\,2} = 0",
        r"\mathcal{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)^{(0)}",
    ):
        assert required in genus

    for required in (
        r"\ClaimStatusDefinitional",
        r"\beta_T",
        r"\mathbf{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA)",
        r"\mathsf{SC}^{\mathrm{ch,top}}",
        "identification datum",
        "only when",
        "quasi-isomorphism",
        r"\bar B(\cA)",
        "neither",
        "physical bulk factorisation algebra",
    ):
        assert required in oca

    for required in (
        r"\ClaimStatusProvedHere",
        r"\mathcal{U}(\cA)",
        r"\mathsf{SC}^{\mathrm{ch,top}}",
        "typed pair",
        r"(\mathbf{Z}^{\mathrm{der}}_{\mathrm{ch}}(\cA),\,\cA)",
        "The bar coalgebra",
        "is not itself",
        "not a physical bulk without the OCA datum",
    ):
        assert required in swiss

    for required in (
        r"\ClaimStatusProvedHere",
        "A comparison between the physical bulk and the cochain derived center",
        "OCA datum",
        "quasi-isomorphism condition",
        "extra hypothesis",
    ):
        assert required in comparison


def test_bar_is_e1_engine_not_swiss_cheese_output():
    """The ordered bar computes/resolves the centre but is not SC."""
    source = _source(EN_KOSZUL_DUALITY_TEX)

    principle = _block(source, "princ:sc-two-incarnations", "principle")
    theorem = _block(source, "thm:bar-e1-coalgebra", "theorem")

    for required in (
        r"\barB^{\mathrm{ord}}(\cA)",
        r"\Eone",
        "does \\emph{not} carry",
        r"\mathsf{SC}^{\mathrm{ch,top}}",
        "operation-space witness",
        "not a chain-level",
        "computed \\emph{using} the bar complex as a resolution",
        "derived center is the cochain-level local closed-sector slot",
    ):
        assert required in principle

    for required in (
        r"\ClaimStatusProvedHere",
        r"\barB^{\mathrm{ord}}(\cA)",
        "single-colored",
        r"\Eone",
        "does not carry",
        r"\mathsf{SC}^{\mathrm{ch,top}}",
        "computed using",
        "as a resolution",
        "$2^n$-term coshuffle",
    ):
        assert required in theorem


def test_presentation_indexed_centres_and_drinfeld_firewall_are_pinned():
    """The five centre presentations are not identified by notation."""
    source = _source(THREE_HOCHSCHILD_TEX)

    bulk = _block(
        source, "rem:derived-centre-not-physical-bulk-without-comparison", "remark"
    )
    centres = _block(source, "def:presentation-indexed-derived-centres", "definition")
    comparison = _block(source, "constr:presentation-centre-comparison-maps", "construction")

    for required in (
        r"Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)",
        r"\mathrm{OC}_{\cA}",
        "physical bulk object is not identified",
        "only after a named open/closed comparison quasi-isomorphism",
        "Without",
        "only the cochain-level derived centre is in scope",
    ):
        assert required in bulk

    for required in (
        r"\ClaimStatusDefinitional",
        "presentation-indexed",
        r"Z^{\mathrm{der}}_{\mathrm{ch}}(\cA)",
        r"Z^{\mathrm{der}}_{\Eone\text{-}\mathrm{ch}}",
        r"Z^{\mathrm{der}}_{\Einf\text{-}\mathrm{ch}}",
        r"Z^{\mathrm{der}}_{\mathrm{mode}}",
        r"Z^{\mathrm{der}}_{\mathrm{cat}}",
        r"\mathfrak Z_{\mathrm{Dr}}(\mathcal C)",
        "not a chiral derived-centre complex",
        "These five objects are not identified by notation",
    ):
        assert required in centres

    for required in (
        "H1",
        "H2",
        "H3",
        "H4",
        "Each map is a quasi-isomorphism only on its named generic comparison surface",
        "do not coincide by default",
        "not itself an equality of presentation-indexed centres",
    ):
        assert required in comparison


def test_theorem_c_c0_c1_c2_surfaces_are_separated():
    """C0/C1/C2 are distinct; scalar K^kappa is only a trace shadow."""
    source = _source(HIGHER_GENUS_COMPLEMENTARITY_TEX)

    trace = _block(source, "def:derived-centre-scalar-trace-kappa", "definition")
    conductor = _block(source, "prop:scalar-conductor-c1-trace-shadow", "proposition")
    complexes = _block(source, "def:complementarity-complexes", "definition")
    theorem_c = _block(source, "thm:quantum-complementarity-main", "theorem")
    c2 = _block(source, "thm:shifted-symplectic-complementarity", "theorem")

    for required in (
        r"\ClaimStatusDefinitional",
        r"\rho_{\cB;g,n}",
        r"H^2\!\left(Z^{\mathrm{der}}_{\mathrm{ch}}(\cB)\right)_{\mathrm{diag}}",
        r"\operatorname{tr}_{\kappa,\cB;g,n}",
        r"\vartheta_{\cB;g,n}^{(2)}",
        "Theorem--D trace pair",
        "open/closed comparison, centre reconstruction",
        "shifted-symplectic BV/QME structure",
    ):
        assert required in trace

    for required in (
        r"\ClaimStatusConditional",
        "C1",
        "Theorem~D",
        r"\chi^-_{\cA;g,n}",
        "trace--eigenclass compatibility",
        r"K^\kappa(\cA)",
        r"\kappa(\cA)+\kappa(\cA^!)",
        "one-dimensional trace shadow",
        "source objects",
    ):
        assert required in conductor

    for required in (
        r"\ClaimStatusDefinitional",
        r"\mathbf C_{g,n}(\cA)",
        r"\mathbf Q_{g,n}(\cA^!)",
        r"j_Z",
        r"\sigma_{\cA^!}j_Z=-j_Z\sigma_{\cA}",
        r"\chi^-_{\cA;g,n}",
        "strict-flat centre complexes",
        "cochain involutions",
        "genuine-partner comparison datum",
        "scalar traces give the conductor shadow",
    ):
        assert required in complexes

    for required in (
        r"\ClaimStatusConditional",
        r"\mathrm{C}_{1a}",
        r"\mathrm{C}_{1b}",
        "H-level",
        "S-level",
        r"\mathbf{C}_{g,n}(\cA) \;\simeq\;",
        r"\chi^-_{\cA;g,n}",
        r"Q_{g,n}(\cA^!)",
        r"-d_{g,n}",
        "represented Koszul-pair data",
        "perfectness",
        "non-degenerate cochain-level pairing",
    ):
        assert required in theorem_c

    for required in (
        r"\ClaimStatusConditional",
        r"\mathrm{C}_2",
        "conditional BV package",
        "cyclic nondegeneracy input",
        "degree~$+1$",
        "$(-1)$-shifted Poisson",
        "$(-1)$-shifted symplectic",
        "Lagrangian subspaces",
    ):
        assert required in c2


def test_ambient_formal_moduli_and_example_computations_are_scoped():
    """Derived intersections and family computations are conditional checks."""
    complementarity = _source(HIGHER_GENUS_COMPLEMENTARITY_TEX)
    hochschild = _source(CHIRAL_HOCHSCHILD_KOSZUL_TEX)

    datum = _block(
        complementarity, "def:ambient-complementarity-tangent-complex", "definition"
    )
    moduli = _block(complementarity, "def:complementarity-formal-moduli", "definition")
    fmp = _block(complementarity, "thm:ambient-complementarity-fmp", "theorem")
    examples = _block(
        hochschild, "rem:standard-family-theorem-h-computation-surfaces", "remark"
    )

    for required in (
        r"\ClaimStatusDefinitional",
        r"T_{\mathrm{comp}}(\cA)",
        r"\operatorname{fib}",
        r"\nabla_{\cA} - \nabla_{\cA^!}",
        "linearized Maurer--Cartan equation",
    ):
        assert required in datum

    for required in (
        r"\ClaimStatusDefinitional",
        r"\mathcal M_{\cA}",
        r"\mathcal M_{\cA^!}",
        r"\mathcal M_{\mathrm{comp}}(\cA)",
        r"K^{\mathrm{comp}}_{\tau}(\cA,\cA^!)",
        "missing converse datum",
        "Acyclicity",
        "transversality",
        "the converse requires",
    ):
        assert required in moduli

    for required in (
        r"\ClaimStatusConditional",
        "perfectness",
        "nondegeneracy",
        "closed invariant non-degenerate pairing of degree~$-1$",
        "one-sided deformation problems define Lagrangian maps",
        "linear shadow",
    ):
        assert required in fmp

    for required in (
        "proven bounded vertex-cohomology calculations",
        "rank-one even superboson",
        "Virasoro algebra",
        r"\cite[Conjecture~7.5]{BDSK21}",
        "bounded-to-chart quasi-isomorphism",
        r"\mathcal W",
        "admissible quotients",
        "logarithmic triplet algebras",
        r"K_{\cA,S}",
    ):
        assert required in examples
