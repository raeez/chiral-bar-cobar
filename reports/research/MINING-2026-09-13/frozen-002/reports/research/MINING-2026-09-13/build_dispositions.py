"""Bind recovered claims and remaining obligations to exact retained sources."""

from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
inventory = json.loads((HERE / 'source-inventory.json').read_text())
chapter = ROOT / 'platonic/chapters/ordered_native_collision.tex'
chapter_lines = chapter.read_text().splitlines()
items = []


def source(suffix, anchors):
    row = next(x for x in inventory['sources'] if x['source'].endswith(suffix))
    return {k: row[k] for k in ('source', 'sha256', 'preserved')} | {'anchors': anchors}


def add(identifier, claim, status, sources, labels, proof, residual=''):
    destinations = []
    for label in labels:
        needle = '\\label{' + label + '}'
        line = next(i for i, text in enumerate(chapter_lines, 1) if needle in text)
        destinations.append({'path': str(chapter.relative_to(ROOT)), 'label': label, 'line': line})
    items.append({'id': identifier, 'mathematical_statement': claim,
                  'disposition': status, 'sources': sources,
                  'destination': destinations, 'proof_or_reason': proof,
                  'consuming_theorem': labels, 'residual_obligation': residual})


C = 'c78745d9a966c927739a49f3b22192c389065372a24de6990b6e58355e9bc75d.txt'
E = 'ebc8bb469caa65b9042f8361e2d94043a2058141da1a1e23e85cbd51c34db0.txt'
B = '/manuscript/ordered-coefficient-bar.tex'
O = '/manuscript/ordered-collisions-and-residues.tex'
S = '/returns/ordered_chiral_substance-final-01.md'

add('M01', 'The two-chart ordered DGA has cohomology R plus principal parts in degree one and derived collision fibre k x k.',
    'integrated', [source(C, 'Chapter 11.1, lines 2275-2318'), source(O, 'proposition prop:ocr-line-algebra')],
    ['prop:native-binary-restrictions'], 'Endpoint multiplication and bounded flat base change are recomputed in the actual TeX proof.')
add('M02', 'Relative formality fails: the derived fibre of the cohomology algebra is dual numbers.',
    'integrated', [source(C, 'Theorem 11.1'), source(O, 'thm:ocr-relative-nonformality and its one-variable consequence')],
    ['prop:native-binary-restrictions'], 'A bounded flat square-zero model has dual-number fibre; its nilpotent cannot map to a nonzero nilpotent in k x k.')
add('M03', 'Thom-Sullivan coefficients carry the actual higher comparison data; ordinary integration is not a strict Alexander-Whitney algebra map.',
    'integrated', [source(C, 'Chapter 11.2, lines 2320-2344'), source(S, 'Section 1')],
    ['thm:native-ordered-collision'], 'The candidate uses the compatible-form commutative model. Its derivative connection is componentwise, and the complex comparison is stated separately.')
add('M04', 'The finite order-chart gluing has one residue-field branch per tuple of equality-block orders.',
    'integrated', [source(C, 'Proposition 12.1, lines 2440-2478'), source(S, 'Sections 1-2')],
    ['prop:native-collision-ran-boundary'], 'The bounded flat Cech fibre decomposes into full simplices indexed by restrictions to equality blocks.')
add('M05', 'On a smooth separated finite-type curve the same order-chart geometry is intrinsic and its coefficient object is a sheaf-level derived pushforward.',
    'integrated', [source(C, 'Section 14.6'), source('/returns/collision_bar_exact_review-final-01.md', 'finding 9')],
    ['thm:native-ordered-collision'], 'Cartier diagonal localizations support a flat connection. The proof constructs the sheaf and its right D-module normalization explicitly.')
add('M06', 'Nested collision substitutions must retain every order face and a declared domain of inverted differences.',
    'integrated', [source(C, 'Sections 15.2-15.3 and 15.7'), source(S, 'Section 3')],
    ['thm:native-ordered-collision'], 'The new zero-scale collision map restricts to lexicographically expanded block charts before repeating coordinates. Only cross-block denominators survive; nested concatenations agree.')
