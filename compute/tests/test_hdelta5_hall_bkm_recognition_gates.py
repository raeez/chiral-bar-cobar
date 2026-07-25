from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VOL3 = ROOT.parent / "calabi-yau-quantum-groups"

GUIDE = ROOT / "chapters/frame/guide_to_main_results.tex"
PART_II = ROOT / "chapters/frame/part_ii_platonic_introduction.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"
PART_III = ROOT / "chapters/frame/part_iii_platonic_introduction.tex"
OPEN_BEILINSON = ROOT / "chapters/frame/open_beilinson_tower_platonic.tex"
LANDSCAPE = ROOT / "chapters/examples/landscape_census.tex"
DEFORMATION = ROOT / "chapters/examples/deformation_quantization.tex"
W_ALGEBRAS = ROOT / "chapters/examples/w_algebras.tex"
YANGIAN_FOUNDATIONS = ROOT / "chapters/examples/yangians_foundations.tex"
YANGIAN_COMPUTATIONS = ROOT / "chapters/examples/yangians_computations.tex"
YANGIAN_DK = ROOT / "chapters/examples/yangians_drinfeld_kohno.tex"
GENUS_EXPANSIONS = ROOT / "chapters/examples/genus_expansions.tex"
BAR_COMPLEX_TABLES = ROOT / "chapters/examples/bar_complex_tables.tex"
LATTICE_FOUNDATIONS = ROOT / "chapters/examples/lattice_foundations.tex"
SYMMETRIC_ORBIFOLDS = ROOT / "chapters/examples/symmetric_orbifolds.tex"
EXCEPTIONAL_YANGIAN = ROOT / "chapters/examples/exceptional_yangian_koszul_duality_platonic.tex"

K3_CHIRAL = VOL3 / "chapters/examples/k3_chiral_bialgebra_platonic.tex"
K3E_BKM = VOL3 / "chapters/examples/k3e_bkm_chapter.tex"
CY_TO_CHIRAL = VOL3 / "chapters/theory/cy_to_chiral.tex"


def read(path: Path) -> str:
    return path.read_text()


def squashed(path: Path) -> str:
    return " ".join(read(path).split())


def test_vol_i_summaries_keep_hdelta5_as_open_recognition_target():
    required = (
        r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
        r"\ClaimStatusOpen",
        "determinant comparison problem",
        r"H_{\Delta_5}^{\mathrm{det}}",
        "compact Hall--Borcherds recognition package",
        "PBW presentation theorem",
        "Mittag--Leffler",
        r"\chi_{\mathrm{top}}(K3)=24",
        "open analytic obligation",
        "all-orders associator on a Hall realisation",
        "compact Hall source, comparison maps, and pentagon identities",
    )
    retired = (
        r"genus-$1$ free energy of $\mathbf H_{\Delta_5}$",
        r"chiral bialgebra realisation $\mathbf H_{\Delta_5}$",
        r"carves $\mathbf H_{\Delta_5}$",
        r"pentagon tower $\{\phi^{(n)}\}_{n\ge 3}$ of $\mathbf H_{\Delta_5}$",
        r"\ClaimStatusProvedElsewhere]\label{thm:guide-k3-master-L-value}",
        r"\ClaimStatusProvedElsewhere]",
        r"=\;-\log\Delta_5 \;-\; 24\,L'(0,\Delta_5,\mathrm{std})",
    )

    for path in (GUIDE, PART_II):
        text = squashed(path)
        for fragment in required:
            assert fragment in text, f"{fragment!r} missing from {path}"
        for fragment in retired:
            assert fragment not in text, f"retired fragment {fragment!r} still in {path}"


def test_vol_i_frame_surfaces_type_hdelta5_as_an_open_comparison():
    required = (
        r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
        r"\ClaimStatusOpen",
        r"H_{\Delta_5}^{\mathrm{det}}",
        "determinant comparison",
        "Mittag--Leffler",
        r"\chi_{\mathrm{top}}(K3)=24",
    )
    retired = (
        r"The genus-$1$ free energy of $\mathbf H_{\Delta_5}$",
        r"genus-$1$ free energy of $\mathbf H_{\Delta_5}$ is the master",
        r"its chiral bialgebra realisation $\mathbf H_{\Delta_5}$",
        r"\mathbf H_{\Delta_5} =\mathrm{Borch}(F_3,\phi^{K3}_{0,1})",
    )

    for path in (PART_III, OPEN_BEILINSON):
        text = squashed(path)
        for fragment in required:
            assert fragment in text, f"{fragment!r} missing from {path}"
        for fragment in retired:
            assert fragment not in text, f"retired fragment {fragment!r} still in {path}"

    assert r"\ClaimStatusOpen" in read(PART_III)


