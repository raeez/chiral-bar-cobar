Attack-heal note: B85 "Orbifold route: Z/n-invariants preserves E_n structure"
Author: Raeez Lorgat
Date: 2026-04-18

## Attack

B85 (Vol I CLAUDE.md line 487) is written as a BARE SLOGAN:

  "B85. Orbifold route: Z/n-invariants preserves E_n structure."

Unlike every other Blacklist entry B1-B84 and B86-B94, B85 has no
`BAD -> CORRECT` healing arrow and no explicit FORBIDDEN form. It
sits in the Blacklist section (ostensibly a list of forbidden
patterns) but reads ambiguously as a slogan that could be either
endorsed or retracted depending on the reader. The Vol II
Part VI climax (`thm:monster-orbifold-e3` at
`chapters/connections/3d_gravity.tex:7107-7203`), the Vol II
AGENTS.md line 110, and the Vol II CLAUDE.md FM120 (line 480) all
depend on an interpretation of this slogan, but in three different
ways. The slogan as written is underdetermined.

## First-principles analysis

Four distinct statements have been compressed into the B85 slogan,
with markedly different truth values:

(S1) Trivial-action invariants. If a finite group G acts trivially
on an E_n-algebra A in a G-equivariant ambient, then A^G = A is
trivially E_n. Lurie HA 5.1.2.2 in the G-equivariant category.
This is tautological and not the content of the orbifold route.

(S2) Nontrivial-action invariants, underlying algebra only.
If G acts nontrivially on an E_n-algebra A (say a VOA), then the
invariant subalgebra A^G carries a VOA structure (Dong-Mason 1997,
Miyamoto). This is the CFT-level orbifold theorem and says nothing
about E_n-topological enhancement.

(S3) Nontrivial-action G-gauging preserving E_n-topological. If
A is E_n-topological (in the programme sense: E_2-chiral tensor
E_{n-2}-topological via Sugawara), G acts on A via
E_n-equivariant BV data, and the Dijkgraaf-Witten class
alpha_G in H^{n+1}(BG, U(1)) vanishes, then the G-gauged bulk
theory is E_n-topological and its boundary is A // G. This is
the content of the Vol II Monster theorem
(`thm:monster-orbifold-e3`), specialised to G = Z/2, n = 3,
A = V_Lambda (Leech lattice VOA).

(S4) Unconditional "Z/n-invariants preserves E_n" slogan. FALSE
in general. Vol II FM120 documents this: finite-group invariants
in the sense of Lurie HA 5.1 covers (S1) and (in a restricted
form) the untwisted sector V_Lambda^+ of (S3), but does not
cover the twisted sector V_Lambda^{tw,+}. The full V^natural
construction requires orbifold BV gauging with explicit anomaly
cancellation, not bare invariants.

The user's prompt raised a secondary question: is H^{Z/2} = Vir at
c = 1 an example of (S3)? No. The standard "Heisenberg / Vir at
c = 1" identification is NOT Z/2 invariants of H; it is the
lattice-rank-1 orbifold sector V_{sqrt(2)Z} / Z/2 which
contains a copy of a Virasoro module (Dong-Griess-Mason
discriminant lattice). "Symmetric fermion Z/2 orbifold = Vir at
c = 1/2 (Ising)" is the correct physics example; it is an
instance of (S3) with G = Z/2 acting on a real free fermion,
the DW anomaly vanishing because H^3(BZ/2, U(1)) classes on a
fermion system reduce to Arf invariants that can be computed
and shown zero for suitable boundary conditions. These are all
consistent with Vol II Monster theorem (S3), NOT with the bare
slogan (S4).

## Verdict

B85 as written conflates (S1), (S2), (S3), (S4). The Vol II
inscription (`thm:monster-orbifold-e3`) correctly scopes the
construction to (S3) with four explicit preconditions: freely
generated parent, equivariant BV data, vanishing DW class,
orbifold BV gluing. The Vol II FM120 entry correctly flags the
(S4) slogan as a failure mode. But Vol I B85 still reads as a
bare slogan without scoping, which is itself an AP255 /
AP269 / AP280 instance: advertising a mechanism ("orbifold route")
without inscribing the preconditions.

## Heal (scope qualifier, Vol I Blacklist B85)

