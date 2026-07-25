"""Guards for the standard-family formula and comparison surfaces."""

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
LANDSCAPE = ROOT / "chapters/examples/landscape_census.tex"
HEISENBERG = ROOT / "chapters/frame/heisenberg_frame.tex"
KAC_MOODY = ROOT / "chapters/examples/kac_moody.tex"
BETA_GAMMA = ROOT / "chapters/examples/beta_gamma.tex"
W_DEEP = ROOT / "chapters/examples/w_algebras_deep.tex"
SYMMETRIC_ORBIFOLDS = ROOT / "chapters/examples/symmetric_orbifolds.tex"
EXCEPTIONAL_YANGIAN = (
    ROOT / "chapters/examples/exceptional_yangian_koszul_duality_platonic.tex"
)


def read(path: Path) -> str:
    return path.read_text()


def compact(text: str) -> str:
    return (
        re.sub(r"\s+", "", text)
        .replace(r"\(", "")
        .replace(r"\)", "")
    )


def longtable_block(text: str, label: str) -> str:
    anchor = rf"\label{{{label}}}"
    label_pos = text.index(anchor)
    start = text.rfind(r"\begin{longtable}", 0, label_pos)
    end = text.index(r"\end{longtable}", label_pos)
    return text[start : end + len(r"\end{longtable}")]


def row_window(table: str, start: str, end: str) -> str:
    start_pos = table.index(start)
    end_pos = table.index(end, start_pos)
    return table[start_pos:end_pos]


def test_standard_family_source_data_names_three_mathematical_surfaces():
    text = read(LANDSCAPE)
    required = (
        r"\paragraph{Standard families: objects, formulas, and sources.}",
        r"\label{par:standard-family-source-data}",
        "the singular products defining",
        "the formulas derived from those products",
        "the comparison morphisms that carry these formulas from the OPE presentation",
        r"\caption{Defining formulas, parameter loci, and mathematical sources}",
        r"\label{tab:standard-family-status}",
        r"\caption{Presentations, finite calculations, and comparison morphisms}",
        r"\label{tab:standard-family-ambient}",
        r"\caption{Bar, quadratic-dual, Verdier-dual, and centre constructions}",
        r"\label{tab:standard-family-five-object-package}",
    )
    squashed = " ".join(text.split())
    for fragment in required:
        assert " ".join(fragment.split()) in squashed, fragment


def test_status_table_retains_exact_local_formulas():
    table = compact(
        longtable_block(read(LANDSCAPE), "tab:standard-family-status")
    )
    required = (
        r"J(z)J(w)\simk(z-w)^{-2}",
        r"d[J|J]=k\mathbf1",
        r"r^{\mathrm{coll}}(z)=k/z",
        r"\kappa_{\mathrm{mod}}(\cH_k)=k",
        r"\mathfrakC(x,y,z)=\kappa_\fg(x,[y,z])",
        r"\{\mathfrakC,\mathfrakC\}=0",
        r"r_{\max}=3",
        r"\kappa_{\mathrm{mod}}=d(k+h^\vee)/(2h^\vee)",
        r"\kappa_{\mathrm{mod}}(\beta\gamma_\lambda)=6\lambda^2-6\lambda+1",
        r"S_3=0,S_4=-5/12,S_r=0",
        r"\kappa_{\mathrm{mod}}=c/2,S_3=2",
        r"S_4=10/[c(5c+22)]",
        r"\alpha(c)=16/(22+5c)",
        r"K_N^c=4N^3-2N-2",
        r"K_3^{\kappa_{\mathrm{mod}}}=250/3",
        r"\mathfrakz(\widehat{\fg}_{-h^\vee})\cong\mathcalO(\mathrm{Op}_{\fg^\vee}(D))",
        r"C_{n,r}(h_n,v)=\sum_{t=0}^{r}\binom{n-r+t}{t}e_{r-t}(v)h_n^t",
        r"\kappa=(k+4)/4=(6-c)/[2(3-c)]",
        r"\varepsilon(\alpha,\beta)=(-1)^{\langle\alpha,\beta\rangle}\varepsilon(\beta,\alpha)",
        r"q_p:\mathcalW(p)^{\mathrmi}\to\barB(\mathcalW(p))",
        r"\rho_{\fg,N}:R_{\fg,\leN}^{\perp}\toR_{\fg,\leN}(-\hbar)",
    )
    for fragment in required:
        assert compact(fragment) in table, fragment


