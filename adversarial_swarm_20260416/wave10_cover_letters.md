# Wave 10 — Adversarial audit: Cover letters and submission documents

**Auditor scope (read-only):**
`standalone/cover_letter_garland_lepowsky.tex` (58 lines, *Journal of Algebra*),
`standalone/cover_letter_seven_faces.tex` (70 lines, *Duke Math. J.*),
`standalone/cover_letter_shadow_towers.tex` (57 lines, *Inventiones*),
`standalone/cover_letter_virasoro_r_matrix.tex` (62 lines, *Letters in Math. Phys.*),
`standalone/editorial.tex` (18 lines; concordance/constitution wrapper, not a cover letter),
plus the four companion papers
(`garland_lepowsky.tex` 1401 ll, `seven_faces.tex` 938 ll,
`shadow_towers.tex` 2318 ll, `virasoro_r_matrix.tex` 395 ll).

**Cross-references:** master CLAUDE.md (Vol I) and Vol III CLAUDE.md;
prior swarm reports `wave1_shadow_classification.md`, `wave2_bp_self_duality.md`,
`wave3_chern_weil_levels.md`, `wave6_introduction_survey.md`,
`wave7_w_algebras_minimal.md`, `wave7_examples_BP_betagamma_KM.md`.

**Date:** 2026-04-16. **Stance:** adversarial referee with HEAL-not-downgrade
mandate. Where a claim survives and admits a sharper restatement, the report
records the upgrade path; where it does not, scope must be tightened.

**Bottom line.** The four cover letters are short, professionally pitched, and
mostly defensible — but each carries at least one promotion, omission, or
status overclaim that an adversarial referee would target on first reading.
Two of the four (Garland–Lepowsky, Virasoro $R$-matrix) make a concrete
promise in the letter that the companion paper either does not support
in the form claimed, or supports only through a tautological "computation".
None of the four has fatal misrepresentation, and three of the four have
a credible *upgrade path* that would let the letter make a stronger,
genuinely defensible claim than the one currently on the page.

`editorial.tex` is not a cover letter — it is a `\documentclass{book}`
archive wrapper that loads the concordance and constitution chapters
of the main monograph. It contains no editorial policy text in itself;
the actual editorial text lives in `chapters/connections/editorial_constitution.tex`,
which is out of scope for this wave.

---

## Section 1 — Per-letter triage table

| # | Letter | Target | Headline claim | Verdict | One-line attack |
|---|---|---|---|---|---|
| L1 | `cover_letter_garland_lepowsky.tex` | *J. Algebra* | "five main theorems" of modular Koszul duality, with explicit $\dim H^n(\widehat{\mathfrak{sl}}_2) = 2n{+}1$ formula and $\kappa(k)+\kappa(-k-2h^\vee)=0$ identity | **NEEDS-TIGHTENING** | The companion paper proves $\dim H^n(B(V_k(\mathfrak{sl}_2))) = 2n{+}1$ but the abstract's general statement is "polynomial growth governed by the Weyl group of $\mathfrak g$" while the Warning at the end of §4 explicitly says higher-rank dimensions differ from CE (§4 Warning, ll. 477–501): for $\mathfrak{sl}_3$, $\dim H^2(B) = 36$ vs $\dim H^2_{\rm CE} = 20$. The cover letter advertises a Weyl-group dimension formula that the paper itself disclaims for rank ≥ 2. |
| L2 | `cover_letter_seven_faces.tex` | *Duke Math. J.* | Master theorem: a single object $r(z)$ has **seven** distinct presentations with **seven** equivalence proofs, **each by an independent compute engine** | **MIXED-OVERCLAIM** | The companion paper §5 lists 14 engines and a per-volume status table that calls F2/F5/F6/F7 "cited" or "specialized" in Vol I (the volume the letter says is being submitted), and *only F1, F3, F4* are "proved" in Vol I. The "each link by an independent argument" part is technically defensible (each F_i↔F_j is a different argument), but "each by an independent compute engine" is a slogan that the table does not support: a single engine (`theorem_three_way_r_matrix_engine`) covers F5, F6, **and** F7 simultaneously. |
| L3 | `cover_letter_shadow_towers.tex` | *Inventiones* | Four results "are proved", including $F_g = \kappa\cdot\lambda_g^{\rm FP}$ for uniform-weight algebras and the explicit $\delta F_2(\mathcal W_3) = (c{+}204)/(16c)$ "negative resolution" of multi-generator universality | **NEEDS-TIGHTENING** | The companion paper's main algebraicity theorem is **explicitly restricted to a one-dimensional primary line** (§ 1.4, Thm 1.2 hypothesis); the letter omits this and presents a *global* shadow-tower theorem. Wave 1 §2.1 documented this exact scope inflation. The "two-independent-methods" tautology flagged in wave 1 is not in *this* cover letter — it lives in the engine code; the letter cleanly states "four results are proved", which is fair. The headline omission is the primary-line scope. |
| L4 | `cover_letter_virasoro_r_matrix.tex` | *LMP* | Two main computations: closed form $R(z) = z^{2h}\exp(-c/(4z^2))$ and the "alternative finite proof" via $S_3(\mathrm{Vir}_c) = 2$ being $c$-independent | **NEEDS-TIGHTENING** | The $S_3=2$ "proof" in the companion paper §4 (Thm 5.1) is the one-line ratio $S_3 = (T_{(1)}T)_{\rm lin}/(T_{(3)}T)_{\rm const} = 2T/(c/2) = 4T/c$, with $\kappa$ cancelling; this is the *defining ratio* of $S_3$ on the Virasoro primary line, *not* an independent computation. Wave 3 (and the audit prompt for this wave) correctly identified this as effectively a BPZ normalization, *not* a shadow-tower derivation. The letter sells it as "an alternative finite proof of class M" but the proof reduces to the definition. The closed form $R(z) = z^{2h}\exp(-c/(4z^2))$ is genuine, and is the strongest defensible headline. |

**Editorial note.** None of the four letters credits an LLM, includes
co-authors other than Raeez Lorgat, or mentions submission to multiple journals.
All four end with the canonical "not under consideration" attestation. **No
AP/cosmetic fixes required on these surface counts.**

---

## Section 2 — Novelty audit (AP155, AP15)

For each letter, the question is: does the letter present as **new** something
that already exists in the literature under a different name, and are the
attributions to prior work correct?

### L1 — Garland–Lepowsky letter

**Headline novelty claim:** "extends the Garland–Lepowsky framework to the
chiral bar complex of the affine Kac–Moody vertex algebra $\widehat{\mathfrak g}_k$
on algebraic curves."

