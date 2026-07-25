"""Guards for the repaired chiral-climax theorem and scalar ledger."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
TARGET = ROOT / "chapters/theory/chiral_climax_platonic.tex"


def source() -> str:
    return TARGET.read_text()


def normalized() -> str:
    return re.sub(r"\s+", " ", source())


class TestTypedArnoldSurface:
    def test_kz_comparison_has_four_named_hypotheses(self):
        text = source()
        for hypothesis in (
            r"H_{\mathrm{fin}}",
            r"H_{\log}",
            r"H_{\mathrm{Borch}}",
            r"H_{\mathrm{FM}}",
        ):
            assert hypothesis in text
        assert r"\nabla^{B,0}_{A,V,n}" in text
        assert "FM-boundary residue realization" in text

    def test_operator_and_form_halves_are_both_present(self):
        text = normalized()
        assert "disjoint-pair infinitesimal braid relation" in text
        assert "simple-pole projection of the Borcherds identity" in text
        assert "Arnold's three-term form identity" in text


class TestScalarTypeFirewall:
    def test_five_scalar_types_are_separated(self):
        text = source()
        for scalar in (
            r"K^c(A)",
            r"K^\kappa(A)",
            r"c_{\mathrm{gh}}(R_\bullet)",
            r"K^{\mathrm{lat}}(L)",
            r"\kappa_{\mathrm{BKM}}(\Phi)",
        ):
            assert scalar in text

    def test_computed_vol_i_modular_ledger(self):
        text = normalized()
        assert r"K^\kappa(A)\in\left\{0,13,\frac{250}{3}\right\}" in text
        assert r"\{0,13,250/3\}_{\mathrm{Vol\,I}}" in text

    def test_bp_lane_is_central_and_modular_slot_is_open(self):
        text = source()
        assert r"K^c_{\mathrm{BP}}" in text
        assert "=50" in text
        assert "The generators $J,G^+,G^-,T$ are even" in text
        window = text[text.index(r"\item \emph{Bershadsky--Polyakov.}") :]
        window = window[: window.index(r"\item \emph{Mukai lattice candidate.}")]
        assert r"\ClaimStatusOpen" in window
        assert r"K^\kappa_{\mathrm{BP}}" in window

    def test_mukai_eight_is_lattice_exact_and_chiral_conditional(self):
        text = normalized()
        assert (
            r"K^{\mathrm{lat}}\bigl(\widetilde H(K3,\mathbb Z)\bigr) =2c_+=8"
            in text
        )
        for hypothesis in (
            r"H_{\mathrm{chart}}",
            r"H_{\mathrm{KD}}",
            r"H_{\mathrm{scalar}}",
            r"H_{\mathrm{mod}}",
            r"H_{\mathrm{quantum}}",
        ):
            assert hypothesis in text
        assert r"\{0,8,13,250/3\}_{H_{\mathsf B}}" in text

    def test_stale_bp_and_universal_ghost_claims_are_absent(self):
        text = source()
        retired = (
            r"\frac{98}{3}",
            "98/3",
            "universal identity",
            "genuinely disjoint",
            r"E^{\mathrm{nod}}_{24}",
        )
        for fragment in retired:
            assert fragment not in text
        assert re.search(r"(?<!\d)196(?!\d)", text) is None
        assert re.search(
            r"\\kappa\(A\)\s*&?=\s*-\\,?\\cghost",
            text,
        ) is None


class TestK3FrontierStatus:
    def test_bruinier_and_lusztig_are_scoped_to_actual_inputs(self):
        text = normalized()
        assert "Bruinier (2002, Lemma~5.1) supplies a coefficient-field statement" in text
        assert "Lusztig (1990) constructs quantum groups at a chosen admissible root order" in text
        assert "the comparison maps themselves remain the open mathematics" in text

    def test_humbert_and_canonical_curve_surfaces_are_open(self):
        text = source()
        for label in (
            r"\label{lem:cclimax-H1-failure}",
            r"\label{lem:cclimax-H3-failure}",
            r"\label{lem:cclimax-H4-failure}",
            r"\label{thm:cclimax-global-inversion-all-admissible}",
            r"\label{thm:climax-crown-canonical-curve}",
        ):
            start = text.index(label)
            window = text[start : start + 1000]
            assert r"\ClaimStatusOpen" in window

    def test_elliptic_k3_base_and_reference_curve_are_distinguished(self):
        text = normalized()
        assert (
            r"An elliptic K3 fibration \(\pi\colon K3\to\mathbb P^1\) "
            r"has base \(\mathbb P^1\)"
            in text
        )
        assert (
            r"The elliptic factor \(E\), the base \(\mathbb P^1\), "
            r"and the nodal fibres are three distinct geometric objects."
            in text
        )
