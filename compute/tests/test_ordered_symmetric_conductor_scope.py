"""Guardrails for ordered-to-symmetric conductor descent language."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]

CANONICAL = ROOT / "chapters/theory/universal_conductor_K_platonic.tex"
E1_PRIMACY = ROOT / "standalone" / "e1_primacy_ordered_bar.tex"
ORDERED_CHIRAL_HOMOLOGY = ROOT / "standalone" / "ordered_chiral_homology.tex"
INTRO_FULL_SURVEY = ROOT / "standalone" / "introduction_full_survey.tex"
INTRO_BACKUP = ROOT / "chapters" / "theory" / "introduction.tex.bak"

FIRST_READER_SURFACES = [
    ROOT / "chapters/frame/guide_to_main_results.tex",
    ROOT / "chapters/frame/preface.tex",
    ROOT / "chapters/theory/introduction.tex",
    ROOT / "chapters/theory/bar_cobar_adjunction_curved.tex",
    ROOT / "chapters/theory/bar_construction.tex",
    ROOT / "standalone/introduction_full_survey.tex",
    ROOT / "standalone/programme_summary.tex",
    ROOT / "standalone/programme_summary_section1.tex",
    ROOT / "standalone/survey_modular_koszul_duality.tex",
    ROOT / "standalone/e1_primacy_ordered_bar.tex",
    ROOT / "standalone/five_theorems_modular_koszul.tex",
    ROOT / "standalone/koszulness_fourteen_characterizations.tex",
]


def visible(path: Path) -> str:
    lines = []
    for line in path.read_text().splitlines():
        if line.lstrip().startswith("%"):
            continue
        lines.append(line)
    return "\n".join(lines)


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def assert_anchor(text: str, anchor: str) -> None:
    assert compact(anchor) in compact(text), anchor


def test_universal_conductor_names_the_a8_descent_package():
    tex = visible(CANONICAL)
    required = (
        "\\mathbf H_{\\mathrm{uc}}(\\cA)",
        "complete separated conilpotent",
        "quantum Yang--Baxter equation",
        "strong unitarity\n$R^{21}(-z)R^{12}(z)=\\id$",
        "local system $L_R$",
        "regular-singular\nnearby-cycle extension",
        "compatible with the chiral\ncollision products",
        "L_R$-twisted derived completed coinvariants",
        "ordered information-loss conductor",
        "\\operatorname{Fib}\\!",
        "Theorem~\\ref{thm:uc-r-twisted-dg-lie-descent}",
        "Corollary~\\ref{cor:eight-cor-R-descent}",
        "Lemma~\\ref{lem:R-twisted-completed-coinvariants}",
    )
    for anchor in required:
        assert_anchor(tex, anchor)


def test_universal_conductor_proves_finite_window_r_twisted_dg_lie_descent():
    tex = visible(CANONICAL)
    required = (
        "Finite-window $R$-twisted descent for the differential\nand bracket",
        "\\label{thm:uc-r-twisted-dg-lie-descent}",
        "shuffle-compatible coefficient multiplication",
        "R_n\\otimes_{\\mathbb Q[\\Sigma_n]} C_n/F^N C_n",
        "averaging commutes\nwith \\(d_B\\) only under the stated equivariance",
        "the bracket descends to\na continuous chain map",
        "The coefficient map~\\(\\mu_{m,n}\\) carries the natural tensor-product\ntwist",
        "Reynolds representative",
        "same formula on a broader window is a continuous linear projection\nto a shadow",
    )
    for anchor in required:
        assert_anchor(tex, anchor)


def test_universal_conductor_identifies_degree_two_rmatrix_kernel():
    tex = visible(CANONICAL)
    required = (
        "Degree-two conductor kernel and ordered\n\\texorpdfstring{$r$}{r}-matrix data",
        "\\label{thm:uc-degree-two-rmatrix-kernel}",
        "\\ker(K_{\\cA,2}^{\\mathrm{ch}})\n=\n\\ker(\\mathrm{Re}_2)",
        "\\operatorname{im}\\!\\left(\\frac{1-s}{2}\\right)",
        "ordered\ntwo-particle residue coefficients \\(r_{\\cA,\\alpha}(z)\\)",
        "r_{\\cA,\\alpha}^{-}(z):=\n\\frac12\\bigl(r_{\\cA,\\alpha}(z)-s\\cdot r_{\\cA,\\alpha}(z)\\bigr)",
        "kernel is\nexactly the ordered \\(r\\)-matrix data killed by symmetric averaging",
        "\\mathcal B_n(\\cA;\\mathcal W)",
        "\\beta^-:=(1-\\mathrm{Re}_n)\\beta\\in\\ker(K_{\\cA,n}^{\\mathrm{ch}})",
        "generation hypothesis supplies exhaustion",
    )
    for anchor in required:
        assert_anchor(tex, anchor)


def test_first_reader_surfaces_do_not_present_general_averaging_as_naive_projection():
    combined = "\n".join(visible(path) for path in FIRST_READER_SURFACES)
    compact_combined = compact(combined)
    retired = (
        "kills the $R$-matrix",
        "discards the $R$-matrix",
        "none of which survive the passage to\n$\\Sigma_n$-coinvariants",
        "is the $\\Sigma_n$-coinvariant projection: lossy",
        "which is the $\\Sigma_n$-coinvariant projection at each degree.\nThis map is a quasi-isomorphism",
    )
    for fragment in retired:
        if compact(fragment) in compact_combined:
            raise AssertionError(f"retired averaging/conductor phrase remains: {fragment!r}")


def test_e1_primacy_averaging_surjectivity_is_conditional_finite_window():
    tex = visible(E1_PRIMACY)
    required = (
        "is a chosen finite-window chain section",
        "without that window and homotopy the displayed average is merely a\nlinear projection",
        "\\ClaimStatusConditional",
        "Type signature: \\textup{(}Open quadrant, ordered-to-symmetric\nconvolution presentation",
        "finite-window chain section of the ribbon-forgetting\ncomparison",
        "coefficient-multiplication\npackage of the universal conductor",
        "section/homotopy datum, coefficient multiplication, and kernel\ncondition",
        "Surjectivity is a finite-window statement",
        "finite-window\ncriterion of Theorem~\\ref{thm:uc-r-twisted-dg-lie-descent}",
    )
    for anchor in required:
        assert_anchor(tex, anchor)

    retired = (
        "is any section of the ribbon-forgetting quotient",
        "Surjectivity: every $\\Sigma_n$-invariant homomorphism",
        "Under the fixed strong-unitary \\(R\\)-twisted descent datum, the\naveraging map",
        "Without this descent\ndatum there is only the ordered dg Lie algebra",
    )
    for fragment in retired:
        assert compact(fragment) not in compact(tex)


def test_ordered_chiral_homology_descent_uses_finite_direct_image_not_coarse_equivalence():
    tex = visible(ORDERED_CHIRAL_HOMOLOGY)
    required = (
        "\\providecommand{\\ClaimStatusConditional}{}",
        "\\label{prop:sym-descent}",
        "\\ClaimStatusConditional",
        "finite direct image along \\(X^n\\to X^{(n)}\\)",
        "regular extension across diagonals",
        "category of $\\cD$-modules on $[X^n / \\Sigma_n]$",
        "not an equivalence between $\\cD$-modules on the quotient stack\nand arbitrary $\\cD$-modules on the coarse symmetric power",
        "Stabilizers along diagonals retain equivariant data",
        "\\pi_{n,+}\\cF_n^{\\mathrm{ord}}",
        "\\operatorname{Re}_{\\Sigma_n}",
        "The de~Rham functor commutes with finite direct image",
        "derived coinvariants agree with ordinary coinvariants",
    )
    for anchor in required:
        assert_anchor(tex, anchor)

    retired = (
        "the quotient stack\n$[X^n / \\Sigma_n]$ and the coarse moduli space\n$X^{(n)} = X^n / \\Sigma_n$ have equivalent $\\cD$-module\ncategories",
        "ramified along the diagonals, but equivariant descent\nis not affected by ramification in characteristic zero",
        "finite-dimensional symmetric-group action",
    )
    for fragment in retired:
        assert compact(fragment) not in compact(tex)


def test_lossy_descent_is_kernel_criterion_not_universal_noninjectivity():
    tex = visible(ORDERED_CHIRAL_HOMOLOGY)
    intro = visible(INTRO_FULL_SURVEY)
    intro_backup = visible(INTRO_BACKUP)

    required = (
        "\\label{prop:lossy-descent}",
        "\\ClaimStatusProvedHere",
        "completed \\(\\Sigma_n\\)- or \\(R\\)-twisted coinvariant descent",
        "is the completed coinvariant quotient and is therefore surjective",
        "\\ker(\\av_n)\n=\n\\overline{",
        "\\left\\langle \\sigma\\cdot c-c\\;:\\;",
        "relations \\(r\\sigma\\otimes c-r\\otimes\\sigma c\\)",
        "non-injective precisely when the ordered\narity-\\(n\\) carrier has a nonzero nontrivial",
        "When that\ncomponent vanishes, the descent is lossless in arity",
        "for scalar abelian windows this anti-invariant part may vanish",
        "The listed classes are then witnesses, not extra axioms",
    )
    for anchor in required:
        assert_anchor(tex, anchor)

    intro_required = (
        "is a surjective coinvariant quotient; its kernel is\nthe completed span",
        "non-injective exactly on windows where such components survive",
        "For Heisenberg, $r(z) = k/z$ is already scalar",
    )
    for anchor in intro_required:
        assert_anchor(intro, anchor)

    retired = (
        "is surjective but not injective for $n \\geq 2$",
        "forces non-trivial elements\nof $\\ker(\\av_n)$",
        "$\\operatorname{av}$ is surjective but not injective: the kernel",
    )
    combined = tex + "\n" + intro + "\n" + intro_backup
    for fragment in retired:
        assert compact(fragment) not in compact(combined)


def test_first_reader_surfaces_name_twisted_descent_and_formal_conductor():
    anchors = {
        "chapters/frame/guide_to_main_results.tex": (
            "$L_R$-twisted completed coinvariant descent",
            "strong\nunitarity $R^{21}(-z)R^{12}(z)=\\id$",
            "ordered conductor is erased",
        ),
        "chapters/theory/introduction.tex": (
            "$L_R$-twisted derived completed\ncoinvariant descent",
            "regular-singular Fulton--MacPherson\nextension",
            "formal homotopy fibre is the ordered\ninformation-loss conductor",
        ),
        "chapters/theory/bar_cobar_adjunction_curved.tex": (
            "untwisted characteristic-zero Reynolds representative",
            "$L_R$-twisted derived completed\ncoinvariant descent",
            "PBW/Koszul $E_\\infty$ surface",
        ),
        "standalone/programme_summary.tex": (
            "$L_R$-twisted derived completed coinvariant descent",
            "formal ordered information-loss conductor",
        ),
        "standalone/survey_modular_koszul_duality.tex": (
            "$L_R$-twisted derived completed coinvariant descent",
            "formal homotopy\nfibre of this descent is the ordered information-loss conductor",
        ),
    }
    for relative_path, required in anchors.items():
        text = visible(ROOT / relative_path)
        for anchor in required:
            assert_anchor(text, anchor)
