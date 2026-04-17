# Wave 1 — Adversarial Audit of the Chiral Quantum Group Equivalence Cluster

**Date**: 2026-04-17.
**Targets**: `thm:chiral-qg-equiv-ordered`, `thm:glN-chiral-qg`, `thm:w-infty-chiral-qg-completed`,
`thm:chiral-qg-equiv-elliptic`, `thm:chiral-qg-equiv-toroidal-formal-disk`,
`prop:yangian-ordered-koszul`, `prop:sl2-yangian-triangle-concrete`,
`thm:grt1-rigidity`, lemma `qdet-central-all-N`, `thm:glN-chiral-qg` Argument B (Feigin–Frenkel
replacement of JKL26).

**Modus operandi**: read the .tex source for each label; compare to the CLAUDE.md status-table
narrative; flag overclaims, label-only inscriptions, and circular forwarding; pin the
sharpest defensible scope. NO .tex edits.

---

## Attack

### F1. The "Feigin–Frenkel screening replaces JKL26" claim is not enacted in the chapter.

Status table (CLAUDE.md, "gl_N chiral QG" row) reads:
> **PROVED UNCONDITIONAL all N≥2 via Feigin–Frenkel screening** (JKL26 phantom eliminated)
> Feigin–Frenkel replacement of Argument B (2026-04-16): W_N = ∩ ker(Q_{α_i}) inside
> rank-(N-1) Heisenberg (class G with explicit chiral QG datum).

Source check, `chapters/theory/ordered_associative_chiral_kd.tex:10273-10285`
(the proof body of `thm:glN-chiral-qg`, Argument B):

> "The JKL vertex bialgebra theorem~\cite{JKL26} applies to the CoHA of the Jordan quiver
> at arbitrary rank~$N$ (their Theorem~C holds for general quivers with potential). The
> vertex coproduct on $\cH_{\mathrm{Jor},N} \cong Y^+(\widehat{\mathfrak{gl}}_N)$ satisfies
> ...and identifies with the Drinfeld coproduct."

`grep -n "Feigin.{0,3}Frenkel\|FF.screening\|screening operator"` in
`ordered_associative_chiral_kd.tex` returns ZERO matches. The chapter's actual Argument B is
JKL26-cited verbatim. The "phantom-elimination" description in CLAUDE.md does not exist in
the source; it is an aspirational future heal recorded as if it were an inscription.

Even if the FF replacement were inscribed, two structural questions remain unaddressed:

(i) Q_{α_i} is a screening operator commuting with the Sugawara T(z) (Feigin–Frenkel 1996,
Frenkel–Ben-Zvi). The chiral coproduct Δ_z on the Heisenberg parent has not been shown to
commute with Q_{α_i} as a map of E_1-chiral coalgebras; only the conformal structure is
preserved. Without Q_{α_i} ∘ Δ_z = (Δ_z ⊗ Δ_z) ∘ Q_{α_i} (or its appropriate chiral-Hopf
analog), the kernel ∩ ker(Q_{α_i}) does NOT inherit a coproduct from the parent.

(ii) The Drinfeld coproduct on the Heisenberg parent is the trivial primitive coproduct
Δ_z(J) = J⊗1 + 1⊗J (because Heis is class G). The Δ_z on W_N is **not** primitive on the
spin-≥2 generators — it carries (Ψ−1)/Ψ cross-terms (`thm:miura-cross-universality`). So
the screening kernel cannot inherit Δ_z from the trivial parent; it requires a NEW coproduct
construction on the kernel, which is precisely what JKL26 supplies via the CoHA route. The
"FF replacement" prose elides this: replacing ⊃JKL by ⊂Heis does not give the coproduct.

**Verdict**: F1 stands. Argument B remains JKL26-dependent in the source.

### F2. The 8 "strengthening inscriptions" of `thm:chiral-qg-equiv-ordered` live in standalones, not the main chapter.

CLAUDE.md status table for "Chiral QG equiv" claims 8 inscriptions: (1) `def:ordered-koszul-
chiral-algebra`, (2) `prop:yangian-ordered-koszul`, (3) `thm:chiral-qg-equiv-ordered`, (4)
`prop:sl2-yangian-triangle-concrete`, (5) `thm:glN-chiral-qg`, (6) `thm:w-infty-chiral-qg-
completed`, (7) `thm:grt1-rigidity`, (8) `thm:chiral-qg-equiv-elliptic` and
`thm:chiral-qg-equiv-toroidal-formal-disk`.

