# Wave 1 Adversarial Audit: Theorem C (Quantum Complementarity)

**Target.** Vol I status table claim: "Theorem C PROVED unconditionally on
Koszul locus (C0, C1); C2 Lagrangian upgrade conditional only on BV package",
with nine 2026-04-16 strengthening inscriptions: T1 `lem:derived-center-koszul-equivalence`
(brace dg / E_2 Deligne--Tamarkin / H^0 naive); T2 `prop:perfectness-standard-landscape`
UNCONDITIONAL family-by-family (Heis finite, KM via Kac--Kazhdan, Vir generic c,
W_N via Fateev--Lukyanov, lattice via theta/eta, betagamma via character);
T3 C1 reflexivity unconditional once perfectness is a theorem; T4
`thm:theorem-C-g0` separate +3 shift resolution; T5 C2 hypothesis pinning;
T6 C0 unconditional once T2 absorbs perfectness; T7 MC5 closes class-M C2(iii)
weight-completed; T8 `prop:delta-f-cross-w3-g2 = (c+204)/(16c)`; T9
`thm:C-PTVV-alternative` genuinely independent C1 at g >= 2.

Source files audited: `chapters/theory/higher_genus_complementarity.tex`
(`lem:perfectness-criterion` line 304; `thm:fiber-center-identification`
line 388; `thm:quantum-complementarity-main` line 540;
`thm:shifted-symplectic-complementarity` line 2017; `prop:ptvv-lagrangian` line 2194);
`chapters/theory/higher_genus_foundations.tex` (`prop:gauss-manin-uncurving-chain`
line 368); `chapters/theory/higher_genus_modular_koszul.tex` (line 246);
`standalone/multi_weight_cross_channel.tex` (`prop:delta-f-cross-w3-g2`
line 608); `standalone/five_theorems_modular_koszul.tex` (lines 2911--2956,
the Wave-14 narration); `standalone/theorem_index.tex`
(lines 2375--2379, the index claims pointing at `theorem_C_refinements_platonic.tex`).

## ATTACK

### F1 (CRITICAL). Five of the nine "wave-14 inscriptions" T1, T2, T4, T6, T9 are PHANTOM.

`standalone/theorem_index.tex:2375--2379` lists `lem:derived-center-koszul-equivalence`,
`prop:perfectness-standard-landscape`, `thm:theorem-C-g0`, `thm:C-PTVV-alternative`
all with `\detokenize{chapters/theory/theorem_C_refinements_platonic.tex}`.
That file does NOT EXIST (`ls: No such file or directory`). Grepping all of
`chapters/` for these labels yields hits only inside `chapters/frame/preface.tex`
(at line 5066 they appear as `\phantomsection\label{...}` placeholders so that
preface `\ref` does not break) and inside `chapters/frame/programme_overview_platonic.tex`
(narrative reference). The actual proof bodies advertised in the wave-14 narrative
are NOT inscribed anywhere in the Vol I theory chapters.

The status table at CLAUDE.md says "9 strengthening inscriptions (2026-04-16)";
on the source the count of *inscribed* strengthenings is FOUR (T3, T5, T7, T8 are
narrative claims about the existing chapter; T8 is the only fully inscribed
one, and lives in `standalone/multi_weight_cross_channel.tex`, not in a body
chapter). The other five are paper-promises pointing at a file that was never
created. This is the same `prop:delta-f-cross-w3-g2` standalone-only siting
flagged in the parallel Theorem D audit (D-attack F7).

### F2. `lem:perfectness-criterion` is a CONDITIONAL lemma, not the unconditional `prop:perfectness-standard-landscape` T6 advertises.

The actually inscribed lemma at `higher_genus_complementarity.tex:304` proves
perfectness *under two hypotheses*: (i) PBW filterability of `\bar B^{(g)}(\cA)`
with Koszul-acyclic `gr_F`; (ii) finite-dimensional flat fiber cohomology
`H^n(\bar B^{(g)}_{flat}(\cA)|_\Sigma) < \infty` for all n at every closed point
of `\overline{\mathcal{M}}_g`. Both hypotheses are family-dependent. (i) holds
for the standard landscape via the bar-degree (= weight) filtration only because
the modular Koszul axiom MK1 is satisfied -- itself part of the *hypothesis*
of being a "modular pre-Koszul datum". (ii) is the non-trivial input: it asserts
finiteness *at every* closed point including boundary strata of M-bar_g, not
merely at smooth fibers. The advertised "T2 unconditional family-by-family"
verification (Heisenberg via finite weight, KM via Kac--Kazhdan, Vir at generic c,
W_N via Fateev--Lukyanov, lattice via theta/eta, betagamma via character) is the
sketch of what would *need* to be done to discharge hypothesis (ii) for each
family; it is NOT inscribed as proof. Each citation needs to be specifically
extended to *boundary* fibers of M-bar_g (nodal curves), where conformal blocks
typically degenerate -- and *that* is the substantive content of perfectness on
the moduli compactification, not on the smooth Teichmuller part.

