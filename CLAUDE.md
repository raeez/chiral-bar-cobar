# CLAUDE.md -- Modular Koszul Duality Programme (Canonical Reference)

## Identity

E_1-E_1 operadic Koszul duality in the homotopical modular chiral realm on algebraic curves. One form (eta = d log(z_1 - z_2)), one relation (Arnold), one object (Theta_A), one equation (D*Theta + 1/2[Theta,Theta] = 0). The primitive object is B^ord(A) = T^c(s^{-1}A-bar): ordered bar, deconcatenation coproduct, R-matrix, Yangian. The symmetric bar B^Sigma is the Sigma_n-coinvariant shadow. Physics IS the homotopy type: A-infinity = scattering, SC^{ch,top} governs the (bulk, boundary) pair, modular L-infinity = genus tower. The five theorems A-D+H are the invariants that survive averaging.

**Bar complex is E_1-coassociative; SC^{ch,top} emerges on the derived center (CRITICAL, corrected 2026-04-12):** The bar complex B^{ord}(A) = T^c(s^{-1}A-bar) is an E_1-chiral coassociative COALGEBRA (over ChirAss^!). It has a differential + deconcatenation coproduct. It does NOT carry SC^{ch,top} structure. The SC^{ch,top} structure (or E_3 with conformal vector) emerges on the DERIVED CENTER Z^{der}_{ch}(A) = ChirHoch*(A,A), computed USING the bar complex as a resolution. The bar complex is the E_1 engine; the derived center is the SC^{ch,top}/E_3 output. thm:bar-swiss-cheese (claiming B(A) is an SC-coalgebra) needs retraction or careful restatement — see FOUND-11. princ:sc-two-incarnations in en_koszul_duality.tex states this correctly.

Three volumes by Raeez Lorgat. Vol I *Modular Koszul Duality* (this repo, ~2,650pp). Vol II *A-infinity Chiral Algebras and 3D HT QFT* (~/chiral-bar-cobar-vol2, ~1,633pp). Vol III *CY Categories, Quantum Groups, and BPS Algebras* (~/calabi-yau-quantum-groups, ~259pp). Total ~4,542pp, 120K+ tests, 3,463 tagged claims. This file is the canonical reference; Vols II/III inherit shared content and add volume-specific material.

**Crystallized programme identity (2026-04-12):** We are studying **holomorphic chiral (factorisation) (co)homology** via **bar and cobar chain constructions** at **various different geometric locations**, hence the **different (modular) operads** at play. The geometry determines the operad, the operad determines the bar complex, the bar complex computes the factorisation (co)homology. The five theorems are structural properties. The shadow tower is the characteristic class data. The E_n circle is the holographic structure.

**The E_n operadic circle (2026-04-12):** E_3(bulk) → E_2(boundary chiral) → E_1(bar/QG) → E_2(Drinfeld center) → E_3(derived center). Each arrow is: restriction to codim-2 defect, ordered bar complex, categorified averaging (Drinfeld center), higher Deligne (derived center). The circle closes for 3d HT theories with conformal vector; without conformal vector, stuck at SC^{ch,top} (the intermediary between E_1-chiral and E_3).

**SC^{ch,top} ≠ E_3 (2026-04-12):** The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, making C-translations Q-exact) = E_3. Without conformal vector: stuck at SC^{ch,top}. thm:topologization in en_koszul_duality.tex PROVED for affine KM V_k(g) at non-critical level k != -h^v (Sugawara explicit). For general chiral algebras with conformal vector (Virasoro, W-algebras): CONJECTURAL (conj:topologization-general), depends on constructing the 3d HT BRST complex. Proof is cohomological (Q-cohomology); for class M, chain-level E_3 may fail.

**Five notions of E_1-chiral algebra (2026-04-12):** (A) strict ChirAss-algebra, (B) A_inf in End^{ch}_A, (C) EK quantum vertex algebra, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}(X). Each has own derived center. (B)↔(C) via Drinfeld associator on Koszul locus. Warning installed at algebraic_foundations.tex warn:multiple-e1-chiral.

**Three Hochschild theories (2026-04-12):** (i) Topological HH: E_1-algebra input → E_2 output (Deligne). (ii) Chiral HH (ChirHoch): E_inf-chiral input → E_inf output, concentrated {0,1,2} (Theorem H). (iii) Categorical HH: dg category input → E_2 with CY shifted Poisson. NEVER conflate. The geometry determines which Hochschild: curve X → chiral, R → topological, CY category → categorical. Constitutional statement in memory/project_hochschild_constitutional_statement.md.

**Architecture (2026-04-12):** E_n chiral algebra theory stays in Vol I (pure algebra/operads). ALL physics moves to Vol II. Vol III provides the geometric source (CY categories → chiral algebras via the E_n circle).

**North star:** platonic_ideal_reconstituted_2026_04_12.md is THE SINGLE REFERENCE for all structural questions.

## HOT ZONE -- Top 10 Repeat Offenders

Read this section BEFORE any Edit. These are the APs that fire repeatedly across waves despite being catalogued. Each entry is an operational template, not prose. Source: ap_recurrence_archaeology_wave12.md. If you only read 80 lines of CLAUDE.md, read these.

### HZ-1. AP126/AP141 (r-matrix level prefix) -- 6 waves, 90+ instances

Template, fill BEFORE writing any r-matrix:

```
family:               [Heis / affine KM / Vir / W_N / Yang rational / Calogero-Moser]
r(z) written:         [formula with level prefix visible]
level parameter:      [k / k+h^v / hbar / c]
AP141 k=0 check:      r(z)|_{level=0} = [value]    required: 0 (trace-form convention)
match?                [Y/N]   <-- must be Y for trace-form; for KZ convention, k=0 gives Omega/(h^v*z) != 0 for non-abelian g (correct: Lie bracket persists)
source:               landscape_census.tex line [N] OR compute engine
FORBIDDEN bare forms: Omega/z (no level), k Omega/z^2
```

Canonical forms (trace-form convention): `r^KM(z) = k*Omega/z`, `r^Heis(z) = k/z`, `r^Vir(z) = (c/2)/z^3 + 2T/z`. KZ equivalent: `r^KM(z) = Omega/((k+h^v)*z)`. After every r-matrix: grep the file for bare `\Omega/z` without level prefix; if any match, STOP.

### HZ-2. AP40 (environment matches tag) -- 5 waves, 70+ instances

Decision tree, answer BEFORE writing `\begin{...}`:

```
Q1: Is there a complete proof here or in cited literature?
    NO  -> \begin{conjecture} + \ClaimStatusConjectured. STOP.
    YES -> Q2
Q2: Backbone main result / supporting / auxiliary?
    main       -> \begin{theorem}
    supporting -> \begin{proposition}
    auxiliary  -> \begin{lemma}
Q3: Self-contained or cited?
    self-contained -> \ClaimStatusProvedHere + \begin{proof}
    cited          -> \ClaimStatusProvedElsewhere + Remark[Attribution]
UNCERTAIN -> default \begin{conjecture}. Downgrade is cheaper than rename.
```

Vol III default: `\begin{conjecture}` regardless. Label prefix follows environment (AP125).

### HZ-3. AP32 (uniform-weight tag on F_g) -- 4 waves, 30+ instances

Every formula of the form `F_g = ... lambda_g ...` or `obs_g = ...` MUST be followed within the same sentence by ONE of:

```
(a) (UNIFORM-WEIGHT)
(b) (ALL-WEIGHT, with cross-channel correction delta F_g^cross)
(c) (g=1 only; ALL-WEIGHT at g=1 is unconditional)
(d) (LOCAL: scope defined in surrounding paragraph, see ref:...)
```

No "in a theorem" loophole: tag required in prose, remarks, and definitions.

### HZ-4. AP1 (kappa from memory) -- 4 waves, 15+ instances

Writing kappa from memory is FORBIDDEN. Before writing ANY kappa expression:

```
Step 1: Identify family (Heis / Vir / KM / W_N / free / coset / SVir / BP / betagamma)
Step 2: Open landscape_census.tex, copy the formula WITH citation comment
Step 3: Paste with comment: % AP1: formula from landscape_census.tex:LINE; k=0 -> VALUE verified
Step 4: Evaluate at two boundary values and write results in comment
```

Quick reference (cross-check census before use):
- KM: `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`; k=0 -> dim(g)/2; k=-h^v -> 0 (critical)
- Vir: `kappa(Vir_c) = c/2`; c=13 -> 13/2 (self-dual)
- Heis: `kappa(H_k) = k`; k=0 -> 0
- W_N: `kappa(W_N) = c*(H_N - 1)` where `H_N = 1 + 1/2 + ... + 1/N`. NOT `H_{N-1}`. Verify at N=2: H_2=3/2, H_2-1=1/2, so kappa(W_2)=c/2 matches Virasoro.

### HZ-5. AP125/AP124 (label prefix and uniqueness) -- 3 waves, 25+ instances

Before writing `\label{foo}`:

```
(i)  Prefix matches environment: thm: theorem, prop: proposition, lem: lemma,
     conj: conjecture, rem: remark, def: definition, eq: equation
(ii) Uniqueness across all three volumes:
     grep -rn '\\label{foo}' ~/chiral-bar-cobar ~/chiral-bar-cobar-vol2 ~/calabi-yau-quantum-groups
     0 matches -> safe. >=1 match -> rename with volume suffix (v1-, v2-, v3-).
```

Downgrade atomicity: when downgrading theorem -> conjecture, rename `thm:foo -> conj:foo` AND update every `\ref{thm:foo}` across three volumes in the SAME tool-call batch. No intermediate commit.

### HZ-6. AP10/AP128 (hardcoded expected values) -- 3 waves, 12+ engines

Every hardcoded expected value in a test file requires a `# VERIFIED` comment citing at least TWO sources from different categories:

```
[DC] direct computation     [LT] literature (paper + eq #)
[LC] limiting case          [SY] symmetry
[CF] cross-family           [NE] numerical (>=10 digits)
[DA] dimensional analysis
```

Engine-test sync check: when correcting an engine formula, derive the new expected value from an INDEPENDENT source, NOT from the corrected engine output. Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### HZ-7. AP113 (bare kappa in Vol III) -- 3 waves, 165 baseline instances

Bare `\kappa` in Vol III is permitted IFF the section begins with a local definition:

```
"In this section we write kappa for kappa_{ch}(H_Lambda) (respectively kappa_{BKM}, kappa_{cat}, kappa_{fiber})."
```

Approved subscripts (closed set): `{ch, cat, BKM, fiber}`. FORBIDDEN: `{global, BPS, eff, total, naive}`.

Decision tree:
- chiral algebra -> `kappa_ch`
- BKM algebra -> `kappa_BKM`
- Euler characteristic -> `kappa_cat`
- lattice/fiber -> `kappa_fiber`

### HZ-8. AP4 (proof after conjecture) -- 3 waves, 40+ instances

Before `\begin{proof}`:

```
Step 1: Look at the nearest preceding \begin{...} within 30 lines
Step 2: theorem/prop/lemma -> proof may follow
        conjecture/heuristic/remark/definition -> STOP, use \begin{remark}[Evidence]
Step 3: ClaimStatus tag check
        ProvedHere -> self-contained proof body
        ProvedElsewhere -> paragraph attributing, NOT re-proof
        Conjectured -> AP40 upstream violation
```

### HZ-9. AP25/AP34/AP50 (four-functor discipline) -- 3 waves, 15+ instances

Write this list before any paragraph mentioning "bar", "cobar", "Koszul dual", or "derived center":

```
% FOUR OBJECTS:
% 1. B(A) = bar coalgebra = T^c(s^{-1} A-bar) with deconcatenation + twist
% 2. A^i = H^*(B(A)) = dual coalgebra (Koszul cohomology of bar)
% 3. A^! = ((A^i)^v) = dual ALGEBRA (linear or Verdier dual)
% 4. Z^der_ch(A) = derived chiral center = Hochschild cochains = bulk
```

FORBIDDEN conflations:
- "bar-cobar produces bulk" (wrong: bar-cobar inverts to A; bulk is Hochschild)
- "Omega(B(A)) is the Koszul dual" (wrong: that is INVERSION)
- "the Koszul dual equals the bar complex" (wrong: bar is coalgebra, dual is algebra)
- "D_Ran(B(A)) is the cobar complex" (wrong: D_Ran is Verdier; cobar is Omega)

### HZ-10. AP29/V2-AP29 (AI slop) -- 4 waves, 40+ instances over 3 zero-tolerance commits

PRE-WRITE mental check: does the sentence start with one of the banned tokens below? If yes, REWRITE before typing.

POST-WRITE grep (mandatory):

```
Banned (case-insensitive): moreover, additionally, notably, crucially, remarkably,
interestingly, furthermore, "we now", "it is worth noting", "worth mentioning",
"it should be noted", "it is important to note", delve, leverage, tapestry,
cornerstone, landscape (as metaphor), journey, navigate (non-geometric)

Em-dash (---, U+2014) FORBIDDEN. Use colons, semicolons, separate sentences.

Hedging ban in math: arguably, perhaps, seems to, appears to. If math clear, state it. If not, mark as conjecture.
```

Three separate cleanup commits in Vol II prove aspirational instructions insufficient. Post-write grep is the only reliable enforcement.

## The Beilinson Principle

"What limits forward progress is not the lack of genius but the inability to dismiss false ideas." Every claim is false until independently verified from primary source. Prefer a smaller true theorem to a larger false one. Every numerical claim requires 3+ genuinely independent verification paths (direct computation, alternative formula, limiting case, symmetry/duality, cross-family, literature+convention, dimensional analysis, numerical evaluation).

**Epistemic hierarchy** (higher wins): (1) Direct computation > (2) .tex source +/-100 lines > (3) Build system > (4) Published literature > (5) concordance.tex > (6) This file > (7) Memory. Before every assertion: "How do I know this? Read the source, computed it, or assumed it?" If assumed, stop and verify.

## E1-First Prose Architecture (MANDATORY)

The ordered bar B^ord(A) is the primitive object of this programme. Every chapter, every section, every theorem presentation MUST construct the E1 ordered story first, then derive the symmetric story by averaging. The pattern:

1. CONSTRUCT the E1 object (B^ord, r(z), Theta_A in g^{E1}, the matrix-valued curvature).
2. EXHIBIT the E1 structure (deconcatenation coproduct, R-matrix, Yangian).
3. APPLY the averaging map av: g^{E1} -> g^mod (lossy Sigma_n-coinvariant projection).
4. DERIVE the symmetric result (kappa = av(r(z)), obs_g = kappa*lambda_g, the shadow tower).

NEVER state a symmetric-bar result (kappa, obs_g, shadow tower) without first showing the E1 object it projects from. NEVER frame the five theorems as "concerning the symmetric bar" — they EXTRACT the Sigma_n-invariant content of the ordered bar. The symmetric bar is the shadow; the ordered bar generates.

The convolution algebra has two levels: g^{E1}_A (the primitive, carrying the R-matrix) and g^mod_A (the coinvariant shadow, carrying only kappa). Theta_A lives in g^{E1}_A; everything in this monograph is its Sigma_n-coinvariant projection.

## The Five Objects (NEVER CONFLATE)

A (algebra) -- B(A) (bar coalgebra) -- A^i=H*(B(A)) (dual coalgebra) -- A^!=((A^i)^v) (dual algebra) -- Z^der_ch(A) (derived center = bulk). Omega(B(A))=A is INVERSION. A^! from VERDIER duality. Bulk from HOCHSCHILD cochains. B^ord is the primitive; B^Sigma is the av-image shadow. "The bar complex" without qualifier means B^ord; B^Sigma only when factorization picture needed.

## Key Constants

kappa(KM)=dim(g)(k+h^v)/(2h^v). kappa(Vir)=c/2. kappa(Heis)=k. kappa(W_N)=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j. Vir^!=Vir_{26-c}. Self-dual at c=13. kappa+kappa'=0 (KM/free), 13 (Vir). QME: hbar*Delta*S+(1/2){S,S}=0. sl_2 bar H^2=5 (not 6). Desuspension: |s^{-1}v|=|v|-1, NOT +1. eta(q)=q^{1/24}*prod(1-q^n). Bar propagator d log E(z,w): ALWAYS weight 1. Prime form: section of K^{-1/2} boxtimes K^{-1/2}. FM_n(X): blowup along diagonals, NOT complement. Grading: COHOMOLOGICAL (|d|=+1). Curved A-inf: m_1^2(a)=[m_0,a]. Bar d^2=0 always; curvature appears as m_1^2 != 0.
alpha_g = 2*rank + 4*dim*h^v (universal Hilbert-series growth, all simple types). d_alg in {0,1,2,inf} (depth gap: 3 impossible, prop:depth-gap-trichotomy). kappa(BP)+kappa(BP^!)=98/3 (self-dual k=-3).

## True Formula Census

Canonical source for every formula. Never write from memory; cite this census or landscape_census.tex. Each entry has (canonical form, two sanity checks, wrong variants). Source: true_formula_census_draft_wave12.md (C1-C31 full entries).

**C1. Heisenberg kappa.** `kappa(H_k) = k`. Checks: k=0 -> 0; k=1 -> 1 (matches c_Heis(1)=1). Wrong: k/2 (Vir pattern-match), k*dim/(2h^v) (KM paste).

