# Deep structural critique and upgrade roadmap
## Chiral Duality in the Presence of Quantum Corrections — latest iteration

This report is not a referee report in the ordinary sense. It is a structural attack on the monograph as a mathematical object, aimed at turning the current manuscript into the strongest possible theorematic version of itself.

The current state is substantially stronger than earlier iterations. The homological core is now largely sound. The main remaining work is not to repair a collapsed main theorem but to harmonize the whole manuscript around one semantic level, one status discipline, and one research programme architecture.

## Executive diagnosis

1. The core theorem chain A/B/C/D is now much stronger.
   - Complementarity is no longer driven by an invalid dimension count but by a Verdier involution and Lagrangian splitting.
   - Bar–cobar inversion is scoped to the Koszul locus and coderived persistence off it.
   - The scalar modular package is separated from the full Maurer–Cartan package.
   - The KL target category is corrected to the semisimplified tilting quotient.

2. The manuscript’s main remaining live mathematical weakness is the periodicity package.
   - The structural “periodicity profile” reformulation is a real improvement.
   - But the chapter still contains overproved “minimal model / WZW modular periodicity” theorems whose present proofs rely on an invalid coefficient-periodicity mechanism.
   - The transport theorem for periodicity under duality still packages conditional statements as if fully proved.

3. The main structural weakness is backward propagation.
   - Chapter 34 now gives the right status ledger and the right homotopy-level architecture.
   - Earlier chapters still often speak in a pre-34 dialect, especially Chapter 1 and some examples / tables.

4. The correct next revision is not a local patch pass. It is a doctrinal rewrite pass.
   - Enforce H/M/S semantics everywhere.
   - Enforce scalar-vs-full package discipline everywhere.
   - Enforce “proved / conditional / conjectural / programme” status tags everywhere.
   - Enforce one notation for fiberwise curved differential vs total strict differential.

## The single best editorial principle

Every major statement should be written in three synchronized forms.

- H-level: the homotopy-native statement in the stable / coderived / factorization / formal-moduli language.
- M-level: the chosen dg or explicit bar-complex model.
- S-level: the cohomological, numerical, generating-function, or table-level shadow.

Then every theorem and conjecture should declare which of the three levels it lives on.

This one change would clean up a large fraction of the current drift.

---

## Chapter-by-chapter critique

### Chapter 1 (pp. 47–76): The Heisenberg algebra

### What is strong
- The chapter remains the best pedagogical atom in the book.
- It exhibits the entire architecture in the smallest example: bar differential, curvature, genus tower, complementarity, characteristic package.

### What is wrong
- It still overstates the status of the full modular characteristic package in the Heisenberg case.
- The current definition presents the package as if the universal Maurer–Cartan class, ambient deformation complex, and full package were already fully established objects here, whereas later chapters distinguish the proved scalar package from the conjectural full non-scalar completion.
- Because this is the first chapter, the drift is damaging: it teaches the reader the wrong status discipline at the start.

### Correct upgrade
- Rewrite the chapter to present two nested packages:
  1. the scalar package for Heisenberg: kappa, genus tower, complementarity shadow;
  2. the full package as the conjectural natural completion, previewed but not yet claimed.
- Add a small boxed note: “In the Heisenberg case the scalar package already determines everything visible in this chapter; the full non-scalar package is introduced as the object the later theory wants to construct, not as a theorem of Chapter 1.”

### How to upgrade the local conjectural content
- Prove the Heisenberg instance of the full package if possible, separately, rather than importing the general conjectural vocabulary. The Heisenberg case is the one family where explicit cyclic deformation models may be tractable enough to actually construct Theta_H.

---

### Chapter 2 (pp. 77–88): Introduction

### What is strong
- This chapter is now much closer to the manuscript’s true final form.
- It cleanly separates Theorems A/B/C/D, introduces H/M/S semantics, distinguishes curved fiberwise differential from strict total differential, and states that the scalar package is proved while the full package is conjectural.
- It also compresses the open landscape into five master conjectures.