**Audit:**
- The bar cohomology of $V_k(\mathfrak g)$ at non-critical level is Koszul
  via the PBW spectral sequence — the *mechanism* is exactly the Whitehead
  reduction of Garland–Lepowsky 1976, which is what `garland_lepowsky.tex` §3
  spells out. So the letter's framing as a *chiral extension* is honest.
- The **dimension formula** $\dim H^n(\widehat{\mathfrak{sl}}_2) = 2n{+}1$
  is a $\mathfrak{sl}_2$-specific result. The companion paper Remark 4.7
  (l. 691) explicitly says "$\widehat{\mathfrak{sl}}_2$ is the **unique**
  interacting algebra with sub-exponential bar cohomology growth", placing
  it in a hierarchy ($\widehat{\mathfrak{sl}}_3$ conjectural at exponential
  $8^n$). The letter writes "more generally, polynomial growth governed by
  the Weyl group of $\mathfrak g$" — this is **not** what the companion
  proves: higher-rank growth is exponential, not polynomial.
- The **Verdier intertwining** $A^! = $ Chevalley–Eilenberg algebra at the
  Feigin–Frenkel dual level is classical at Vol I level (it is precisely
  what bar-cobar duality on the chiral side delivers); the letter's claim
  is the chiral lift, which is the new content. Status: **defensible**.
- The conductor identity $\kappa(k) + \kappa(-k-2h^\vee) = 0$ is correct
  for affine KM with the trace-form $\kappa$ (wave 3, wave 7); for $\widehat{\mathfrak g}_k$
  in the trace convention, $\kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)$,
  so $\kappa(k) + \kappa(-k-2h^\vee) = \dim(\mathfrak g)[(k+h^\vee) + (-k-h^\vee)]/(2h^\vee) = 0$. ✓

**Attributions:** Garland–Lepowsky 1976 — correctly cited and used.
Kostant 1961 — correctly cited (companion §2). Priddy 1970 (Koszul) —
cited in the companion proof. Feigin–Frenkel — implicitly invoked but
not cited in the letter (the dual level $-k - 2h^\vee$ is theirs).

**Verdict:** the **letter overpromises a Weyl-group polynomial dimension
formula** that the companion does not prove and explicitly denies for
rank ≥ 2. **Healing path:** in the letter, replace "polynomial growth
governed by the Weyl group of $\mathfrak g$" with "polynomial growth
$\dim H^n = 2n{+}1$ for $\widehat{\mathfrak{sl}}_2$, with growth-rate
hierarchy among rank-≥-2 algebras (linear, exponential, sub-exponential)
catalogued in the paper". This is **stronger** than the current claim
because it names the hierarchy explicitly and pins the linear case to
$\mathfrak{sl}_2$.

### L2 — Seven-faces letter

**Headline novelty claim:** "a single algebraic object … appears in seven
independent mathematical traditions under seven different names" and the
master theorem proves a seven-way identification.

**Audit (AP155 trigger).** Each of the seven faces is a **known object**
from prior literature (Drinfeld 1985, STS 1983, FFR 1994, GK/Hinich,
DNP 2025, KZ 2025, GZ 2026). The novelty is the **identification**, not
the objects. Inflation analysis (consistent with wave-6 finding on
"7 vs 4"):

- Faces F5 (Yangian $r$-matrix) and F6 (Sklyanin tensor) are **classically
  identified** by Drinfeld 1985 / Semenov-Tian-Shansky 1983; the letter
  itself states "the identification F5⇔F6 is Drinfeld's and
  Semenov-Tian-Shansky's classical result" (l. 343). So F5 and F6 are
  not two new "presentations": they are already known to be the same
  object under quantization/dequantization. Counting them as two
  separate faces is double-counting in a way the letter does not flag.
- Faces F4 (GZ commuting differentials) and F7 (Gaudin generator) are
  the **same operator** at different analytic limits: F4 = differential
  operator order $k_{\max}-1$ for $k_{\max} \geq 3$; F7 = simple-pole
  truncation. The companion §3 ¶ "F4 ⇔ F7" (ll. 390–401) explicitly
  derives F4 from F7 by collision-residue extraction at $k=1$: same
  formula. So F4 and F7 are also a paired identification.
- Faces F3 (PVA $r$-matrix) and F1 (twisting morphism) live in dual
  categorical worlds (classical vs $E_1$); the F1⇔F3 identification
  is the Koszul-bar duality between PVA and chiral algebra, which is
  also classical at Vol I level (Tamarkin et al.).
- Faces F1 (twisting morphism, GK/Hinich) and F2 (DNP line operator
  $R$-twist) are the **bar-cobar identification** — also a known
  identification under translation between two languages.

**Genuine "new" content:**
- The **identification of F4/F7 with F1** via the bar-intrinsic
  $\Theta_{\mathcal A}$ is the new arrow; everything else is either
  classical (F5⇔F6) or a translation (F1⇔F2, F1⇔F3, F1⇔F4 by GZ26
  pull-back).
- The number of *genuinely new* identifications proved in this paper
  is **closer to 4** (F1↔F2, F1↔F3, F1↔F4, F4↔F7) than 7. Counting
  F5 and F6 as separate "new presentations" is the inflation. This is
  the wave-6 "4 distinct objects inflated to 7 presentations" finding,
  precisely.

**Attributions:** Drinfeld 1985, STS 1983, FFR 1994, Ginzburg–Kapranov,
Hinich, Dimofte–Niu–Py 2025, Khan–Zeng 2025, Gaiotto–Zeng 2026 — all
**correctly cited** in the companion. The letter itself does not cite,
but names them; this is normal cover-letter practice.

**Verdict:** **letter inflates the count from 4 genuinely new
identifications to 7 "presentations"**, with two of the seven (F5, F6)
being a pair already classically identified by Drinfeld and STS, and
(F4, F7) being two analytic limits of the same operator. **Healing
path:** restate in the letter as "the collision residue $r(z)$ unifies
seven presentations of three pre-existing structural types
(twisting-morphism / classical-$r$-matrix / commuting-Hamiltonian),
with four genuinely new bilateral identifications proved in this
paper". The companion paper's §6 status table makes this honest reading
available; the cover letter inverts it.

### L3 — Shadow towers letter

**Headline novelty claim:** "first complete modular Koszul duality theory
on algebraic curves, unifying and extending work of Beilinson–Drinfeld,
Francis–Gaitsgory, Loday–Vallette, and Costello–Gwilliam."