**C2. Virasoro kappa.** `kappa(Vir_c) = c/2`. UNIQUE family with kappa=c/2. Checks: c=0 -> 0; c=13 -> 13/2 self-dual. Wrong: c (drop 1/2); c/24 (anomaly confusion).

**C3. Affine KM kappa.** `kappa(V_k(g)) = dim(g)(k+h^v)/(2h^v)`. Checks: k=0 -> dim(g)/2 (NOT zero); k=-h^v -> 0 (critical). Wrong: dim(g)*k/(2h^v) (Sugawara shift dropped); k/2 (Heis paste); c/2 (Vir paste).

**C4. Principal W_N kappa.** `kappa(W_N) = c*(H_N - 1)`, `H_N = sum_{j=1}^{N} 1/j`. Checks: N=2 -> H_2-1=1/2 so kappa(W_2)=c/2=kappa_Vir; N=3 -> 5c/6. Wrong: c*H_{N-1} (AP136 off-by-one: at N=2 gives c, wrong by factor 2); c*H_N - 1 (parenthesization); (c/2)*H_N.

**C5. Fermionic bc central charge.** `c_bc(lambda) = 1 - 3(2*lambda-1)^2`. Checks: lambda=1/2 -> 1 (single Dirac fermion); lambda=2 -> -26 (reparam ghost). Wrong: -1+3(2*lambda-1)^2 (sign flip); 1-3(2*lambda+1)^2 (inner sign).

**C6. Bosonic betagamma central charge.** `c_betagamma(lambda) = 2(6*lambda^2 - 6*lambda + 1)`. Checks: lambda=1/2 -> -1 (symplectic boson); lambda=2 -> 26 (matter ghost, c_bg + c_bc = 0). Wrong: 2(6*lambda^2+6*lambda+1) (middle sign).

**C7. bc/betagamma complementarity.** `c_betagamma(lambda) + c_bc(lambda) = 0`. Checks: lambda=1 -> 2+(-2)=0; lambda=2 -> 26+(-26)=0 (string ghost cancellation). Wrong: `= c` (Koszul conductor confusion); `- = 0` (sign).

**C8. Virasoro self-dual point.** Under `c -> 26-c`: `kappa+kappa' = 13`. Self-dual at c=13 (NOT c=26, NOT c=0). Wrong: "self-dual at c=26" (confusing c+c'=26 with fixed point).

**C9. Affine KM classical r-matrix.** Two equivalent conventions coexist: (i) trace-form `r(z) = k*Omega/z` where Omega is the inverse Killing form Casimir (d-log absorption of OPE double pole; level prefix k MANDATORY, AP126); (ii) KZ normalization `r(z) = Omega/((k+h^v)*z)` (collision-residue dualization; Sugawara denominator). Bridge identity: `k*Omega_tr = Omega/(k+h^v)` at generic k. Checks (trace-form): k=0 -> r=0 (abelian limit, double pole vanishes); k=-h^v -> critical level. Checks (KZ): k=0 -> Omega/(h^v*z) != 0 (Lie bracket persists for non-abelian g); k=-h^v -> diverges (Sugawara singularity). Averaging: av(k*Omega/z) = k*dim(g)/(2h^v) = kappa_dp (double-pole channel); full kappa = av(r) + dim(g)/2 (Sugawara shift from simple-pole self-contraction, see C13). Wrong: Omega/z (bare, AP126 -- MOST VIOLATED); k*Omega/z^2 (double pole).

**C10. Heisenberg classical r-matrix.** `r^Heis(z) = k/z`. Checks: k=0 -> 0; av(k/z)=k=kappa. Wrong: k/z^2 (OPE pole confusion); 1/z (level stripped).

**C11. Virasoro classical r-matrix.** `r^Vir(z) = (c/2)/z^3 + 2T/z`. Cubic + simple, NOT quartic. Check: OPE has quartic pole; d-log absorbs one (AP19). Wrong: (c/2)/z^4 (forgets absorption); c/z^3 (drops 1/2 and 2T/z).

**C12. r-matrix/OPE pole absorption.** `pole_r = pole_OPE - 1` via d-log absorption. Heis OPE ~ 1/z^2 -> r ~ 1/z; Vir OPE ~ 1/z^4 -> r ~ 1/z^3.

**C13. Averaging map identity.** `av(r(z)) = kappa(A)` at degree 2 for abelian algebras (Heisenberg, free fields): direct. For NON-ABELIAN KM (trace-form convention r=k*Omega/z): `av(r(z)) = k*dim(g)/(2h^v) = kappa_dp` (double-pole channel only). The full kappa includes the Sugawara shift: `kappa(V_k(g)) = av(r(z)) + dim(g)/2 = dim(g)*(k+h^v)/(2h^v)`. The dim(g)/2 term is kappa_sp, the simple-pole self-contraction through the adjoint Casimir eigenvalue 2h^v (proved at kac_moody.tex:1430-1474, introduction.tex:1182, higher_genus_modular_koszul.tex:3060). Wrong: `av(r)=k` for KM (bare level, forgets trace); `av(r)=kappa` for non-abelian KM without Sugawara shift (FM11).

**C14. Bar complex uses augmentation ideal.** `B(A) = T^c(s^{-1} A-bar)`, `A-bar = ker(epsilon)`. NOT `T^c(s^{-1} A)` (AP132). NOT `T^c(s A-bar)` (AP22). NOT `T(s^{-1} A-bar)` (tensor ALGEBRA loses deconcatenation).

**C15. Desuspension grading.** `|s^{-1} v| = |v| - 1`. Mnemonic: bar = down = desuspension = s^{-1}. Wrong: `+1` (suspension direction).

**C16. E_8 fundamental dimensions.** `{248, 3875, 30380, 147250, 2450240, 6696000, 146325270, 6899079264}`. Adjoint = omega_1 = 248. Sum = 7056003287. Wrong: 779247 (not any E_8 irreducible, Wave 10-8 error); 3875 as adjoint (confusing omega_2 with omega_1). Source: `compute/lib/bc_exceptional_categorical_zeta_engine.py::FUNDAMENTAL_DIMS['E8']`.

**C17. W_N conformal weight range.** Generators at `s in {2, 3, ..., N}`. N-1 generators, highest weight N. Checks: W_2 -> {2} = Vir; W_3 -> {2,3}. Wrong: `{2,...,N+1}` (extra phantom field); `{1,...,N}` (includes weight-1 field).

**C18. Koszul complementarity per family.** `K(A) = kappa(A)+kappa(A^!)`: 0 for KM/Heis/lattice/free; 13 for Vir; 250/3 for W_3; 196 for Bershadsky-Polyakov. NOT universal 0 (AP24).

**C19. Harmonic number.** `H_N = sum_{j=1}^{N} 1/j`. H_1=1, H_2=3/2. `H_{N-1} != H_N - 1`: at N=2, H_1=1 but H_2-1=1/2 (AP136).

**C20. Bershadsky-Polyakov Koszul conductor.** `K_BP = c(k) + c(-k-6) = 196`. Self-dual level k=-3. Wrong: K_BP=76 (corrected in Wave 7); K_BP=2 (AP140, confusing with ghost constant C_{(2,1)}=2).

**C21. Igusa cusp form / BKM kappa.** `wt(Phi_10) = 10 = 2*kappa_BKM(K3xE)`, so `kappa_BKM(K3xE) = 5`. Phi_10 = Delta_5^2. Wrong: kappa_BKM = 10 (identifies kappa with full weight); kappa_BKM = 2.

**C22. Dedekind eta.** `eta(tau) = q^{1/24} * prod_{n>=1}(1-q^n)`. Prefactor q^{1/24} ESSENTIAL for modular weight 1/2 transformation. Wrong: dropping q^{1/24}; q^{1/12} prefactor.

**C23. Bicoloured partitions.** `1/eta^2 = q^{-1/12} sum p_{-2}(n) q^n`, coefficients `(1, 2, 5, 10, 20, ...)` (OEIS A002513). Wrong: triangular (1,3,6,10,...) (AP135); ordinary partitions (1,1,2,3,5,...).

**C24. Cauchy integral normalization.** `[z^{n-1}] f(z) = (1/(2*pi*i)) * contour_integral f(z) dz/z^n`. Wrong: 1/(2*pi) (missing i gives zero for real integrands, AP120). Sanity: F_1 = kappa/24.

**C25. MC equation.** `d*Theta + (1/2)[Theta, Theta] = 0`. QME: `hbar*Delta*S + (1/2){S,S} = 0`. Wrong: drop the 1/2 (except odd parity); sign flip.

**C26. G/L/C/M classification.** G (r=2, Heis), L (r=3, aff KM), C (r=4, betagamma), M (r=inf, Vir/W_N). Shadow depth != Koszulness.

**C27. Chiral Hochschild of Vir.** `ChirHoch^*(Vir_c)` concentrated in degrees {0,1,2}; polynomial Hilbert series. This is AMPLITUDE (topological), NOT virtual dimension (arithmetic) (AP134). NOT C[Theta] (AP94). NOT Gelfand-Fuchs (GF infinite, AP95).

**C28. Arnold form vs KZ connection.** KZ: `nabla_KZ = d + sum r_{ij} dz_{ij}` with `dz_{ij}`, NOT `d log z_{ij}`. Arnold form `omega_{ij} = d log(z_i - z_j)` is a bar-construction coefficient, NOT the connection form (AP117). For affine KM: `r_{ij}(z) = k*Omega_{ij}/z`.

**C29. Genus-1 period matrix collapse.** `(Im Omega)^{-1}` is a gxg MATRIX at g>=2; degenerates to scalar 1/Im(tau) at g=1. Write formulas in full matrix form; verify at g=2 (AP118).

**C30. Delta discriminant.** `Delta = 8*kappa*S_4`. Finite tower iff Delta=0; for kappa!=0 iff S_4=0. LINEAR in kappa (NOT quadratic, AP21). Heis: S_4=0, Delta=0, class G. Vir: S_4!=0, Delta!=0, class M.

**C31. Bershadsky-Polyakov complementarity conductor.** `kappa(BP) + kappa(BP^!) = 98/3` (NOT 1/3). `varrho_BP = 1/6`. Checks: K_BP = c(k) + c(-k-6) = 196 (cross-check C20); at self-dual level k=-3, kappa(BP) = 49/3. Wrong: kappa(BP)+kappa(BP^!)=1/3 (off by factor 98); varrho_BP=1/2 (confusing with rank-1 value).

## Wrong Formulas Blacklist

Concrete forbidden forms repeatedly emitted. Source: wrong_formulas_blacklist_wave12.md (B1-B51). Grep these after every .tex write; any match = fix immediately.

**r-matrix / level prefix**

- B1. `r(z) = \Omega/z` (bare, no level). CORRECT: trace-form `r(z) = k\Omega/z` or KZ `r(z) = \Omega/((k+h^\vee)z)`. AP126. Regex: `r\(z\)\s*=\s*\\Omega\s*/\s*z` (catches bare form without any level prefix or Sugawara denominator).
- B2. `r^Vir(z) = (c/2)/z^4` (quartic). CORRECT: `(c/2)/z^3 + 2T/z`. AP19/AP21.
- B3. `r^Vir(z) = (c/2)/z^2`. CORRECT: cubic + simple. AP19/AP27.
- B4. `\Omega\,d\log z` (no k prefix). CORRECT: `k\Omega\,d\log z`. AP117/AP126.

**central charges / kappa**

- B5. `c_{bc}(\lambda) = 2(6\lambda^2 - 6\lambda + 1)` (bosonic form labelled fermionic). CORRECT: `c_{bc} = 1 - 3(2\lambda-1)^2`. AP137.
- B6. `c_{\beta\gamma}(\lambda) = 1 - 3(2\lambda-1)^2` (fermionic form labelled bosonic). CORRECT: `c_{bg} = 2(6\lambda^2-6\lambda+1)`. AP137.
- B7. `\kappa(W_N) = c*H_{N-1}`. CORRECT: `c*(H_N - 1)`. AP136.
- B8. `\kappa = c/2` unqualified. CORRECT: specify family; `c/2` is Virasoro ONLY. AP1/AP39.
- B9. `\kappa + \kappa' = 0` unscoped. CORRECT: 0 for KM/free; 13 for Vir; family-specific otherwise. AP24/AP8.
- B10. `\kappa = S_2/2`. CORRECT: `S_2 = \kappa` (no factor of 2). Only Vir has kappa=c/2. AP39.
- B11. `av(r(z)) = \kappa` for non-abelian KM. CORRECT: `av(r(z)) + dim(g)/2 = kappa(V_k(g))`. FM11.
- B12. Bare `\kappa` in Vol III. CORRECT: subscripted `\kappa_{ch|cat|BKM|fiber}`. AP113.
- B13. `\kappa_{global|BPS|eff|total|naive}` in Vol III. CORRECT: approved set only. AP113.

**bar complex / suspension**

- B14. `T^c(s^{-1} A)`. CORRECT: `T^c(s^{-1} \bar A)`. AP132.
- B15. `T^c(s A)` (bare suspension). CORRECT: `T^c(s^{-1} \bar A)`. AP22/AP45.
- B16. `|s^{-1} v| = |v| + 1`. CORRECT: `|v| - 1`. AP22/AP45.
- B17. `\eta(q) = \prod(1-q^n)` (missing q^{1/24}). CORRECT: `q^{1/24}*prod(1-q^n)`. FM13.

**boundaries / combinatorics**

- B18. W_N weights `{2,...,N+1}` (N generators). CORRECT: `{2,...,N}` (N-1 generators).
- B19. `H_N = \sum_{j=1}^{N-1} 1/j`. CORRECT: upper limit N. AP116.
- B20. `C_n` counts binary trees with n leaves. CORRECT: with n+1 leaves (n internal nodes). AP133.

**numerical data**

- B21. E_8 fundamental = 779247. Not any E_8 irreducible. FM5.
- B22. `dim H^2(B(sl_2)) = 6`. CORRECT: 5.
- B23. Genus-2 stable graphs = 6. CORRECT: 7. AP123.
- B24. `1/\eta(q)^2` coefficients (1,3,6,10,...). CORRECT: (1,2,5,10,20,...) bicoloured partitions. AP135.
- B25. `K_{BP} = 2`. CORRECT: `K_{BP} = 196`. AP140.

**scope / quantifier**

- B26. `obs_g = \kappa * \lambda_g` untagged. CORRECT: append (UNIFORM-WEIGHT) or (ALL-WEIGHT + delta F_g^cross). AP32.
- B27. `A \iff B` in theorem where only forward proved. CORRECT: `\implies` + Remark on converse. AP36.
- B28. "k=0 r-matrix vanishes and algebra fails Koszulness" for affine KM. CORRECT: k=0 is abelian limit, still Koszul; k=-h^v is critical, Koszulness fails. FM4.
- B29. Theorem C^{E1} with `n` free on RHS but only `g` on LHS. CORRECT: fully quantify n with `2g-2+n > 0`. AP139.

**macros / labels / LaTeX**

- B30. `\end{definition>` (> instead of }). Regex: `\\end\{[^}]*>`. FM7.
- B31. `\begin{theorem>`. Symmetric.
- B32. `\cW` in standalone without `\providecommand`. FM6.
- B33. `Part~IV`, `Chapter~12` hardcoded. CORRECT: `\ref{part:...}`. V2-AP26/FM10.
- B34. Duplicate `conj:kappa-bps-universality` across Vol I and Vol III. AP124/FM15.
- B35. `\begin{conjecture} \label{thm:foo}` prefix mismatch. AP125/FM14.
- B36. `\cite{GeK98}` without bibitem. Emits [?]. AP28.

**numerical coefficients**

- B37. `F_2 = 1/5760` or `7/2880`. CORRECT: `7/5760`. FM21.
- B38. `\frac{1}{2\pi}\oint` (missing i). CORRECT: `\frac{1}{2\pi i}\oint`. AP120.
- B39. KM r-matrix not vanishing at k=0. AP126/AP141.

**prose hygiene**

- B40. Markdown in LaTeX: backtick numerals, **bold**, _italic_. CORRECT: $...$, \textbf, \emph. AP121.
- B41. Em-dash (`---` or Unicode U+2014). CORRECT: colon, semicolon, separate sentences.
- B42. AI slop vocabulary: `notably, crucially, remarkably, interestingly, furthermore, moreover, delve, leverage, tapestry, cornerstone`.

**depth / dimension / fiber-base**

- B43. `d_alg(Vir) = 3`. CORRECT: `d_gen(Vir) = 3`, `d_alg(Vir) = inf` (class M). AP131/FM18.
- B44. Bare `d(Vir) = 3` without `gen`/`alg` subscript. AP131.
- B45. `vdim ChirHoch^*(A) = 2`. CORRECT: amplitude [0,2], NOT vdim. AP134/FM17.
- B46. `\omega_g = d\tau`. CORRECT: `\omega_g = c_1(\lambda)` on M-bar_g; d\tau lives on the curve, not on moduli. AP130/FM19.

**grading / curved**