### What is wrong
- The chapter still occasionally writes as if the modular characteristic package CA were already fully operational, before later qualifying that Theta_A is conjectural.
- The introduction also pushes too much conceptual freight through Chapter 1’s Heisenberg packaging, which is not yet synchronized with the new status discipline.

### Correct upgrade
- Tighten the introduction by explicitly saying “full package” only when you mean the formalized conjectural package, and “scalar/spectral package” when you mean the proved content.
- Add one table near §2.3:
  - Layer / object / status / first theorem / chapter of full treatment.

### How to upgrade conjectural statements to theorematic roadmap
- Keep the five master conjectures, but add for each one:
  - precise missing input,
  - nearest existing theorem that will generalize,
  - canonical test family.

---

### Chapter 3 (pp. 89–92): Algebraic foundations and bar constructions

### What is strong
- This chapter supplies the algebraic prehistory and makes the manuscript legible to algebraists.

### What is wrong
- The current project still has too many definitions of “Koszul pair” across the manuscript. The source tree confirms that multiple versions remain alive.
- This chapter should not silently reintroduce chiral or modular versions of notions that later chapters make more precise.

### Correct upgrade
- Keep only the purely classical definition here.
- Add forward references: classical Koszul pair, chiral Koszul pair, modular Koszul object.
- State explicitly that every later generalization is a refinement or enhancement of the chapter-3 algebraic prototype.

### How to upgrade
- The upgrade is editorial and conceptual, not theorematic: eliminate definitional drift so later proofs only need to cite one canonical definition.

---

### Chapter 4 (pp. 93–104): Operadic foundations and bar constructions

### What is strong
- This is where the manuscript correctly anchors itself in Ayala–Francis / factorization / Ran-space language.
- The chapter’s universal viewpoint is the right ambient formulation for the whole project.

### What is wrong
- The chapter is still doing too much explicit verification at the same level as the main theorems.
- Several later proofs depend on this chapter only through a small number of universal lemmas; the rest is foundational scaffolding that should be compressed.

### Correct upgrade
- Extract the true load-bearing results into an early “operadic core” subsection and move the lengthy verification tables to an appendix or an end-of-chapter technical supplement.
- Make the main lesson explicit: the concrete configuration-space bar construction is a model for a factorization-theoretic bar object.

### How to upgrade
- Promote the universal adjunction and Verdier-functoriality statements to H-level theorems; treat the explicit operadic checks as M-level model verification.

---

### Chapter 5 (pp. 105–170): Configuration spaces

### What is strong
- This chapter is the geometric engine room of the manuscript.
- The FM compactification, logarithmic forms, Ran-space interface, and chain-level constructions are all essential to the identity of the work.

### What is wrong
- The chapter is overgrown. It currently mixes:
  1. FM geometry,
  2. punctured/logarithmic variants,
  3. elliptic/theta-function preliminaries,
  4. higher-genus / hyperbolic / Teichmüller digressions,
  5. explicit coordinates,
  6. Ran-space sheaf theory.
- The result is mathematically rich but strategically diffuse.

### Correct upgrade
- Split the chapter internally into three theorematic layers:
  - 5A. FM geometry actually used by the bar differential and residues.
  - 5B. Ran-space and factorization interface.
  - 5C. frontier geometry (elliptic/theta/hyperbolic/log variants).
- Move 5C material into a “frontier geometry” chapter or appendix unless it is directly used in a proof.

### How to upgrade conjectural/frontier parts
- The logarithmic FM and degeneration material should be turned into a theorematic bridge to punctured-curve bar complexes. That is a natural future theorem family and a real generalization target, not just context.

---

### Chapter 6 (pp. 171–308): Bar and cobar constructions

### What is strong
- This is one of the true core chapters.
- The construction is explicit, computable, and distinctive.
- The later monograph depends on it at many points.