**Audit:**
- Beilinson–Drinfeld 2004 (chiral algebras): the chiral bar complex on
  algebraic curves is *theirs*. The letter's framing "extending classical
  Koszul duality from graded algebras over a field to chiral algebras
  on algebraic curves" is *exactly* what BD did. So "first complete
  modular Koszul duality theory on algebraic curves" is **defensible
  only with the qualifier "modular"** (i.e., over $\overline{\mathcal M}_{g,n}$,
  with the genus expansion built in). BD's framework is at the level
  of $\Ran(X)$; the *modular* extension to $\overline{\mathcal M}_{g,n}$
  is the new content.
- Francis–Gaitsgory 2012 (chiral Koszul duality): they prove chiral
  Koszul duality at $\Ran(X)$. Again, the *modular extension* is the new
  content.
- Loday–Vallette: classical bar-cobar duality. The chiral lift is the
  new content.
- Costello–Gwilliam: factorization algebras, BV-quantization. The
  identification with the modular bar-cobar machine is part of the
  programme.

**Verdict:** the "first" claim is defensible with a one-word edit:
"first complete **modular** Koszul duality theory on algebraic curves"
→ this is fine because "modular" is exactly what extends BD/FG/LV/CG.
But as written, the prose reads as if "Koszul duality on algebraic
curves" is being introduced for the first time, which inverts the
attribution. **Healing path:** rephrase: "first complete *modular*
Koszul duality theory on $\overline{\mathcal M}_{g,n}$, extending the
Ran-space bar constructions of Beilinson–Drinfeld and Francis–Gaitsgory,
the operadic Koszul duality of Loday–Vallette, and the BV-factorization
framework of Costello–Gwilliam to the modular setting".

**Attributions:** correct, but mis-balanced (the new word *modular* is
buried; the old word *Koszul* is foregrounded). Independent of
attribution, the body of the letter is honest: each of the four results
is stated as "is proved", which matches the companion's `\begin{theorem}`
environments.

### L4 — Virasoro $R$-matrix letter

**Headline novelty claim:** "a closed-form expression for the spectral
$R$-matrix of the Virasoro algebra on a primary state of conformal weight
$h$: $R(z) = z^{2h}\exp(-c/(4z^2))$."

**Audit:**
- The closed form $R(z) = z^{2h}\exp(-c/(4z^2))$ is **genuinely new in
  the bar-cobar / collision-residue framework**. The exponential of a
  scalar function of $z$ on a primary state with $L_0$ eigenvalue $h$
  reduces to abelian path-ordering, and the Virasoro central term
  $c/(4z^2)$ is the only quantum correction. As a *closed-form
  $R$-matrix on the Virasoro primary line*, this is a clean, finite,
  publishable result.
- The "alternative finite proof of class M membership" via $S_3 = 2$
  (companion §4 Thm 5.1) is the issue: the proof is one line,
  $S_3 = 2T/(c/2) \cdot \kappa/\kappa = 2$, with $\kappa$ cancelling.
  This is **the BPZ normalization** of Virasoro, not a shadow-tower
  derivation. The letter's claim "providing an alternative finite
  proof of class M membership" oversells a one-line ratio extraction
  as a separate proof method. The genuine content is that the
  $c$-independence falls out trivially from the structure of the OPE,
  which is interesting but not a "proof" in the sense the cover letter
  implies.

**Attributions:** BD, BPZ, FBZ, FG, Kac, Zhu — all correctly cited in
the bibliography of the companion paper. The letter itself names BPZ
implicitly (the Virasoro OPE is BPZ). No mis-attribution.

**Verdict:** the **closed-form $R$-matrix is the strongest defensible
headline**. The "alternative finite proof of class M via $S_3 = 2$" is
**reframable**: it is not an independent proof, it is a definition-level
observation that the cubic shadow on the Virasoro primary line is
$c$-independent. **Healing path:** drop "alternative finite proof" from
the letter and replace with "and the cubic shadow $S_3(\mathrm{Vir}_c) = 2$
is $c$-independent — a structural statement that follows directly from
the BPZ normalization of the Virasoro OPE on the primary line." This is
sharper *and* honest, and frees the letter to lead more strongly with
the closed form.

---

## Section 3 — Status overclaim analysis (AP4, AP40, AP-CY11)

For each letter, the cross-volume status of cited theorems vs the
status presented to the editor:

### L1 — Garland–Lepowsky letter

| Claim in letter | Status in companion | Status in CLAUDE.md | Verdict |
|---|---|---|---|
| "$\widehat{\mathfrak g}_k$ is chirally Koszul at all non-critical levels" | `\begin{theorem}` Thm 4.2, proof via PBW SS collapse | "PBW concentration, $V_k(\mathfrak g)$ is Koszul for all $k \neq -h^\vee$" — Vol I L420 (Thm-A) | **Consistent**, ProvedHere defensible |
| "Verdier intertwining theorem identifies the chiral Koszul dual with the chiral envelope at the Feigin–Frenkel dual level" | Companion Thm 4.4 (Verdier intertwining) | Vol I AP/conductor entries; rho_K = 0 for KM | **Consistent**, but the letter promises a *theorem* called "Verdier intertwining" with a specific name; the companion paper's Verdier intertwining theorem is **proved on the evaluation-generated core** (cf wave 6 finding O9: "MC4 — proved on standard landscape; one-stop limit conditional"). The letter elides "evaluation-generated core". |
| "bar cohomology dimensions are level-independent outside a finite exceptional set, with $\dim H^n(\widehat{\mathfrak{sl}}_2) = 2n{+}1$" | Companion Cor 4.6 (the explicit $\mathfrak{sl}_2$ formula) | Vol I CLAUDE.md does not list this as a theorem; it is companion-internal | The $\mathfrak{sl}_2$ count is fine; the *level-independence outside an exceptional set* is **not** proved in the companion paper — the companion says level-independence for non-critical $k \neq -h^\vee$, but the letter's "outside a finite exceptional set" suggests a stronger result. |
| "shadow obstruction tower terminates at degree 3 (class L)" | Companion Thm 5.x — class L for $\widehat{\mathfrak g}_k$ | Vol I CLAUDE.md / classification.tex: confirmed class L for KM | **Consistent** |
| "modular characteristic $\kappa = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)$ is additive and satisfies $\kappa(k)+\kappa(-k-2h^\vee) = 0$" | Companion: yes | Vol I AP39: $\kappa(\widehat{\mathfrak g}_k) = \dim(\mathfrak g)(k+h^\vee)/(2h^\vee)$ verified | **Consistent** |