- B47. `[m,[m,f]] = (1/2)[[m,m],f]` at even `||m||`. CORRECT: tautological at even; identity requires odd. AP138.
- B48. `m_1^2 = 0` universally in curved A-inf. CORRECT: `m_1^2(a) = [m_0, a]`. AP46.
- B49. `d^2 = kappa * omega_g` stated as bar differential. CORRECT: `d^2_bar = 0` always; `d^2_fib = kappa*omega_g` is the FIBERWISE statement at g>=1. AP46/AP87.

**promotion / sector**

- B50. `dim SC^mix_{k,m} = (k-1)! * m!`. CORRECT: `(k-1)! * C(k+m, m)` (binomial). AP89.
- B51. `B_{SC}(A)` for one-colour input. CORRECT: SC is two-coloured, use promotion `A -> (A,A)`. AP86.
- B52. `kappa(BP) + kappa(BP^!) = 1/3`. CORRECT: `98/3`. AP140/C31.
- B53. "Koszul duality over a point is Koszul duality over P^1". FALSE. Formal disk recovers point; P^1 has nontrivial global topology. AP142. Regex: `over a point.*is.*over.*P\^1|over a point.*is.*over.*\\mathbb\{P\}`
- B54. `B(A)` is a coalgebra over `SC^{ch,top}` / "the bar complex presents the Swiss-cheese algebra." FALSE. B(A) is an E_1 coassociative coalgebra. SC^{ch,top} emerges in the chiral derived center pair (C^bullet_{ch}(A,A), A). AP165. Regex: `bar.*presents.*Swiss|coalgebra over.*\\SCchtop|\\SCchtop.*coalgebra`
- B55. "The bar differential is the closed color" / "the bar coproduct is the open color." FALSE. d_B and Delta make B(A) an E_1 dg coalgebra, NOT an SC two-color datum. AP165.
- B56. "Curved SC^{ch,top}-algebra" for the genus >= 1 bar complex. FALSE. It is a curved A_infinity-chiral algebra. The curvature d^2_{fib} = kappa * omega_g is on the A_infinity structure, not on an SC structure. AP165.
- B57. `(SC^{ch,top})^! ~ SC^{ch,top}` / "SC is Koszul self-dual." FALSE. SC^! = (Lie, Ass, shuffle-mixed). The closed dims are (n-1)! vs 1. The duality FUNCTOR is an involution but the OPERAD is not self-dual. AP166.
- B58. "E_3-chiral" for the topologized derived center. FALSE. The conformal vector kills the chiral direction; the result is E_3-TOPOLOGICAL. AP168.
- B59. "Topologization proved for all chiral algebras with conformal vector." FALSE. Proved only for affine KM V_k(g) at non-critical level. General case conjectural (conj:topologization-general). AP167.
- B60. "A^! is an SC-algebra." FALSE. A^! is an SC^!-algebra = (Lie, Ass)-algebra. The closed color is Lie (Sklyanin bracket), not Com. AP172.
- B61. "Chiral QG equivalence for all four families." FALSE scope inflation. Proved abstractly on Koszul locus; verified concretely only for sl_2 Yangian + affine KM. Elliptic partial. Toroidal absent. AP174.
- B62. `Delta_z(T) = T⊗1 + 1⊗T + (1/Psi)(J⊗J)`. WRONG Miura coefficient. CORRECT: `(Psi-1)/Psi`. The 1/Psi error agrees accidentally at Psi=2. Derived from Delta_z(psi_2) - (1/(2Psi))Delta_z(J)^2 where the subtraction removes 1/Psi from the coefficient. AP128/FM31. Regex: `1/\\Psi.*J\s*\\otimes\s*J` without `Psi\s*-\s*1`.
- B63. `nabla = d + A` with flat section `dPhi = +A*Phi`. INCONSISTENT. Correct: `nabla = d - A` gives `nabla(Phi)=0 => dPhi = A*Phi`. FM29. Regex: `\\nabla\s*=\s*d\s*\+\s*` in ANY context where flat sections use `dPhi = +A*Phi`.
- B64. Belavin r-matrix via Weierstrass zeta `zeta(z) = theta_1'/theta_1 + 2*eta_1*z`. WRONG: extra linear term breaks CYBE. Correct: Pauli decomposition `sum w_a sigma_a tensor sigma_a / 2`. FM30.
- B65. "Degeneration tau->i*inf recovers rational r-matrix." MISLEADING. Degeneration is TWO-STEP: elliptic -> trigonometric (XXZ) at tau->i*inf, then -> rational at z->0. FM30.
- B62. `S_2 = c/12` for Virasoro. CORRECT: `S_2 = \kappa = c/2`. The c/12 is the lambda-bracket divided-power coefficient (c/2)/3!, NOT the shadow invariant. AP177.
- B63. `S_4 \sim 2/(5c^2)` at large c. CORRECT: `S_4 \sim 2/c^2`. The 10/(5c^2) = 2/c^2, not 2/(5c^2). AP178.
- B64. RETRACTED (degree is correct; arity banned). AP176.
- B65. RETRACTED (degree is correct; arity banned). AP176.
- B66. RETRACTED (degree is correct; arity banned). AP176.
- B67. RETRACTED (degree is correct; arity banned). AP176.
- B68. "S_2 = c/12, which is the Virasoro central charge itself." DOUBLE ERROR: S_2 = c/2 (not c/12), and the central charge is c (not c/12). AP177.
- B69. `pi_3(BU) = \Z`. CORRECT: `pi_3(BU) = 0` (Bott periodicity: pi_{odd}(BU) = 0). Confusion with pi_3(U) = Z. AP181.
- B70. `\kappa_{\mathrm{ch}} = h^{1,1}` for local surfaces. CORRECT: `\kappa_{\mathrm{ch}} = \chi(S)/2`. These differ when h^{0,2} != 0 (e.g., K3: h^{1,1}=20 but chi/2=12). AP182.
- B71. McKay quiver of Z_3 = K_{3,3}. CORRECT: 3 copies of the oriented 3-cycle. K_{3,3} is undirected bipartite. AP183.
- B72. "Excision of [0,1] at t gives B(A) tensor B(A)." CORRECT: excision gives B_L tensor_A B_R = B(A) (one copy, tensor over A). Coproduct is Delta: B(A) -> B(A) tensor B(A) (two copies, plain tensor). AP184.
- B73. "pi_4(BU) = Z provides native E_2 for CY_4." CORRECT: pi_4(BU) = Z is the obstruction GROUP, not a guarantee. AP185.

## Opus 4.6 Quirks and Failure Modes

Model-specific failure patterns observed across ~100 Opus 4.6 agent invocations. These are not generic anti-patterns (see AP catalog below) but recurrent behaviours of this specific model on this specific manuscript. Source: opus_46_failure_modes_wave12.md (FM1-FM22).

**FM1. Generic-formula reaching ("pretty version" attractor).** Opus falls back to the canonical textbook form when memory is uncertain. For affine KM, training-data weight makes `Omega/z` the default; the level-prefixed `k*Omega/z` is less prevalent. Evidence: AP126/AP141, 42+ instances. Counter: append to every r-matrix prompt: "After writing ANY r-matrix, substitute k=0 and verify r vanishes. Do not proceed until k=0 -> r=0."

**FM2. Level-prefix dropping on summarisation.** When Opus summarises a displayed formula from an earlier file read, it omits scalar prefactors even if the source had them. Lost prefixes: k, c/2, kappa, 1/(2*pi*i). Counter: re-Read the source lines verbatim before typing; do not rely on context cache.

**FM3. Bosonic/fermionic conformal-anomaly conflation.** `c_bg` and `c_bc` look structurally similar (both polynomial in lambda with centre at 1/2) and satisfy c_bg+c_bc=0. Opus swaps them under pressure. Counter: after writing any ghost central charge, substitute lambda=2 AND lambda=1 and verify c_bc(2)=-26, c_bg(2)=+26, sum=0 pointwise.

**FM4. k=0 vs k=-h^v confusion at Kac-Moody.** Opus conflates the abelian limit k=0 (where r(z)=0, algebra becomes classically trivial, still Koszul) with the critical level k=-h^v (where centre jumps, not Koszul). Both "destroy the r-matrix" loosely. Counter: before any KM limit statement, emit a two-row table distinguishing the two.

**FM5. Wrong fundamental Lie-algebra dimensions.** Opus generates plausible dimensions not in the actual irreducible list. Example: 779247 for E_8 is not any irreducible. Counter: grep `compute/lib/` for canonical value BEFORE writing. If no match, refuse the numerical value and use the symbolic name `V_{omega_1}(E_8)`.

**FM6. Undefined macros in standalone extraction.** Monograph macros (`\cW`, `\hol`, `\Ran`, `\FM`, `\chHoch`) are not inherited by standalone .tex extractions. Counter: after producing any standalone, grep for `\\[a-zA-Z]+` control sequences and cross-check against the standalone's preamble.

**FM7. LaTeX structural typo `\end{definition>`.** Opus occasionally produces `}` -> `>` on closing environments. Passes visual inspection; fails at compile time. Counter: after every Edit to a .tex file, grep `\\end\{[^}]*>` (and symmetric `\\begin\{[^}]*>`) on the file.

**FM8. Universal-quantifier drift on uniform-weight theorems.** Opus writes "for all genera" for Theorem D without the scope tag. Counter: mandate the three-line template before any obs_g or F_g equation (scope, tag, equation).

**FM9. Harmonic-number off-by-one.** Opus confuses `H_{N-1} = sum_{j=1}^{N-1} 1/j` with `H_N - 1 = sum_{j=2}^{N} 1/j`. At N=2, H_1=1 but H_2-1=1/2. CLAUDE.md itself had this error. Counter: after any harmonic-number shift, evaluate at N=2 AND N=3 and compare numerically.

**FM10. Hardcoded part number drift (`Part~IV` vs `\ref{part:...}`).** Cross-volume references as hardcoded roman numerals break silently on reorganisation. Counter: after any Edit, grep `Part~[IVX]+|Chapter~[0-9]+` in the file and replace with `\ref{part:...}`.

**FM11. Sugawara shift missing in av(r(z)) = kappa.** For abelian Heisenberg, `av(r) = kappa` holds cleanly. For non-abelian KM, `av(r) + dim(g)/2 = kappa(V_k(g))`. Opus writes the abelian form universally. Counter: before writing av(r)=kappa, state the family (abelian vs non-abelian).

**FM12. Mid-response truncation on long audit tasks.** Opus truncates between fix and report when both are requested in the same turn. Counter: separate fix execution from report writing across two tool calls.

**FM13. Auto-completion to the majority-variant.** Opus auto-completes to the most common training-data form even when the manuscript uses a different convention. Example: `eta(q) = prod(1-q^n)` (missing q^{1/24}). Counter: break the formula across multiple lines and annotate each term's convention.

**FM14. AP125 label/environment mismatch on tag changes.** Downgrading a theorem to a conjecture changes `\begin{theorem}` to `\begin{conjecture}` but forgets to rename `thm:foo` to `conj:foo`. Counter: atomic 3-step edit -- rename environment, rename label, grep-and-replace all refs, in the same tool-call batch.

**FM15. Duplicate labels across volumes.** Parallel agents independently create labels with the same natural name across volumes. Counter: before creating `\label{foo}`, grep all three volumes; if match, prefix with v1/v2/v3.

**FM16. Silent kappa-family conflation.** Opus picks kappa from the most recently-mentioned family when context shifts. Counter: every kappa formula carries an explicit family superscript; bare `\kappa` forbidden in mathematical contexts.

**FM17. Amplitude/dimension conflation for ChirHoch.** Opus conflates "cohomological amplitude [0,2]" (topological) with "virtual dimension 2" (arithmetic). Counter: any sentence mentioning ChirHoch and a numerical invariant must choose explicitly.

**FM18. Generating-depth vs algebraic-depth conflation.** `d_gen(Vir) = 3` (m_3 generates recursively) but `d_alg(Vir) = inf` (class M). Counter: every depth statement carries the subscript `gen` or `alg`. Refuse bare `d(...)`.

**FM19. Fiber-base confusion: forms on Sigma vs classes on M-bar_g.** `d\tau` is a form on the elliptic curve; `omega_g = c_1(lambda)` is a class on moduli space. Counter: before writing `omega_g = [expression]`, state the space each side lives on.

**FM20. Iff-drift.** Opus writes "iff" when the converse is obvious-looking but not proved. Counter: before `\iff`, emit a two-line template: "Forward: ... proved in ___. Reverse: ... proved in ___ OR CONJECTURED."

**FM21. Dimensional analysis reconstruction with wrong prefactor.** Opus gets powers right but numerical prefactors (1/2, 1/24, 1/(2*pi*i), 7/5760) wrong. Counter: for any numerical coefficient in {F_g, lambda_g, Bernoulli numbers, Faber-Pandharipande values}, Read the canonical source file in compute/lib/ before writing.

**FM22. Koszul conductor numerical substitution errors.** Opus conflates global Koszul conductor `K = c + c'` with local constants from the same derivation (ghost numbers, grading shifts). Example: K_BP=2 instead of 196. Counter: for any Koszul conductor, first write `K = c + c'`, substitute the two central charges, then evaluate.

**FM23. Local-global conflation on curves ("over a point = over P^1").** Opus identifies Koszul duality over a point with Koszul duality over P^1, collapsing the chain point <- D -> A^1 -> P^1. Training data favours the slogan "genus 0 = classical" without distinguishing which genus-0 space (formal disk, affine line, projective line). THREE independent errors: (1) a homotopy retract is DATA, not an identity—relating A^1 to a point requires specifying the retraction and transfer maps; (2) the formal disk D is not a point—the thickening carries geometric content (completion, growth conditions) that may not be invisible to Koszul duality; (3) A^1 already has Arnold relations and FM compactifications in H*(Conf_n(A^1)); P^1 adds compactness and different global topology. Counter: before writing ANY comparison between "over a point" and "over a curve", name the specific space (point, D, A^1, P^1, general X), state the comparison data (retraction, localization, formal thickening), and explicitly state whether the comparison is on-the-nose or requires extra structure. Refuse unqualified "is".

**FM24. B-cycle monodromy i^2 error.** When hbar contains a factor of pi*i (from a non-standard convention), the formula q = e^{2*pi*i*hbar} gives q = e^{2*pi*i*pi*i/(k+2)} = e^{-2*pi^2/(k+2)}, which is a REAL number less than 1, not a root of unity. The i^2 = -1 turns an imaginary exponential into a real exponential. This error propagates silently because q still "looks like" a parameter. Counter: after defining q = e^{2*pi*i*hbar}, substitute a specific integer k and verify q is on the unit circle (|q| = 1).

**FM25. The SC^{ch,top} disaster of 2025-2026 (Opus 4.6 structural confabulation).** Opus constructed an elaborate but FALSE framework claiming B(A) is an SC^{ch,top}-coalgebra. The chain of errors:

(1) WRONG: "The bar differential is the closed/holomorphic color of SC." TRUTH: The bar differential d_B comes from the chiral product (OPE residues at FM boundary strata). It is the differential of a dg coalgebra over (ChirAss)^!, NOT a "color" of SC. Having operations that USE FM_k(C) geometry does not make d_B an "E_2 color" — it is a single degree-1 map, not a parametrized family of operations.

(2) WRONG: "The deconcatenation coproduct is the open/topological color of SC." TRUTH: Deconcatenation is the cofree tensor coalgebra structure on T^c(V). It is coassociative. This makes B(A) an E_1-coassociative coalgebra. It is NOT a separate "color" of a two-colored operad.

(3) WRONG: "Together, d_B and Delta make B(A) an SC-coalgebra." TRUTH: A dg coassociative coalgebra (differential + coproduct) is a SINGLE-colored E_1 dg coalgebra. Having two structures does not make it two-colored. SC is two-colored (bulk + boundary); B(A) is one object, not a pair.

(4) WRONG: "The SC structure on B(A) is dual to the SC structure on (Z^{der}(A), A)." TRUTH: B(A) is an INPUT to the Hochschild computation. The derived center C^bullet_ch(A,A) is computed FROM B(A) via the convolution Hom(B(A), A). The SC structure emerges in the OUTPUT (the derived center pair), not on the INPUT (the bar complex). The passage B(A) → C^bullet_ch(A,A) is the Hochschild construction, not an operadic duality.

(5) WRONG: "E_1-chiral = E_1-topological (on R)." TRUTH: E_1-chiral means operations from ordered configurations on a CURVE (2-real-dimensional, holomorphic structure). E_1-topological means operations from Conf_k(R) (1-real-dimensional). A chiral algebra on a curve X is a factorization algebra on a real 2-manifold sensitive to holomorphic structure. Calling the bar complex "E_1" without "chiral" conflates these. The bar complex is over (ChirAss)^!, NOT (Ass)^!.

(6) WRONG: "The Steinberg analogy: B(A) presents SC as the Steinberg variety presents the Hecke algebra." TRUTH: Retired. The Steinberg variety is a geometric object in the representation theory of reductive groups. The bar complex is a coalgebra computing the derived center. These are unrelated constructions at different categorical levels.

Counter: NEVER write B(A) and SC^{ch,top} in the same sentence attributing SC to B(A). The SC structure lives on (C^bullet_ch(A,A), A). The bar complex is over (ChirAss)^!, single-colored, E_1-chiral-coassociative.