### What is wrong
- The chapter is still too chain-model heavy without enough up-front homotopy compression.
- Many local sign and residue verifications are repeated at the same logical level as major structural theorems.
- The distinction between explicit model, universal construction, and physical interpretation is not always cleanly tiered.

### Correct upgrade
- Reframe the chapter around three universal results:
  1. existence of the bar object,
  2. its coalgebraic/factorization structure,
  3. Verdier passage to cobar.
- Push long degree-by-degree verifications and physical interpretations into subsections clearly labeled “model-level realization.”

### How to upgrade the conjectures here
- The BRST / anomaly-cancellation conjectures should be restated later in the physics part as extensions of the proved bar object, not as dangling conjectures in the construction chapter.

---

### Chapter 7 (pp. 309–320): Non-abelian Poincaré duality and Koszul dual cooperads

### What is strong
- This chapter is part of the repaired core.
- It supports the modern interpretation of Theorem A.

### What is wrong
- Its results are stronger conceptually than their later deployment. Later chapters often cite consequences without reminding the reader that these are H-level statements about factorization/cosheaf duality, not merely bar-complex accidents.

### Correct upgrade
- Add a “how this chapter is used later” section listing exactly where it feeds Theorems A, C, and the module theory.
- This will prevent later chapters from re-proving or re-motivating what is already accomplished here.

---

### Chapter 8 (pp. 321–446): Higher genus extension and quantum corrections

### What is strong
- This is now the strongest single chapter in the manuscript.
- It contains the repaired complementarity theorem, the fiberwise-vs-total differential distinction, the modular Koszul object definition, the scalar/full package split, and the correct entry point for the five master conjectures.

### What is wrong
- The chapter still contains conditional interacting-family claims that are too compressed in their proof language.
- The PBW-degeneration obstruction is now correctly isolated, but the text still tends to glide over the gap by saying that the associated graded argument “therefore extends” at generic parameters. That should be stated more sharply as: “here is the exact missing theorem.”
- The chapter also now carries a large fraction of the entire book’s conceptual burden; this is efficient mathematically but makes it easy for earlier chapters to fall out of sync.

### Correct upgrade
- Promote §8.17 to the formal hinge of the entire book. Add a visible chapter-opening note: “This chapter supersedes earlier heuristic formulations of modular characteristic data.”
- Split the interacting-family proposition into:
  1. a proved conditional theorem: modular Koszulity follows from higher-genus PBW degeneration;
  2. a conjecture asserting that degeneration.

### How to turn the conjectures into theorems
- Conjecture 8.17.14 / 34.9.1 should be the first serious theorem target in any sequel or major revision. The route is clear:
  - identify a genus-compatible filtered model of the interacting bar complex,
  - prove a deformation-invariance theorem for the PBW spectral sequence under central curvature,
  - control extension problems at E2.
- This is the right “entry theorem” for making the interacting families unconditional.

---

### Chapter 9 (pp. 447–492): Chiral Koszul duality

### What is strong
- This chapter now lives inside a clearer global architecture than before.

### What is wrong
- The proof chain should be made even more modular. Several later chapters cite it in ways that suggest “Chiral Koszul duality” is one undifferentiated block rather than a theorem family with precise hypotheses.

### Correct upgrade
- Add an end-of-chapter dependency digest:
  - A0 twisting morphisms,
  - A1 concentration,
  - A2 Verdier-geometric duality,
  - B inversion on the Koszul locus.

---

### Chapter 10 (pp. 493–520): Chiral Koszul pairs

### What is strong
- The chapter’s role in the current manuscript is clearer than before.

### What is wrong
- It still participates in the definitional drift problem. The source tree indicates multiple “Koszul pair” definitions still survive across chapters.

### Correct upgrade
- Make this chapter’s definition the unique canonical chiral version.
- Add a “classical / chiral / modular” comparison table with exact logical implications.

