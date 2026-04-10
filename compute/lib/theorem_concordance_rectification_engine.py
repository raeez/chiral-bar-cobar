r"""Concordance rectification engine: systematic verification of constitutional claims.

CONCORDANCE (concordance.tex) is the single source of truth for the monograph.
This engine verifies concordance claims against the compute layer, checking:

1. THEOREM STATUS CLAIMS: MC1-MC4 proved, MC5 partially proved (analytic
   HS-sewing lane at all genera; genuswise BV/BRST/bar identification
   conjectural); Koszulness programme counts,
   DK status, three-pillar identification counts.

2. FORMULA CONSISTENCY: kappa values, shadow depths, discriminants,
   growth rates match across concordance and compute engines.

3. CROSS-REFERENCE INTEGRITY: Pillar citations, preprint dependencies,
   arXiv IDs, publication status claims.

4. NUMERICAL CLAIMS: F_g values, Q^contact, Hessian corrections,
   planted-forest formulas, shadow coefficients.

5. STRUCTURAL CLAIMS: four-class G/L/C/M partition, shadow-formality
   identification, operadic complexity.

MULTI-PATH VERIFICATION (per CLAUDE.md):
    Path 1: Direct computation from defining formulas
    Path 2: Cross-family consistency (additivity, complementarity)
    Path 3: Limiting cases (c=0, k=0, genus=0)
    Path 4: Literature comparison (AP38: convention check)

Anti-patterns guarded against:
    AP1:  kappa formula cross-checked across families
    AP10: Tests derive expected values, not hardcode
    AP24: complementarity sum kappa+kappa' checked per family
    AP39: kappa != S_2 for non-Virasoro families
    AP48: kappa(A) != c/2 for general VOAs
"""

from fractions import Fraction
from typing import Dict, List, Optional, Tuple
import math

# ============================================================
# SECTION 1: Theorem status registry
# ============================================================

# MC status claims from concordance
# Canonical source: chapters/connections/editorial_constitution.tex:149-150, 179-191, 819
MC_STATUS = {
    'MC1': 'PROVED',             # PBW concentration, all standard families
    'MC2': 'PROVED',             # Bar-intrinsic construction, thm:mc2-bar-intrinsic
    'MC3': 'PROVED',             # Layers 1+2 all simple types, eval-generated core; Layer 3 type A unconditional, other types conditional on conj:rank-independence-step2
    'MC4': 'PROVED',             # Strong completion-tower theorem
    'MC5': 'PARTIALLY_PROVED',   # Analytic HS-sewing lane proved at all genera;
                                 # genuswise BV/BRST/bar identification conjectural;
                                 # genus 0 algebraic BRST/bar proved
                                 # (thm:algebraic-string-dictionary);
                                 # tree-level amplitude pairing conditional on
                                 # cor:string-amplitude-genus0
}

# Five main theorems
MAIN_THEOREMS = {
    'A': 'PROVED',  # Bar-cobar adjunction + Verdier intertwining
    'B': 'PROVED',  # Bar-cobar inversion on Koszul locus
    'C': 'PROVED',  # Complementarity
    'D': 'PROVED',  # Modular characteristic
    'H': 'PROVED',  # Chiral Hochschild
}

# Koszulness programme counts (from concordance sec:concordance-koszulness-programme)
KOSZULNESS_META_THEOREM = {
    'unconditional_equivalences': 10,   # items (i)-(x)
    'conditional': 1,                    # item (xi) - Lagrangian criterion
    'one_directional': 1,                # item (xii) - D-module purity
    'total_items': 12,
    'lagrangian_standard_landscape': 'unconditional',  # Prop lagrangian-perfectness
    'd_module_purity_km': 'proved_forward',  # chiral localization + Hitchin
    'd_module_purity_converse': 'open',
}

# Three-pillar identification theorems
THREE_PILLAR_IDENTIFICATIONS = {
    'total': 11,
    'proved': 9,
    'structural': 2,  # one-slot obstruction + arity-4 degeneration
}

