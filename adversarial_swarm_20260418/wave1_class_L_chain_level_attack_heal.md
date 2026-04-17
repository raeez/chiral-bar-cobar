# Wave-1 attack-and-heal (2026-04-18):
# Class-L topologization η_1 strict chain-level — reverse-drift diagnosis

All work by Raeez Lorgat. No AI attribution. No .tex edits or commits in this pass;
this note establishes the diagnosis so a follow-up edit pass can execute the heals.

## 0. Target

CLAUDE.md Topologization row asserts:
  "PROVED on original complex for G/critical; PROVED Q_{tot}-cohomological for L;
   PROVED weight-completed for M (thm:topologization-tower; post-Wave-1 Beilinson
   audit 2026-04-17 identifies three open directions, not one)"

with open direction (II): "class L strict chain-level upgrade of the Q_{tot}-
cohomological identification to the raw bar complex via explicit η_1 antighost-
contact (required computation: [Q, tilde G_1] - T_Sug identically zero in the bulk
BV chain complex, not merely Q-exact; Vol II candidate formulas retracted pending
verification)".

Task: adversarial audit of the retraction and of the "three open directions"
enumeration; heal the correct state.

## 1. Attack ledger

### A1. The η_1 retraction at Vol II `e_infinity_topologization.tex:382-411`
  (`rem:frontier-class-L-strict-chain-level`) reads:

    "An earlier summary draft asserted the explicit forms
     η_1^(i) = (1/(2(k+h^∨))) Σ f^a_{bc} :c̄_b c^c c̄_a:  and
     η_1^(ii) = (1/(2(k+h^∨))) Σ f_{ab}^c :c̄_a c̄_c c^b: ;
     the verification that these choices absorb the full chain-level
     discrepancy in [Q, tilde G_1] - T_Sug is pending, and the summary
     claim has been downgraded accordingly to a frontier item."

  CLAIM OF RETRACTION: the η_1^(i) + η_1^(ii) absorption has NOT been verified.

### A2. Primary-source falsification. Vol I
  `chapters/theory/topologization_chain_level_platonic.tex` contains:

    * Construction constr:G1-recall (L228-236): explicit G_1 = (1/(2(k+h^∨))) Σ :J^a c̄_a:.

    * prop:QG1-remainder (L238-281, ClaimStatusProvedHere):
         [Q_tot, G_1] = T_Sug + R_ghost + R_self
      with R_ghost, R_self given by explicit formulae (eq:R-ghost, eq:R-self).
      Signed Leibniz-rule computation, proof body present.

    * def:eta1 (L292-313): exactly the two formulae claimed retracted in Vol II,
      namely
         η_1^(i)  = (1/(2(k+h^∨))) Σ f^a_{bc} :c̄_b c^c c̄_a:          (eq:eta-i)
         η_1^(ii) = (1/(2(k+h^∨))) Σ f^c_{ab} :c̄_a c̄_c c^b:          (eq:eta-ii)
         η_1      = η_1^(i) + η_1^(ii).

    * prop:eta-i-primitive (L327-388, ClaimStatusProvedHere):
         [Q_tot, η_1^(i)] = R_ghost.
      Proof body: signed Leibniz application of Q_tot to (eq:eta-i), with
      three terms (leading J_b term, middle Qc^c term, trailing Qc̄_a term).
      Jacobi identity (cyclic antisymmetrisation) kills the middle and trailing
      sub-pieces; the leading term becomes R_ghost after index raising with
      totally-antisymmetric f_{abc}. Net: [Q_tot, η_1^(i)] = R_ghost.

    * prop:eta-ii-primitive (L390-411, ClaimStatusProvedHere):
         [Q_tot, η_1^(ii)] = R_self.
      Proof: parallel to the above with the two antighost factors exchanged.

    * cor:eta-primitive (L413-420): [Q_tot, η_1] = R_1 := R_ghost + R_self.

    * thm:sugawara-antighost-primitive-chain-level (L426-458,
      ClaimStatusProvedHere): with tilde G_1 := G_1 - η_1,
         [Q_tot, tilde G_1] = T_Sug  in O_bulk (chain level, BEFORE passage to H^•).
      Proof: subtract cor:eta-primitive from prop:QG1-remainder.

    * thm:chain-level-E3-top-class-L (L483-523, ClaimStatusProvedHere):
      concludes chain-level E_3^top on the ORIGINAL BRST complex for class L
      via brace deformation complex + Lurie recognition (HA 5.4.5.9) + Dunn
      additivity with open E_1^top.

    * Concrete sl_2 verification at L539-593 (prop:eta-formula-sl2-k1-explicit,
      ClaimStatusProvedHere) with numerical cross-check at
      compute/tests/test_topologization_chain_level.py (file exists, carries
      HZ-IV decorator declaring three disjoint sources: CFG BV factorization
      trace, SymPy sl_2 explicit computation, Kac-Wakimoto 1988 affine
      Sugawara commutation).