### F3. T4 `thm:theorem-C-g0` "+3 shift resolution" silently invokes a Verdier pairing of the WRONG degree at g=0.

The narrative at `five_theorems_modular_koszul.tex:2934--2937` claims:
"at g=0, M-bar_{0,3} = pt, the involution acts trivially, Q_0(A^!)=0, and the
Verdier pairing is of degree 0 (not -3)." Cross-check the inscribed C1
`thm:quantum-complementarity-main` lines 568--577: "For g >= 1, Verdier duality
induces a cochain-level pairing of cohomological degree -(3g-3)". Substitute
g=0 in the formula 3g-3 to get -3 *positive*, i.e. a +3 shift. The narrative
"Verdier pairing of degree 0 (not -3)" SILENTLY DROPS the (3g-3) shift at g=0
without explanation. The actual content at g=0 in the inscribed C1 is:
M-bar_{0,3}=pt, the unique point class is sigma-fixed, so Q_0(A) = H^0(pt, Z(A))
and Q_0(A^!) = 0 (lines 604--608). This is correct; *but* it is NOT a "Verdier
pairing of degree 0" -- there is *no* Verdier pairing at g=0 in this inscription,
because the involution is trivial. The +3 shift "contradiction" is not a
contradiction in the inscribed text; it is an artifact of misreading the formula
(3g-3) at g=0. T4 is a PHANTOM resolution of a non-issue and is at risk of
introducing a phantom Verdier-pairing-of-degree-0 if anyone tries to inscribe it.

### F4. T9 `thm:C-PTVV-alternative` cannot be genuinely independent because the inscribed PTVV ingredient `prop:ptvv-lagrangian` already DEPENDS on `thm:quantum-complementarity-main`.

`prop:ptvv-lagrangian` at `higher_genus_complementarity.tex:2194` is the only
inscribed PTVV statement. Its proof body (lines 2238--2247) writes:
"Condition (b): Since C_g = Q_g(A) ⊕ Q_g(A^!) (Theorem~\ref{thm:quantum-complementarity-main})".
The PTVV embedding is a CONSEQUENCE of the eigenspace decomposition, not an
INDEPENDENT route to it. Any "thm:C-PTVV-alternative" built atop this proposition
would fail HZ-IV import-time disjointness: it would call C1 to prove C1.
Same structural issue identified in parallel D-audit F6.

The genuine PTVV-independent route would be: construct R-Map(M-bar_g, BG_A)
mapping stack with explicit anti-symplectic Verdier involution at the
*derived-stack* level (no pre-passage through Q_g eigenspaces); prove
non-degeneracy of the induced shifted form intrinsically; then *derive* the
eigenspace decomposition. As advertised in `five_theorems_modular_koszul.tex:2953`,
this would require a fresh inscription using PTVV+Calaque--Haugseng--Scheimbauer
machinery; it is NOT in the source.

### F5. C0 `thm:fiber-center-identification` is HYPOTHESIS-CONDITIONED on the Koszul locus AND on `prop:gauss-manin-uncurving-chain` cancellation, which uses the Lagrangian property of A-cycles.

The inscribed C0 at line 388 reads "Then [conditions (i)-(iii) hold]" given that
(a) A carries a modular pre-Koszul datum, AND (b) `R\pi_{g*} \bar B^{(g)}_flat(A)`
is perfect (via lem:perfectness-criterion -- see F2 above). The kappa=0 recovery
clause (iii) is genuinely unconditional. The Koszul-locus clause (ii) is
conditional on perfectness (F2). The chain-level uncurving identity in
`prop:gauss-manin-uncurving-chain` Step (ii) at line 412 uses
"the Lagrangian property of the A-cycle subspace cancels the Arakelov form
against the period correction". This is *one* explicit choice of polarization;
the proof asserts but does not check that the cancellation is independent of
the polarization choice. For class M (Vir, W_N) at generic c the cancellation
is fine; for non-uniform-weight multi-generator families the period correction
acquires cross-terms that the present uncurving identity does not handle.
This is the same uncurving issue that propagates into the cross-channel
correction `delta F_g^cross` of Theorem D.

### F6. T8 `prop:delta-f-cross-w3-g2 = (c+204)/(16c)` is INSCRIBED and verified, but only at (W_3, g=2). The status-table sentence "explicit cross-channel correction" is sound at this single point; for g>=3 or other multi-weight families it is OPEN.