**FM26. False operad self-duality claim.** Opus claimed "(SC^{ch,top})^! ~ SC^{ch,top}" (Koszul self-dual) in thm:SC-self-duality, misciting Livernet [Liv06] (which proves Koszulity, not self-duality). The manuscript's OWN compute engine (sc_koszul_dual_cooperad_engine.py) computes SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!, manifestly different from SC = (Com, Ass) with closed dim = 1. The error: confusing "the duality FUNCTOR is an involution on SC-algebras" with "the OPERAD is self-dual." These are different: (P^!)^! ~ P (tautological for Koszul operads) does NOT mean P^! ~ P. Counter: before claiming any operad is self-dual, verify dim P(n) = dim P^!(n) at all degrees.

**FM27. Scope inflation in metadata.** Opus inflated concrete computational results into universal claims in CLAUDE.md/MEMORY.md. Example: "chiral QG equivalence for all four families" when the paper only verifies concretely for sl_2 Yangian + affine KM. The abstract theorem is proved on the Koszul locus, but concrete verification requires explicit computation at each family. Counter: metadata claims must carry explicit scope qualifiers matching the actual verification level.

**FM29. RETRACTED.** The arity→degree rename was correct and intentional. "Arity" is banned from the manuscript (AP176 CONSTITUTIONAL). "Degree" is the universal term for all index-counting contexts. The rename was NOT an error.

**FM30. Lambda-bracket divided-power coefficient conflation.** Opus wrote the lambda-bracket coefficient c/12 where the shadow invariant S_2 = c/2 was required. The lambda-bracket {T_λ T} = (c/12)λ^3 uses divided powers (T_{(3)}T/3! = (c/2)/6 = c/12). Opus confused the PRESENTATION-DEPENDENT coefficient c/12 with the PRESENTATION-INDEPENDENT invariant S_2 = κ = c/2. The error was compounded by writing "which is the Virasoro central charge itself" (c/12 is NOT c). Counter: shadow invariants S_r are NUMBERS (family invariants), not convention-dependent coefficients. S_2 = κ ALWAYS. After writing any S_r value, verify against Vol I census: S_2(Vir) = c/2.

**FM32. Homotopy group computation from wrong space (BU vs U).** Opus computed pi_3(BU) = Z, confusing BU with U. The loop space relation pi_k(BU) = pi_{k-1}(U) was not applied: pi_3(BU) = pi_2(U) = 0 (Bott periodicity, even homotopy of U vanishes). The confusion is natural because pi_3(U) = Z IS the standard result, but the classifying space BU shifts the index by one. Counter: ALWAYS write the fiber sequence X -> EX -> BX and the resulting pi_k(BX) = pi_{k-1}(X) before computing any homotopy group of a classifying space. Check Bott periodicity PARITY after the shift.

**FM33. Formula applied outside its hypothesis domain.** Opus applied kappa_ch = chi(S)/2 (valid for local surfaces Tot(K_S -> S)) to the conifold (Tot(O(-1)^2 -> P^1), which is NOT Tot(K_S -> S) since K_{P^1} = O(-2) != O(-1)^2). The formula gave the correct numerical answer (kappa = 1) by coincidence, but the derivation is mathematically invalid. Counter: before applying ANY formula, verify the input satisfies the stated hypotheses. A correct answer from an invalid argument is worse than a wrong answer from a valid one — it masks the error.

**FM34. Excision/coproduct categorical level confusion.** Opus conflated two operations at different categorical levels: (a) excision (a gluing/descent property, produces one object from two halves via tensor product OVER A), and (b) the coproduct (a coalgebra structure map, produces the tensor product of two copies as a plain tensor product). The confusion is natural because both involve "cutting" and "tensor products," but excision is a SHEAF property (works over the algebra) while the coproduct is a COALGEBRA structure (works in the category of vector spaces). Counter: when writing a coproduct interpretation, verify the codomain is B(A) ⊗ B(A) (plain), not B_L ⊗_A B_R (over A).

**FM31. Asymptotic cancellation failure.** Opus wrote 10/(5c^2) = 2/(5c^2) instead of 2/c^2. The error: failing to cancel the common factor 5 between numerator 10 and denominator 5c^2. This is an ARITHMETIC error, not a conceptual one, but it propagates silently because 2/(5c^2) "looks like" a valid large-c asymptotic. Counter: after writing ANY asymptotic a/f(c), substitute c=100 and verify the numerical value matches the exact formula.

**FM29. Sign convention d+A vs d-A.** Opus writes KZ connection as nabla = d + A (math convention) but flat section equations as dPhi = +A*Phi (physics convention d-A). These are INCONSISTENT: nabla = d+A gives nabla(Phi) = dPhi + A*Phi = 0, hence dPhi = -A*Phi (wrong sign). The physics convention nabla = d-A is correct: nabla(Phi) = dPhi - A*Phi = 0, hence dPhi = +A*Phi. Counter: after writing ANY connection definition, verify nabla(Phi)=0 gives the displayed flat section equation. The standalone was harmonized (23 sign changes) in the 2026-04-12/13 session.

**FM30. Belavin r-matrix Weierstrass vs Pauli.** Opus uses Weierstrass zeta zeta(z) = theta_1'/theta_1 + 2*eta_1*z for the elliptic r-matrix Cartan channel. WRONG: the extra 2*eta_1*z term breaks the CYBE. The correct Belavin construction uses Pauli-matrix decomposition: r(z) = sum_{a=1}^3 w_a(z,tau) sigma_a tensor sigma_a / 2, with w_a = theta_{a+1}/theta_1 * theta_1'(0)/theta_{a+1}(0). The degeneration to rational is a TWO-STEP chain: elliptic -> trigonometric (Im tau -> inf) -> rational (z -> 0), NOT a single limit. Counter: verify CYBE numerically after writing any elliptic r-matrix.

**FM31. Miura coefficient universality.** The (Psi-1)/Psi coefficient on cross-terms in the Drinfeld coproduct Delta_z is UNIVERSAL across spins: it appears on J tensor J (spin 2) and on J tensor T + T tensor J (spin 3). At higher spins, new COMPOSITE corrections appear ((1-Psi)/(2Psi^2) at spin 3) but the primary coefficient persists. Counter: when extending coproduct formulas to higher spins, verify the (Psi-1)/Psi coefficient persists on the leading cross-term.

**FM32. RTT sign convention dependence.** The level-1 RTT commutation relation sign depends on the R-matrix convention: additive R(u) = uI + Psi*P gives [t_{ij}, t_{kl}] = Psi(delta_{il} t_{kj} - delta_{kj} t_{il}); Molev's 1-P/u convention gives the opposite sign. Counter: always state which R-matrix convention before writing RTT relations.

**FM33. Quantum determinant column ordering.** The central quantum determinant qdet T(u) for Y(gl_N) uses DECREASING column index ordering in the column determinant (j=N-1 leftmost, j=0 rightmost). The "left-to-right in j" ordering (j=0 leftmost) is NOT central at N >= 3 (coincidentally agrees at N=2). Counter: always specify column ordering when writing qdet formulas. Cite Molev Theorem 1.6.4 for the correct convention.

**FM34. Heat equation prefactor diagonal vs off-diagonal.** The genus-g heat equation d/dOmega_{ab} Theta = coefficient * d^2/(dz_a dz_b) Theta has prefactor 1/(4πi) for a=b (diagonal) and 1/(2πi) for a≠b (off-diagonal). The factor of 2 comes from the symmetric matrix chain rule: d/dOmega_{aa} = (1/2) d/d(Omega_{aa} as independent variable). Writing 1/(2πi) uniformly is a notational convention that absorbs the factor into the matrix derivative, but produces wrong numerical results when Omega_{aa} is treated as an independent variable in computations.

**FM28. Topologization scope conflation.** Opus marked thm:topologization as ClaimStatusProvedHere without scope, when the proof is verified only for affine KM at non-critical level (where Sugawara is explicit). For Virasoro and W-algebras, the proof depends on constructing the 3d HT BRST complex, which the manuscript itself acknowledges as conditional. Furthermore, the proof is COHOMOLOGICAL (works on Q-cohomology, not cochains). For class M, where chain-level data is essential, the E_3 may exist only on cohomology. Counter: every topologization claim must carry "(proved for affine KM at non-critical level; conjectural in general; cohomological, not chain-level)."

## Theorem Status

| Thm | Status | Key result |
|-----|--------|------------|
| A | PROVED | Bar-cobar adjunction + Verdier intertwining on Ran(X) |
| B | PROVED | Bar-cobar inversion: Omega(B(A)) -> A qi on Koszul locus |
| C | PROVED | Complementarity; C0 (fiber-center identification) unconditional, C1 (Lagrangian eigenspace) unconditional, C2 (scalar BV pairing) conditional on uniform-weight |
| D | PROVED | obs_g=kappa*lambda_g uniform-weight; multi-weight: +delta_F_g^cross |
| H | PROVED | ChirHoch*(A) polynomial Hilbert series, concentrated in cohomological degrees {0,1,2} |
| MC1-4 | PROVED | PBW, MC element, thick gen (all types), completion tower; MC3 layer 3 (shifted prefundamental generation) unconditional in type A, conditional outside type A |
| MC5 | ANALYTIC PROVED, CODERIVED PROVED, CHAIN-LEVEL CONJECTURAL | (1) Analytic HS-sewing proved at all genera (thm:general-hs-sewing, thm:heisenberg-sewing); (2) genus-0 algebraic BRST/bar comparison proved (thm:algebraic-string-dictionary); (3) BV=bar in coderived category proved for all four shadow classes including class M (thm:bv-bar-coderived); (4) genuswise chain-level BV/BRST/bar identification conjectural (class M chain-level false; conj:master-bv-brst); (5) tree-level amplitude pairing conditional on cor:string-amplitude-genus0 |
| Koszul | 10+1+1 | 10 unconditional + Lagrangian (conditional) + D-mod purity (one-dir) |
| D^2=0 | PROVED | Convolution (M-bar_{g,n}) + ambient (Mok25 log FM) |
| Theta_A | PROVED | Bar-intrinsic; all-degree inverse limit (thm:recursive-existence) |
| SC-formal | PROVED | SC-formal iff class G (prop:sc-formal-iff-class-g) |
| Depth gap | PROVED | d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy) |
| ChirHoch^1 KM | PROVED | ChirHoch^1(V_k(g)) = g; total dim = dim(g)+2 (prop:chirhoch1-affine-km) |
| Topologization | PROVED (affine KM); CONJECTURAL (general) | SC^{ch,top} + Sugawara = E_3 for V_k(g) at k != -h^v (thm:topologization). General chiral algebras with conformal vector: conj:topologization-general. Proof cohomological; class M chain-level open. |
| E_3 identification | PROVED (simple g) | Z^der_ch(V_k(g)) ≅ A^lambda as E_3-families over lambda*H^3(g)[[lambda]] (thm:e3-identification). Proof: E_3 formality (Kontsevich) + 1-dim of H^3(g) forces order-by-order uniqueness. For non-simple g: open (H^3 may be higher-dimensional). |
| Chiral QG equiv | PROVED | Three structures (R-matrix, A_inf, coproduct) determine each other on Koszul locus (thm:chiral-qg-equiv). Independent proof via CoHA (rem:independent-proof-coha). |
| gl_N chiral QG | PROVED (all N >= 1) | W_N carries chiral quantum group datum with Yang R-matrix, Drinfeld coproduct, non-trivial RTT for N >= 2 (thm:glN-chiral-qg). N=1 = thm:w-infty-chiral-qg. OPE compatibility by coderivation + JKL. |
| Verlinde recovery | PROVED | Verlinde Z_g = sum S_{0j}^{2-2g} recovered from ordered chiral homology at integer level (prop:verlinde-from-ordered). Handle attachment and separating factorization verified. |
| ker(av) formula | PROVED (all simple g) | dim(ker(av_n)) = d^n - C(n+d-1,d-1) for d-dim rep of any simple g (prop:ker-av-schur-weyl). Type-independent: depends only on dim V. |
| Genus-2 construction | CONSTRUCTED | Ordered chiral homology on Sigma_2: KZB with 2x2 Siegel period matrix, chi=-12 at degree 2, doubly-dynamical parameter (conj:g2-ddybe). |
| Miura coefficient | CORRECTED + UNIVERSAL | (Psi-1)/Psi on J⊗J (spin 2), J⊗T+T⊗J (spin 3), J⊗W_{s-1}+W_{s-1}⊗J (spin 4). Mechanism spin-independent: binom(s-2,s-2)=1 from Drinfeld minus 1/Psi from Miura :J·W_{s-1}: coefficient. conj:miura-cross-universality installed. 51+67+24 tests. |
| Z_g closed forms | DISCOVERED (g=0..6) | P_g(n) = n^{g-1}(n²-1)·R_{g-2}(n²), n=k+2. Z_2=n(n²-1)/6, Z_3=n²(n²-1)(n²+11)/180, Z_4=n³(n²-1)(2n⁴+23n²+191)/7560, Z_5=n⁴(n²-1)(n²+11)(3n⁴+10n²+227)/226800, Z_6=n⁵(n²-1)(2n⁸+35n⁶+321n⁴+2125n²+14797)/2993760. Leading coeffs = ζ(2g-2)/(2^{g-2}π^{2g-2}). Rational generating fn G_n(x) = Σ 1/(1-a_j x), a_j = n/(2sin²(πj/n)). |
| W_N Stokes count | DISCOVERED | Stokes rays for W_N KZ = 4N-4 (linear in N). W_2(Vir): 4. W_3: 8. W-W channel (pole 2N) dominates. Poincare rank = 2N-2. |
| Shadow = GW(C³) | IDENTIFIED | Shadow tower at κ=Ψ produces perturbative constant-map GW free energies F_g^{GW,const}(C³). MacMahon M(q) on DT side via MNOP. Shadow IS full GW for C³ (no compact curves). |
| Conformal anomaly | QUANTIFIED | Obstruction to constant coproduct = c/2 = κ(Vir_c). Quartic pole excess: primitive Delta gives c/(z-w)⁴ but need c/2. At c=0: obstruction vanishes (Heisenberg, constant coproduct exists). At c≠0: spectral parameter FORCED. |
| DS intertwining | VERIFIED | (pi_3×pi_3)∘Delta_z^{sl_3} = Delta_z^{W_3}∘pi_3 verified with 57 tests. Spectral coassociativity uses shifted parameters. |
| AP128 bar H^2 | FIXED | sl2_bar_dims gave h_2=6 (CE/Riordan). Correct chiral bar: h_2=5. New sl2_chiral_bar_dims() function. AP63 discrepancy: Orlik-Solomon form factor. |
| Quantum det ordering | FOUND | Central qdet uses DECREASING column index (j=N-1 leftmost). At N=3, increasing-index ordering is NOT central. 74 tests. |
| E_3 via Dunn | PROVED (alternative) | prop:e3-via-dunn: CG factorization E_1^top×E_2^hol + Sugawara topologization + Dunn = E_3^top. Independent of HDC. |
| E_3 for gl_N | EXTENDED | E_3 identification extends to gl_N via two independent invariant bilinear forms B_tr, B_ab. Both determined by formal disk comparison. |
| KZB flatness | VERIFIED | Heat equation d_tau(wp_1) = (1/(4πi))d_w(wp+wp²) at machine precision. Prefactor 1/(4πi) diagonal vs 1/(2πi) off-diagonal (symmetric matrix chain rule). |

## Anti-Patterns by Cognitive Trigger

### BEFORE WRITING A FORMULA

**kappa** (AP1, AP9, AP20, AP24, AP48, AP136): DISTINCT per family, NEVER copy. KM=dim(g)(k+h^v)/(2h^v), Vir=c/2, W_N=c*(H_N-1) where H_N=sum_{j=1}^{N} 1/j (AP136: NOT c*H_{N-1}), Heis=k. Always qualify: kappa^{KM}, kappa^{Vir}. Complementarity: kappa+kappa'=0 (KM/free), 13 (Vir), NOT universal. State WHICH algebra: intrinsic vs kappa_eff=kappa(matter)+kappa(ghost) vs kappa(B) where B=A^!. **AP1 operational mandate**: before writing ANY kappa formula, (a) read landscape_census.tex for that family, (b) evaluate at k=0 and k=-h^v, (c) cross-check compute/. Writing kappa from memory is FORBIDDEN.

**pole/weight** (AP19, AP21, AP27): r-matrix poles = OPE poles - 1 (d log absorbs one pole). Vir r-matrix: (c/2)/z^3 + 2T/z, NOT quartic. Bar propagator weight 1, NEVER weight h. Scalar formula FAILS at g>=2 for multi-weight (delta_F_g^cross != 0). u=eta^2=lambda=kappa(B)*omega_g is LINEAR in kappa, NEVER quadratic.

**grading/signs** (AP22, AP23, AP44, AP45, AP46, AP49): Desuspension LOWERS: |s^{-1}v|=|v|-1. In LaTeX: ALWAYS s^{-1}, NEVER bare s in bar-complex formula. T^c(s^{-1} A-bar), NOT T^c(s A-bar). Mnemonic: bar=down=desuspension=s^{-1}. eta(q) includes q^{1/24}. OPE mode vs lambda-bracket: T_{(3)}T=c/2 becomes {T_lambda T}=(c/12)*lambda^3 (divided power 1/n!). A-hat(ix)-1 starts at x^2; verify F_1 matches leading order. sqrt(Q_L) is flat section; H(t)=t^2*sqrt(Q_L) NOT horizontal. Cross-volume conventions: Vol I=OPE modes, Vol II=lambda-brackets, Vol III=motivic. NEVER paste without conversion.

