# Wave 4: Adversarial review of 3d quantum gravity, holographic, and entanglement claims

**Date**: 2026-04-16
**Reviewer**: adversarial swarm (Vol I)
**Target files**:
- `~/chiral-bar-cobar/standalone/three_dimensional_quantum_gravity.tex` (2,799 lines, "Paper M", scaffold tagged for Annals)
- `~/chiral-bar-cobar/standalone/holographic_datum.tex` (~1,250 lines, full holographic datum paper)
- `~/chiral-bar-cobar/standalone/w3_holographic_datum.tex` (575 lines, $\mathcal{W}_3$ extension)
- `~/chiral-bar-cobar/chapters/connections/holographic_datum_master.tex` (~5,300 lines, "seven faces" master)
- `~/chiral-bar-cobar/chapters/connections/holographic_codes_koszul.tex` (792 lines)
- `~/chiral-bar-cobar/chapters/connections/thqg_entanglement_programme.tex` (~960 lines)
- `~/chiral-bar-cobar/chapters/connections/thqg_introduction_supplement.tex` (227 lines)
- `~/chiral-bar-cobar/chapters/connections/entanglement_modular_koszul.tex` (~1,100 lines)
- `~/chiral-bar-cobar/chapters/connections/frontier_modular_holography_platonic.tex` (~5,300 lines)

---

## Section 1. Triage of holographic / 3d gravity / entanglement claims

The Vol I holographic / 3d gravity programme rests on six load-bearing identifications. Each is graded **PROVED**, **CORRECT-AS-RESTRICTED**, **NARRATION**, or **CONFABULATION**.