---

### Chapter 11 (pp. 521–554): Chiral Hochschild cohomology and Koszul duality

### What is strong
- The chapter is conceptually important because it should connect the bar story to cyclic deformation and index theory.
- The manuscript’s current introduction and Chapter 34 already elevate this role.

### What is wrong
- This is still the weakest theorematic chapter.
- The periodicity package is better conceptualized than before, but its two flagship “proved here” modular periodicity theorems remain overclaimed.
- The proof mechanism goes through T-matrix periodicity and theta/eta-series reasoning in a way that does not actually establish periodicity of bar-cohomology dimensions.
- The chapter now correctly says that general rational modular periodicity is conjectural, but the minimal-model / WZW special cases are still not established by the printed argument.
- The transport theorem under duality still bundles proved and conditional statements together.

### Correct upgrade
- Rewrite the chapter around the periodicity profile Pi_A rather than a scalar period.
- Split all current periodicity statements into:
  1. structural profile statements (proved),
  2. modular formulas (conditional),
  3. quantum periodicity (proved),
  4. geometric weak bound (proved),
  5. sharp geometric / reflected modular periodicity (conjectural).

### How to turn conjectures into theorems
- For modular periodicity, the right theorem is probably not “Fourier coefficients are periodic.” The correct strategy is to construct an actual periodic autoequivalence or finite-order action on the relevant homotopy object.
- For the minimal-model/WZW special cases, a realistic route is:
  - move from character periodicity to a theorem about periodicity of fusion / filtration data at the chain level,
  - then prove compatibility of the bar differential with the periodic operator.
- Until that is proved, downgrade the minimal-model and WZW theorems.

---

### Chapter 12 (pp. 555–624): Chiral modules and geometric resolutions

### What is strong
- This chapter is likely one of the least controversial theoretically.
- The module perspective is crucial for later DK / KL / boundary-category interpretations.

### What is wrong
- The module story is stronger than many of the later physics-facing applications, but the manuscript does not always mark the boundary.

### Correct upgrade
- Add a final section stating exactly which module-theoretic equivalences are fully proved and which later statements only use them heuristically.

---

### Chapter 13 (pp. 625–638): Quantum corrections to Arnold relations

### What is strong
- This is an elegant local chapter and an important bridge from geometry to deformation.

### What is wrong
- Its conceptual significance is larger than the chapter’s current positioning. It should be linked more explicitly to the universal Maurer–Cartan story and to the cyclic deformation object.

### Correct upgrade
- Add a short final section: “From corrected Arnold relations to the cyclic deformation complex.”

---

### Chapter 14 (pp. 639–662): HH

### What is strong
- This chapter is part of the deformation-theoretic bridge.

### What is wrong
- The title is too compressed relative to its mathematical role.
- The chapter should more clearly explain whether it is about HH^*, HH_*, cyclic structures, or all three at once. Earlier versions had confusion here; the current text is better but still terse.

### Correct upgrade
- Rename or subtitle the chapter to make the homological direction explicit.
- Add a one-page conventions block at the start.

---

### Chapter 15 (pp. 653–662): E_n Koszul duality and higher-dimensional bar complexes

### What is strong
- This is a natural extension chapter and is now better placed as a frontier/prospective theorem family.

### What is wrong
- It is still too close to the main theorematic spine in tone. The E_n extension is not yet on the same status level as the curve case.

### Correct upgrade
- Clearly mark this chapter as “proved low-dimensional scaffolding + programme-level extension.”
- Move any statements that depend on higher-dimensional AQFT or Chern–Simons input into a visibly conjectural stratum.

### How to turn the conjecture into theorems
- The route runs through an E_n version of the configuration-space bar construction plus explicit comparison with known factorization homology theorems. This is a sequel project, not a patch.

---

### Chapter 16 (pp. 663–678): Derived structures and geometric Langlands correspondence