**boundaries/forms** (AP116, AP117, AP118, AP136): AP116: After writing ANY summation sum_{j=a}^{b}, verify by substituting the smallest index. H_N=sum_{j=1}^{N} 1/j, NOT sum_{j=1}^{N-1}. Always check the boundary case. AP117: Connection 1-form is r(z)dz, NOT r(z) d log(z). KZ = sum r_{ij} dz_{ij}. Arnold form d log(z_i-z_j) is a bar-construction coefficient, not the connection form. NEVER write d log without verifying. AP118: Any formula that simplifies at g=1 because a matrix becomes scalar MUST be written in full multi-dimensional form. (Im Omega)^{-1} is a matrix at g>=2. Verify formulas at g=2 where the period matrix is 2x2. AP136: H_{N-1} != H_N - 1. Evaluate at smallest N to distinguish.

**ratios/reciprocals** (AP129, AP137): AP129: When a formula involves a/b, the most common transcription error is b/a. ALWAYS substitute a known numerical value to verify. AP137: Bosonic c_{βγ} and fermionic c_{bc} satisfy c_{βγ}+c_{bc}=0. They look similar but have opposite signs. VERIFY: check c_total=0.

**fiber-base/depth** (AP130, AP131, AP134): AP130: Objects on the fiber (forms on Σ_g) are NOT objects on the base (classes on M̄_g). Verify: does this expression live on moduli or on the curve? AP131: Generating depth (degree at which higher ops are determined) != algebraic depth (whether tower terminates). Vir: d_gen finite, d_alg=∞. AP134: Cohomological amplitude [0,d] != virtual dimension d.

**bar complex** (AP132, AP141): AP132: B(A) uses the augmentation ideal Ā=ker(ε), NOT A. T^c(s^{-1} Ā), never T^c(s^{-1} A). AP141: r-matrix k=0 vanishing check after EVERY r-matrix formula.

**duality** (AP33, AP29, AP31): H_k^! = Sym^ch(V*) != H_{-k}. Same kappa, different algebras. delta_kappa=kappa-kappa' (asymmetry, vanishes c=13) != kappa_eff=kappa(matter)+kappa(ghost) (cancellation, vanishes c=26). kappa=0 implies m_0=0 (uncurved); higher-degree components independent. F_1=0 does NOT imply F_g=0.

**computation discipline** (AP3, AP10, AP61): Compute independently. NEVER pattern-match across occurrences. Cross-family consistency checks are real verification; single-family hardcoded tests insufficient. Verify against OPE table, landscape_census.tex, cross-engine comparison. **AP10 strengthened**: every hardcoded expected value MUST have a comment citing 2+ independent derivation paths. For combinatorial counts, cite generating function or recursion. Bare numbers with no derivation trail are future AP10 violations.

### BEFORE WRITING A SCOPE CLAIM

AP6: Specify genus, degree, level (convolution vs ambient) for D^2=0, kappa, Theta_A.
AP7: Before writing universal quantifier, verify proof has no implicit type/genus/level restriction.
AP8: NEVER "self-dual" unqualified. Specify which duality, which c. Virasoro self-dual at c=13.
AP14: Koszulness != SC formality. Koszul = bar H* in degree 1. SC formal = m_k^{SC}=0 for k>=3. All standard families Koszul; only class G SC-formal.
AP18: "Entire standard landscape" -> list every family, check each against hypotheses.
AP30: CohFT flat identity requires vacuum in V. ALWAYS list conditional axioms at cross-reference.
AP32: Genus-1 != all-genera. obs_1=kappa*lambda_1 unconditional. Multi-weight g>=2: scalar formula FAILS. **Every occurrence of obs_g, F_g, lambda_g in a theorem MUST carry explicit tag: (UNIFORM-WEIGHT) or (ALL-WEIGHT, with cross-channel correction). Untagged = violation.**
AP36: "implies" proved, "iff" claimed -> write "implies" until converse has independent proof. **Before writing "iff" or biconditional arrow, STOP: is the converse proved in the same theorem? If not, write "implies."**
AP67: Strong gen != FREE strong gen. W(p) has 4 strong generators but FREE strong gen OPEN.
AP138: Degenerate graded Jacobi. At even suspended degree ||m||=0, [[m,m],f]=0 is TAUTOLOGICAL. The identity [m,[m,f]]=½[[m,m],f] requires ||m|| ODD. Check parity before using Jacobi to relate ad_m^2 to [[m,m],-].
AP139: Unbound variable in theorem. If LHS depends on {g} but RHS on {g,n}, the variable n is FREE. Every variable in a displayed equation within a theorem MUST be quantified. Found in Thm C^{E1}.

### BEFORE WRITING ABOUT OBJECTS

**four functors** (AP25, AP34, AP50): B(A)=coalgebra. D_Ran(B(A))=B(A!)=algebra. Omega(B(A))=A. Z^der_ch(A)=bulk. FOUR distinct objects from four distinct functors. Omega(B(A))=A is INVERSION, NOT Koszul duality. D_Ran is VERDIER. Bulk is HOCHSCHILD. A^!_inf (Verdier, chain-level) != A^! (linear duality, strict). Compatibility IS Theorem A. NEVER "bar-cobar produces bulk."

**operadic** (AP65, AP81, AP82, AP83, AP84, AP85, AP88, AP103, AP104): B_P(A)=P^!-coalgebra != BP=cooperad (different levels). Three coalgebra structures: Lie^c (Harrison, coLie), Sym^c (coshuffle, 2^n terms), T^c (deconcatenation, n+1 terms). Coshuffle != deconcatenation. Factorization coproduct (Sym^c on Ran) != deconcatenation (T^c on ordered configs); R-matrix descent relates. B_{Com}(A) is coLie, NOT cocommutative. P^i=cooperad != P^!=(P^i)^v=operad. Cotriple bar != operadic bar. E_1 is PRIMITIVE; modular/symmetric is av-image.

**SC/promotion** (AP86, AP87, AP89, AP90, AP91, AP92, AP93): B_{SC}(A) for one-colour ill-formed. SC is two-coloured; use promotion A->(A,A). Closed=B_{Com}(A), open=B_{Ass}(A), plus mixed sector. SC mixed-sector dim = (k-1)!*C(k+m,m), NOT (k-1)!*m!. FM_n(X) connected; only strata factor. Curved d^2=kappa*omega_g NOT coderivation (factor-2 cross-term at g>=1). Two curvatures: mu_0 (algebra, genus 0, strict) vs d_fib^2=kappa*omega_g (fiberwise, genus>=1, Hodge). delta_F_g^cross in CLOSED sector: "mixed channels" (propagator) != "mixed sector" (open-closed SC).

**shadow/Hochschild** (AP94, AP95, AP96, AP97, AP98, AP100, AP102): ChirHoch*(Vir_c) concentrated in degrees {0,1,2}. NEVER C[Theta]. ChirHoch != Gelfand-Fuchs (GF infinite-dim, ChirHoch bounded). Shadow algebra has graded Lie bracket, NOT ring. av: g^{E_1}->g^mod is LOSSY; av(r(z))=kappa. kappa Eulerian weight parity-dependent. Theorem C: C0 fiber-center; C1 Lagrangian eigenspace decomposition unconditional; C2 shifted symplectic/BV upgrade conditional. Scalar kappa+kappa'=K follows from C1 + Theorem D, not from C2. Theorems must specify which bar: B^ord, B^Sigma, or B^Lie.

### BEFORE WRITING PROSE

AP105: Heisenberg = abelian KM at level k = abelian CS boundary. SAME OPE J(z)J(w) ~ k/(z-w)^2. Simple-pole requires ODD generator (symplectic fermion).
AP106: NEVER "This chapter constructs..." Open with the PROBLEM. CG deficiency opening.
AP108: Heisenberg = CG opening, NOT the atom. Atom of E_1 = genuinely nonlocal (Yangian, EK quantum VA).
AP109: NEVER list results before proving them. Theorems appear when mathematics demands.
AP111: No "What this chapter proves" blocks. Restructure instead.
AP107: r^coll(z) differs from Laplace-transform r(z) for odd generators.
**Prose laws**: (1) No AI slop (notably/crucially/remarkably/interestingly/furthermore/moreover/delve/leverage/tapestry/cornerstone). (2) No hedging where math is clear. (3) No em dashes; use colons, semicolons, or separate sentences. (4) No passive voice hedging. (5) Every paragraph forces the next. (6) State once, prove once. (7) Scope always explicit. (8) Comparison with prior work: one sentence per paper.

### AFTER EVERY EDIT

AP2: Read actual .tex proof, not CLAUDE.md description. Descriptions are claims ABOUT source.
AP5: Grep ALL THREE volumes for variant forms: ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2, ~/calabi-yau-quantum-groups. After EVERY correction.
AP12: When proving a claim, search entire manuscript for variants. Update all instances same commit.
AP17: After writing ANY new theorem, IMMEDIATELY audit before building next result.
AAP1: Grep for `antml` or `</invoke>` in .tex after every write.
AAP7: Grep current file before writing formula that appears elsewhere in same file.

### BEFORE COMMITTING STATUS

AP4: ClaimStatusProvedHere = verify proof proves stated claim. Status tag != ground truth.
AP40: Environment MUST match tag. Conjectured -> \begin{conjecture}. ProvedElsewhere -> theorem + Remark attribution.
AP60: Tag only genuinely new content ProvedHere. Classical parts ProvedElsewhere with attribution.
AP47: Evaluation-generated core != full category. MC3 proved on eval core; DK-4/5 downstream.

## Pre-Edit Verification Protocol

Fill-in-the-blank templates mandatory BEFORE writing the listed formula classes. Filling out a template IS the verification; the blank forces the computation; the computation catches the error. Source: pre_edit_verification_protocol_wave12.md (PE-1 through PE-12 full entries).

Invocation protocol: before every Edit touching a trigger pattern, write the relevant template as a fenced block in the reply text (NOT in the .tex file), fill it in, end with `verdict: ACCEPT`, THEN invoke Edit. If any `match?` is `N` or any required source is blank, `verdict: REJECT` and re-draft.

Eight highest-priority templates follow. Remaining four (PE-3 complementarity, PE-6 exceptional dimensions, PE-9 summation boundary, PE-12 prose hygiene) are in the source draft.

**PE-1. r-matrix write** (AP126, AP141, AP19, AP20)

Trigger: any r-matrix formula or reference to `r(z)`, `r_{ij}`, classical r-matrix.

```
## PRE-EDIT: r-matrix
family:                    [Heis / affine KM / Vir / W_N / lattice / Yangian / other]
r(z) written:              [full formula with level prefix]
level parameter symbol:    [k / k+h^v / hbar / c / Psi]
OPE pole order p:          [_]
r-matrix pole order p-1:   [_]              # AP19: d log absorbs one pole
convention:                [trace-form k*Omega/z / KZ Omega/((k+h^v)*z)]
AP126 check (trace-form):  r(z)|_{k=0} = [_]    expected: 0
  (KZ convention: k=0 gives Omega/(h^v*z) != 0 for non-abelian g; this is correct)
match?                     [Y/N]            # must be Y for trace-form; N/A for KZ non-abelian
AP141 grep check:          bare \Omega/z instances in edit scope: [N]
bare \Omega/z allowed?     N
critical-level check (KM): r(z)|_{k=-h^v} = [_]    (trace-form: finite; KZ: diverges)
source:                    [landscape_census.tex:LINE / compute/module.py]
verdict:                   [ACCEPT / REJECT]
```

**PE-2. kappa formula write** (AP1, AP9, AP24, AP39, AP48, AP136)

Trigger: any formula involving kappa or variants (kappa_eff, kappa(B), kappa_ch, kappa_BKM, kappa_cat, kappa_fiber).

```
## PRE-EDIT: kappa
family:                    [Heis / Vir / KM / W_N / bc / betagamma / svir / other]
kappa formula written:     [_]
census citation:           landscape_census.tex:LINE, kappa^{family} = [_]
match?                     [Y/N]            # STOP if N
AP39 uniqueness: is kappa = S_2?  [Y/N]
  if Y, is family Vir?     [Y/N]            # only Vir has kappa = S_2/2 = c/2
evaluation paths:
  at k=0:                  [_]  expected [_]
  at k=-h^v (KM):          [_]  expected 0
  at c=13 (Vir):           [_]  expected 13/2
AP136 boundary (W_N):      formula uses [H_N / H_{N-1} / H_N - 1]
  substitute N=2:          [_]  expected c/2 (W_2 = Vir)
wrong variants avoided:
  NOT kappa(Vir) = c       NOT kappa(W_N) = c*H_{N-1}
  NOT kappa(Heis) = k/2    NOT kappa(KM) = (k+h^v)/(2h^v) (missing dim(g))
verdict:                   [ACCEPT / REJECT]
```

**PE-4. bar complex formula** (AP132, AP22, AP23, AP44)

Trigger: `B(A)`, `T^c(...)`, any bar-construction formula, any desuspension.

```
## PRE-EDIT: bar complex
object written:            B(A) = [_]
T^c argument:              [s^{-1} \bar A / s^{-1} A / s \bar A / bare A]
AP132 augmentation:        \bar A = ker(epsilon) present?  [Y/N]   # must be Y
AP22 desuspension:         |s^{-1} v| = |v| [-1 / +1]              # must be -1
s^{-1} (NOT bare s) used?  [Y/N]                                   # must be Y
coproduct type:            [deconcatenation T^c / coshuffle Sym^c / coLie]
match to intended bar?     [B^ord -> deconc / B^Sigma -> coshuffle / B^Lie -> coLie]
grading:                   cohomological |d|=+1?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-5. Vol III kappa write** (AP113)

Trigger: ANY kappa occurrence in `~/calabi-yau-quantum-groups/**/*.tex`. Zero tolerance.

```
## PRE-EDIT: Vol III kappa
subscript written:         [kappa_ch / kappa_cat / kappa_BKM / kappa_fiber / OTHER]
subscript present?         [Y/N]   # must be Y; bare kappa FORBIDDEN
subscript justification:   [chiral shadow / categorified / BKM / fiber correction]
census citation:           Vol III landscape_census_cy.tex:LINE
grep BEFORE write:         bare `\kappa[^_]` hits: [N]
grep AFTER write:          bare `\kappa[^_]` hits: [N]
delta = 0?                 [Y/N]   # must be Y
verdict:                   [ACCEPT / REJECT]
```

**PE-7. Label creation** (AP124, AP125)

Trigger: any `\label{...}` write.

```
## PRE-EDIT: label
environment:               [theorem / proposition / conjecture / definition / remark / lemma]
label written:             \label{prefix:name}
prefix match (AP125):      theorem->thm, prop->prop, conj->conj, def->def, rem->rem, lem->lem
match?                     [Y/N]   # must be Y
AP124 duplicate check (grep all three volumes):
  Vol I matches:           [N]
  Vol II matches:          [N]
  Vol III matches:         [N]
  total BEFORE:            [N]
  total AFTER:             [N]
  delta = 1?               [Y/N]   # must be Y
if duplicate, rename with volume suffix and update all \ref
verdict:                   [ACCEPT / REJECT]
```

**PE-8. Cross-volume formula** (AP5, AP3)

Trigger: any formula shared across volumes (kappa, r-matrix, Theta_A, bar differential, connection 1-form, complementarity).

```
## PRE-EDIT: cross-volume formula
formula:                   [_]
Vol I grep:                [hits, canonical form]
Vol II grep:               [hits, canonical form]
Vol III grep:              [hits, canonical form]
consistent across volumes? [Y/N]
if inconsistent:
  canonical volume:        [Vol I / II / III]
  other volumes updated same session?  [Y/N]  # must be Y (AP5)
convention conversion?     [OPE(I) -> lambda(II) / motivic(III) / NA]
conversion applied?        [Y/N/NA]
verdict:                   [ACCEPT / REJECT]
```

**PE-10. Scope quantifier** (AP6, AP7, AP32, AP139)

Trigger: any theorem statement, any obs_g / F_g / lambda_g formula, any universal quantifier.

```
## PRE-EDIT: scope quantifier
statement:                 [_]
genus:                     [g=0 / g=1 / g>=2 / all g / UNSPECIFIED -> REJECT]
degree:                     [n=_ / all n / UNSPECIFIED -> REJECT]
level:                     [convolution M-bar_{g,n} / ambient Mok25 log FM / both / NA]
AP32 weight tag:           [(UNIFORM-WEIGHT) / (ALL-WEIGHT + delta F_g^cross) / NA]
tagged in statement?       [Y/N]  # must be Y for any g>=2 claim
AP139 free-variable audit:
  variables on LHS:        {_}
  variables on RHS:        {_}
  LHS superset RHS?        [Y/N]  # if N, bind the free variable
AP36 implies vs iff:       [implies / iff]
  if iff, converse proved in same theorem?  [Y/N]
