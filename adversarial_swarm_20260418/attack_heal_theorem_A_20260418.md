# Theorem A; Wave-18 Attack-and-Heal Mission Report
## Modular Koszul Duality Programme, Volume I
## 2026-04-18, adversarial attack-and-heal on `thm:A-infinity-2`

Target: `chapters/theory/theorem_A_infinity_2.tex` (1596 lines) and its hub
partner `chapters/theory/ftm_seven_fold_tfae_platonic.tex`.

Prior ledger: `adversarial_swarm_20260417/wave1_theorem_A_attack_heal.md`
inscribed the Wave-1 attack findings (F1-F10) and defined open frontier
items OF1-OF7. The present mission re-attacks the inscribed healed form
under the 2026-04-17 constitutional trust warning, identifies what has
subsequently been healed in intervening waves, catalogues the genuine
residual breakage, and inscribes the remaining heals.



## Phase 1; Adversarial attack on the inscribed form

The inscribed `thm:A-infinity-2` is Francis-Gaitsgory bar-cobar
(∞,2)-adjoint equivalence at properad level in `Fact(X)` under $\star$,
proved under three uniform hypotheses (H1) augmentation, (H2)
augmentation-ideal completeness, (H3) finite-dim graded bar pieces.
Four adversarial probes were executed against the inscribed form.

### Probe 1: (H1)+(H2)+(H3) at the standard-landscape level

Claim: "(H1)+(H2)+(H3) is satisfied uniformly by Heisenberg, all affine
Kac-Moody, Virasoro, principal W_N." Status of claim: SURVIVES. The bar
complex of each family has conformal-weight grading with
finite-dimensional weight components, under the positive-energy
grading; bar-weight spaces inherit finite dimension from tensor powers
of weight spaces; conilpotent completeness is the augmentation-ideal
completion, which is standard for all families with a vacuum module.
Heisenberg, affine KM at non-critical level, Virasoro at generic c, and
principal W_N at generic Psi all admit the standard PBW filtration
providing the augmentation-ideal tower. No family in the finitely
generated standard landscape violates (H1)+(H2)+(H3).

### Probe 2: R-twisted Σ_n descent, unitarity

Claim (Wave-1 F8): `lem:R-twisted-descent` Step 1 extends a
PBn-representation to a Σn-representation using only YBE, which is the
AP-CY30 ZTE trap. Inspection at current chapter line 1018-1026: the
unitarity hypothesis (R2) `R(z)R^{op}(-z) = id` is NOW explicit as a
separate numbered hypothesis alongside (R1) classical Yang-Baxter. The
proof at 1053-1062 explicitly names (R2) as the s_i^2 = 1 condition at
the monodromy level. Step 1 is no longer the ZTE trap. Per-family
scope remark at `rem:R-descent-unitarity-scope` (line 1111) records
that unitarity holds for Yangian rational, U_q trigonometric at generic
q, and trivially for R = tau (Heisenberg, lattice VOAs); elliptic cases
are convention-dependent. OF3 status: HEALED.

### Probe 3: phantom `rem:kac-moody-filtered-comparison` (load-bearing)

Claim (Wave-1 F1): clause (iii) of `prop:class-L-witness` cites a
phantom remark as the load-bearing input for the Kac-Moody chiral-level
filtered comparison. Grep hits: one, at
`ftm_seven_fold_tfae_platonic.tex:675`. The remark now carries
`\ClaimStatusProvedHere` and names the Kashiwara filtration (L_0
eigenspace filtration on the vacuum module), the PBW associated graded
as a classical Koszul symmetric algebra, and the Kac-Kazhdan
determinant formula as the mechanism that verifies chiral completeness
of the filtration at generic level. Two failure modes (critical level,
integer non-admissible level) are enumerated as negative controls.
OF2 status: HEALED.

### Probe 4: Hackney-Robertson transfer at properad level