### What is strong
- The chapter identifies the right direction: critical level, derived stacks, and geometric Langlands are not ornamental; they are natural endpoints of the bar picture.

### What is wrong
- The chapter’s theorematic center is still too speculative relative to the current proved machinery.
- It should be much more explicit about which claims are proved by reduction to known literature and which are visionary extrapolations.

### Correct upgrade
- Split the chapter into “proved derived identifications” and “Langlands programme.”
- In the latter part, every conjecture should state the precise missing derived-algebraic-geometric input.

---

### Chapter 17 (pp. 679–696): The lattice construction

### What is strong
- Important examples and bridge to free-field / VOA constructions.

### What is wrong
- The chapter’s place in the global architecture is underexplained.

### Correct upgrade
- Add an explicit paragraph: lattice constructions are a source of modular Koszul examples and of stress tests for the scalar/spectral package distinction.

---

### Chapter 18 (pp. 697–756): Examples

### What is strong
- This chapter assembles the example zoo and is important for the empirical credibility of the theory.

### What is wrong
- It still carries programme-level claims too close to proved examples.
- The theorematic and heuristic parts need stronger typography and status separation.

### Correct upgrade
- Split each example section into:
  - proved computations,
  - conditional consequences,
  - horizon conjectures.
- Add a legend at the beginning of the chapter.

---

### Chapter 19 (pp. 757–790): Complete example: the beta-gamma system

### What is strong
- Excellent test case for the theory.

### What is wrong
- This chapter should carry more of the burden for the spectral/discriminant story than it currently does.

### Correct upgrade
- Make beta-gamma the canonical worked example for the spectral package, not just another example chapter.
- Add a subsection explicitly connecting its discriminant to the shared spectral sheet story.

---

### Chapter 20 (pp. 791–834): Explicit Kac–Moody Koszul duals

### What is strong
- Core representation-theoretic material.
- The KL category correction is a major improvement.

### What is wrong
- The admissible-level / KL / coderived story is still too bundled.
- Several logically distinct conjectures are packed together as “KL from bar-cobar.”

### Correct upgrade
- Split the programme into three theorem targets:
  1. periodic/CDG/N-complex structure at admissible level,
  2. identification of the corresponding stable/coderived category,
  3. braided KL comparison.
- Ensure every later reference uses the corrected target category C(U_q(g)) rather than the full Rep(U_q(g)).

### How to upgrade the conjectures into theorems
- First prove the admissible-level homological structure internally, without KL.
- Then compare categories.
- Only then attempt braided monoidality.

---

### Chapter 21 (pp. 835–916): W-algebra Koszul duals

### What is strong
- The chapter is ambitious and central for the non-free-field world.

### What is wrong
- It still sits on multiple unresolved fronts at once: interacting-family PBW degeneration, DS reduction, and infinite-generator horizons.
- As a result, the chapter sometimes reads as if its strongest conclusions were already theorematic.

### Correct upgrade
- Separate finite-type W_N results from W_infty / infinite-generator aspirations.
- Make every DS-invariance claim track whether it is about scalar package, discriminant, or full package.

### How to upgrade conjectures
- The road is:
  1. resolve higher-genus PBW degeneration for W_N,
  2. sharpen DS reduction at the spectral level,
  3. only then formulate a completed W_infty bar theory.

---

### Chapter 22 (pp. 917–938): Chiral deformation quantization

### What is strong
- This chapter sits naturally at the interface with Kontsevich/formality themes.

### What is wrong
- It is conceptually tied to the cyclic deformation complex, but the manuscript has not yet fully exploited that relationship.

### Correct upgrade
- Re-anchor the chapter explicitly in the Type I/IV conjecture templates from Chapter 34.
- Make the deformation-quantization conjectures visibly downstream of the cyclic L_infty construction.

---

### Chapter 23 (pp. 939–948): Deformation quantization examples

### What is strong
- Useful and concrete.