**Verdict:** L1 status claims are **mostly consistent** with the companion;
two minor scope omissions ("evaluation-generated core" and "finite
exceptional set"). Both can be repaired by tightening the letter prose.

### L2 — Seven-faces letter

| Claim in letter | Status in companion | Status in CLAUDE.md | Verdict |
|---|---|---|---|
| "main theorem establishes a seven-way identification chain F1⇔F2⇔⋯⇔F7" | Companion Thm 3.1 — but the per-face status table (companion §6) lists F2, F5, F6, F7 as **"specialized"** in Vol I | Vol I CLAUDE.md does not list "Seven-faces" as a single named theorem; it appears in `seven_faces.tex` standalone only | Letter promises "seven-way identification chain"; companion delivers a **chain** but four of the seven faces are "specialized", which means proved in another volume of the monograph and **specialized to the standard landscape** in Vol I. The letter omits the volume-status decomposition. |
| "with each link proved by an independent argument and verified by an independent compute engine" | Companion §5 — 14 engines, with `theorem_three_way_r_matrix_engine` covering F5, F6, **and** F7 simultaneously | n/a | "Each link by an *independent* compute engine" is **false at face value**: at minimum F5/F6/F7 share an engine. **AP155 / AP10 violation**: the letter overstates the independence of verification. |
| "agreement is controlled by three numerical invariants $(p_{\max}, k_{\max}, r_{\max})$ classifying the standard landscape into four shadow classes G, L, C, M" | Companion §4 invariants table | Vol I CLAUDE.md: G/L/C/M classification confirmed | **Consistent** |
| "trichotomy of Hamiltonian operator orders {0, 0, ≥ 2} for classes {G ∪ L, C, M}" | Companion §4 trichotomy | Wave 1 §2.2 noted the "trichotomy vs quadrichotomy" oscillation in the standalone files, with class C grafted on by stratum separation | **Defensible at $k_{\max}$ trichotomy level**, but the four-class partition under the same name is a different invariant ($r_{\max}$). The letter conflates the two without acknowledging. |

**Verdict:** L2 makes two non-negligible status overstatements (independent
engines, hidden volume-specialization). The trichotomy/quadrichotomy
oscillation surfaces in the abstract.

### L3 — Shadow towers letter

| Claim in letter | Status in companion | Status in CLAUDE.md | Verdict |
|---|---|---|---|
| "shadow obstruction tower… is algebraic of degree 2 along each primary line, governed by a shadow metric" | Companion Thm 1.2 with explicit primary-line hypothesis | n/a | **Consistent if "primary line" is in the letter** — but the letter writes "is algebraic of degree 2 along each primary line", which is fine. ✓ |
| "the critical discriminant $\Delta = 8\kappa S_4$ partitions the standard landscape into four depth classes" | Companion Thm 1.3 four-class partition | Vol I CLAUDE.md: G/L/C/M classification | **Consistent**, but class C is via stratum separation (companion l. 232), not directly from the discriminant — the letter's "partitions … into four depth classes" elides this. |
| "$F_g = \kappa \cdot \lambda_g^{\rm FP}$ for uniform-weight algebras" | Companion Thm 1.5 | Vol I CLAUDE.md AP32: "obs_g, F_g, lambda_g must carry UNIFORM-WEIGHT or ALL-WEIGHT tag" | **Consistent and properly scoped** ("for uniform-weight algebras"). ✓ |
| "multi-weight algebras exhibit a genuine cross-channel correction ($\delta F_2(\mathcal W_3) = (c+204)/(16c)$), resolving the multi-generator universality problem negatively" | Companion Thm 1.5 + Rem | Vol I CLAUDE.md: cross-channel correction, multi-generator universality resolved negatively | **Consistent** ✓ |
| "gravitational coproduct obtained by BRST reduction is strictly primitive at all degrees" | Companion §… (later) | Vol I CLAUDE.md: gravitational coproduct primitive | **Consistent** ✓ |

**Verdict:** L3 is the **cleanest of the four cover letters** at the
status-claim level. The headline "first complete modular Koszul duality
theory" needs minor attribution rebalancing (§2 above), but the in-body
result claims match the companion environments. **No "two independent
methods" tautology in the letter** — that lives in the engine code, and
the letter prudently does not invoke it.

### L4 — Virasoro $R$-matrix letter

| Claim in letter | Status in companion | Status in CLAUDE.md | Verdict |
|---|---|---|---|
| "closed-form expression for the spectral $R$-matrix … $R(z) = z^{2h}\exp(-c/(4z^2))$" | Companion Computation 2.1 — a `\begin{computation}` environment, not `\begin{theorem}` | n/a | **Status mismatch**: letter says "main result is a closed-form expression" (theorem-level claim); companion calls it a `\begin{computation}` (definition-level). Cover letter promotes a Computation to a Theorem implicitly. |
| "$S_3(\mathrm{Vir}_c) = 2$ is proved to be independent of the central charge $c$, providing an alternative finite proof of class M membership" | Companion Thm 5.1 (`\begin{theorem}`) | Vol I CLAUDE.md AP39: $\kappa = c/2$ for Virasoro; cubic shadow is the "first higher obstruction beyond $\kappa$" | The companion *does* tag $S_3=2$ as `\begin{theorem}`, so the status promotion is consistent at the companion level. The "alternative finite proof of class M" framing is what oversells: the proof is the BPZ ratio (§2 / wave 3 finding). |
| "first correction $R_2 = -c/4$ is the genus-zero $A_\infty$-formality obstruction" | Companion Prop 6.1 (Non-formality witness) | Vol I CLAUDE.md: non-formality of Virasoro consistent with class M | **Consistent**, but "genus-zero $A_\infty$-formality obstruction" is a strong claim that requires the **shadow-formality identification** $S_3 \neq 0 \Leftrightarrow m_3 \neq 0$ — wave 1 §2.6 documented that this identification is proved by gesture, not by careful sign/weight comparison. The letter inherits the gestural status. |

**Verdict:** L4 has one genuine **status promotion** (Computation →
Theorem in the cover letter), one **scope inflation** ($S_3=2$ ratio
sold as "alternative proof"), and one **inherited weakness**
(shadow-formality identification at chain level). All three are repairable.

---

## Section 4 — Internal-consistency check (letter vs companion paper)

For each letter, the question is: does every theorem promised in the
letter have a matching `\begin{theorem}` (or equivalent) in the companion,
with the same statement?

### L1 — Garland–Lepowsky

| Letter promise | Companion environment | Match? |
|---|---|---|
| (1) chirally Koszul at all non-critical $k$ | Thm 4.2 (`\begin{theorem}[Chiral Koszulness of $V_k(\mathfrak g)$]`) | **YES** ✓ |
| (2) Verdier intertwining theorem | Thm 4.4 / proposition with this name in companion | **YES** but with "evaluation-generated core" qualifier in body |
| (3) bar cohomology dimensions level-independent | Cor 4.6 + Prop 4.7 | **PARTIAL**: $\mathfrak{sl}_2$ explicit; "level-independent outside finite exceptional set" not stated as a single theorem |
| (4) shadow tower terminates at degree 3 | Discussed in §5 | **YES** at proposition level |
| (5) $\kappa$ formula and conductor identity | Stated in companion §1 abstract | **YES** ✓ |

**Verdict:** 4/5 matches with one partial. The letter's "five main
theorems" framing is honest but item (3) requires editor latitude.

### L2 — Seven-faces

| Letter promise | Companion environment | Match? |
|---|---|---|
| Master theorem (seven-way identification) | Thm 3.1 (`\begin{theorem}[Seven-face identification]`) | **YES** ✓ |
| "each link by an independent compute engine" | §5 — 14 engines, but several engines cover multiple faces | **NO**: shared engines for F5/F6/F7 |
| Three invariants classifying into four classes | §4 invariants table | **YES** ✓ |
| Trichotomy {0, 0, ≥ 2} for {G∪L, C, M} | §4.x | **YES** ✓ |

**Verdict:** 3/4 with one engine-independence overclaim.

### L3 — Shadow towers

| Letter promise | Companion environment | Match? |
|---|---|---|
| Shadow tower algebraic of degree 2 along each primary line | Thm 1.2 (algebraicity) | **YES** ✓ |
| Four-class partition by $\Delta = 8\kappa S_4$ | Thm 1.3 | **YES** with class C via stratum separation caveat |
| $F_g = \kappa \cdot \lambda_g^{\rm FP}$ uniform-weight | Thm 1.5 | **YES** ✓ |
| $\delta F_2(\mathcal W_3) = (c+204)/(16c)$ | Thm 1.5 (genus-2 universality) | **YES** ✓ |
| Gravitational coproduct primitive | Later theorem in companion | **YES** ✓ |

**Verdict:** 5/5. **The cleanest letter-companion correspondence.**

### L4 — Virasoro $R$-matrix

| Letter promise | Companion environment | Match? |
|---|---|---|
| Closed form $R(z) = z^{2h}\exp(-c/(4z^2))$ | Computation 2.1 (`\begin{computation}`) | **PARTIAL**: companion uses Computation, letter says "main result" |
| $S_3 = 2$ $c$-independence | Thm 5.1 (`\begin{theorem}`) | **YES** at status, **WEAK** at content (BPZ ratio) |
| $R_2 = -c/4$ as non-formality witness | Prop 6.1 | **YES** at status, **WEAK** at content (gestural) |
| Class M certified | Cor 5.2 | **YES** ✓ |

**Verdict:** 2/4 strong, 2/4 partial. The strongest defensible result
(closed form) is the one with the weakest status environment in the
companion (Computation, not Theorem); the inverse holds for $S_3 = 2$.

---

## Section 5 — First-principles analyses (per AP-CY61 / AP186 protocol)

### 5.1 The "alternative finite proof of class M" in L4 — the ghost theorem

**Wrong claim (effective).** "$S_3(\mathrm{Vir}_c) = 2$ provides an
alternative finite proof of class M membership."

**The ghost theorem.** What the claim *gets right*: the cubic shadow on
the Virasoro primary line is genuinely $c$-independent — this is a
non-trivial structural feature, since *a priori* the cubic shadow could
depend on every OPE coefficient. The cancellation $\kappa/\kappa = 1$
in the ratio reflects a **homogeneity** of the cubic obstruction in the
modular characteristic. In modular Koszul duality, this homogeneity is
exactly what underwrites the algebraicity theorem $H^2 = t^4 Q$ (wave 1):
the cubic shadow $S_3 = \alpha$ enters $Q$ as a coefficient *additively*
(via $12 \kappa \alpha t$), and the ratio extraction is the
zero-eigenvalue mode of the convolution. So "$S_3 = 2$" is not a
proof of class M, but it **is** the structural witness that the *Virasoro
primary line is on the constant-$\alpha$ section of the algebraicity
fibration*.

**The correct relationship.** Class M membership for Virasoro is proved
by $\Delta = 8\kappa S_4 \neq 0$, not by $S_3 \neq 0$. The cubic shadow
is the witness for class **L** (Lie); the discriminant $\Delta$ is the
witness for class **M** (mixed). The letter conflates these two
witnesses.

**Healing path.** Replace "alternative finite proof of class M" with
"the structural witness that Virasoro lies on the homogeneous section
of the algebraicity fibration ($S_3 = $ constant in $c$)". Class M is
proved separately by $\Delta_{\rm Vir} = 40\kappa S_4 = 40 \cdot c \cdot
1/[c(5c+22)] \cdot (1/2) \neq 0$.

### 5.2 The "seven independent compute engines" claim in L2 — the ghost theorem

**Wrong claim.** "Each link of the seven-way chain is verified by an
*independent* compute engine."

**The ghost theorem.** What the claim *gets right*: there are 14 compute
engines in the seven-faces project, each implementing a specific
verification step (Yangian $r$-matrix, GZ commuting differentials,
Sklyanin bracket, …). The verification is genuinely **structural**: each
engine produces a numerical value or symbolic identity that is then
matched across engines.

**What the claim *gets wrong*.** The 14 engines do not partition the
seven faces; some engines verify multiple faces simultaneously (e.g.,
`theorem_three_way_r_matrix_engine` covers F5, F6, **and** F7 in one
computation). So "each link by an independent engine" is false; what is
true is "each face is covered by at least one engine, and the engines
verify the face identifications collectively". This is a weaker but
still respectable claim.

**The correct relationship.** The 14 engines provide
**network-redundant** verification: 7 faces × 14 engines, with overlaps,
gives a verification graph that is connected and densely covered, but
not a 1-1 face-to-engine matching. The right framing is "verification
network with per-face coverage ≥ 2 and per-link coverage ≥ 1", not
"independent engines".

**Healing path.** Replace "each link verified by an independent compute
engine" with "the seven-face identification is verified by a network of
14 compute engines covering all face pairs with overlap; the per-engine,
per-face test allocation is in §5 of the paper".

### 5.3 The "first complete modular Koszul duality theory" claim in L3 — the ghost theorem

**Wrong claim (mild).** "first complete modular Koszul duality theory"
unifying BD, FG, LV, CG.

**The ghost theorem.** What the claim *gets right*: the **modular**
extension of chiral Koszul duality from $\Ran(X)$ to $\overline{\mathcal M}_{g,n}$,
incorporating the genus expansion via stable graphs, is genuinely new
in this paper. The four-class partition (G/L/C/M) and the shadow metric
$Q(t)$ are also genuinely new structural inputs.

**What the claim *gets wrong*.** "First complete modular Koszul duality
theory" reads as "first Koszul duality on algebraic curves", which
inverts the attribution to BD and FG. The new word is **modular**, not
*Koszul* and not *on algebraic curves*.

**The correct relationship.** The stack of contributions is:
- BD 2004: chiral algebras on $\Ran(X)$, bar complex.
- FG 2012: chiral Koszul duality on $\Ran(X)$.
- LV 2012: operadic Koszul duality (algebraic curves not yet).
- CG 2017: factorization algebras, BV.
- **This paper:** the modular extension to $\overline{\mathcal M}_{g,n}$,
  the algebraicity of the shadow tower, the four-class partition.

**Healing path.** Insert "modular" prominently: "first complete modular
Koszul duality theory on $\overline{\mathcal M}_{g,n}$, building on the
chiral Koszul duality of Beilinson–Drinfeld and Francis–Gaitsgory at
$\Ran(X)$, the operadic Koszul duality of Loday–Vallette, and the
factorization-algebra framework of Costello–Gwilliam".

### 5.4 The "polynomial growth governed by the Weyl group" claim in L1 — the ghost theorem

**Wrong claim.** "$\dim H^n(\widehat{\mathfrak g}_k)$ has polynomial
growth governed by the Weyl group of $\mathfrak g$".

**The ghost theorem.** What the claim *gets right*: the classical
Garland–Lepowsky theorem expresses $H^*(\mathfrak n_-^{\rm loop})$ in
terms of the affine Weyl group, and the **Euler characteristic** at
each conformal weight is governed by the Weyl group.

**What the claim *gets wrong*.** The **dimension** of bar cohomology in
the chiral setting is *not* the Weyl-group count. The companion's own
Warning 4.x (l. 477–501) makes this explicit: for $\mathfrak{sl}_3$,
$\dim H^2(B) = 36$ vs $\dim H^2_{\rm CE} = 20$. The chiral bar carries
an Orlik–Solomon form factor that the Lie cochain does not. So the
Garland–Lepowsky concentration survives, but the *dimension* does not
match the Weyl-group count.

**The correct relationship.** The Garland–Lepowsky concentration
(*single bidegree*) survives in the chiral setting; the
*Weyl-group dimension formula* does not, except for $\mathfrak{sl}_2$
where the Orlik–Solomon factor coincides with the Lie cochain.

**Healing path.** Replace the letter's "polynomial growth governed by
the Weyl group of $\mathfrak g$" with "polynomial growth in the
$\mathfrak{sl}_2$ case ($\dim H^n = 2n+1$); the Garland–Lepowsky
concentration into a single bidegree per conformal weight survives for
all simple $\mathfrak g$, with explicit dimension formulas dependent
on the rank".

### 5.5 The "two-independent-methods" tautology in `shadow_towers.tex` — does it surface in the cover letter?

**Wave-1 finding.** The shadow_towers compute engine has two methods
(`mc_recursion_rational` and `sqrt_ql_rational`) that compute the same
identity $H^2 = t^4 Q$ in two notational forms; the engine claims they
are "independent verifications", but they are algebraic restatements
of the same recursion.

**Cover letter check.** L3 (cover_letter_shadow_towers.tex) **does not
invoke this tautology**: the letter's "Four results are proved" is
based on the four `\begin{theorem}` environments in the companion,
not on the engine cross-validation. **No surface in cover letter.**

**Verdict:** L3 prudently sidesteps the wave-1 tautology. The letter
is clean on this front.

---

## Section 6 — Three upgrade paths (stronger claims to make)

The user's brief is HEAL-not-downgrade: where the letter can defensibly
say *more*, identify what.

### Upgrade 6.1 — L2 (Seven-faces): from "seven presentations" to "Sasaki diagram"

**Current.** Seven faces, identified pairwise.

**Upgrade.** State the seven-face identification as a *Sasaki diagram*
— a commutative graph with 7 vertices (the faces) and 6+ edges (the
proven equivalences), with the edges classified by **arrow type**:
classical-quantum (F5↔F6), spectral-coordinate (F4↔F7), categorical
(F1↔F2), semiclassical (F1↔F3). Then the "novelty" claim becomes "the
Sasaki diagram has 4 new edges; the other 3 were classically known and
are recovered". This is **stronger** than the current claim because
it articulates the architecture; it is **more honest** because it
acknowledges classical edges; and it gives the editor a clean image
of what is contributed.

The "F1↔F2↔F3↔F4↔F5↔F6↔F7" linear chain also reads as a single path,
which is misleading: the actual graph is closer to a wheel with F1
at the center. State the wheel.

### Upgrade 6.2 — L4 (Virasoro): from "closed form on a primary state" to "$E_1$-Hopf $R$-matrix"

**Current.** Closed form $R(z) = z^{2h}\exp(-c/(4z^2))$ on a
primary state.

**Upgrade.** The closed form is the abelian path-ordered exponential of
the rank-1 $\Theta_{\rm Vir}$ on the primary line. This is the
**universal $R$-matrix of the $E_1$-chiral bialgebra structure on
$B^{\rm ord}({\rm Vir}_c)$ restricted to the primary lane**. Stating it
this way (a) connects to the $E_1$-chiral bialgebra programme of Vol II
(AP-CY23), (b) makes the LMP audience see the link to integrable
systems, (c) places the result inside a structural framework rather
than as an isolated computation. The $S_3 = 2$ result then becomes a
**consequence** of the closed form (cubic shadow = 2 means
$\partial_z^2 \log R$ has a simple pole at $z=0$ with residue $-c/2$,
modulo conventions), not an "alternative finite proof".

### Upgrade 6.3 — L3 (Shadow towers): from "Riccati-quadratic" to "spectral curve"

**Current.** $H(t)^2 = t^4 Q(t)$, with $Q$ quadratic.

**Upgrade.** The relation $H^2 = t^4 Q$ defines a *spectral curve*
$\Sigma_A := \{H^2 = t^4 Q\}$ in the $(t, H)$-plane, parametrized by
the three invariants $(\kappa, \alpha, S_4)$. The shadow-tower
coefficients $S_r$ are residues of the meromorphic differential
$\eta_A := H \,dt / t^{r+1}$ on $\Sigma_A$. This **embeds the modular
Koszul duality framework into the Eynard–Orantin topological recursion
formalism**: the shadow tower is the topological recursion on $\Sigma_A$
restricted to genus zero. The four-class partition then corresponds to
**four shapes of the spectral curve**: G (degenerate, double cover),
L (parabola), C (special quartic), M (smooth quadratic). This is the
**Annals-grade restatement** wave 1 §2.1 already proposed; the cover
letter could lead with it.

The wave-1 audit suggested an even stronger upgrade: a *matrix-Riccati*
extension to multi-lane chiral algebras, with $\delta F_2(\mathcal W_3)$
sitting inside a higher-dimensional quadric. This would resolve the
"multi-generator universality problem" *positively* at the abstract
level. If this can be supported, it is a stronger headline than the
"resolved negatively" current framing.

---

## Section 7 — Punch list

In order of priority. Each item is one specific edit to the cover
letter (not the companion paper). Items P1–P5 are HIGH (would be
flagged by a hostile referee on first reading). Items P6–P12 are
medium. Items P13+ are minor.

### High priority (HIGH-1 through HIGH-5)

P1. **L1, l. 39:** "polynomial growth governed by the Weyl group of $\mathfrak g$"
    is **falsified** by the companion's own Remark 4.7 (linear growth
    is unique to $\mathfrak{sl}_2$; higher rank is exponential).
    Replace with: "with $\dim H^n = 2n{+}1$ for $\widehat{\mathfrak{sl}}_2$,
    and a growth-rate hierarchy (linear, exponential by rank) catalogued
    in the paper".

