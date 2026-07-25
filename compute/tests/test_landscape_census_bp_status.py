r"""Semantic guards for the Bershadsky--Polyakov census lane."""

from pathlib import Path
import re


CENSUS = Path("chapters/examples/landscape_census.tex")
SOURCE = CENSUS.read_text()


def _between(start: str, end: str) -> str:
    """Return the unique source interval delimited by ``start`` and ``end``."""

    start_index = SOURCE.index(start)
    end_index = SOURCE.index(end, start_index)
    return SOURCE[start_index:end_index]


MASTER_TABLE = _between(
    r"\label{tab:master-invariants}",
    r"\begin{remark}[Bershadsky--Polyakov conformal-vector conventions]",
)
BP_CONVENTION = _between(
    r"\label{rem:bp-census-convention-separation}",
    r"\noindent The Schellekens",
)
WITNESS_THEOREM = _between(
    r"\label{thm:census-witness-complementarity}",
    r"\begin{proposition}[Archetype-by-archetype",
)
ARCHETYPE_BRIDGE = _between(
    r"\label{prop:archetype-complementarity-bridge}",
    r"\begin{proposition}[Mukai lattice arithmetic",
)
B_FAMILY_PROPOSITION = _between(
    r"\label{prop:G-B-heisenberg-rho-bifurcation}",
    r"\begin{remark}[Three-path computation of the archetype table]",
)
SELF_DUAL_LOCUS = _between(
    r"\label{thm:census-self-dual-locus}",
    r"\begin{remark}[Three-path computation of",
)
SELF_DUAL_VERIFICATION = _between(
    r"\label{rem:self-dual-locus-verification}",
    r"\begin{remark}[Koszul conductor for",
)
K3_BKM_SYNTHESIS = _between(
    r"\label{rem:landscape-1}",
    r"\begin{remark}[Scalar typing of rows adjacent to K3$\times$E]",
)
BRUINIER_SCOPE = _between(
    r"\label{prop:canonical-bruinier-heegner-chern}",
    r"\begin{proposition}[Half K3 Jacobi coefficients",
)


def test_master_table_separates_exact_central_and_open_modular_data():
    assert r"-\dfrac{(2k{+}3)(3k{+}1)}{k{+}3}" in MASTER_TABLE
    assert "& $50$" in MASTER_TABLE
    assert "open: direct genus-$1$ curvature" in MASTER_TABLE
    assert (
        "PH$^{\\mathrm{BP},c}$/OP$^{\\mathrm{BP},g=1}$/"
        "CD$^{\\mathrm{BP,DS}}$"
    ) in MASTER_TABLE
    assert "ordinary bosonic vertex algebra with even strong" in MASTER_TABLE
    assert "1+\\frac23+\\frac23+\\frac12=\\frac{17}{6}" in MASTER_TABLE
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in MASTER_TABLE
    assert "open-genus-one-computation" in MASTER_TABLE


def test_convention_record_preserves_both_exact_central_conductors():
    assert r"K^c_{\mathrm{BP}}=50" in BP_CONVENTION
    assert r"c_{\mathrm{BP}}^{\mathrm{shift}}(-k-6)=196" in BP_CONVENTION
    assert "$G^+$ and $G^-$ are even" in BP_CONVENTION
    assert "diagnostic is $17/6$" in BP_CONVENTION
    assert r"\kappa_{\mathrm{BP}}=c_{\mathrm{BP}}/6" in BP_CONVENTION
    assert r"\varrho_{\mathrm{BP}}=1/6" in BP_CONVENTION
    assert r"K^\kappa_{\mathrm{BP}}=25/3" in BP_CONVENTION
    assert "former proposal" in BP_CONVENTION
    assert r"\ClaimStatusConjectured" in BP_CONVENTION
    assert "open-genus-one-computation" in BP_CONVENTION
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in BP_CONVENTION


def test_former_bp_value_stays_outside_certified_scalar_range():
    assert r"\{0,\,13\}" in SOURCE
    assert r"\{0,\,13,\,250/3\}" in SOURCE
    assert r"\{0,\,8,\,13,\,250/3\}" in SOURCE
    assert r"\{0,\,13,\,250/3,\,25/3\}" not in SOURCE
    assert r"\{0,\,8,\,13,\,250/3,\,25/3\}" not in SOURCE

    former_occurrences = list(re.finditer(r"(?<![\d-])25/3(?!\d)", SOURCE))
    assert len(former_occurrences) == 3
    for occurrence in former_occurrences:
        context = SOURCE[
            max(0, occurrence.start() - 420) : occurrence.end() + 420
        ]
        assert "former" in context
        assert r"\ClaimStatusConjectured" in context


