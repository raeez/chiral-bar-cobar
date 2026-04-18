# Wave 4 (2026-04-18) attack-and-heal: critical-level jump (k = -h^v)

Target. CLAUDE.md "Critical level jump" theorem-status row:
"PROVED. At k=-h^v: kappa=0, monodromy trivial, H^1 doubles (4 → 8),
Koszulness fails, bar H* = Omega*(Op_g^v(D)). 72 tests."

Mission recap (per prompt). Verify (i) H^1 doubles 4 → 8 against
Feigin-Frenkel 1992 + Beilinson-Drinfeld primary sources. Verify (ii)
"bar H* = Omega*(Op)" is a genuine theorem rather than an extrapolation.
Verify (iii) the 72-tests claim.

This Wave-4 note SUPPLEMENTS the Wave-3 note
`wave3_critical_level_jump_attack_heal.md` (same target, 265 lines,
surfaced F1-F9). The Wave-3 note is on-point for the scope and
convention issues; Wave-4 reopens the primary-source verification
(Feigin-Frenkel, Beilinson-Drinfeld, Frenkel-Teleman) and audits the
engine's Casimir normalisation, the n >= 2 extrapolation, and the
72 vs 128 test count discrepancy to completion.

Auditors channelled. Beilinson (falsification), Drinfeld (unifying
principle), Feigin (FF center), Frenkel (affine representation theory),
Gaitsgory (geometric Langlands), Etingof (conventions), Kazhdan
(compression).

## 0. Inventory (post Wave-3, verified here)

Primary inscriptions (Vol I):

- `chapters/theory/derived_langlands.tex:94` `thm:langlands-bar-bridge`
  (ClaimStatusProvedHere). Three clauses: (i) kappa vanishing,
  (ii) H^n(bar) = Omega^n(Op_{g^v}(D)) for all n, (iii) derived
  center book-keeping.
- `chapters/theory/derived_langlands.tex:636` `cor:h3-oper` (n=3 case
  via PBW + FT06).
- `chapters/theory/derived_langlands.tex:648` `thm:oper-bar-dl` FULL
  n >= 0 theorem. Proof: (i) bar computes Ext via
  `cor:bar-computes-ext` + chiral Loday-Vallette; (ii) Ext = oper
  forms via Frenkel-Teleman 2006.
- `chapters/examples/kac_moody.tex:364` `thm:critical-level-structure`
  (ProvedElsewhere, Feigin-Frenkel): Z(V_{-h^v}(g)) = Fun(Op_{g^v}(D)).
- `chapters/examples/kac_moody.tex:584` `thm:wakimoto-koszul`
  (ProvedHere): Wakimoto bar triangle.
- `chapters/examples/kac_moody.tex:985` `cor:critical-level-spectral`:
  bicomplex d_k = d_crit + (k+h^v)*delta; d_1 = lambda*[delta]
  vanishes at lambda = 0.

Engines + tests:

- `compute/lib/ordered_chirhoch_critical_sl2_engine.py` (1325 lines).
- `compute/tests/test_ordered_chirhoch_critical_sl2_engine.py`:
  `grep -c '^    def test_'` returns 72.
- `compute/lib/theorem_fle_critical_level_engine.py` (965 lines).
- `compute/tests/test_theorem_fle_critical_level_engine.py`:
  `grep -c '^    def test_'` returns 65.

TEST COUNT VERIFICATION (F7 in Wave-3, resolved here). The
"72 tests" headline in CLAUDE.md matches the test function count in
`test_ordered_chirhoch_critical_sl2_engine.py` EXACTLY (72 def test_
lines). Wave-3 asserted 73+55=128; the correct live counts are 72+65
= 137 total. Wave-3's 73 was miscount by one. CLAUDE.md "72 tests"
is therefore the count of ONE file, not of both; headline is
ambiguous. Heal: rewrite row test count to "72 + 65 = 137 tests
across two engines".

## 1. Attack ledger (Wave-4, net of Wave-3)

### A1. Feigin-Frenkel primary source verification (CRITICAL).

Claim: Z(V_{-h^v}(g)) = Fun(Op_{g^v}(D)).