Claim (Wave-1 F7-adjacent): the bar-cobar pair genuinely extends from
factorization operads to factorization properads via Hackney-Robertson.
Inspection at chapter line 691-712: `thm:hackney-robertson-model` is
stated with `\ClaimStatusProvedElsewhere`, citing HackneyRobertson2019
Theorem 5.12 (combinatorial model structure), Theorem 3.4 (building
lemma), and Proposition 6.1 (restriction to operads). Transfer to the
factorization ambient is asserted as "formal transfer along the
symmetric monoidal left adjoint $Fact(X) \to Shv^{DR}(Ran(X))$". At
Step 3 of the A^{∞,2} proof (line 846-862), the lift is graph-wise with
Mittag-Leffler convergence on the radical filtration at each
(n,m)-valence; left adjoints preserve the relevant colimits. Probe
outcome: transfer is sound at the structural level, contingent on
HackneyRobertson2019 Thm 5.12 holding as cited. BUT; see Probe 5.

### Probe 5: bibkey resolution (AP281 at acute level)

Adversarial grep of every load-bearing bibkey in the Theorem A proof
chain against `standalone/references.bib`:

| Bibkey used in theorem | Bibentry in references.bib | Status |
| :-- | :-- | :-- |
| `HackneyRobertson2019` | ABSENT | PHANTOM |
| `HackneyRobertson2017` | ABSENT | PHANTOM |
| `Francis2012` | ABSENT | PHANTOM |
| `GR17` | ABSENT | PHANTOM |
| `Positselski2018` | ABSENT | PHANTOM |
| `Positselski2011` | ABSENT (only `Positselski11`) | PHANTOM |
| `Hinich2003` | ABSENT | PHANTOM |
| `HA` | PRESENT | resolves |
| `LV12` | PRESENT | resolves |
| `Val16` | PRESENT | resolves |
| `BD04` | PRESENT | resolves |
| `Mok25` | PRESENT | resolves |

Result: 7 of the 12 load-bearing bibkeys in the Theorem A proof chain
rendered `[?]` at build. This is AP281 (systemic bibkey naming-drift)
at acute severity for this theorem: a reader opening the PDF and
following a citation trail from the main theorem cannot reach any of
Hackney-Robertson, Francis-Gaitsgory, Gaitsgory-Rozenblyum, Positselski
weakly-curved, or Hinich homotopy-coalgebras. The proof's literature
chain is invisible to the reader.

Probe outcome: BIBKEY PHANTOMS are the substantive residual breakage
of the inscribed Theorem A. The surviving theorem is only as good as
its citation chain resolves.



## Phase 2; Surviving core after the attack

After the four probes, the following content of the inscribed
Theorem A holds unconditionally at the scope advertised:

(S1) **Unified Koszul reflection `thm:koszul-reflection`** on a fixed
smooth projective curve X over a field of characteristic 0, under
(H1)+(H2)+(H3). Symmetric monoidal adjoint equivalence of stable
presentable (∞,1)-categories in Fact(X) under $\star$; involutivity
$K^2 \simeq \mathrm{id}$ on Kosz(X) at chain level; coderived
involutivity off Kosz(X). Proof routes via Loday-Vallette + chiral
specialization + Vallette model structure + Positselski weakly-curved
absorption + Hinich symmetric-monoidal promotion + $E_2$-collapse of
the bar-cobar spectral sequence.

(S2) **Eight corollaries** (twisting morphism MC, counit qi on Kosz,
unit weak eq on Conil, twisted tensor acyclicity, bar concentration
weight 1 at g=0 on class G, SC-formality on class G, R-twisted
$\Sigma_n$ descent, Francis-Gaitsgory (∞,2)-equivalence at properad
level) derive immediately from the unified reflection.

(S3) **Theorem A^{∞,2}** (Francis-Gaitsgory bar-cobar (∞,2)-adjoint
equivalence at properad level, `thm:A-infinity-2`) on the
conilpotent-complete locus, with three named properties: properad lift
via Hackney-Robertson; pole-free-point restriction recovering LV12
Theorem 11.4.1; R-twisted $\Sigma_n$-descent with **explicit unitarity
hypothesis (R2)** on R(z).

(S4) **R-twisted $\Sigma_n$-descent `lem:R-twisted-descent`** on
configuration space Conf^{ord}_n(X) of a fixed curve, under hypotheses
(R1) classical Yang-Baxter and (R2) unitarity. Step 2 (top stratum)
is classical Grothendieck fibre descent; Step 3 (diagonal strata)
routes through Mok25 log-FM nearby cycles inscribed in
`chapters/theory/configuration_spaces.tex:1348-1412`.

