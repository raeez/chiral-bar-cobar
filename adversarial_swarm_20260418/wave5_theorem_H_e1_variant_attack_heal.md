# Wave 5 Theorem H E_1-variant attack-and-heal (2026-04-18)

Target. `thm:hochschild-concentration-E1`
(`chapters/theory/chiral_hochschild_koszul.tex:1373`), the E_1-variant
route for Theorem H's {0,1,2}-concentration via ordered FM +
pure-braid Orlik-Solomon, plus load-bearing companions
`thm:pbw-koszulness-criterion`
(`chapters/theory/chiral_koszul_pairs.tex:784`),
`lem:chiral-quadratic-koszul`
(`chiral_hochschild_koszul.tex:657`),
`lem:chiral-homotopy-transport`
(`chiral_hochschild_koszul.tex:1216`), and
`prop:fm-tower-collapse` (`chiral_hochschild_koszul.tex:762`).

Status entering the session. The same target was audited earlier
this day in `attack_heal_theorem_H_20260418.md`; the Wave-5 mission
brief arrived with six attack vectors that map one-for-one onto the
earlier ledger's findings A1-A5 plus a companion check on the
`R(z) ne tau` obstruction framing. No new mathematical gap was
surfaced; this note records the status of each vector and
supersedes the earlier note only in the pointer table below.

## Attack vectors versus findings.

1. Is `thm:hochschild-concentration-E1` inscribed or advertised?
   INSCRIBED. Theorem body at lines 1370-1391 with `ClaimStatusProvedHere`;
   proof body at lines 1393-1421. The earlier session's A5 check was
   the same grep, with the same result. No AP255.

2. Ingredients inscribed vs folklore?
   FM^ord: inscribed inside the proof body (lines 1395-1400), via the
   ordered Fulton-MacPherson compactification. Pure-braid
   Orlik-Solomon Koszulity: cited as Shelton-Yuzvinsky 1997
   (`SheltonYuzvinsky1997` bibkey) at line 1403, with the Koszul
   structure transported onto the ordered chiral bar through
   `lem:chiral-homotopy-transport`:1216. Ordered chiral Koszul dual of
   the Yangian: the E_1-chiral Yangian case is explicitly handed off
   to the ordered associative chiral Koszul-duality framework
   (`ordered_associative_chiral_kd.tex`) by
   `rem:E1-scope-hochschild-concentration`:1425-1448; the theorem
   under audit does NOT claim to prove the Yangian case.  No AP272.

3. R(z) != tau obstruction class as quantum-group content?
   Framing: the `rem:E1-scope-hochschild-concentration` explicitly
   separates ordered-bar Koszulity (the E_1-chiral Yangian content,
   handled in the ordered appendix) from the symmetric-bar {0,1,2}
   bound (the E_infty-chiral content of Theorem H proper). The
   obstruction to a symmetric-side {0,1,2} bound for an E_1-chiral
   input is therefore scoped as the averaging gap rather than
   inscribed as an explicit cohomology class here. The sharpened
   form (AP266) lives, correctly, in
   `ordered_associative_chiral_kd.tex`; re-inscribing it inside
   Theorem H would conflate the two scopes.

4. AP277 status of the test body?
   HEALED. `compute/tests/test_theorem_H_hochschild_koszul.py:81-121`
   calls `chirhoch_heisenberg`, `chirhoch_virasoro`,
   `chirhoch_affine_km("sl_2")` with hardcoded Hilbert triples
   (1,1,1), (1,0,1), (1,3,1) and totals 3, 2, 5. The prior
   Wave-14 "three hard-coded True booleans" concern no longer
   applies; the test body is non-tautological.

5. HZ-IV disjointness.
   Decorator prose cites three disjoint classical sources:
   Feigin-Fuchs 1984 (Fock/BRST resolution for Virasoro),
   Wang 1998 (semi-infinite BRST for W_N), Whitehead + Kunneth
   (affine sl_2). Residual (honest): the numerical values the
   test asserts are sourced from `chirhoch_dimension_engine.py`,
   whose dataclass entries cite the chapter under review; the
   three external classical sources are bibliographic provenance
   rather than independent numerical engines. The earlier note
   A3 recorded this as "partial HZ-IV; disjoint numerical engine
   for Feigin-Fuchs / Wang not yet implemented," which is the
   correct status.

6. `thm:pbw-koszulness-criterion` inscription.
   INSCRIBED. Label at `chiral_koszul_pairs.tex:784`; three
   hypotheses + proof body at lines 783-853; the proof is a
   standard PBW spectral-sequence argument reducing chiral
   Koszulness to classical Koszulness of the associated graded
   via flat filtration (Priddy's theorem in the Kac-Moody case,
   cited at line 895). Stale phantom-file tag in
   `standalone/theorem_index.tex` was already corrected in the
   earlier session (H2).

Critical level. `rem:critical-level-dimensional-divergence`:1884-1928
inscribes the failure mechanism at `k = -h^vee` with mathematical
content (Feigin-Frenkel centre populates `ChirHoch^0`; PBW
associated graded becomes non-Koszul; FM-tower collapse fails).
This is not a rhetorical scope tag.

## Surviving core (3 sentences).

Theorem H's {0,1,2}-concentration and the sharp bigraded Hilbert
series remain PROVED on the Koszul locus with critical level
`k = -h^vee` excluded via an explicit dimensional-divergence mechanism.
The E_1-variant theorem establishes the same concentration intrinsically
on the ordered FM side via pure-braid Orlik-Solomon Koszulity
transported through the Fresse chain map, without invoking the
symmetric-bar concentration theorem, and its "E_1" label refers to the
first page of the collision-depth spectral sequence, not to
E_1-chiral input algebras. The ordered bar cohomology of the
E_1-chiral Yangian, and the R-matrix obstruction to its
symmetric-side {0,1,2} bound, are scoped to the ordered
associative chiral Koszul-duality framework rather than to this
theorem.

## Heal per finding.

H1. No new heal required. The earlier session's heals on
    `lem:chiral-quadratic-koszul` non-degeneracy (Step 1 explicit
    on the OPE-residue pairing), AP255 phantom-file correction,
    and AP277 test-body status are the operative heals for the
    current Wave-5 brief.

H2. Wave-5 specific: none. The ordered-bar Yangian AP266 sharpening
    is not a re-heal of Theorem H; it lives in
    `ordered_associative_chiral_kd.tex` (`thm:chiral-qg-equiv`
    surrounding discussion) and should be audited there, not
    here. The current brief's sentence "symmetric-bar obstruction
    R(z) ne tau IS the quantum-group content" is a scope pointer
    (the residual after Theorem H's averaging step), not an
    unresolved obligation of Theorem H.

## Commit plan.

None. This note records status; no `.tex`, engine, or test
changes were made. The earlier Wave-5 session already committed
the substantive heals (`lem:chiral-quadratic-koszul` non-degeneracy,
theorem-index phantom correction); the CLAUDE.md Theorem H row
already reflects those heals. The present note exists only to
close the mission-brief loop with the correct pointer to the
earlier ledger.

Raeez Lorgat, 2026-04-18.