The Vol I B85 entry is reformatted to match the B1-B84 / B86+
convention, with explicit BAD -> CORRECT healing arrow and
citation to the Vol II inscription:

  B85 (revised). "Orbifold route: Z/n-invariants preserves E_n
  structure" (bare slogan) -> FORBIDDEN. Correct scoped statement:
  "E_n-topological G-gauging requires (i) G-equivariant BV data on
  an E_n-topological parent, (ii) vanishing Dijkgraaf-Witten class
  alpha_G in H^{n+1}(BG, U(1)), (iii) orbifold BV gluing of
  untwisted + twisted sectors. Trivial-action G-invariants
  preserve E_n tautologically (Lurie HA 5.1 in the G-equivariant
  ambient); this is not the orbifold route. Nontrivial-action
  G-invariants on a VOA give a VOA (Dong-Mason 1997) but not
  automatically E_n-topological. See Vol II
  `thm:monster-orbifold-e3` for the paradigmatic instance: Monster
  V^natural = V_Lambda // Z/2 is E_3-topological via Leech even
  unimodularity forcing alpha_sigma = 0. Regex trigger: any prose
  sentence of the form `Z/n invariants preserve E_n` or
  `Z/n orbifold inherits E_n` without explicit BV equivariance +
  DW anomaly vanishing."

This heal is LOCAL TO CLAUDE.md (Blacklist entry). No manuscript
edits required: the Vol II Monster theorem is correctly scoped;
Vol I Blacklist needs the format upgrade so future agents do not
treat B85 as endorsement of the bare slogan.

## Propagation

AP5 cross-volume audit:

  Vol I: zero manuscript sites treating B85 as proved general
    principle. The `standalone/sc_chtop_pva_descent.tex:1580`
    inscription is a reference forward to the Vol II orbifold
    route via Khan-Zeng PVA descent, which is correct: that
    standalone quotes `thm:wave14-khan-zeng` clause asserting
    "recovers the Vol II orbifold route via Z/n-invariants
    preserving E_n-structure." This phrasing is compressed; it
    refers to (S3) scoped by the Khan-Zeng hypothesis (freely
    generated PVA), not to (S4). No edit needed at this site;
    the Khan-Zeng hypothesis is stated in the same theorem.

  Vol II: `thm:monster-orbifold-e3` correctly scoped. FM120 and
    FM132 correctly flag the slogan. AGENTS.md line 110 phrases
    the claim as "Z/2-invariants of E_n preserve E_n" in the
    context of V_Leech^+ specifically (not V^natural); this is
    still compressed but scoped to the untwisted sector, which
    is the tautological (S2)-for-VOA + E_n-preservation under
    trivial-boundary-condition sector. No edit needed.

  Vol III: no matches for the bare slogan.

## AP assignments (minimal, per mission constraint)

AP1281 (BARE-SLOGAN BLACKLIST ENTRY). A Blacklist entry written
without the standard `BAD -> CORRECT` healing arrow is
underdetermined: agents cannot tell whether it names a forbidden
pattern or a correct pattern. Canonical violation: Vol I
CLAUDE.md B85 "Orbifold route: Z/n-invariants preserves E_n
structure" lacks the arrow. Counter: every Blacklist entry must
carry an explicit arrow. Healing template: convert the bare
slogan to `BAD form -> CORRECT scoped statement. [citation to
inscribed theorem]`. Distinct from AP236 (blacklist-slug leakage
into typeset parenthetical): AP236 is about slug IDs reaching
the PDF; AP1281 is about Blacklist entries in CLAUDE.md having
underspecified format.

AP1282 (FINITE-GROUP INVARIANTS vs GAUGING CONFLATION).
Invariants A^G for a finite group G acting on an E_n-algebra A
preserve the underlying algebra structure (and even the E_n
structure when G acts trivially or in the G-equivariant category
sense of Lurie HA 5.1). Gauging A // G is a DIFFERENT operation
requiring (i) equivariant BV data, (ii) DW anomaly class alpha_G
in H^{n+1}(BG, U(1)) vanishing, (iii) twisted-sector inclusion.
Invariants and gauging coincide only when the DW class vanishes
AND the twisted sectors are trivial. Canonical violation: Vol II
FM120 (Monster V^natural = V_Leech^+ "inherits E_3-topological by
finite-group invariants" conflated Z/2 gauging with trivial-action
invariants). The Vol II Monster theorem correctly uses gauging.
Counter: any claim "G-invariants preserves E_n" for nontrivial G
action must specify (a) whether G acts on the E_n-algebra
structure equivariantly (then invariants work if the action lifts
to BV data), or (b) whether the operation is gauging (then DW
anomaly must vanish and twisted sectors must be included). Related
to AP184 (excision vs coproduct codomain discipline): same class
of operation-identity confusion at different layer.

## Mission closure

Build: n/a (notes-only, no .tex edits).
Test: n/a.
Propagation: complete per AP5 audit above.
Report: this file.
Commits: none (no manuscript changes; Blacklist healing is a
CLAUDE.md update that requires user authorisation).