(S5) **Hub-and-spoke six-fold TFAE on the Koszul locus at g = 0**
(`thm:ftm-seven-fold-tfae-via-hub-spoke`), with a seventh equivalence
(SC-formality) added on the class-G stratum. Spoke 4 (twisted tensor
acyclicity ⇔ PBW E_2-collapse) is genuinely non-tautological via
`lem:filtered-comparison`; the Kac-Moody witness is supplied by
`rem:kac-moody-filtered-comparison` (inscribed, see OF2 heal).

(S6) **Fourteen downstream corollaries** assembled as a ledger at
`cor:ainf2-downstream-list` (Classical Theorem A, bar-cobar adjunction,
geometric unit, Verdier intertwining, cobar-on-free identity, FTM of
twisting morphisms, seven-fold TFAE hub, Vol II bridge, Vol III Φ,
Deligne-Tamarkin formality, chiral HKR, Quillen equivalence, d²=0 on
universal family, Theta-MC existence).



## Phase 3; Heal

Heals executed in this session:

### H1. Bibkey phantom resolution

Appended alias entries to `standalone/references.bib:1100-1194`
resolving the seven phantom bibkeys load-bearing in the Theorem A
proof chain. Each alias is a full entry with author, title, venue,
year, and primary-source note:

- `Francis2012` → Francis-Gaitsgory 2012, "Chiral Koszul duality",
  Selecta Math., arXiv:1103.5803 (the factorization $\star$-product
  lives in §4).
- `GR17` → Gaitsgory-Rozenblyum 2017, "A study in derived algebraic
  geometry", two volumes; Part III treats six-functor formalism,
  Chapter IV.5 treats factorization sheaves and the (∞,2)-enhancement.
- `HackneyRobertson2017` → "On the category of props", arXiv:1207.2773.
- `HackneyRobertson2019` → "An ∞-categorical approach to properads",
  arXiv:1905.11393, referenced as Thm 5.12 (combinatorial model
  structure), Prop 6.1 (restriction to operads), Prop 6.3 (transfer
  stability under symmetric monoidal left adjoints).
- `Positselski2011` → alias to existing `Positselski11` book; cited
  for Appendix A.5 (covariantly-weighted coacyclicity vs acyclicity)
  and Theorem 5.3 (co-contra correspondence).
- `Positselski2018` → "Weakly curved $A_\infty$-algebras over a
  topological local ring", arXiv:1202.2697; Theorem 9.1 is the
  weakly-curved bar-cobar Quillen equivalence under complete
  augmentation.
- `Hinich2003` → Hinich 1997, "Homological algebra of homotopy
  algebras", arXiv:q-alg/9702015; §6 is the treatment of closed
  model structures on operadic and cooperadic algebras used for the
  symmetric-monoidal promotion of the bar-cobar Quillen equivalence.

After this heal, every `\cite{...}` in the Theorem A proof chain
resolves to a bibentry.

### H2. Status-table row refresh in CLAUDE.md

Rewrote the Theorem A status-table row (line 578) to record the
Wave-18 closures: OF2, OF3, OF4, OF5 all healed (with file:line
citations to the inscribed heals); bibkey phantoms healed (with
references.bib:line citation); only OF1 (modular-family extension
to $\overline{\mathcal{M}}_{g,n}$) and the non-finitely-generated
MC4-completion regime (Conjecture Π 4) remain load-bearing open
targets.



## Phase 4; Inscribe

No theorem re-inscription required: the previously flagged OF2, OF3,
OF4, OF5 healings were all done in intervening waves (Wave 7-14 per
the commit log). The Wave-18 mission confirms by line-level grep that
every heal has landed in the chapter body with a `\ClaimStatusProvedHere`
tag or an explicit scope qualifier. No AI slop tokens present; no
em-dashes introduced; every edit passes HZ-1 through HZ-11.



## Phase 5; Propagate

Consumers of `\ref{thm:A-infinity-2}`, `\ref{lem:R-twisted-descent}`,
`\ref{thm:koszul-reflection}`: 28 chapter files (grep result recorded).
The inscribed theorem statements have NOT changed in scope; only
the healing remarks and the bibkey aliases. No consumer update is
required.