| # | Claim | Locus | Verdict |
|---|-------|-------|---------|
| H1 | "Modular Koszul duality of $\mathrm{Vir}_c$ constitutes the **complete** algebraic description of 3d gravity." | 3DQG abstract L57-69 | **NARRATION** (stronger than supported) |
| H2 | "Koszul duality $\mathrm{Vir}_c \leftrightarrow \mathrm{Vir}_{26-c}$ is gravitational S-duality." | 3DQG abstract L75; thm:vir-koszul L998 | **CONFABULATION** (no string-theoretic S-duality argument) |
| H3 | $A_X^! = \mathrm{Vir}_{26-c}$ via Verdier dual + cobar (Koszul shift = $bc$ ghost central charge). | 3DQG L1016-1034 | **NARRATION** (proof asserts the shift, doesn't derive it) |
| H4 | "Page curve emerges from Koszul complementarity"; Page time $t_P = 3 S_{\mathrm{BH}}/13$ is $c$-independent. | 3DQG sec:page-curve L1927+; ent_modular_koszul conj:ent-page-curve L981 | **CORRECT-AS-RESTRICTED** (algebraic identity; physical identification heuristic, recently honestly downgraded in `entanglement_modular_koszul`) |
| H5 | "Koszulness $\Leftrightarrow$ exact holographic reconstruction" (Theorem G12). | holographic_codes_koszul L339-421 | **CORRECT-AS-RESTRICTED** when read as bar/cobar exact recovery; **NARRATION** when read as HKLL bulk reconstruction |
| H6 | "Holographic codes from Koszul duality" — symplectic code structure, code rate $R = 1/2$, distance $d = 2$, redundancy = $r_{\max}-2$. | holographic_codes_koszul thm:hc-symplectic-code L220-283; rem:hc-universal-parameters L673-699 | **NARRATION** for code rate / distance; **PROVED** for Lagrangian isotropy fact (Verdier-isotropic decomposition is real) |
| H7 | Entanglement entropy = scalar projection of bar complex; $S_{\mathrm{EE}}(\cA)+S_{\mathrm{EE}}(\cA^!) = (c+c')/3 \cdot \log(L/\varepsilon)$. | ent_modular_koszul L234-294 | **PROVED-AS-RESTRICTED** (scalar level uses Calabrese–Cardy as imported input — labeled `ProvedElsewhere` correctly at L134) |
| H8 | BTZ as MC element of $\mathfrak{g}^{\mathrm{mod}}_{\mathrm{Vir}_c}$ (thm:btz-mc, 3DQG L1748-1775). | 3DQG L1746 | **NARRATION** (the MC equation is stated to "equal" $F_\pm = 0$; the proof is an assertion sketch, not a computation) |
| H9 | The "gravitational Yangian" $\mathcal{Y}_{\mathrm{grav}}$ at $c=13$ generates the Page-curve symmetry. | 3DQG sec:gravitational-yangian L2645-2798 | **CONFABULATION** (Vir does not have a known Yangian; conj:yangian-symmetry L2758 is a wishlist tagged \conjecture but the surrounding prose treats it as a discovered structure) |
| H10 | de Sitter entropy from $\kappa \to -|\kappa|$ analytic continuation; Banks finiteness. | 3DQG sec:de-sitter L2524-2604 | **NARRATION** (the Wick rotation continuation is asserted to "preserve the shadow tower"; no proof of analytic continuation in the genuine sense) |
| H11 | Holographic datum $\mathcal{H}(\cA) = (\cA, \cA^!, \cC, r(z), \Theta_\cA, \nabla^{\mathrm{hol}})$ is a **complete** invariant. | holo_datum thm:holographic-explicit L1254; thqg_intro_supplement L185-225 | **CORRECT-AS-RESTRICTED** (datum exists; "complete invariant" claim of recovery (R1)–(R4) is at the level of restricted recovery, not categorical reconstruction) |
| H12 | Bulk = $\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA) \simeq \mathbb{C}\llbracket c \rrbracket$ and the bulk-boundary-line "triangle commutes". | 3DQG sec:gravitational-bulk L607-744; holo_datum sec:bbl L885-1023 | **CORRECT-AS-RESTRICTED** for the Hilbert series; **NARRATION** for the "triangle" being a single object viewed three ways (it isn't; see Section 4.3 below) |

---

## Section 2. Per-claim attack/defence/repair

### H1 — "Complete algebraic description of 3d gravity" (3DQG abstract)

**Attack.** The abstract (L57-69) states the modular Koszul package is the *complete* description of 3d gravity. This is stronger than what the paper proves. The paper computes a Virasoro chiral algebra and its bar/Koszul-dual data; this is the boundary CFT (Liouville-like sector or pure Vir), not the gravitational *quantum* path integral. Witten's 2007 analysis of pure 3d gravity argues that the holomorphically factorised partition function for $c=24k$ requires the Monster-like extremal CFT — a much more delicate object than $\mathrm{Vir}_c$. The paper cites neither the Witten 2007 analysis nor Maloney–Witten on the modular sum diverging. The "complete" claim ignores: (a) the gravitational sum over geometries (3DQG only treats the smooth hyperbolic sector implicitly); (b) wormhole / replica saddles (treated only via the Page-curve heuristic in §sec:page-curve); (c) non-perturbative effects beyond Borel resummation.

**Defence.** Within the **perturbative on-shell algebraic** scope, the holographic datum captures: $\kappa = c/2$ (Brown–Henneaux), the genus tower $F_g = (c/48)\hat{A}$ corrections, and the saddle-point Cardy formula. This is real algebraic content.

**Repair.** Restrict the abstract: replace "constitutes the complete algebraic description" with "constitutes the **boundary algebraic** description in the perturbative regime, including the genus expansion of the gravitational free energy and the Cardy entropy". Cite Witten 2007 explicitly as the unresolved nonperturbative completion. Otherwise this is AP155 overclaiming and FM43-style scope inflation.

### H2 — "Koszul duality is gravitational S-duality" (abstract L75; thm:vir-koszul L998)

**Attack.** "S-duality" is a precise term in physics: a strong/weak coupling exchange, typically $g \to 1/g$, often with a Z-action on a coupling space, with non-trivial spectrum-matching theorems. None of these features appear in the proof of thm:vir-koszul. The "duality" $c \leftrightarrow 26-c$ is the Feigin–Fuchs / contragredient symmetry of $\mathrm{Vir}$. Calling this S-duality conflates: (i) Koszul duality (algebraic involution on bar coalgebra); (ii) the Feigin–Fuchs reflection (acting on Verma modules); (iii) physical S-duality of 3d gravity (which, if it exists, must exchange $G \to 1/G$ in some sense, i.e. $c \to 1/c$ at large $c$, NOT $c \to 26-c$). At $c=13$ self-duality, $G = 3\ell/(2 \cdot 13)$ is not the "inverse" of any physically meaningful coupling.

**Defence.** The matching $c + (26-c) = 26$ is correct as the matter-plus-bc-ghost central charge cancellation. The "gravitational" reading is genuine in that $26-c$ is the Koszul-conjugate central charge.

**Repair.** Rename "gravitational S-duality" to "Feigin–Fuchs / Koszul reflection". Drop S-duality language unless an explicit $G_N \leftrightarrow ?$ map is given. AP155 hard violation.

### H3 — Verdier dual / cobar gives $\mathrm{Vir}_{26-c}$ (3DQG L1016-1034)

**Attack.** The "proof" of thm:vir-koszul (3DQG L1016-1034) is a sketch:
- L1018-1021: "By the bar-cobar theorem, the cobar of $D_{\mathrm{Ran}}(\bar B)$ recovers an algebra: on the Koszul locus, this algebra is $\mathrm{Vir}_{26-c}$." — This *asserts* the conclusion. The bar-cobar theorem only gives that cobar-of-bar recovers $\cA$, not $\cA^!$ at central-charge-shifted level.
- L1022-1029: "The central charge shift $c \mapsto 26-c$ arises from the Shapovalov transposition: the Koszul dual of the Verma module at conformal weight $h$ over $\mathrm{Vir}_c$ is the contragredient Verma module at weight $h$ over $\mathrm{Vir}_{26-c}$. The shift by $26$ is the $bc$ ghost central charge: the Verdier duality functor on the bar complex has the same effect as coupling to the $bc$ ghost system." — This is a *narrative* identification, not a proof. The genuine result is Feigin's (1984) intertwining $V_h^{c} \to V_{1-h}^{26-c}$ for Verma modules; Vol I needs to either cite this or prove it within the bar complex.

**Defence.** The shift $c \mapsto 26-c$ is correct and known: it's the Felder/Frenkel–Ben-Zvi reflection $c \leftrightarrow 26-c$ from coupling matter to the $bc$ ghost system (BRST quantisation of bosonic string). The bar/cobar machine *reproduces* this shift.

**Repair.** Write the proof as: (i) cite Feigin / Frenkel–Ben-Zvi for the central-charge shift; (ii) verify that the Vol I bar/cobar machine reproduces it via an explicit chain-level computation; (iii) state the result as "Theorem (Feigin '84, recovered via bar-cobar): ...". This is AP155 overclaim of novelty + AP-CY57 narration-not-construction.

### H4 — Page time $t_P = 3 S_{\mathrm{BH}}/13$ from complementarity (3DQG sec:page-curve)

**Attack.** The mathematical computation (L2186-2196) is correct: rate $c/6$ + rate $(26-c)/6 = 26/6$ summed gives $t_P = 6 S_{\mathrm{BH}}/26 = 3 S_{\mathrm{BH}}/13$. The *physical* identification of the two saddles with Hawking and Island saddles requires:
- a gravitational dual where the bar complex $\bar B(\cA^!)$ controls the island geometry (the manuscript admits this in `entanglement_modular_koszul.tex` L984-993 — this honest downgrade exists);
- the rate $(26-c)/6$ to be the actual entanglement-evaporation rate of the Koszul-dual saddle (asserted in def:evaporation-rate L2058-2075, but this is not derived from any island computation; it is *defined* by analogy);
- a justification for *why* the Koszul-dual sector should be identified with the island. Penington–AEMM islands come from the gravitational path integral over replica wormholes; the Koszul dual is an *algebraic* construction. The link is NOT proved.

**Defence.** The structural shadow of complementarity (two saddles, period-2, crossing-time $\propto K$) is real and worth highlighting. The downgrade in `entanglement_modular_koszul` to `\ClaimStatusConjectured` and the explicit "epistemic note" L984-993 are honest scholarship. The 3DQG paper at L2289-2319 has rem:island that draws the analogy but flags it as identification, not theorem.

**Repair.** **Already partially done in `entanglement_modular_koszul.tex`** (the conjecture status + epistemic note added). The 3DQG paper still has thm:page-curve at L2077 stated as a `\begin{theorem}` (not `\begin{conjecture}`); this is the strongest correctable piece. **Action**: convert thm:page-curve in 3DQG to `\begin{theorem}[Algebraic Page-time identity]` — the *crossing-time identity* is genuinely a theorem given the stated rates. Add a separate `\begin{conjecture}[Page curve]` for the *physical identification* with the gravitational Page curve.

### H5 — Koszulness ⇔ exact holographic reconstruction (G12, holo_codes L339)

**Attack.** Read literally, "exact holographic reconstruction" suggests HKLL bulk reconstruction (every bulk operator is recovered from the boundary algebra modulo gauge). The proof (L385-421) actually proves: bar-cobar exact recovery $\Omega(B(\cA)) \to \cA$ is a quasi-iso iff $\cA$ is Koszul. This is a tautology since K4 is *defined* as bar-cobar quasi-iso. The (iii) ⇒ (i) step (L408-414) says "if $\cA$ is not Koszul, the counit is not a quasi-iso, so bulk operators depending on lost cohomology cannot be recovered, contradicting (iii)." This silently *defines* (iii) (= "every bulk operator in $C^\bullet_{\mathrm{ch}}$ is recoverable from $B(\cA)$") to be K4. There is no independent **physical** notion of "bulk reconstruction" being verified. Compare AP155: the manuscript's contribution is the **construction path** (bar-cobar ↔ Koszul), not the physical theorem that holographic codes work this way.

**Defence.** As an algebraic statement (K4 ⇔ K4), the theorem is trivially true. The structural mapping to PYHP / holographic-code thinking is real and instructive.

**Repair.** Rephrase: "Koszulness is **equivalent to** the algebraic **bar-cobar inversion** condition (tautological); we **interpret** this as a precise algebraic incarnation of the exact-bulk-reconstruction property of holographic codes (PYHP)." This kills the (iii) ⇒ (i) circularity. AP-CY57 narration violation.

### H6 — Code rate $R=1/2$, distance $d=2$, redundancy $= r_{\max}-2$ (rem:hc-universal-parameters L673)

**Attack.** Three sub-claims:
- **Rate $R = 1/2$**: derived from Lagrangian half-dimensionality (correct), but conditional on perfectness (K11 marked $*$ in the 12-dictionary L573-617). Stating it as a "universal parameter" L678-682 obscures this dependency.
- **Distance $d = 2$**: derived as "the bar degree shift, which equals 2 (the desuspension $s^{-1}$ has degree $-1$, so the first nontrivial bar element has degree 2)". This is an *algebraic* degree, not a code-distance in the QECC sense (minimum weight of an undetectable error). The conflation is silent. Compare AP-CY57.
- **Redundancy = $r_{\max} - 2$**: thm:hc-shadow-redundancy L458 conjectures-then-proves (L460) that "shadow depth controls redundancy"; the proof L514-547 only shows that the shadow tower has $r_{\max}-2$ levels of obstruction. This is not the same as having $r_{\max}-2$ "redundancy channels" in the QECC sense. The mapping is structural, not formal.

**Defence.** The Lagrangian structure is real. The structural analogy to QECC is suggestive.

**Repair.** Mark the three "universal parameters" as **structural analogies, not literal QECC parameters**. Use $\dim_{\mathrm{algebraic}}$, $r_{\mathrm{shadow}}$, $\dim_{\mathrm{Lag}}/\dim_{\mathrm{ambient}} = 1/2$ language to disambiguate from QECC $d, n, k$. The honest reading is `Theorem [Algebraic invariants of the Koszul code]` not `Universal code parameters`.

### H8 — BTZ as MC element (3DQG thm:btz-mc L1748)

**Attack.** The "proof" L1766-1774 is one paragraph: "The BTZ solution is a flat connection... Flatness becomes the MC equation: the highest-weight state $|h, \bar h\rangle$ in the Virasoro module satisfies the conformal Ward identities, which are exactly the components of the MC equation projected to the boundary." This conflates several things:
- Flatness of the Chern-Simons gauge field $F_\pm = 0$ is a *spacetime* equation;
- The MC equation $D\Theta + \frac{1}{2}[\Theta,\Theta] = 0$ is an *algebraic* equation in $\mathfrak{g}^{\mathrm{mod}}_{\mathrm{Vir}_c}$;
- The "conformal Ward identities" relate stress-tensor insertions in correlation functions, NOT to the MC equation directly.
The mapping from BTZ (a particular flat connection on the solid torus with specified holonomy) to a particular MC element $h\,e_h + \bar h\, e_{\bar h}$ is a *parametrisation by $(h,\bar h)$*, but the assertion that this satisfies the MC equation in the convolution algebra is unproved.

**Defence.** BTZ is a thermal state with Cardy degeneracy $\rho(h) \sim e^{2\pi\sqrt{ch/6}}$. The label $(h,\bar h)$ is a genuine point in the Virasoro module space.

**Repair.** Either: (a) provide an explicit chain-level proof that $\alpha_{\mathrm{BTZ}} = h e_h + \bar h e_{\bar h}$ is in $\mathrm{MC}(\mathfrak{g}^{\mathrm{mod}})$ — i.e. compute $D\alpha_{\mathrm{BTZ}}$ and $[\alpha_{\mathrm{BTZ}},\alpha_{\mathrm{BTZ}}]$ explicitly; or (b) downgrade thm:btz-mc to `\begin{construction}` ("BTZ defines a candidate MC element") with the MC condition as a follow-up proposition. As stated, this is AP-CY57 narration.

### H9 — Gravitational Yangian at $c=13$ (3DQG sec:gravitational-yangian L2645-2798)

**Attack.** Triple violation:
- **Vir has no known Yangian.** The Yangian $Y(\fg)$ is defined for finite-dimensional simple Lie algebras $\fg$. Vir is infinite-dimensional, and there is no published construction of $Y(\mathrm{Vir})$. The phrase "the Yangian $Y(\mathfrak{vir}_{13})$ associated to the Virasoro Lie algebra" (conj:yangian-symmetry L2767) presumes existence.
- **The "shadow obstruction tower at $c=13$"** is an infinite sequence of rational numbers ($S_2 = 13/2, S_3 = -13, S_4 = 10/1131, \ldots$), L2687-2693. Calling this set of numbers a "Yangian symmetry" requires a Hopf algebra structure with coproduct, antipode, and RTT relations. The conjecture L2776 asserts RTT relations but provides no construction of $T(z)$ in the alleged Yangian.
- **AP150 confabulation**: the "gravitational Yangian" is constructed from disparate ingredients (the shadow tower, the $r$-matrix at $c=13$, the conjectural RTT relations) that do not form a known Yangian-like structure. The composite arrow has not been built.

**Defence.** The point that $c=13$ has special structure (Koszul self-dual, equal saddles) is correct. The notation $\mathcal{Y}_{\mathrm{grav}}$ is harmless if used as a *name* for "the algebra of conserved charges of the shadow tower at $c=13$".

**Repair.** Rename to "the conserved-charge algebra at $c=13$" or "the Koszul-self-dual symmetry algebra". Drop "Yangian" unless a Yangian-like RTT presentation is given. The conj:yangian-symmetry already carries `\begin{conjecture}`; the surrounding prose at L2649-2756 should match. AP150 + AP155 hybrid.

### H10 — De Sitter via $\kappa \to -|\kappa|$ (3DQG sec:de-sitter L2524-2604)

**Attack.** The Wick rotation $\ell \mapsto i\ell$ from AdS$_3$ to dS$_3$ is much more delicate than "the central charge continues to $c_{\mathrm{dS}} = 3\ell_{\mathrm{dS}}/(2G)$" (L2540-2542). For dS$_3$:
- The Brown–Henneaux argument breaks down: dS$_3$ has no asymptotic conformal boundary at spatial infinity in the same sense.
- The "central charge" of dS$_3$ has been studied (Strominger 2001, Maloney–Strominger–Yin) and is *imaginary* in many natural prescriptions, not real.
- The claim L2596-2603 that the convergent shadow tower is "consistent with" Banks finite-dimensional $\mathcal{H}_{\mathrm{dS}}$ is heuristic at best; convergence of a perturbation series in $\kappa$ does NOT imply finite-dimensionality of the underlying Hilbert space.

**Defence.** As a formal analytic continuation of the bar/Koszul algebraic data, the substitution $\ell \to i\ell$ is well-defined and gives $\kappa_{\mathrm{dS}}$ real (since $c$ continues to a real value).

**Repair.** Replace "The central charge continues to..." with "We **define** $c_{\mathrm{dS}} := 3\ell_{\mathrm{dS}}/(2G)$ as the formal continuation of the Brown–Henneaux value; the physical interpretation as an asymptotic CFT central charge of dS$_3$ requires additional input (cite Strominger 2001) and is **not** established here." Mark thm:desitter at L2536 as `\begin{theorem}[Formal de Sitter shadow tower]`. Drop "Banks consistency" remark or downgrade to clearly heuristic.

### H11 — Holographic datum is a complete invariant (holo_datum thm:holographic-explicit L1254)

**Attack.** "Complete invariant" is precisely defined in algebraic geometry / categorification: two objects are isomorphic iff their invariants agree. The paper does not prove that distinct chiral algebras with the same six-component datum must be isomorphic. Recovery propositions (R1)–(R4) at holo_datum L967-989 only show that *certain projections* of the datum can be reconstructed from each other, not that the datum determines $\cA$.

**Defence.** The datum collects the natural invariants of the chiral Koszul structure, and for the three computed examples ($\cH_k$, $\widehat{\fsl}_2{}_k$, $\mathrm{Vir}_c$) it does fully determine the algebra (each is determined by a single parameter $k$ or $c$).

**Repair.** Replace "complete invariant" with "characteristic datum" or "complete **projection-recovery** invariant" with the precise scope: "for each component, recover the corresponding projection of $\Theta_\cA$; reconstruction of $\cA$ from $\mathcal{H}(\cA)$ is conditional on a Tannakian-style hypothesis (open)."

### H12 — "Bulk-boundary-line triangle is a single object viewed three ways" (holo_datum L217-223; thqg_intro_supplement L156-184)

**Attack.** The three vertices are three *different* algebraic objects:
- Boundary $\cA$: the chiral algebra itself (an $E_1$-chiral or $E_\infty$ object on $X$);
- Bulk $\mathbf{C}_g(\cA) = R\Gamma(\overline{\cM}_g, \cZ(\cA))$: the global sections of the centre over moduli;
- Lines $\cA^!\text{-mod}$: a categorical module category.
These are objects of three genuinely different categories (chiral algebras, perfect complexes, dg categories). Calling them "the same object viewed three ways" (3DQG L890; holo_datum L217) is AP-CY57 narration. The functorial relationships between them are real, but they are *distinct objects connected by functors*, not a single object.

**Defence.** All three are derived from the bar complex $\bar B(\cA)$ via different functors. There is genuine unification.

**Repair.** Replace "single object viewed three ways" with "three **functorial outputs** of the bar complex $\bar B(\cA)$ via three distinct functors". This is the honest reading.

---

## Section 3. AP155 novelty audit table

| Claim | Existing literature | Manuscript contribution | Verdict |
|-------|--------------------|--------------------------|---------|
| Page time $t_P \propto S_{\mathrm{BH}}/c$ | Page 1993, Penington 2019, AEMM 2019 | crossing-time computed from rates $c/6$ and $(26-c)/6$ | **construction path new**; result well-known structurally |
| BTZ Cardy entropy $S = 2\pi\sqrt{ch/6}$ | Strominger 1997, Birmingham–Sachs–Sen 1998 | re-derived from modular characteristic via Cardy | **construction path new**; result identical |
| RT/CC entropy $S = (c/3)\log(L/\varepsilon)$ | Calabrese–Cardy 2004 | imported via Lemma 1 (correctly attributed `\ClaimStatusProvedElsewhere`) | honest |
| Holographic codes structure | PYHP 2015, ADH 2015 | symplectic (not orthogonal) Lagrangian splitting | **structural analogy with new flavour** |
| Modular flow ↔ shadow connection | Tomita–Takesaki, Witten 2018 (review) | structural conjecture | downgraded honestly to `\begin{conjecture}` |
| 3d gravity = SL(2,R)×SL(2,R) CS | Achucarro–Townsend 1986, Witten 1988 | cited correctly | honest |
| Brown–Henneaux $c = 3\ell/(2G)$ | BH 1986 | cited correctly | honest |
| FLM bulk corrections to RT | Faulkner–Lewkowycz–Maldacena 2013 | identified (heuristically) with shadow corrections $\delta S_r$ | **identification heuristic**, correctly flagged at ent_modular_koszul L546-548 |
| Strominger–Vafa via Cardy | Strominger–Vafa 1996 | reformulated via $\kappa$ | **reformulation**, AP155 |
| Hawking–Page transition | Hawking–Page 1983 | algebraic incarnation via two saddles | **construction path new** |
| QES formula | Engelhardt–Wall 2014 | identified (heuristically) with shadow Ward identity | downgraded to `\begin{conjecture}` |
| Koszul S-duality | none (this is the manuscript's new naming) | naming + computation | **CONFABULATION** of the term "S-duality" |
| Gravitational Yangian | none ($Y(\mathrm{Vir})$ does not exist in literature) | naming + conjecture | **CONFABULATION** + AP150 |
| Borel singularity at $A_{\mathrm{inst}} = (2\pi)^2 |c-13|/13$ | Eberhardt 2020 (resurgence in 3d gravity) | derived from complementarity | **construction path new** but unciteed precedent |
| Mock modular Eisenstein at genus 1 (3DQG L1665-1700) | Zagier mock theta, Bringmann–Folsom–Ono | recovered via fibre differential | **reformulation** |

**Bottom line**: At least 4 named results are reformulations of known results without explicit attribution as "recovered via new path"; 2 named structures ("Koszul S-duality", "gravitational Yangian") are confabulations.

---

## Section 4. First-principles analyses

### 4.1 Confusion: "Koszul duality = S-duality"

**Wrong claim**: $\mathrm{Vir}_c \leftrightarrow \mathrm{Vir}_{26-c}$ is "gravitational S-duality".

**Ghost theorem**: There IS a real algebraic involution $c \mapsto 26-c$ that exchanges chiral algebra and Koszul dual. This is the Feigin–Fuchs reflection, well-established at the level of Verma modules.

**Precise error**: "S-duality" presupposes a coupling-inversion structure ($g \to 1/g$ for Yang–Mills, $\tau \to -1/\tau$ for type IIB). The Koszul reflection $c \to 26-c$ is *additive*, not multiplicative. At $c \to \infty$ (semiclassical), the dual $26-c \to -\infty$ is *not* a "weak coupling" of the original.

**Correct relationship**: Koszul reflection ⊆ Verdier duality on bar coalgebras, manifested as $c \leftrightarrow 26-c$ via the bc-ghost central charge; **NOT** a coupling-inversion duality. Type: **label/content** confusion.

### 4.2 Confusion: "BTZ is an MC element"

**Wrong claim**: BTZ black hole is an MC element of the convolution algebra.

**Ghost theorem**: BTZ corresponds to a specific point in the Virasoro module space (a primary state $|h, \bar h\rangle$ with $h, \bar h$ determined by $M, J$). The Cardy degeneracy of states at $(h, \bar h)$ matches the BH entropy.

**Precise error**: A primary state is an element of a *module*, not of the *Lie algebra* / convolution algebra. The MC equation is in $\mathfrak{g}^{\mathrm{mod}}_{\mathrm{Vir}_c}$ (the convolution dg Lie algebra), not in the module of states. The statement "$\alpha_{\mathrm{BTZ}} = h e_h + \bar h e_{\bar h} \in \mathfrak{g}^{\mathrm{mod}}$" presupposes that the generators $e_h, e_{\bar h}$ exist in the convolution algebra, which is unproven for arbitrary $h$.

**Correct relationship**: BTZ defines a *Cardy state* in the module category, not an MC element of the convolution Lie algebra. The relationship of the Cardy state to the bar / shadow data is real but indirect (via the modular S-transform, not directly via MC). Type: **algebra/module** confusion (a sub-type of algebra/coalgebra).

### 4.3 Confusion: "Bulk-boundary-line triangle is one object viewed three ways"

**Wrong claim**: The three vertices are a single object (the bar complex $\bar B(\cA)$ with its $E_1$-chiral coassociative structure) viewed from three angles.

**Ghost theorem**: There IS a unifying algebraic structure: the bar complex is an $E_1$-chiral coassociative coalgebra, and **functors** out of this coalgebra produce the boundary, bulk, and line vertices. The functors are:
- Cobar $\Omega \dashv B$: recovers boundary $\cA$;
- Centre $C^\bullet_{\mathrm{ch}}(\cA, \cA)$: derives the bulk;
- Module category $\cA^!\text{-mod}$ via Koszul dualisation: produces the lines.

**Precise error**: A single object can have many functorial outputs without itself BEING those outputs. Calling boundary, bulk, lines "the same object" conflates the source of a functor with its target. Type: **construction/narration** confusion (AP-CY57).

### 4.4 Confusion: "Holographic datum is a complete invariant"

**Wrong claim**: The six-component datum $\mathcal{H}(\cA)$ is a complete invariant of $\cA$.

**Ghost theorem**: The datum captures the natural projections of the bar-intrinsic MC element $\Theta_\cA$. For chirally Koszul algebras with a single generating field of fixed conformal weight (Heisenberg, Vir), the datum essentially determines $\cA$ up to isomorphism via parameter recovery (recover $k$ for $\cH_k$; recover $c$ for $\mathrm{Vir}_c$).

**Precise error**: "Complete invariant" requires: $\mathcal{H}(\cA_1) \cong \mathcal{H}(\cA_2) \Rightarrow \cA_1 \cong \cA_2$. The manuscript proves only: certain projections of the datum can be re-extracted from other projections (the "recovery propositions" R1–R4). This does NOT establish completeness.

**Correct relationship**: $\mathcal{H}(\cA)$ is a **functorial datum** (a projection of $\Theta_\cA$ to a fixed list of slots). Its discriminating power is open in general. For the three computed families it is *parameter-complete* (single-parameter algebras determined by their parameter). Type: **necessary/sufficient** confusion.

### 4.5 Confusion: "Distance $d=2$" of the Koszul code

**Wrong claim**: The Koszul code has code distance $d = 2$ (rem:hc-universal-parameters L685-689).

**Ghost theorem**: The bar complex augmentation ideal starts at degree 2 (since $s^{-1}$ has degree $-1$ and the lowest non-vacuum bar element has internal degree at least 1, so total degree $\geq 2$). This is an algebraic graded structure.

**Precise error**: Code distance in QECC is the minimum weight of an undetectable error operator: $d = \min\{\mathrm{wt}(E) : E \in \mathcal{N}(\mathcal{S}) \setminus \mathcal{S}\}$. There is no notion of "weight" for algebraic bar elements; the algebraic degree is not the QECC weight. The conflation L686-689 is silent.

**Correct relationship**: The bar-degree of the lowest nontrivial bar element is 2; this is an *algebraic invariant*, not a QECC code distance. Type: **label/content** confusion.

---

## Section 5. Three upgrade paths

### Path A (strongest, hardest to achieve)
**Universal holographic Koszul-duality theorem**: state and prove that for every chiral Koszul vertex algebra $\cA$ on a smooth projective curve $X$, the bar complex $\bar B(\cA)$ on a closed surface $\Sigma$ computes the bulk gravitational partition function $Z_{\mathrm{grav}}(\Sigma)$ on AdS$_3 \times \Sigma$ in the algebraic limit. Concretely:

> For $\cA = \mathrm{Vir}_c$, $Z_{\mathrm{grav}}^{\mathrm{boundary}}(\Sigma_g) = \exp(\sum_{g'} F_{g'}(\bar B(\mathrm{Vir}_c))$, where $F_{g'}$ are the genus free energies computed as scalar projections of $\Theta_{\mathrm{Vir}_c}$ on $\overline{\cM}_{g'}$.

This requires: (i) precise identification of the boundary CFT; (ii) sum over geometries on the bulk side reduced to a sum over boundary chiral algebra states; (iii) modular invariance theorem matching the bar Euler product to a modular form. **Pieces in place**: $F_1 = c/48$ (proved), $\hat A$-genus formula (proved). **Pieces missing**: bulk-side derivation, modularity of full $Z_{\mathrm{grav}}$ in the algebraic limit, treatment of the sum over geometries.

### Path B (medium)
**Explicit symplectic-code construction from Koszul pairs**: starting with the Lagrangian decomposition $\mathbf{C}_g(\cA) = \mathbf{Q}_g(\cA) \oplus \mathbf{Q}_g(\cA^!)$, give an **explicit recipe** for building a quantum stabiliser code (or an algebraic analogue) with parameters $[[n, k, d]]$ readable from the bar/Koszul data. The Theorem G12 + Theorem hc-symplectic-code give the algebraic prerequisites; the missing step is the QECC translation (Lagrangian-isotropic stabiliser group, code subspace as joint $+1$ eigenspace). For Heisenberg this should reproduce a Gaussian / continuous-variable code; for Vir at finite truncation, a stabiliser code over a finite field.

**Pieces in place**: Lagrangian isotropy proved (prop:hc-knill-laflamme), 12-dictionary structure, shadow-depth-as-redundancy.
**Pieces missing**: explicit stabiliser group construction, finite-dimensional truncation, explicit $[[n, k, d]]$ for at least one chiral family.

### Path C (genuine breakthrough)
**AdS$_3$/CFT$_2$ entanglement-modular dictionary as a chain-level equivalence of factorisation algebras**: prove that the boundary chiral algebra $\cA$ on $\partial \mathrm{AdS}_3 = \mathbb{C}$ and the bulk Chern–Simons factorisation algebra on AdS$_3$ are quasi-isomorphic as $E_3$-algebras (or as $\mathsf{SC}^{\mathrm{ch,top}}$-algebras), with the entanglement modular Hamiltonian on the boundary identified with the symplectic generator of the boundary deformation on the bulk. Such a theorem would justify all the entanglement / modular flow conjectures (G13–G16) in `thqg_entanglement_programme.tex`.

**Pieces in place**: the $\mathsf{SC}^{\mathrm{ch,top}}$ structure on the centre pair $(\cZ^{\mathrm{der}}_{\mathrm{ch}}(\cA), \cA)$ (proved), $E_3$-topologisation for affine KM at non-critical level (Vol II thm:topologization), the shadow connection $\nabla^{\mathrm{hol}}$.
**Pieces missing**: chain-level $E_3$ for Vir (currently cohomological only, see Vol III rem:e3-scope); identification of the modular Hamiltonian with a specific algebraic object on the bulk; treatment of the gravitational sum over geometries.

---

## Section 6. Consolidated punch list (priority order)

**P1 — must-fix to avoid AP155 / AP-CY57 / AP150 violations**

1. **3DQG abstract L57-86**: replace "constitutes the complete algebraic description of the gravitational theory" with "constitutes the boundary algebraic description in the perturbative regime". Add explicit caveat citing Witten 2007 / Maloney–Witten on the gravitational sum.

2. **3DQG thm:vir-koszul L998 + abstract L75**: drop "S-duality" language; rename to "Koszul reflection" or "Feigin–Fuchs involution at the bar level". Cite Feigin 1984 explicitly. Rewrite proof L1016-1034 as: cite Feigin → verify reproduction in bar/cobar → state as "reproduces Feigin's reflection".

3. **3DQG thm:btz-mc L1748**: downgrade to `\begin{construction}` and provide either a chain-level proof of MC condition or restructure as "BTZ defines a Cardy state" (the more honest framing).

4. **3DQG sec:gravitational-yangian L2645-2798**: rename "gravitational Yangian" to "conserved-charge algebra at $c=13$" or "Koszul-self-dual symmetry algebra". The conj:yangian-symmetry already has `\begin{conjecture}`; align the surrounding prose. **Drop** "Yangian $Y(\mathrm{vir}_{13})$" language since $Y(\mathrm{Vir})$ does not exist.

5. **3DQG thm:page-curve L2077**: split into (a) `\begin{theorem}[Algebraic crossing-time identity]` for the calculation, (b) `\begin{conjecture}[Page curve]` for the physical identification with the gravitational Page curve. The companion downgrade in `entanglement_modular_koszul.tex` L981 is already done; mirror it here.

6. **3DQG sec:de-sitter L2524-2604**: mark thm:desitter as `\begin{theorem}[Formal de Sitter shadow tower]` (formal continuation, not physical theorem). Drop "Banks consistency" remark or downgrade to clearly heuristic.

7. **holographic_codes_koszul rem:hc-universal-parameters L673-699**: add explicit caveat that "rate $R = 1/2$, distance $d = 2$, redundancy $= r_{\max} - 2$" are **structural parameters of the algebraic Koszul code**, NOT literal QECC parameters. Use $R^{\mathrm{alg}}, d^{\mathrm{alg}}$ notation.

8. **holographic_codes_koszul thm:hc-koszulness-exact-qec L339-421**: rephrase the theorem to make K4 ⇔ K4 tautology explicit. Drop the (iii) ⇒ (i) circularity. State as "Koszulness is the algebraic incarnation of holographic exact recovery; the **physical** identification with HKLL bulk reconstruction is **structural**, not theorematic."

**P2 — should-fix for completeness**

9. **holo_datum L217-223 + 3DQG L890**: replace "single object viewed three ways" with "three functorial outputs of the bar complex". Mirror in thqg_intro_supplement L156-184.

10. **holo_datum thm:holographic-explicit L1254**: the term "complete invariant" implicit in "the six components are determined by the single datum $c$" is fine *for Vir*. State explicitly: "for Heisenberg, KM at fixed $\fg$, and Vir, the datum is parameter-complete; general completeness is open."

11. **w3_holographic_datum**: this paper inherits the same issues. Audit terminology consistency with the main 3DQG paper after fixes.

**P3 — opportunity for genuine upgrade**

12. **Pursue Path B (symplectic code construction)** — closest to the existing material. The Lagrangian isotropy + dictionary already in `holographic_codes_koszul` could be upgraded to an explicit stabiliser-code construction for at least the Heisenberg case.

13. **Pursue Path C piece**: prove chain-level $E_3$ for $\mathrm{Vir}_{13}$ at the self-dual point (which the manuscript hints is the most structured locus). This would give the cleanest setting for the bulk-boundary $E_3$ equivalence.

---

## Cache write-back

Two recurring patterns from this audit appear ≥2 times across this and prior waves; will append to `/Users/raeez/calabi-yau-quantum-groups/appendices/first_principles_cache.md`:

- **"BTZ is an MC element"** (this audit, plus a related conflation in earlier `holographic_datum_master`): module element vs algebra/Lie element. Type: algebra/module, sub-type of algebra/coalgebra.
- **"Triangle is one object viewed three ways"** (3DQG, holo_datum, thqg_intro_supplement — three locations): construction/narration AP-CY57 in the holographic context.

Cache entry text (to be appended):

```
| 138 | "BTZ is an MC element of the convolution Lie algebra" | BTZ is a Cardy state in the module category | Cardy state in module ≠ MC element in algebra | Module element vs algebra element. The convolution dg Lie algebra contains structural data; the modules contain physical states. | algebra/module | three_dimensional_quantum_gravity.tex L1748; holographic_datum.tex L1748+ |
| 139 | "BBL triangle = one object viewed three ways" | three functorial outputs of the bar complex | source object ≠ functor target | Single source object can have many functorial outputs without BEING those outputs. The relation is functoriality, not identity. | construction/narration (AP-CY57) | three_dimensional_quantum_gravity.tex L890; holographic_datum.tex L217; thqg_introduction_supplement.tex L156 |
```

---

**End of report.** Total ~3,950 words. No edits to manuscript files. No commits.