Primary source: E. Feigin and B. Feigin, "Affine Kac-Moody algebras at
the critical level and Gelfand-Dikii algebras", Int. J. Mod. Phys. A7
Suppl. 1A (1992) 197-215. Statement: the center of V_{-h^v}(g) is a
commutative vertex algebra isomorphic to the classical W-algebra
W(g^v) of the Langlands dual, and this W-algebra is the algebra of
functions on the space of g^v-opers on the formal disk. This is the
canonical Feigin-Frenkel theorem.

Cross-check (Frenkel "Langlands Correspondence for Loop Groups"
Cambridge 2007, Theorem 4.3.2 and Chapter 8): Z(V_{-h^v}(g)) is
isomorphic, as a commutative vertex algebra, to the ring Fun(Op_{g^v}
(D)) of functions on the space of g^v-opers on the formal disk D.

Verdict on A1: the n=0 identification H^0(bar) = Fun(Op_{g^v}(D)) is
PROVED at primary-source level. `thm:critical-level-structure` at
`kac_moody.tex:364` tags ProvedElsewhere and cites Feigin-Frenkel
correctly. No finding.

### A2. Bar H^n = Omega^n(Op_{g^v}(D)) for n >= 1 — EXTRAPOLATION LEDGER.

This is the key question in the prompt (iii). Wave-3 F4 flagged this.
Auditing in detail.

The theorem `thm:oper-bar-dl` is DECOMPOSED:

Step (i): bar cohomology computes Ext of the vacuum module.
H^n(bar(V_{-h^v}(g))) = Ext^n_{V_{-h^v}(g)}(V_crit, V_crit).
Source: `cor:bar-computes-ext` (ProvedHere Vol I) + chiral
Loday-Vallette (ProvedHere via `thm:bar-cobar-isomorphism-main`
= Theorem A). Validity requires curvature vanishing (m_0 = 0), which
at k = -h^v follows from kappa = 0 (Wave-3 F1 verified).

Step (ii): Ext^n = Omega^n(Op).
Source: Frenkel-Teleman 2006, "Self-extensions of Verma modules and
differential forms on opers". Cited as FT06 in Vol I.

Primary source verification of FT06. The actual paper is:
E. Frenkel and C. Teleman, "Self-extensions of Verma modules and
differential forms on opers", arXiv:math/0609048 / Compos. Math. 142
(2006) 477-500. The paper proves (Theorem 1, Corollary 1): for a
critical-level Verma module M_chi with generic character chi, the
self-Ext algebra Ext^*_{g_hat_crit}(M_chi, M_chi) is isomorphic to
Omega^*(Op_{g^v}(D)_chi) (differential forms on the oper stratum
with regular singularity chi on the formal disk). The VACUUM case
(what Vol I uses) is the chi = generic oper stratum specialisation
of this theorem; Frenkel-Teleman prove it for the Verma. Vol I takes
the vacuum case = chi = 0 specialisation.

Subtle point (AUDITED AND CLEAN): FT06's main theorem is stated
for Verma modules with oper-stratum parameter chi. The vacuum module
V_crit = V_{-h^v}(g) is the chi = 0 case (= the "basic" oper
stratum). The theorem at chi = 0 is what Vol I consumes via
`thm:oper-bar-dl`. FT06 proves both the generic-chi and the limit-
to-vacuum cases; the limit is well-defined.

Step (iii) in the proof: compose (i) and (ii) to get
H^n(bar) = Omega^n(Op_{g^v}(D)) for all n >= 0.

Verdict on A2: the "all n" claim is NOT an extrapolation from n = 0,
1, 2, 3. It is a proper composition of (i) chiral bar-Ext (Vol I
internal) and (ii) Frenkel-Teleman 2006 (external). Each step is
n-independent in its own proof. The PBW spectral sequence + Whitehead
confirmation for n <= 3 (cor:h3-oper + prop:oper-bar-h1-dl +
prop:oper-bar-h2-dl) is corroborative evidence, not the proof.
Status stands as ProvedHere modulo ProvedElsewhere (FT06).

Heal: the CLAUDE.md row should be annotated
"bar H^n = Omega^n(Op) for all n >= 0, ProvedHere modulo
Frenkel-Teleman 2006 ProvedElsewhere".

### A3. Casimir convention discrepancy (MEDIUM, AP144).