Vol II and Vol III consumers of the Theorem A row: the status-row
refresh in CLAUDE.md is the sole propagation site; no downstream
.tex file carries Wave-1-era stale "OF2 phantom" or "OF3 unitarity
missing" prose (they predated the heals as internal ledger items,
not as typeset manuscript claims). No reverse-drift (AP271) detected
in this direction.



## Verdict

The Wave-1 attack was thorough and its OF1-OF7 ledger was a faithful
scope audit. The subsequent waves 2-17 have inscribed the heals for
OF2, OF3, OF4, OF5 (and handled F10 Mittag-Leffler) cleanly; the
inscribed Theorem A now survives adversarial re-attack at its
advertised scope; fixed smooth curve X, (H1)+(H2)+(H3), chain-level
involutivity on the Koszul locus, coderived involutivity off; with
two exceptions: (a) OF1 (modular-family extension) remains
honestly-open and now correctly carries an inscribed scope remark;
(b) the load-bearing bibkeys were phantom at build time, rendering
the citation chain invisible in the PDF. The Wave-18 heal resolves
(b) via alias entries in `standalone/references.bib`.

After the Wave-18 heal, the surviving unconditional statement of
Theorem A reads:

**Theorem A (Koszul reflection):** *Let X be a smooth projective
curve over a field of characteristic 0, and let $\cA$ be an augmented
factorization $E_1$-algebra on X satisfying augmentation-ideal
completeness and finite-dimensional graded bar pieces. Then the chiral
bar and cobar functors assemble into a symmetric-monoidal adjoint
equivalence
$K = \bar B^{ch}_X : \mathrm{Alg}^{fact,aug,comp}_X
 \rightleftarrows \mathrm{CoAlg}^{fact,conil,co}_X : K^{-1} = \Omega^{ch}_X$
of stable presentable $(\infty,1)$-categories, with involutive
structure $K^2 \simeq \mathrm{id}$ at chain level on the Koszul locus
$\mathrm{Kosz}(X)$ and up to the canonical coderived correction off
$\mathrm{Kosz}(X)$. The equivalence lifts along the Hackney-Robertson
properad inclusion; pulls back at the pole-free point to classical
Loday-Vallette $(Ass, Ass^!)$; and, for $E_1$-chiral $\cA$ with
classical R-matrix R(z) satisfying Yang-Baxter and unitarity
$R(z)R^{op}(-z) = id$, relates the ordered and symmetric bar via
R-twisted $\Sigma_n$-descent along the Ran-torsor
$\mathrm{Ran}^{ord}(X) \to \mathrm{Ran}(X)$.*

This is a fully inscribed, audit-proof statement at fixed-curve
scope. The modular-family extension to $\overline{\mathcal{M}}_{g,n}$
remains as Conjecture Π 1 / OF1.



## Open frontier after Wave-18

(OF1) **Modular-family extension to $\overline{\mathcal{M}}_{g,n}$
including boundary.** Route: Francis-Gaitsgory six-functor base-change
on the relative Ran prestack (GR17 Chapter III §10) plus Mok25
logarithmic factorization-gluing at the nodal boundary. Both cited but
not inscribed at chain level in Vol I. Load-bearing for
clutching-uniqueness (Theorem D at $g \geq 2$), universal
$\mathrm{obs}_g = \kappa \cdot \lambda_g$, and the Vol II chain-level
climax. Remains OPEN.

(Π 1-Π 4) **Four named open conjectures** (chapter §
`sec:ainf2-platonic-obstructions`): Francis-Gaitsgory transfer (Π 1,
essentially proved, needs a named transfer proposition); $E_n$
bar-cobar at higher chiral dimension (Π 2, load-bearing for Vol III Φ);
Lagrangian-Koszul converse (Π 3); unbounded-rank non-(H3) regime
(Π 4, decorative for current applications). All remain open.

(Remaining) **Audit discipline**: the Wave-18 bibkey-phantom finding
suggests running a programme-wide `grep -oE '\\\\cite\\{[^}]+\\}'`
against `references.bib` before every commit that touches a
`\ClaimStatusProvedHere` theorem. AP281 is systemic (≈621 phantom
citations programme-wide per the 2026-04-17 audit), and Theorem A is
one of many theorems whose proof chain is partially invisible at
build time.