### What is wrong
- The chapter would be stronger as an appendix-like worked companion to Chapter 22 rather than as an independent theorematic block.

### Correct upgrade
- Shrink and integrate with Chapter 22 or explicitly present it as a laboratory chapter.

---

### Chapter 24 (pp. 949–972): Yangians and shifted Yangians

### What is strong
- This is one of the most successful frontier chapters.
- The evaluation-locus and chain-level derived Drinfeld–Kohno results now create a real proved bridge.

### What is wrong
- The full factorization-categorical theorem is still genuinely conjectural, and the rest of the book must keep that boundary visible.
- The current chapter itself is relatively honest; propagation elsewhere is the issue.

### Correct upgrade
- Add a boxed decomposition of the full DK problem:
  - chain-level theorem proved,
  - factorization-level evaluation locus proved,
  - extension to full category O open,
  - dependence on Yangian Koszulness and factorization-level Kazhdan equivalence.

### How to upgrade the conjectures
- The most realistic path is not to “prove full DK” all at once, but to prove Yangian Koszulness for larger classes and extend the evaluation-locus factorization comparison step by step.

---

### Chapter 25 (pp. 973–988): Toroidal and elliptic algebras

### What is strong
- The chapter identifies the correct successor geometry: Fay replacing Arnold.

### What is wrong
- The material is mathematically suggestive but not yet proportioned to the rest of the book.
- It should be framed as the beginning of a sequel theory, not as a near-finished extension.

### Correct upgrade
- Explicitly state that this chapter supplies prototypes and obstruction data for an elliptic/toroidal sequel.

### How to upgrade the conjectures
- First isolate the correct elliptic propagator identity and bar-nilpotence mechanism.
- Then build the toroidal bar object in a completed setting.

---

### Chapter 26 (pp. 989–1026): Explicit genus expansions

### What is strong
- This is where the scalar package becomes experimentally persuasive.
- The A-hat genus pattern is one of the manuscript’s most compelling emergent phenomena.

### What is wrong
- The chapter should more aggressively distinguish between “explicitly computed,” “fit by universal theorem,” and “suggestive but not yet theorematic.”

### Correct upgrade
- Add a three-column status legend to every summary table:
  - computed directly,
  - deduced from general theorem,
  - conjectural extrapolation.

### How to upgrade conjectures
- The index-theoretic conjectures should be bundled into a GRR-style theorem target, not pursued piecemeal example by example.

---

### Chapter 27 (pp. 1027–1100): Detailed computations

### What is strong
- This chapter gives computational weight to the claims.

### What is wrong
- The conjecture registry here is still noisy. In particular, the source contains a duplicated-label / doubled-status issue for the sl3 generating-function and discriminant conjectures.
- That kind of bookkeeping damage matters because this chapter is supposed to be the computational evidence repository.

### Correct upgrade
- Clean the conjecture labels immediately.
- Split the chapter into:
  - proved computations,
  - conjectural recurrences / generating functions,
  - spectral/discriminant extrapolations.

### How to upgrade conjectures
- The correct route is structural: prove recurrence/transfer-matrix control first, then deduce generating functions and discriminants.

---

### Chapter 28 (pp. 1101–1106): Explicit computations via NAP duality

### What is strong
- Potentially very useful as a computational shortcut.

### What is wrong
- Too short and under-integrated. It currently reads more like a promising appendix than a chapter.

### Correct upgrade
- Either expand it into a general computational framework used by Chapters 26–27, or move it into an appendix.

---

### Chapter 29 (pp. 1107–1132): Feynman diagram interpretation of bar-cobar duality

### What is strong
- Good conceptual bridge to perturbative QFT.

### What is wrong
- The physical dictionary is more speculative than the chapter structure advertises.
- The chapter should clearly distinguish what is already proved at genus 0 from what remains heuristic at higher genus.

