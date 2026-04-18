# FTM Seven-Fold TFAE — Spoke 4 OF2 Heal Verification (2026-04-18)

## Mission

Verify Wave-18 heal of OF2 (Theorem A): Kac-Moody filtered-comparison
phantom remark inscribed at
`chapters/theory/ftm_seven_fold_tfae_platonic.tex:673-729`.

## Findings

### (i) Anchor existence — PASS

Within `ftm_seven_fold_tfae_platonic.tex`:

- `prop:class-L-witness` inscribed at line 635 (ClaimStatusProvedHere).
- `rem:kac-moody-filtered-comparison` inscribed at line 675
  (ClaimStatusProvedHere), span 673-729.
- `lem:filtered-comparison` cited 5x within the chapter
  (lines 252, 348, 467, 768, 783, 816); the label itself is inscribed
  in the canonical home at
  `chapters/theory/chiral_koszul_pairs.tex:353` with a proof body
  routing through Eilenberg-Moore strong convergence and
  LV12 Theorem 3.2.1.

No phantom remains. The cross-reference chain
`prop:class-L-witness (iii)` -> `rem:kac-moody-filtered-comparison`
-> `lem:filtered-comparison` fully resolves.

### (ii) Mathematical content of rem:kac-moody-filtered-comparison — PASS

Proof body at lines 673-729 inscribes the expected content:

- **Kashiwara filtration on vacuum V_k(sl_2)**: identified as the
  L_0-eigenspace (conformal-weight) filtration, equivalently the PBW
  filtration on U(sl_2-hat) restricted to the vacuum Verma-quotient
  (lines 680-685).
- **Associated graded**: gr^F V_k(sl_2) = Sym(sl_2[t^{-1}] t^{-1}),
  Koszul classically (lines 685-688).
- **Kac-Kazhdan determinant step**: at generic k, the Shapovalov form
  on each conformal-weight component is non-degenerate; this supplies
  finiteness-at-each-weight, which is what closes the inverse limit
  at the chiral level (lines 698-703).
- **Non-tautology witness**: two failure cases inscribed —
  (a) critical level k=-h^v=-2, Feigin-Frenkel centre + Kac-Kazhdan
  singular vectors at every bounded weight invalidate completeness;
  (b) integer non-admissible k in Z_{>=0}, Verma multiplicity grows
  unboundedly within fixed L_0-eigenspace (lines 705-718).
- **Primary sources**: Kac-Kazhdan 1979, Kac 1998 Ch.11,
  Frenkel-Ben-Zvi 2004 sec 5.3 (lines 724-728).

The remark demonstrates genuine non-tautology at the chiral level
consistent with Beilinson discipline: classical associated-graded
Koszulness does NOT automatically imply filtered chiral Koszulness;
the implication is non-vacuous precisely because completeness
(inverse-limit of Kashiwara-filtered quotients as chiral modules)
requires the Kac-Kazhdan generic-level multiplicity estimate.

### (iii) Clause (iii) of prop:class-L-witness resolution — PASS

Lines 645-653 of `prop:class-L-witness` state that the
filtered-comparison lemma is load-bearing: naive associated-graded
gives classical Koszul acyclicity of Sym(sl_2[t^{-1}] t^{-1}), but
the filtered lift to the chiral twisted tensor product on P^1
requires the Kashiwara filtration hypothesis, with explicit
`\ref{rem:kac-moody-filtered-comparison}` pointing to the proof body
at line 651.

Proof body (lines 660-671) routes:
- (i) from `thm:kac-shapovalov-koszulness` (generic k => PBW-Koszul
  => E_2-collapse);
- (ii) from Spoke 4 of
  `thm:ftm-seven-fold-tfae-via-hub-spoke`;
- (iii) from the Kashiwara-filtration identification used in the
  proof of `prop:d-module-purity-km-equivalence`, combined with the
  inscribed remark.

Clause (iii) now resolves cleanly: no phantom, no forward-reference
lemma, no AP242 violation.

### (iv) Spoke 4 PROVED status — PASS (within scope)

The summary table at lines 746-778 presents six spokes with both
directions. Spoke 4 rows:

- Forward (hub => acyclic):
  Lem twisted-product-cone-counit + Spoke 2.
- Reverse (acyclic => hub): Lem filtered-comparison (tagged
  "filtered-comparison, non-tautological").

Lines 780-788 identify Spoke 4's reverse as the ONLY non-tautological
bidirection; all other arrows route through the universal FTM, the
PBW-Koszulness criterion, and the SC-formality characterisation.
The witness at V_k(sl_2) (prop:class-L-witness) and its underlying
Kashiwara-completeness step (rem:kac-moody-filtered-comparison) now
make the non-tautology visible as a worked counterexample rather
than a structural assertion.

## Residuals

Two minor items observed during audit; not blocking:

1. **Scope qualifiers inside rem:kac-moody-filtered-comparison**.
   Failure case (b) ("integer non-admissible levels in Z_{>=0} with
   non-generic fusion") conflates positive-integer level and
   admissible-but-non-generic level. Frenkel-Kac realisation at
   positive integer level gives a well-defined, self-contained
   Kashiwara completeness statement; the failure mode at (b) is
   specifically for the non-admissible stratum where Verma
   descendants acquire primitive vectors. A subsequent rectification
   could split (b) into (b1) positive-integer + admissible (completeness
   holds by Frenkel-Kac) and (b2) non-admissible (completeness fails).
   Not urgent; the remark's main claim (generic k is the non-vacuous
   witness stratum) stands.

2. **Cross-volume label uniqueness**. Grep confirms
   `rem:kac-moody-filtered-comparison` is unique across Vol I chapters;
   not checked against Vol II and Vol III in this audit. HZ-5
   discipline: extend the grep before any future edit renaming or
   duplicating this label.

## Verdict

OF2 HEALED. Theorem A Spoke 4 PROVED status holds at its inscribed
scope (genus zero, generic k, V_k(sl_2) witness). The phantom
`rem:kac-moody-filtered-comparison` identified in CLAUDE.md Theorem A
row is no longer phantom: the remark is inscribed with proof body and
primary-source attribution; the consumer `prop:class-L-witness (iii)`
resolves; the underlying `lem:filtered-comparison` lives in
`chiral_koszul_pairs.tex:353` with a proof body. Spoke 4 non-tautology
is witnessed at V_k(sl_2) through the Kac-Kazhdan completeness step.

## Anti-patterns (minimal, per AP314 throttle)

No new APs inscribed. The heal exhibits the correct
sharpened-obstruction pattern (AP266): non-tautology is made explicit
by exhibiting two adjacent strata (critical level; non-admissible
integer) at which completeness fails and Spoke 4 reverse direction
breaks. This is the positive template AP266 encourages.

## Files touched

None (verification only). No commits.

## Author

Raeez Lorgat, 2026-04-18.
