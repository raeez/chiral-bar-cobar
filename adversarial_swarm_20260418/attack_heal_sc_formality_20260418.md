# Attack-and-Heal: SC-formality iff class G (prop:sc-formal-iff-class-g)

Date: 2026-04-18. Target: `chapters/theory/chiral_koszul_pairs.tex:3236-3359` (main inscription);
companion `prop:swiss-cheese-nonformality-by-class` at `chiral_koszul_pairs.tex:3101-3225`;
companion `prop:sc-formality-by-class` at `higher_genus_modular_koszul.tex:17672-17757`.
Author: Raeez Lorgat.

## 0. Scope and method

The mission is an adversarial Beilinson attack on the CLAUDE.md theorem-status row

> "SC-formal: PROVED. SC-formal iff class G. Forward: operadic tower truncation (Delta=0).
> Converse: shadow tower controls SC ops. ALT: operadic both directions (H11)."

Five attack vectors:
(i)  locate and read the inscription;
(ii) forward direction (class G => SC-formal) -- literal vs cohomological $\Delta=0$;
(iii) converse (SC-formal => class G) -- shadow-tower control, Step 1 bridge;
(iv) ALT H11 -- is a second proof inscribed, or a remark-level placeholder?
(v)  multi-generator scope -- lattice rank >= 2, Leech, affine $\fsl_n$ with multiple currents.

## 1. Findings

### F1. Primary inscription located

Canonical label `\label{prop:sc-formal-iff-class-g}` at `chapters/theory/chiral_koszul_pairs.tex:3237`.
Environment: `\begin{proposition}[...; \ClaimStatusProvedHere]`. HZ-5 label discipline
(AP124 uniqueness across three volumes): only one inscription of this exact label;
the companion `prop:sc-formality-by-class` in `higher_genus_modular_koszul.tex:17674`
is a DIFFERENT proposition covering three aspects (bar-cohom formality, SC on $\cA$,
$L_\infty$ brackets on $\gAmod$). HZ-11 (cross-volume proof-locality): the proof
cites `thm:shadow-formality-identification` (Vol I, `higher_genus_modular_koszul.tex:15979`),
`thm:e1-primacy` (Vol I, `introduction.tex:1463`), `thm:shadow-archetype-classification`
(Vol I, `higher_genus_modular_koszul.tex:17369`). All three lemmas live in Vol I.
No cross-volume phantom.

### F2. CRITICAL: unproved two-colour transfer bridge (Step 1 converse)

The converse direction relies on the logical chain
\[
m_r^{\mathrm{SC}} = 0 \;\Longrightarrow\; \text{degree-}r\text{ tree} = 0
                   \;\Longrightarrow\; S_r(\cA) = \operatorname{av}(\text{tree}) = 0,
\]
inscribed at `eq:sc-formal-shadow-vanishing` (line 3320). The first implication
is asserted via PROSE at lines 3327-3333:

> "the mixed-sector operation IS the genus-0 tree: vanishing of the open-colour output
> forces vanishing of the tree itself (the tree is a connected genus-0 amplitude with a
> fixed set of external legs; it is not a formal cancellation but a structural vanishing
> of the tree sum)."

This is an assertion, not a derivation. The cited `thm:shadow-formality-identification`
identifies $S_r(\cA) = \ell_r^{(0),\mathrm{tr}}$ (CLOSED sector, post-averaging); it says
nothing about zero-detection of the OPEN lift before averaging. The cited `thm:e1-primacy`
gives the surjective averaging map and its kernel at degree 3 (Drinfeld associator), but
does NOT give an injective statement that would let one lift a zero-closed-output conclusion
back to a zero-tree conclusion.

Worse, `thm:e1-primacy`(iv) explicitly states that $\ker(\operatorname{av})$ is NON-TRIVIAL
(contains the Drinfeld associator at degree 3). So av is lossy -- yet the converse tries to
use a colour-change step whose analogue at the $E_1$ level would require precisely the
injectivity that av refuses. The correct two-colour transfer lemma (from SC open-colour
output back to a statement about the tree sum as an $E_1$-element) is MISSING.

This is exactly the CRITICAL finding surfaced in `opus_audit_20260413_224154/OA1_sc_formality.md:4`,
authored 2026-04-13 under a Codex audit. The commit log shows the file was touched in
55b2a242 ("SC-formality operadic proof: both directions without bilinear form (AP218 resolved)")
BEFORE the OA1 audit, and subsequent commits (e2dd5b34 Wave-5, 15eca7d0 Waves 4-8) did NOT
heal the OA1 CRITICAL gap. Current source still carries the "open-colour lift" assertion at
line 3273 with no `\ref{}` to a proved two-colour transfer theorem.

### F3. SERIOUS: class-$M$ "$m_k^{\mathrm{SC}} \neq 0 \; \forall k$" overclaim

The companion table in `prop:swiss-cheese-nonformality-by-class` at line 3140 writes

> $M$ ... $\neq 0 \; \forall\, k \geq 5$

