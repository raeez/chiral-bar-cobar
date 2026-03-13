# SESSION PROMPT v25 — The Fourier Seed
# Launch: "Read notes/SESSION_PROMPT_v25.md and execute it."
# Supersedes: v24 (doctrinal stabilization). References CLAUDE.md for invariants.
# Date: March 2026
# Trigger: The monograph describes its bar construction as a non-abelian Fourier
#          transform but never computes it as one. This session constructs it.

---

## DIRECTIVE

Write LaTeX. Construct the bar complex as a one-dimensional non-abelian Fourier
transform through four explicit computations of increasing complexity. Prove that
it specializes to the classical bar-cobar adjunction when the curve degenerates to
a point. Identify Theorems A–D as the four structural properties of this transform.
Every output is a Definition, Proposition, Computation, Theorem, or Remark — never
a description of what should be written.

## METHOD GUARDRAILS

Apply the Chriss--Ginzburg method structurally, not stylistically:

1. Treat the chapter as synthesis mathematics:
   the computations are not warmups but the direct route to the
   governing mechanism.
2. Bring in background only at the moment the Fourier transform
   construction requires it.
3. Let each section arise from a failure of the previous level:
   point to curve, genus~0 to elliptic, fixed curve to families.
4. Use the examples as frame tiles in a mosaic of one subject, not as
   detached illustrations.
5. State every bridge to geometry, representation theory, or physics as
   a theorematic identification or a precise status-tagged remark.

---

## PHASE 0: GROUND (read only, no writing)

Read IN THIS ORDER:

```
1. CLAUDE.md                                         — all invariants, especially Critical Pitfalls
2. main.tex:633-718                                  — current abstract
3. chapters/theory/introduction.tex:1-80             — current opening
4. chapters/theory/bar_cobar_construction.tex:1-200  — bar definition + differential components
5. chapters/frame/heisenberg_frame.tex:1-200         — frame atom
6. chapters/connections/concordance.tex:1-100        — constitutional status
7. bibliography/references.tex                       — existing references (for Loday-Vallette, Polishchuk, etc.)
```

**Gate**: Do not write LaTeX until all 7 are read. In extended thinking, write the
five objects you will construct:

1. The propagator kernel η_{ij} = d log(z_i - z_j) and its genus-1 correction
2. The integral transform B_n(A) with three-component differential
3. Four explicit evaluations: point, P^1/Heisenberg, E_τ/Heisenberg, P^1/KM
4. The specialization theorem (curve → point recovers classical bar)
5. The identification of Theorems A–D as transform properties

---

## PHASE 1: BUILD

