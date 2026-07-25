"""Scope guards for the KSDual fixed-locus statements."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
MASTER_RECONSTRUCTION = ROOT / "chapters/connections/master_reconstruction.tex"
MASTER_CONCORDANCE = ROOT / "chapters/connections/master_concordance.tex"
FOURIER_SEED = ROOT / "chapters/theory/fourier_seed.tex"
TYPE_SYSTEM = ROOT / "appendices/type_system.tex"
FIVE_THEOREMS = ROOT / "standalone/five_theorems_modular_koszul.tex"
CLAUDE = ROOT / "CLAUDE.md"


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


class TestMasterKSDualScope:
    def test_ksdual_definition_uses_the_homotopy_fixed_curved_ambient(self):
        window = window_after(MASTER_RECONSTRUCTION, r"\label{sec:mr-ksdual}", 4500)
        for anchor in (
            "finite-type curved, weight-completed ambient",
            r"Theorem~\ref{thm:universal-defect-construction}",
            r"Proposition~\ref{prop:fourier-five-duality-objects}",
            r"\Kosz^{\mathrm{ft,curv}}(X,D,\tau)",
            "homotopy-fixed locus over the\nuncurved Koszul charts",
            r"A point is a triple $(A_b,\varphi_b,H_b)$",
            "The homotopy-fixed datum",
            r"$(\varphi_b,H_b)$ determines membership",
        ):
            assert_anchor(window, anchor)

    def test_ksdual_theorem_is_an_equivariant_reconstruction_restriction(self):
        window = window_after(MASTER_RECONSTRUCTION, r"\label{thm:mr-ksdual}", 9000)
        for anchor in (
            r"hypothesis package $H_{\mathrm{MR}}\cup H_\sigma$",
            r"Let $(A_b,\varphi_b,H_b)$ be a point of",
            "The fixed-point equivalence identifies the chart algebra with\nits Koszul dual",
            "Independently, the bar--cobar counit identifies",
            r"under $H_1$",
            "equivariant factorization Eilenberg--Watts and center\ncomparisons",
            r"\xrightarrow[H_Z]{\sim}Z_{\ch}^{\mathrm{int}}(\mathsf C)",
            r"An $H_\sigma$-equivariant modular realization",
            r"\mathfrak O^K_{g,n}(A_b)=\mathfrak O^K_{g,n}(A_b^!)",
            r"\operatorname{obs}^{\mathrm{Hdg}}_{g,n}(A_b)",
            r"F_{g,n}(A_b;\alpha)=F_{g,n}(A_b^!;\alpha)",
        ):
            assert_anchor(window, anchor)

    def test_ksdual_witness_remark_separates_orbit_data_and_fixed_data(self):
        window = window_after(
            MASTER_RECONSTRUCTION,
            r"\label{rem:mr-ksdual-witnesses}",
            4500,
        )
        for anchor in (
            r"orbit datum is a pair $(A,\sigma A)$ together with scalar identities",
            r"A KSDual point is the triple $(A,\varphi,H)$",
            r"$\mathcal H_k\mapsto \mathrm{Sym}^{\ch}(V^*)$",
            r"Remark~\ref{rem:fourier-heisenberg-not-selfdual}",
            r"$\beta\gamma_\lambda\leftrightarrow bc_\lambda$",
            r"$V_{\Lambda_{24}}^!\simeq V_{\Lambda_{24}}$",
            "Mukai-enhanced K3 Heisenberg",
            r"$2c_+(\mathrm{Mukai}(K3))=8$",
            r"\ClaimStatusConjectured{} under",
            r"$H_{\mathsf B}$",
            "coherent homotopy $H$",
        ):
            assert_anchor(window, anchor)

        assert r"\label{rem:fourier-heisenberg-not-selfdual}" in visible(FOURIER_SEED)

    def test_master_reconstruction_w3_bp_scalar_lanes_are_typed(self):
        source = visible(MASTER_RECONSTRUCTION)
        label = r"\label{rem:mr-ksdual-witnesses}"
        label_pos = source.index(label)
        start = source.rfind(r"\begin{remark}", 0, label_pos)
        end = source.index(r"\end{remark}", label_pos)
        block = source[start:end]
        compact = re.sub(r"\s+", "", block)

        for anchor in (
            r"\ClaimStatusComputed",
            r"c_{\mathcalW_3}(k)=2-\frac{24(k+2)^2}{k+3}",
            r"c_{\mathcalW_3}(k)+c_{\mathcalW_3}(-k-6)=100",
            r"c^{\mathrm{mid}}_{\mathcalW_3}=50",
            r"k=-3\pmi",
            r"c_{\mathrm{BP}}(k)=-\frac{(2k+3)(3k+1)}{k+3}",
            r"K^c_{\mathrm{BP}}=c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50",
            r"c^{\mathrm{mid}}_{\mathrm{BP}}=25",
            r"k=-3\pm2i",
            r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}",
            r"c_{\mathrm{BP}}^{\mathrm{shift}}(k)=2-\frac{24(k+1)^2}{k+3}",
            r"c_{\mathrm{BP}}^{\mathrm{shift}}(k)+c_{\mathrm{BP}}^{\mathrm{shift}}(-k-6)=196",
        ):
            assert anchor in compact, anchor

        for anchor in (
            "vertex operator algebra whose strong generators",
            r"$J,G^+,G^-,L$ are even fields",
            r"\cite[\S2.1]{FKR20}",
            "genus-$1$\nanomaly ratio therefore requires the complete non-separating curvature\ncalculation",
            "direct genus-$1$ curvature computation of the non-separating modular trace",
            "exact central-charge midpoint",
            r"regular $k\ne-3$",
            "finite-type bar dual or a completed continuous nondegenerate Verdier pairing",
            "subregular hook-type DS/bar transport",
            "computed-secondary scalar convention",
        ):
            assert_anchor(block, anchor)

        normalization_start = block.index("The conditional normalization")
        normalization_end = block.index(
            "The exact central-charge midpoint", normalization_start
        )
        normalization = re.sub(
            r"\s+", "", block[normalization_start:normalization_end]
        )
        for anchor in (
            r"\kappa_{\mathrm{BP}}(k)=\frac16c_{\mathrm{BP}}(k)",
            r"\varrho_{\mathrm{BP}}=\frac{\kappa_{\mathrm{BP}}(k)}{c_{\mathrm{BP}}(k)}=\frac16",
            r"K^\kappa_{\mathrm{BP}}=\varrho_{\mathrm{BP}}K^c_{\mathrm{BP}}=\frac{25}{3}",
            r"\ClaimStatusOpen",
        ):
            assert anchor in normalization, anchor
        assert r"\ClaimStatusComputed" not in normalization

        for stale in (
            r"=98",
            r"\frac{98}{3}",
            r"98/3",
        ):
            assert stale not in compact

        normalized_block = re.sub(r"\s+", " ", block)
        assert (
            "same scalar condition occurs at the analytically continued shifted levels"
            not in normalized_block
        )
        assert "The strong-generator ratio and modular conductor are" not in block

    def test_concordance_and_claude_rule_surfaces_match_repaired_scope(self):
        concordance = visible(MASTER_CONCORDANCE)
        for anchor in (
            "finite-type curved, weight-completed ambient",
            "Its homotopy-fixed locus\nover the uncurved Koszul charts is",
            r"$\KSDual(X,D,\tau)$ of Definition~\ref{def:mr-ksdual}",
            r"triple $(A_b,\varphi_b,H_b)$",
            "Theorem~A supplies\nthe separate bar--cobar equivalence under $H_1$",
            "Theorem~H carries its\nfamily-indexed deformation-retract hypotheses",
            "Each row carries a scalar parameter involution or orbit relation",
            "Parameter relation & Fixed-parameter candidate",
            "At an object-level KSDual point",
        ):
            assert_anchor(concordance, anchor)

        claude = visible(CLAUDE)
        for anchor in (
            "finite-type curved Verdier--Koszul ambient",
            r"Theorem H remains conditional on its \(H_H\) package",
            "actual fixed locus",
            "Universal Trace Identity is the equivariant signature",
        ):
            assert_anchor(claude, anchor)

    def test_stale_ksdual_overclaims_do_not_return(self):
        source = "\n".join(
            visible(path)
            for path in (
                MASTER_RECONSTRUCTION,
                MASTER_CONCORDANCE,
                TYPE_SYSTEM,
                FIVE_THEOREMS,
                CLAUDE,
            )
        )
        for forbidden in (
            "every reconstruction step is an equivalence",
            "at every level of the tower",
            "the five-archetype dichotomy stabilises",
            "Self-dual scalar witnesses",
            "On the finite standard-landscape atlas the $\\KSDual$ witnesses include",
            "self-dual fixed point under $\\sigma$",
            "self-dual locus $\\kappa+\\kappa^!=0$",
        ):
            assert forbidden not in source

    def test_type_system_and_summary_scope_ksdual_exactness_by_package(self):
        type_system = visible(TYPE_SYSTEM)
        for anchor in (
            "finite-type curved\nVerdier--Koszul ambient",
            "On the admissible Koszul-complete part of\n$\\KSDual$",
            "Theorem~A restricts from adjunction to its unit / counit\n"
            "equivalence under the Koszul-complete package",
            "every other projection\nretains its own reconstruction morphism and hypothesis package",
            "for every family datum $H_H(\\Ab;S)$, Theorem~H identifies the\n"
            "complete chiral Hochschild complex with a strong deformation retract",
            "critical, non-Koszul, and completed families carry\n"
            "their own support sets, spectral sequences, and convergence data",
            "membership in\n$\\KSDual$ is carried by the coherent homotopy-fixed datum",
        ):
            assert_anchor(type_system, anchor)

        five = visible(FIVE_THEOREMS)
        for anchor in (
            "finite-type curved\nVerdier--Koszul ambient",
            "chosen self-duality map\n$\\sigma_\\cA\\colon\\cA\\xrightarrow{\\sim}K_X(\\cA)$ represents the fixed\npoint",
            "Theorem~H retains its family support set~$S$",
            "five-archetype label is rigid on the admissible finite-type\n"
            "curved fixed locus",
            "the finite-type curved\nVerdier--Koszul fixed-point criterion supplies KSDual membership",
        ):
            assert_anchor(five, anchor)
