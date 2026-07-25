from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

MASTER = ROOT / "chapters/connections/holographic_datum_master.tex"
SUPPLEMENT = ROOT / "chapters/connections/thqg_introduction_supplement.tex"
EN_KOSZUL = ROOT / "chapters/theory/en_koszul_duality.tex"
UNIVERSAL_CONDUCTOR = ROOT / "chapters/theory/universal_conductor_K_platonic.tex"
ARITHMETIC_SHADOWS = ROOT / "chapters/connections/arithmetic_shadows.tex"
CONCORDANCE = ROOT / "chapters/connections/concordance.tex"
FRONTIER_HOLOGRAPHY = ROOT / "chapters/connections/frontier_modular_holography_platonic.tex"
INTRODUCTION = ROOT / "chapters/theory/introduction.tex"
GENUS_COMPLETE = ROOT / "chapters/connections/genus_complete.tex"
HIGHER_GENUS_MODULAR_KOSZUL = ROOT / "chapters/theory/higher_genus_modular_koszul.tex"
THQG_SUPPLEMENT_BODY = ROOT / "chapters/connections/thqg_introduction_supplement_body.tex"
POINCARE_DUALITY_QUANTUM = ROOT / "chapters/theory/poincare_duality_quantum.tex"
BV_BRST = ROOT / "chapters/connections/bv_brst.tex"
FEYNMAN_DIAGRAMS = ROOT / "chapters/connections/feynman_diagrams.tex"
PREFACE = ROOT / "chapters/frame/preface.tex"
PREFACE_5_9 = ROOT / "chapters/frame/preface_sections5_9_draft.tex"
PREFACE_10_13 = ROOT / "chapters/frame/preface_sections10_13_draft.tex"
E1_PRIMACY = ROOT / "standalone/e1_primacy_ordered_bar.tex"
N3_E1_PRIMACY = ROOT / "standalone/N3_e1_primacy.tex"
ORDERED_CHIRAL_HOMOLOGY = ROOT / "standalone/ordered_chiral_homology.tex"
CY_TO_CHIRAL = ROOT / "standalone/cy_to_chiral_functor.tex"
CY_QG_HCS = ROOT / "standalone/cy_quantum_groups_6d_hcs.tex"
HOLOGRAPHIC_DATUM = ROOT / "standalone/holographic_datum.tex"
YANGIANS_DK = ROOT / "chapters/examples/yangians_drinfeld_kohno.tex"
DEFORMATION_QUANTIZATION = ROOT / "chapters/examples/deformation_quantization.tex"
INTRO_SURVEY = ROOT / "standalone/introduction_full_survey.tex"
PROGRAMME_SUMMARY = ROOT / "standalone/programme_summary.tex"
PROGRAMME_SUMMARY_2_4 = ROOT / "standalone/programme_summary_sections2_4.tex"
PROGRAMME_SUMMARY_5_8 = ROOT / "standalone/programme_summary_sections5_8.tex"
PROGRAMME_SUMMARY_9_14 = ROOT / "standalone/programme_summary_sections9_14.tex"
SURVEY_TRACK_A = ROOT / "standalone/survey_track_a_compressed.tex"
SURVEY_TRACK_B = ROOT / "standalone/survey_track_b_compressed.tex"

STANDALONES = (
    ROOT / "standalone/programme_summary_sections5_8.tex",
    ROOT / "standalone/programme_summary.tex",
    ROOT / "standalone/programme_summary_sections9_14.tex",
    ROOT / "standalone/w3_holographic_datum.tex",
    ROOT / "standalone/three_dimensional_quantum_gravity.tex",
    ROOT / "standalone/survey_modular_koszul_duality.tex",
    ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ROOT / "standalone/survey_track_b_compressed.tex",
)


def read(path: Path) -> str:
    return path.read_text()


def squashed(path: Path) -> str:
    return " ".join(read(path).split())


def assert_required(path: Path, fragments: tuple[str, ...]) -> None:
    text = squashed(path)
    for fragment in fragments:
        assert fragment in text, f"{fragment!r} missing from {path}"


