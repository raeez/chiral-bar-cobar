"""Guards for stable genuine-partner Theorem C consumers in the modular chapter."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"


def source() -> str:
    return SOURCE.read_text()


def environment(label: str, kind: str) -> str:
    text = source()
    label_at = text.index(rf"\label{{{label}}}")
    start = text.rindex(rf"\begin{{{kind}}}", 0, label_at)
    end = text.index(rf"\end{{{kind}}}", label_at)
    return text[start:end]


def test_stable_consumer_convention_and_legacy_symbol_elimination() -> None:
    text = source()
    convention = environment("conv:hgmk-theorem-c-stable-consumer", "convention")

    for required in (
        r"n_g:=",
        r"3,&g=0",
        r"1,&g=1",
        r"0,&g\geq2",
        r"d_{g,n_g}:=3g-3+n_g",
        r"\mathbf C_{g,n_g}(\cB)",
        r"\chi^-_{\cA;g,n_g}",
        r"\rho_{\cB;g,n_g}",
    ):
        assert required in convention

    for legacy in (
        r"Q_g",
        r"\mathbf{Q}_g",
        r"\mathbf Q_g",
        r"\mathbf C_g(\cA)",
        r"[-(3g{-}3)]",
        r"\cM_{1,0}",
        r"^{(1,0)}",
    ):
        assert legacy not in text


def test_one_channel_criteria_keep_the_partner_genuine_then_transport_it() -> None:
    verdier = environment("prop:one-channel-verdier-criterion", "proposition")
    ptvv = environment("prop:one-channel-ptvv-criterion", "proposition")
    chain = environment("prop:one-channel-chain-model-criterion", "proposition")

    for required in (
        r"L_g^!\subset Q_{g,n_g}(\cA^!)",
        r"\widetilde L_g^!:=(H^*\chi^-_{\cA;g,n_g})^{-1}L_g^!",
        r"E_g \;=\; L_g \oplus \widetilde L_g^!",
    ):
        assert required in verdier

    for required in (
        r"H_{\mathrm C_2}^{\mathrm{BV}}",
        r"C_{g,n_g}^\pm",
        r"\mathbf{L}_g^-",
        r"[-d_{g,n_g}]",
    ):
        assert required in ptvv

    for required in (
        r"\iota_g^{!,+}",
        r"\hookrightarrow \mathbf Q_{g,n_g}(\cA^!)",
        r"\widetilde\iota_g^-",
        r"(\chi^-_{\cA;g,n_g})^{-1}\circ\iota_g^{!,+}",
        r"[-d_{g,n_g}]",
    ):
        assert required in chain


def test_five_interface_theorem_uses_the_full_c_and_scalar_packages() -> None:
    theorem = environment("thm:five-from-theta", "theorem")

    for required in (
        r"\sigma_{\cA},\sigma_{\cA^!}",
        r"j_Z\colon\mathbf C_{g,n_g}(\cA)",
        r"\chi^-_{\cA;g,n_g}",
        r"(\chi^-_{\cA;g,n_g})^{-1}\mathbf Q_{g,n_g}(\cA^!)",
        r"-d_{g,n_g}",
        "ten-input C2 package",
        r"\rho_{\cB;g,n_g}",
        "trace--eigenclass compatibility",
        "Theorem~D",
    ):
        assert required in theorem

    assert "is the trace of the MC equation" not in theorem


def test_explicit_theta_separates_line_concentration_from_hodge_specialization() -> None:
    theorem = environment("thm:explicit-theta", "theorem")

    assert r"\Theta_{\cA}^{\min}" in theorem
    assert r"\eta\otimes\Gamma_{\cA}" in theorem
    assert r"\Gamma_{\cA}\in\Gmod" in theorem
    assert "tautological-line support and trace-isolation hypotheses" in theorem
    assert r"\Gamma_{\cA}=\kappa(\cA)\Lambda" in theorem
    assert r"H_D^K" in theorem
    assert r"H_D^{\mathrm{tr}}" in theorem


def test_mc2_partner_clause_uses_represented_centres_before_scalar_trace() -> None:
    text = source()
    theorem = environment("thm:mc2-conditional-completion", "theorem")
    completion = environment("thm:mc2-full-resolution", "theorem")
    label_at = text.index(r"\label{thm:mc2-conditional-completion}")
    proof_start = text.index(r"\begin{proof}", label_at)
    proof_end = text.index(r"\end{proof}", proof_start)
    proof = text[proof_start:proof_end]

    for required in (
        r"\label{mc2-hyp:partner}",
        r"(\sigma_{\cA},\sigma_{\cA^!},j_Z,",
        r"\chi^-_{\cA;g,n_g}",
        "bar--centre comparison",
        r"Q_{g,n_g}(\cA^!)",
        "ten-input C2 package",
    ):
        assert required in theorem

    assert r"\rho_{\cB;g,n_g}" in proof
    assert "trace--eigenclass compatibility" in proof
    assert "all four hypotheses" in completion
    assert r"Hypothesis~\textup{\ref{mc2-hyp:partner}}" in completion


def test_cross_polarized_graph_sum_has_a_typed_cross_pairing() -> None:
    hamiltonian = environment("def:modular-bar-hamiltonian", "definition")
    carrier = environment(
        "def:ambient-modular-complementarity-algebra", "definition"
    )
    principle = environment("prop:chriss-ginzburg-structure", "proposition")

    for required in (
        r"\beta_{\cA}^{+-}\colon",
        r"V_{\cA}\otimes V_{\cA^!}",
        r"(\beta_{\cA}^{+-})^\sharp",
        r"P_{\cA}^{+-}:=(\beta_{\cA}^{+-})^{-1}",
        r"\beta_{\cA}^{++}=\beta_{\cA}^{--}=0",
    ):
        assert required in hamiltonian

    assert r"P_{\cA}^{+-}" in carrier
    assert "same-side edges" in carrier
    assert r"\ClaimStatusConditional" in principle
    assert "C0/C1" in principle
    assert r"H_D" in principle
    assert r"H_H" in principle


def test_square_zero_and_pbw_chains_stop_at_their_intrinsic_outputs() -> None:
    text = source()
    bipartite = environment("rem:mc2-bipartite", "remark")
    pbw_scope = environment("rem:pbw-propagation-scope", "remark")
    functor = environment("thm:universal-modular-deformation", "theorem")

    assert r"V_{\cA}\otimes V_{\cA^!}\to" in bipartite
    assert "\to" not in bipartite
    for required in (
        "bar-intrinsic shadow obstruction tower",
        "inversion package",
        "C0/C1a",
        "C1b",
        "C2",
        r"H_D",
        r"H_H(\cA;S)",
    ):
        assert required in pbw_scope

    assert "bar/MC construction and its shadow projections are natural" in functor
    assert "named package" in functor
    for inflated in (
        "The five main theorems follow from genus-$0$ Koszulity",
        "gives the five main theorems at all genera",
        "The five theorems and all shadow invariants are natural",
        "The five main theorems and the genus expansion descend",
    ):
        assert inflated not in text


def test_global_ledger_keeps_five_reconstruction_packages_independent() -> None:
    text = source()
    start = text.index("The theorem ledger separates")
    end = text.index("% THE MODULAR BAR-HAMILTONIAN", start)
    ledger = text[start:end]

    for required in (
        "Theorem~A --- conditional",
        r"H_{\mathrm{fact}}\cup H_{\mathrm{conv}}",
        r"H_{\mathrm{VD}}",
        "Theorem~B --- conditional",
        r"H_{\mathrm{CL}}",
        "Theorem~C --- conditional",
        r"\mathbf Q_{g,n_g}(\cA^!)",
        r"(\chi^-_{\cA;g,n_g})^{-1}",
        "C1b",
        "C2",
        "Theorem~D --- conditional",
        r"H_D^1",
        r"\overline{\cM}_{1,1}",
        r"\delta F_g^{\mathrm{cross}}",
        "Theorem~H --- conditional",
        r"H_H(\cA;S)",
    ):
        assert required in ledger

    assert "shifted-symplectic pairing from Verdier duality" not in ledger
    assert "aspects of a single object" not in ledger


def test_scalar_outputs_remain_typed_projections_of_the_mc_tower() -> None:
    shadow = environment("def:shadow-postnikov-tower", "definition")
    tower = environment("constr:tower-template", "construction")
    polyakov = environment("prop:polyakov-degree-two-projection", "proposition")
    interpretation = environment("rem:theta-interpretation", "remark")

    assert r"\pi_2^{\mathrm{sc}}(\Theta_{\cA})=\kappa(\cA)" in shadow
    assert r"\Theta_{\cA}^{\leq 2} = \kappa(\cA)" not in shadow
    assert r"\pi_2^{\mathrm{sc}}(\Theta_{\cA})=\kappa(\cA)" in tower
    assert "scalar projection of the truncation" in tower
    assert r"\pi_{2,g}^{\mathrm{sc}}(\Theta_\cA)=\kappa\Lambda_g" in polyakov
    assert "represented uniform-weight scalar lane" in polyakov
    for required in (
        r"\pi_{2,\mathrm{Hdg}}^{\mathrm{sc}}",
        r"\rho_{\cB;g,n_g}",
        "trace--eigenclass compatibility",
        "normalized Theorem~D trace",
    ):
        assert required in interpretation
    assert r"\Theta_{\cA}+\Theta_{\cA^!}" not in interpretation


def test_explicit_theta_splits_general_line_from_km_bracket_package() -> None:
    theorem = environment("thm:explicit-theta", "theorem")

    for required in (
        "minimal cyclic",
        "one-channel degree-two package",
        "KM minimal-bracket package",
        "The one-channel support and one-dimensionality give",
        "For an affine",
        r"H^*(\Defcyc(\cA),l_1)",
        r"l_3^{\mathrm{tr}}=\phi",
        "Minimal-line MC equation",
        "full deformation",
        "Pointed genus-$1$ trace",
        r"H_D^1",
        r"\operatorname{tr}_{1,1}[\theta_{1,1}]",
        r"\overline{\mathcal{M}}_{1,1}",
        "KM higher-genus representative",
    ):
        assert required in theorem

    assert theorem.index("For an affine") < theorem.index(
        r"H^*(\Defcyc(\cA),l_1)"
    )
    assert r"\lambda_1\in H^2(\overline{\mathcal M}_{1,1})" in theorem
    assert "lies on\n $\\overline{\\mathcal M}_g$ for~$g\\geq2$" in theorem


def test_required_type_signatures_and_envelope_scope_are_guarded() -> None:
    five = environment("thm:five-from-theta", "theorem")
    explicit = environment("thm:explicit-theta", "theorem")
    mc2 = environment("thm:mc2-conditional-completion", "theorem")
    completion = environment("thm:mc2-full-resolution", "theorem")
    principle = environment("prop:chriss-ginzburg-structure", "proposition")
    carrier = environment(
        "def:ambient-modular-complementarity-algebra", "definition"
    )
    envelope = environment("thm:envelope-koszul", "theorem")

    for block in (five, explicit, mc2, completion, principle, carrier, envelope):
        assert "Type signature:" in block
        assert "Open quadrant" in block

    assert r"\ClaimStatusDefinitional" in carrier
    for required in (
        "EK1",
        "EK2",
        "EK3",
        "genus-$0$ envelope",
        "gives MK3",
        "inversion package",
        "C0/C1a",
        r"H_D",
        r"H_H(\cA;S)",
    ):
        assert required in envelope
    assert "gives the five main theorems" not in envelope


def test_pointed_genus_one_claims_name_the_stable_base_and_trace_package() -> None:
    text = source()
    blocks = (
        environment("cor:conditional-allgenera-km", "corollary"),
        environment("cor:conditional-allgenera-virasoro", "corollary"),
        environment("rem:mc2-2-resolution", "remark"),
        environment("thm:mc2-conditional-completion", "theorem"),
        environment("thm:mc2-full-resolution", "theorem"),
        environment("thm:perturbative-exactness", "theorem"),
    )

    for block in blocks:
        assert r"H_D^1" in block
        assert "1,1" in block

    for stale in (
        "scalar trace is unconditional at genus~$1$",
        "scalar-trace input is unconditional only at genus~$1$",
        "Resolved at genus~$1$ universally",
        "proved only at genus~$1$",
        "genus-$1$ comparison is the universal part",
        "proved unconditionally at genus~$1$",
    ):
        assert stale not in text