def test_witness_theorem_keeps_bp_genus_one_invariant_open():
    assert r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50" in WITNESS_THEOREM
    assert r"K^\kappa_{\mathrm{BP}}(k)" in WITNESS_THEOREM
    assert r"\ClaimStatusOpen" in WITNESS_THEOREM
    assert "direct genus-$1$" in WITNESS_THEOREM
    assert "reciprocal-weight diagnostic is therefore $17/6$" in WITNESS_THEOREM
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in WITNESS_THEOREM
    assert r"K^\kappa_{\mathrm{BP}}=25/3" not in WITNESS_THEOREM


def test_archetype_bridge_has_a_symbolic_bp_row():
    assert (
        r"$\mathsf{M}$-ext & $\mathrm{BP}_k$ (minimal) "
        "& open & $50$ & open & open"
    ) in ARCHETYPE_BRIDGE
    assert r"\{0,8,13,250/3\}" in ARCHETYPE_BRIDGE
    assert r"\{0,13\}" in ARCHETYPE_BRIDGE
    assert "four unconditional pairs" in ARCHETYPE_BRIDGE
    assert (
        r"H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}"
        in ARCHETYPE_BRIDGE
    )
    assert "The seventh, BP, row" in ARCHETYPE_BRIDGE
    assert r"(1/6,50)" not in ARCHETYPE_BRIDGE


def test_bp_self_dual_record_uses_the_central_midpoint_only():
    assert r"\kappa^*(\mathrm{BP})$ has status \ClaimStatusOpen" in SELF_DUAL_LOCUS
    assert r"c^{\mathrm{mid}}_{\mathrm{BP}}=50/2=25" in SELF_DUAL_LOCUS
    assert r"k=-3\pm2i" in SELF_DUAL_LOCUS
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in SELF_DUAL_LOCUS
    assert "BP conductor is~$50$, with midpoint~$25$" in SELF_DUAL_VERIFICATION
    assert "shifted BP scalar convention and its conductor~$196$" in SELF_DUAL_VERIFICATION
    assert "modular midpoint is open" in SELF_DUAL_VERIFICATION


def test_b_family_separates_mukai_arithmetic_from_chiral_candidate():
    assert r"U^4\oplus E_8(-1)^2" in B_FAMILY_PROPOSITION
    assert r"\operatorname{sig}\widetilde H(K3,\mathbb Z)=(4,20)" in B_FAMILY_PROPOSITION
    assert r"2c_+(\Lambda_{\mathrm{Muk}})=8" in B_FAMILY_PROPOSITION
    assert r"\ClaimStatusProvedHere" in B_FAMILY_PROPOSITION
    assert r"\ClaimStatusConjectured" in B_FAMILY_PROPOSITION
    for hypothesis in ("chart", "KD", "scalar", "mod", "quantum"):
        assert f"H_{{\\mathrm{{{hypothesis}}}}}" in B_FAMILY_PROPOSITION
    assert r"\left(\frac16,48,8,4\right)" in B_FAMILY_PROPOSITION


def test_b_family_source_audit_removes_the_former_three_faces_argument():
    assert r"\cite[Lemma~5.1]{Bruinier2002}" in BRUINIER_SCOPE
    assert r"N'=\operatorname{lcm}(N,8)" in BRUINIER_SCOPE
    assert "chosen admissible" in BRUINIER_SCOPE
    assert r"\ClaimStatusConjectured" in BRUINIER_SCOPE
    assert r"(H_{\mathrm{mod}},H_{\mathrm{quantum}})\subset H_{\mathsf B}" in BRUINIER_SCOPE
    assert r"\Z/8" not in BRUINIER_SCOPE
    assert "torsion generator" not in BRUINIER_SCOPE
    assert "order-$8$ monodromy" not in SOURCE
    assert "Beilinson--Drinfeld Koszul-conductor identity on indefinite lattices" not in SOURCE
    assert "Mukai--Bruinier--Borcherds" not in SOURCE


def test_k3_synthesis_types_eight_as_a_conditional_chiral_value():
    assert r"2c_+(\widetilde H(K3,\mathbb Z))=8" in K3_BKM_SYNTHESIS
    assert r"K^{\kappa_{\mathrm{ch}}}_{\mathsf B}=8" in K3_BKM_SYNTHESIS
    assert r"\ClaimStatusConjectured" in K3_BKM_SYNTHESIS
    assert r"H_{\mathsf B}" in K3_BKM_SYNTHESIS