verdict:                   [ACCEPT / REJECT]
```

**PE-11. Differential form type** (AP117, AP27, AP130)

Trigger: any write of a connection 1-form, KZ connection, Arnold form, bar propagator.

```
## PRE-EDIT: differential form
what:                      [connection 1-form / bar propagator / Arnold form / KZ / other]
form written:              [_]
expected type:
  connection 1-form: r(z) dz  (NOT d log)
  KZ:                sum r_{ij} dz_{ij}
  Arnold form:       d log(z_i - z_j)  (bar coefficient, NOT connection)
  bar propagator:    d log E(z,w)  (weight 1 ALWAYS, AP27)
match?                     [Y/N]
AP27 propagator weight:    1?  [Y/N]
AP117 d log check:         if d log appears, Arnold-form context? [Y/N]
space the form lives on:   [fiber Sigma_g / base M-bar_{g,n} / FM_n(X) / Ran(X)]
AP130 fiber-base:          object on fiber vs class on base correctly distinguished? [Y/N]
verdict:                   [ACCEPT / REJECT]
```

Refusal criteria: reject own edit if any `match?` = N, any blank source, any `FORBIDDEN` ticked, grep delta mismatch. On reject: re-draft, re-fill, proceed only when `verdict: ACCEPT`.

Remaining templates PE-3 (complementarity), PE-6 (exceptional dimensions), PE-9 (summation boundary), PE-12 (prose hygiene) in `compute/audit/pre_edit_verification_protocol_wave12.md`.

## Additional Anti-Patterns (Reference)

### Epistemic
AP11: Single-point external dependency -> flag in concordance with source, status, fallback.
AP13: Forward references must be transparent about genus/level/type restrictions.
AP15: E_2* is quasi-modular. Genus-1 propagator IS E_2*. Graph sums produce quasi-modular {E_2*,E_4,E_6}, NOT {E_4,E_6}.
AP26: Fock inner product != BPZ for weight>=4, rank>=3 W-algebras.
AP28: NEVER use undefined terminological qualifier in 3+ locations.
AP35: False proof, true conclusion -> two cancelling errors. Fix BOTH.
AP37: SS page from FULL differential, not pole order heuristics. Lie homology != Hochschild homology.
AP38: Literature values: record source paper AND convention. DVV != Eichler-Zagier. Derive independently.
AP39: kappa != S_2 for non-Virasoro. Coincide only rank-1. Lookup: Heis_k: kappa=k (NOT k/2). Vir_c: kappa=c/2 (ONLY family where kappa=S_2/2). KM: kappa=dim(g)(k+h^v)/(2h^v).
AP41: Prose mechanism != mathematical mechanism. "Residue extracts simple-pole coefficient" WRONG.
AP42: State level of validity explicitly for sophisticated identifications.
AP43: Central object without \begin{definition} -> property list is conjecture, not definition.

### Computational
AP59: Three invariants: p_max(OPE pole) != k_max(collision depth=p-1) != r_max(shadow depth, independent). betagamma: p=1,k=0,r=4.
AP62: "depends only on dim(g)" = Euler char only. Individual bar cohom dims need full bracket.
AP63: CE(g_-) != chiral bar for multi-gen. Orlik-Solomon form factor differs. sl_3 chiral H^2=36 vs CE H^2=20.
AP64: CE weight vs PBW degree produce different sequences. Always specify grading.
AP66: Free-field GFs NOT D-finite (Lipshitz/Stanley). Interacting algebras ARE.
AP68: PVA slab ghost c != kappa. SVir: kappa=(3c-2)/4. Hierarchy: Sigma_0=13 > Sigma_1=41/4 > Sigma_2=1 > Sigma_4=0.
AP69: tau_shadow = kappa-deformed KdV. Obstruction kappa(kappa-1). Standard KdV only at kappa=1.
AP70: Shadow L^sh has POLES at s=1,2. Negative integers are trivial zeros. F_g <-> L^sh(1-2g) FAILS.
AP71: Shadow kappa != Dyson beta. At c=13, kappa=6.5, not 13.
AP72: W-algebra NOP bar has d^2 != 0. Needs full singular OPE + Orlik-Solomon.
AP73: BV=bar: PROVED G/L, CONDITIONAL C/M (harmonic decoupling).
AP74: False Bernoulli-Dirichlet identity. LHS entire, RHS has poles s=1,2. Verify numerically at s=0.
AP75: Koszulness = PBW degree concentration, NOT conformal weight grading.
AP76: Y_{1,1,1} has c=0, kappa=Psi, NOT c=3.
AP77: Stokes ratio on convergent series spurious. Use direct Pade, not Borel.
AP78: Never conjecture from isolated number-theoretic coincidences.
AP79: W(p) has 4 generators (T + sl_2 triplet), not 2. Count fields, not isotypic components.
AP80: Engine without test file -> verify BOTH exist after every agent completion.
AP135: q-expansion coefficients. 1/eta(tau)^r has r-coloured partition numbers p_{-r}(n), NOT simpler sequences. r=2: (1,2,5,10,20,...) bicoloured partitions, NOT triangular (1,3,6,10,...). OEIS lookup before hardcoding.
AP140: Koszul conductor vs local constant. K=c+c' is a GLOBAL duality invariant. Ghost numbers, grading shifts, normalization factors are LOCAL. K_BP=196, not 2.

### Empirical (AP116-AP123, from 150-commit error archaeology)
AP116: Summation boundary verification. After writing sum_{j=a}^{b}, substitute smallest index. H_N=sum_{j=1}^{N}, NOT N-1. Off-by-one is the #1 formula error that passes visual inspection.
AP117: Differential form type. Connection is r(z)dz, NOT r(z) d log(z). KZ=sum r_{ij} dz_{ij}. Arnold d log(z_i-z_j) is bar coefficient, not connection. NEVER write d log without verification.
AP118: Genus-1 scalar collapse. Formula at g=1 where matrix=(Im Omega)^{-1} becomes scalar 1/Im(tau) MUST be written in full matrix form. Verify at g=2 with 2x2 period matrix.
AP119: Convergent vs divergent series. Before applying Borel summation: verify series is Gevrey-1 (factorial divergence). If |F_{g+1}/F_g| approaches constant (not growing like 2g), series is Gevrey-0. Use direct Pade, NOT Borel.
AP120: Cauchy integral normalization is 1/(2*pi*i), NOT 1/(2*pi). Missing i gives zero for real coefficients. Always verify F_1=kappa/24 as sanity check.
AP121: Modality hygiene. In LaTeX, NEVER use Markdown: no backtick numerals (`29` -> $29$), no **bold** -> \textbf, no _italic_ -> \emph. Grep for backticks after every .tex write.
AP122: Test tolerance proportional to magnitude. For Q~10^17, absolute tol 1e-4 is meaningless. Use relative: abs(computed-expected)/abs(expected) < rtol. Always verify tolerance achievable at float precision.
AP123: Combinatorial enumeration completeness. Verify count against known formula or generating function BEFORE hardcoding. Genus-2 stable graphs: 7 (not 6). Hand enumeration without cross-check = future AP10 violation.

### Deep Empirical (AP124-AP128, from 300-commit deep archaeology)
AP124: Duplicate \label{} across chapters. Before creating ANY \label{foo}, grep the entire manuscript. Parallel agents independently create labels with the same natural name. LaTeX silently uses the last definition, misdirecting cross-refs. Run: grep -rn '\\label{' chapters/ appendices/ | sort by label | check for duplicates.
AP125: Label prefix MUST match environment. \begin{conjecture} uses conj:, \begin{theorem} uses thm:, \begin{proposition} uses prop:. When upgrading/downgrading, rename label AND update all \ref instances atomically. Stale thm: prefix on a conjecture misleads agents who grep for conj: to find conjectures.
AP126: Level-stripped r-matrix. Classical r-matrix for affine KM at level k is r(z) = k*Omega/z, NOT Omega/z. The level k survives d-log absorption. Verify: at k=0 the r-matrix MUST vanish. 42+ instances found across all three volumes (12 in first commit, 30 more in full-volume CG sweep). THE MOST VIOLATED AP in the manuscript. After writing ANY r-matrix, verify k=0 -> r=0.
AP127: Cross-refs to migrated chapters. When migrating \input{chapter} between volumes, immediately add \phantomsection\label{} stubs for EVERY label in the migrated file, and grep for all \ref{} pointing to those labels. Never leave a bare \ref to a label that no longer exists in the build.
AP128: Engine-test synchronized to same wrong value. When correcting a compute engine formula, NEVER update test expectations from engine output. Derive correct expected value INDEPENDENTLY (different formula, limiting case, literature). Then update both. The engine and test sharing the same wrong mental model is the most dangerous AP10 variant.

### Full-Volume Rectification (AP129-AP141, from 48-agent cross-volume CG sweep)
AP129: Reciprocal formula. When a formula involves a ratio a/b, the most common transcription error is b/a or -b/a. Both "look right" because they contain the same symbols. S_4(Vir) = 10/[c(5c+22)] was written as -(5c+22)/(10c) (the negative reciprocal). VERIFY: substitute a known value (e.g. c=1) and check the NUMBER before trusting the symbolic form.
AP130: Fiber-base level confusion. Objects on the fiber (dτ ∈ H^{1,0}(E_τ)) are NOT objects on the base (c_1(λ) ∈ H^2(M̄_g)). The Hodge CLASS ω_g = c_1(E) lives on moduli space; the holomorphic FORM dτ lives on the elliptic curve. Before writing ω_g = [expression], verify: does [expression] live on M̄_g or on Σ_g?
AP131: Generating depth != algebraic depth. d_gen (the degree at which all higher operations are determined by lower ones) ≠ d_alg (whether the tower terminates). Virasoro: m_3 generates all m_k (finite generating depth), but ALL m_k are nonzero (d_alg = ∞, class M). Writing d_alg(Vir) = 1 because "m_3 generates everything" conflates the two. Always specify WHICH depth.
AP132: Augmentation ideal in bar complex. B(A) = T^c(s^{-1} Ā), where Ā = ker(ε) is the AUGMENTATION IDEAL, NOT T^c(s^{-1} A). Using A instead of Ā includes the unit and breaks the construction. Found twice in the same chapter: the error survives visual inspection because A and Ā look similar. Mnemonic: bar complex uses bar A.
AP133: Catalan index shift. C_n counts binary trees with n+1 leaves (equivalently n internal nodes). The most common error: writing C_k when you mean C_{k-1} (or vice versa). C_3=5 (4 leaves) ≠ C_4=14 (5 leaves). VERIFY: count the leaves, subtract 1, THEN look up the Catalan number.
AP134: Cohomological amplitude != virtual dimension. Concentration of ChirHoch* in degrees {0,1,2} means cohomological amplitude [0,2]. This is NOT "virtual dimension 2". Virtual dimension depends on the specific algebra and is typically defined via an Euler characteristic or index. The amplitude is a topological invariant of the complex; the virtual dimension is an arithmetic one.
AP135: Partition number family confusion. Expansion coefficients of 1/η(τ)^r are r-coloured partition numbers p_{-r}(n). At r=1: (1,1,2,3,5,...) ordinary partitions. At r=2: (1,2,5,10,20,...) bicoloured partitions, NOT triangular numbers (1,3,6,10,...). Always identify the EXACT combinatorial sequence (OEIS lookup) before writing q-expansion coefficients.
AP136: Harmonic number notation trap. H_{N-1} ≠ H_N - 1. H_{N-1} = sum_{j=1}^{N-1} 1/j. H_N - 1 = (sum_{j=1}^{N} 1/j) - 1 = sum_{j=2}^{N} 1/j. At N=2: H_1=1 but H_2-1=1/2. CLAUDE.md itself had this error (kappa(W_N)=c*H_{N-1} instead of c*(H_N-1)). When a formula involves harmonic numbers with shifted arguments, ALWAYS evaluate at the smallest N to distinguish.
AP137: Bosonic/fermionic partner confusion. c_{βγ}(λ) = 2(6λ²-6λ+1) and c_{bc}(λ) = 1-3(2λ-1)² are DIFFERENT formulas satisfying c_{βγ}+c_{bc}=0. They involve the same variable λ, similar polynomial structure, and opposite signs. VERIFY: check c_total=0 after substitution. At λ=1: c_{βγ}=2, c_{bc}=-2. Writing one when you mean the other gives the wrong sign of c.
AP138: Degenerate graded identity. At even suspended degree ||m||=0, the graded Jacobi identity gives [[m,m],f]=0 (tautological), NOT [m,[m,f]]=½[[m,m],f]. The "½ trick" requires ||m|| odd (where the graded antisymmetry gives [m,m]≠0). Before using Jacobi to relate ad_m^2 to [[m,m],-], CHECK the parity of ||m||. At even degree, the identity is vacuous.
AP139: Unbound variable in theorem. If the LHS of a displayed equation depends on variables {g} but the RHS depends on {g,n}, the variable n is FREE. Every variable in a theorem statement MUST be either universally quantified ("for all n") or bound by the context ("at each degree n with 2g-2+n>0"). Unbound variables make the theorem ill-formed. Found in Theorem C^{E1} where the complementarity equation had n on the RHS but only g on the LHS.
AP140: Koszul conductor vs local constant. The Koszul conductor K=c+c' is a GLOBAL duality invariant. Local constants from specific computations (ghost numbers, grading shifts, normalization factors) are DIFFERENT numbers. K_BP=196 was written as 2 (confusing with a ghost constant C_{(2,1)}=2). Before writing a Koszul conductor, verify: is this c+c' or something else?
AP141: AP126 is systemic. The original AP126 noted "12 instances across 5 files." This rectification session found 30 MORE instances across all three volumes. The error survives because Ω/z and kΩ/z look similar and both give valid-looking formulas. ENFORCEMENT: after writing ANY r-matrix formula, (a) check that k=0 gives r=0, (b) grep the manuscript for bare Ω/z without level prefix.
AP142: Local-global conflation on curves. "Koszul duality over a point is Koszul duality over P^1" is FALSE. Three distinct errors collapse into this slogan, each independently fatal:
(a) A HOMOTOPY RETRACT IS DATA. A^1 deformation-retracts onto a point, but modular Koszul duality over A^1 requires EXTRA DATA (the choice of retraction, the homotopy, the transfer maps) to be related to modular Koszul duality over a point. The retract does not make them "the same"; it gives a specific, non-canonical comparison that carries information. Without specifying this data, the comparison is not even well-posed.
(b) A DISK IS NOT A POINT. The formal disk D = Spec C[[z]] is not a pure point. The thickening D -> {0} carries geometric content: formal power series vs polynomial vs convergent functions, growth conditions, completion. Vertex algebras live on the formal disk, not on a point. The passage from vertex-algebraic Koszul duality on D to classical Koszul duality over a point requires discarding this thickening data, and it is not a priori clear that nothing is lost.
(c) A^1 ALREADY HAS ARNOLD RELATIONS. Configuration spaces Conf_n(A^1) carry the Arnol'd algebra: the forms omega_ij = d log(z_i - z_j) satisfy the Arnold relation omega_ij ^ omega_jk + cyc = 0. These are present on A^1, NOT only on P^1. The passage point -> A^1 introduces configuration-space topology, FM compactifications, and the ordered-vs-unordered bar distinction. The passage A^1 -> P^1 adds compactness and different global topology (compact FM compactifications, different homotopy type of Conf_n(P^1) vs Conf_n(A^1)).
CONSEQUENCES: (i) genus-0 chiral Koszul duality is NOT "just" classical Koszul duality—the passage from a point to A^1 already introduces Arnold relations, FM compactifications, and the E_1/E_inf bar distinction; (ii) claims that "everything new happens at g >= 1" are overstated—curvature/anomaly phenomena are new at g >= 1, but configuration-space geometry is new already at g = 0 on A^1; (iii) the fiber of modular Koszul duality over each step of the chain point <- D -> A^1 -> P^1 -> general X has not been systematically studied in this programme and should not be claimed to be trivial; (iv) even at the first step (formal disk vs point), the comparison requires the retraction data and it is an open question whether modular Koszul duality sees the thickening. BEFORE writing any claim comparing Koszul duality "over a point" with "over a curve": specify WHICH space (point / formal disk D / A^1 / P^1 / general X), specify the COMPARISON DATA (retraction, localization, formal thickening), state WHETHER the identification is on-the-nose or requires extra structure, and acknowledge WHAT geometric content is present in each step.

### From 100-Commit Archaeology (AP143-AP148, April 2026)
AP143: DS ghost charge background shift omission. DS reduction from sl_N to W_{N,f} requires subtracting the full ghost central charge c_ghost(N,f,k) = c(sl_N,k) - c(W_{N,f},k), which includes the background charge contribution from the DS BRST complex. The simplified formula c_ghost(N,k=0) = N*(N-1) OMITS this background charge; the correct formula gives (N-1)*((N^2-1)*(N-1)-1). At N=7: 1722 vs 42. This error caused a cascade across W6/W7 shadow tower engines where engine and test were synchronized to the same wrong value (AP128 variant). VERIFY: at N=2, ghost_c = 1*((4*1)-1) = 3 = c(sl_2,0) - c(Vir,0) = 3 - 0. Before writing ANY DS ghost formula for N>=3, compute c(sl_N,k) - c(W_{N,f},k) directly from the Fateev-Lukyanov formula.
AP144: Convention coexistence without bridge. Different chapters independently develop conventions for the same object (r-matrix: trace-form k*Omega/z vs KZ Omega/((k+h^v)*z); kappa: several families). The conventions agree at generic parameter values but diverge at boundary values (k=0, k=-h^v). When multiple conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site, and boundary behavior must be checked in EACH convention separately. The r-matrix normalization issue (C9/C13/AP126 inconsistency, resolved April 2026) is the canonical example. After introducing ANY convention for a shared object, grep all three volumes for alternative conventions of the same object and install bridge identities.
AP145: Restructuring propagation debt. Any structural reorganization (Part renumbering, chapter migration, label renaming) creates O(N) propagation debt where N is the number of cross-references. Vol II's 10→8 Part restructuring required 24 stale Part reference fixes in a single commit. Chapter migration from Vol I to Vol II broke cross-references. BEFORE restructuring: grep for all references to the affected labels/Part numbers across all three volumes. AFTER: verify every reference resolves. Budget O(N) follow-up work, not O(1).
AP146: Mega-campaign straggler commits. After large agent campaigns (100+ agents), results arrive asynchronously. The pattern: launch N agents → commit results that arrive → stragglers arrive after commit → follow-up commit needed. This creates commit noise, risks merge conflicts, and can leave partial work committed. MITIGATION: AAP9 (wait for all agents) helps but does not eliminate the problem when agents have variable runtime. After any mega-campaign commit, expect at least one follow-up commit for stragglers and plan accordingly.
AP147: Circular proof routing. Theorem B and def:koszul-chiral-algebra appeared mutually circular until the routing was made explicit: twisted-tensor → cone identification → bar-cobar (commit 65262ee). When a proof chain involves multiple theorems that reference each other, insert a ROUTING REMARK citing the primitive non-circular anchor. If no such anchor exists, the proof is genuinely circular and must be restructured.
AP148: r-matrix normalization is convention-dependent (see corrected C9). Two conventions for affine KM: trace-form r(z)=k*Omega/z (AP126 k=0 check applies; av(r)=kappa_dp only; Sugawara shift dim(g)/2 needed for full kappa) and KZ r(z)=Omega/((k+h^v)*z) (k=0 gives nonzero for non-abelian; av not simply related to kappa). Bridge: k*Omega_tr = Omega/(k+h^v) at generic k. BEFORE writing any r-matrix formula for affine KM, state which convention and verify boundary behavior in that convention.

AP149: Resolution propagation failure. When a conjecture is proved, disproved, or retracted, ALL references retain their old status unless explicitly updated. This includes: (a) concordance.tex, (b) preface.tex, (c) introduction.tex, (d) standalone papers, (e) CLAUDE.md theorem status table, (f) label prefixes (conj: -> thm: or vice versa), (g) other volumes. All updates in the SAME session. Evidence: 6+ instances in 100-commit window (multi-weight universality "remains open" after negative resolution; W(2) Koszulness retraction; MC3 scope narrowing; Theorem H dim<=4 bound removal). The cascade AP40 downgrade -> AP125 label rename -> cross-volume ref update -> AP4 proof-to-remark must be atomic.
AP150: Agent confabulation of mathematical structures. Agents can stitch together disparate results from different categorical levels into claimed structures (e.g., an "E_n operadic circle" E_3->E_2->E_1->E_2->E_3) that do not exist in any manuscript. COUNTER: every claimed multi-step structure must be verified arrow-by-arrow against actual .tex source. Each arrow must have an independent theorem reference. If ANY arrow is conjectural, the structure is conjectural.
AP151: Convention clash within a single file. Two different definitions of the same symbol hbar (e.g., 1/(k+2) in one section vs pi*i/(k+2) in another) produce cascade errors in downstream formulas. The B-cycle monodromy q = e^{2*pi*i*hbar} becomes real instead of a root of unity when hbar has an extra factor of pi*i. COUNTER: after writing ANY formula involving hbar, grep the file for all other definitions of hbar and verify consistency.
AP152: "Ordered" ambiguity (labeled vs time-ordered). "Ordered configurations" on a curve means LABELED (non-coinvariant), not totally ordered (the curve has no natural total order). The total ordering lives in the topological direction R. The bar complex B^{ord}(A) is a MIXED object: holomorphic differential (from OPE on C) + topological coproduct (from deconcatenation along R). COUNTER: always specify whether "ordered" means "labeled on C" or "time-ordered on R."
AP153: E_3 scope inflation. The E_3 structure on the derived chiral center Z^{der}_{ch}(A) via the Higher Deligne Conjecture requires B-bar^Sigma(A) to exist as an E_2-coalgebra. For E_inf-chiral algebras (all standard VAs), B-bar^Sigma exists and E_3 follows. For genuinely E_1-chiral algebras (Yangians), B-bar^Sigma does NOT exist (the D-module doesn't descend to X^{(n)}), and the ordered bar gives only E_2 via classical Deligne. COUNTER: every E_3 claim must specify: is the input E_inf or E_1? If E_1, the passage to E_3 requires the Drinfeld center (conjectural).
AP154: Two distinct E_3 structures. (a) Algebraic E_3: from HDC on E_2 bar coalgebra, no conformal vector needed. (b) Topological E_3: from Sugawara topologisation, requires conformal vector at non-critical level. These are NOT the same; their identification as families over hbar*H^3(g)[[hbar]] is CONJECTURAL (conj:e3-identification). Topological E_3 (b): PROVED for affine KM at non-critical level (thm:topologization); CONJECTURAL for general chiral algebras with conformal vector (conj:topologization-general in Vol I, conj:E3-topological-climax in Vol II). Proof is cohomological; for class M, chain-level E_3 may fail. COUNTER: always specify which E_3 and whether the claim requires Sugawara.
AP155: "New invariant" overclaiming. The ordered chiral homology framework recovers known invariants (KZB from Bernard 1988, elliptic R-matrix from Felder 1994, Verlinde from BD) from a unified bar-complex construction. The novelty is ARCHITECTURAL (a new framework), not COMPUTATIONAL (new numbers). Claiming "genuinely new E_1 invariants" when the numbers are known under other names is misleading. COUNTER: for any claimed "new invariant," check Bernard/Felder/Etingof-Varchenko/Calaque-Enriquez-Etingof.
AP156: Quasi-periodicity convention for wp_1. Two different functions both called wp_1: (a) theta_1'(z|tau)/theta_1(z|tau) -- periodic under z->z+1, quasi-periodic under z->z+tau with increment -2*pi*i. (b) Weierstrass zeta_tau(z) = (a) + 2*eta_1*z -- quasi-periodic under BOTH z->z+1 (increment 2*eta_1) and z->z+tau. These produce DIFFERENT monodromy formulas. COUNTER: always specify which function and verify the quasi-periodicity at the point of use.
AP157: Degeneration-dependent "invariants." A formula computed from a specific degeneration (separating vs non-separating) of a higher-genus curve is NOT an invariant of the curve unless degeneration-independence is proved. The separating degeneration of a genus-2 curve contains ZERO genuinely genus-2 information (everything is determined by genus-0 S-matrix + genus-1 R-matrix eigenvalues). The non-separating channel carries genuinely new data. COUNTER: always specify the degeneration type and state whether independence is proved or assumed.
AP158: SC^{ch,top} != E_3. The Swiss-cheese operad is two-coloured with directionality (no open-to-closed). Dunn additivity does NOT apply to coloured operads. E_3 requires the topologization theorem: SC^{ch,top} + inner conformal vector (Sugawara at non-critical level, T(z) = {Q,G(z)}) = E_3-TOPOLOGICAL (NOT E_3-chiral). The conformal vector KILLS the chiral direction at the cohomological level: C-translations become Q-exact, the complex structure on C becomes irrelevant in cohomology, the two SC colors collapse, and Z^{der}_{ch}(A) becomes a genuine E_3-TOPOLOGICAL algebra. Without conformal vector: stuck at SC^{ch,top} (two colors remain distinct). At critical level k=-h^v: Sugawara undefined, topologization fails. NEVER write "E_3-chiral" for the topologized bulk; it is E_3-topological. Vol II MUST construct the E_3-topological structure on Z^{der}_{ch}(A) explicitly at chain level — define it, prove it, verify on examples, and characterize the obstruction when conformal vector is absent.
AP159: Four Yangian types on different geometric spaces. (1) Classical Y_hbar(g): E_1-topological on R. (2) dg-shifted Y^{dg}_hbar(g): at point/formal disk, from Koszul duality. (3) Chiral Y(g)^{ch}: E_1-chiral on curve X, D-module with R-twisted OPE. (4) Spectral: factorization on A^1_u. Conflating any two is a type error. The dg-shifted (2) is NOT the chiral (3); passage 2->3 is the globalization problem. Use ^{ch} superscript for Object 3, ^{dg} for Object 2.
AP160: Three Hochschild theories -- geometry determines which. (i) Topological HH: E_1 input -> E_2 (Deligne). (ii) Chiral ChirHoch: E_inf-chiral input -> {0,1,2} (Theorem H). (iii) Categorical HH: dg category -> E_2 with CY shifted Poisson. Bare "Hochschild" MUST carry qualifier (chiral/topological/categorical) in non-historical contexts. Conv:three-hochschild in concordance.tex is constitutional.
AP161: Five notions of E_1-chiral algebra are NOT interchangeable. (A) strict ChirAss, (B) A_inf in End^{ch}, (C) EK quantum VA, (D) A_inf in E_1-chiral, (E) factorization on Ran^{ord}. Each has own derived center. (B)<->(C) on Koszul locus only. Warn:multiple-e1-chiral in algebraic_foundations.tex.
AP162: E_3 requires conformal vector. NEVER claim E_3 structure without stating: (a) the conformal vector exists, (b) the level is non-critical, (c) T(z) is Q-exact in the bulk. At critical level k = -h^v: Sugawara undefined, topologization fails, stuck at SC^{ch,top}. Status: PROVED for affine KM (thm:topologization); CONJECTURAL for general (conj:topologization-general). The proof is cohomological; for class M algebras the chain-level E_3 structure is open.
AP163: "Lives on R x C" is unjustified for E_1-chiral algebras. An E_1-chiral algebra is defined via operad maps into End^{ch}_A on a curve X. The SC^{ch,top} bar complex is a coalgebra over a PRODUCT operad, NOT a factorization algebra on the product space R x C. The passage to a factorization algebra on R x C requires additional work (the chiral Deligne-Tamarkin principle, en_koszul_duality.tex).
AP164: Chiral Gerstenhaber != topological Gerstenhaber. The chiral bracket uses OPE residues on FM_k(C) configuration spaces. The topological bracket uses little 2-disks operations. They agree for E_inf input via formality; they diverge for E_1 input. Always specify "chiral Gerstenhaber" or "topological Gerstenhaber."
AP165: B(A) is NOT an SC^{ch,top}-coalgebra. The bar complex B(A) = T^c(s^{-1} A-bar) is an E_1 chiral coassociative coalgebra (differential from chiral product, deconcatenation coproduct). It is a SINGLE E_1 coalgebra, not a two-colored SC datum. The SC^{ch,top} structure emerges in the chiral derived center: the chiral Hochschild cochain complex C^bullet_{ch}(A,A) (defined via the chiral endomorphism operad End^{ch}_A with spectral parameters from FM_k(C), NOT topological Hochschild cochains RHom_{A^e}(A,A)) carries brace operations and a Gerstenhaber bracket, and the pair (C^bullet_{ch}(A,A), A) is the SC^{ch,top} datum (bulk acting on boundary). FORBIDDEN claims: "B(A) is a coalgebra over SC^{ch,top}"; "the bar complex presents the Swiss-cheese algebra"; "the bar differential is the closed color"; "the bar coproduct is the open color." COUNTER: after writing any sentence involving B(A) and SC^{ch,top} in the same paragraph, verify that SC is attributed to the derived center pair, not to B(A).

### From 2026-04-12 SC Adversarial Audit (AP166-AP175)
AP166: SC^{ch,top} is NOT Koszul self-dual. SC^! = (Lie^c, Ass^c, shuffle-mixed) with closed dim = (n-1)!. SC = (Com, Ass, product-mixed) with closed dim = 1. MANIFESTLY DIFFERENT. What IS true: the bar-cobar duality functor on SC-algebras is an involution ((A^!)^! ~ A). Koszul duality EXCHANGES Com (closed) with Lie (closed); Ass (open) is self-dual. The Livernet [Liv06] citation proves Koszulity, NOT self-duality. FORBIDDEN: "(SC^{ch,top})^! ~ SC^{ch,top}" or "SC is Koszul self-dual." CORRECT: "SC Koszul duality exchanges Com <-> Lie while preserving Ass; the duality functor is an involution."
AP167: Topologization scope. thm:topologization is PROVED for affine KM V_k(g) at non-critical level k != -h^v (where Sugawara T = {Q,G} is explicit). For general chiral algebras with conformal vector: CONJECTURAL (conj:topologization-general). The proof is COHOMOLOGICAL (works on Q-cohomology, not on cochains). For class M (Virasoro), where chain-level BV/bar is false, the E_3 may exist only on cohomology. COUNTER: every topologization reference must carry scope qualifier "(proved for affine KM at non-critical level)."
AP168: E_3 is TOPOLOGICAL, not chiral. When conformal vector exists: Sugawara makes C-translations Q-exact, complex structure on C becomes irrelevant in cohomology, two SC colors collapse, E_2^{hol} x E_1^{top} -> E_2^{top} x E_1^{top} = E_3^{top} via Dunn. The E_3 is a genuine TOPOLOGICAL algebra independent of the complex structure. FORBIDDEN: "E_3-chiral." CORRECT: "E_3-topological" (with conformal vector hypothesis).
AP169: SC^{ch,top} is the GENERIC case; E_3 is special. Most chiral algebras do NOT have conformal vector (Heisenberg, lattice, critical level, E_1-chiral, free fields without Sugawara). For these, SC^{ch,top} is the FINAL answer. The volume must treat SC^{ch,top} as a first-class object with generators-and-relations, multiple presentations, and many-fold proof redundancy.
AP170: Two incompatible Yangian definitions. def:e1-chiral-yangian = E_1-factorization + RTT (weaker). def:chiral-yangian-datum = quadruple (A, S(z), Delta^{ch}, {m_k}) with four axioms including modular MC tower (stronger). Equivalence is OPEN. Main obstruction: constructing the chiral coproduct from E_1-factorization data alone.
AP171: Associator dependence dichotomy. The chiral QG equivalence (R-matrix <-> A_inf <-> coproduct) holds "up to choice of Drinfeld associator Phi." COHOMOLOGICAL derived center = ASSOCIATOR-INDEPENDENT (proved for sl_2: GRT_1 shifts P_3 by coboundaries). COCHAIN-LEVEL derived center = ASSOCIATOR-DEPENDENT (the cochain-level E_3 carries the quantum group structure). Bar-side invariants (kappa, shadow tower) are associator-FREE. Cobar-side and coproduct-side depend on Phi. Analogous to deformation quantization: gauge-equivalent star products.
AP172: A^! is an SC^!-algebra, NOT an SC-algebra. The Koszul dual A^!_line carries CLOSED = Lie (Sklyanin bracket) and OPEN = Ass (Yangian product). This is an (SC^{ch,top})^!-algebra = (Lie, Ass)-algebra, NOT an SC-algebra = (Com, Ass)-algebra. FORBIDDEN: "A^! is an SC-algebra." CORRECT: "A^! is an SC^!-algebra = (Lie, Ass)-algebra."
AP173: Yangian derived center not computed. Z^{der}_{ch}(Y(g)^{ch}) — the derived center of the poster-child E_1-chiral algebra — is not computed anywhere. Only the ordered chiral center at low degrees (2-3) for sl_2 on the formal disk exists. The center is predicted INFINITE-DIMENSIONAL (classical center C[qdet T(u)] at degree 0). For E_1 input: only E_2 (not E_3), because B^Sigma doesn't exist and HDC is unavailable.
AP174: Chiral QG equivalence scope. thm:chiral-qg-equiv is proved abstractly on the Koszul locus. CONCRETE verification: sl_2 Yangian and affine KM only. Elliptic: partial (KZB connection, no QG equiv at genus 1). Toroidal: absent. FORBIDDEN: "equivalence for all four families." CORRECT: "proved abstractly; verified for sl_2 Yangian + affine KM."
AP175: Pentagon of equivalences is a star. The five SC presentations (operadic, Koszul, factorization, BV/BRST, convolution) are pairwise equivalent, but all equivalences route through the operadic hub. No single pentagon theorem. Three direct links with independent mathematical content: Koszul-BV, BV-Convolution, Factorization-Convolution.

### From 2026-04-12 Deep Mathematical Audit (AP176-AP180)
AP176: CONSTITUTIONAL — "arity" is BANNED. The word "arity" does NOT appear anywhere in the manuscript. "Degree" is the universal term for: bar complex grading, operadic input count, tree vertex valence, Stasheff identity level, SC mixed sector parameters, cooperad/operad component indices, endomorphism operad components, brace insertion count, and all other contexts where Loday-Vallette would use "arity." This is a deliberate, permanent terminological decision. NEVER reintroduce "arity." NEVER suggest reverting "degree" to "arity." NEVER flag the use of "degree" in operadic contexts as an error. If an agent proposes restoring "arity" anywhere, the proposal is WRONG. The ~25 instances of "an degree" (article mismatch) should be corrected to "a degree." Grep check after every .tex edit: `grep -rn '\\barity\\b' chapters/ appendices/ standalone/` must return ZERO hits.
AP177: S_2 = c/12 lambda-bracket divided-power confusion (Vol II, 3d_gravity.tex). The shadow invariant S_2 = kappa = c/2 for Virasoro (Vol I, 7 independent instances in higher_genus_modular_koszul.tex + concordance.tex). The Vol II 3d gravity chapter writes "S_2 = c/12" in FIVE places (lines 121, 1628, 1798, 1835, 6934), confusing the lambda-bracket divided-power coefficient c/12 = (c/2)/3! with the shadow invariant S_2 = kappa = c/2. The factor of 6 = 3! is the divided power from {T_lambda T} = (c/12)*lambda^3 (where c/12 = T_{(3)}T / 3! = (c/2)/6). The shadow invariant S_2 is convention-INDEPENDENT: it equals kappa = av(r(z)) = c/2 for Virasoro, regardless of whether presented in OPE or lambda-bracket. Line 7757 also says "which is the Virasoro central charge itself" — c/12 is NOT the central charge (c is). COUNTER: after writing ANY S_r value in lambda-bracket context, verify S_2 = kappa by checking against Vol I census. If S_2 != kappa, the convention is wrong.
AP178: S_4 large-c asymptotic off by factor 5 (Vol II, 3d_gravity.tex line 7763). The manuscript writes "S_4 = 10/[c(5c+22)] ~ 2/(5c^2) at large c." WRONG. 10/[c(5c+22)] = 10/(5c^2 + 22c) ~ 10/(5c^2) = 2/c^2 at large c. The correct asymptotic is 2/c^2, NOT 2/(5c^2). Off by factor 5. The error: the denominator 5c^2 was retained inside the fraction instead of being cancelled against the numerator 10. COUNTER: after writing ANY asymptotic, substitute c=100 and verify: 10/[100*522] = 10/52200 ≈ 1.916e-4; 2/c^2 = 2/10000 = 2e-4 (matches); 2/(5c^2) = 2/50000 = 4e-5 (off by 5x).
AP179: Graph vertex valence: "degree" vs "arity" context-dependent. In GRAPH THEORY, vertex valence is called "degree" (standard). In OPERAD THEORY, tree vertex valence is called "arity" (Loday-Vallette convention). The manuscript's Feynman graph contexts (thqg_fredholm_partition_functions.tex, thqg_gravitational_complexity.tex) involve graph vertices carrying transferred operations ell_k — these are BOTH graph vertices AND operadic operations. Convention: use "valence" or "arity" for vertices carrying operadic data (because the number indexes the operation ell_k); use "degree" only for pure graph-theoretic contexts without operadic interpretation.
AP180: Cross-volume convention clash for shadow coefficients. Vol I defines S_r as the degree-r projection of Theta_A in the convolution algebra, with S_2 = kappa. Vol II 3d_gravity.tex uses "S_2" for a different quantity (the lambda-bracket coefficient c/12 = kappa/6). No bridge identity is given. AP144 requires: when two conventions coexist, a BRIDGE IDENTITY must be stated explicitly at every site. The bridge is: S_2^{Vol I} = kappa = c/2 = 6 * S_2^{lambda-bracket} (if the latter is even a well-defined invariant, which is doubtful since S_r should not depend on presentation). Most likely resolution: S_2^{Vol II} is simply WRONG and should be corrected to c/2.
AP181: pi_3(BU) = Z false (Bott periodicity). Vol III fukaya_categories.tex lines 209, 396, 413 claim pi_3(BU) = Z. WRONG. By Bott periodicity, pi_k(BU) = Z for k even, 0 for k odd. Since 3 is odd, pi_3(BU) = 0. The confusion: pi_3(U) = Z (loop space), but pi_3(BU) = pi_2(U) = 0. The SAME volume's cy_to_chiral.tex line 331 correctly states pi_3(BU) = 0. The fukaya_categories.tex proposition on CY_3 dimension dependence uses pi_3(BU) = Z as the reason the S^3-framing is obstructed; this proof mechanism is FALSE. The CORRECT reason CY_3 gives E_1 (not E_2) is the antisymmetric Euler form structural obstruction (prop:e1-obstruction-categorical), NOT a topological obstruction (which vanishes). COUNTER: before writing ANY homotopy group pi_k(BX), verify via the fiber sequence pi_k(BX) = pi_{k-1}(X) and check Bott periodicity parity.
AP182: Local-surface formula applied outside its domain. The formula kappa_ch = chi(S)/2 applies to local surfaces Tot(K_S -> S). The conifold Tot(O(-1) oplus O(-1) -> P^1) has fiber O(-1)^2, NOT K_{P^1} = O(-2), so it is NOT a local surface. The toric_cy3_coha.tex line 305 applies kappa_ch = chi(P^1)/2 = 1 to the conifold; the value kappa = 1 is correct (from DT computation) but the DERIVATION is wrong (applies formula outside its hypotheses). Similarly, kappa = h^{1,1} is cited for P^1 x P^1 (line 199), which happens to agree with chi/2 for this surface but not in general (K3: h^{1,1}=20 but chi/2=12). COUNTER: before applying kappa_ch = chi(S)/2, verify that the geometry is Tot(K_S -> S); if not, derive kappa from DT invariants directly.
AP183: McKay quiver misidentification. toric_cy3_coha.tex line 186 calls the McKay quiver of C^3/Z_3 "the complete bipartite graph K_{3,3}." WRONG. K_{3,3} is an undirected bipartite graph with two parts of size 3. The McKay quiver is a DIRECTED graph: 3 copies of the oriented 3-cycle (0->1->2->0), giving 9 directed arrows. It is not bipartite (all vertices play symmetric roles). COUNTER: K_{a,b} is undirected bipartite; McKay quivers are directed. Never call a McKay quiver K_{a,b}.
AP184: Excision vs coproduct conflation. prop:bar-interval-identification Part (iv) in Vol II bar-cobar-review.tex conflates the excision formula (cutting [0,1] at t recovers B(A) = B_L(A) otimes_A B_R(A) as a derived tensor product OVER A of two one-sided bars) with the deconcatenation coproduct (Delta: B(A) -> B(A) otimes B(A) as a plain tensor product). Excision recovers the ORIGINAL B(A) from two halves; the coproduct maps B(A) into the PRODUCT of two copies. These are different mathematical operations. The coproduct is the cofree coalgebra structure on T^c(s^{-1} A-bar), not excision. COUNTER: excision = gluing (produces one copy via tensor over A); coproduct = splitting (produces tensor product of two copies). Never conflate.
AP185: Obstruction group vs enabler. cy_to_chiral.tex line 771 says "pi_4(BU) = Z provides native E_2" for CY_4. WRONG direction: pi_4(BU) = Z is the GROUP WHERE THE OBSTRUCTION LIVES, not a guarantee that E_2 exists. When the obstruction class in pi_4(BU) is nonzero, E_2 is OBSTRUCTED. The correct statement: "pi_4(BU) = Z provides a Z-valued obstruction to S^4-framing; when this obstruction vanishes, E_2 structure exists." COUNTER: nonzero homotopy group = potential obstruction, not automatic structure.

### Operadic-Structural
AP99: K11 Lagrangian CONDITIONAL (perfectness + bar-cobar normal-complex).
AP101: "qi not merely iso on cohomology" is tautological. Use "qi of A-inf-algebras" vs "chain qi."
AP110: Each volume's preface tells its OWN story. Cross-volume in delineated subsections.
AP112: Never trust stale page counts. Verify against fresh builds.
AP113: kappa without subscripts FORBIDDEN in Vol III. Always kappa_ch, kappa_BKM, kappa_cat, kappa_fiber.
AP114: Stub chapters (<50 lines, no theorems) create false coverage -> develop or comment out.
AP115: Architectural CLAUDE.md claims must be enacted in .tex. Metadata-source gap is the most dangerous anti-pattern.

## Regression Safeguards (non-AP)

RS-3: Physics IS the homotopy type, not a "bridge." Costello-Gaiotto-Dimofte are substance, not applications.
RS-4: Costello/Dimofte/Gaiotto content belongs in mathematical core, not "connections" chapters.
RS-9: The slab is a bimodule, NOT a Swiss-cheese disk. Two boundary components.
RS-10: Single-pass agent work without audit FORBIDDEN. Beilinson loop mandatory for chapters.
RS-12: The programme is THREE volumes, not two.
RS-13: In Vol II, gravity is the CLIMAX (Part VI), not middle content.
RS-14: Introduction orients, Overture instantiates. Introduction first, Overture second.
RS-15: Koszul programme before higher_genus in the dependency DAG.
RS-19: The preface is a complete survey, not a compressed summary. Save before compressing.

## Agent Anti-Patterns

AAP2: Terminology rename MUST be atomic across all three volumes in single session.
AAP3: Formula implemented ONCE in canonical module, import everywhere.
AAP4: \begin{proof} only after theorem/prop/lemma with ProvedHere. Use Remark[Evidence] for conjectures.
AAP5: Build-artifact commits batched with content. Never standalone artifact commits.
AAP6: Search ALL THREE volumes before downgrading a status tag.
AAP8: README claims independently verifiable by test suite.
AAP9: Wait for ALL agents to finish before launching new batch.
AAP10: After agent completion, verify BOTH engine AND test files exist.
AAP11: Every hardcoded expected value derivable by 2+ independent paths.
AAP12: Asymptotic tolerance proportional to 1/log(N) or verified by two methods.
AAP13: NEVER downgrade model without user permission. Wait and retry on rate limit.
AAP14: Unique branch name per agent.
AAP15: Serialize builds or use isolated worktrees. Parallel pdflatex kills.
AAP16: git stash FORBIDDEN. Use git diff > patch.diff + git apply instead.
AAP17: Verify edits via git diff, not agent narrative.
AAP18: Confabulating operadic theory -> compute or cite (Loday-Vallette, Vallette, Livernet). NEVER analogize.

## Structural Facts

**Shadow tower**: Theta_A := D_A - d_0 is MC (thm:mc2-bar-intrinsic). kappa, C, Q are projections. All-degree convergence PROVED. G/L/C/M: G(r=2,Heis), L(r=3,aff), C(r=4,betagamma), M(r=inf,Vir/W_N). Shadow depth != Koszulness. Delta=8*kappa*S_4: Delta=0 <-> finite tower. SC formality: A is SC-formal iff class G (prop:sc-formal-iff-class-g). Depth gap: d_alg in {0,1,2,inf}; gap at 3 (prop:depth-gap-trichotomy). ChirHoch^1(V_k(g)) = g with total dim = dim(g)+2 (prop:chirhoch1-affine-km).

**Convolution**: dg Lie Conv_str is strict model of L-inf Conv_inf. MC moduli coincide. Full L-inf needed for transfer/formality/gauge equivalence.

**E_1 primacy**: B^ord is the primitive (Stasheff). av: g^{E_1} -> g^mod lossy Sigma_n-coinvariant projection. av(r(z))=kappa at degree 2. All standard chiral algebras are E_inf (local); E_1=nonlocal (Yangian, EK quantum VA). NEVER "E_inf means no OPE poles."

**Three-pillar constraints**: (1) Convolution sL-inf hom_alpha(C,A) is NOT strict Lie. (2) hom_alpha fails as bifunctor in both slots simultaneously (RNW19). MC3 one slot at a time. (3) Log FM != classical FM; requires snc pair (X,D).

## Architecture

**Vol I**: Introduction + Overture (Heisenberg CG opening, unnumbered) + Part I (Bar Complex: Thms A-D+H, 12 Koszul equivs) + Part II (Characteristic Datum: shadow tower, G/L/C/M/M*/W, higher-genus, E_1 modular) + Part III (Standard Landscape: all families, census) + Part IV (Physics Bridges: E_n, factorization envelopes, derived Langlands) + Part V (Seven Faces of r(z): F1 bar-cobar twisting, F2 DNP25 line-operator, F3 Khan-Zeng PVA, F4 Gaiotto-Zeng sphere Hamiltonians, F5 Drinfeld Yangian, F6 Sklyanin/STS83, F7 FFR94 Gaudin) + Part VI (Frontier) + Appendices.

**Vol II** (~1,500pp, ~/chiral-bar-cobar-vol2): SC^{ch,top} bar differential = holomorphic factorization on C, coproduct = topological factorization on R. Seven parts: I(Open Primitive) II(E_1 Core) III(Seven Faces) IV(Char Datum) V(HT Landscape) VI(3D Quantum Gravity = CLIMAX) VII(Frontier). See Vol II CLAUDE.md for V2-AP1-24 (E_1/E_inf hierarchy).

**Vol III** (~206pp, ~/calabi-yau-quantum-groups): CY -> chiral functor Phi. Five parts: I(CY Engine) II(CY Char Datum) III(CY Landscape) IV(Seven Faces r_CY) V(CY Frontier). 12 stub chapters. kappa subscripts MANDATORY. See Vol III CLAUDE.md for AP-CY1-8 (kappa-spectrum).

## Writing Standard

Channel: Gelfand (inevitability), Beilinson (falsification), Drinfeld (unifying principle), Kazhdan (compression), Etingof (clarity), Polyakov (physics=theorem), Nekrasov (seamless passage), Kapranov (higher structure IS math), Ginzburg (every object solves a problem), Costello (factorization), Gaiotto (dualities compute), Witten (physical insight precedes proof). **Convergent loop mandatory**: WRITE -> REIMAGINE (Gelfand/Beilinson/Drinfeld) -> REWRITE from scratch -> BEILINSON AUDIT (adversarial) -> REIMAGINE AGAIN -> REWRITE AGAIN -> CONVERGE (zero findings >= MODERATE). Preface/intro: 3+ iterations. Chapter openings: 2+. **CG structural moves**: deficiency opening, unique survivor, instant computation, forced transition, decomposition table, dichotomy, sentence-as-theorem.

## Skills

```
/build                      Build all three volumes, tests, census
/audit [target]             Deep Beilinson audit (6 hostile examiners)
/chriss-ginzburg-rectify [file]  Full 5-phase CG + Beilinson rectification (canonical)
/rectify-all                Rectification across all chapters, all volumes, parallel tiers
/research-swarm [topic]     Launch 30+ research agents on frontier
/verify [claim]             Multi-path verification (3+ independent paths)
/propagate [pattern]        Cross-volume AP5 propagation check
/compute-engine [name]      Scaffold compute engine with multi-path tests
/beilinson-swarm            Beilinson rectification swarm across all chapters
/rectify [file]             Beilinson rectification loop (lighter than CG)
/beilinson-rectify [file]   CG fortification + rectification (v1, use /chriss-ginzburg-rectify for v2)
/chriss-ginzburg-rectify-v1 [file]  CG rectification v1 (superseded by /chriss-ginzburg-rectify)
```

RS-1,2,5,6,7,8,11,16,17,18,20 merged into corresponding APs above. AP16 superseded by AP27.

## Build

```
pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast    # Vol I
cd ~/chiral-bar-cobar-vol2 && make                                # Vol II
cd ~/calabi-yau-quantum-groups && make fast                       # Vol III
make test                                                         # Fast tests
make test-full                                                    # All tests (~119K)
python3 scripts/generate_metadata.py                              # Census
```

CAUTION: Watcher spawns competing pdflatex; always kill before builds.

## Session Protocol

1. Read this file. 2. Build: `pkill -9 -f pdflatex; sleep 2; make fast`. 3. Tests: `make test`. 4. `git log --oneline -10`. 5. Read .tex source before any edit (never from memory). 6. After each change: build+test. After each correction: grep ALL THREE volumes (AP5). 7. Never guess a formula: compute or cite. Check landscape_census.tex (AP1). 8. Apply convergent writing loop to all prose. 9. Session end: build all three volumes, run tests, summarize errors by class. 10. Before first Edit, read the HOT ZONE section (HZ-1 through HZ-10) and run the Pre-Edit Verification Protocol mental check: is the pending edit touching an r-matrix, kappa, bar complex, label, Vol III kappa, cross-volume formula, scope quantifier, or differential form? If yes, fill the corresponding PE-1..PE-12 template as a fenced block in the reply BEFORE invoking Edit, ending with `verdict: ACCEPT`.

Details: FRONTIER.md (research programme status), MEMORY.md (session history), concordance.tex (constitution).

## LaTeX

All macros in main.tex preamble. NEVER \newcommand in chapters (use \providecommand). Memoir class, EB Garamond (newtxmath + ebgaramond). Tags: \ClaimStatusProvedHere, \ClaimStatusProvedElsewhere, \ClaimStatusConjectured, \ClaimStatusHeuristic. Label everything with \label{def:}, \label{thm:}. Cross-reference with \ref. Do not add packages without checking compatibility. Do not create new .tex files when content belongs in existing chapters.

## Git

All commits authored by Raeez Lorgat. NEVER credit an LLM. No co-authored-by, no generated-by, no AI attribution anywhere. Constitution: concordance.tex. git stash FORBIDDEN (AAP16).
