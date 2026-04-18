# D$^2$ = 0 convolution family theorem: adversarial audit and heal

## Modular Koszul Duality Programme, Volume I
## 2026-04-18; attack-and-heal on CLAUDE.md D$^2$ = 0 status row

Author: Raeez Lorgat.

> **RETRACTED 2026-04-18** per Wave-X Mok25 programme-wide audit
> (`adversarial_swarm_20260418/attack_heal_mok25_programme_audit_20260418.md`).
> Phase 2 finding below ("The `Mok25` bibkey resolves against no primary
> source", ~line 119-134) is SUPERSEDED. Mok25 is REAL: Siao Chi Mok,
> arXiv:2503.17563, "Logarithmic Fulton--MacPherson configuration spaces"
> (March 2025, v2 May 2025). The "phantom-bibkey" inheritance framing for
> D$^2$ = 0 is retracted. The load-bearing dependency on Mok25 for the
> ambient log-FM construction remains a single-preprint pillar (AP1241),
> but the mechanism is NOT fabricated. Correct heal: bibkey harmonization
> (Siao Chi Mok, arXiv:2503.17563, 2025) + AP1241 scope registration.

Target: the CLAUDE.md Theorem Status row

```
| D^2=0 | PROVED | Convolution on universal family over M̄_{g,n}; ambient Mok25 log FM. |
```

flagged for audit in parallel with the Wave-18 Theorem-A modular-family
attack (OF1), which surfaced the `Mok25` bibkey as an AP281 phantom
bibliographic citation with no locatable primary source. If the CLAUDE.md
row genuinely commits D$^2$ = 0 to an ambient construction that depends
on Mok25, the row's PROVED status is inherited-phantom; if the row
conflates two logically independent theorems, the row needs scope
separation.

AP block: AP1341-AP1360, used sparingly.

## Phase 1. Locate and read the theorem bodies

Two distinct theorems carry the `D^2 = 0` headline in
`chapters/theory/higher_genus_modular_koszul.tex`:

- `thm:convolution-d-squared-zero` at line 32404, `\ClaimStatusProvedHere`,
  title "Square-zero: convolution level", two-line proof.
- `thm:ambient-d-squared-zero` at line 32418, `\ClaimStatusProvedHere`,
  title "Square-zero: ambient level", four-step proof depending on
  Mok25.

### 1.1 Convolution-level theorem body (line 32404-32416)

Statement: on the modular convolution algebra
$\mathfrak{g}^{\mathrm{mod}}_{\cA}$, the differential satisfies
$D^2 = 0$.

Proof, verbatim:

> $D$ is the transport of the boundary operator $\partial$ on
> $C_*(\overline{\mathcal{M}}_{g,n})$ through the Hom functor, and
> $\partial^2 = 0$ on the chain complex of any topological space.

No dependency on Mok25. No dependency on a log-FM compactification.
No dependency on planted-forest corrections. The only input is the
universal fact $\partial^2 = 0$ on the singular-chain complex of any
topological space, specialised to the Deligne-Mumford compactification
$\overline{\mathcal{M}}_{g,n}$ (which is a topological space whatever its
algebro-geometric subtleties). This proof is unconditional; it was
unconditional before the programme inscribed Mok25; it remains
unconditional after any retraction of Mok25.

### 1.2 Ambient-level theorem body (line 32418-32566)

Statement: on the ambient complementarity algebra
$\mathfrak{g}^{\mathrm{amb}}_{\cA}$, the five-component differential
$D_{\cA} = d_{\mathrm{int}} + [\tau_{\cA},-] + d_{\mathrm{sew}} +
d_{\mathrm{pf}} + \hbar\Delta$ satisfies $D_{\cA}^2 = 0$. Fiberwise
curvature is $\dfib^2 = \kappa(\cA)\cdot\omega_g$ with
$\omega_g = c_1(\lambda)$ the Hodge class.

Proof architecture:

- Step 1. The correct carrier is Mok's relative log-FM space
  $\operatorname{FM}_k(\cC_{g,n}/\overline{\cM}_{g,n})$ of the universal
  stable curve.
- Step 2. Collision part: $\partial_{\mathrm{coll}}^2 = 0$ by fiberwise
  Arnold cancellation. Unconditional.
- Step 3. Degeneration part and curvature: pushforward along the
  universal curve identifies the base-boundary defect with
  $\omega_g = c_1(\lambda)$, scaled by $\kappa(\cA)$.
- Step 4. Total differential: expand $\partial^2 = 0$ on
  $\operatorname{FM}_k(\cC_{g,n}/B)$ with respect to the collision /
  degeneration decomposition; the three pieces are precisely the
  diagonal $d_B^2 = 0$, the fiberwise curvature
  $\kappa(\cA)\cdot\omega_g$, and the mixed codimension-2 cancellation
  that rewrites as the ambient master identity.

Step 4 is the load-bearing step and rests on two Mok25 claims:
(a) normal-crossings boundary of $\operatorname{FM}_k(\cC_{g,n}/B)$;
(b) stratification by planted forests.

### 1.3 Inscribed Mok25 scope remark (line 32568-32606)

The chapter already carries an honest scope remark,
`rem:mok-dependency`, which reads in part:

> Theorem~\ref{thm:ambient-d-squared-zero} rests on a single external
> package: Mok's relative log Fulton--MacPherson compactification
> together with its degeneration formula (\cite[Theorem 3.3.1, Theorem
> 5.3.4]{Mok25}). [...] This result is not proved in this monograph.
> If \cite{Mok25} is revised or the result is not confirmed by
> publication, Theorem \ref{thm:ambient-d-squared-zero} reverts to
> conditional status, and the following downstream results are
> similarly affected: [planted-forest depth filtration; log clutching
> law; quartic clutching construction; all ambient-level cross-term
> cancellations]. By contrast, the convolution-level $D^2 = 0$
> (Theorem~\ref{thm:convolution-d-squared-zero}) is unconditional: it
> depends only on $\partial^2 = 0$ on $C_*(\overline{\mathcal{M}}_{g,n})$,
> which is a topological triviality. All five main theorems (A-D, H),
> the bar-intrinsic MC construction (Theorem~\ref{thm:mc2-bar-intrinsic}),
> and the shadow obstruction tower (Theorem~\ref{thm:recursive-existence})
> depend only on the convolution-level result and are unaffected by any
> revision of~\cite{Mok25}.

This remark is precisely the honest accounting the audit would have
inscribed. It was authored before the Wave-18 Mok25 swarm and
anticipates the Mok25 phantom finding.

## Phase 2. Primary-source cross-check on Mok25

The parallel Wave-18 attack-heal on Theorem A OF1
(`adversarial_swarm_20260418/attack_heal_thmA_modular_20260418.md`,
Phase 1 verdict, :88-96) states:

> The `Mok25` bibkey resolves against no primary source findable at
> the level of programme-wide discipline (AP281 acute case plus AP269
> sharpened-obstruction territory: fabricated-mechanism check). The
> bibkey is load-bearing for the nodal-boundary factorization-gluing
> step of OF1 and for the modular-family base-change at the boundary
> divisor. Without a primary source, the inscribed scope remark's
> reference "(b) Mok25 logarithmic factorization-gluing at the boundary
> (nodal degenerations)" is citation-level aspiration, not verified
> external input.

Confirmed at the bibliographic level: `standalone/references.bib:601-607`
entry for `Mok25` is a bare `@article{Mok25, ..., note = {Preprint}}`
with no arXiv number, no DOI, no venue, no submission date. The author
name "Chung-Pang Mok" is a known mathematician working in Langlands /
trace-formula geometry, not logarithmic FM compactifications; no arXiv
listing by Mok with the cited title is locatable.

Pending definitive closure by the Wave-18 Thm-A-OF1 report (which
inscribes the Mok25 verdict at programme level), D$^2$ = 0 inherits the
same phantom-bibkey finding.

## Phase 3. Scope assessment and audit verdict

### 3.1 The CLAUDE.md row is compressed and misleading

The current row reads

```
| D^2=0 | PROVED | Convolution on universal family over M̄_{g,n}; ambient Mok25 log FM. |
```

which can be parsed two ways:

- **Compressed-conjunction reading**: "both the convolution and the
  ambient D$^2$ = 0 statements are proved; the ambient uses Mok25 log
  FM." This matches the inscribed scope remark `rem:mok-dependency` IF
  the reader knows to distinguish the two theorems. A naive reader
  taking "PROVED" at face value inherits the ambient's Mok25 dependency
  as a PROVED status, which is the AP271 reverse-drift failure mode
  (CLAUDE.md overstates manuscript success; the manuscript itself is
  honest at `rem:mok-dependency`).

- **Naive-single-theorem reading**: "D$^2$ = 0 is one theorem,
  PROVED via the ambient Mok25 construction." This misreads the
  chapter. The convolution-level theorem is the load-bearing one for
  the five main theorems; the ambient is structural enrichment.

### 3.2 Does the proof actually need Mok25?

Substantively, NO, for the claim that propagates to Theorems A-D-H:

- `thm:convolution-d-squared-zero` is one line of topology
  ($\partial^2 = 0$ on singular chains of
  $\overline{\mathcal{M}}_{g,n}$) and needs no FM compactification at
  all, much less a logarithmic one, and no Mok25.
- `thm:mc2-bar-intrinsic`, `thm:recursive-existence`, and the
  downstream MC propagations consume the convolution-level statement,
  per `rem:mok-dependency:32598-32605`.

Substantively, YES, for the structural enrichment:

- `thm:ambient-d-squared-zero` genuinely needs the log-FM
  normal-crossings property and the planted-forest stratification; if
  Mok25 is phantom or non-existent, Step 4 of the ambient proof has no
  primary source and the ambient D$^2$ = 0 reverts to conditional.
- The planted-forest depth filtration, the log clutching law, the
  quartic clutching construction, and all ambient-level cross-term
  cancellations inherit the same conditional status.

### 3.3 Scope verdict

The load-bearing D$^2$ = 0 for the programme's five main theorems is
**UNCONDITIONAL** on a fixed smooth curve AND over
$\overline{\mathcal{M}}_{g,n}$ including boundary, because the
convolution-level proof uses only topological $\partial^2 = 0$ on the
chain complex of $\overline{\mathcal{M}}_{g,n}$. No Mok25, no log-FM, no
relative FM of the universal curve.

The ambient-level enrichment D$^2$ = 0 is **CONDITIONAL** on Mok25
normal-crossings + planted-forest stratification. Pending Mok25 primary-
source confirmation (Wave-18 Thm-A-OF1 finding: no primary source
locatable), the ambient-level statement should carry
`\ClaimStatusConditional` or `\ClaimStatusProvedElsewhere` with an
explicit attribution-remark naming the conditional dependency.

Note a status-tag drift flag: the ambient theorem currently carries
`\ClaimStatusProvedHere` (line 32418) while the scope remark admits
conditional status "if Mok25 is revised or the result is not confirmed
by publication". This is AP256 (aspirational-heal) in miniature inside
the same chapter: the status tag advertises stronger than the remark
admits. Given Wave-18's Mok25-phantom finding, the tag should be
retracted to `\ClaimStatusConditional`.

## Phase 4. Heal

### 4.1 CLAUDE.md status row rewrite

Replace the current one-line row with a scope-separated two-sub-item row:

```
| D^2=0 | PROVED at convolution level UNCONDITIONAL (topological
 $\partial^2 = 0$ on $\overline{\cM}_{g,n}$, no Mok25); CONDITIONAL at
 ambient level on Mok25 log-FM primary source (Wave-18 Thm-A-OF1 finds
 Mok25 bibkey is AP281 phantom with no locatable primary source;
 pending definitive retraction). | Convolution-level
 (thm:convolution-d-squared-zero, higher_genus_modular_koszul.tex:32404)
 is load-bearing for Theorems A-D-H, MC2, recursive-existence
 shadow tower; unaffected by Mok25 status. Ambient-level
 (thm:ambient-d-squared-zero, :32418) provides planted-forest
 / clutching / quartic-degeneration structural enrichment; conditional.
 Honest scope remark already inscribed at rem:mok-dependency:32568-32606. |
```

### 4.2 Ambient-level status-tag retraction (AP256 heal)

At `higher_genus_modular_koszul.tex:32418`, the current header

```latex
\begin{theorem}[Square-zero: ambient level; \ClaimStatusProvedHere]
\label{thm:differential-square-zero}
\label{thm:ambient-d-squared-zero}
```

should be retagged

```latex
\begin{theorem}[Square-zero: ambient level; \ClaimStatusConditional]
\label{thm:differential-square-zero}
\label{thm:ambient-d-squared-zero}
```

with the scope remark `rem:mok-dependency` strengthened from
"reverts to conditional if Mok25 is revised" to the current reading
"conditional pending Mok25 primary-source confirmation; Wave-18 finds
the bibkey phantom". This is an editorial heal pending the Wave-18
Thm-A-OF1 definitive verdict on Mok25.

If Mok25 is definitively retracted (Wave-18 resolves negatively), the
inscribed scope-remark downstream consequences apply verbatim:
`def:vol1-rigid-planted-forest-depth-filtration`, `thm:log-clutching-degeneration`,
`constr:degree4-degeneration`, and all ambient-level cross-term
cancellations cited in the proof.

### 4.3 No propagation gap for the main theorems

Per `rem:mok-dependency:32598-32605`, the main theorems A-D-H,
`thm:mc2-bar-intrinsic`, and `thm:recursive-existence` depend only on
the convolution-level D$^2$ = 0, which is unconditional. No propagation
retraction is needed for the programme's five-main-theorems backbone.
This is the most important finding: the apparent load-bearing Mok25
dependency flagged in the Theorem Status table does NOT propagate to
the main theorems, because the inscribed architecture routes the main-
theorems dependency through the unconditional convolution-level
theorem, not through the conditional ambient-level theorem.

### 4.4 AP inscription

Register AP1341 in the CLAUDE.md AP catalogue:

**AP1341 (Status-row headline conflates two theorems with distinct
dependency status)**. CLAUDE.md theorem-status row with a single
headline "PROVED" when the theorem family actually contains two
separate inscribed theorems, one unconditional and one conditional on
an external source whose primary-source status is unverified. A naive
reader taking the headline at face value inherits the conditional
dependency as PROVED (AP271 reverse-drift). Counter: for any status row
whose theorem family has $\geq 2$ inscribed variants with distinct
dependency profiles, split the row into per-variant lines with explicit
scope qualifiers, OR inline the scope-separation into the row's
right-hand cell. Canonical violation 2026-04-18: the D$^2$ = 0 row
compressed unconditional convolution-level and Mok25-conditional
ambient-level into a single "PROVED" headline; the manuscript's
inscribed `rem:mok-dependency` was honest, but the CLAUDE.md row
obscured the distinction. Distinct from AP270 (multi-object status-row
conflation counts a compound row advertising one banner whose numeric
signature doesn't match one inscribed object): AP1341 is specifically
the conflated-dependency-status variant where both variants exist and
are correctly inscribed but their distinct dependency profiles are
flattened. Healing: per-variant status lines; grep `rem:` near the
cited theorems for honest scope remarks already present in the
manuscript but not propagated to CLAUDE.md.

## Phase 5. Verdict summary

| Object | Advertised | Actual | Action |
|--------|-----------|--------|--------|
| `thm:convolution-d-squared-zero` | PROVED | UNCONDITIONAL (topological $\partial^2 = 0$) | None; correct. |
| `thm:ambient-d-squared-zero` | PROVED | CONDITIONAL on Mok25 log-FM primary source | Retag `\ClaimStatusProvedHere` $\to$ `\ClaimStatusConditional` pending Wave-18 Thm-A-OF1 Mok25 verdict. |
| CLAUDE.md D$^2$ = 0 row | Single "PROVED" headline | Compressed-conjunction obscures dependency-profile split | Split row into per-variant lines with explicit scope. |
| Main theorems A-D-H dependency | Via D$^2$ = 0 | Via convolution-level D$^2$ = 0 only | No propagation gap; main theorems unaffected. |
| Scope remark `rem:mok-dependency` | Inscribed at :32568-32606 | Correct and honest | No change; it is the audit's own verdict, inscribed pre-hoc. |

## Notes

- Honest accounting: the chapter's own scope remark
  `rem:mok-dependency` authored this exact audit in advance. The
  manuscript is better-structured than the CLAUDE.md row suggests;
  the failure mode is status-row compression, not manuscript overreach.
- Cross-reference to Wave-18 Thm-A-OF1: that swarm's Phase 1 verdict
  on Mok25 (no locatable primary source) is the upstream finding this
  audit consumes; definitive closure of the D$^2$ = 0 ambient
  conditional depends on Mok25's definitive status resolution.
- AP1341 is the single new AP inscribed. AP1342-AP1360 reserved
  unused.

## Appendix: Grep trail

- `\label{thm:convolution-d-squared-zero}`:
  `chapters/theory/higher_genus_modular_koszul.tex:32405`.
- `\label{thm:ambient-d-squared-zero}`:
  `chapters/theory/higher_genus_modular_koszul.tex:32420`.
- `rem:mok-dependency`:
  `chapters/theory/higher_genus_modular_koszul.tex:32568`.
- Mok25 bibkey:
  `standalone/references.bib:601-607` (bare preprint entry, no arXiv
  / DOI / venue).
- CLAUDE.md row: single line containing "D^2=0 ... PROVED ...
  Convolution on universal family over M̄_{g,n}; ambient Mok25 log FM.".
- Guide-to-main-results table at
  `chapters/frame/guide_to_main_results.tex:117-121` advertises
  "Ambient $D^2 = 0$ ... proved via Mok's log-FM normal-crossings
  result", which inherits the same scope-tag drift as CLAUDE.md and
  should be retagged conditional in the same pass.