Cross-volume label search:

- `def:ordered-koszul-chiral-algebra` — appears with `-sf` suffix in
  `standalone/seven_faces.tex` only; NOT in chapters/.
- `prop:yangian-ordered-koszul` — appears with `-sa` suffix in
  `standalone/e1_primacy_ordered_bar.tex` only.
- `thm:chiral-qg-equiv-ordered` — appears with `-sf` suffix in `standalone/seven_faces.tex`,
  status `\ClaimStatusProvedElsewhere`, body delegates to "the body of the monograph".
- `prop:sl2-yangian-triangle-concrete` — NOT FOUND in any chapter or standalone in Vol I.
- `thm:w-infty-chiral-qg-completed` — NOT FOUND.
- `thm:grt1-rigidity` — `\phantomsection\label` only in `chapters/frame/preface.tex:5074`,
  PLUS body in `standalone/seven_faces.tex` with `\ClaimStatusProvedElsewhere`.
- `thm:chiral-qg-equiv-elliptic`, `thm:chiral-qg-equiv-toroidal-formal-disk` — only in
  `standalone/seven_faces.tex` with `-sf` suffix.

A `\ClaimStatusProvedElsewhere` standalone that points to nowhere in the body is **circular
forwarding** (AP190 hidden imports + AP227 ProvedHere forwarding inverse). The "8
inscriptions" are predominantly: (a) standalone-only, (b) phantom-section anchors, or (c)
non-existent (cases 4, 6).

**Verdict**: F2 stands. The status-table inscription count overstates Vol I main-chapter
coverage by a factor ≥4 (the only label genuinely inscribed and proved in a Vol I chapter
is `thm:chiral-qg-equiv` and its corollary `cor:bar-encodes-all-structural`, plus
`thm:glN-chiral-qg` and `thm:w-infty-chiral-qg`).

### F3. Elliptic chiral QG: Belavin in source, Felder in CLAUDE.md.

CLAUDE.md (status table + Open Frontiers reconstitution): "elliptic via Felder R(z,τ) + Fay
trisecant". Source `chapters/examples/yangians_drinfeld_kohno.tex:7269-7281`: the elliptic
r-matrix is the **Belavin/Belavin–Drinfeld** form, with Cartan channel
ζ_τ(z) · H⊗H/2 and root channels φ_±(z,τ) E⊗F + φ_∓(z,τ) F⊗E.

Felder's dynamical R-matrix and Belavin's vertex R-matrix are different objects:

- **Belavin** is non-dynamical (does not depend on auxiliary λ); for sl_N it lives in
  End(C^N ⊗ C^N) and uses theta-function entries indexed by Z_N × Z_N.
- **Felder** R(z, λ, τ) is dynamical (depends on λ ∈ h*); satisfies the **dynamical** YBE,
  not the ordinary YBE; arises from IRF/face-model statistical mechanics.

Vertex–IRF correspondence relates them at sl_2 level (Felder–Pasquier; Foda et al.), but is
NOT automatic at higher rank (FM38). Saying "Felder + Fay" while inscribing Belavin
conflates two different elliptic R-matrices.

Worse: line 7318 of `yangians_drinfeld_kohno.tex` writes
`ζ_τ(z) = θ_1'(z|τ)/θ_1(z|τ) + 2η_1·z` — exactly the **Weierstrass zeta** that **FM30
flags as breaking CYBE**. The proof attempts a degeneration ζ_τ → π cot(πz) but does not
verify that the candidate elliptic r-matrix as written satisfies CYBE algebraically; it
notes only "verified numerically (relative error <10^{-6} at Im τ=12)" via
`elliptic_rmatrix_shadow.py`. Numerical CYBE on a single (z_1, z_2, z_3, τ) point at
finite tolerance is not a proof of an algebraic identity.

**Verdict**: F3 stands. The elliptic chiral QG theorem in Vol I is a **partial Belavin**
construction — leading-order ℏ, sl_2 only, CYBE numerically checked at one point — masquerading
in the status table as Felder + Fay.

### F4. Toroidal chiral QG: no chapter inscription exists.

`grep -rln "toroidal.*chiral.qg\|toroidal.*formal.disk\|U_{q,t}(\\\\ddot{\\\\fsl}_N)"` in
`chapters/` returns **zero hits** for any of the structural patterns. The status-table claim
"toroidal formal-disk PROVED via SV CoHA + Miki DIM" is supported only by the standalone
`seven_faces.tex:1019-1030` with `\ClaimStatusProvedElsewhere`, pointing back to nothing in
the chapters. The phrase "Global extension to P^1×P^1 is conditional on the class-M chain-level
topologization frontier" hedges the global claim, but the formal-disk claim itself has no
proof body in Vol I.