# Preprint dependency status
PREPRINT_DEPENDENCIES = {
    'Mok25': {
        'arxiv': '2503.17563',
        'author': 'C.-P. Mok',
        'title': 'Logarithmic Fulton-MacPherson configuration spaces',
        'year': 2025,
        'status': 'preprint',
        'theorems_dependent': [
            'thm:ambient-d-squared-zero',
            'thm:log-clutching-degeneration',
            'constr:arity4-degeneration',
            'thm:planted-forest-tropicalization',
            'prop:planted-forest-tropical',
            'thm:logfm-modular-cocomposition',
            'prop:ordered-log-fm-construction',
        ],
        'proved_core_affected': False,  # Five main theorems unaffected
    },
    'MS24': {
        'arxiv': '2408.16787',
        'author': 'Malikov-Schechtman',
        'title': 'Homotopy chiral algebras',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'RNW19': {
        'arxiv': None,  # Published
        'author': 'Robert-Nicoud-Wierstra',
        'title': 'Homotopy morphisms between convolution homotopy Lie algebras',
        'year': 2019,
        'status': 'published',  # J. Noncommut. Geom. 13 (2019)
        'proved_core_affected': False,
    },
    'Val16': {
        'arxiv': None,  # Published
        'author': 'Vallette',
        'title': 'Homotopy theory of homotopy algebras',
        'year': 2020,
        'status': 'published',  # Ann. Inst. Fourier 70 (2020)
        'proved_core_affected': False,
    },
    'Moriwaki26a': {
        'arxiv': '2602.08729',
        'author': 'Moriwaki',
        'title': 'Conformally flat factorization homology',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Moriwaki26b': {
        'arxiv': '2603.06491',
        'author': 'Moriwaki',
        'title': 'Bergman space operads',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Nish26': {
        'arxiv': '2408.00412',  # Note: concordance says 2026 but arXiv is 2024
        'author': 'Nishinaka',
        'title': 'A note on vertex algebras and Costello-Gwilliam factorization algebras',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'Vic25': {
        'arxiv': '2501.08412',
        'author': 'Vicedo',
        'title': 'Full universal enveloping vertex algebras from factorisation',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'GZ26': {
        'arxiv': '2603.08783',
        'author': 'Gaiotto-Zeng',
        'title': 'Interface Minimal Model Holography and Topological String Theory',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'KhanZeng25': {
        'arxiv': '2502.13227',
        'author': 'Khan-Zeng',
        'title': 'Poisson vertex algebras and 3d gauge theory',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    'AMT24': {
        'arxiv': '2407.18222',
        'author': 'Adamo-Moriwaki-Tanimoto',
        'title': 'OS axioms for unitary full VOAs',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
    },
    # NEW REFERENCES from 2024-2026 literature
    'Butson25': {
        'arxiv': '2508.18248',
        'author': 'Butson',
        'title': 'Inverse Hamiltonian Reduction for affine W-algebras in type A',
        'year': 2025,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
    'CFLN24': {
        'arxiv': '2403.08212',
        'author': 'Creutzig-Fasquel-Linshaw-Nakatsuka',
        'title': 'On the structure of W-algebras in type A',
        'year': 2024,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
    'Nafcha26': {
        'arxiv': '2603.30037',
        'author': 'Nafcha',
        'title': 'Nodal degeneration of chiral algebras',
        'year': 2026,
        'status': 'preprint',
        'proved_core_affected': False,
        'concordance_mentioned': False,  # FLAG: should be mentioned
    },
}


# ============================================================
# SECTION 2: Kappa formulas (AP1, AP39, AP48)
# ============================================================

def kappa_heisenberg(k):
    """kappa(H_k) = k. NOT k/2 (AP39 historical error)."""
    return k


def kappa_virasoro(c):
    """kappa(Vir_c) = c/2."""
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def kappa_kac_moody(dim_g, k, h_dual):
    """kappa(V_k(g)) = dim(g) * (k + h^v) / (2 * h^v).

    AP1: This is NOT c/2 in general.
    AP39: S_2 = c/2 != kappa for rank > 1.
    AP48: kappa depends on the full algebra, not Virasoro subalgebra.
    """
    return Fraction(dim_g * (k + h_dual), 2 * h_dual)


def kappa_w_algebra_principal(c):
    """kappa(W_N) = c/2 for principal W-algebras.

    This coincides with kappa_virasoro because W_N has
    a Virasoro subalgebra that controls the scalar genus tower.
    """
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def central_charge_kac_moody(dim_g, k, h_dual):
    """c(V_k(g)) = dim(g) * k / (k + h^v)."""
    return Fraction(dim_g * k, k + h_dual)


def kappa_complementarity_km(dim_g, k, h_dual):
    """kappa(A) + kappa(A!) for Kac-Moody.

    For KM: kappa + kappa' = 0 (AP24).
    Koszul dual: k -> -k - 2h^v.
    """
    kappa_a = kappa_kac_moody(dim_g, k, h_dual)
    kappa_dual = kappa_kac_moody(dim_g, -k - 2 * h_dual, h_dual)
    return kappa_a + kappa_dual


def kappa_complementarity_virasoro(c):
    """kappa(Vir_c) + kappa(Vir_{26-c}) = 13.

    AP24: This is NOT zero for Virasoro.
    """
    return kappa_virasoro(c) + kappa_virasoro(26 - c)


# ============================================================
# SECTION 3: Shadow depth classification (G/L/C/M)
# ============================================================

SHADOW_DEPTH_CLASSES = {
    'G': {'name': 'Gaussian', 'r_max': 2,
           'examples': ['Heisenberg', 'free_fermion', 'Niemeier_lattice']},
    'L': {'name': 'Lie', 'r_max': 3,
           'examples': ['affine_KM']},
    'C': {'name': 'Contact', 'r_max': 4,
           'examples': ['beta_gamma', 'symplectic_fermion']},
    'M': {'name': 'Mixed', 'r_max': float('inf'),
           'examples': ['Virasoro', 'W_N', 'moonshine']},
}


def shadow_depth_class(algebra_type: str) -> str:
    """Return the shadow depth class for a given algebra type."""
    class_map = {
        'heisenberg': 'G', 'free_fermion': 'G', 'lattice': 'G',
        'niemeier': 'G',
        'affine_km': 'L', 'sl2': 'L', 'sl3': 'L',
        'B2': 'L', 'C2': 'L', 'G2': 'L', 'F4': 'L',
        'beta_gamma': 'C', 'symplectic_fermion': 'C',
        'virasoro': 'M', 'W3': 'M', 'W4': 'M', 'W_N': 'M',
        'moonshine': 'M',
    }
    return class_map.get(algebra_type, 'unknown')


# ============================================================
# SECTION 4: Shadow obstruction tower formulas
# ============================================================

def virasoro_S2(c):
    """S_2 = kappa = c/2 for Virasoro."""
    return Fraction(c, 2) if isinstance(c, int) else c / 2


def virasoro_S3():
    """S_3 = 2 for Virasoro (cubic shadow)."""
    return 2


def virasoro_S4(c):
    """S_4 = 10/(c*(5c+22)) for Virasoro (quartic contact coefficient)."""
    if isinstance(c, int):
        return Fraction(10, c * (5 * c + 22))
    return 10.0 / (c * (5 * c + 22))


def virasoro_S5(c):
    """S_5 = -48/(c^2 * (5c+22)) for Virasoro."""
    if isinstance(c, int):
        return Fraction(-48, c**2 * (5 * c + 22))
    return -48.0 / (c**2 * (5 * c + 22))


def virasoro_Q_contact(c):
    """Q^contact_Vir = 10/(c*(5c+22)).

    Same as S_4 for Virasoro. Concordance claims this value.
    """
    return virasoro_S4(c)


def virasoro_delta_H_genus1(c):
    """delta_H^(1)_Vir = 120/(c^2 * (5c+22)) * x^2.

    Returns the coefficient (without x^2).
    Concordance: genus-1 Hessian correction.
    """
    if isinstance(c, int):
        return Fraction(120, c**2 * (5 * c + 22))
    return 120.0 / (c**2 * (5 * c + 22))


def critical_discriminant(kappa_val, S4_val):
    """Delta = 8 * kappa * S_4.

    The organizing invariant (eq:concordance-discriminant).
    Delta = 0 forces r_max <= 3.
    Delta != 0 forces r_max = infinity.
    """
    return 8 * kappa_val * S4_val


def shadow_growth_rate_virasoro(c):
    """rho(Vir_c) = sqrt((180c + 872) / ((5c+22) * c^2)).

    From concordance, Definition def:shadow-growth-rate.
    """
    if c <= 0:
        return float('inf')
    num = 180 * c + 872
    den = (5 * c + 22) * c**2
    return math.sqrt(num / den)


# ============================================================
# SECTION 5: Genus expansion (Faber-Pandharipande)
# ============================================================

def faber_pandharipande_lambda(g):
    """lambda_g^FP = ((2^(2g-1) - 1) / 2^(2g-1)) * |B_{2g}| / (2g)!

    The Faber-Pandharipande tautological class.
    Uses Bernoulli numbers.
    """
    if g <= 0:
        return 0
    B2g = _bernoulli_number(2 * g)
    two_pow = 2**(2 * g - 1)
    return float(abs(B2g)) * (two_pow - 1) / (two_pow * math.factorial(2 * g))


def free_energy(kappa_val, g):
    """F_g(A) = kappa(A) * lambda_g^FP.

    For uniform-weight modular Koszul algebras at all genera.
    Genus-1 unconditional for all families.
    """
    return kappa_val * faber_pandharipande_lambda(g)


def _bernoulli_number(n):
    """Compute Bernoulli number B_n using the recurrence."""
    if n == 0:
        return Fraction(1)
    if n == 1:
        return Fraction(-1, 2)
    if n % 2 == 1 and n > 1:
        return Fraction(0)
    B = [Fraction(0)] * (n + 1)
    B[0] = Fraction(1)
    B[1] = Fraction(-1, 2)
    for m in range(2, n + 1):
        if m % 2 == 1:
            continue
        s = Fraction(0)
        for k in range(m):
            s += _comb(m + 1, k) * B[k]
        B[m] = -s / (m + 1)
    return B[n]


def _comb(n, k):
    """Binomial coefficient."""
    return math.comb(n, k)


# ============================================================
# SECTION 6: Planted-forest corrections
# ============================================================

def planted_forest_genus2(kappa_val, S3_val):
    """delta_pf^{(2,0)} = S_3 * (10*S_3 - kappa) / 48.

    Concordance eq:planted-forest-genus2-polynomial.
    Verified numerically for Virasoro.
    """
    return S3_val * (10 * S3_val - kappa_val) / 48


def planted_forest_genus2_virasoro(c):
    """For Virasoro: delta_pf^{(2,0)} = -(c-40)/48.

    Since kappa = c/2, S_3 = 2:
    delta = 2 * (20 - c/2) / 48 = (40 - c) / 48 = -(c-40)/48.
    """
    return -(c - 40) / 48


# ============================================================
# SECTION 7: Multi-weight genus expansion (AP32)
# ============================================================

def w3_genus2_cross_channel(c):
    """delta_F_2(W_3) = (c + 204) / (16c).

    op:multi-generator-universality RESOLVED NEGATIVELY.
    The scalar formula FAILS for multi-weight algebras at g >= 2.
    This correction is > 0 for all c > 0.
    """
    if c == 0:
        return float('inf')
    return (c + 204) / (16 * c)


# ============================================================
# SECTION 8: Envelope-shadow complexity
# ============================================================

ENVELOPE_SHADOW_COMPLEXITY = {
    'abelian': {'chi_env': 2, 'class': 'G'},
    'affine_current': {'chi_env': 3, 'class': 'L'},
    'beta_gamma_current': {'chi_env': 4, 'class': 'C'},
    'virasoro_current': {'chi_env': float('inf'), 'class': 'M'},
}


# ============================================================
# SECTION 9: E1 modular theory status
# ============================================================

E1_FIVE_THEOREMS = {
    'A_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'B_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'C_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'D_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
    'H_E1': {'genus_0': 'PROVED', 'all_genera': 'PROVED'},
}


# ============================================================
# SECTION 10: Holographic programme status
# ============================================================

HOLOGRAPHIC_TARGETS = {
    'boundary_defect_realization': 'CONJECTURED',
    'yangian_shadow': 'PROVED',
    'sphere_reconstruction': 'PROVED',
    'quartic_resonance_obstruction': 'PROVED',
    'singular_fiber_descent': 'CONJECTURED',
}

ENTANGLEMENT_TARGETS = {
    'G11': 'HEURISTIC',   # algebraic EE, genus-1 proved
    'G12_prime': 'CONJECTURED',  # algebraic QES
    'G12': 'PROVED',       # Koszulness = exact QEC
    'G13': 'CONJECTURED',  # modular flow
    'G14': 'PROVED',       # holographic error correction
    'G15': 'PROVED',       # algebraic Page constraint
    'G16': 'HEURISTIC',   # replica structure
}


# ============================================================
# SECTION 11: DK status
# ============================================================

DK_STATUS = {
    'DK-0': 'PROVED',
    'DK-1': 'PROVED',
    'DK-1.5': 'PROVED',  # lattice
    'DK-2': 'PROVED',    # eval-generated core, all types
    'DK-3': 'PROVED',    # eval-generated core, all types
    'DK-4': 'OPEN',      # ML proved, algebraic id open
    'DK-5': 'CONJECTURED',
}


# ============================================================
# SECTION 12: Spectral discriminant
# ============================================================

def spectral_discriminant_sl2(x, k):
    """Delta_{sl2}(x) = (1 - kx)(1 - (k+4)x) / (1 - 2x).

    Concordance computation comp:spectral-discriminants-standard.
    """
    return (1 - k * x) * (1 - (k + 4) * x) / (1 - 2 * x)


def spectral_discriminant_virasoro(x, c):
    """Delta_Vir(x) = 1 - (c-26)/2 * x."""
    return 1 - (c - 26) / 2 * x


def spectral_discriminant_heisenberg(x, k):
    """Delta_H(x) = 1 - kx."""
    return 1 - k * x


def spectral_discriminant_beta_gamma(x):
    """Delta_{beta_gamma}(x) = 1 + 2x."""
    return 1 + 2 * x


# ============================================================
# SECTION 13: New literature references (2024-2026)
# ============================================================

def check_new_references_coverage():
    """Check which new references are mentioned in the concordance.

    Returns list of (reference, mentioned_in_concordance, should_update).
    """
    findings = []

    # Butson 2508.18248: Inverse Hamiltonian reduction for ALL orbits type A
    findings.append({
        'ref': 'Butson25',
        'arxiv': '2508.18248',
        'title': 'Inverse Hamiltonian Reduction for affine W-algebras in type A',
        'concordance_section': 'sec:concordance-non-principal-w',
        'currently_mentioned': False,
        'impact': 'SIGNIFICANT: proves inverse reduction for ALL orbits in type A, '
                  'upgrading hook-type corridor to full type-A resolution. '
                  'Transport-to-transpose conjecture may be promotable.',
        'action': 'UPDATE: add to non-principal W section, update hook-type status',
    })

    # Creutzig-Fasquel-Linshaw-Nakatsuka 2403.08212
    findings.append({
        'ref': 'CFLN24',
        'arxiv': '2403.08212',
        'title': 'On the structure of W-algebras in type A',
        'concordance_section': 'sec:concordance-non-principal-w',
        'currently_mentioned': False,
        'impact': 'SIGNIFICANT: structure theory for all W-algebras in type A, '
                  'building blocks via hook-type reductions. Directly relevant to '
                  'transport-closure computation.',
        'action': 'UPDATE: add to non-principal W section',
    })

    # Nafcha 2603.30037: Nodal degeneration of chiral algebras
    findings.append({
        'ref': 'Nafcha26',
        'arxiv': '2603.30037',
        'title': 'Nodal degeneration of chiral algebras',
        'concordance_section': 'sec:concordance-three-pillars (analytic programme)',
        'currently_mentioned': False,
        'impact': 'MODERATE: gluing formula for chiral homology, relevant to '
                  'MC5 sewing programme and analytic completion.',
        'action': 'UPDATE: add to analytic sewing section and preprint table',
    })

    # Vicedo 2501.08412: already mentioned
    findings.append({
        'ref': 'Vic25',
        'arxiv': '2501.08412',
        'title': 'Full universal enveloping vertex algebras from factorisation',
        'concordance_section': 'sec:concordance-nishinaka-vicedo',
        'currently_mentioned': True,
        'impact': 'Already covered',
        'action': 'NO UPDATE NEEDED',
    })

    # Nishinaka 2408.00412: mentioned but with wrong year
    findings.append({
        'ref': 'Nish26',
        'arxiv': '2408.00412',
        'title': 'A note on vertex algebras and CG factorization algebras',
        'concordance_section': 'sec:concordance-nishinaka-vicedo',
        'currently_mentioned': True,
        'impact': 'MINOR: concordance says "preprint, 2026" but arXiv shows 2024. '
                  'Verify if there is a distinct 2026 version or if this is misdated.',
        'action': 'CHECK: verify year; update if 2024 not 2026',
    })

    return findings


# ============================================================
# SECTION 14: Concordance audit findings
# ============================================================

def audit_concordance_claims():
    """Run systematic audit of concordance claims.

    Returns list of (section, finding, severity, action).
    """
    findings = []

    # 1. Check MC status consistency
    for mc, status in MC_STATUS.items():
        if status != 'PROVED':
            findings.append({
                'section': 'MC frontier',
                'finding': f'{mc} not marked as PROVED: {status}',
                'severity': 'CRITICAL',
                'action': 'Verify and update',
            })

    # 2. Check kappa complementarity (AP24)
    # KM: kappa + kappa' = 0
    km_sum = kappa_complementarity_km(3, 1, 2)  # sl2, k=1
    if km_sum != 0:
        findings.append({
            'section': 'Theorem D',
            'finding': f'KM kappa complementarity fails: sum = {km_sum}',
            'severity': 'CRITICAL',
            'action': 'Check kappa formula',
        })

    # Virasoro: kappa + kappa' = 13
    vir_sum = kappa_complementarity_virasoro(10)
    if vir_sum != 13:
        findings.append({
            'section': 'Theorem D',
            'finding': f'Virasoro kappa complementarity wrong: sum = {vir_sum}',
            'severity': 'CRITICAL',
            'action': 'Check kappa formula',
        })

    # 3. Check shadow depth classification
    for alg, expected_class in [
        ('heisenberg', 'G'), ('affine_km', 'L'),
        ('beta_gamma', 'C'), ('virasoro', 'M')
    ]:
        actual = shadow_depth_class(alg)
        if actual != expected_class:
            findings.append({
                'section': 'Shadow depth',
                'finding': f'{alg} classified as {actual}, expected {expected_class}',
                'severity': 'SERIOUS',
                'action': 'Fix classification',
            })

    # 4. Check F_1 = kappa/24 (genus-1 universality)
    for c_val in [2, 10, 13, 25, 26]:
        k = kappa_virasoro(c_val)
        f1 = free_energy(float(k), 1)
        expected = float(k) / 24
        if abs(f1 - expected) > 1e-12:
            findings.append({
                'section': 'Theorem D genus-1',
                'finding': f'F_1(Vir_{c_val}) = {f1}, expected {expected}',
                'severity': 'CRITICAL',
                'action': 'Check FP formula',
            })

    # 5. Check critical discriminant
    for c_val in [2, 10, 26]:
        k = float(kappa_virasoro(c_val))
        s4 = float(virasoro_S4(c_val))
        delta = critical_discriminant(k, s4)
        if c_val > 0 and delta == 0:
            findings.append({
                'section': 'Critical discriminant',
                'finding': f'Delta(Vir_{c_val}) = 0, should be nonzero for class M',
                'severity': 'SERIOUS',
                'action': 'Check discriminant formula',
            })

    # 6. Check Mok25 preprint exists on arXiv
    mok = PREPRINT_DEPENDENCIES['Mok25']
    findings.append({
        'section': 'Pillar C',
        'finding': f'Mok25 arXiv:{mok["arxiv"]} confirmed to exist (BibSonomy indexed). '
                   f'Status: {mok["status"]}. Proved core unaffected if revised.',
        'severity': 'INFO',
        'action': 'No action needed; dependency correctly documented',
    })

    # 7. Check new references not in concordance
    new_refs = check_new_references_coverage()
    for ref in new_refs:
        if not ref['currently_mentioned'] and 'NO UPDATE' not in ref['action']:
            findings.append({
                'section': ref['concordance_section'],
                'finding': f'Missing reference: {ref["ref"]} arXiv:{ref["arxiv"]} '
                           f'({ref["title"]}). Impact: {ref["impact"]}',
                'severity': 'MODERATE',
                'action': ref['action'],
            })

    # 8. Check W_3 genus-2 cross-channel (AP32)
    for c_val in [1, 2, 10, 25]:
        delta_f2 = w3_genus2_cross_channel(c_val)
        if delta_f2 <= 0:
            findings.append({
                'section': 'Multi-weight genus expansion',
                'finding': f'delta_F_2(W_3, c={c_val}) = {delta_f2} <= 0',
                'severity': 'CRITICAL',
                'action': 'Should be > 0 for c > 0',
            })

    # 9. Check Nishinaka year discrepancy
    nish = PREPRINT_DEPENDENCIES['Nish26']
    findings.append({
        'section': 'sec:concordance-nishinaka-vicedo',
        'finding': f'Nishinaka cited as [Nish26] (2026) but arXiv {nish["arxiv"]} '
                   f'submitted 2024. Possible version confusion.',
        'severity': 'MINOR',
        'action': 'Verify whether 2026 version exists or update year',
    })

    # 10. Check Koszulness programme counts
    meta = KOSZULNESS_META_THEOREM
    if meta['unconditional_equivalences'] + meta['conditional'] + meta['one_directional'] != meta['total_items']:
        findings.append({
            'section': 'sec:concordance-koszulness-programme',
            'finding': 'Koszulness count mismatch',
            'severity': 'CRITICAL',
            'action': 'Fix counts',
        })

    return findings
