"""Structural and executable guards for lattice Hochschild charge data."""

import cmath
from pathlib import Path

import pytest

from compute.lib.lattice_hochschild_charge_engine import (
    charges_in_window,
    conformal_energy,
    filtration_reindexing,
    gamma_shift_set,
    reversed_order_ratio,
    translate_charge,
    translation_table,
    validate_even_gram,
)


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "chapters/examples/lattice_foundations.tex"


def _compact() -> str:
    return "".join(SOURCE.read_text().split())


def test_lattice_cochains_decompose_by_charge_shift_at_finite_weight():
    text = _compact()
    start = text.index(r"\begin{proposition}[Chargedecomposition")
    end = text.index(r"\end{proposition}", start)
    block = text[start:end]
    for token in (
        r"\ClaimStatusProvedHere",
        "positive-definiteevenintegrallattice",
        "projectingeveryinputandtheoutput",
        r"\Gamma_{n,N}",
        r"(1\leqi\leqn)",
        r"C^n_{\mathrm{ch}}(\Vlat_\Lambda,\Vlat_\Lambda)^{[\gamma]}_{\leqN}",
        r"\alpha_1+\cdots+\alpha_n+\gamma",
        "derivedinverselimit",
        "conformal-weight-completedproduct",
    ):
        assert token in block
    assert r"(\gamma,\gamma)/2\leqN" not in block


def test_group_cohomology_requires_the_named_chain_comparison():
    text = _compact()
    for token in (
        r"H_{\Lambda}^{\mathrm{HH}}",
        r"\Lambda$-modulestructure~$\rho",
        r"\Xi_\Lambda\colon",
        r"\widehatC^\bullet_{\mathrm{ch}}(\Vlat_\Lambda,\Vlat_\Lambda)^{[0]}",
        r"\widehatC^\bullet(\Lambda;\cH_\rho)",
        r"R\!\varprojlim_NC^\bullet(\Lambda;(\cH_\rho)_{\leqN})",
        "Mittag--Lefflerquasi-isomorphism",
        r"\widehatH^n(\Lambda;\cH_\rho)",
        r"\ClaimStatusConditional",
    ):
        assert token in text


def test_unimodularity_and_internal_charge_define_independent_gradings():
    text = _compact()
    start = text.index(r"\begin{remark}[Unimodularityandcharge]")
    end = text.index(r"\end{remark}", start)
    block = text[start:end]
    assert r"D(\Lambda)=\Lambda^*/\Lambda" in block
    assert r"\bigoplus_{\alpha\in\Lambda}\cHe^\alpha" in block
    assert "defineindependentgradings" in block


def test_a1_conclusion_is_scoped_to_the_comparison_package():
    text = _compact()
    start = text.index(r"\begin{example}[\texorpdfstring{$A_1$}{A1}charge-zero")
    end = text.index(r"\end{example}", start)
    block = text[start:end]
    assert r"H_{A_1}^{\mathrm{HH}}" in block
    assert "finiteoscillatorwindow" in block
    assert "Mittag--Lefflerclause" in block
    assert "fullchiralcohomologyadditionallycarries" in block


def test_e1_lattice_complex_uses_charge_shift_and_finite_windows():
    text = _compact()
    start = text.index(r"\begin{proposition}[$\Eone$latticecharge-shiftcomplex;")
    end = text.index(r"\end{proposition}", start)
    block = text[start:end]
    for token in (
        r"\ClaimStatusProvedHere",
        "positive-definiteevenlattice",
        r"\bigoplus_{\gamma\in\Gamma_{n,M}}",
        r"CC^n_{\Eone,\mathrm{ch}}(V_\Lambda^{N,q})^{[\gamma]}_{\leqM}",
        "derivedinverselimit",
        "oscillatorrestriction",
        r"\operatorname{res}_{\cH}\colon",
        r"CC^\bullet_{\Eone,\mathrm{ch}}(\cH,\cH)",
        "completedaveragingquasi-isomorphism",
    ):
        assert token in block
    assert "oscillatorsubcomplex" not in block
    assert r"H_{\mathrm{per}}" not in block


def test_e1_collision_coefficient_and_braiding_ratio_are_separated():
    text = _compact()
    start = text.index(r"\begin{proposition}[$\Eone$latticecharge-shiftcomplex;")
    end = text.index(r"\end{proposition}", start)
    block = text[start:end]
    assert r"\varepsilon_{N,q}(\alpha_i,\alpha_j)" in block
    assert (
        r"\frac{\varepsilon_{N,q}(\alpha_i,\alpha_j)}"
        r"{\varepsilon_{N,q}(\alpha_j,\alpha_i)}"
    ) in block