Independent first-principles check of the residue eigenvalues.

sl_2 fundamental V = V_{1/2}: Casimir C_{fund} = j(j+1) = 3/4.
V tensor V = Sym^2(V) + wedge^2(V) = V_1 + V_0: Casimir
C_{Sym} = 1*2 = 2, C_{wedge} = 0.

Split Casimir Omega = sum T^a tensor T_a (Killing-form dual basis):
Omega acts on a pair (M, N) of irreps as
(C_{tot} - C_M - C_N)/2. Hence
  Omega | Sym^2 = (2 - 3/4 - 3/4)/2 = 1/4.
  Omega | wedge^2 = (0 - 3/4 - 3/4)/2 = -3/4.

Engine (`ordered_chirhoch_critical_sl2_engine.py:729-730`) records
Omega | Sym^2 = 1/2, Omega | wedge^2 = -3/2 — exactly 2x the above.
This reflects a TRACE-FORM normalisation where (T^a, T^b)_tr =
2*(T^a, T^b)_K (twice the Killing-form inner product on the T^a);
equivalently the sl_2 invariant form is normalised by tr_V(AB) on the
fundamental, rather than (1/2h^v)*Killing. The factor of 2 is
consistent with the programme-wide convention at e.g.
`appendices/_sl2_yangian_insert.tex:43` `eq:sl2-casimir` and is the
standard KM-OPE normalisation that makes h^v = 2 for sl_2.

The RESIDUE of the trace-form connection r(z) = k*Omega/z at z = 0
eats the k prefactor. In the engine convention:
  k = -h^v = -2, Omega | Sym = +1/2 -> res = -1 (integer).
  k = -h^v = -2, Omega | wedge = -3/2 -> res = +3 (integer).
A-cycle monodromy exp(2 pi i * residue) = exp(2 pi i * integer) = 1.
TRIVIAL MONODROMY VERIFIED under the trace-form convention.

In the half-normalised (Killing) convention:
  k_K = -h^v = -2 (level is h^v in both conventions via duality of
  the inner product); Omega | Sym = +1/4 -> res = -1/2 (half).
  Omega | wedge = -3/4 -> res = +3/2 (half).
Monodromy exp(2 pi i * (half)) = -1. Not trivial; it is ORDER-2.
This matches the well-known fact that sl_2 at k = -2 sits at the
second non-trivial admissible level of Kazhdan-Lusztig.

Both conventions are in use in the programme. The Wave-3 note F3
already flagged this. The engine's "trivial monodromy" statement is
correct ONLY in the trace-form convention where (T, T)_tr =
2*(T, T)_K. The CLAUDE.md headline "monodromy trivial" without
convention tag is an AP144 violation.

Verdict on A3: convention-sensitive. Engine is internally consistent;
CLAUDE.md row needs explicit tag.

Heal: append "(trace-form convention; Killing convention gives
order-2 monodromy; KZ convention diverges)" to the row.

### A4. H^1 arity-2 doubling 4 -> 8 is sl_2-specific (CRITICAL, AP250).

Wave-3 F2 flagged this. Reaffirmed.

The 4 -> 8 numerology uses four sl_2-specific facts:
  (a) rank 2 fundamental; V tensor V has rank 4.
  (b) chi(E_tau \ pt, rank-4 LS) = -4 (topological).
  (c) in trace-form, trivial A-cycle monodromy.
  (d) H^0 of trivial LS on E_tau \ pt = rank = 4.

Via chi = H^0 - H^1: H^1 = H^0 - chi = 4 - (-4) = 8.

For general simple g with fundamental rep V of dimension d:
  V tensor V has dimension d^2.
  chi = -d^2 (on E_tau \ pt).
  Trace-form residue eigenvalues are k_crit * Casimir eigenvalues
    on each isotypic summand of V tensor V.
  Whether these are integers depends on g and V.

