# Wave-7 Attack-and-Heal: Theorem A^{∞,2} clause (iii) R-twisted Σ_n descent — unitarity hypothesis propagation

**Date**: 2026-04-18
**Target**: Vol I `chapters/theory/theorem_A_infinity_2.tex:1011-1136` `lem:R-twisted-descent` + all clause-(iii) consumers.
**Author (adversarial channel)**: Etingof/Polyakov/Kazhdan/Gelfand/Nekrasov/Kapranov/Bezrukavnikov/Costello/Gaiotto/Witten.
**Predecessor**: Wave-1 2026-04-17 attack (F8 + OF3) and Wave-1 second-pass (F11); AP298 canonical instance.

---

## 1. Inscription verification

`lem:R-twisted-descent` at `theorem_A_infinity_2.tex:1011-1041` is inscribed post-Wave-1 with:

- Hypothesis **(R1)** classical Yang–Baxter, label `R1`.
- Hypothesis **(R2)** unitarity `R(z) R^{op}(-z) = id`, label `R2`, where `R^{op}(w) = τ · R(w) · τ`.
- Statement head reads `\begin{lemma}[R-matrix-twisted Σ_n-descent, unitary R]`.
- Proof Step 1 (lines 1053-1062) explicitly invokes (R2): "Passage from the pure braid representation to a representation of the full symmetric group Σ_n is *not* a formal consequence of (R1) alone: it requires the relation s_i²=1 at each elementary transposition, which at the monodromy level reads R(z)R^{op}(-z)=id. This is precisely Hypothesis (R2) (unitarity)."
- Scope remark `rem:R-descent-unitarity-scope` at lines 1111-1136 is present.

**Verdict**: Wave-1 OF3 is inscribed at the lemma. ✓

---

## 2. Family-coverage audit

Verified against primary sources and the inscribed scope remark. Table columns: (R1) YBE; (R2) unitarity; descent conclusion.

| $R$-matrix | (R1) YBE | (R2) $R(z)R^{op}(-z)=\id$ | Conclusion |
|------------|----------|---------------------------|------------|
| Rational Yangian $Y_\hbar(\mathfrak{g})$, simple $\mathfrak{g}$ | ✓ Drinfeld 1985 | ✓ direct on evaluation module (Chari–Pressley 1994 §12.3) | lemma applies unconditionally |
| Trigonometric $U_q(\widehat{\mathfrak{g}})$, generic $q$ | ✓ | ✓ at generic $q$; fails at roots of unity together with Koszulness | lemma applies on Koszul locus |
| Heisenberg, free fermions, lattice VOAs at generic rank | (R1) vacuous ($R=\tau$) | ✓ vacuous ($\tau^2=\id$) | Step 4 degeneration; descent = ordinary $\Sigma_n$-coinv |
| **Belavin-Pauli Z_N** ($r(z) = \sum_a w_a(z)\,\sigma_a\otimes\sigma_a/2$ on $\mathfrak{sl}_N$) | ✓ (Belavin 1981; Faddeev–Takhtajan; CYBE verified numerically) | ✓ $w_a(-z)=-w_a(z)$ forces $r(z)+r^{op}(-z)=0$; lifting to unitary $R$ at quantum level uses Pauli symmetry $\tau(\sigma_a\otimes\sigma_a)\tau = \sigma_a\otimes\sigma_a$ so $R^{op}=R$ and $R(z)R(-z)=\id$ | lemma applies |
| **Belavin-Weierstrass convention** ($\zeta$-based, quasi-periodic correction) | ✗ (FM30: Weierstrass $\zeta$-based $r$-matrix breaks CYBE) | N/A — (R1) already fails | OUTSIDE SCOPE; moot |
| **Felder dynamical** $R(z,\lambda,\tau)$ | dynamical YBE (Felder 1994, Theorem 2.1) — ordinary (R1) fails; requires dynamical (R1) | dynamical unitarity $R(z,\lambda)R^{op}(-z,\lambda)=\id$ holds *with* $\lambda$-shift bookkeeping (Felder 1994; Felder–Varchenko 1996) | OUTSIDE SCOPE of present (R1)+(R2) — lemma is for non-dynamical $R$; dynamical descent requires separate formulation |
| Roots of unity $U_q(\widehat{\mathfrak{g}})$ | ✓ | ✗ fails concurrently with Koszulness | OUTSIDE Koszul locus |