def test_e1_periodicity_carries_its_filtration_reindexing():
    text = _compact()
    start = text.index(r"\begin{definition}[Latticecharge-periodicitydatum;")
    end = text.index(r"\end{definition}", start)
    block = text[start:end]
    for token in (
        r"For$\beta\in\Lambda$",
        "familyofcontinuouschainisomorphisms",
        r"T_{N\beta,\gamma}\colon",
        r"T_{N\beta}:=(T_{N\beta,\gamma})_{\gamma\in\Lambda}",
        r"\Delta_{N\beta}(\lambda)",
        r"N(\lambda,\beta)+\frac{N^2(\beta,\beta)}2",
        "completedtransitionmaps",
    ):
        assert token in block

    cor_start = text.index(
        r"\begin{corollary}[PeriodictransportoflatticeHochschildcohomology;"
    )
    cor_end = text.index(r"\end{corollary}", cor_start)
    corollary = text[cor_start:cor_end]
    assert r"\ClaimStatusConditional" in corollary
    assert r"H^\bullet(T_{N\beta,\gamma})\colon" in corollary
    assert "charge-dependentreindexing" in corollary


def test_reduction_mod_n_uses_a_compatible_periodicity_family():
    text = _compact()
    start = text.index(r"\begin{remark}[Charge-shiftcomputation]")
    end = text.index(r"\end{remark}", start)
    block = text[start:end]
    assert "compatiblefamilyofperiodicitydata" in block
    assert r"\Lambda/N\Lambda" in block
    assert r"\Delta_{N\beta}" in block


A1_GRAM = ((2,),)
A2_GRAM = ((2, -1), (-1, 2))


def test_a1_finite_window_computes_degree_dependent_gamma_sets():
    gram = validate_even_gram(A1_GRAM)
    assert charges_in_window(gram, 1) == ((-1,), (0,), (1,))
    assert gamma_shift_set(gram, 1, 1) == tuple((value,) for value in range(-2, 3))
    assert gamma_shift_set(gram, 2, 1) == tuple((value,) for value in range(-3, 4))


def test_a1_charge_reversal_exhibits_the_false_uniform_energy_bound():
    gram = validate_even_gram(A1_GRAM)
    source = (1,)
    target = (-1,)
    shift = (target[0] - source[0],)
    assert conformal_energy(gram, source) == 1
    assert conformal_energy(gram, target) == 1
    assert conformal_energy(gram, shift) == 4
    assert shift in gamma_shift_set(gram, 1, 1)


def test_a2_window_is_the_zero_charge_together_with_six_roots():
    gram = validate_even_gram(A2_GRAM)
    charges = set(charges_in_window(gram, 1))
    assert charges == {
        (0, 0),
        (1, 0),
        (0, 1),
        (1, 1),
        (-1, 0),
        (0, -1),
        (-1, -1),
    }


def test_period_translation_changes_charge_and_filtration_by_exact_formula():
    gram = validate_even_gram(A2_GRAM)
    charge = (1, 0)
    beta = (0, 1)
    period = 3
    translated = translate_charge(charge, period, beta)
    shift = filtration_reindexing(gram, charge, period, beta)
    assert translated == (1, 3)
    assert shift == 6
    assert conformal_energy(gram, translated) - conformal_energy(gram, charge) == shift


def test_translation_table_realizes_an_invertible_charge_state_transition():
    gram = validate_even_gram(A2_GRAM)
    charges = charges_in_window(gram, 1)
    table = translation_table(gram, charges, 4, (1, -1))
    assert len(table) == len(charges)
    assert len({target for target, _ in table.values()}) == len(charges)
    for source, (target, shift) in table.items():
        assert translate_charge(target, -4, (1, -1)) == source
        assert conformal_energy(gram, target) - conformal_energy(gram, source) == shift


def test_collision_coefficient_and_reversed_order_ratio_are_distinct_data():
    period = 5
    zeta = cmath.exp(2j * cmath.pi / period)
    epsilon_ab = zeta
    epsilon_ba = -(zeta ** -1)
    ratio = reversed_order_ratio(epsilon_ab, epsilon_ba)
    assert abs(epsilon_ab - zeta) < 1e-12
    assert abs(ratio - (-(zeta ** 2))) < 1e-12
    assert abs(ratio - epsilon_ab) > 1e-6


@pytest.mark.parametrize(
    "gram",
    (
        ((1,),),
        ((2, 1), (0, 2)),
        ((2, 4), (4, 2)),
    ),
)
def test_lattice_window_rejects_odd_asymmetric_and_indefinite_gram_data(gram):
    with pytest.raises(ValueError):
        validate_even_gram(gram)