add('M07', 'Finite rational source expressions admit coherent punctured-scale expansions for fixed scale-marked trees.',
    'pending', [source(C, 'Theorems 15.3-15.4, lines 3100-3192'), source(S, 'Sections 3 and 6')], [],
    'Retained complete source and public derivation. This positive theorem concerns punctured scales, distinct from the constructed diagonal pullback.',
    'Construct a comparison between these punctured expansion maps and the zero-scale D-module collision map, including specialization or nearby-cycle data.')
add('M08', 'Arbitrary intermediate Laurent series do not admit unrestricted tree refinement.',
    'refuted-with-proof', [source(C, 'Section 15.6'), source(S, 'Section 3')], [],
    'The series sum(t^n u^(-n^2)) maps under u=delta*a, t=delta*epsilon to terms delta^(n-n^2), which have no uniform lower delta bound. The failed claim is unrestricted refinement, not finite-pole expansion.')
add('M09', 'The omega-weighted finite-state multiplication is an associative dg algebra over its commutative coefficient algebra.',
    'pending', [source(B, 'equation eq:ocb-multiplication and proposition prop:ocb-coefficient-algebra'), source(S, 'Section 4')], [],
    'The original algebra and its bar/dual formulas remain preserved. The new free-word state algebra is a different explicitly declared object.',
    'Supply a nonhorizontal connection or a larger state resolution and prove a carrier-preserving comparison; no identification with the native free-word algebra is asserted.')
add('M10', 'The omega-weighted product can be horizontal while all free state generators remain horizontal.',
    'refuted-with-proof', [source(B, 'eq:ocb-multiplication, considered with the proposed constant state connection')],
    ['prop:native-collision-ran-boundary'], 'The necessary derivation identity fails: derivative_z_i(omega_ij b_ij)=-dq_ij/(z_i-z_j)^2 b_ij is nonzero on an adjacent-exchange edge, while the input derivative is zero.')
add('M11', 'The cohomological adjacent bar face uses b2(sa,sb)=(-1)^|a|s(ab), giving the associator on three inputs.',
    'integrated', [source(B, 'eq:ocb-bar-faces and prop:ocb-bar-square'), source('/returns/recovery_bar_construction-final-01.md', 'full two-sided proof; opposite homological convention explicitly converted')],
    ['thm:native-collision-bar'], 'All disjoint, overlapping and internal terms are treated. Exact parity and noncommutative word checks independently exercise the formulas.')
add('M12', 'The relative augmentation dual computes RHom through a semifree left bar resolution and its convolution lifts.',
    'integrated', [source(B, 'section Why the augmentation dual computes derived endomorphisms')],
    ['thm:native-collision-bar'], 'The candidate supplies the leading-face sign, insertion contraction, semifree induction, and comodule composition interpretation. The category is dg coefficient modules, not horizontal Hom.')
add('M13', 'Positive weight makes the counit cut filtration finite; completed reconstruction must target the completed state algebra.',
    'integrated', [source(C, 'Sections 2.3-2.4, lines 812-888'), source(B, 'thm:ocb-reconstruction')],
    ['prop:native-collision-cobar'], 'The proof includes the gap sign exponent and finite filtration. Completion is the derived inverse limit of finite weight quotients; the free-word target is explicitly completed.')
add('M14', 'Weight completion is degreewise and finite-weight base change precedes limits.',
    'integrated', [source('/returns/bar_chapter_exact_review-final-01.md', 'A008-bar-01'), source('/returns/bar_chapter_exact_review-final-02.md', 'lines 281-334, 463-538, 603-622 of reviewed source'), source(B, 'completion convention')],
    ['prop:native-collision-cobar'], 'The candidate uses degreewise Hom products and derived inverse limits. It makes no pullback/infinite-product interchange.')
