# Wave 3 attack-and-heal: critical-level jump (k = -h^v)

Target. CLAUDE.md "Critical level jump" theorem-status row:
"PROVED. At k=-h^v: kappa=0, monodromy trivial, H^1 doubles (4 → 8),
Koszulness fails, bar H* = Omega*(Op_g^v(D)). 72 tests."

Auditors channelled. Etingof (quantum-group conventions), Kazhdan
(compression), Beilinson (falsification), Gelfand (inevitability),
Frenkel (FF center), Feigin (Koszulness), Witten (physical scope).

## 0. Where the claim lives

Inscription:
- `chapters/examples/kac_moody.tex`
 - `thm:critical-level-structure` (line 364, ProvedElsewhere on
 Feigin-Frenkel): Z(g_hat_{-h^v}) = Fun(Op_{g^v}(D)).
 - `rem:critical-level` (line 485): Sugawara undefined,
 center infinite-dimensional, curvature m_0 vanishes.
 - `thm:sl2-critical` (line 639, ProvedElsewhere): sl_2
 specialisation.
 - `thm:wakimoto-koszul` (line 584, ProvedHere): Wakimoto bar
 triangle at critical level.
 - `cor:critical-level-spectral` (line 985): bicomplex spectral
 sequences with d_1 = (k+h^v)*delta.
- `chapters/theory/derived_langlands.tex`
 - `thm:langlands-bar-bridge` (line 94, ProvedHere): the
 statement linking bar cohomology to oper forms.
 - `thm:oper-bar-dl` (line 648, ProvedHere): H^n(B) =
 Omega^n(Op) for all n.
 - `cor:h3-oper` (line 636): n = 3 case via PBW + FT06.
- Engines + tests:
 - `compute/lib/ordered_chirhoch_critical_sl2_engine.py` (1325 lines)
 - `compute/tests/test_ordered_chirhoch_critical_sl2_engine.py`
 (846 lines, ~73 test functions)
 - `compute/lib/theorem_fle_critical_level_engine.py` (965 lines)
 - `compute/tests/test_theorem_fle_critical_level_engine.py`
 (872 lines, ~55 test functions)

Total ~128 test functions across the two files (the "72 tests" in
CLAUDE.md undercounts; cf. AP254 / AP280).

## 1. Attack ledger

### F1 (HIGH, AP1 / HZ-4 / AP-KAPPA conflation).
CLAUDE.md row reads "kappa=0" unqualified. Correct statement:
kappa(V_{-h^v}(g)) = dim(g) * (k + h^v) / (2 h^v) = 0 at k = -h^v
for every simple g. The vanishing is a definitional consequence of
the Sugawara shift, not an independent theorem. Not a violation per
se; just deserves the tag "kappa vanishes as a consequence of
kappa = dim(g)(k + h^v)/(2 h^v)".

### F2 (CRITICAL, AP250 / AP239 algorithm-uniformity + naming).
"H^1 doubles (4 → 8)" is an AFFINE sl_2 statement for V ⊗ V (two
punctures on E_tau). The engine at `ordered_chirhoch_critical_sl2_engine.py:680-720`
derives this from:
(a) rank-4 local system on E_tau \ {0} with fundamental rep V ⊗ V;
(b) trace-form connection r(z) = k*Omega/z at k = -2 has residue
eigenvalues {-1, +3} (integers) on Sym^2(V) resp. Lambda^2(V);
(c) A-cycle monodromy exp(2 pi i * integer) = 1; hence H^0 = 4;
(d) chi(E_tau \ {0}, V ⊗ V) = -4, so H^1 = 8 via Euler.

The 4 → 8 doubling is sl_2-on-V⊗V-specific. For general simple g
at arity 2 on V_fund ⊗ V_fund, the residue eigenvalues of
k_crit * Omega_tr = -h^v * Omega_tr are NOT generically integers.
Example: sl_3 fundamental, Omega_tr on V_3 ⊗ V_3 has eigenvalues
4/3 (sym) and -2/3 (alt) in a natural normalisation; residue
eigenvalues = -h^v * {4/3, -2/3} = {-4, +2} after multiplication
by h^v = 3. Integers in that case. But for sl_n fund ⊗ fund the
pattern is n-dependent and the CLAUDE.md entry is not quantified.

Severity: statement-level scope inflation. CLAUDE.md presents "4 → 8"
as a universal signature of the critical-level jump; it is affine
sl_2 on V ⊗ V only.

### F3 (MEDIUM, AP144 / FM4 convention caveat missing).
Engine derivation of H^1 = 8 uses trace-form convention r(z) =
k*Omega/z, precisely because the KZ convention
r(z) = Omega/((k + h^v) z) DIVERGES at k = -h^v. Engine docstring
lines 722-727 flag this honestly. CLAUDE.md row does not. Without
the convention tag, "monodromy trivial, H^1 doubles 4 → 8" reads
as convention-free. This is a classic AP144 (bridge-identity needed
per site) + FM4 (k=0 vs k=-h^v boundary care).

