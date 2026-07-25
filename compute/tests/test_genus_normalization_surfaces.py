"""Source-level guards for the genus tower and scalar lane conventions."""

from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[2]
GENUS_COMPLETE_TEX = REPO_ROOT / "chapters/connections/genus_complete.tex"
HIGHER_GENUS_FOUNDATIONS_TEX = (
    REPO_ROOT / "chapters/theory/higher_genus_foundations.tex"
)
SIGNS_AND_SHIFTS_TEX = REPO_ROOT / "appendices/signs_and_shifts.tex"
LANDSCAPE_CENSUS_TEX = REPO_ROOT / "chapters/examples/landscape_census.tex"
MASTER_CONCORDANCE_TEX = REPO_ROOT / "chapters/connections/master_concordance.tex"
EXCEPTIONAL_YANGIAN_TEX = (
    REPO_ROOT / "chapters/examples/exceptional_yangian_koszul_duality_platonic.tex"
)
ORDERED_ASSOCIATIVE_TEX = (
    REPO_ROOT / "chapters/theory/ordered_associative_chiral_kd.tex"
)


def _source(path: Path) -> str:
    return path.read_text()


def _block(source: str, label: str, env: str, end_env: str | None = None) -> str:
    label_pos = source.index(rf"\label{{{label}}}")
    start = source.rindex(rf"\begin{{{env}}}", 0, label_pos)
    end_marker = rf"\end{{{end_env or env}}}"
    return " ".join(source[start:source.index(end_marker, start)].split())


def test_formal_genus_class_and_curvature_are_typed():
    """Formal genus data, diagonal trace, and curvature identity are typed."""
    source = _source(GENUS_COMPLETE_TEX)

    formal = _block(source, "def:formal-genus-class-hodge-normalization", "definition")
    diagonal = _block(source, "def:diagonal-trace-ordered-curvature", "definition")
    curvature = _block(
        source,
        "prop:ordered-curvature-scalar-hodge-projection",
        "proposition",
        "proof",
    )
    genus_one = _block(source, "rem:genus-one-anomaly-kzb-comparison", "remark")

    for required in (
        r"\ClaimStatusDefinitional",
        r"\mathcal F_g(\cA)",
        r"\operatorname{CW}_{\cA,g}(\Theta_\cA)",
        r"R^\bullet(\overline{\cM}_{g,0})",
        r"\operatorname{tr}^{\mathrm{FP}}_g",
        r"\lambda_g^{\mathrm{FP}}",
        r"\frac{2^{2g-1}-1}{2^{2g-1}}\frac{|B_{2g}|}{(2g)!}",
        "analytic free energy only after",
        "HS-sewing or trace-class hypothesis",
    ):
        assert required in formal

    for required in (
        r"\ClaimStatusDefinitional",
        r"\operatorname{tr}_{\mathrm{diag}}",
        "diagonal OPE channel",
        r"\operatorname{tr}_{\mathrm{diag}}\bigl(r_\cA(z)\bigr)=\kappa(\cA)",
        "ordered two-point residue kernel",
        r"d_{\mathrm{fib}}^{\mathrm{ord}}",
    ):
        assert required in diagonal

    for required in (
        r"\ClaimStatusConditional",
        "Type signature",
        r"\bigl(d_{\mathrm{fib}}^{\mathrm{ord}}\bigr)^2",
        r"r_\cA(z)\cdot\omega_g",
        "endomorphism-valued curvature classes",
        "neither a scalar identity",
        r"\kappa(\cA)\lambda_g",
        r"F_g^{\mathrm{diag}}(\cA)=\kappa(\cA)\lambda_g^{\mathrm{FP}}",
    ):
        assert required in curvature

    for required in (
        r"\widehat E_2(\tau)=E_2(\tau)-\frac{3}{\pi\,\operatorname{Im}\tau}",
        r"\widehat E_2-E_2",
        "no holomorphic preimage",
        "KZB",
        "cohomological class, the quasi-modular representative, and the analytic connection are different objects",
    ):
        assert required in genus_one