**Finding**: Scope remark `rem:R-descent-unitarity-scope` treats elliptic Belavin/Felder as "convention-dependent", which is correct but under-specified. The table above refines:
- Belavin-Pauli: IN scope (unitary).
- Belavin-Weierstrass: OUT on (R1) already (FM30).
- Felder dynamical: OUT on (R1)-non-dynamical; separate formulation required.

The audit does not rewrite the scope remark — the "convention-dependent" phrasing subsumes both Belavin-Pauli in-scope and Belavin-Weierstrass out-on-CYBE, plus Felder out-on-dynamical. A reader following the Pauli convention per FM30 stays in scope.

---

## 3. Consumer enumeration (AP5 propagation)

Live-tex `\ref{lem:R-twisted-descent}` consumers, Vol I only (Vol II/III return no hits):

| # | Site | Old state | Post-Wave-7 |
|---|------|-----------|-------------|
| 1 | `theorem_A_infinity_2.tex:782-794` clause (iii) of `thm:A-infinity-2` | omits (R2) | **HEALED**: clause title now reads "Ordered-to-symmetric descent (unitary R)"; explicit YBE + unitarity + family scope inline |
| 2 | `theorem_A_infinity_2.tex:467-481` `cor:eight-cor-R-descent` | omits (R1)+(R2) | **HEALED**: title reads "unitary R"; both hypotheses inline with family scope |
| 3 | `theorem_A_infinity_2.tex:1209` D7 Spoke 7 SC-formality via A2-iii | silent inheritance | **HEALED**: inline note that class-$\mathsf{G}$ has $R(z)=\tau$, so (R2) is vacuous on that stratum |
| 4 | `e1_modular_koszul.tex:54` av-decomposition remark | bare citation | **HEALED**: inline YBE + unitarity qualifier |
| 5 | `e1_modular_koszul.tex:2752` Step 2 five-theorems bridge | bare citation | **HEALED**: inline YBE + unitarity qualifier |
| 6 | `ordered_associative_chiral_kd.tex:86` scope remark | bare citation | **HEALED**: inline YBE + unitarity qualifier |
| 7 | `standalone/N3_e1_primacy.tex:1063-1065` ordered-Koszul def | bare verb citation | **HEALED**: inline qualifier |
| 8 | `standalone/five_theorems_modular_koszul.tex:2835-2839` A^{E_1} upgrade | bare verb citation | **HEALED**: inline qualifier |
| 9 | `standalone/e1_primacy_ordered_bar.tex:1711-1727` sibling `lem:R-twisted-descent-sa` | used pure braid PBr_n, Σ_n extension implicit | **HEALED**: statement now requires (R1)+(R2); Step explaining s_i²=id via unitarity added; title reads "unitary R"; scope remark merged into body |

`standalone/theorem_index.tex:2370` index entry kept as short descriptor (not a load-bearing prose consumer); optional future edit to add "(unitary R)".

---

## 4. Theorem A clause (iii) vs `thm:theorem-A-E1` (E_1-ordered variant)

**Finding**: CLAUDE.md theorem-status row advertises `thm:theorem-A-E1` ("E_1-ordered variant proved via pure braid Orlik-Solomon Koszulity") but grep of Vol I returns **zero** `\label{thm:theorem-A-E1}`. The E_1 variant is currently advertised-only (AP241 / AP255 phantom candidate). Residual open:

- **OF8 (new)**: either inscribe `thm:theorem-A-E1` locally as a named theorem with its pure-braid Shelton-Yuzvinsky proof, or rename CLAUDE.md row to reference `standalone/e1_primacy_ordered_bar.tex` Theorem $A^{E_1}$ as `\ClaimStatusProvedElsewhere` with explicit attribution.
- For Wave-7 scope: no edit; flag for future wave.