### F4 (HIGH, AP272 folklore-citation / AP250 algorithm-uniformity).
"Koszulness fails" at k = -h^v is stated as proved. The inscription
chain is: kappa = 0 + H^0(B) jumps from C to Fun(Op) (infinite-dim)
⟹ bar cohomology no longer concentrated in degree 1 ⟹ classical
Koszulness criterion fails. The first implication is immediate;
the second hinges on `thm:oper-bar-dl` = `thm:langlands-bar-bridge`.
Proof of `thm:oper-bar-dl`:
 (i) bar computes Ext (ProvedHere, via Cor. bar-computes-ext +
 chiral Loday-Vallette);
 (ii) Ext = oper forms (Frenkel-Teleman 2006, ProvedElsewhere).
Step (ii) is cited at citation level to Frenkel-Teleman "Self-
extensions of Verma modules..." - the single external dependency
is load-bearing. AP272 discipline: grep the Vol I bibliography for
FT06; verify the cited result matches the form used here (it does,
but the citation density for "Koszulness fails at k=-h^v" reduces
to ONE external paper). Status: adequate under HZ-11 Option (b)
ProvedElsewhere attribution; but CLAUDE.md "PROVED" obscures the
external dependency.

### F5 (LOW-MEDIUM, AP266 obstruction-class sharpening opportunity).
"Koszulness fails" is stated as a negative. AP266 discipline
recommends EXHIBITING the obstruction class explicitly. The
obstruction here is the nontrivial class
 [dS_2] in H^1(B(V_{-h^v}(sl_2)))
generating the weight-2 piece of Omega^1(Op_{sl_2}(D)) =
C[S_2] * dS_2. `prop:oper-bar-h1-dl` inscribes this. A CLAUDE.md
pointer to the explicit generating class would upgrade the "fails"
statement to a sharpened frontier item (Beilinson falsification
handle: any alternative Koszul-dual construction at k = -h^v must
reproduce [dS_2] as the generator of its degree-1 bar cohomology).

### F6 (MEDIUM, AP280 three-step epistemic inflation).
"H^1 doubles (4 → 8)" headline rests on `test_H1_arity2_critical`
at `test_ordered_chirhoch_critical_sl2_engine.py:465-475`. The test
body asserts `arity2.critical_dim == 12` only; H^1 = 8 is derived
INSIDE the engine via chi constraint, not independently cross-
checked. Two-path verification would be:
 Path A (engine): chi(E_tau \ {0}) * rank = -4, plus H^0 = 4 from
 trivial monodromy, gives H^1 = 8.
 Path B (disjoint): direct de Rham computation of Omega^1(E \ {0},
 V ⊗ V) with trace-form connection, or Whitehead spectral sequence
 at arity 2.
Path B is not inscribed in either test file. Engine + test share
the same mental model (chi constraint on punctured E_tau). AP128
engine-test synchronisation risk is present but low (chi is
topological, independent of the mechanism producing H^0 = 4).

### F7 (MEDIUM, AP254 closure-count drift).
CLAUDE.md says "72 tests"; actual `def test_` count across the two
critical-level test files is approximately 73 + 55 = 128. The
"72" is stale; either it counts one file only or it is a legacy
figure from before expansions. Not load-bearing for mathematics,
but the discipline requires accurate counts (AP254).

### F8 (spot-check, no HZ-IV findings at surface level).
Three largest tests spot-checked
(`test_H1_arity2_critical` :465,
 `test_H0_arity2_critical` :426,
 `test_critical_limit_monodromy` :444):
each asserts a concrete numerical value (12, 4, True/4/8) computed
by engine functions. No `assert True` / `assert_sources_disjoint`
HZ-IV decorator tautologies surface. `test_ff_center_generating_function_sl2`
(test_theorem_fle_critical_level_engine.py:687) computes FF
generating function from exponents at two independent call sites
and compares. Looks legitimate. No AP277 / AP287 / AP288 vacuous-
decorator alerts at surface scan (deeper scan would require reading
all 128 bodies; deferred).

### F9 (LOW, irregular-de-Rham caveat).
Engine lines 60-74 honestly record that at k = -h^v the KZ connection
is IRREGULAR (Stokes phenomenon); Deligne-Malgrange-Sabbah irregular
de Rham theory is then required. The bar-complex route bypasses
this by passing through the bicomplex decomposition
d_k = d_crit + (k + h^v) * delta, with only d_crit surviving at
k = -h^v. Bar route is not a "solution" to the irregular-de-Rham
problem; it is a DIFFERENT computation that agrees cohomologically.
CLAUDE.md row does not mention the irregular-singularity subtlety;
the bar route is clean, but a reader expecting KZB monodromy
analysis gets something else.

## 2. Surviving core (Drinfeld-style)