P2. **L2, ll. 47–49:** "each link proved by an independent argument and
    verified by an independent compute engine" — FALSE on the
    independent-engine claim (`theorem_three_way_r_matrix_engine` covers
    F5, F6, F7 simultaneously). Replace with: "each link by an
    independent argument; the seven-face identification is verified
    by a 14-engine compute network with each face covered by at least
    two engines".

P3. **L2, ll. 30–44:** Seven-face enumeration counts F5 (Yangian
    $r$-matrix) and F6 (Sklyanin tensor) as **two separate
    presentations**, but the letter itself states (l. 53–54) that
    F5↔F6 is "the classical theorem of Drinfeld and STS". This is
    **double-counting**. Restate as: "seven presentations across four
    structural types (twisting morphism, classical $r$-matrix,
    commuting Hamiltonian, Poisson tensor), with four genuinely new
    bilateral identifications proved here".

P4. **L4, ll. 24–34:** "closed-form expression for the spectral
    $R$-matrix" — companion calls it a `\begin{computation}`, not a
    `\begin{theorem}`. Either upgrade the companion environment to
    `\begin{theorem}` (the proof in Computation 2.1 is fully rigorous;
    the upgrade is justified) or downgrade the letter's claim from
    "main result" to "main computation". Recommended: upgrade the
    companion.