def test_status_table_preserves_conditional_and_open_boundaries():
    table = longtable_block(read(LANDSCAPE), "tab:standard-family-status")
    windows = {
        "beta_gamma": row_window(table, r"\(\beta\gamma_\lambda\),", r"\(\Vir_c\)"),
        "virasoro": row_window(table, r"\(\Vir_c\)", r"Principal \(\mathcal W_N\)"),
        "principal_w": row_window(table, r"Principal \(\mathcal W_N\)", "Critical affine"),
        "symmetric": row_window(table, "Symmetric orbifold", r"Triplet \(\mathcal W(p)\)"),
        "triplet": row_window(table, r"Triplet \(\mathcal W(p)\)", "Admissible affine quotient"),
        "admissible": row_window(table, "Admissible affine quotient", "Super-Yangian"),
        "super": row_window(table, "Super-Yangian", "Exceptional affine and Yangian rows"),
        "exceptional": row_window(table, "Exceptional affine and Yangian rows", r"\bottomrule"),
    }
    required_by_row = {
        "beta_gamma": "conditional",
        "virasoro": "conditional",
        "principal_w": "conditional on DS/bar transport",
        "symmetric": "proved character identity; bar comparison open",
        "triplet": r"proved \(C_2\)-finiteness; Koszulness conjectured",
        "admissible": "proved finite windows; global comparison open",
        "super": "conditional",
        "exceptional": "affine formulas proved; Yangian comparison conditional",
    }
    for row, expected in required_by_row.items():
        assert compact(expected) in compact(windows[row]), row


def test_ambient_table_names_realization_maps_and_completions():
    table = compact(
        longtable_block(read(LANDSCAPE), "tab:standard-family-ambient")
    )
    required = (
        r"quadraticcomparisonq_{\cH}",
        r"q_{V_k(\fg)}:V_k(\fg)^{\mathrmi}\to\barB(V_k(\fg))",
        r"finite-typeVerdierdualityandcontinuousduals",
        r"transportedalongtheDS/barmorphism",
        r"Reynoldsbarmapforthefixed-pointalgebra",
        r"theconesofq_pandof\barB(V_k(\fg))\to\barB(L_k(\fg))",
        r"finite-windowmaps\rho_{\fg,N}",
        r"theinverselimitrequiresMittag--LefflercompatibilityandcompletedPBW",
    )
    for fragment in required:
        assert compact(fragment) in table, fragment


def test_five_object_table_separates_bar_dual_and_centre_constructions():
    text = read(LANDSCAPE)
    table = compact(
        longtable_block(text, "tab:standard-family-five-object-package")
    )
    prelude = compact(
        text[
            text.index("The full bar coalgebra and the quadratic Koszul dual coalgebra") :
            text.index(r"\begin{longtable}", text.index("The full bar coalgebra"))
        ]
    )
    required_prelude = (
        r"\barB(A)=T^c(s^{-1}\barA)",
        r"q_A:A^{\mathrmi}\longrightarrow\barB(A)",
        r"A^!=\mathbbD_{\Ran}(A^{\mathrmi})",
        r"Z_{\mathrm{ch}}^{\mathrm{der}}(A)=C^\bullet_{\mathrm{ch}}(A,A)",
    )
    for fragment in required_prelude:
        assert compact(fragment) in prelude, fragment

    required_rows = (
        r"(\operatorname{Sym}^{\mathrm{ch}}(V^*[1]),m_0=-k\omega)",
        r"\mathrm{CE}^{\mathrm{ch}}(\widehat{\fg}_{-k-2h^\vee})",
        r"\Vir_{26-c}",
        r"\mathcalW_N^{k'}",
        r"A^!\simeqAontheunimodularlocus",
        r"fullquadraticcomparisonisanopenconstruction",
        r"fixed-pointfullbarwithReynoldscomparison",
        r"finite-windowinverse-RTTdual",
        r"pro-centreaftercompatibleinverselimit",
    )
    for fragment in required_rows:
        assert compact(fragment) in table, fragment


def test_family_chapters_supply_primary_formula_anchors():
    anchors = {
        HEISENBERG: (
            r"\label{eq:frame-heisenberg-ope}",
            r"\label{thm:frame-heisenberg-bar}",
            r"\label{thm:frame-heisenberg-koszul-dual}",
            r"\kappa(\mathcal{H}_k) = k",
        ),
        KAC_MOODY: (
            r"\kappa^{\mathrm{KM}}(V_k(\fg))",
            r"r^{\mathrm{coll}}_{\mathrm{KM}}(z)",
            r"r_{\max} = 3",
            "Feigin--Frenkel oper",
        ),
        BETA_GAMMA: (
            r"\beta(z)\gamma(w)\sim 1/(z{-}w)",
            r"S_4 = -\tfrac{5}{12}",
            r"\kappa(\beta\gamma_\lambda)+\kappa(bc_\lambda)=0",
            r"\lambda = 1/2",
        ),
        W_DEEP: (
            r"\Lambda={:}TT{:}-\frac{3}{10}\partial^2T",
            r"16}{5c+22",
            r"250/3",
            "Bershadsky--Polyakov",
        ),
        SYMMETRIC_ORBIFOLDS: (
            r"\label{sec:symn-dmvv}",
            "DMVV product formula",
            "ordered-bar Hilbert series",
        ),
        EXCEPTIONAL_YANGIAN: (
            r"\widehat Y_\hbar(E_6)^{!,\mathrm{cont}}",
            r"\widehat Y_\hbar(E_7)^{!,\mathrm{cont}}",
            r"\widehat Y_\hbar(E_8)^{!,\mathrm{cont}}",
        ),
    }
    for path, fragments in anchors.items():
        text = read(path)
        for fragment in fragments:
            assert fragment in text, f"{fragment!r} missing from {path}"