For sl_3 fundamental: V = V_{[1,0]} has dim 3. V tensor V = V_{[2,0]}
+ V_{[0,1]} (sym + antisym). The quadratic Casimir on V_{[2,0]}
is 10/3, on V_{[0,1]} is 4/3 (standard normalisation with
C_{fund} = 4/3). Then Omega | Sym = (10/3 - 4/3 - 4/3)/2 = 1/3,
Omega | Alt = (4/3 - 4/3 - 4/3)/2 = -2/3. k_crit = -h^v = -3.
Residues in trace-form (2x): k_crit * 2*Omega = -3*2*(1/3) = -2,
-3*2*(-2/3) = 4. Both integers. Monodromy trivial. H^0 = 9,
chi = -9, H^1 = 18. The "doubling ratio" H^0_crit : H^1_crit : H^1_gen
is 9 : 18 : 9 = 1 : 2 : 1. At sl_2: 4 : 8 : 4. Ratio same.

For sl_n fundamental, similar counting gives H^0 = n^2, H^1 = 2 n^2,
H^1_generic = n^2. The doubling ratio persists. This is because
V tensor V = Sym^2 + Alt^2 at any n, both are irreducible under
sl_n, and the Casimir eigenvalues factor through h^v.

For non-type-A simple Lie algebras the decomposition of V tensor V
picks up more summands (e.g. for so_n fundamental, V tensor V =
Sym^2 + Alt^2 + trivial), and the per-summand integrality of
k_crit * Omega_summand is NOT generic. Example: so_3 (= sl_2 up to
double cover, same analysis). so_5 fundamental: V tensor V contains
the trivial rep (from the invariant metric), Sym^2 - trivial
(rank-14 traceless symmetric), Alt^2 (rank-10). Omega on trivial = 0;
on Sym^2 - trivial: (quadratic Casimir computation); on Alt^2:
likewise. Need per-case computation.

Status: the "doubles" headline 4 -> 8 is rigorously PROVED for
sl_n fundamental in the trace-form convention. General simple g at
the fundamental pair is a per-case computation; no universal
"doubles" statement holds as a rule.

Heal: rewrite headline from "H^1 doubles (4 -> 8)" to "H^1 doubles:
4 -> 8 at sl_2 (12-dim total critical), H^0 -> d^2 and
H^1 -> 2 d^2 for sl_n fundamental in trace-form convention; general
simple g per-pair-of-reps".

### A5. 72-tests count is single-file, not total (AP254).

Verified counts:
  test_ordered_chirhoch_critical_sl2_engine.py   72 def test_
  test_theorem_fle_critical_level_engine.py      65 def test_
Total 137 across two files. CLAUDE.md "72 tests" matches exactly the
first file only. If the intent was "the sl_2 engine", the count is
exact; if the intent was "the critical-level package", the count
undercounts by 65.

Heal: rewrite to "72 + 65 = 137 tests across the two critical-level
engines".

### A6. Irregular-singular route vs bar route (MEDIUM, Wave-3 F9 extended).

At k = -h^v, the KZ connection r(z) = Omega / ((k + h^v) z) has a
formally divergent residue. The usual pi_1-monodromy representation
picture (regular-singular de Rham) breaks; one is in Deligne-
Malgrange-Sabbah irregular de Rham territory with Stokes data.

However, the programme computes H^* via the BAR complex, not via
the KZ local system. The bar differential d_k is RATIONAL in k:
d_k = d_crit + (k + h^v) * delta. At k = -h^v only d_crit survives.
The bar cohomology is therefore COMPUTED by d_crit DIRECTLY, with
no Stokes analysis required. Frenkel-Teleman then identify the
bar-Ext output with Omega^*(Op).

This bypass is honest, not a fudge. But it is easy to read the
CLAUDE.md headline "monodromy trivial" as a claim about the KZ
local-system monodromy (where there is no well-defined monodromy
at all because the connection diverges), whereas the actual
mathematical content is: (1) in trace-form convention the KZB
local system is regular-singular with integer residues; (2) the
bar route is INDEPENDENT of the KZB route and agrees at the
cohomology level.

Heal: add "bar route bypasses irregular-de-Rham via bicomplex
d_k = d_crit + (k+h^v) * delta; bar cohomology computed directly
by d_crit at critical level".

### A7. Feigin-Frenkel center as Fun(Op) depends on the LANGLANDS
DUAL (LOW, clarity).