(Survives.) The proposition body in `multi_weight_cross_channel.tex:608--641`
sums sunset (D), theta (F), bridge-loop (E) graph contributions on M-bar_{2,0};
the arithmetic 15/(2c) + 1/16 + 21/(4c) = (c+204)/(16c) is correct.
Cross-checked against the parallel D-audit which also confirmed five verification
paths (graph sum, propagator variance, large-c limit, complementarity, parity).

### F7. T1 `lem:derived-center-koszul-equivalence` (brace dg / E_2 Deligne--Tamarkin / H^0 naive recovery) is the cleanest healing route but is PHANTOM.

The narrative is mathematically plausible (Deligne--Tamarkin produces an E_2
algebra structure on Hochschild cochains; H^0 of a brace dg algebra is the
naive center). The inscribed Vol I has `prop:gauss-manin-uncurving-chain`
which gives chain-level uncurving but does NOT establish the brace dg equivalence
between Z^der_ch(A) and Z^der_ch(A^!). The Koszul reflection theorem upstream
(climax) gives kappa = -c_ghost(BRST), which is a SCALAR identity, not the
chain-level brace dg equivalence T1 advertises. T1 would be the right next
inscription, but it is a future direction, not a present theorem.

## SURVIVORS

(S1) **C0 in coderived form, kappa=0 recovery, Heisenberg / Virasoro / single-generator
families.** `thm:fiber-center-identification` clause (i) (coderived) and clause (iii)
(kappa=0 ordinary recovery) are inscribed and unconditional. For families with
kappa=0 (Kac--Moody at level k=0; Vir at c=0; betagamma in particular conventions)
the ordinary derived pushforward identification with the center local system
is solid.

(S2) **C1 H-level eigenspace decomposition `lem:involution-splitting`.** The
characteristic-zero linear-algebra splitting under an involution is unconditional;
the chiral-Koszul realization at H-level holds with no further hypothesis.

(S3) **Verdier perfect duality at g >= 1**, *given* the Verdier-duality-on-FM
input (clauses (ii) of `thm:quantum-complementarity-main`). This is standard
algebraic geometry, no preprint dependence (cf.
`rem:theorem-c-mok-independence` line 628).

(S4) **PTVV Lagrangian embedding** of Q_g(A), Q_g(A^!) inside C_g as a
*consequence* of C1 (not an independent route): `prop:ptvv-lagrangian`,
inscribed and correct under H-level decomposition.

(S5) **`prop:delta-f-cross-w3-g2 = (c+204)/(16c)`** at the single point
(W_3, g=2). Five verification paths.

(S6) **g=0 statement Q_0(A) = H^0(pt, Z(A)), Q_0(A^!) = 0.** Inscribed correctly
inside `thm:quantum-complementarity-main` lines 604--608; does NOT need the
phantom T4 "Verdier pairing of degree 0" framing.

(S7) **C2 conditional shifted-symplectic complementarity**
`thm:shifted-symplectic-complementarity`, properly tagged
`\ClaimStatusConditional`, hypotheses pinned (`thm:config-space-bv` +
`thm:bv-functor` + Verdier comparison + bar-chart Lagrangian lift). The
T5 narrative pinning of C2 hypotheses is consistent with the inscribed text.

## PLATONIC RECONSTITUTION

**Theorem C (Sharpened, 2026-04-17).**

*(C0a)* **Coderived fiber-center, unconditional.** For every modular Koszul
chiral algebra A on the Koszul locus, the curved fiber bar family
`(\bar B^{(g)}(A), d_fib)` determines a well-defined coderived object;
`prop:gauss-manin-uncurving-chain` supplies a strict flat representative
`(\bar B^{(g)}(A), D_g)` in the derived category.

*(C0b)* **Ordinary derived realization, conditional on perfectness.** If
`R\pi_{g*}` of the strict flat representative is perfect on M-bar_g, then
`H^0` recovers the center local system Z_A and `H^q = 0` for q ≠ 0.
Perfectness for the standard landscape is a *family-by-family hypothesis*,
not currently inscribed; the wave-14 narrative T2 supplies the family-by-family
sketches that need to be discharged for each family at *boundary* strata of
M-bar_g.

*(C0c)* **Kappa=0 recovery, unconditional.** When kappa(A) = 0, the curved
and flat representatives coincide as ordinary complexes; (C0b) holds without
the perfectness hypothesis.

*(C1)* **Eigenspace decomposition at H-level, unconditional on the Koszul locus.**
For every chiral Koszul pair (A, A^!) and every g >= 0:
- *(g=0)* Q_0(A) = H^0(pt, Z(A)), Q_0(A^!) = 0. No Verdier pairing -- the
  "+3 shift" is a misreading of (3g-3) at g=0 and not a contradiction.