and the $\mathbf{M}$-row of `prop:sc-formal-iff-class-g`'s proof table at line 3351
declares $S_r \neq 0$ for $r \geq 5$ without qualification. The cited `thm:shadow-archetype-classification`
at `higher_genus_modular_koszul.tex:17418-17434` proves

- $S_3, S_4$ nonzero for Virasoro (explicit formulas);
- $o_5(\mathrm{Vir}) = \{\mathfrak{C}, \mathfrak{Q}\}_H \neq 0$ for GENERIC $c$ (not all $c$);
- the tower is infinite "by induction on the all-degree master equation".

"Infinite" here means "infinitely many nonzero higher shadows", NOT "nonzero at every
single degree $r \geq 5$". The sharper statement -- degree-by-degree nonvanishing --
is NOT proved. The programme's own engine `theorem_ainfty_nonformality_class_m_engine.py`
verifies $S_3, S_4, S_5$ for Virasoro but not $S_r$ at all $r \geq 5$.

This is the SERIOUS finding of OA1 (second bullet, `opus_audit_20260413_224154/OA1_sc_formality.md:6`).
Still unhealed.

### F4. ALT H11 is folded into the primary, not a separate alternative

CLAUDE.md advertises "ALT: operadic both directions (H11)". The programme's healing note
`healing_20260413_132214/H11_SC_formal_alt.md:1-16` reports

> "The operadic alternative proof is now present on the live surface at
> chapters/theory/chiral_koszul_pairs.tex:2923. I tightened the converse ..."