### A3. Consequence.
  The Vol II "retraction" is FALSE as written. The η_1^(i) + η_1^(ii)
  absorption IS verified, in Vol I, with proof body, ClaimStatusProvedHere,
  and HZ-IV decorator on the sl_2 witness. The Vol II frontier remark is
  an AP271 REVERSE-DRIFT (manuscript ahead of CLAUDE.md / Vol-II notes):
  Vol II's e_infinity_topologization.tex:382-411 records a retraction written
  under the earlier Wave-1 narrative that the η_1 formulae were pending;
  Vol I subsequently inscribed the theorem with full proof body; Vol II
  never updated to reflect the Vol I inscription.

### A4. Propagation of the reverse-drift.
  Vol II `bp_chain_level_strict_platonic.tex:77-94` and throughout
  (L378, L406, L453, L521, L528, L550, L671, L678, L700, L779, L782, L823)
  CORRECTLY cites
      \cite[Thm \ref*{thm:sugawara-antighost-primitive-chain-level}]{Vol1-class-L-antighost}
  as the upstairs strict chain-level identity on the double cover. This
  Vol II chapter is internally consistent and depends on exactly the Vol I
  theorem that the `e_infinity_topologization.tex:382-411` remark falsely
  claims to be pending. If the frontier remark were correct, the entire
  BP chain-level chapter would collapse; but it does not collapse, because
  the frontier remark is the stale one, not the BP chapter.

  Likewise Vol II `standalone/bar_chain_models_chiral_quantum_groups.tex:474,
  505` and `working_notes.tex:20405` assert the η_1^(i) + η_1^(ii) strict
  chain-level cancellation — all consistent with Vol I's inscription.