def assert_forbidden(path: Path, fragments: tuple[str, ...]) -> None:
    text = squashed(path)
    for fragment in fragments:
        assert fragment not in text, f"retired fragment {fragment!r} still in {path}"


def test_live_holographic_master_keeps_typed_seven_entry_datum():
    assert_required(
        MASTER,
        (
            "and a physical bulk interpretation requires the open--closed comparison datum",
            "The seven-entry datum",
            r"\bigl(\cA,\;\cA^i,\;\cA^!,\;\cC,\;r_\cA(z),\;\Theta_\cA,\;\nabla^{\mathrm{hol}}\bigr)",
            r"$\cA^{\mathrm i}:=C_X(s^{-1}V,s^{-2}R)$",
            r"$q_\cA\colon\cA^{\mathrm i}\to\barBch_X(\cA)$",
            r"$\rho_\partial\colon \cC\to\cA$",
            r"Bare \emph{bulk} language is avoided below",
            "T18(i) is the chiral derived centre, while T18(iii) is the $3$d HT quantum field theory",
        ),
    )


def test_live_supplement_separates_bar_dual_closed_sector_and_lines():
    assert_required(
        SUPPLEMENT,
        (
            "Holographic datum: the seven-entry package",
            r"\bigl(\cA,\;\cA^i,\;\cA^!,\;\mathbf{C}_{\mathrm{ch}}(\cA),\; r(z),\;\Theta_\cA,\;\nabla^{\mathrm{hol}}\bigr)",
            r"The line category $\mathsf{Line}(\cA)=\cA^!\text{-}\mathsf{mod}$ is the module category attached to the third entry; it is not the fourth entry.",
            r"The bar, Verdier, and Hochschild entries are typed functorial constructions from~$\cA$; they are not projections of $\Theta_\cA$.",
            "Algebraic datum versus physical bulk",
        ),
    )


def test_en_koszul_keeps_sc_and_e3_on_the_right_objects():
    assert_required(
        EN_KOSZUL,
        (
            r"The symmetric bar $\barB^{\Sigma}(\cA)$ does \emph{not} carry a natural $\mathsf{E}_3$ structure.",
            r"it is not the tensor product $\Etwo \otimes \Eone$.",
            r"$\SCchtop \not\simeq \mathsf{E}_3$.",
            r"This is the correct $\mathsf{E}_3$ object: the derived center, not the symmetric bar.",
            "observable complex with the full $3$d bulk unless the OCA",
        ),
    )