def test_genus_variables_loop_sign_and_formal_language_are_pinned():
    """Genus variables, hbar-degree, loop sign, and formal/analytic split are explicit."""
    signs = _source(SIGNS_AND_SHIFTS_TEX)
    foundations = _source(HIGHER_GENUS_FOUNDATIONS_TEX)

    convention = _block(signs, "conv:genus-variable-normalization-table", "convention")
    differentials = _block(foundations, "conv:higher-genus-differentials", "convention")
    curvature_operator = _block(
        foundations,
        "prop:chain-level-curvature-operator",
        "proposition",
        "proof",
    )

    for required in (
        r"\ClaimStatusDefinitional",
        r"t & k+h^\vee",
        r"q & e^{2\pi i\tau}",
        r"\hbar & \text{genus/quantum formal parameter}",
        r"z & \text{local collision or spectral coordinate}",
        r"\omega & \text{holomorphic differential on a curve}",
        r"\omega_g & \text{Chern--Weil Hodge-curvature package}",
        r"\mathcal F_g(\cA) & \text{formal genus cohomology class}",
        r"F_g(\cA) & \text{Faber--Pandharipande scalar trace",
        r"\operatorname{tr}_{\mathrm{diag}}",
        r"\lambda_g^{\mathrm{FP}}",
        r"\kappa(\cA) & \text{degree-two scalar modular characteristic}",
        r"K^\kappa(\cA,\cA^!)",
        r"\bar B^{\mathrm{full}}=\prod_{g\ge0}\hbar^g\bar B^{(g)}",
        r"\hbar\Delta",
        "loop edge is oriented by the determinant line",
        "nonseparating loop has sign",
        "string-coupling symbol is $g_s$",
    ):
        assert required in convention

    for required in (
        r"\ClaimStatusDefinitional",
        r"d_{\mathrm{FT}} = d_{\mathrm{tree}} + d_{\mathrm{loop}}",
        r"m_1^{(g)\,2}(a)",
        r"[m_0^{(g)},a]_{m_2}",
        r"\operatorname{tr}_{\mathrm{diag}}\!\bigl(m_0^{(g)}\bigr)",
        r"\kappa(\cA)\cdot\omega_g",
        r"\Dg{g}",
        r"d_{\mathrm{per}}^{(g)}",
        r"\nabla_{\mathrm{KS}}^{\mathrm{GM}}",
    ):
        assert required in differentials

    for required in (
        r"\ClaimStatusConditional",
        r"\label{eq:chain-curvature-operator}",
        r"m_1^{(g)\,2}(a)",
        r"[m_0^{(g)},a]_{m_2}",
        "inner-curvature formula",
        "scalar projected representative",
        "uniform-weight scalar lane",
        "Hodge curvature matrix",
        r"\det\!\Bigl(\frac{i}{2\pi}\Theta_{\mathbb{E}}\Bigr)",
    ):
        assert required in curvature_operator

    title_re = re.compile(
        r"\\begin\{(?:theorem|proposition|corollary|definition|computation)\}"
        r"\[[^\]]*free energy",
        re.IGNORECASE,
    )
    for path in (
        GENUS_COMPLETE_TEX,
        HIGHER_GENUS_FOUNDATIONS_TEX,
        REPO_ROOT / "chapters/examples/genus_expansions.tex",
        REPO_ROOT / "chapters/theory/higher_genus_modular_koszul.tex",
    ):
        assert not title_re.search(_source(path)), path


def test_master_concordance_bp_lanes_are_pinned():
    """The exact BP central lane and open modular lane stay distinct."""
    compact_concordance = re.sub(r"\s+", "", _source(MASTER_CONCORDANCE_TEX))
    for required in (
        r"c_{\mathrm{BP}}(k)=-\frac{(2k+3)(3k+1)}{k+3}",
        r"c_{\mathrm{BP}}(k)+c_{\mathrm{BP}}(-k-6)=50",
        r"$J,T,G^+,G^-$areeven",
        r"$1+2/3+2/3+1/2=17/6$",
        r"\ClaimStatusOpen{}pendingthecompletegenus-oneminimal-DScurvaturecalculation",
        r"\kappa_{\mathrm{BP}}=c_{\mathrm{BP}}/6$wouldimply$K^\kappa_{\mathrm{BP}}=25/3",
        r"c_{\mathrm{BP}}^{\mathrm{shift}}(k)=2-\frac{24(k+1)^2}{k+3}",
        r"c_{\mathrm{BP}}^{\mathrm{shift}}(k)+c_{\mathrm{BP}}^{\mathrm{shift}}(-k-6)=196",
        r"H_{\mathrm{BP}}^{\mathrm{DS/bar}}",
        r"c^{\mathrm{mid}}_{\mathrm{BP}}=25=50/2",
        r"k=-3\pm2i",
    ):
        assert required in compact_concordance

    for stale in (r"98/3", r"c=98", r"98=196/2"):
        assert stale not in compact_concordance
    assert r"K^\kappa_{\mathrm{BP}}=\frac16\,K^c_{\mathrm{BP}}" not in compact_concordance