What is proved unconditionally at k = -h^v for a simple Lie algebra g
with dual Coxeter number h^v:
 (i) kappa(V_{-h^v}(g)) = 0 (tautological, Sugawara shift);
 (ii) the curvature m_0 = (k + h^v)/(2 h^v) * Casimir vanishes;
 (iii) Feigin-Frenkel center enlarges to Fun(Op_{g^v}(D))
 (Feigin-Frenkel 1992, ProvedElsewhere);
 (iv) bar cohomology acquires degrees 0 through
 dim(g) - rank(g), identified with the oper differential-form
 package Omega^*(Op_{g^v}(D)) via bar-Ext + Frenkel-Teleman
 (`thm:oper-bar-dl`, ProvedHere at the chain level modulo FT06);
 (v) classical Koszulness (bar cohom concentrated in degree 1)
 fails at k = -h^v for every simple g.

What is affine-sl_2-specific (NOT universal):
 - the numerical jump H^0: 0 → 4, H^1: 4 → 8 at arity 2 on
 E_tau \ {0} in the trace-form convention;
 - the trivial monodromy of the A-cycle (integer residue
 eigenvalues);
 - the "total dim doubles from 4 to 12" headline.

What remains conjectural:
 - admissible-level periodic CDG (`conj:periodic-cdg`);
 - full categorical FLE (Gaitsgory-Raskin 2024 cited, not inscribed
 at the chain level).

## 3. Heal plan per finding

F1: inline annotation in CLAUDE.md row reading kappa via C3/HZ-4
 formula. Status tag: ACCEPT (no status change).

F2: rewrite CLAUDE.md row header from "H^1 doubles (4 → 8)" to
 "H^1 arity-2 trace-form jump 4 → 8 inscribed for affine sl_2
 fundamental on E_tau \ {0}; general simple g is per-pair-of-reps".
 Status tag: SCOPE CORRECTION (no mathematics changes; headline
 scope aligned to inscription scope).

F3: append "(trace-form convention; KZ convention diverges)" to
 the monodromy-trivial headline. Status tag: ACCEPT.

F4: rewrite "Koszulness fails" as "classical Koszulness fails
 (bar cohom spreads across degrees 0..dim(g)-rank(g));
 `thm:oper-bar-dl` ProvedHere modulo Frenkel-Teleman 2006".
 Status tag: ATTRIBUTION (HZ-11 Option b discipline made visible).

F5: add obstruction-class pointer: "explicit degree-1 obstruction
 class [dS_2] in H^1(B(V_{-h^v}(sl_2))) generates C[S_2] * dS_2
 = Omega^1(Op_{sl_2}(D)) weight-2 piece (prop:oper-bar-h1-dl).
 AP266 sharpened form."
 Status tag: SHARPENED FRONTIER.

F6: no test-level change required; the chi-constraint mechanism is
 mathematically correct. Flag for future Wave: inscribe a disjoint
 Whitehead-spectral-sequence verification of H^1 = 8 at arity 2
 (AP128 synchronisation insurance). Status tag: FRONTIER HZ-IV
 queue item.

F7: update "72 tests" to accurate count. Suggested Bash:
 `grep -c '^    def test_' compute/tests/test_ordered_chirhoch_critical_sl2_engine.py`
 +
 `grep -c '^    def test_' compute/tests/test_theorem_fle_critical_level_engine.py`
 then set CLAUDE.md to the sum.
 Status tag: ACCEPT (book-keeping only).

F8: no change required at this audit scope.

F9: append "(bar route bypasses irregular-de-Rham via bicomplex
 decomposition d_k = d_crit + (k + h^v) * delta)" to the CLAUDE.md
 row. Status tag: ACCEPT.

## 4. Inscription plan (no commits without separate sign-off)

Proposed CLAUDE.md "Critical level jump" row rewrite
(for a future commit by Raeez Lorgat):

> Critical level jump | PROVED at k=-h^v for all simple g:
> kappa = dim(g)(k+h^v)/(2h^v) = 0; curvature m_0 vanishes;
> Feigin-Frenkel center enlarges to Fun(Op_{g^v}(D))
> (FF92, ProvedElsewhere); bar cohomology
> H^n(B) = Omega^n(Op_{g^v}(D)) for all n (thm:oper-bar-dl
> ProvedHere modulo Frenkel-Teleman 2006); classical
> Koszulness fails (bar cohom no longer concentrated in degree 1);
> explicit degree-1 obstruction class [dS_2] generating the
> weight-2 piece of Omega^1(Op) (AP266 sharpened form). Affine
> sl_2 arity-2 trace-form jump: H^0: 0 → 4, H^1: 4 → 8 on
> E_tau \ {0} from A-cycle monodromy trivialisation
> (integer residue eigenvalues -1 on Sym^2, +3 on Lambda^2);
> convention-dependent (KZ connection diverges, bar route via
> bicomplex d_k = d_crit + (k + h^v) delta bypasses irregular
> de Rham). ~128 tests across
> test_ordered_chirhoch_critical_sl2_engine.py (73) +
> test_theorem_fle_critical_level_engine.py (55).

No .tex edits are required to heal the inscription; the
manuscript body is already accurate at the relevant theorem
statements. Only the CLAUDE.md summary row needs the scope /
convention qualifiers.

No commits planned; this note is the scoping ledger for a
future CLAUDE.md edit batched with Wave 3 rectifications.