def test_standalone_surfaces_use_seven_entry_open_closed_gates():
    required_by_path = {
        ROOT / "standalone/programme_summary_sections5_8.tex": (
            "The algebraic comparison data are a seven-entry tuple with typed maps",
            r"$\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)$",
            r"$q_\cA\colon\cA^{\mathrm i}\to B_X(\cA)$",
            r"$K_X(\cA)=\mathbb D_{\Ran}B_X(\cA)$",
            "a physical bulk requires the open--closed comparison map",
            "the hypothesis package comprises finite-type or completed duality, the line comparison, and the open--closed comparison map",
        ),
        ROOT / "standalone/programme_summary.tex": (
            "The algebraic comparison data are a seven-entry tuple with typed maps",
            r"$\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)$",
            r"$q_\cA\colon\cA^{\mathrm i}\to B_X(\cA)$",
            r"$K_X(\cA)=\mathbb D_{\Ran}B_X(\cA)$",
            "a physical bulk requires the open--closed comparison map",
            "Its hypothesis package comprises finite-type or completed duality, the line comparison, and the open--closed comparison map",
        ),
        ROOT / "standalone/programme_summary_sections9_14.tex": (
            "only after the typed open--closed and line-comparison maps are supplied",
            r"\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)",
            r"q_\cA\colon\cA^{\mathrm i}\to B_X(\cA)",
            r"K_X(\cA)=\mathbb D_{\Ran}B_X(\cA)",
            "line category is \\(\\cA^!\\)-modules only on the strict line-comparison surface",
            "a physical bulk requires the open--closed comparison map",
        ),
        ROOT / "standalone/w3_holographic_datum.tex": (
            "holographic modular Koszul datum} is the seven-entry package",
            r"$\cA^{\mathrm i}=C_X(s^{-1}V,s^{-2}R)$",
            r"$q_\cA\colon\cA^{\mathrm i}\to\barB_X^{\mathrm{ch}}(\cA)$",
            r"$K_X(\cA)=\mathbb D_{\Ran}\barB_X^{\mathrm{ch}}(\cA)$",
            "under the line comparison and open--closed comparison packages",
            "the closed-sector entry is the derived centre",
        ),
        ROOT / "standalone/three_dimensional_quantum_gravity.tex": (
            "seven-entry algebraic package",
            "physical bulk datum only after the open--closed comparison and the line-comparison maps are supplied",
            r"\mathrm{Vir}_c^{\mathrm i}=C_X(s^{-1}V_c,s^{-2}R_c)",
            r"K_X(\mathrm{Vir}_c)=\mathbb D_{\Ran}",
            r"\bar B_X^{\mathrm{ch}}(\mathrm{Vir}_c)",
            "algebraic closed-sector object",
        ),
        ROOT / "standalone/survey_modular_koszul_duality.tex": (
            "The seven-entry holographic datum",
            r"B_\partial^{\mathrm i}=C_X(s^{-1}V_\partial,s^{-2}R_\partial)",
            r"K_X(B_\partial)=\mathbb D_{\Ran}\barB_X(B_\partial)",
            "line operators are Koszul-dual modules only after the line-comparison map",
            "a physical bulk requires the open--closed comparison map",
        ),
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex": (
            "comparison surface into a seven-entry structure",
            "presentation coalgebra, full-bar Verdier algebra, strict Koszul dual, derived closed sector",
            "line-comparison surface attached to the strict dual",
            "physical holographic correspondence additionally requires the open--closed and line-comparison maps",
        ),
        ROOT / "standalone/survey_track_b_compressed.tex": (
            "algebraic comparison surface into a seven-entry object",
            "presentation coalgebra, full-bar Verdier algebra, strict Koszul dual, derived closed sector",
            "line-comparison surface; the derived centre occupies the closed-sector entry",
            "physical holographic correspondence additionally requires the open--closed and line-comparison maps",
        ),
    }

    for path, fragments in required_by_path.items():
        assert_required(path, fragments)


def test_boundary_bar_duality_summaries_do_not_identify_bar_with_bulk():
    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        (
            "completed boundary modules are equivalent to analytic comodules",
            "at curved genus the expected objects are analytic contramodules over the curved dual",
            "not an identification with the physical bulk factorization algebra",
            "requires the open--closed comparison datum",
        ),
    )
    for path in (
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        ROOT / "standalone/survey_track_b_compressed.tex",
    ):
        assert_required(
            path,
            (
                "completed boundary modules are expected to be analytic comodules",
                "curved genus uses analytic contramodules over the curved dual",
                "not a physical-bulk identification without the open--closed comparison datum",
            ),
        )


def test_polyakov_and_string_criticality_need_brst_data():
    required_by_path = {
        ROOT / "standalone/survey_modular_koszul_duality.tex": (
            "anomaly-accounting dictionary",
            "determinant-line, ghost, and BRST data",
            r"BRST condition $c_{\mathrm{matter}}+c_{\mathrm{ghost}}=0$",
            "external BRST ghost resolution",
        ),
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex": (
            "anomaly-accounting dictionary",
            "BRST current, and nilpotence equation",
            r"BRST cancellation \(c_{\mathrm{matter}}+c_{\mathrm{ghost}}=0\)",
            "external BRST ghost resolution",
        ),
        INTRO_SURVEY: (
            r"after choosing the \(bc\)-ghost complex",
            "Scalar Koszul duality gives the",
            "string criticality additionally requires",
            "The full Polyakov measure additionally contains",
        ),
        PREFACE_5_9: (
            "anomaly-accounting dictionary",
            "A string-critical claim requires a determinant line",
            r"BRST anomaly-cancellation equation",
            "KSDual fixed-point condition belongs to the separate Verdier--Koszul lane",
            "external BRST ghost resolution",
        ),
    }

    for path, fragments in required_by_path.items():
        assert_required(path, fragments)

    forbidden = (
        "proves Polyakov's worldsheet functional-integral",
        "follows from Koszul duality at the scalar level alone",
        "is the bar-complex computation of Polyakov's path integral",
        "At genus~$1$ the correspondence is controlled by~$\\kappa$ alone",
    )
    for path in (
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        INTRO_SURVEY,
        PREFACE_5_9,
    ):
        assert_forbidden(path, forbidden)


