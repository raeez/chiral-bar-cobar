"""Source guards for the quadratic-presentation/bar/Verdier type firewall."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def live_tex() -> list[Path]:
    return sorted((ROOT / "chapters").rglob("*.tex")) + sorted(
        (ROOT / "standalone").rglob("*.tex")
    )


AI = (
    r"(?:\\cA|\\mathcal\{A\}|(?<![A-Za-z\\])A)"
    r"(?:_\{[^}]+\}|_[A-Za-z\\]+)?"
    r"(?:\^\{\\mathrm\s*\{?i\}?\}|\^\{i\}|\^i)"
)
AI_AS_BAR_COHOMOLOGY = re.compile(
    AI + r"\s*(?::=|=|&\s*=\s*&|\\coloneqq)\s*H\^"
)
BAR_COHOMOLOGY_TO_PARTNER = re.compile(
    r"(?:\\cA|\\mathcal\{A\}|(?<![A-Za-z\\])A)\^!"
    r".{0,50}(?:\\mathbb D|D_|\\vee).{0,50}H\^"
    r"|H\^.{0,50}(?:\\mathbb D|D_|\\vee).{0,50}"
    r"(?:\\cA|\\mathcal\{A\}|A)\^!"
)
REVERSED_QUADRATIC_MAP = re.compile(
    r"(?:\\bar\{?B\}?|\\barB).{0,100}"
    r"(?:\\longrightarrow|\\to|\\xrightarrow).{0,100}" + AI
)


def test_presentation_coalgebra_is_never_defined_as_bar_cohomology():
    offenders = []
    for path in live_tex():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if AI_AS_BAR_COHOMOLOGY.search(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}")
    assert offenders == []


def test_partner_has_no_direct_bar_cohomology_bypass_or_reversed_q_map():
    bypasses = []
    reversals = []
    for path in live_tex():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            anchor = f"{path.relative_to(ROOT)}:{number}"
            if BAR_COHOMOLOGY_TO_PARTNER.search(line):
                bypasses.append(anchor)
            if REVERSED_QUADRATIC_MAP.search(line):
                reversals.append(anchor)
    assert bypasses == []
    assert reversals == []


def test_foundational_chapters_display_all_comparison_maps():
    required = {
        "chapters/theory/bar_construction.tex": (
            r"\cA^i:=C_X(s^{-1}\mathcal V,s^{-2}R)",
            r"q_\cA\colon\cA^i\longrightarrow\barB_X(\cA)",
            r"K_X(\cA):=\mathbb{D}_{\operatorname{Ran}}\barB_X(\cA)",
            r"\mathbb D(q_\cA)",
            r"\nu_\cA\colon K_X(\cA)\to\cA^!",
        ),
        "chapters/theory/bar_cobar_adjunction_curved.tex": (
            r"\cA^i=C_X(s^{-1}V,s^{-2}R)",
            r"q_\cA\colon\cA^i\longrightarrow\barBch(\cA)",
            r"K_X(\cA)=\mathbb D_{\Ran}\barBch(\cA)",
            r"\nu_\cA\colon K_X(\cA)\longrightarrow\cA^!",
        ),
        "chapters/theory/chiral_koszul_pairs.tex": (
            r"\cA_1^{\mathrm i}=C_X(s^{-1}V_1,s^{-2}R_1)",
            r"q_{\cA_1}\colon\cA_1^{\mathrm i}\longrightarrow",
            r"\mathbb D(q_{\cA_1})",
            r"\nu_{12}\colon K_X(\cA_1)\xrightarrow{\sim}\cA_2",
        ),
    }
    for relative, fragments in required.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {relative}"


def test_chiral_koszul_pairs_residue_candidate_has_a_typed_comparison_roof():
    text = (ROOT / "chapters/theory/chiral_koszul_pairs.tex").read_text(
        encoding="utf-8"
    )
    lane = text.split(r"\section{Quadratic recognition and residue-dual comparison}", 1)[
        1
    ].split(r"\section{Explicit calculations:", 1)[0]
    compact = re.sub(r"\s+", "", lane)
    required = (
        r"\mathcalA^{\mathrm i}=C_X(s^{-1}\mathcalV,s^{-2}R)",
        r"q_{\mathcalA}\colon\mathcalA^{\mathrm i}\longrightarrowB_X(\mathcalA)",
        r"\mathcalC_{\mathcalA}^{\mathrm{res}}=C_X(s^{-1}\mathcalV^\vee,s^{-2}R^\perp)",
        r"C_X(s^{-1}\mathcalV^\vee,s^{-2}R^\perp)=\bigl(\mathcalA^!_{\mathrm{quad}}\bigr)^{\mathrm i}",
        r"H_{\mathrm{res}}(\mathcalA;\beta,\chi)",
        r"\chi_{\mathcalA,\beta}\colon\mathcalA^{\mathrm i}\longrightarrow\mathcalC_{\mathcalA}^{\mathrm{res}}",
        r"\nu_{\mathcalA}=c_{\mathcalA}\circ\mathbbD(q_{\mathcalA})",
    )
    for fragment in required:
        assert re.sub(r"\s+", "", fragment) in compact, fragment
    assert r"\mathcal{A}^{\mathrm i}_{\mathrm{cand}}" not in lane
    assert r"\Phi\colon" not in lane
    assert r"B_X(\mathcalA)\xleftarrow" in compact
    assert r"\mathcalA^{\mathrmi}\xrightarrow" in compact


def test_chiral_koszul_pairs_keeps_nonquadratic_bar_outputs_distinct():
    text = (ROOT / "chapters/theory/chiral_koszul_pairs.tex").read_text(
        encoding="utf-8"
    )
    required = (
        r"\mathsf H_c^{\mathrm{bar}}(\mathrm{Vir})",
        r"K_X(\mathrm{Vir}_c)",
        r"\nu_{\mathrm{Vir}_c}\colon K_X(\mathrm{Vir}_c)",
        r"\mathsf H^{\mathrm{bar}}(W_3)",
        r"K_X(W_3)",
        r"\mathsf H^{\mathrm{bar}}(W_N)",
        r"K_X(W_N)",
        r"\mathcal C_{\mathcal A}^{\mathrm{bar,ord}}",
        r"K_X^{\mathrm{ord}}(\mathcal A)",
    )
    for fragment in required:
        assert fragment in text, fragment
    forbidden = (
        "\\mathrm{Vir}_c^{\\mathrm i}\n=H^*",
        "W_3^{\\mathrm i}\n=H^*",
        "W_N^{\\mathrm i}\n=H^*",
        "\\mathcal{A}^{\\mathrm i}_{\\mathrm{ord}}\n\\coloneqq \\bar{B}",
    )
    for pattern in forbidden:
        assert pattern not in text, pattern


def test_chiral_koszul_pairs_has_no_double_cobar_partner_route():
    text = (ROOT / "chapters/theory/chiral_koszul_pairs.tex").read_text(
        encoding="utf-8"
    )
    assert (
        re.search(
            r"\\Omega.{0,120}(?:\\to|\\longrightarrow|\\xrightarrow|\\simeq)"
            r".{0,80}(?:\\cA|\\mathcal\{A\}|A)\^!",
            text,
            flags=re.DOTALL,
        )
        is None
    )
    assert r"\Omega_XB_X(\mathcal A)\to\mathcal A" in text


def test_repaired_koszul_claims_and_alias_are_conditional():
    text = (ROOT / "chapters/theory/chiral_koszul_pairs.tex").read_text(
        encoding="utf-8"
    )
    claims = {
        "cor:bar-cohomology-koszul-dual": "corollary",
        "thm:coalgebra-axioms-verified": "theorem",
        "thm:bar-computes-koszul-dual-complete": "theorem",
        "thm:chiral-koszul-duality": "theorem",
        "cor:circularity-free-koszul": "corollary",
        "thm:structure-exchange": "theorem",
        "thm:ainfty-duality-exchange": "theorem",
    }
    for label, environment in claims.items():
        marker = rf"\label{{{label}}}"
        label_index = text.index(marker)
        start = text.rfind(rf"\begin{{{environment}}}", 0, label_index)
        end = text.index(rf"\end{{{environment}}}", label_index)
        block = text[start:end]
        assert start >= 0, label
        assert r"\ClaimStatusConditional" in block, label
        assert r"\ClaimStatusProvedHere" not in block, label


def test_concordance_syncs_the_quadratic_recognition_status_ledger():
    text = (ROOT / "chapters/connections/concordance.tex").read_text(
        encoding="utf-8"
    )
    ledger = text.split("Quadratic-recognition subsidiary status ledger.", 1)[1]
    ledger = ledger.split(r"\end{tabular}", 1)[0]
    labels = (
        "thm:coalgebra-axioms-verified",
        "thm:bar-computes-koszul-dual-complete",
        "thm:chiral-koszul-duality",
        "cor:circularity-free-koszul",
        "cor:bar-cohomology-koszul-dual",
        "thm:structure-exchange",
        "thm:ainfty-duality-exchange",
    )
    for label in labels:
        assert rf"\ref{{{label}}}" in ledger, label
    assert ledger.count(r"\ClaimStatusConditional") == 6
    assert r"\ClaimStatusProvedHere" not in ledger
    for package in (
        r"H_{\mathrm{CL}}",
        r"H_{\mathrm{res}}",
        r"H_{\mathbb D}^{\mathrm{bar}}",
        r"\nu_A=c_A\circ\mathbb D(q_A)",
    ):
        assert package in ledger, package


def test_repaired_standalones_use_family_indexed_theorem_h_support():
    surfaces = (
        "standalone/programme_summary.tex",
        "standalone/survey_modular_koszul_duality.tex",
        "standalone/survey_modular_koszul_duality_v2.tex",
        "standalone/survey_track_a_compressed.tex",
    )
    for relative in surfaces:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert "H_H(" in text, relative
        assert r"\operatorname{Supp}" in text, relative
        assert r"\subseteq S" in text, relative
        assert r"\{0,2,3\}" in text, relative
        assert "strong deformation retract" in text, relative
        assert "amplitude $[0,2]$" not in text, relative
        assert r"degrees $\{0,1,2\}$" not in text, relative