### Correct upgrade
- Make the physics-dictionary conjecture template from Chapter 34 explicit here.
- Rephrase each conjecture as an asserted quasi-isomorphism between deformation complexes, not as a loose slogan.

---

### Chapter 30 (pp. 1133–1154): BV-BRST formalism and Gaiotto’s perspective

### What is strong
- The genus-0 bridge is now significantly stronger than earlier versions.
- The chapter contributes to one of the monograph’s most ambitious external connections.

### What is wrong
- The genus-0 theorematic gains are at risk of being obscured by higher-genus programme language.

### Correct upgrade
- Split the chapter into:
  1. proved genus-0 BRST/bar identifications,
  2. higher-genus programme.
- Make it explicit that the higher-genus statements require Costello renormalization input and remain correctly conjectural.

### How to upgrade conjectures
- The right path is incremental: extend BRST=bar beyond genus 0 first in families where the renormalization/control problem is tractable, rather than aiming for the full all-genera identity at once.

---

### Chapter 31 (pp. 1155–1174): Holomorphic-topological boundary conditions and 4d origins

### What is strong
- The chapter connects the monograph to a serious modern physics literature.

### What is wrong
- It should be more explicit about which statements are imported analogies, which are mathematically formulated conjectures, and which are genuine consequences of current theorems.

### Correct upgrade
- Organize the chapter by template type from Chapter 34: Type II, Type VII, etc.

---

### Chapter 32 (pp. 1175–1180): Knot invariants and the Kontsevich integral

### What is strong
- A potentially beautiful bridge.

### What is wrong
- The link remains too compressed and too conjectural for its current placement.

### Correct upgrade
- Make the chapter a short programme note unless the propagator identification is made fully rigorous.

### How to upgrade
- Either prove the propagator comparison rigorously or downgrade the chapter’s strongest cross-identifications to ProvedElsewhere / conjectural bridge statements.

---

### Chapter 33 (pp. 1181–1198): Physical origins

### What is strong
- This chapter now works well as narrative synthesis.

### What is wrong
- It still risks sounding like a proof chapter when it is actually a programme chapter.

### Correct upgrade
- Treat it explicitly as interpretation and programme rather than theorematic extension.
- Cross-link every major sentence to the precise theorem or conjecture it is interpreting.

---

### Chapter 34 (pp. 1199–1226): Concordance with primary literature

### What is strong
- This is now the most mature chapter in the manuscript.
- It gives the right stratification of conjectures, the right homotopy templates, the right nine-futures status accounting, and the right articulation of what the project wants to become.

### What is wrong
- The rest of the book has not caught up to it.
- Some status statements inside Chapter 34 still inherit overstrong periodicity claims from Chapter 11.

### Correct upgrade
- Use Chapter 34 as the control document for a global propagation pass.
- Every earlier chapter should be rewritten to match its terminology and status categories.

### How to upgrade the master conjectures
- 34.9.1 PBW degeneration: first target; turns conditional interacting families into unconditional ones.
- 34.9.2 cyclic L_infty and Theta_A: foundational target; turns the scalar/spectral package into full modular homotopy theory.
- 34.9.3 full factorization-categorical DK/KL: structural extension after 34.9.1 and Yangian/KL input.
- 34.9.4 completed bar theory for infinite generators: necessary for W_infty and Yangian towers.
- 34.9.5 BV/BRST/bar identification at all genera: downstream physics completion.

---

## How to upgrade the five master conjectures into proofs

### Conjecture 34.9.1 — Higher-genus PBW degeneration

This is the entry point. Without it, interacting families remain conditional.

### Required proof strategy
1. Build a genus-compatible filtered model whose associated graded is genuinely genus-0-like, not just morally so.
2. Prove a filtered deformation theorem showing central/fiberwise curvature does not alter the relevant filtered differential on the associated graded.
3. Control extension data and higher differentials at E2.
4. Do this first for affine Kac–Moody, then Virasoro, then W_N.

