"""Semantic guards for collision kernels, coinvariants, traces, and CYBE images."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

SOURCES = {
    "core": ROOT / "chapters/theory/e1_modular_koszul.tex",
    "higher_genus": ROOT / "chapters/theory/higher_genus_modular_koszul.tex",
    "y": ROOT / "chapters/examples/y_algebras.tex",
    "part_iii": ROOT / "chapters/frame/part_iii_platonic_introduction.tex",
    "heisenberg": ROOT / "chapters/frame/heisenberg_frame.tex",
    "frontier": ROOT / "chapters/connections/frontier_modular_holography_platonic.tex",
    "ordered": ROOT / "appendices/ordered_associative_chiral_kd.tex",
    "genus_one": ROOT / "chapters/connections/genus1_seven_faces.tex",
    "seven_faces": ROOT / "chapters/connections/holographic_datum_master.tex",
    "nonlinear_shadows": ROOT / "appendices/nonlinear_modular_shadows.tex",
    "notation_appendix": ROOT / "appendices/notation_index.tex",
    "preface_2_4": ROOT / "chapters/frame/preface_sections2_4_draft.tex",
    "preface_5_9": ROOT / "chapters/frame/preface_sections5_9_draft.tex",
    "standalone_genus_one": ROOT / "standalone/genus1_seven_faces.tex",
    "cy_to_chiral": ROOT / "standalone/cy_to_chiral_functor.tex",
    "programme": ROOT / "standalone/programme_summary.tex",
    "programme_2_4": ROOT / "standalone/programme_summary_sections2_4.tex",
    "standalone_holographic": ROOT / "standalone/holographic_datum.tex",
    "virasoro_kernel": ROOT / "standalone/virasoro_r_matrix.tex",
    "classification": ROOT / "standalone/classification_trichotomy.tex",
    "e1_primacy": ROOT / "standalone/e1_primacy_ordered_bar.tex",
    "survey_track_a": ROOT / "standalone/survey_track_a_compressed.tex",
    "survey_track_b": ROOT / "standalone/survey_track_b_compressed.tex",
    "en_circle": ROOT / "standalone/en_chiral_operadic_circle.tex",
    "notation": ROOT / "standalone/notation_index.tex",
    "survey": ROOT / "standalone/survey_modular_koszul_duality_v2.tex",
    "cy_quantum_groups": ROOT / "standalone/cy_quantum_groups_6d_hcs.tex",
    "shadow_towers": ROOT / "standalone/shadow_towers.tex",
    "shadow_towers_v3": ROOT / "standalone/shadow_towers_v3.tex",
    "ordered_homology": ROOT / "standalone/ordered_chiral_homology.tex",
    "drinfeld_kohno": ROOT / "standalone/drinfeld_kohno_bridge.tex",
    "chiral_chern_weil": ROOT / "standalone/chiral_chern_weil.tex",
    "introduction_full": ROOT / "standalone/introduction_full_survey.tex",
    "five_theorems": ROOT / "standalone/five_theorems_modular_koszul.tex",
    "higher_genus_foundations": ROOT / "chapters/theory/higher_genus_foundations.tex",
    "yangian_foundations": ROOT / "chapters/examples/yangians_foundations.tex",
    "logarithmic_w": ROOT / "chapters/examples/logarithmic_w_algebras.tex",
    "bar_construction": ROOT / "chapters/theory/bar_construction.tex",
    "shadow_quadrichotomy": ROOT / "chapters/theory/shadow_tower_quadrichotomy_platonic.tex",
    "derived_langlands": ROOT / "chapters/theory/derived_langlands.tex",
    "concordance": ROOT / "chapters/connections/concordance.tex",
    "programme_5_8": ROOT / "standalone/programme_summary_sections5_8.tex",
    "programme_9_14": ROOT / "standalone/programme_summary_sections9_14.tex",
    "garland": ROOT / "standalone/garland_lepowsky.tex",
    "gaudin": ROOT / "standalone/gaudin_from_collision.tex",
    "thqg_open_closed": ROOT / "chapters/connections/thqg_open_closed_realization.tex",
    "thqg_supplement": ROOT / "chapters/connections/thqg_introduction_supplement.tex",
    "thqg_supplement_body": ROOT / "chapters/connections/thqg_introduction_supplement_body.tex",
    "w3_chapter": ROOT / "chapters/examples/w3_holographic_datum.tex",
    "w3_standalone": ROOT / "standalone/w3_holographic_datum.tex",
    "multi_weight": ROOT / "standalone/multi_weight_cross_channel.tex",
    "n3_e1_primacy": ROOT / "standalone/N3_e1_primacy.tex",
    "three_dimensional_qg": ROOT / "standalone/three_dimensional_quantum_gravity.tex",
    "guide": ROOT / "chapters/frame/guide_to_main_results.tex",
    "part_iv": ROOT / "chapters/frame/part_iv_platonic_introduction.tex",
    "ordered_chapter": ROOT / "chapters/theory/ordered_associative_chiral_kd.tex",
    "standalone_seven_faces": ROOT / "standalone/seven_faces.tex",
}


def _text(path: Path) -> str:
    return " ".join(path.read_text().split())


def test_core_types_operator_coinvariant_before_scalar_trace():
    text = _text(SOURCES["core"])
    required = [
        r"q_n\colon \End_\cA(n)\longrightarrow \End_\cA(n)_{h\Sigma_n}",
        r"\tau_{\cA,n}^{\mathrm{res}}\colon \End_\cA(n)_{h\Sigma_n}\longrightarrow\C",
        r"\kappa_{\mathrm{dp}}(\cA) :=\tau_\cA\!\left(q_2(K_\cA^{\mathrm{coll}})\right)",
        r"S_n(\cA) :=\tau_{\cA,n}^{\mathrm{res}}\!\left(",
        r"H_{\mathrm{CYBE}}^{\mathrm{rep}}(\cA)",
    ]
    for fragment in required:
        assert fragment in text


def test_repaired_surfaces_preserve_the_three_step_chain():
    requirements = {
        "higher_genus": [
            r"K_\cA^{\mathrm{coll}}",
            r"q_2(K_\cA^{\mathrm{coll}})\in\End_\cA(2)_{h\Sigma_2}",
            r"\kappa(\cA) :=\tau_{\cA,2}^{\mathrm{res}}q_2(K_\cA^{\mathrm{coll}})",
            r"S_r(\cA) \;:=\; \operatorname{Sh}_r(\cA)",
        ],
        "y": [
            r"K_Y^{\mathrm{coll}}(z)",
            r"q_2(K_Y^{\mathrm{coll}})",
            r"\tau_{Y,2}^{\mathrm{res}}q_2(K_Y^{\mathrm{coll}})=\Psi",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}(Y;W)",
        ],
        "part_iii": [
            r"K_\cA^{\mathrm{coll}}(z)",
            r"q_2(K_\cA^{\mathrm{coll}})",
            r"\tau_{\cA,2}^{\mathrm{res}}",
            r"r_\cA(z)=\rho_\cA(K_\cA^{\mathrm{coll}}(z))",
        ],
        "heisenberg": [
            r"K_{\mathcal H}^{\mathrm{coll}}(z)=k\Omega_{\mathcal H}/z",
            r"q_2(K_A^{\mathrm{coll}}(z))",
            r"\tau_{A,2}^{\mathrm{res}}",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}",
        ],
        "frontier": [
            r"K_\cA^{\mathrm{coll}}(z)",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}(\cA;W)",
            r"H_Y(\cA;W)",
            r"(\pi_\cA)_2^{\mathrm{coll}}",
        ],
        "ordered": [
            r"K_A^{\mathrm{coll}}(z)",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}(A;W)",
            r"r_A(z):=\rho_A(K_A^{\mathrm{coll}}(z))",
        ],
        "genus_one": [
            r"K_\cA^{(1),\mathrm{coll}}(z, \tau)",
            r"\bigl(\pi_\cA^{(1)}\bigr)_{2}^{\mathrm{coll}}(z,\tau)",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}",
            r"\rho_{\mathrm{KZ}}\!\left(",
        ],
        "seven_faces": [
            r"K_\cA^{\mathrm{coll}}(z)",
            r"\kappa(\cA)=\tau_{\cA,2}^{\mathrm{res}} q_2(K_\cA^{\mathrm{coll}})",
            r"S_r(\cA)=\tau_{\cA,r}^{\mathrm{res}} q_r",
            r"H_{\mathrm{CYBE}}^{\mathrm{rep}}",
        ],
    }
    for name, fragments in requirements.items():
        text = _text(SOURCES[name])
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {SOURCES[name]}"


def test_scalar_collapse_slogans_do_not_return_on_repaired_surfaces():
    forbidden = [
        r"whose coinvariant is $\kappa",
        r"\mathrm{av}(r(z)) = \kappa",
        r"the classical r-matrix r(z) = \Res^{\mathrm{coll}}_{0,2}",
        r"collision residue of~$\Theta_\cA$ canonically produces a dg-shifted Yangian",
    ]
    for path in SOURCES.values():
        text = _text(path)
        for fragment in forbidden:
            assert fragment not in text, f"retired fragment {fragment!r} in {path}"


def test_repaired_surfaces_have_balanced_tex_environments():
    token = re.compile(r"\\(begin|end)\{([^}]+)\}")
    for path in SOURCES.values():
        stack: list[str] = []
        for raw_line in path.read_text().splitlines():
            line = raw_line.split("%", 1)[0]
            for kind, environment in token.findall(line):
                if kind == "begin":
                    stack.append(environment)
                else:
                    assert stack, f"unmatched end{{{environment}}} in {path}"
                    opened = stack.pop()
                    assert opened == environment, (
                        f"begin{{{opened}}} closed by end{{{environment}}} in {path}"
                    )
        assert not stack, f"unclosed environments {stack!r} in {path}"
