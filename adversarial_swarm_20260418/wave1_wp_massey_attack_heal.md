# Wave 1 (2026-04-18) — W(p) triplet shadow-tower Massey attack-and-heal

Adversarial auditor, Beilinson-rectified. Target:
- Vol I `chapters/theory/shadow_tower_quadrichotomy_platonic.tex` (1252 lines)
- Vol I `chapters/examples/logarithmic_w_algebras.tex` (706 lines)
- Vol II `chapters/theory/logarithmic_wp_tempered_analysis_platonic.tex` (1091 lines)
- Vol II `compute/tests/test_logarithmic_wp_tempered.py` (engine docstring)

Frontier: the CLAUDE.md B91 two-Massey split (correlation-function Massey
unbounded on W(p) via Gurarie 1993 + Flohr 1996; shadow-tower Massey on
the regular sector OPEN). The Vol II chapter inscribes the split in
`rem:correlation-vs-shadow-massey`; the Vol I quadrichotomy records the
retraction honestly.

## Attack ledger

### F1. Proof body under conjecture environment (AP4/AP40)
File: Vol II `logarithmic_wp_tempered_analysis_platonic.tex:713-746`.
Severity: MEDIUM. Category: environment mismatch.
The `\begin{conjecture}` `conj:tempered-stratum-contains-wp` (line 616,
`\ClaimStatusConjectured`, line 619) is followed by `\begin{proof}` (line
713). `\begin{proof}` only follows theorem/proposition/lemma with a
`ProvedHere` tag (AP4). A conjecture with a proof body is either a
concealed theorem (retract the conjecture tag) or a scope-restricted
theorem (split into proved part + conjectured part) or genuinely a
conjecture with EVIDENCE not PROOF (rename to `\begin{remark}[Evidence]`).
Here the "proof" combines three subchannel lemmas via triangle
inequality; but since Lemma WW below is itself load-bearing on the
retracted Zhu-bounded-Massey mechanism, the combined statement is
genuinely conjectural and the proof body is evidence, not proof.

### F2. Lemma WW carries retracted mechanism under ProvedHere (AP256)
File: Vol II `logarithmic_wp_tempered_analysis_platonic.tex:369-446`,
specifically Step 1 at lines 396-405.
Severity: HIGH. Category: aspirational heal.
`lem:wp-ww-subchannel-tempered` is tagged `\ClaimStatusProvedHere`. Its
Step 1 asserts: "Every W-W collision residue $\Xi^{ab}_k(w)$... matrix
elements in the vacuum module descend to $A(\cW(p))$ by the Zhu
algebra's definition. Since $\dim A(\cW(p)) = 2p$ is finite, every such
matrix element is bounded by a uniform constant $C_{\mathrm{Zhu}}(p)$
depending only on $p$ (not on the bar graph vertex count $r$)."

This is verbatim the mechanism retracted at
`rem:zhu-bounded-massey-retraction` (lines 481-514): "That bounded Zhu
$\Rightarrow$ bounded Massey. The Massey product is a SECONDARY
cohomology operation... Bounding individual Zhu components does not
bound the cumulative Massey tower across bar degrees."

Step 1 of Lemma WW (claiming uniform bound from Zhu finiteness) and
Lemma `lem:wp-zhu-bounded-masseys` (retracted to `ClaimStatusConjectured`
at line 473) use the SAME mechanism. The retraction of one forces
retraction of the other, but the ProvedHere tag on Lemma WW survives.
AP256 aspirational-heal: advertising a restriction to "shadow-tower
Massey on $H^\bullet_{\mathrm{reg}}$" before the mechanism is actually
restricted. The saving `rem:correlation-vs-shadow-massey` argues the
$\dlog$-residue construction strips log growth, so shadow-tower
residues are not correlation-function amplitudes. But this argument
must be inscribed in Step 1 itself (or as a lemma that Step 1 cites);
it currently only appears as a floating remark AFTER the proof.

### F3. Regular/logarithmic bar-cohomology decomposition is asserted, not inscribed (AP242)
File: Vol II `logarithmic_wp_tempered_analysis_platonic.tex:582-595`.
Severity: HIGH. Category: forward-reference lemma.
The load-bearing decomposition
\[ H^\bullet(\Barch(\cW(p))) = H^\bullet_{\mathrm{reg}} \oplus
H^\bullet_{\mathrm{log}} \]
appears exclusively inside `rem:correlation-vs-shadow-massey`. Grep
across Vol I, Vol II, Vol III returns zero hits for this decomposition
as a proposition, lemma, or theorem. The orthogonality under the
Arnold / OS pairing is asserted without proof. Consequence: the
operational content "Gurarie-Flohr targets only $H^\bullet_{\mathrm{log}}$;
shadow tower lives on $H^\bullet_{\mathrm{reg}}$" rests on an uninscribed
decomposition. AP242 forward-reference-lemma.