def test_master_concordance_principal_w3_scalar_status_is_split():
    """The exact W3 central conductor and conditional modular image stay separate."""
    source = _source(MASTER_CONCORDANCE_TEX)
    compact_source = re.sub(r"\s+", "", source)

    for required in (
        r"H_{\mathrm{diag}}^{g=1}+H_{W_N}^{\mathrm{DS/bar}}",
        r"\kappa(\mathcalW_N)=c(H_N-1)",
        r"$K_3^c=100$exactly",
        r"$250/3$on$H_{\mathrm{diag}}^{g=1}+H_{W_3}^{\mathrm{DS/bar}}$",
        r"\{0,\,13\}",
        r"$K_3^\kappa=250/3$",
        r"\{0,\,13,\,250/3\}",
    ):
        assert re.sub(r"\s+", "", required) in compact_source

    assert "The proved scalar values in the displayed rows are" not in source


def test_ordered_line_normalization_is_separate_from_theorem_c_conductor():
    """A chosen nonzero line-side square root is not a universal conductor law."""
    source = _source(ORDERED_ASSOCIATIVE_TEX)
    block = _block(source, "rem:oackd-3", "remark")

    for required in (
        r"K^\kappa(A,A^!)=\kappa(A)+\kappa(A^!)",
        r"P^{\kappa}_{\mathrm{line}}(A)",
        r"P^{\kappa}_{\mathrm{line}}(A)\in\CC^\times",
        r"\hbar^{2}\,P^{\kappa}_{\mathrm{line}}(A)",
        "records the chosen line-side normalisation",
        "zero-product lanes",
        r"2c_+=2\cdot4=8",
        r"H_{\mathsf B}",
        r"\{0,13,250/3\}",
        "remain separate open comparison ledgers",
    ):
        assert required in block

    for stale in (
        r"\hbar^{2}\,K^{\kappa_{\mathrm{ch}}}(A)",
        "family-independent multiplicative pairing",
        r"\{0,8,13,250/3,25/3\}",
        "three genuinely independent derivations",
    ):
        assert stale not in block


def test_master_concordance_theorem_lanes_and_fixed_c_are_typed():
    """Theorem A, Theorem B, and fixed-C second-kind maps stay disjoint."""
    source = _source(MASTER_CONCORDANCE_TEX)
    start = source.index(r"\textbf{Lane} & \textbf{Functorial operation}")
    end = source.index(r"\end{tabular}", start)
    table = " ".join(source[start:end].split())

    for required in (
        r"Universal reconstruction & $\epsilon_\cA\colon\Omega B(\cA)\to\cA$",
        "Theorem~A is the universal bar--cobar counit equivalence",
        r"Quadratic recognition & $q_\cA\colon\cA^{\mathrm i}\to B(\cA)$",
        r"Theorem~B recognizes the locus on which $q_\cA$ is a quasi-isomorphism",
        r"Fixed-$C$ second kind",
        r"D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})\simeq D^{\mathrm{ctr}}(C\text{-}\mathrm{ContraFact})",
        "separate second-kind statement",
    ):
        assert required in table

    assert "Theorem~B: strict quasi-isomorphism" not in table