P5. **L4, ll. 48–50:** "alternative finite proof of class M membership"
    — the $S_3 = 2$ argument is the BPZ ratio extraction, not an
    independent class-M proof (class M is via $\Delta \neq 0$, not
    $S_3 \neq 0$). Replace with: "and the cubic shadow $S_3 = 2$ is
    $c$-independent — a structural witness to homogeneity of the
    Virasoro primary line in the algebraicity fibration".

### Medium priority (MED-6 through MED-12)

P6. **L3, ll. 47–49:** "first complete modular Koszul duality theory"
    — needs prominent "modular" qualifier to avoid attribution
    inversion against BD, FG. Rewrite per §5.3 healing path.

P7. **L1, l. 36:** "Verdier intertwining theorem" — companion proves
    on the evaluation-generated core. State this scope in the letter
    as "(on the evaluation-generated core)".

P8. **L1, l. 37:** "level-independent outside a finite exceptional set"
    — companion proves only at non-critical $k \neq -h^\vee$, not
    "outside a finite exceptional set" (which is a stronger claim).
    Replace with "at all non-critical levels $k \neq -h^\vee$".

P9. **L2, ll. 50–53:** trichotomy {0, 0, ≥ 2} for {G ∪ L, C, M} is
    the operator-order trichotomy ($k_{\max}$); the four-class
    partition is shadow depth ($r_{\max}$). The letter conflates
    them under "trichotomy". Disambiguate: "the operator-order
    trichotomy $k_{\max} \in \{0, 1, \geq 3\}$, distinct from the
    four-class shadow-depth partition $r_{\max} \in \{2,3,4,\infty\}$".