def test_arithmetic_shadows_keeps_derived_centre_closed_sector_typed():
    assert_required(
        ARITHMETIC_SHADOWS,
        (
            "inside the derived-centre closed-sector data on that comparison surface",
            "it is not an equality with the scalar shadow invariants",
        ),
    )
    assert_forbidden(
        ARITHMETIC_SHADOWS,
        ("inside derived-centre bulk data",),
    )


def test_bar_construction_is_typed_as_twisting_not_bulk_forgetfulness():
    assert_required(
        PREFACE,
        (
            r"The bar is the coalgebraic resolution at level \(2\)",
            r"The derived centre is the endomorphism object at level \(3\)",
            r"\Theta_{\cA}:=D_{\cA}-d_0",
        ),
    )

    for path in (
        PREFACE_10_13,
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        ROOT / "standalone/survey_track_b_compressed.tex",
    ):
        text = squashed(path)
        assert "twisting" in text
        assert "derived centre" in text or "derived center" in text
        assert "open--closed comparison" in text or "requires OCA" in text

    for path in (
        PREFACE,
        PREFACE_10_13,
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        ROOT / "standalone/survey_track_b_compressed.tex",
    ):
        assert_forbidden(path, (r"\barB$ forgets the bulk",))


def test_standalone_hochschild_surfaces_are_closed_sector_not_bulk():
    assert_required(
        E1_PRIMACY,
        (
            "Z^der_ch(A) = derived chiral center = Hochschild cochains",
            "algebraic closed-sector actor; physical bulk requires OCA data",
        ),
    )
    assert_required(
        ORDERED_CHIRAL_HOMOLOGY,
        (
            r"Closed-sector $\Etwo$ versus topological $\Ethree$",
            r"The algebraic closed-sector $\Etwo$",
            "a physical bulk interpretation requires the open--closed comparison datum",
        ),
    )
    for path in (
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    ):
        assert_required(
            path,
            (
                "closed-sector",
                "derived centre",
                "open--closed comparison",
            ),
        )
    assert_required(
        SURVEY_TRACK_A,
        (
            "derived center pair",
            "universal closed sector",
            "open--closed comparison map",
        ),
    )
    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        (
            "universal algebraic closed-sector actor",
            "closed-sector operators acting on the boundary",
            "physical bulk operators require the open--closed comparison",
        ),
    )
    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        (
            "the algebraic closed sector acting on the boundary",
            "physical realisation as the bulk algebra of a 3d holomorphic--topological gauge theory requires the open--closed/HT comparison datum",
            r"closed-sector descriptor $\cZ^{\der}_{\ch}(\cH_k)$",
            "The physical bulk comparison is extra OCA data",
        ),
        )


def test_loop_connes_and_operator_action_are_closed_sector_not_bulk_slogans():
    for path in (
        CONCORDANCE,
        FRONTIER_HOLOGRAPHY,
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        SURVEY_TRACK_B,
        INTRO_SURVEY,
    ):
        assert_required(
            path,
            (
                "genus creation in the cochain-level closed sector",
                "open Connes trace mechanism",
            ),
        )

    for path in (PROGRAMME_SUMMARY, PROGRAMME_SUMMARY_5_8):
        assert_required(
            path,
            (
                "closed-sector operators act on the boundary",
                "physical-bulk action requires an open--closed comparison",
                "Closed-sector operators restrict to boundary operators through the Swiss-cheese action",
                "physical-bulk restriction exists only after OCA data",
            ),
        )

    assert_required(
        INTRO_SURVEY,
        (
            "classifies \\emph{closed-sector operators} acting on the boundary",
            "A physical bulk action requires an open--closed comparison datum",
            "closed-sector module contributions",
        ),
    )
    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        (
            "classifying cochain-level closed-sector operators",
            "Physical bulk operators require the open--closed comparison datum",
        ),
    )