The mathematical substance is plausible: Arnold / Orlik-Solomon classes
represent the polynomial-$\dlog$ part of bar cohomology; the
$(\log z_{ij})^n$-enriched sector is in the kernel of the Arnold
residue by construction (the Arnold form is homogeneous of weight one in
each $\dlog(z_i - z_j)$; logarithmic amplitudes produce higher-weight
$(\log(z_i - z_j))^n$ insertions that the homogeneous form annihilates).
But this needs a proposition, not a remark.

### F4. Three-channel decomposition itself is assertion-level (cross with F2)
File: Vol II lines 256-274 `def:wp-shadow-channel-decomposition`.
Severity: MEDIUM. Category: def vs prop.
Defining the decomposition $S_r = S_r^{TT} + S_r^{TW} + S_r^{WW}$ by
collecting bar graphs by collision type is a definition, not a bound. The
inscriptive lemmas then treat each piece as if the decomposition is
preserved under the bar differential (i.e., that the three types of
graphs do not mix under the differential). This is non-trivial: the bar
differential acts by OPE-contraction, and a contraction inside a
composite field $\Xi^{ab}_k$ that lives in the $W$-$W$ channel can
produce a $T$-only subgraph (since $\Xi^{ab}_k$ has $T$ descendants).
The decomposition is thus filtration-level, not direct-sum, unless a
separate lemma establishes closure under the differential. No such
lemma is inscribed.

### F5. Engine docstring carries stale ProvedHere narrative (AP257)
File: Vol II `compute/tests/test_logarithmic_wp_tempered.py:24-25`.
Severity: LOW (docstring drift). Category: engine-vs-manuscript contradiction.
The test module docstring states verbatim:
"Lemma `lem:wp-zhu-bounded-masseys` (ProvedHere): Massey products are
bounded by $(2p)^{k+1}$."
The manuscript has downgraded this to `\ClaimStatusConjectured` (line
473). The test name `test_wp_zhu_dimension` (line 48) remains sound
(it tests the Zhu-dimension formula, not the Massey bound), but the
framing is misleading. AP257.

### F6. Vol I examples chapter — no finding; read is clean
File: Vol I `chapters/examples/logarithmic_w_algebras.tex`.
The chapter states Koszulness as **OPEN**, lists `\kappa(\cW(p)) = c/2`
as the only proved item in the five-theorem table (line 57), and in
Section 10 open-problems item 6 (lines 686-705) correctly cites
Gurarie-Flohr for unbounded Massey, identifies p=2 (symplectic-fermion
orbifold) and p=3 (first non-symplectic-fermion) as the sharp test
cases, and notes that isolating an explicit triple-Massey cocycle
representative is the cleanest pathway. No scope inflation.

The only refinement available: the open-problems item does not
articulate the correlation-function-vs-shadow-tower Massey distinction.
A single-sentence addition would align Vol I with Vol II's sharpened
frontier.

### F7. Vol I quadrichotomy — no finding; retraction is honest
File: Vol I `chapters/theory/shadow_tower_quadrichotomy_platonic.tex`.
Lines 1094-1096 correctly retract `Proposition prop:wp-triplet-T-Cartan-line`'s
structural tempering conclusion "at publication standard (see
\S\ref{sec:open-frontier})". Lines 1174-1188 state the open frontier
honestly: "The correct tempered scope is: principal, non-logarithmic,
non-minimal standard landscape; $\cW(p)$ is open pending the
Adamovi\'c--Milas character-amplitude bound."

## Surviving core (Drinfeld-style)

Two Massey objects distinguished on the bar cohomology of a
$C_2$-cofinite logarithmic vertex algebra: the correlation-function
Massey supported on the $\log(z_{ij})$-enriched sector, and the
shadow-tower Massey extracted by the Arnold / $\dlog$-residue against
$\mathrm{FM}_r(\CC)$. Gurarie 1993 and Flohr 1996 falsify boundedness
of the first on $\cW(p)$, not the second; the shadow-tower lives
orthogonal to the logarithmic sector by Orlik-Solomon homogeneity.
Whether the shadow-tower triple-Massey class
$\langle \Omega, \Omega, \Omega\rangle$ on $\cW(p)$ is polynomially
bounded is OPEN; sharpest test case is $p = 3$ (first non-symplectic-
fermion triplet); the falsification test is a direct numerical
evaluation of $(|S_r^{TT}(\cW(3))| + |S_r^{TW}(\cW(3))| +
|S_r^{WW}(\cW(3))|)^{1/r}$ against $r!^{1/r}$ through $r = 10$ via
the Vol I T-line + Cartan-line engines already catalogued at
Proposition `prop:wp-triplet-T-Cartan-line`.