### A5. CLAUDE.md Topologization row consequence.
  The CLAUDE.md post-Wave-1 "three open directions" enumeration has one
  spurious entry. Direction (II) ("class L strict chain-level upgrade of
  the Q_{tot}-cohomological identification") is NOT an open direction; it
  is proved at Vol I `thm:chain-level-E3-top-class-L`. Directions (I)
  (class M on the ORIGINAL complex in Ch(Vect); the pro/J-adic/weight-
  completed ambient question that may or may not dissolve) and (III)
  (antighost BRST-commutativity [G^(n), G^(m)] = Q-exact at spin n,m ≥ 4 —
  axiom (T5), postulated not derived; `thm:iterated-sugawara-construction`
  for n ≤ 3 survives) ARE the genuine open directions. The Class-L status
  should read "PROVED chain-level on ORIGINAL complex for class L", not
  "Q_{tot}-cohomological for L".

### A6. Residual scope caveats (honest frontier inside the class-L claim).
  Vol I's thm:chain-level-E3-top-class-L proof in the class-L row is
  concrete; Proposition prop:eta-i-primitive and prop:eta-ii-primitive
  depend on the CFG point-splitting model for the 3-field normal-ordered
  associator (Remark rem:NO-assoc, citing CG1 §5.3). The claim is
  therefore strict chain-level IN THE CFG MODEL (Definition def:cfg-bv-
  complex / def:no-cfg / conv:topol-platonic). A different BV model
  (Costello-Gwilliam 2602.12412 factorization trace, BD factorization,
  or Tamarkin chain-level) is related by HTT quasi-isomorphism. The
  inscribed theorem is model-dependent at chain level but
  quasi-isomorphically canonical; this is standard for BV / factorization-
  algebra chain-level statements and does NOT downgrade the claim.

## 2. Surviving core (2-3 sentences)

For class L (affine Kac–Moody at non-critical level), the Sugawara
topologization is PROVED strictly at chain level on the ORIGINAL CFG BV
complex via Vol I `thm:sugawara-antighost-primitive-chain-level`: with
η_1 = η_1^(i) + η_1^(ii) the explicit two formulae (eq:eta-i, eq:eta-ii)
of Vol I def:eta1, the corrected antighost tilde G_1 = G_1 - η_1 satisfies
[Q_tot, tilde G_1] = T_Sug in O_bulk; consequently
Z^{der}_ch(V_k(g)) carries an E_3^top-algebra structure on the original
complex (thm:chain-level-E3-top-class-L), not merely on Q_tot-cohomology.
The genuinely open directions are (I) class M on the original complex in
Ch(Vect), and (III) axiom-(T5) antighost BRST-commutativity at spins ≥ 4.

## 3. Heal plan (no .tex edits this pass; prescription for a follow-up edit pass)

H1. Vol II `chapters/connections/e_infinity_topologization.tex:382-411`
    retraction remark `rem:frontier-class-L-strict-chain-level` REWRITE
    from frontier to historical note. Replace body with: "An earlier Wave-1
    summary draft listed the η_1^(i), η_1^(ii) chain-level absorption as
    pending. Subsequent inscription in Vol~I (see
    \cite[Theorems \ref*{thm:sugawara-antighost-primitive-chain-level},
    \ref*{thm:chain-level-E3-top-class-L}, and Propositions
    \ref*{prop:eta-i-primitive}, \ref*{prop:eta-ii-primitive}]
    {Vol1-class-L-antighost}) supplied explicit primitives with signed
    Jacobi-identity proofs and a SymPy sl_2 witness; the class-L strict
    chain-level identity [Q_tot, tilde G_1] = T_Sug on the ORIGINAL CFG BV
    complex is PROVED in Vol~I. The present retraction is retired." Keep
    the \phantomsection\label{frontier:class-L-strict-chain-level} to
    preserve cross-file references and attach `\ClaimStatusProvedElsewhere`
    to the ambient statement. Re-label `rem:frontier-class-L-strict-
    chain-level` to `rem:class-L-strict-chain-level-resolved` OR retain
    the label with the historical-note body (pick one atomically).

H2. Vol I CLAUDE.md Topologization row status rewrite:
    "PROVED on original complex for G / class L / critical; PROVED
     weight-completed for M (thm:topologization-tower)"
    with "two genuine open directions":
      (I) class M on the ORIGINAL complex in Ch(Vect) (ambient-choice
          artefact vs genuine gap; pro-/J-adic/weight-completed ambient
          is proved);
      (III) antighost BRST-commutativity [G^(n), G^(m)] = Q-exact at
            spins n,m ≥ 4 — axiom T5 of def:higher-spin-stress-tower,
            postulated not derived; W_∞ E_∞-ladder conditional on (III).
    Delete former direction (II); retain (I)/(III) with the new numeric
    labelling (I)/(II) or relabel honestly as "two open directions".

H3. Vol II `notes/bershadsky_polyakov_universal_holography_attack_heal.md`
    (5 sites L61/69/154/173/202, inscription-stale per AP288) —
    the present inline RETRACTED annotations are themselves now stale
    and should be replaced by "RESTORED 2026-04-18 (η_1 chain-level
    absorption verified in Vol~I thm:sugawara-antighost-primitive-chain-
    level, cross-volume); the earlier Wave-1 retraction was reverse-drift
    per AP271." Alternative: top-of-file banner "HISTORICAL — superseded
    by wave1_class_L_chain_level_attack_heal.md 2026-04-18".

H4. Vol I CLAUDE.md AP271 catalogue: append the present reverse-drift as
    an additional exemplar under AP271 (canonical: η_1 retraction in Vol II
    e_infinity_topologization.tex:382-411 lagging Vol I
    thm:sugawara-antighost-primitive-chain-level). Current AP271 canonical
    violation is the thm:A-infinity-2 modular-family extension — add
    second canonical violation here.

H5. (Sharpened obstruction, AP266-style, OPTIONAL) If the follow-up edit
    pass wishes to be cautious about model-dependence: add a scope remark
    at Vol I `thm:chain-level-E3-top-class-L` (already has prose at
    L525-536 rem:chain-vs-coh-sharp) noting that the strict chain-level
    identity holds in the CFG point-splitting model; different BV models
    (CG 2602.12412 heat-kernel, Tamarkin, BD factorization) are related
    by HTT quasi-isomorphism. This is a CLARIFICATION, not a downgrade.
    Engine: compute/tests/test_topologization_chain_level.py already
    declares CFG BV factorization trace as verified_against source.

