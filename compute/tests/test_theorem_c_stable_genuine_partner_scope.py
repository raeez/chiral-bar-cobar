"""Structural guards for the stable genuine-partner form of Theorem C."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/theory/higher_genus_complementarity.tex"


def _source() -> str:
    return SOURCE.read_text()


def _environment(label: str, environment: str) -> str:
    source = _source()
    label_position = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{environment}}}", 0, label_position)
    end = source.index(rf"\end{{{environment}}}", label_position)
    return source[start:end]


def test_stable_base_convention_covers_zero_one_and_unpointed_higher_genus():
    convention = _environment("conv:theorem-c-stable-base", "convention")

    assert r"2g-2+n>0" in convention
    assert r"d_{g,n}:=3g-3+n" in convention
    assert r"3,&g=0" in convention
    assert r"1,&g=1" in convention
    assert r"0,&g\geq2" in convention
    assert r"\overline{\mathcal M}_g:=\overline{\mathcal M}_{g,n_g}" in convention


def test_genuine_partner_is_constructed_in_its_own_centre_complex():
    definition = _environment("def:complementarity-complexes", "definition")

    assert r"\mathbf C_{g,n}(\cA^!)" in definition
    assert r"\sigma_{\cA^!}j_Z=-j_Z\sigma_{\cA}" in definition
    assert r"j_Zp_{\cA}^{-}=p_{\cA^!}^{+}j_Z" in definition
    assert r"\chi^-_{\cA;g,n}" in definition
    assert r"\mathbf Q_{g,n}(\cA^!)" in definition
    assert r"\subset \mathbf C_{g,n}(\cA^!)" in definition


def test_main_theorem_consumes_stable_partner_data_and_dimension_shift():
    theorem = _environment("thm:quantum-complementarity-main", "theorem")

    assert r"Fix a stable pair \((g,n)\)" in theorem
    assert r"(\sigma_{\cA},\sigma_{\cA^!},j_Z,\chi^-_{\cA;g,n})" in theorem
    assert r"(\chi^-_{\cA;g,n})^{-1}\mathbf{Q}_{g,n}(\cA^!)" in theorem
    assert r"-d_{g,n}" in theorem
    assert "Type signature: Open quadrant" in theorem
    assert r"g\geq0" not in theorem
    assert r"3g{-}3" not in theorem
    assert r"Q_0(\cA^!)=0" not in theorem


def test_scalar_trace_uses_a_named_modular_realization_and_eigenclasses():
    trace = _environment("def:derived-centre-scalar-trace-kappa", "definition")
    conductor = _environment(
        "prop:scalar-conductor-c1-trace-shadow", "proposition"
    )

    assert r"\rho_{\cB;g,n}" in trace
    assert r"\vartheta_{\cB;g,n}^{(2)}" in trace
    assert r"H^2\!\left(\mathbf C_{g,n}(\cB)\right)" in trace
    assert "Theorem--D trace pair" in trace
    assert r"p_{\cA}^{+}\vartheta_{\cA;g,n}^{(2)" in conductor
    assert r"(\chi^-_{\cA;g,n})^{-1}" in conductor
    assert r"\operatorname{tr}^{-}_{\kappa,\cA;g,n}" in conductor
    assert r"p_{\cA}^{+}\theta_{\cA}^{(2)}" not in conductor


def test_public_complementarity_source_uses_computed_value_terminology():
    source = _source()
    assert "certificate" not in source.lower()
    assert r"K^\kappa_{\mathrm{cert}}" not in source
    assert r"K^\kappa_{\mathrm{computed}}" in source