def test_master_concordance_five_theorem_surface_keeps_ab_typed():
    """The summary table assigns reconstruction, recognition, and fixed-C exactly."""
    source = _source(MASTER_CONCORDANCE_TEX)
    section = source.index(r"\label{sec:master-concordance-theorem-surfaces}")
    start = source.index(r"\begin{tabular}", section)
    end = source.index(r"\end{tabular}", start)
    table = " ".join(source[start:end].split())

    for required in (
        r"A & Universal bar--cobar reconstruction",
        r"$\epsilon_\cA\colon\Omega B(\cA)\to\cA$",
        "complete enhanced associative Ran ambient under $H_1$",
        r"B & Quadratic Koszul recognition",
        r"$q_\cA\colon\cA^{\mathrm i}\to B(\cA)$ is a quasi-isomorphism",
        r"$\Omega(\cA^{\mathrm i})\to\cA$ is a quasi-isomorphism",
        r"-- & Fixed-$C$ second-kind equivalence",
        r"D^{\mathrm{co}}(C\text{-}\mathrm{CoFact})\simeq D^{\mathrm{ctr}}(C\text{-}\mathrm{ContraFact})",
        r"$\mathsf{Tw}^{\mathrm{ch}}_{\mathrm{acyc}}(C,A,\tau)$",
    ):
        assert required in table

    for stale in (
        "B & Bar--cobar inversion / chiral Positselski",
        r"Strict inversion $\Omega B(\cA)\simeq\cA$",
        "raw direct-sum class-$M$ chain inversion is false",
    ):
        assert stale not in table


def test_master_concordance_w3_midpoint_fibre_is_canonical():
    """The principal W3 midpoint fibre is k=-3 plus or minus i."""
    source = _source(MASTER_CONCORDANCE_TEX)
    start = source.index(r"\emph{Complex scalar-midpoint fibres")
    end = source.index(r"\end{remark}", start)
    compact = re.sub(r"\s+", "", source[start:end])

    for required in (
        r"c_{\cW_3}(k)=2-\frac{24(k+2)^2}{k+3}",
        r"=50-24\left((k+3)+\frac{1}{k+3}\right)",
        r"c_{\cW_3}(k)=50",
        r"(k+3)^2+1=0",
        r"k=-3\pmi",
    ):
        assert required in compact

    assert r"4/(k+3)" not in compact


def test_kappa_lane_constants_and_k3_firewall_are_pinned():
    """Kappa lanes, K3 constants, and no Yangian/RTT transfer are explicit."""
    census = _source(LANDSCAPE_CENSUS_TEX)
    concordance = " ".join(_source(MASTER_CONCORDANCE_TEX).split())
    exceptional = _source(EXCEPTIONAL_YANGIAN_TEX)

    k3 = _block(
        census,
        "prop:G-B-heisenberg-rho-bifurcation",
        "proposition",
        "proof",
    )
    firewall = _block(
        exceptional,
        "prop:exceptional-yangian-no-dk-root-k3-promotion",
        "proposition",
    )

    for required in (
        r"\ClaimStatusConjectured",
        r"hypothesis package $H_{\mathsf B}",
        r"\Lambda_{\mathrm{Muk}}=\widetilde H(K3,\mathbb Z)",
        "rank~$24$ and signature~$(4,20)$",
        r"2c_+(\Lambda_{\mathrm{Muk}})=8",
        r"(\varrho,K,K^\kappa,\kappa^{\mathrm{mid}})",
        r"\left(\frac16,48,8,4\right)",
        r"\ClaimStatusProvedHere",
        "chiral-conductor interpretation",
        r"\ClaimStatusConjectured under~$H_{\mathsf B}$",
    ):
        assert required in k3

    for required in (
        r"K^\kappa(\cA):=\kappa(\cA)+\kappa(\cA^!)",
        r"Heisenberg $\mathcal H_k$",
        r"Affine $V_k(\fg)$",
        r"$\beta\gamma_\lambda$",
        r"\mathrm{Vir}_c",
        r"$13$",
        r"Principal $\mathcal W_3^k$",
        r"$250/3$",
        r"Bershadsky--Polyakov",
        r"$25/3$",
        r"Mukai-enhanced K3 Heisenberg",
        r"$8$",
        "Borcherds weight $\\kappa_{\\mathrm{BKM}}(\\Delta_5)=5$ occupies its own typed lane",
    ):
        assert required in concordance

    for required in (
        r"\ClaimStatusConditional",
        "A transfer from a neighboring construction",
        r"\mathscr R_{\fg,N}",
        r"\vartheta_{\fg,N}",
        "Drinfeld--Kohno supplies monodromy and braiding",
        "root-of-unity specialization supplies an integral form",
        "The K3 construction supplies the completed Hall--Drinfeld bialgebra",
        r"\mathcal Y^{\mathrm{Hall}}_\hbar(\mathrm{CoHA}_{K3\times E})",
        r"the comparison theorem is the construction of $K_{\fg,\hbar}$",
        r"Definition~\ref{def:finite-yangian-module-packet}",
    ):
        assert required in firewall