def test_cy_functor_and_programme_summaries_type_closed_sector_not_bulk():
    assert_required(
        CY_TO_CHIRAL,
        (
            "is the closed-sector--boundary algebraic system",
            "It is a physical boundary--bulk system only after that comparison",
            "the chiral Hochschild cochain complex encoding the algebraic closed-sector slot",
            "a physical bulk interpretation requires the open--closed comparison datum",
        ),
    )
    assert_forbidden(
        CY_TO_CHIRAL,
        (
            "is the boundary--bulk system",
            "encoding the bulk sector",
        ),
    )

    assert_required(
        N3_E1_PRIMACY,
        (
            "this is the cochain-level closed-sector actor",
            "closed-sector entry",
            "A physical bulk interpretation requires an open--closed comparison datum",
        ),
    )
    assert_forbidden(
        N3_E1_PRIMACY,
        (
            "plays the role of the bulk",
            "closed (bulk) sector",
        ),
    )

    for path in (PROGRAMME_SUMMARY, PROGRAMME_SUMMARY_2_4):
        assert_required(
            path,
            (
                "is the universal closed-sector algebra",
                "the cochain-level operator algebra acting on the boundary algebra",
                "A physical bulk interpretation requires the open--closed comparison datum",
            ),
        )
        assert_forbidden(
            path,
            (
                "is the universal bulk algebra",
                "the algebra of operators in the interior",
            ),
        )


def test_closed_sector_actions_are_not_declared_physical_bulk_without_oca():
    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        (
            "maps the algebraic closed-sector actor to this $E_2$-algebra",
            "an algebraic closed-sector equivalence at this comparison surface",
            "physical-bulk reading requires the open--closed comparison datum",
        ),
    )
    assert_forbidden(
        ROOT / "standalone/survey_modular_koszul_duality.tex",
        ("maps the holomorphic bulk algebra to this $E_2$-algebra",),
    )

    assert_required(
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        (
            "whose OCA image is the physical bulk sector of a 3d gauge theory",
        ),
    )
    assert_forbidden(
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        ("image is the bulk sector of a 3d gauge theory",),
    )

    assert_required(
        CY_QG_HCS,
        (
            r"The $\Ethree$-operad acts on the derived center $\Zder(A_\cC)$",
            r"the $\Ethree$-action is on the algebraic closed-sector actor $\Zder(A_\cC)$",
            "physical-bulk reading requires the OCA/HT comparison datum",
        ),
    )
    assert_forbidden(
        CY_QG_HCS,
        (
            r"$\Ethree$-action is on the bulk algebra",
            "bulk algebra (the derived center)",
        ),
    )