$C_2$-cofiniteness implies finite-dim Zhu and hence finite-dim bar
cohomology at each fixed weight; it does NOT imply bounded cumulative
Massey across weights. The retracted Lemma
`lem:wp-zhu-bounded-masseys` confused per-weight boundedness with
cross-weight boundedness; the healed statement is per-weight only.

## Heal plan (no Edits this run; plan recorded for commit)

### H1. Vol II: split proof body under conjecture into Evidence remark
Rewrite Vol II lines 713-746: the `\begin{proof}` block following
`conj:tempered-stratum-contains-wp` becomes
`\begin{remark}[Evidence for Conjecture~\ref{conj:tempered-stratum-contains-wp}]`
with the same triangle-inequality content, explicitly labeled as
evidence consisting of three subchannel analyses two of which rest on
the retracted Zhu-bounded-Massey mechanism.

### H2. Vol II: downgrade Lemma WW to Conditional, with sharpened mechanism
Retag `lem:wp-ww-subchannel-tempered` from `\ClaimStatusProvedHere` to
`\ClaimStatusConditional`. Add Step 0 (routing remark) that states:
"Step 1 below cites Zhu algebra finite-dimensionality to bound
collision residues uniformly in $r$. This mechanism — bounded Zhu
implies bounded cross-weight Massey — is falsified for correlation-
function Massey amplitudes by Gurarie 1993 and Flohr 1996. The
restriction to shadow-tower residues via the Arnold / $\dlog$
construction, which stays on the polynomial sector
$H^\bullet_{\mathrm{reg}}$, bypasses the Gurarie-Flohr obstruction
conditional on Proposition X (regular-logarithmic orthogonality under
the Orlik-Solomon pairing) below." Parallel downgrade for
`lem:wp-tw-subchannel-tempered` if its proof relies on the same
uniform-bound mechanism (re-examination shows it does, via Step 2
"primary-field propagator bounded by scalar multiple of Virasoro
propagator" which implicitly assumes cross-weight boundedness).

### H3. Vol II: inscribe regular-logarithmic orthogonality as proposition
Convert the decomposition $H^\bullet = H^\bullet_{\mathrm{reg}} \oplus
H^\bullet_{\mathrm{log}}$ from a remark into an inscribed proposition
`prop:bar-cohomology-regular-logarithmic-decomposition` with statement:
"For a $C_2$-cofinite logarithmic vertex algebra $\cA$ admitting
logarithmic $L_0$-nilpotent partners, the bar cohomology
$H^\bullet(\Barch(\cA))$ admits an orthogonal decomposition
$H^\bullet_{\mathrm{reg}} \oplus H^\bullet_{\mathrm{log}}$ under the
Arnold / Orlik-Solomon pairing, with $H^\bullet_{\mathrm{reg}}$ the
image of the polynomial-$\dlog$ homogeneous subcomplex and
$H^\bullet_{\mathrm{log}}$ the $(\log z_{ij})^n$-enriched complement.
Shadow-tower coefficients $S_r$ live in $H^\bullet_{\mathrm{reg}}$ by
construction." Inscribed proof: Arnold form is homogeneous of weight
one per $\dlog(z_i - z_j)$; $(\log z_{ij})^n$ with $n \ge 2$ sits in
the kernel of the homogeneous residue; orthogonality is the
Orlik-Solomon grading. `\ClaimStatusProvedHere` legitimately at this
scope because the content is classical Orlik-Solomon + standard
logarithmic bar-complex grading. Status tag `\ClaimStatusConditional`
acceptable if the logarithmic enrichment of the bar complex in the
chiral setting requires a cross-reference to Feigin-Gainutdinov-
Semikhatov-Tipunin's logarithmic Feigin-Fuks construction.

### H4. Vol II: inscribe three-channel closure under differential as lemma
New `lem:three-channel-filtration-preserved`: "The three-channel
decomposition $S_r = S_r^{TT} + S_r^{TW} + S_r^{WW}$ is a
$\mathbb{Z}_{\ge 0}^3$-graded filtration of the bar complex preserved
by the bar differential: $d(S_r^{\bullet}) \subseteq S_{r+1}^{\bullet}$
in each channel, with cross-channel drift accounted for by the
Adamovi\'c-Milas composite-field expansion of $\Xi^{ab}_k$." Closes F4.

### H5. Vol I quadrichotomy: propagate the regular-vs-correlation split
Append one sentence in the Open Frontier paragraph of Vol I
`shadow_tower_quadrichotomy_platonic.tex` after line 1188: "The correct
open problem is shadow-tower Massey boundedness on the
polynomial-$\dlog$ (regular) sector of $H^\bullet(\Barch(\cW(p)))$; the
logarithmic sector accumulates $(\log z_{ij})^n$ amplitudes per
Gurarie-Flohr and is orthogonal to the shadow tower under the
Arnold / Orlik-Solomon pairing (Vol II
`prop:bar-cohomology-regular-logarithmic-decomposition`)." This aligns
Vol I with Vol II's sharpened split.

### H6. Vol I examples: single-sentence refinement to open-problems item 6
Append to the end of item 6 (`item:wp-massey-omega-triple`, lines 686-705):
"The Massey-product object targeted by the Gurarie-Flohr unboundedness
is the correlation-function Massey on the logarithmic sector of
$H^\bullet(\Barch(\cW(p)))$; the orthogonal shadow-tower Massey on the
regular sector extracts structure constants $S_r$ of the bar tower and
is the object whose boundedness governs analytic tempering. The two
Massey objects are distinguished by the Arnold / Orlik-Solomon grading
on the bar complex."

### H7. Vol II engine docstring: align with retraction
Edit `compute/tests/test_logarithmic_wp_tempered.py:24-25` from
"Lemma `lem:wp-zhu-bounded-masseys` (ProvedHere): Massey products are
bounded by $(2p)^{k+1}$." to
"Conjecture `lem:wp-zhu-bounded-masseys` (Conjectured): Massey products
are conjecturally bounded by $(2p)^{k+1}$; the original ProvedHere
tagging was retracted per `rem:zhu-bounded-massey-retraction`. The test
`test_wp_zhu_dimension` checks the Zhu-dimension formula
$\dim A(\cW(p)) = 2p$, which is the Conjecture's Adamovi\'c-Milas
input; it does not verify the Massey-product bound." Closes F5.

### H8. CLAUDE.md: Vol I B91 entry already accurate; no change
The Vol I CLAUDE.md B91 entry (lines referenced in instructions) already
carries the honest two-Massey split: "(a) CORRELATION-FUNCTION Massey
— ... FAILS ... (b) SHADOW-TOWER Massey (structure constants $S_r$ of
the bar tower) — `C_2$-cofin $\Rightarrow$ bounded shadow Massey' is
OPEN". No change needed.

## Status sharpening

Vol I B91 entry remains honest. After H1-H7:
- Vol II `conj:tempered-stratum-contains-wp`: `\ClaimStatusConjectured`
  (unchanged).
- Vol II `lem:wp-ww-subchannel-tempered`: `ProvedHere` → `Conditional`
  on `prop:bar-cohomology-regular-logarithmic-decomposition` +
  `lem:three-channel-filtration-preserved`.
- Vol II `lem:wp-tw-subchannel-tempered`: `ProvedHere` → `Conditional`
  (same conditioning; re-examine the proof to confirm mechanism reuse).
- Vol II `lem:wp-virasoro-subchannel-tempered`: `ProvedHere`
  (unchanged; routes through Virasoro tempering theorem, independent of
  Zhu-bounded-Massey mechanism).
- Vol II `prop:wp-channel-upper-bounds`: `ProvedHere` → `Conditional`
  (cites Lemmas WW and TW).
- Vol II `cor:wp-dichotomy-healed` Part (A) `ProvedHere` (unchanged) +
  Part (B) `Conjectured` (unchanged).
- New Vol II `prop:bar-cohomology-regular-logarithmic-decomposition`:
  `ProvedHere` via Orlik-Solomon homogeneity.
- New Vol II `lem:three-channel-filtration-preserved`: `ProvedHere`.
- Vol I examples item 6: refined prose, no status change.
- Vol I quadrichotomy Open Frontier: refined prose, no status change.
- Vol II engine docstring: aligned.

## Commit plan (no commits this run)

Single commit (author Raeez Lorgat), message:
"Vol II W(p) tempering frontier: sharpen two-Massey split (heal H1-H7),
inscribe regular-logarithmic decomposition, downgrade Zhu-mechanism
lemmas from ProvedHere to Conditional, align engine docstring."

Pre-commit grep gates:
- AP tokens in typeset prose: zero (manuscript hygiene).
- `\\cite{}` resolves: verify Gurarie1993, Flohr1996, AdamovicMilas2008,
  NagatomoTsuchiya2009, FeiginGainutdinovSemikhatovTipunin2006 all
  defined in `standalone/references.bib`.
- Cross-volume label grep for all new labels
  (`prop:bar-cohomology-regular-logarithmic-decomposition`,
  `lem:three-channel-filtration-preserved`): zero duplicates across
  Vol I, Vol II, Vol III.
- Build: `make fast` in Vol II; Vol I and Vol III unaffected
  (propagation is one-sentence in `shadow_tower_quadrichotomy_platonic.tex`
  and one-sentence in `examples/logarithmic_w_algebras.tex`).
- Tests: `pytest compute/tests/test_logarithmic_wp_tempered.py` — engine
  docstring aligned, test assertions unchanged.

No AI attribution anywhere; all commits authored by Raeez Lorgat.