P10. **L4, ll. 41–46:** "$R_2 = -c/4$ … generates the infinite
     primitive-cumulant series" — depends on the shadow-formality
     identification, which is proved by gesture in the companion
     (wave 1 §2.6). Either tighten the companion proof or downgrade
     "generates" to "is the leading term in".

P11. **L3, ll. 27–34:** mention class C (depth 4) explicitly. The
     letter currently lists G/L/M/contact in the abstract but does
     not name class C, which the companion does. Add the class label.

P12. **L4, ll. 36–40:** "bosonic parity of the desuspended Virasoro
     generator" — the parity argument is for *single-generator
     bosonic algebras of integer spin*. Add scope: "for single-generator
     bosonic algebras of integer spin".

### Minor (MIN-13+)

P13. **All four letters:** add the canonical `Co-Authored-By: …` line
     attestation that no AI was used to author scientific content
     (per CLAUDE.md). [Optional; not standard in cover letters.]

P14. **L2, l. 65:** "tradition of publishing work at the interface" —
     standard cover-letter cliché. Could be sharpened with one named
     prior Duke paper to anchor the tradition (e.g., a recent
     conformal-blocks or geometric-Langlands paper in Duke).

P15. **L1, l. 49:** "natural venue given the algebraic content" —
     similarly bland. Could name a *J. Algebra* paper on Kac–Moody
     vertex algebras as anchor.

P16. **L4, l. 49:** "well suited to *Letters in Mathematical Physics*"
     — the LMP page-limit constraint is real (typically ≤ 25 pages);
     the companion is 395 lines ≈ 12 pages, which is fine. No edit
     needed; consider noting the page count in the letter.

P17. **L3, l. 41:** "($\delta F_2(\mathcal W_3) = (c{+}204)/(16c)$)"
     — wave 1 §2.7 noted this is computed correctly but verified only
     within the same Frobenius-algebra framework (no independent
     conformal-block check). Adding a sentence "verified by stable-graph
     summation across seven graphs and cross-checked at seven values
     of $c$" would defuse the AP-CY49 / AP10 attack.

P18. **L1, ll. 31–44:** "(1)…(2)…(3)…(4)…(5)" — five numbered results,
     but the companion paper has more than five theorems (the dimension
     count, the Weyl-group structure, the Garland–Lepowsky reduction,
     the PBW collapse, etc.). The "five theorems" framing is a
     *selection*, not an enumeration. Frame as "five headline results"
     to avoid the implication of completeness.