Write `chapters/theory/fourier_seed.tex` (~15 pages). This is a new chapter placed
between the introduction and bar_cobar_construction.tex. (Justification for new
file: this is foundational motivating content that precedes the general theory; the
introduction is already 1300+ lines; CLAUDE.md prohibits new files only when content
belongs in an existing chapter — this content doesn't.)

### §1. The kernel

**Definition.** The logarithmic propagator on C_2(A^1):

  η_{ij} = d log(z_i - z_j) = (dz_i - dz_j)/(z_i - z_j).

**Proposition** (\ClaimStatusProvedHere). Three properties:

1. η_{ij} has a simple pole along Δ_{ij} with residue 1.
2. dη_{ij} = 0 on C_2(X) \ Δ.
3. (Arnold relation) η_{12} ∧ η_{23} + η_{23} ∧ η_{31} + η_{31} ∧ η_{12} = 0
   in Ω^2(C̄_3(X), log D).

Proof: write the three-term computation explicitly — substitute
η_{ij} = (dz_i - dz_j)/(z_i - z_j), expand the wedge products, collect terms by
numerator. The cancellation is exact.

**Proposition** (\ClaimStatusProvedHere). On E_τ, the propagator acquires a period
correction:

  η^{(1)}_{ij} = d log θ_1(z_i - z_j | τ) + 2πi Im(z_i - z_j)/Im(τ) · dz̄_i.

The Arnold relation fails: its residual equals ω_1, the Arakelov (1,1)-form.
Compute this failure as a 3-line chain of equalities.


### §2. The transform

**Definition.** The bar complex at tensor power n:

  B_n(A) = (s^{-1} Ā)^{⊗n} ⊗ Ω^•(C̄_n(X), log D)

with differential d = d_int + d_res + d_dR.

(Reference: the general definition appears in Chapter~\ref{ch:bar-cobar}. Here we
compute it.)

**Computation (a): X = Spec k, A = Λ(V)** (exterior algebra on a point).

C_n(pt) = pt. No forms. No propagator. d_dR = 0, d_res reduces to the Koszul
differential. Result: B(Λ(V)) = Sym^c(s^{-1}V) with zero differential. State as
Proposition. The exterior algebra is the Fourier transform of the symmetric
coalgebra. This is Com^! = Lie (check against CLAUDE.md: yes,
Λ = free Com-algebra, dual coalgebra is cofree Lie^!-coalgebra).

**Computation (b): X = P^1, A = H_k** (Heisenberg).

Write the OPE: α(z)α(w) = k/(z-w)^2 + reg.

- n=1: B_1 = s^{-1}α. No form factor. d = 0.
- n=2: Element s^{-1}α(z_1) ⊗ s^{-1}α(z_2) ⊗ η_{12}. Compute:

    d_res(s^{-1}α(z_1) ⊗ s^{-1}α(z_2) ⊗ η_{12})
      = Res_{z_1=z_2} [k/(z_1-z_2)^2] · d log(z_1-z_2)
      = k · 1.

  Write this as a Computation environment with every step.

- n=3: Three boundary strata D_{12}, D_{23}, D_{13}. Write the three residue
  contributions. Arnold relation forces d^2 = 0. Write the cancellation explicitly.

**Theorem** (\ClaimStatusProvedHere): B(H_k) ≅ Sym^{ch,c}(V*[-1]) with induced
level -k.

Remark: H_k is NOT self-dual. H_k^! = Sym^{ch}(V*), not H_{-k}. (CLAUDE.md check.)

**Computation (c): X = E_τ, A = H_k** (elliptic curve).

Same elements. Replace η_{12} → η^{(1)}_{12}. Arnold failure ⟹ d_fib^2 = k · ω_1.
Period integral correction:

  D_1 = d_fib + Σ_{a=1}^{g} t_a ⊗ ∮_{A_a}

satisfies D_1^2 = 0. Write this for g=1 with the single A-cycle.

**Proposition** (\ClaimStatusProvedElsewhere, ref Polishchuk or Faltings): For k=1,
the transform B_{E_τ}(H_1) is the Fourier–Mukai kernel P on
Jac(E_τ) × Jac^(E_τ).

(Verify that Polishchuk is in bibliography/references.tex. If not, add the
reference.)

**Computation (d): X = P^1, A = ĝ_k** (Kac–Moody).

OPE: J^a(z)J^b(w) ~ kκ^{ab}/(z-w)^2 + f^{ab}_c J^c(w)/(z-w).

n=2 bar differential: TWO contributions.
- First-order pole → bracket term f^{ab}_c · s^{-1}J^c ⊗ η_{12}
- Second-order pole → Killing term kκ^{ab} · 1

Result: B(ĝ_k) is the curved chiral Chevalley–Eilenberg coalgebra
Ĉ^•_ch(g, kκ).


### §3. Specialization

**Theorem** (\ClaimStatusProvedHere). (Specialization to a point.) Let X = Spec k.
Then:

1. C̄_n(Spec k) = Spec k for all n.
2. Ω^•(C̄_n, log D) = k (no forms, no propagator).
3. d_dR = 0 and d_res reduces to the binary bracket differential.
4. B_X(A) reduces to T^c(s^{-1}Ā, d_bracket), the classical bar construction of
   Loday–Vallette.

Proof: items (1)–(3) are immediate. Item (4) follows because the general
three-component differential d = d_int + d_res + d_dR collapses to d_int + d_res
when X = pt, and d_res at X = pt extracts only the leading OPE coefficient, which
is the binary product.

Write the specialization diagram as a tikzcd:

  ChirAlg(X) --B_X--> Fact^c(Ran X)
      |                      |
      | X=pt                 | X=pt
      v                      v
  Alg_k -----B-----> CoAlg_k


### §4. The four properties

**Theorem** (The four properties of the Fourier transform).

(A) Intertwining. D_{Ran} ∘ B_X ≃ B_X ∘ (-)^!. (= Theorem A.)

(B) Inversion. On the Koszul locus, Ω(B(A)) →~ A. (= Theorem B.)

(C) Plancherel. Q_g(A) ⊕ Q_g(A!) ≃ RΓ(M̄_g, Z_A). (= Theorem C.)

(D) Characteristic function. κ(A) determines the genus expansion; its generating
    function is the Â-genus. (= Theorem D.)

**Remark** (Classical Fourier analogues).

| Property | Chiral (this monograph)        | Classical Fourier              |
|----------|-------------------------------|-------------------------------|
| (A)      | Verdier intertwining          | f̂(f·g) = f̂(f) * f̂(g)       |
| (B)      | Bar-cobar inversion           | f̂^{-1} ∘ f̂ = id              |
| (C)      | Lagrangian complementarity    | ||f||² = ||f̂||² (Parseval)    |
| (D)      | Modular characteristic κ      | Char. function determines moments |

**Remark.** These four properties and the specialization theorem (§3) contain the
entire subject. The remainder of Part 1 develops the proofs. Part 2 computes the
transform for each standard family.


### §5. The landscape (~1 page)

Table of the Fourier transform evaluated on each standard family:

| A           | B(A)                               | κ(A)                         | c(A)                         |
|-------------|------------------------------------|-----------------------------|------------------------------|
| H_k         | Sym^{ch,c}(V*[-1]), level -k       | k                           | 1                            |
| ĝ_k        | Curved CE coalgebra, level -k-2h^∨ | k·dim(g)/(k+h^∨)           | k·dim(g)/(k+h^∨)           |
| Vir_c       | Curved CE coalgebra                | c/2                         | c                            |
| W_N         | Via DS reduction                   | DS formula                  | DS formula                   |

State: "The detailed computations appear in Part 2 (Chapters~\ref{ch:...}–\ref{ch:...})."


### §6. Genus as deformation variable (preview, ~1 page)

**Remark** (\ClaimStatusProvedHere, ref thm:mc2-full-resolution). At genus g ≥ 1, the
bar complex B_g(A) is a family of curved cochain complexes over M̄_g. The proved
invariant κ(A) is the scalar shadow of the proved Maurer–Cartan class

  Θ_A ∈ MC(Def_cyc(A) ⊗̂ RΓ(M̄_{g,•}, Q)).

What remains open is the outer categorical and infinite-generator lift
of this deformation package: coderived/factorization functoriality,
the DK/KL extension, and the MC4 coefficient comparison.

Tag explicitly: κ and Θ_A are \ClaimStatusProvedHere; the outer
categorical lift beyond the current theorem surface is programme.

---

## PHASE 2: INTEGRATE (five surgical edits)

### 2a. main.tex

Insert `\include{chapters/theory/fourier_seed}` between
`\include{chapters/theory/introduction}` and
`\include{chapters/theory/bar_cobar_construction}`.

### 2b. Abstract (main.tex:658)

After "For the Heisenberg algebra on an elliptic curve this specializes to the
classical Fourier–Mukai transform on the Jacobian." ADD:

"When $X$ degenerates to a point, the propagator vanishes and the transform reduces
to the classical bar--cobar adjunction of Loday--Vallette; the entire theory of
operadic Koszul duality is the zero-dimensional shadow."

### 2c. Introduction (chapters/theory/introduction.tex, opening section)

Add a Remark (~3 sentences) after the logarithmic 1-form discussion: "The bar
construction is a one-dimensional non-abelian Fourier transform whose kernel is the
logarithmic propagator. Its four structural properties — intertwining, inversion,
Plancherel, characteristic function — are Theorems A–D. The explicit computations
of Chapter~\ref{ch:fourier-seed} exhibit this identification for the Heisenberg and
Kac–Moody families before the general theory."

### 2d. bar_cobar_construction.tex (opening)

Add a Remark: "The reader who has worked through the Fourier seed computations
(Chapter~\ref{ch:fourier-seed}) has already seen the bar differential extract OPE
coefficients via residues against the logarithmic propagator. We now develop the
general construction."

### 2e. heisenberg_frame.tex

Add a Remark connecting the Heisenberg bar to the Fourier identification: "The bar
complex B(H_k) is the abelian one-dimensional Fourier transform of the Heisenberg
algebra. The Â-genus appearing in Theorem D is its characteristic function — the
analogue of e^{-t|ξ|^2} for the classical heat kernel."

---

## PHASE 3: VERIFY

1. `pkill -9 -f pdflatex 2>/dev/null || true; sleep 2; make fast` — must compile clean
2. Every formula vs CLAUDE.md Critical Pitfalls (bar = desuspension s^{-1};
   Com^! = Lie; Heisenberg not self-dual; Arnold signs;
   prime form = K^{-1/2} ⊗ K^{-1/2}; Sugawara coefficient)
3. Every \ClaimStatus tag matches actual proof density
4. No \newcommand in chapter file — use preamble macros only
5. All \label follow convention: def:, thm:, prop:, rem:, comp:
6. All cross-references use \ref / \eqref, never hardcoded

---

## ANTI-PATTERNS (hard constraints)

**A1**: No meta-narrative. Sentences beginning "One can observe," "The theory
naturally," "The monograph yearns," "It is worth noting" are BANNED. Write
mathematical content.

**A2**: No commentary without LaTeX. If you write 3+ consecutive sentences of
English that are not inside a proof/remark environment, you are meta-narrating.
Stop. Write the Definition or Computation instead.

**A3**: No invariant violations. BEFORE writing any formula, check it against
CLAUDE.md Critical Pitfalls. The penalty for a wrong sign or convention is a
corrupted manuscript.

**A4**: Scope bound. ONE new file + FIVE surgical edits. If you feel the urge to
write a second new chapter, resist. Depth over breadth.

**A5**: Time gate. If Phase 0 reading is complete and you have not begun writing
LaTeX, you are in a planning loop. Begin writing §1 immediately.

**A6**: No vague labels. Every mathematical environment gets a \label. Every forward
reference uses \ref. "See the later chapter" without \ref is banned.

---

## SUCCESS CRITERIA

| # | Criterion                                                     | How to verify                |
|---|---------------------------------------------------------------|------------------------------|
| 1 | A reader can compute B_2(H_k) by hand after reading §2(b)    | The residue computation has every step |
| 2 | Specialization X → pt is a proved Proposition with proof      | Check fourier_seed.tex §3    |
| 3 | Theorems A–D are explicitly identified as Fourier properties  | Check §4                     |
| 4 | Genus-1 curvature for Heisenberg is computed line by line     | Check §2(c)                  |
| 5 | Classical Fourier analogues appear as a Remark                | Check §4 table               |
| 6 | `make fast` compiles cleanly                                  | Run it                       |
| 7 | All \ClaimStatus tags are correct                             | Grep and verify              |