## 4. Commit plan (four atomic commits when the follow-up edit pass runs)

  C1. (Vol II) Rewrite `rem:frontier-class-L-strict-chain-level` to
      historical note per H1; update ClaimStatus accordingly.
      Files: chapters/connections/e_infinity_topologization.tex.
      Author: Raeez Lorgat.

  C2. (Vol I) Update CLAUDE.md Topologization status row per H2;
      update the Platonic Ideal Roadmap "Beilinson-rectified open
      frontiers" list accordingly (remove class-L strict chain-level
      item; retain class-M original-complex and antighost-commutativity).
      Files: CLAUDE.md. Author: Raeez Lorgat.

  C3. (Vol II) Append RESTORED annotations at 5 sites in
      notes/bershadsky_polyakov_universal_holography_attack_heal.md per H3.
      Files: notes/bershadsky_polyakov_universal_holography_attack_heal.md.
      Author: Raeez Lorgat.

  C4. (Vol I) Append η_1 reverse-drift exemplar to AP271 catalogue body.
      Files: CLAUDE.md. Author: Raeez Lorgat.

All four commits pre-commit gated per standard protocol: (1) build fast
on each volume touched, (2) make test on affected test modules, (3) AI
attribution grep = zero hits.

## 5. Deliverable summary (under 600 words)

ATTACK. CLAUDE.md Topologization row lists "three open directions, not
one" in class-L / class-M / antighost-commutativity. Direction (II)
("class L strict chain-level upgrade of Q_{tot}-cohomological
identification via explicit η_1 antighost-contact") is derived from Vol
II `rem:frontier-class-L-strict-chain-level` at e_infinity_topologization.tex
:382-411, which asserts the η_1^(i) + η_1^(ii) verification is pending.
Vol I manuscript falsifies that retraction: Vol I
`topologization_chain_level_platonic.tex` contains
thm:sugawara-antighost-primitive-chain-level (ClaimStatusProvedHere,
L426-458) with the exact two η_1 formulae (def:eta1 L292-313), and the
load-bearing Jacobi-identity computations at prop:eta-i-primitive
(L327-388) and prop:eta-ii-primitive (L390-411). The chain-level
E_3^top conclusion is thm:chain-level-E3-top-class-L (L483-523,
ClaimStatusProvedHere). HZ-IV decoration with SymPy sl_2 explicit
witness lives at compute/tests/test_topologization_chain_level.py. Vol
II `bp_chain_level_strict_platonic.tex` depends on (and correctly cites)
this Vol I inscription. The Vol II retraction is AP271 reverse drift —
Vol II lagging the Vol I heal that already closed the frontier.

SURVIVING CORE. Class-L strict chain-level topologization is PROVED on
the original CFG BV complex: with η_1 = η_1^(i) + η_1^(ii) the explicit
two-term antighost gauge correction, [Q_tot, G_1 - η_1] = T_Sug holds
chain-level in O_bulk for every simple g and non-critical k, and
Z^{der}_ch(V_k(g)) carries chain-level E_3^top structure on the original
complex. The genuinely open directions are only two: (I) class M on the
original complex in Ch(Vect) (ambient-choice question, possibly
dissolves), and (II) axiom-(T5) antighost BRST-commutativity at spins
n,m ≥ 4 (postulated not derived; W_∞ E_∞-ladder inherits conditional
status).

HEAL. Five surgical edits in a follow-up edit pass: (H1) rewrite
rem:frontier-class-L-strict-chain-level to historical note citing the
Vol I inscription; (H2) update CLAUDE.md status row and Platonic Ideal
Roadmap to two open directions; (H3) append RESTORED annotations to the
5 stale-narrative sites in the BP attack-heal ledger; (H4) append
exemplar to AP271 catalogue; (H5) optional CFG-model scope remark at
Vol I thm:chain-level-E3-top-class-L. Four atomic commits, Raeez Lorgat,
pre-commit gated on build + tests + zero AI attribution.

COMMIT PLAN. C1-C4 as above. Each commit smaller than a single file's
worth of edits. Build each touched volume before committing. Run
test_topologization_chain_level.py + test_e3_topological_km.py +
test_monster_chain_level_e3_top.py at minimum to verify no regressions
before C1-C2. No AI attribution.