- *(g >= 1)* `\mathbf C_g(A) ≃ \mathbf Q_g(A) ⊕ \mathbf Q_g(A^!)` with Verdier
  pairing of cohomological degree -(3g-3) and Lagrangian splitting; perfect
  duality `\mathbf Q_g(A) ≃ \mathbf Q_g(A^!)^\vee[-(3g-3)]`.

*(C2)* **Shifted-symplectic bar-side upgrade, conditional on the BV package.**
`thm:shifted-symplectic-complementarity` upgrades C1 to (-1)-shifted symplectic
on the formal moduli problem, requiring (i) BV bracket on `\bar B^ch(A)`
(`thm:config-space-bv`); (ii) bracket-compatible Verdier comparison
(`thm:bv-functor`); (iii) bar-chart Lagrangian lift
(`lem:bar-chart-lagrangian-lift`). On the uniform-weight lane this is sufficient;
multi-weight requires a corrected pairing
`omega_g^corr = omega_g^diag + omega_g^cross` indexed by the same graphs that
define `delta F_g^cross` (research programme, not inscribed).

*(C2')* **Multi-weight scope.** `delta F_2^cross(W_3) = (c+204)/(16c)` proved
at (W_3, g=2). All other (algebra, genus) pairs with cross-channel correction:
open frontier.

## AP225 VERDICT (C-route)

The proper "platonic clutching lemma" closing AP225 from the C-route is a
**Verdier-eigenspace clutching uniqueness**: under hypotheses (i) Q_1(A) = ker(σ-1)
on M-bar_{1,1}; (ii) separating clutching ξ_h^* respects the Verdier eigenspace
decomposition with multiplicativity Q_g = Q_h ⊠ Q_{g-h} on the boundary stratum
δ_h ⊂ M-bar_g; (iii) non-separating clutching ξ_irr^* sends Q_g to Q_{g-1}·ψ,
the Q_g(A) eigenspace decomposition is uniquely determined modulo the
numerical-equivalence kernel N^g(M-bar_g). On the socle quotient
R^g(M-bar_g) / N^g(M-bar_g) this is *unconditional via Graber--Vakil*; lifting
to on-the-nose equality in R^g(M-bar_g) requires the lambda_g-conjecture for
g >= 3. The C-route conclusion matches the D-route conclusion of the parallel
audit: AP225 is closed on the *socle quotient* not in the *tautological ring
itself* for g >= 3.

## OPEN FRONTIER

(OF1) **The phantom file `theorem_C_refinements_platonic.tex`.** Five wave-14
inscriptions T1, T2, T4, T6, T9 are advertised in `theorem_index.tex` but not
inscribed in any body chapter. Either inscribe (priority on T1 brace dg
equivalence and T2 family-by-family perfectness on boundary strata) or retract
the wave-14 narrative claim of "9 strengthenings".

(OF2) **Boundary-stratum perfectness for the standard landscape.** Family-by-family
verification of clause (ii) of `lem:perfectness-criterion` at all closed
points of M-bar_g, including nodal degenerations. Heisenberg and uniform-weight
free fields are immediate; Vir at minimal-model points c_{p,q}, KM at admissible
levels, W_N at non-generic c need separate analysis (Arakawa C_2-cofiniteness
input, not currently cited at this site).

(OF3) **Genuinely independent PTVV alternative for C1.** Present
`prop:ptvv-lagrangian` cites C1; an *alternative* route via mapping stack
R-Map(M-bar_g, BG_A) without back-citation would close T9 honestly and yield
an HZ-IV-decoratable proof.

(OF4) **Multi-weight C2 corrected pairing `omega_g^cross`.** Construct from
the cross-channel graph sum, prove Verdier-anti-invariance and non-degeneracy,
test on (W_3, g=2). Closes the C2 multi-weight gap.

(OF5) **Lambda_g-conjecture residue for AP225.** Same as D-route OF2: the
on-the-nose lift from socle to R^g requires algebraic-geometric input external
to the Koszul programme.

**Verdict.** Theorem C is unconditional in coderived form and at H-level on
the Koszul locus, with an inscribed BV-conditional shifted-symplectic upgrade.
The status-table phrase "9 strengthening inscriptions" should be revised to
"4 inscribed (T3, T5, T7, T8); 5 phantom pending creation of
`theorem_C_refinements_platonic.tex` (T1, T2, T4, T6, T9)". The C2-route to
AP225 closes only on the socle quotient for g >= 3, matching the D-route
verdict.