The *ordered* E_1-variant (pure braid P_n → Orlik–Solomon → Σ_n) has the *same* unitarity requirement for the PB_n → Σ_n descent step; the Shelton–Yuzvinsky Koszulity is at pure braid level and is independent. Thus any future inscription must carry the same (R2) hypothesis or restrict to class-G ($R=\tau$, where the Σ_n-extension is trivial).

---

## 5. Heals applied (atomic, no commits per brief)

Files touched (8 edits across 6 files):

- `chapters/theory/theorem_A_infinity_2.tex` — clause (iii) header + body; `cor:eight-cor-R-descent` header + body; D7 Spoke 7 remark.
- `chapters/theory/e1_modular_koszul.tex` — two sites (lines 52-54, 2750-2756).
- `chapters/theory/ordered_associative_chiral_kd.tex` — line 85-88 scope remark.
- `standalone/N3_e1_primacy.tex` — line 1063-1065.
- `standalone/five_theorems_modular_koszul.tex` — line 2835-2839.
- `standalone/e1_primacy_ordered_bar.tex` — sibling lemma `lem:R-twisted-descent-sa` rewritten with (R1)+(R2).

---

## 6. Residual open

- **OF8 (above)**: `thm:theorem-A-E1` phantom inscription (AP241 / AP255 candidate). Recommended healing: inscribe in `theorem_A_infinity_2.tex` §ainf2-R-descent as `\begin{theorem}[Theorem A^{E_1}, ordered E_1-variant via pure-braid Orlik–Solomon]` citing Shelton–Yuzvinsky 1997, or retarget CLAUDE.md to the standalone.
- **OF9 (new, lower priority)**: `rem:R-descent-unitarity-scope` treats elliptic cases as a single "convention-dependent" class. A future refinement could inscribe the Belavin-Pauli vs Belavin-Weierstrass vs Felder-dynamical trichotomy of §2 above as a sub-remark; for now the coarse scope remark is accurate and the table above serves as the working-notes record.
- **OF10**: `standalone/theorem_index.tex:2370` index descriptor is terse ("B^ord relates to B^Sigma at properad level"); optional future edit to add "(unitary R)".

No CLAUDE.md status-table update is required: the row for Theorem A already carries the "fixed-curve" scope and the lemma-level unitarity qualifier is inside `rem:R-descent-unitarity-scope` (Wave-1 heal H11); Wave-7 propagates the qualifier to the eight consumer sites above.

---

## 7. AP cross-references

- AP7: Before universal quantifier, verify proof has no implicit type/genus/level restriction. Wave-7 removes the implicit restriction from consumers.
- AP271: Reverse drift — CLAUDE.md vs manuscript. Pre-Wave-7: consumers were *silently* unconditional while lemma was scoped; this was a reverse-drift at the consumer level. Post-Wave-7: consumers now explicitly carry the (R1)+(R2) qualifier.
- AP297: Lemma header mentions a hypothesis the consumer does not inherit. Pre-Wave-7: all seven external consumers. Post-Wave-7: all consumers propagate.
- AP298: "Pure braid → Σ_n extension via YBE alone" fallacy at one higher codim. Wave-1 caught it at the lemma; Wave-7 caught it at the sibling `lem:R-twisted-descent-sa` in `standalone/e1_primacy_ordered_bar.tex` where the extension step was previously implicit (quotient by PBr_n rather than Σ_n).
- FM30: Belavin Weierstrass-$\zeta$ breaks CYBE — relevant to §2 table row "Belavin-Weierstrass OUT".

---

## 8. Beilinson verdict

The smaller true theorem: "$R$-twisted $\Sigma_n$-descent holds for $E_1$-chiral algebras whose classical $R$-matrix satisfies YBE **and** unitarity." This covers the programme's concrete witnesses (rational Yangians, generic-$q$ trigonometric $U_q(\widehat{\fg})$, trivial-$R$ locally-constant families, Belavin-Pauli elliptic). The larger false theorem — "descent from YBE alone" — is retracted at every site. The programme's climax clause (iii) now carries its hypothesis explicitly at the theorem body, at the corollary body, at the SC-formality consumer, and across all live-tex cross-references.