**Verdict**: F4 stands. Toroidal chiral QG is unproved in Vol I; the status entry should be
downgraded to ConjecturedHere or moved to a Vol III standalone with explicit inscription.

### F5. The "DS intertwining HZ-IV fix via independent sl_3 RTT" is tautological by construction.

CLAUDE.md status table: "DS intertwining HZ-IV fix via independent sl_3 RTT computation
inscribed (no longer tautological)". Source check `compute/lib/ds_coproduct_intertwining_engine.py`
docstring lines 103-104:

> "AT DEGREE 1, the intertwining is a TAUTOLOGY for the Cartan sector (both sides use the
> same Drinfeld formula)..."

Line 70: "These are the SAME formulas as delta_psi(1) and delta_psi(2) from the
miura_spin3_coproduct_engine."

The "57 verifications" verify a self-consistent specialisation: the engine derives the LHS
and RHS from the same Miura-derived formulas, then verifies they agree. This is precisely the
AP128 anti-pattern (engine and test sharing same mental model). Genuine independence at the
spin-3 W generator (the only place where the intertwining is non-tautological) is delegated to
`w3_gravitational_coproduct.py` with a "higher-arity HPL terms" placeholder.

**Verdict**: F5 stands. The HZ-IV decorator on `test_ds_coproduct_intertwining_engine.py`
fails the disjointness rationale at the spin-1 sector and is unverified at spin-3.

### F6. qdet centrality: external Molev citation, not an internal lemma.

Status table: "Lemma `qdet-central-all-N` inscribed internally (Molev's antisymmetriser
argument, not external citation)." Source check: `qdet-central-all-N` does not appear as a
labeled lemma anywhere in `chapters/`. Every qdet-central reference in
`ordered_associative_chiral_kd.tex` (lines 2735, 10025, 10042, 10177, 10340, 10428) cites
**Molev~\cite{Molev07}** as external authority. The "internal antisymmetriser inscription"
exists in the prose but not as a theorem-environment lemma with proof.

Even on the substance: Molev proves qdet centrality for the **classical Yangian** Y(gl_N)
in RTT formalism with **Yang's rational R(u) = uI + ηP** acting on End(C^N⊗C^N). The Vol I
chiral version (eq. 10184: Δ_z(T(u)) = T(u)·T(u−z)) carries a SPECTRAL PARAMETER z that
Molev's argument does not include. Whether the antisymmetriser argument transfers to the
Δ_z-coproduct setting is the key chiral question; it is asserted without proof.

**Verdict**: F6 stands. qdet centrality at the chiral level is asserted-by-citation, not
inscribed as an internal lemma.

### F7. Two-parameter gl_N RTT match with `rem:e3-non-simple-gl-N` is dimensional, not structural.

Status table: "Two-parameter gl_N RTT matches `rem:e3-non-simple-gl-N` (both give Sym^2
(gl_N^*)^{gl_N} = 2-dim)." This is a **dimension count match**, not a constructive identification.
Sym^2(gl_N^*)^{gl_N} is 2-dim because gl_N = sl_N ⊕ Z(gl_N) decomposes as a direct sum of a
simple summand and a 1-dim center, giving B_tr (Killing form on sl_N component) and B_ab
(scalar form on the center). The two-parameter gl_N RTT carries (k_sl, k_ab) levels which
also match a 2-dim cone of invariant forms. But "both 2-dim" is a coincidence of dimension;
the **isomorphism** between the RTT cone and the H^3-derived cone via E_3 identification is
not proved.

**Verdict**: F7 stands as a structural caveat. Numerical match ≠ canonical isomorphism.

### F8. AP171 associator dichotomy makes the "equivalence" non-canonical at cochain level.

CLAUDE.md AP171: "Chiral QG equiv holds 'up to Drinfeld associator Φ'. COHOMOLOGICAL derived
center = ASSOCIATOR-INDEPENDENT (sl_2 proved). COCHAIN-LEVEL = ASSOCIATOR-DEPENDENT."