Examination of the current source shows the primary proof IS operadic (line 3247: "The
proof is operadic: both directions use the genus-0 tree-shadow correspondence..."). So the
H11 edits WERE installed as the PRIMARY proof, not as a separate `\begin{remark}[Alternative proof]`.
Grep across `chapters/` for `Alternative.*SC.formal` returns zero inscribed alternatives
for this proposition. Consequence: the CLAUDE.md "ALT: operadic both directions (H11)"
row misrepresents a PRIMARY-PROOF REWRITE as a SECOND INDEPENDENT PROOF. This violates
AP240 (closure-by-repackaging) and AP241 (advertised-but-not-inscribed characterization):
the ALT column claims a redundancy that does not exist in the source.

### F5. Multi-generator class-G scope (forward) is partially asserted

The forward direction lists three families (Heisenberg $\cH_c$, lattice VOA $V_\Lambda$,
free fermion) as the class-G locus (lines 3286-3296). For each, a ONE-SENTENCE mechanism
is given. For lattice VOAs the mechanism CITES `cor:lattice-postnikov-termination`, but
that corollary is a SHADOW statement (shadow tower truncates at degree 2), not a
CHAIN-LEVEL SC-formality statement. The same two-colour transfer bridge (F2) is needed to
push shadow truncation to chain-level SC vanishing. The Leech / rank-48 / rank-72 lattice
VOAs classified as class-$G$ in `thm:shadow-archetype-classification:17348-17356` inherit
this gap: their shadow tower is proved to truncate, but the deduction that chain-level
$m_r^{\mathrm{SC}} = 0$ for $r \geq 3$ relies on the same missing two-colour transfer lemma.

Multi-generator affine KM (class L) is formally $m_3^{SC} \neq 0$, $m_4^{SC} = 0$ (Jacobi
kills the quartic, `rem:loop-exactness-ordering:3094`); the claim "one-loop exact" is
family-level and does not require per-generator verification, so F5 does not escalate to
CRITICAL -- but the LATTICE-VOA leg of class G does inherit F2.

### F6. Literal $\Delta = 0$ vs cohomological truncation

The forward direction does NOT use "$\Delta = 0$" as a literal condition. CLAUDE.md
status row says "Delta=0"; source at line 3336 correctly notes the HIGHER WARNING
"$\Delta = 0$ is necessary but not sufficient: class L has $\Delta = 0$ but $S_3 \neq 0$".
So "$\Delta = 0$" in CLAUDE.md is a SHORTHAND for "shadow tower truncates at $r = 2$",
NOT for the discriminant condition alone. Not a programme error, but a CLAUDE.md
formulation vulnerable to FM8 (universal-quantifier drift) if re-transcribed by later
agents. HEAL optional.

### F7. Label / AP audit (non-blocking)

- AP124 uniqueness: single inscription, OK.
- AP125 prefix: `prop:` matches `\begin{proposition}`, OK.
- AP165 / AP-SC-BAR: proof correctly attributes SC to the $(B(\cA), ...)$ pair via the
  tree-shadow correspondence, does NOT claim $B(\cA)$ is an SC-coalgebra. OK.
- AP166 / AP-SC-NOT-SELFDUAL: proof does not invoke self-duality. OK.
- AP172: does not assert $\cA^!$ is SC-algebra. OK.
- AP28: every cited label resolves. OK.
- AP176 arity ban: source uses "degree". OK.

## 2. Verdict

The two CRITICAL and SERIOUS findings of OA1 (2026-04-13) survive four commits and remain
on the live surface as of 2026-04-18. The CLAUDE.md theorem-status row

> "SC-formal: PROVED. SC-formal iff class G. Forward: operadic tower truncation (Delta=0).
> Converse: shadow tower controls SC ops. ALT: operadic both directions (H11)."

overstates the proof state on three counts: (a) F2 (unproved two-colour transfer bridge
in the converse); (b) F3 (class-M degree-by-degree overclaim in the companion table); (c)
F4 (ALT H11 is folded into the primary, not a separate alternative). The proposition
itself is a CONDITIONAL theorem whose conditional lemma ("open-colour SC output vanishes
=> underlying $E_1$ tree vanishes") is plausible but uninscribed.

## 3. Heal menu

Three honest healings, listed in order of increasing retreat:

**H-SC-1 (preferred).** Inscribe the missing two-colour transfer lemma as a named
proposition, then cite it from Step 1 of the converse. The content: for the
two-coloured SC operad, the open-colour output map at genus 0 on the transferred
tree sum from $\gAmod^{E_1}$ is INJECTIVE on the connected-tree component at every
degree $r \geq 3$. Proof candidate: the open-colour structure at the output is given
by the bulk-to-boundary structure map $\iota: \cA \to B(\cA)$ (or its dual $\pi: B(\cA) \to \cA$
composed with the boundary inclusion), which on CONNECTED trees of positive degree is
injective because the tree sum is the image of a free generator under a free-algebra
inclusion. This HEALS F2 and F5-lattice. Status tag stays `\ClaimStatusProvedHere`.

**H-SC-2 (intermediate).** Weaken the companion `prop:swiss-cheese-nonformality-by-class`
$\mathbf{M}$-row from "$\neq 0 \; \forall k \geq 5$" to "nonzero for infinitely many $k \geq 5$"
(the true statement). Also weaken the $\mathbf{M}$-row of `prop:sc-formal-iff-class-g`
proof table. Update CLAUDE.md theorem-status row accordingly. This HEALS F3 without
touching F2.

**H-SC-3 (downgrade).** If H-SC-1 is rejected, downgrade the environment of
`prop:sc-formal-iff-class-g` from `\begin{proposition}[...\ClaimStatusProvedHere]` to
`\begin{proposition}[...\ClaimStatusConditional]` with a Remark noting the open
two-colour transfer lemma. Simultaneously retract the CLAUDE.md "ALT H11" claim (F4) and
rewrite the ALT column as "subsumed into primary operadic proof".

## 4. Honest CLAUDE.md rewrite (if H-SC-1 is not immediately available)

> "SC-formal: PROVED unconditional forward for Heisenberg / free fermion; PROVED unconditional
> converse conditional on the two-colour transfer lemma (open-colour SC output vanishes =>
> underlying $E_1$ tree vanishes); class-G lattice-VOA forward inherits the same conditional
> at the shadow-to-chain-level passage. $m_k^{\mathrm{SC}} \neq 0$ for infinitely many $k \geq 5$
> in class $\mathbf{M}$, not degree-by-degree. ALT column: operadic rewrite folded into primary;
> no separate second proof."

## 5. AP candidates surfaced

No new AP candidates; the pattern is covered by existing AP240 (closure-by-repackaging),
AP241 (advertised-but-not-inscribed characterization), AP249 (base-change / inscription
not citation), AP271 (manuscript ahead of CLAUDE.md -- here it is the dual direction,
CLAUDE.md ahead of manuscript, i.e. AP256 aspirational-heal status drift), and AP242
(forward-reference lemma labelled as inscribed, applied to the uninscribed two-colour
transfer). The OA1 audit has been the canonical diagnostic since 2026-04-13; the correct
action is to heal, not to register a new AP.

## 6. Files touched by this note

This note is SOURCE DOCUMENTATION only; no `.tex` file is edited in this session. Heal
candidates are left to a subsequent wave. Patch file `patch_sc_formality_20260418.patch`
is emitted separately per AP316.

## 7. Cross-volume propagation (if H-SC-1 or H-SC-3 is enacted)

- Vol II: `chapters/connections/3d_gravity.tex:488` carries `prop:formality-depth-discriminant`
  (companion statement). AP5 propagation required.
- Vol III: status table propagation (SC-formality is a Vol I result; Vol III inherits it
  via the shadow tower classification for CY-derived chiral algebras).
- Concordance: `chapters/connections/concordance.tex:7226-7229, 9819` references.
- Preface: `chapters/frame/preface.tex:3090, 3128` references.
- Standalone: `standalone/classification.tex:1089` `prop:sc-formality-standalone`;
  `standalone/shadow_towers_v3.tex:1679` `prop:sc-formal`;
  `standalone/survey_modular_koszul_duality.tex:6290` `prop:svy-sc-formal-iff-g`.
  All three standalones independently state the result and need status-tag alignment.