def test_vol_iii_hdelta5_definition_has_source_recognition_gates():
    text = squashed(K3_CHIRAL)

    required = (
        r"\mathbf{H}_{\Delta_5}^{\mathrm{tgt}}",
        "compact Hall--Drinfeld object only after a finite Hall/CoHA source",
        "compact Hopf pairing",
        "source-to-target comparison maps",
        "PBW/no-extra-relations theorem",
        "exact inverse-limit passage",
        "Mittag--Leffler exact inverse limit",
        "No scalar identity replaces these algebraic conditions.",
        r"\Phi_3 = \SpCh_{\Sigma_2, C} \circ \PhiFA_3",
        r"Native operadic level is $\Eone$ on the reference curve $C$",
    )
    for fragment in required:
        assert fragment in text, fragment


def test_vol_iii_bkm_finite_height_recognition_is_not_scalar_shadow():
    text = squashed(K3E_BKM)

    required = (
        "Euler--Hall pairing, coproduct, centre, associator class",
        "finite-height associated graded maps are algebra isomorphisms",
        "no-extra condition",
        "PBW condition",
        "Mittag--Leffler compatibility",
        "The Weyl vector",
        "Even imaginary simple roots",
        "Odd imaginary simple roots",
        "target parity fixture",
        "Finite Borcherds core: superdimensions, PBW, Serre, and primitive coproduct",
        "No Drinfeld $J$-presentation or Yangian coproduct is used",
        "not the Drinfeld-new Hall coproduct",
    )
    for fragment in required:
        assert fragment in text, fragment


def test_zeta8_and_hbar_specialisations_remain_conditional():
    k3_text = squashed(K3_CHIRAL)
    deformation_text = squashed(DEFORMATION)

    k3_required = (
        r"Let $\zeta_8 = e^{2\pi i/8}$",
        "completed Hall--Drinfeld double carrying a divided-power integral form",
        r"PBW dimension trichotomy at \texorpdfstring{$\zeta_8$}{zeta-8}",
        "Real-root PBW block.",
        "First-wall Grassmann enhancement.",
        "2^{21}",
        "2^{25}",
        r"Order-\(\hbar^3\) pentagon closure is checked",
        r"the statement $\hbar^2=-1/8$ is a normalisation convention",
    )
    for fragment in k3_required:
        assert fragment in k3_text, fragment

    deformation_required = (
        r"$\hbar^2=-1/8$ is an external Lusztig/CY-specialization input",
        r"The root-of-unity point \(\hbar^2=-1/8\) is a separate",
        r"The Lusztig value $\hbar^2=-1/8$ belongs to the integral-form",
    )
    for fragment in deformation_required:
        assert fragment in deformation_text, fragment


def test_two_stage_cy_to_chiral_parameter_tagging_is_explicit():
    text = squashed(CY_TO_CHIRAL)

    required = (
        r"\Phi_d^{(\Sigma_{d-1}, C)}(\cC) := \SpCh_{\Sigma_{d-1}, C}(\PhiFA_d(\cC))",
        r"reference curve $C",
        "Stage-$1$ only",
        r"at $d \geq 3$: $E_d \to E_{d - (d-1)} = E_1$",
        r"At $d \leq 2$ this is the proved functorial construction.",
        r"At $d = 3$ it is the framed object-level assignment",
    )
    for fragment in required:
        assert fragment in text, fragment


def test_k3_mukai_bkm_fiber_scalars_stay_on_separate_lanes():
    text = squashed(LANDSCAPE)

    required = (
        r"Row \(\mathbf B\) has five coordinates and realizes the four-element set",
        r"\kappa_{\mathrm{cat}}(K3\times E)&=0",
        r"\kappa_{\mathrm{ch}}^{\mathrm{Heis}}(K3\times E)&=3",
        r"\kappa_{\mathrm{BKM}}(\Delta_5)=5",
        r"\kappa_{\mathrm{fiber}}(K3)&=24",
        r"2c_+(\mathrm{Mukai}(K3))=8",
        r"Its interpretation as $K^\kappa_{\mathcal B}=8$ has status \ClaimStatusConjectured under~$H_{\mathsf B}$",
        "It occupies the Hall--Borcherds/CoHA lane, structurally distinct from the standard RTT Yangian",
        "Scalar typing of rows adjacent to K3$\\times$E",
    )
    for fragment in required:
        assert fragment in text, fragment

    forbidden = (
        r"\kappa_{\mathrm{BKM}} = \kappa_{\mathrm{ch}} + \chi(\mathcal{O}_{\mathrm{fiber}})",
        "Mukai conductor value is a universal scalar value",
        "is a transfer principle for exceptional Yangian RTT presentations",
        r"K^\kappa_{\mathcal B}=2c_+(\mathrm{Mukai}(K3))=8",
        "order-$8$ monodromy",
        r"\Z/8",
    )
    for fragment in forbidden:
        assert fragment not in text, fragment