This is acknowledged but not absorbed into the equivalence statement. Theorem
`thm:chiral-qg-equiv` (line 8403, source) writes "up to the choice of a Drinfeld associator
Φ ∈ exp(t̂_3)". A choice-of-associator IS NOT an equivalence — it is a torsor of equivalences
parameterised by GRT_1(Q). At cochain level, two different choices of Φ give two different
chiral coproducts that are gauge-related but not equal. The "equivalence" therefore reads
correctly only on H^0; on chains it is a (homotopically trivial but combinatorially
non-trivial) GRT_1-torsor of equivalences.

`thm:grt1-rigidity` (the phantom-section, with `\ClaimStatusProvedElsewhere` standalone body)
is the would-be repair: it asserts H^0 invariance and chain-level homotopy invariance. But
the chain-level argument requires the formality theorem for the little-disks operad
(Tamarkin–Kontsevich), which is itself associator-dependent. A circular dependency; the
canonicalisation requires fixing a specific associator class once and for all.

**Verdict**: F8 stands. Either the equivalence is stated on cohomology only (clean), or it is
stated on cochains with explicit "after fixing Φ ∈ GRT_1(Q)/H" choice (also clean). The
current formulation does both at once and elides the choice.

### F9. The `thm:glN-chiral-qg` proves the bialgebra side; the bialgebra ↔ Hopf bridge is missing.

The proof body of `thm:glN-chiral-qg` (lines 10288-10437) constructs (a) R-matrix, (b) Δ_z
coproduct, (c) RTT relation, (d) qdet, (e) A_inf via bar. It does NOT construct (f) antipode.
Per Vol I's own catalogue, "Antipode non-lifting" is in the status table as PROVED (negative):
"S(T(u))=T(u)^{-1} does NOT lift to vertex-algebraic antipode." So the chiral quantum group
is at most a **bialgebra**, not a Hopf algebra. CLAUDE.md uses "chiral quantum group equivalence"
to mean the bialgebra structure; the reader must be told this explicitly. Without the antipode,
"chiral quantum group" is a misnomer; the correct term is "chiral bialgebra equivalence" or
"factorisation bialgebra equivalence."

**Verdict**: F9 stands. The label `thm:chiral-qg-equiv` is misleading without an explicit
"bialgebra-only" qualifier in the title.

### F10. LaTeX hygiene: `\end{theorem>` typo in standalone `seven_faces.tex:1017`.

`standalone/seven_faces.tex:1017` contains `\end{theorem>` (FM7: `>` instead of `}`). This
will fail latex compilation of the standalone if invoked. Same file likely has compile
errors propagating from the elliptic theorem statement.

**Verdict**: F10 stands. Hygiene fix needed in standalone before any further extraction.

---

## Survivors

After the attack, the following elements survive at their stated scope:

1. `thm:chiral-qg-equiv` (line 8403, `ordered_associative_chiral_kd.tex`): the abstract
   triangle (R-matrix) ↔ (chiral A_inf) ↔ (chiral coproduct), STATED on the **ordered Koszul
   locus**, **up to Drinfeld associator Φ**, **at the cohomology / homotopy-fixed-points
   level**. The proof sketch (I→II via Stasheff associahedra; II→III via cobar; III→I via
   chiral Drinfeld formula) is the genuine content; survives if scope is restricted as just
   stated.
2. `thm:w-infty-chiral-qg` (line 8688): for W_{1+∞}[Ψ] specifically, the explicit
   Maulik–Okounkov R-matrix + scalar Δ_z = T(u) ⊗ T(u−z) + JKL26-Argument-B is genuinely
   constructive; survives.
3. `thm:glN-chiral-qg` (line 10111): the bialgebra-side construction at Yang R(u) = uI + ΨP +
   matrix Δ_z(T(u)) = T(u)·T(u−z) + RTT genuine for N≥2 + qdet by Molev citation. Survives
   AS A BIALGEBRA, AS A CITED RESULT for qdet, AT GENERIC Ψ. Argument B currently
   JKL26-dependent (F1).
4. The classical r-matrix degeneration chain
   `r^ell(z, τ) → r^trig(z) → r^rat(z) = kΩ/z` (proposition body with proof in
   `yangians_drinfeld_kohno.tex` near line 7297) survives at the **classical level**,
   numerically verified.

---

## Platonic Reconstitution

The defensible restatement of the cluster:

**Theorem (Chiral bialgebra equivalence on the ordered Koszul locus, cohomological).**
Let A be an E_1-chiral algebra on the ordered Koszul locus over a smooth curve X. After
fixing an associator class [Φ] ∈ GRT_1(Q)/(homotopy), the following structures on A are
naturally isomorphic on H^0:
(I) E_1-chiral structure with a vertex R-matrix S(z) satisfying QYBE, unitarity, shift,
   and hexagon (the EK axioms);
