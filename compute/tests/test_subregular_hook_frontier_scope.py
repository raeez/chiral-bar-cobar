r"""Semantic guards for the subregular/hook frontier chapter."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = (
    ROOT / "chapters" / "connections" / "subregular_hook_frontier.tex"
).read_text(encoding="utf-8")


def _between(start: str, end: str) -> str:
    start_index = SOURCE.index(start)
    end_index = SOURCE.index(end, start_index)
    return SOURCE[start_index:end_index]


PBW = _between(
    r"\begin{theorem}[PBW--Slodowy",
    r"\begin{corollary}[Principal affine",
)
HOOK = _between(
    r"\label{thm:hook-transport-corridor}",
    r"\begin{proposition}[Transport propagation",
)
OPE_DEGREE = _between(
    r"\label{thm:canonical-degree-detection}",
    r"\begin{remark}[The comparison required",
)
BP_AUDIT = _between(
    r"\label{comp:bp-kappa-three-paths}",
    r"\begin{proposition}[Standard Bershadsky--Polyakov",
)
BP_LEDGER = _between(
    r"\label{prop:bp-subregular-standard-family-ledger}",
    r"\begin{remark}[Genus-$1$ curvature calculation required]",
)
BP_COMPANION = _between(
    r"\label{thm:bp-koszul-self-dual}",
    r"\begin{remark}[Exact symbolic identities]",
)


def test_pbw_slodowy_stops_at_the_associated_graded_page():
    assert r"\ClaimStatusConditional" in PBW
    assert r"H_{\mathrm{PBW}}^{\mathrm{bar}}" in PBW
    assert r"E_1^{\mathrm{PBW}}" in PBW
    assert r"\overline B_{\mathrm{alg}}" in PBW
    assert "associated-graded chiral collision complex" in PBW
    assert "collapses at $E_1$" not in PBW


def test_ope_degree_is_kept_separate_from_bar_dual_arity():
    assert r"d_{\mathrm{OPE}}(A;V)" in OPE_DEGREE
    assert "Taylor coefficient" not in OPE_DEGREE
    assert "completed dual" not in OPE_DEGREE
    assert r"d_r = 0" not in OPE_DEGREE


def test_bp_uses_even_fkr_generators_and_standard_conductor():
    assert "even generators $J,G^+,G^-,T$" in BP_AUDIT
    assert r"-\frac{(2k+3)(3k+1)}{k+3}" in BP_AUDIT
    assert r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50" in BP_AUDIT
    assert r"c_{\mathrm{BP}}^{\mathrm{shift}}(-k-6)=196" in BP_AUDIT
    assert r"1+\frac23+\frac23+\frac12=\frac{17}{6}" in BP_AUDIT


def test_bp_modular_invariants_remain_open():
    assert r"\ClaimStatusOpen" in BP_AUDIT
    assert "non-separating genus-$1$" in BP_AUDIT
    assert r"$\kappa_{\mathrm{BP}}$, $\varrho_{\mathrm{BP}}$, and" in BP_LEDGER
    assert r"$K^\kappa_{\mathrm{BP}}$ are open genus-$1$ invariants" in BP_LEDGER
    assert r"H_{\mathrm{BP}}^{H}" in BP_LEDGER
    assert "finite/perfect Verdier duality" in BP_LEDGER
    assert "ordered acyclicity, averaging descent" in BP_LEDGER
    for stale in (
        r"\kappa(\mathrm{BP}_k)=\frac{1}{6}c_{\mathrm{BP}}(k)",
        r"K^\kappa(\mathrm{BP}_k,\mathrm{BP}_{-k-6})=\frac{98}{3}",
        r"\varrho_{\mathrm{BP}} = \frac{1}{6}",
    ):
        assert stale not in SOURCE


def test_hook_and_bp_same_family_statements_name_the_comparison_package():
    assert r"H_{\mathrm{hook}}^{\mathrm{DS/bar}}" in HOOK
    assert "same-family candidate" in HOOK
    assert "Membership in KSDual is the stronger assertion" in HOOK
    assert r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}" in BP_COMPANION
    assert r"(\mathrm{BP}_k)^!\simeq\mathrm{BP}_{-k-6}" in BP_COMPANION
    assert "KSDual membership" in BP_COMPANION
    assert "remains open" in BP_COMPANION