def test_included_vol_i_k3_hall_surfaces_are_conditional_targets():
    surfaces = {
        YANGIAN_FOUNDATIONS: (
            r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
            "only as a conditional recognition target",
            "finite Hall/CoHA source",
            "PBW/no-extra-relations theorem",
            "Mittag--Leffler exact inverse limit",
        ),
        YANGIAN_COMPUTATIONS: (
            r"\mathbf{H}_{\Delta_5}^{\mathrm{tgt}}",
            "occupies a fourth taxonomic slot only conditionally",
            "finite-window",
        ),
        YANGIAN_DK: (
            r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
            "is required to factor through",
            r"\mathcal V^{(n),\mathrm{tgt}}_{\mathrm{K3}}",
        ),
        GENUS_EXPANSIONS: (
            r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
            "conditional K3 target",
            "not a consequence of the bar--cobar counit",
        ),
        BAR_COMPLEX_TABLES: (
            r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
            "target Euler-characteristic cancellation",
            "not a proof that the actual Hall bar complex is acyclic",
        ),
        LATTICE_FOUNDATIONS: (
            "conditional recognition dictionary",
            r"\mathbf H_{\Delta_5}^{\mathrm{tgt}}",
            r"\;\leadsto\;",
        ),
        SYMMETRIC_ORBIFOLDS: (
            r"\mathbf{H}_{\Delta_5}^{\mathrm{tgt}}",
            "target genus-$2$ character",
            "PBW/no-extra-relations theorem",
        ),
        EXCEPTIONAL_YANGIAN: (
            "Affine and Hall companions",
            r"\ClaimStatusConditional",
            r"\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{K3\times E})",
            "The exceptional RTT problem is governed by a different arrow",
            "filtered bialgebra morphism into the displayed Drinfeld double",
        ),
    }

    for path, fragments in surfaces.items():
        text = squashed(path)
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {path}"


def test_included_vol_i_k3_hall_surfaces_do_not_promote_scalar_shadows():
    forbidden_by_path = {
        W_ALGEBRAS: (
            r"At the $K3 \times E$ BKM chiral algebra $\mathbf{H}_{\Delta_5}$",
            r"\Delta^{\mathbf H_{\Delta_5}} \;=\; \Delta^{\mathrm{SV}}\bigm|_{\hbar^2 = -1/8}",
            r"becomes an integrable $\mathbf H_{\Delta_5}$-module",
        ),
        YANGIAN_FOUNDATIONS: (
            r"\mathbf H_{\Delta_5} \;=\; \mathcal D_\hbar",
            "occupies a fourth taxonomic slot, distinct from the three classical",
        ),
        YANGIAN_COMPUTATIONS: (
            r"\mathbf{H}_{\Delta_5} \;=\; \mathcal{D}_\hbar",
            "occupies a fourth taxonomic slot: its underlying Miki generators",
        ),
        YANGIAN_DK: (
            r"\mathrm{GL}(\mathbf H_{\Delta_5}^{\otimes n})",
            r"\mathcal V^{(n)}_{\mathrm{K3}}(Z)",
        ),
        GENUS_EXPANSIONS: (
            r"The K3 chiral bialgebra $\mathbf H_{\Delta_5}$ supplies",
            r"B_{\mathrm{ch}}(\mathbf H_{\Delta_5})\bigm|_{\bar{\mathcal A}_2}",
        ),
        BAR_COMPLEX_TABLES: (
            "i.e.\\ the bar complex is acyclic at the vacuum sector",
            "table come from tensoring with each irreducible $\\mathbf H_{\\Delta_5}$-module",
        ),
        LATTICE_FOUNDATIONS: (
            r"\;=\; \mathbf H_{\Delta_5}",
            "The lattice-theoretic content of the universal functor",
        ),
        SYMMETRIC_ORBIFOLDS: (
            "uses the reciprocal Siegel form as the genus-$2$ character",
        ),
        EXCEPTIONAL_YANGIAN: (
            r"\mathbf H_{\Delta_5} =\mathcal D_\hbar",
            r"\xrightarrow{\;\SpCh_{\Sigma_2,C}\;}\mathbf H_{\Delta_5},",
        ),
    }

    for path, fragments in forbidden_by_path.items():
        text = squashed(path)
        for fragment in fragments:
            assert fragment not in text, f"retired fragment {fragment!r} still in {path}"