### Why this matters
A proof of 34.9.1 upgrades a large cluster of “conditional modular Koszul” statements to unconditional theorems.

---

### Conjecture 34.9.2 — Cyclic L_infty deformation algebra and universal Theta_A

This is the foundational target.

### Required proof strategy
1. Construct Def_cyc(A) as a cyclic L_infty model from bar coderivations / cyclic Hochschild / graph operations.
2. Prove existence of the cyclic pairing compatible with Lie brackets and trace.
3. Define the completed tensor product with RΓ(M_{g,•}).
4. Solve the MC equation in that completed setting.
5. Prove that trace recovers kappa*lambda_g, clutching gives sewing, and Verdier duality gives complementarity.

### Why this matters
It unifies the whole manuscript and turns many shadows into immediate consequences.

---

### Conjecture 34.9.3 — Full factorization-categorical DK/KL extension

### Required proof strategy
1. Fix the E1-factorization/coderived target category precisely.
2. Extend the proved chain-level/evaluation-locus results to dense subcategories with monoidal control.
3. Prove Yangian Koszulness / Kazhdan equivalence on the required domain.
4. Upgrade the square from chain-level commuting diagrams to equivalences of factorization categories.

### Why this matters
It turns the monograph’s quantum-group/Yangian branch from an impressive partial bridge into a full theorematic extension.

---

### Conjecture 34.9.4 — Completed bar theory for infinite-generator duals

### Required proof strategy
1. Build a pro-/completed version of the bar-cobar machine adequate for infinite-generator duals.
2. Prove convergence of finite-stage truncations.
3. Establish comparison with finite-type approximations or filtered towers.
4. Apply first to W_infty / Yangian towers.

### Why this matters
This is the gateway to the big non-finite-type dualities the manuscript keeps circling.

---

### Conjecture 34.9.5 — BV/BRST/bar identification at all genera

### Required proof strategy
1. Treat it as a Type VII quasi-isomorphism-of-deformation-problems statement.
2. Start with the already proved genus-0 identifications.
3. Add renormalization data and Costello-style genus control.
4. Prove compatibility with the modular/cyclic deformation package.

### Why this matters
This is the physics completion, not the mathematical foundation. It should remain downstream.

---

## The monograph’s natural final form

The manuscript wants to become a two-stratum work.

### Stratum I — Proved modular Koszul core
- Theorems A–D on the correct loci.
- Scalar and spectral characteristic packages.
- Chain-level / evaluation-locus DK.
- Free-field and conditional interacting examples.
- The discriminant as the first non-scalar characteristic class.

### Stratum II — Modular homotopy theory programme
- full cyclic L_infty deformation theory,
- coderived Ran formalism off the Koszul locus,
- full factorization-categorical DK/KL,
- completed infinite-generator duality,
- BV/BRST/path-integral/holography dictionary,
- elliptic/toroidal and higher-dimensional extensions.

The current manuscript is strongest when it respects this split.

## Highest-leverage immediate edits

1. Downgrade or re-prove the modular periodicity theorems in Chapter 11.
2. Split periodicity exchange into proved and conditional parts.
3. Rewrite Chapter 1’s package language to match Chapter 8 / Chapter 34 status discipline.
4. Consolidate all definitions of Koszul pair / modular Koszul object.
5. Run a Chapter-34 propagation pass over the whole book.
6. Clean the conjecture registry and duplicate labels.
7. Re-tag every theorem/conjecture by H/M/S level and by status: proved / conditional / conjectural / programme.

## Final verdict

The manuscript is now good enough that the right critique is no longer “is the main architecture false?” It is “how do we make the current architecture read as the first volume of a coherent modular homotopy theory?”

The answer is:
- stabilize the periodicity flank,
- propagate the new semantic/status discipline globally,
- split theorem from programme everywhere,
- and aim the next proof effort at higher-genus PBW degeneration and the cyclic L_infty deformation object.
