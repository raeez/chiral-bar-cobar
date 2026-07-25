"""Scope guards for the Master Reconstruction Bourbaki theorem."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MASTER_RECONSTRUCTION = ROOT / "chapters/connections/master_reconstruction.tex"
MASTER_CONCORDANCE = ROOT / "chapters/connections/master_concordance.tex"


def visible(path: Path) -> str:
    text = path.read_text()
    return "\n".join(
        line for line in text.splitlines()
        if not line.lstrip().startswith("%")
    )


def window_after(path: Path, label: str, chars: int) -> str:
    text = visible(path)
    start = text.find(label)
    assert start >= 0, f"missing label {label}"
    return text[start:start + chars]


def assert_anchor(window: str, anchor: str) -> None:
    normalized_window = re.sub(r"\s+", " ", window)
    normalized_anchor = re.sub(r"\s+", " ", anchor)
    assert anchor in window or normalized_anchor in normalized_window, anchor


class TestMasterBourbakiScope:
    def test_bourbaki_recovery_is_chart_side_and_scalar_descent_stops_at_level_3(self):
        window = window_after(
            MASTER_RECONSTRUCTION,
            r"\label{thm:mr-bourbaki}",
            9000,
        )
        for anchor in (
            "recoverability is chart-side rather than omnidirectional",
            "levels~$0$, $1$, and~$2$ determine one another",
            r"$H_0\cup H_1$",
            "bar--cobar inversion on the Koszul locus",
            "scalar-side descent is conditional and stops at the centre",
            "full trace-plus-clutching system",
            r"strictly more than the bare scalar tuple $(\kappa,Z_g,F_g)$",
            r"Theorem~\ref{thm:mr-H} is a formation-and-concentration theorem",
            "not a reconstruction theorem from level~$3$ to level~$2$",
            "open level-$3$-to-level-$2$ reconstruction problem",
            r"Remark~\ref{rem:mr-five-objects}",
        ):
            assert_anchor(window, anchor)

    def test_bourbaki_rigidity_is_faithful_only_from_levels_0_1_2(self):
        window = window_after(
            MASTER_RECONSTRUCTION,
            r"\label{thm:mr-bourbaki}",
            11000,
        )
        for anchor in (
            "rigidity is faithful only from levels~$0$, $1$, and~$2$",
            r"$\cC^\op$ fixing~$b$",
            r"$A_b$, or on $B(A_b)$",
            "Levels~$3$, $4$, and $5$ do not have this faithfulness",
            "corestriction of the bar coalgebra",
            r"B(\phi)=T^c(s^{-1}\bar\phi)",
            r"to the cogenerators $s^{-1}\bar A_b$",
            r"$\bar\phi=\mathrm{id}_{\bar A_b}$",
        ):
            assert_anchor(window, anchor)

    def test_bourbaki_proof_names_nonfaithful_scalar_witnesses(self):
        window = window_after(
            MASTER_RECONSTRUCTION,
            r"\label{thm:mr-bourbaki}",
            12000,
        )
        for anchor in (
            r"Lemma~\ref{lem:master-scalar-non-faithfulness}",
            r"Theorem~\ref{thm:master-scalar-nonfaithful-witness-c16}",
            "rank-one Heisenberg sign automorphism",
            r"$\alpha\mapsto-\alpha$",
            r"level~$4$ Fock line $F_\lambda$ with $F_{-\lambda}$",
            r"level~$4$ rigidity is at most Morita or inner rigidity",
        ):
            assert_anchor(window, anchor)

        concordance = visible(MASTER_CONCORDANCE)
        assert r"\label{lem:master-scalar-non-faithfulness}" in concordance
        assert r"\label{thm:master-scalar-nonfaithful-witness-c16}" in concordance

    def test_false_any_level_recovery_and_rigidity_phrases_do_not_return(self):
        text = visible(MASTER_RECONSTRUCTION)
        for forbidden in (
            "the typical structure is recovered from any one of its five projections",
            "recoverable from any level",
            "Recoverability from any one level",
            "identity on any one level",
            "acting as the identity at any level",
            "generate all five levels",
            "projections generate all five levels",
        ):
            assert forbidden not in text