P19. **All four letters:** the canonical Vol-status decomposition
     ("proved in Vol I", "specialized to standard landscape", etc.)
     could be moved into a concise footer paragraph. This is best
     practice for multi-volume programmes and pre-empts the editor's
     "what's actually new in the submitted paper?" question.

---

## Section 8 — Patterns appearing 2+ times (cache write-back)

Per CLAUDE.md HZ3-11 and the cache write-back protocol of 2026-04-15,
patterns surfacing twice or more across waves get promoted to the
first-principles cache. From this wave's findings:

### CACHE ENTRY (proposed) — "Cover letter Computation→Theorem promotion"

**Pattern.** A cover letter promotes a `\begin{computation}` (or
`\begin{construction}`, or even `\begin{remark}`) in the companion
paper to "main theorem" status in the letter. The reader (editor)
takes the letter at face value and expects a `\begin{theorem}`
environment, finding only a Computation. Pattern surfaced in: this
wave (L4 closed-form $R$-matrix); previously in
`introduction_full_survey.tex` ProvedHere tag inflation (wave 6 O5).

**Healing.** Either upgrade the companion environment or downgrade the
letter's verb. In submission settings, the upgrade is usually
justified (a Computation that is fully rigorous and standalone
deserves theorem status).

**Cache slot:** appendices/first_principles_cache.md, after entry on
"narrate vs construct" (AP-CY57 cluster). Confusion type:
**status/environment** (new sub-type, related to label/content).

### CACHE ENTRY (proposed) — "Independence overclaim on verification engines"

**Pattern.** A cover letter or programme summary asserts that a
multi-step result is verified by **independent compute engines**, but
the engines share inputs, share derivations, or cover overlapping
verification targets. Pattern surfaced in: this wave (L2 "each link
by an independent compute engine"); previously in wave 1 §2.4
($S_5,\ldots,S_8$ via two methods that are the same identity);
previously in Vol III AP-CY49 ("agent tautological tests").

**Healing.** Replace "independent" with "network-redundant" or
"cross-validated"; report per-engine, per-target test allocation;
adopt the @independent_verification protocol (CLAUDE.md HZ3-11) for
each verification engine.

**Cache slot:** Already covered by AP-CY49, AP10. Add a Vol I-specific
cross-reference here.

### CACHE ENTRY (proposed) — "Letter inflates 4 to 7 (or N to N+k)"

**Pattern.** A cover letter or survey count inflates the underlying
distinct-object count by re-grouping equivalent presentations into
separate items. Pattern surfaced in: this wave (L2 seven-faces, with
genuine count ≈ 4); previously in wave 6 (twelve vs. fourteen Koszul
characterisations: 12 distinct, 14 in standalone title); previously
in wave 6 (programme summary status overclaim cascade).

**Healing.** State the count of *distinct objects* prominently;
state the count of *presentations* (= distinct objects × number of
languages) separately. The two counts differ; presenting the latter
as the former is the inflation.

**Cache slot:** appendices/first_principles_cache.md, new entry under
**inflation** type. Cross-reference: AP155 (overclaim novelty),
wave 6 §2.1 (twelve vs. fourteen).

---

## Section 9 — First-principles protocol summary (per AP-CY61)

Each wrong-pattern claim contains the seed of a correct theorem. The
extracted seeds from this wave:

1. **L4 "alternative finite proof of class M"** → ghost: the cubic
   shadow $S_3 = 2$ on the Virasoro primary line is the **structural
   witness** that the Virasoro lies on the homogeneous section of the
   algebraicity fibration ($\partial_\alpha$ direction in
   $(\kappa, \alpha, S_4)$ space). Class M is via $\Delta$, not $S_3$;
   $S_3 = 2$ is a different result with its own significance.

2. **L2 "seven faces, seven independent engines"** → ghost: the
   seven-face identification is a **Sasaki diagram** with 4 new edges
   and 3 classical edges; the verification network is connected with
   per-link redundancy ≥ 1, not a 1-1 face-to-engine matching.

3. **L1 "polynomial growth governed by the Weyl group"** → ghost:
   Garland–Lepowsky **concentration** survives in the chiral setting
   for all simple $\mathfrak g$; the **dimension formula** is
   Weyl-group-controlled only for $\mathfrak{sl}_2$ (where the
   Orlik–Solomon factor degenerates).

4. **L3 "first modular Koszul duality"** → no ghost; the claim is
   correct with the "modular" qualifier prominent.

5. **L4 closed-form $R$-matrix as Computation** → ghost: this is the
   **universal $R$-matrix of the $E_1$-chiral bialgebra structure on
   $B^{\rm ord}(\mathrm{Vir}_c)$ restricted to the primary lane**;
   stating it this way connects to AP-CY23 and the Vol II E_1-bialgebra
   programme.

---

## Section 10 — Final verdict

| Letter | Submit-as-is? | Required edits | Strongest defensible headline |
|---|---|---|---|
| L1 (Garland–Lepowsky → JoA) | After P1, P7, P8 | 3 high/medium | "Chiral Garland–Lepowsky concentration for all simple $\mathfrak g$, with explicit $\dim H^n(\widehat{\mathfrak{sl}}_2) = 2n{+}1$ formula" |
| L2 (Seven-faces → Duke) | After P2, P3, P9 | 3 high/medium | "Sasaki diagram of identifications: 4 new bilateral arrows linking the bar-cobar twisting morphism to the line-operator $R$-matrix, the PVA $r$-matrix, the GZ commuting differentials, and the Gaudin generator" |
| L3 (Shadow towers → Inv. Math.) | After P6, P11 | 1 medium | "First *modular* Koszul duality theory on $\overline{\mathcal M}_{g,n}$ with explicit Riccati spectral curve and four-class partition" |
| L4 (Virasoro → LMP) | After P4, P5, P10, P12 | 4 medium/high | "Closed-form universal $E_1$-bialgebra $R$-matrix for Virasoro on the primary lane: $R(z) = z^{2h}\exp(-c/(4z^2))$" |

**No letter requires a withdrawal.** All four are submittable after the
edits above. The strongest letter at the status level is L3
(shadow towers); the weakest is L2 (seven faces) due to the
seven-vs-four inflation.

**Editorial.tex** is **not a cover letter**, and is not in scope for
substantive cover-letter audit. It is a documentclass wrapper that
loads the editorial-constitution chapter from `chapters/connections/`.
That chapter would be a separate audit target.

---

*End of wave 10 report.*