add('M15', 'A native finite-power coefficient collision map and a noninjective state merger commute with adjacent ordered bar faces and cuts.',
    'integrated', [source(S, 'Section 9: first missing implication'), source('/returns/collision_bar_exact_review-final-01.md', 'finding 10')],
    ['thm:native-ordered-collision', 'thm:native-collision-bar'], 'The actual morphism Y_J to Y_I and its D-module pullback are constructed. State labels map u_i to u_p(i). The arity-three word square is nonzero before its second differential.',
    'This closes the declared finite-power compatibility step only. It does not identify an arbitrary state system or the omega-weighted algebra with a chiral Ran object.')
add('M16', 'These order-chart coefficient transitions already constitute a Cartesian usual Ran object.',
    'refuted-with-proof', [source(S, 'Sections 8-9, whose scope correctly separates the constructions')],
    ['prop:native-collision-ran-boundary'], 'The binary transition has residue fibre k x k to k, a projection, not an equivalence. This rules out that direct Cartesian identification.',
    'Construct a specified Cartesian replacement and a comparison preserving states, bar operations and all diagonal transitions.')
add('M17', 'Independent binary choices recover every total-order collision without a correction.',
    'refuted-with-proof', [source(C, 'Theorem 12.2 and Section 12.3'), source(S, 'Section 2')], [],
    'At three coincident labels binary choices give eight tournaments; two are directed cycles. Total orders give six. Exact permutation enumeration is retained in check_collisions.py.',
    'The full local-cohomology excision triangle is retained for subsequent integration, not erased by the fibre count.')
add('M18', 'Two complex holomorphic directions have a shifted local-cohomology coefficient and relative nonformality.',
    'pending', [source(O, 'Sections A puncture in the complex plane of dimension two through Specializing to coincidence preserves multiplication')], [],
    'The complete source is preserved. The present native theorem is for a curve and uses its one-dimensional Cartier diagonals.',
    'Compare the two-dimensional coefficient sheaf and its derived transverse restriction to a specified native mixed state operation.')
add('M19', 'The actual half-space mixed configuration maps to the analytic order-chart scheme, with boundary collisions requiring punctured extensions.',
    'pending', [source(C, 'Chapters 13-14')], [],
    'Complete extracted source is retained. A topological coefficient comparison does not create the corresponding state operation.',
    'Supply the analytic/algebraic D-module realization and all bulk-boundary operation maps before importing a mixed action.')
add('M20', 'A scalar residue can replace the full supported principal-parts differential module.',
    'refuted-with-proof', [source(C, 'Sections 11.3-11.5, lines 2348-2400')], [],
    'Residue(x*x^(-2) dx)=1 but x acts by zero on the proposed scalar target, so the residue is not R-linear. The full module has derivative generators with factorial normalizations.')

data = {'status': 'unaccepted source candidate; integrated means implemented, not independently accepted',
        'target': 'A native finite-power ordered collision map with exact bar and cobar compatibility.',
        'items': items,
        'all_preserved_sources': inventory['sources'],
        'public_intermediate_fragments': inventory['public_fragments'],
        'reading_limits': ['Complete load-bearing current TeX proofs were read and independently reconstructed.',
                           'Original C exact lines read include 805-915, 2050-2675, 2790-3320; additional retained source bytes are discovery material.',
                           'Additional matched public fragments and broader returns remain pending where no statement-level disposition above applies.',
                           'The two original extraction files are not duplicates of one another; only identical SHA-256 source occurrences are marked duplicate.'],
        'residual_obligations': ['Independent review of this exact source and PDF.',
                                 'Full Ran/factorization realization and multiplication for chiral convolution.',
                                 'Comparison of free horizontal words with the recovered omega-weighted finite-state algebra.',
                                 'Compatibility with punctured-scale expansions and supported collision residues.',
                                 'Cross-repository propagation through the main integration owner.']}
(HERE / 'mining-dispositions.json').write_text(json.dumps(data, indent=2) + '\n')
print(json.dumps({'statement_dispositions': len(items), 'preserved_source_occurrences': len(inventory['sources']),
                  'preserved_public_fragments': len(inventory['public_fragments'])}))