def test_derived_centres_are_closed_sector_objects_not_bulk_algebras():
    for path in (
        ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
        SURVEY_TRACK_B,
    ):
        assert_required(
            path,
            (
                "Closed sector $=$ derived centre",
                "maps the algebraic closed-sector actor to this $E_2$-algebra",
                "identifying a holomorphic physical bulk with it requires the open--closed comparison datum",
            ),
        )
        assert_forbidden(
            path,
            (
                "Bulk $=$ derived centre",
                "identifies the holomorphic bulk with this $E_2$-algebra",
            ),
        )

    assert_required(
        UNIVERSAL_CONDUCTOR,
        (
            r"$\DerZ(\cA)$ is the algebraic closed-sector Hochschild cochain algebra",
        ),
    )
    assert_forbidden(
        UNIVERSAL_CONDUCTOR,
        (r"$\DerZ(\cA)$ is a bulk algebra",),
    )

    assert_required(
        EN_KOSZUL,
        ("deformation functors of the algebraic closed-sector object",),
    )
    assert_forbidden(
        EN_KOSZUL,
        ("deformation functors of the bulk algebra",),
    )

    assert_required(
        YANGIANS_DK,
        (
            "back to the algebraic closed-sector object",
            "the algebraic closed-sector object is recoverable on the derived-center side",
            "recovery of the algebraic closed-sector object from the boundary algebra",
        ),
    )
    assert_forbidden(
        YANGIANS_DK,
        (
            "back to the bulk algebra",
            "the bulk algebra is recoverable on the derived-center side",
            "recovery of the bulk algebra from the boundary algebra",
        ),
    )

    assert_required(
        PREFACE,
        (
            "constructs the derived centre",
            "The holomorphic-topological bulk comparison is carried by an explicit open--closed functor",
        ),
    )
    assert_forbidden(
        PREFACE,
        ("the derived centre is the bulk algebra of the corresponding 3d",),
    )

    assert_required(
        HOLOGRAPHIC_DATUM,
        (
            "algebraic closed-sector--boundary--line triangle is recovered",
            "physical BBL reading requires the open--closed comparison datum",
            "closed-sector vertex is the chiral derived centre",
            r"\cA_{\mathrm{cl}}",
            "physical bulk interpretation requires the open--closed comparison datum",
            "closed-sector-to-lines edge",
            "with the algebraic closed sector acting on the boundary",
            "physical bulk action requires the open--closed comparison datum",
        ),
    )
    assert_forbidden(
        HOLOGRAPHIC_DATUM,
        (
            r"\emph{Bulk}: the chiral derived centre",
            r"\cA_{\mathrm{bulk}}",
            "bulk--boundary--line triangle is recovered",
            "boundary-to-bulk trace",
            "bulk-to-lines edge",
            "closed-string derived centre",
            "eq:bulk",
            "with bulk acting on boundary",
        ),
    )


def test_bbl_outline_surfaces_use_closed_sector_triangle_language():
    assert_required(
        INTRODUCTION,
        (
            "closed-sector/boundary/line triangle with physical BBL under OCA",
            "closed-sector/boundary/line algebraic triangle that propagates",
            "physical BBL language under OCA",
        ),
    )
    assert_forbidden(
        INTRODUCTION,
        ("bulk/boundary/line triangle",),
    )

    assert_required(
        PROGRAMME_SUMMARY_9_14,
        (
            "package the closed-sector/boundary/line algebraic triangle",
            "physical BBL language only after OCA",
        ),
    )
    assert_forbidden(
        PROGRAMME_SUMMARY_9_14,
        ("package the bulk/boundary/line triangle",),
    )

    assert_required(
        THQG_SUPPLEMENT_BODY,
        (
            "closed-sector/boundary/line algebraic triangle in~$3$d",
            "physical BBL reading requires the open--closed comparison datum",
        ),
    )
    assert_forbidden(
        THQG_SUPPLEMENT_BODY,
        ("bulk/boundary/line triangle in~$3$d",),
    )

    assert_required(
        BV_BRST,
        (
            "is the chiral derived centre, the closed-sector object",
            "relative BRST locus",
            r"filtered comparison map~$\Phi$",
            r"\bigl(Z^{\mathrm{der}}_{\mathrm{ch}}(\cA),\,\cA\bigr)",
        ),
    )
    assert_forbidden(
        BV_BRST,
        (r"$\mathsf{SC}^{\mathrm{ch,top}}$ HT bulk-boundary-line triangle",),
    )

    assert_required(
        FEYNMAN_DIAGRAMS,
        (
            r"\emph{Swiss-cheese pair} $(Z^{\mathrm{der}}_{\mathrm{ch}}(A_b),\, A_b)$",
            "the closed colour",
            "acts on the open colour",
            "Swiss-cheese realisation as theorem",
        ),
    )
    assert_forbidden(
        FEYNMAN_DIAGRAMS,
        ("HT bulk-boundary-line triangle",),
    )

    assert_required(
        GENUS_COMPLETE,
        (
            r"\index{closed sector!from boundary}",
            "The complete packaging of these ingredients (algebraic closed-sector object",
        ),
    )
    assert_forbidden(
        GENUS_COMPLETE,
        (
            r"\index{bulk-boundary correspondence!derived center}",
            "The complete packaging of these ingredients (bulk algebra",
        ),
    )

    assert_required(
        HIGHER_GENUS_MODULAR_KOSZUL,
        (r"\index{derived centre!open--closed comparison}",),
    )
    assert_forbidden(
        HIGHER_GENUS_MODULAR_KOSZUL,
        (r"\index{derived centre!bulk reconstruction}",),
    )

    assert_required(
        SUPPLEMENT,
        (
            "The algebraic closed-sector object",
            "A physical bulk algebra is supplied only by the additional open--closed comparison datum",
        ),
    )
    assert_forbidden(
        SUPPLEMENT,
        ("The bulk algebra $\\mathbf{C}_{\\mathrm{ch}}",),
    )