(II) chiral A_∞ structure in End^ch_A satisfying the chiral Stasheff identities;
(III) E_1-chiral coassociative bialgebra structure with a chiral coproduct Δ^ch up to
     the fixed Φ.
The equivalences are projections of the universal datum B^ord(A) = T^c(s^{-1}Ā). The
construction is **bialgebraic, not Hopf**: an antipode does not lift to the vertex-algebraic
setting.

**Inscribed instances**: scalar W_{1+∞}[Ψ] (`thm:w-infty-chiral-qg`); matrix Y(gl̂_N) at
generic Ψ (`thm:glN-chiral-qg`); EK quantum VOA for sl_2 (the worked example near line 8595).

**Cohomological vs cochain scope**: At cohomology, the equivalence is associator-independent
(GRT_1 acts trivially on H^0). At cochain level, the equivalence is a GRT_1-torsor; choosing
representatives requires fixing Φ. The statement above is at H^0 unless otherwise stated.

**Elliptic addendum**: The genus-1 collision residue construction yields a classical
r^ell(z, τ) of Belavin type, restricted to sl_2, with leading-order ℏ quantum correction.
CYBE is numerically checked, not algebraically proved at finite ℏ. The Felder dynamical
R-matrix and Fay trisecant identity provide an alternative formulation under vertex–IRF
correspondence; this alternative is conjectural in Vol I (FM38) and not currently inscribed.

**Toroidal scope**: No chapter-level inscription exists. The Schiffmann–Vasserot CoHA /
Miki DIM construction lives in the literature; its Vol I inscription is open frontier.

---

## Open Frontier

(OF1) **FF screening Argument B substitution**. Inscribe the argument that
∩ ker(Q_{α_i}) inherits a chiral coproduct from the Heisenberg parent, OR retain JKL26 in
the source and remove the FF-replacement claim from CLAUDE.md.

(OF2) **qdet centrality internalisation**. Either prove the chiral spectral-parameter
extension of Molev's antisymmetriser argument as an internal lemma `lem:qdet-central-chiral`,
or label the qdet centrality `\ClaimStatusProvedElsewhere` with explicit Molev attribution.

(OF3) **Felder vs Belavin elliptic**. Resolve the Felder/Belavin discrepancy. Either
inscribe a Felder-based elliptic theorem (with vertex–IRF transport) or restate the
status-table entry as Belavin-based with sl_2-restricted scope.

(OF4) **Toroidal chiral QG inscription**. Move the SV CoHA / Miki DIM construction from
standalone-only to a Vol I or Vol III chapter with explicit theorem environment and proof.

(OF5) **DS intertwining HZ-IV genuine independence**. Replace the spin-1 tautology
verification with an independent computation at spin-3 W generator (the non-tautological
sector) using `w3_gravitational_coproduct.py` with HPL terms inscribed.

(OF6) **GRT_1 canonicalisation**. Either restrict the chiral QG equivalence to H^0 (clean),
or fix a canonical associator class explicitly (Drinfeld–Bar-Natan rational, Knizhnik–
Zamolodchikov Φ_KZ, etc.) and propagate through all corollaries.

(OF7) **Antipode lifting clarification**. Rename `thm:chiral-qg-equiv` to
`thm:chiral-bialgebra-equiv` or add explicit "bialgebra-only, no antipode" remark in the
theorem title; propagate the rename atomically across three volumes.

(OF8) **Standalone hygiene**. Fix `\end{theorem>` typo in `seven_faces.tex:1017`. Run
`grep '\\end\{[^}]*>' standalone/` after every edit (FM7).

(OF9) **Phantom-anchor purge**. Either inscribe full theorem bodies for `thm:grt1-rigidity`,
`thm:chiral-qg-equiv-ordered`, `prop:sl2-yangian-triangle-concrete`,
`thm:w-infty-chiral-qg-completed`, `thm:chiral-qg-equiv-elliptic`,
`thm:chiral-qg-equiv-toroidal-formal-disk` in Vol I chapters, or delete the phantomsection
anchors and remove from CLAUDE.md status table.

---

## Coverage and discipline

Constitutional metadata hygiene: this audit document lives in `adversarial_swarm_20260417/`
and is not part of any typeset source. The labels `F1`–`F10`, `OF1`–`OF9` are
session-internal scaffolding. None of these tokens appear in the manuscript.

No edits to .tex performed. All findings are read-only.