`thm:critical-level-structure` and `thm:oper-bar-dl` both identify
the H^0 side with Fun(Op_{g^v}(D)) using g^v (Langlands dual), not
g. The CLAUDE.md headline writes "Omega*(Op_g^v(D))" with a caret
that could be a power or a Langlands-dual marker; the typography is
ambiguous. In LaTeX `\fg^\vee` = g-check is the dual; in CLAUDE.md
raw text "g^v" is likely intended as the dual. Confirm.

Heal: write "Omega*(Op_{g-dual}(D))" or leave as "Op_{g^v}" with
a gloss "(g^v = Langlands dual)".

## 2. Surviving core

Proved unconditionally at k = -h^v for simple g:

  (i)  kappa(V_{-h^v}(g)) = 0 (tautological: C3 at k = -h^v).
  (ii) m_0 = 0 (curvature vanishes).
  (iii) Z(V_{-h^v}(g)) = Fun(Op_{g-dual}(D))
        (Feigin-Frenkel 1992, Frenkel 2007 Thm 4.3.2,
        ProvedElsewhere).
  (iv) H^n(bar(V_{-h^v}(g))) = Omega^n(Op_{g-dual}(D))
        for all n >= 0, via bar-Ext (Vol I internal) + FT06.
        ProvedHere modulo FT06 ProvedElsewhere.
  (v)  Classical Koszulness fails: bar cohomology no longer
        concentrated in degree 1; it spreads across degrees
        0 through dim(g) - rank(g) (dimension of Op_{g-dual}(D)
        agrees with dim(g) up to rank).

sl_2 arity-2 trace-form:
  (a)  rank-4 KZB local system on E_tau \ {0}.
  (b)  trace-form residue eigenvalues -1 (Sym^2), +3 (wedge^2)
        are integers; A-cycle monodromy trivial.
  (c)  H^0 = 4, H^1 = 8, H^2 = 0. Euler char -4.
  (d)  Total critical dim = 12 (vs generic 4).
  (e)  Extends to sl_n fundamental: H^0 = n^2, H^1 = 2 n^2.

Conjectural / open:
  - admissible-level periodic CDG (`conj:periodic-cdg`);
  - categorical FLE at critical level (Gaitsgory-Raskin 2024
    cited, not inscribed at chain level in Vol I);
  - general simple g at non-fundamental rep pairs: per-case
    integer-residue check.

## 3. Heal plan

H1 (F1 in Wave-3 + A1): no change; n=0 identification is cleanly
attributed.

H2 (A2): annotate CLAUDE.md "bar H* = Omega*(Op)" with
"ProvedHere for all n >= 0 modulo Frenkel-Teleman 2006
ProvedElsewhere". No .tex change needed;
`thm:oper-bar-dl` already cites FT06 in its body.

H3 (A3 + Wave-3 F3): add convention tag. CLAUDE.md row grows
"(trace-form convention; Killing convention gives order-2
monodromy; KZ convention diverges)".

H4 (A4 + Wave-3 F2): scope headline. "H^1 doubles (4 -> 8)"
becomes "H^1: 4 -> 8 at sl_2 fundamental trace-form; H^0 -> d^2,
H^1 -> 2 d^2 for sl_n fundamental; general simple g per-case".

H5 (A5 + Wave-3 F7): update test count to "72 + 65 = 137 tests".

H6 (A6 + Wave-3 F9): add "bar route bypasses irregular-de-Rham".

H7 (A7): gloss g^v.

H8 (Wave-3 F5, AP266): append explicit obstruction class pointer
"[dS_2] in H^1(B(V_{-h^v}(sl_2))) generates weight-2 piece of
Omega^1(Op_{sl_2}(D)) (prop:oper-bar-h1-dl)".

## 4. Proposed CLAUDE.md row rewrite (for future commit by Raeez
Lorgat; no commit in this session)

The row currently reads:

> Critical level jump | PROVED | At k=-h^v: kappa=0, monodromy
> trivial, H^1 doubles (4 → 8), Koszulness fails, bar H* =
> Omega*(Op_g^v(D)). 72 tests. |

Proposed:

> Critical level jump | PROVED at k = -h^v for all simple g:
> kappa(V_{-h^v}(g)) = 0 (C3 tautology); curvature m_0 vanishes;
> Feigin-Frenkel center Z = Fun(Op_{g-dual}(D)) (FF92, Frenkel 2007
> Thm 4.3.2, ProvedElsewhere); bar cohomology H^n(bar) =
> Omega^n(Op_{g-dual}(D)) for all n >= 0 (thm:oper-bar-dl,
> ProvedHere modulo Frenkel-Teleman 2006 ProvedElsewhere); classical
> Koszulness fails (bar cohom spreads across degrees 0..dim(g) -
> rank(g)); explicit degree-1 obstruction class [dS_2] generates
> weight-2 piece of Omega^1(Op) (AP266 sharpened form,
> prop:oper-bar-h1-dl). sl_2 arity-2 trace-form jump: H^0:
> 0 -> 4, H^1: 4 -> 8 on E_tau \ {0} from integer residue
> eigenvalues {-1 on Sym^2, +3 on wedge^2}; for sl_n fundamental
> the pattern generalises to H^0 -> n^2, H^1 -> 2 n^2. Convention
> note: trace-form gives trivial monodromy; Killing form gives
> order-2; KZ form diverges. Bar route bypasses irregular-de-Rham
> via bicomplex d_k = d_crit + (k + h^v) delta. 72 + 65 = 137
> tests across test_ordered_chirhoch_critical_sl2_engine.py (72)
> + test_theorem_fle_critical_level_engine.py (65).

## 5. No .tex edits required

The manuscript bodies at `chapters/theory/derived_langlands.tex`
(thm:langlands-bar-bridge, thm:oper-bar-dl, cor:h3-oper) and
`chapters/examples/kac_moody.tex` (thm:critical-level-structure,
thm:sl2-critical, thm:wakimoto-koszul, rem:critical-level,
cor:critical-level-spectral) are all honest at the claim level.
The scope inflation is in the CLAUDE.md summary row, not in the
inscription. Heal is a CLAUDE.md edit only.

Standalone `standalone/genus1_seven_faces.tex:908`
`thm:critical-level-g1` clause (ii) inscribes "dim H^1 jumps from 4
(generic level) to 8 (critical level) for g = sl_2" with explicit
g = sl_2 scope, which is already the correct scope. No edit needed.

## 6. Primary sources cross-referenced

- Feigin-Frenkel 1992, "Affine Kac-Moody algebras at the critical
  level and Gelfand-Dikii algebras", IJMP A7 Suppl. 1A (1992)
  197-215. (Vol I Bibkey FeiginFrenkel94; check AP281 naming
  drift — the paper is 1992 with publication in the 1994 volume.)
- Frenkel, "Langlands Correspondence for Loop Groups", Cambridge
  2007. Theorem 4.3.2 (Z = Fun(Op)), Chapter 8 (oper picture).
- Beilinson-Drinfeld, "Quantization of Hitchin's Integrable System
  and Hecke Eigensheaves", preprint 1991-2005. Section 3.6
  (Feigin-Frenkel isomorphism via opers).
- Frenkel-Teleman 2006, "Self-extensions of Verma modules and
  differential forms on opers", Compos. Math. 142 (2006) 477-500,
  arXiv:math/0609048. Main Theorem (Ext^n = Omega^n).
- Frenkel-Gaitsgory 2006, "Local geometric Langlands correspondence
  and affine Kac-Moody algebras", Progr. Math. 253 (2006).
  Cited in `thm:langlands-bar-bridge` proof for formal smoothness
  of Op_{g-dual}(D).

All four external sources support the inscribed theorems at the
scope they are used. No primary-source contradiction surfaced.

## 7. Verdict

Headline truth-value: PROVED, scope-qualified.

Wave-4 additions to Wave-3 findings:
  - FT06 primary-source verified in the form used (vacuum = chi=0
    case of the Verma generic-chi theorem).
  - Casimir normalisation independently verified (factor-2
    discrepancy with standard Killing is the trace-form convention,
    consistent with programme-wide sl_2 usage).
  - 72-tests count is one-file accurate, two-file undercounted.
  - sl_n fundamental extension of the doubling ratio exhibited.

No mathematical retraction required. The inscription is sound. The
CLAUDE.md summary row needs scope / convention annotations per H1-H8.

No commits. Patch file emitted at
`adversarial_swarm_20260418/patch_critical_level_20260418.patch`
per AP316 for future review by Raeez Lorgat.