def test_landau_ginzburg_bulk_language_is_open_closed_gated():
    assert_required(
        DEFORMATION_QUANTIZATION,
        (
            "algebraic closed-sector algebra of the Landau--Ginzburg model",
            "physical-bulk reading requires the Landau--Ginzburg open/closed comparison",
            "closed-sector identification is a direct consequence of the Hochschild--Kostant--Rosenberg theorem",
        ),
    )
    assert_forbidden(
        DEFORMATION_QUANTIZATION,
        (
            "bulk algebra of the Landau--Ginzburg model is identified with",
        ),
    )


def test_bulk_operator_labels_are_closed_sector_until_oca():
    for path in (PROGRAMME_SUMMARY, PROGRAMME_SUMMARY_5_8):
        assert_required(
            path,
            ("Closed-sector operators & Boundary operators",),
        )
        assert_forbidden(
            path,
            ("Bulk operators & Boundary operators",),
        )

    assert_required(
        POINCARE_DUALITY_QUANTUM,
        (
            "closed-sector action",
            "Intrinsic closed-sector operators",
            "boundary-to-intrinsic-closed-sector map",
        ),
    )
    assert_forbidden(
        POINCARE_DUALITY_QUANTUM,
        (
            "bulk action",
            "Intrinsic bulk operators",
            "boundary-to-intrinsic-bulk map",
        ),
    )


def test_retired_physics_bridge_slogans_do_not_return():
    forbidden = (
        "complete data of a holographic system is a sextuple",
        "six-component holographic",
        "six-component structure that records the boundary",
        "full holographic correspondence into a six-component",
        "complete holographic correspondence into a single MC problem",
        "is the complete algebraic encoding",
        "entire holographic system is determined by the chiral algebra on the boundary",
        "derived chiral centre IS the",
        "derived chiral center IS the",
        "derived chiral centre is the bulk algebra",
        "derived chiral center is the bulk algebra",
        "topological bar of the bulk factorization algebra",
        r"B^{\mathrm{top}}(\mathrm{Fact}^{\mathrm{bulk}}_T)",
        "Hochschild cochains = bulk",
        "algebraic bulk $\\Etwo$",
        "bulk chiral homology complex of Volume~II",
        "bulk-boundary-line triangle",
        r"\cA_{\mathrm{bulk}}",
        "universal algebra of bulk operators",
        "classifies bulk operators",
        "bulk acting on boundary",
        r"bulk $= \cH_k$",
        "loops in the bulk are traces on the boundary",
        "classifies bulk operators",
        "bulk operators act on the boundary",
        "Bulk operators restrict to boundary operators",
        "bulk module contributions",
        "derived center classifying bulk operators",
        "derived centre classifying bulk operators",
    )

    for path in (
        *STANDALONES,
        MASTER,
        SUPPLEMENT,
        EN_KOSZUL,
        E1_PRIMACY,
        ORDERED_CHIRAL_HOMOLOGY,
        SURVEY_TRACK_A,
        SURVEY_TRACK_B,
        INTRO_SURVEY,
        PROGRAMME_SUMMARY,
        PROGRAMME_SUMMARY_5_8,
        CONCORDANCE,
        FRONTIER_HOLOGRAPHY,
    ):
        assert_forbidden(path, forbidden)
