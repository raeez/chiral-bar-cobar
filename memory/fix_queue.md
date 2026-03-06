# FIX QUEUE — 12 Remaining Mechanical Items
# Verified against source files March 6, 2026
# Total estimated time: 2.5 hours (or 30 min for quick-wins only)

## QUICK WINS (30 min total — do these as session warmup)

### F1. H5: Missing cross-ref for Heisenberg Koszulness [5 min]
- File: chapters/theory/deformation_theory.tex:1335
- Issue: "The Heisenberg algebra B is Koszul" — no citation to the theorem that proves this
- Fix: Add "(\text{Theorem~\ref{thm:km-chiral-koszul}})" or equivalent ref
- Verify: grep for thm:km-chiral-koszul to confirm label exists

### F2. H19: beta-gamma differential table convention [10 min]
- File: chapters/examples/beta_gamma.tex:738-756
- Issue: Table lists D_{12} nonzero for [gamma|beta|beta|beta] but D_{13} should also be nonzero
- Fix: Add footnote clarifying OPE directionality convention (or fix table entries)
- Verify: check beta(z)gamma(w) vs gamma(z)beta(w) OPE signs

### F3. H28: G_tau partial symbol overload [10 min]
- File: chapters/examples/heisenberg_eisenstein.tex:101,641
- Status: PARTIAL — G_tau vs tilde-G_tau distinguished but base symbol shared
- Fix: Add sentence at line 641: "We write $\widetilde{G}_\tau = -\partial_z G_\tau$ to distinguish..."
- Verify: grep G_tau across file, ensure all uses are unambiguous

### F4. LurieHA missing citation [5 min]
- File: bibliography/references.tex
- Issue: 2 undefined citation warnings for LurieHA (pages 91-92)
- Fix: Add \bibitem{LurieHA} J. Lurie, \emph{Higher Algebra}, 2017.
- Verify: make fast, check 0 undefined citations

### F5. thm:modular-anomaly label mismatch [5 min]
- File: chapters/examples/free_fields.tex:3302
- Issue: \begin{theorem} with \ClaimStatusConjectured — should be \begin{conjecture}
- Fix: Change theorem -> conjecture, label thm: -> conj:
- Verify: grep for ref{thm:modular-anomaly}, update any cross-refs

### F6. Two TODO comments in tex [5 min]
- chapters/connections/genus_complete.tex:417 — %TODO: add Eynard/CEO citation
- chapters/examples/heisenberg_eisenstein.tex:416 — %TODO: add Klingen citation
- Fix: Add bibentries or remove TODOs with scope remarks

### F7. CLAUDE.md census sync [5 min]
- Fix: Update census to PH 695, PE 333, CJ 113, HE 19 = 1160
- Also fix: bibliography count 289 -> 260, pages, proof sketch table (add deformation_theory:957)

---

## MODERATE FIXES (2 hours total — do after quick wins OR skip for depth work)

### F8. H9: Yangian theorem proves wrong thing [30 min]
- File: chapters/theory/koszul_pair_structure.tex:1015-1035
- Issue: thm:chiral-yangian claims Yangian-KL relationship but proof only verifies KM axioms
- Fix: Either (a) downgrade claim to what's proved + cite Feigin-Frenkel for KL, or
       (b) restructure as two results: KM axioms (PH) + KL identification (PE with cite)
- Verify: check claim status tag matches actual content

### F9. H12: I-adic completion convergence [20 min]
- File: chapters/theory/chiral_koszul_pairs.tex:919-950
- Issue: No Mittag-Leffler or convergence argument for I-adic completion
- Fix: Add "The I-adic filtration stabilizes in each internal degree by the
  polynomial growth hypothesis (specifically, each graded component of
  B-bar^n is finite-dimensional), ensuring the Mittag-Leffler condition."
- Verify: check that polynomial growth is indeed a hypothesis of the theorem

### F10. H21: Kontsevich propagator identification gap [30 min]
- File: chapters/connections/kontsevich_integral.tex:390-408
- Issue: PH claim but algebraic-to-analytic propagator identification not proved
- Fix: Either (a) downgrade item (ii) to PE with specific citation, or
       (b) add proof identifying bar propagator Res_{z1=z2}[omega/(z1-z2)] with
       Kontsevich propagator darg(z1-z2)/2pi on the real locus
- Verify: check claim status consistency

### F11. H26: Existence criterion sufficiency [30 min]
- File: chapters/theory/introduction.tex:1132-1157
- Issue: "if and only if" but sufficiency direction incomplete
- Fix: Either (a) complete sufficiency proof (construct Koszul dual from conditions
  1-4 via bar-cobar + completion + Verdier), or (b) weaken to "if" with remark
  noting sufficiency is expected but requires [specific gap]
- Verify: check what the proof actually establishes

### F12. M4: Consolidate Koszul pair definitions [30 min]
- Files: algebraic_foundations.tex:91,351,386 + chiral_koszul_pairs.tex:63
- Issue: 4 definitions of "Koszul pair" with risk of drift
- Fix: Keep def:chiral-koszul-pair in chiral_koszul_pairs.tex as canonical.
  In algebraic_foundations, change to "cf. Definition~\ref{def:chiral-koszul-pair}"
  for chiral versions, keep only the classical definition at line 91.
- Verify: grep 'begin{definition}.*[Kk]oszul pair' to confirm consolidation
