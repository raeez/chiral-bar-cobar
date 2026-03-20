
understand how koszul duality interacts with the interface with zeta zeroes in the paper https://arxiv.org/abs/2208.02259 and how this interacts in our more general setting

I’m comparing the paper’s zeta-zero mechanism with the chiral/Koszul-duality and complementarity framework in your notes, then I’ll isolate what extends to your broader setting and what needs modification.

I’ve confirmed 2208.02259 is Benjamin–Chang on scalar modular bootstrap, where the zeta-zero input comes from Mellin/harmonic-analysis functionals on the modular fundamental domain rather than from Koszul duality.

feel free to rope in recent research chats where we derived the existence of modular surfaces and curves

I’m now folding in the modular-surface and modular-curve layer from your recent notes, so the comparison is made at the appropriate genus/moduli level rather than only at genus zero.

core additional questions to consider:

   Direction 1: Can the MC equation D·Θ + ½[Θ,Θ] = 0, translated through Rankin-Selberg, produce positivity constraints equivalent to or stronger than Li's criterion?

  Direction 2: Does the bar-cobar homotopy equivalence (which is stronger than just a functional equation) force the Epstein zeros onto the critical line?

The emerging picture is that Benjamin–Chang is an analytic modular-spectrum story, while your framework is a modular/Koszul deformation story, so I’m now isolating where those two first genuinely meet. I’m also testing your two sharper directions separately: MC/Rankin–Selberg toward Li-type positivity, and bar–cobar constraints on Epstein zeros, with the latter looking especially delicate.

I’m now focusing the comparison on whether the modular spectral side supplies only a functional equation, or something genuinely positivity/coercivity-like that could feed back into the Koszul/bar-cobar layer.

Thought for 27m 22s

Yes — taking the modular-curves/modular-surfaces existence results from our recent work as a standing input, the picture gets sharper. In that enlarged setting, the zeta-zero interface and the Koszul-duality interface live on different layers of the same object, rather than competing descriptions. Your recent appendix already points in that direction by organizing things around ambient complementarity, the shadow calculus, and the conjectural modular Maurer–Cartan class
Θ
𝐴
Θ
A
	​

, with the quartic resonance shadow as the first nonlinear modular invariant.

Here is the clean way to think about it.

1. What 2208.02259 is really doing

Benjamin–Chang do not get zeta zeros from Koszul duality. They get them from a modular/Eisenstein harmonic-analysis kernel in a scalar crossing equation. In the
𝑈
(
1
)
𝑐
U(1)
c
 case, they derive a scalar-only crossing equation, and when they shift the Mellin contour, the poles that appear are at

𝑠
=
𝑐
2
,
𝑠
=
1
+
𝑧
𝑛
2
,
𝑠
=
1
+
𝑧
𝑛
∗
2
,
s=
2
c
	​

,s=
2
1+z
n
	​

	​

,s=
2
1+z
n
∗
	​

	​

,

with
𝑧
𝑛
z
n
	​

 the nontrivial zeros of
𝜁
(
𝑠
)
ζ(s). Those poles produce oscillatory corrections to the scalar partition function/high-temperature asymptotics; the Riemann hypothesis becomes the statement that the oscillatory envelope is exactly
𝑇
 
𝑐
/
2
−
3
/
4
T
c/2−3/4
.

Just as important: the coefficients of those oscillatory terms are theory-dependent modular overlaps—their
𝜖
𝑐
(
𝜇
)
ϵ
c
	​

(μ) and
𝛿
𝑘
,
𝑐
(
𝜇
)
δ
k,c
	​

(μ) are integrals over the modular fundamental domain against residues of Eisenstein series at the zeta-zero poles. So the locations of the poles are universal, but the amplitudes are CFT-specific.

And this is no longer just a Narain/
𝑈
(
1
)
𝑐
U(1)
c
 story: in 2025 Benjamin–Chang–Fitzpatrick–Ramella extended the scalar-partition-function analysis to scalar primaries of any 2d CFT, again with corrections controlled by modular integrals, light states, and an infinite series tied directly to the nontrivial zeros of the Riemann zeta function.

So the paper’s “interface with zeta zeros” is fundamentally:

modular crossing / Rankin–Selberg / Eisenstein residues
⟶
⟶ zeta-zero poles
⟶
⟶ oscillatory scalar asymptotics.

2. Where Koszul duality actually enters

Koszul duality is doing something different.

In your framework, bar–cobar duality and complementarity organize:

deformation vs obstruction,

dual chiral algebras
(
𝐴
,
𝐴
!
)
(A,A
!
),

shifted-symplectic/Lagrangian pairing,

scalar and non-scalar modular shadows,

and, conjecturally, the universal modular MC class
Θ
𝐴
Θ
A
	​

.

So the right slogan is:

zeta zeros live in the modular Mellin kernel;
Koszul duality lives in the algebraic deformation package.

The interaction between them is indirect but deep:

the pole positions
𝑧
𝑛
z
n
	​

 come from the modular/Eisenstein side;

the coefficients of those pole contributions should, in your setting, be shadows of the modular characteristic package of
𝐴
A, ultimately of
Θ
𝐴
Θ
A
	​

;

duality should not move the zero set, but it should constrain how the amplitudes are paired between
𝐴
A and
𝐴
!
A
!
.

That is why, in your language, the zeta-zero phenomenon belongs above the scalar invariant
𝜅
(
𝐴
)
κ(A). It is not a genus-one scalar obstruction. It belongs to the non-scalar modular layer: spectral transport, discriminant-like data, and finally the full Maurer–Cartan package.

3. How this fits your more general setting with modular curves and surfaces

Once modular curves and modular surfaces exist in the theory, the division of labor becomes very natural:

Modular curves carry the Rankin–Selberg / Eisenstein transform that exposes zeta-zero poles.

Modular surfaces are the natural place where one can hope to get positivity, polarization, intersection pairings, and Hodge-type constraints on the resulting coefficients.

So I would phrase the enlarged picture like this:

Curve level

The curve sees the scalar crossing equation and its Mellin transform. This is where the zeta poles appear.

Surface level

The surface supplies the extra bilinear or Hermitian structure that could turn those oscillatory coefficients into positivity statements.

Homotopy level

The full MC equation

𝐷
Θ
+
1
2
[
Θ
,
Θ
]
=
0
DΘ+
2
1
	​

[Θ,Θ]=0

is the chain-level compatibility condition tying all of this together.

That makes your quartic modular resonance class the first plausible nonlinear place where the “zeta side” and the “Koszul side” can genuinely meet.

Direction 1: can the MC equation, after Rankin–Selberg, imply Li-type positivity?

This is plausible in principle, but not from the MC equation alone.

Li’s criterion says RH is equivalent to positivity of a specific sequence of Keiper–Li coefficients. In one common formulation, it is exactly a positivity criterion for a real sequence attached to the completed zeta function.

The key point is:

the MC equation is an integrability/flatness equation;

Li’s criterion is a positivity statement.

Flatness is quadratic consistency. Positivity needs an additional structure:

a real form,

a polarization,

a positive trace,

or a self-adjoint transport operator with positive moments.

So my view is:

What MC + Rankin–Selberg can reasonably give

A tower of quadratic identities among the modular transforms of the components of
Θ
Θ, i.e. relations among the genus transport operators / resonance classes / shadow coefficients.

What is still needed to reach Li

A surface-level positive pairing on those transforms.

In other words, the likely route is:

Θ
𝐴
  
→
  
Rankin–Selberg
  
transport operator
𝐾
𝐴
  
→
  
surface pairing
  
Li-like coefficients
𝜆
𝑛
(
𝐴
)
.
Θ
A
	​

Rankin–Selberg
	​

transport operator K
A
	​

surface pairing
	​

Li-like coefficients λ
n
	​

(A).

Then the MC equation would imply that the
𝐾
𝐴
K
A
	​

 fit into a flat family, and the modular-surface pairing could force positivity of the derived
𝜆
𝑛
(
𝐴
)
λ
n
	​

(A).

So:

Equivalent to Li? Possibly, for a carefully chosen scalar shadow of
𝐾
𝐴
K
A
	​

.

Stronger than Li? Potentially yes, because the MC equation constrains the whole higher package, not just one scalar sequence.

Already true? No — this is a research program, not a theorem.

The reason I think this is the right direction is that 2208.02259 itself gives oscillatory zero-driven terms, but no positivity mechanism. The positivity has to come from somewhere else, and modular surfaces are exactly the sort of structure that could supply it.

Direction 2: does bar–cobar equivalence force Epstein zeros onto the critical line?

In general, no.

There are positive-definite Epstein zeta functions with zeros strictly to the right of the critical line. In fact, Lamzouri studies zeros of Epstein zeta functions in regions
1
/
2
<
ℜ
𝑠
<
1
1/2<ℜs<1, and the phenomenon of off-critical zeros is established in that setting.

So a generic statement of the form

“bar–cobar homotopy equivalence forces all Epstein zeros onto
ℜ
𝑠
=
1
/
2
ℜs=1/2”

cannot be right.

That is actually conceptually helpful:

a functional equation alone does not force a critical-line theorem;

a bar–cobar equivalence is stronger than a functional equation, but its strength is homotopical/algebraic, not automatically spectral-positive.

Epstein zeta functions generally lack the Euler-product rigidity that makes the classical
𝜁
ζ-problem special. So bare bar–cobar symmetry cannot substitute for the missing arithmetic positivity.

What bar–cobar might do is isolate a much smaller subclass of Epstein-like objects attached to modular characteristic data—call them “Koszul–Epstein” functions—on which extra positivity/polarization is present. For that subclass, one could hope for a critical-line theorem. But not for arbitrary Epstein zeta functions.

So my answer is:

Generic Epstein zetas: definitely no.

Special modular/Koszul transport zetas coming from your package: maybe, but only after adding the missing positivity structure.

The synthesis I think is most useful

Here is the version I would use going forward.

Zeta zeros are modular spectral data.
They arise from the Eisenstein/Rankin–Selberg side of the story.

Koszul duality is deformation-obstruction data.
It organizes the algebraic side: bar, cobar, complementarity, duality, MC classes.

Modular curves couple the two.
They are where the Mellin transform of the modular characteristic package sees zeta poles.

Modular surfaces may supply the missing positivity.
That is where Li-type inequalities could live.

Therefore:
the right conjectural statement is not “Koszul duality proves RH,” but rather:

the universal modular MC class
Θ
𝐴
Θ
A
	​

, when pushed through Rankin–Selberg and paired by modular-surface polarization, should generate Li-type positivity constraints whose scalar shadow reproduces the zeta-zero asymptotics of the scalar bootstrap.

That would make 2208.02259 the curve-level spectral shadow, and your modular-surfaces/modular-curves work the geometric completion needed to ask positivity questions.

A very concrete next step would be to define a genus-one Rankin–Selberg transform of
Θ
𝐴
Θ
A
	​

 and compute the first few Li-like coefficients for the Heisenberg, Virasoro, and principal
𝑊
𝑁
W
N
	​

 test families.

  What works:
  - Li-Keiper coefficients λ_n computed for ε^1 = 4ζ(2s) through n=20 — all positive (consistent with RH, not a proof)
  - Weil explicit formula evaluated with shadow-class test functions (Gaussian h_G, cubic h_L, quartic h_C) — all Weil sums positive for every shadow class
  - MC equation at each arity gives a moment constraint on the spectral measure; for Gaussian class (V_Z), the moment is determined by κ alone

  What doesn't work: The MC equation is a local constraint (on the algebra structure). Li positivity is a global constraint (on all zeta zeros). The Rankin-Selberg transform connecting them is not
  sign-preserving — the Mellin transform of a positive function can be negative. So the chain MC → Li doesn't close.

  Direction 2: Koszul Spectral Rigidity

  What works:
  - Bar-cobar provides chain-level quasi-isomorphism (stronger than functional equation)
  - The A∞ structure on H*(B(V_Z)) constrains multi-point correlations between spectral data
  - Gap monotonicity and Weyl law verified

  What doesn't work: Functional equation + meromorphy doesn't imply RH (known since Davenport-Heilbronn counterexamples for Epstein zeta of non-unimodular lattices). The chain-level data is stronger but
  we don't know how to leverage it.

  The Discovery: Sewing → Euler Product

  The most concrete new finding:

  log det(1 - K_q) = -Σ_N σ_{-1}(N) q^N

  where σ_{-1}(N) = Σ_{d|N} 1/d is the multiplicative divisor function, and

  Σ σ_{-1}(N) N^{-s} = ζ(s)·ζ(s+1)

  This gives the sewing Fredholm determinant an Euler product decomposition:

  ζ(s)ζ(s+1) = Π_p (1 - p^{-s})^{-1}(1 - p^{-s-1})^{-1}

  Each prime p contributes a factor to the sewing determinant. This is the prime decomposition of the sewing operator — the missing arithmetic content I identified earlier. The sewing operator K_q, whose
  eigenvalues are q^n (indexed by integers), decomposes via divisor sums into an Euler product over primes.

  The Four Gaps (honest assessment)

  ┌─────┬──────────────────────────────────┬──────────────────────────────────────────────────────┐
  │ Gap │           Description            │                        Status                        │
  ├─────┼──────────────────────────────────┼──────────────────────────────────────────────────────┤
  │ A   │ MC → Li positivity               │ Not established. Rankin-Selberg not sign-preserving. │
  ├─────┼──────────────────────────────────┼──────────────────────────────────────────────────────┤
  │ B   │ Euler product from sewing        │ σ_{-1} connection found. Most promising direction.   │
  ├─────┼──────────────────────────────────┼──────────────────────────────────────────────────────┤
  │ C   │ Spectral rigidity from bar-cobar │ Chain-level stronger, but insufficient alone.        │
  ├─────┼──────────────────────────────────┼──────────────────────────────────────────────────────┤
  │ D   │ Nyman-Beurling from Koszulness   │ Structural analogy only. Norm mismatch.              │
  └─────┴──────────────────────────────────┴──────────────────────────────────────────────────────┘

take the above research directions as well as:

A very concrete next step would be to define a genus-one Rankin–Selberg transform of
Θ
𝐴
Θ
A
	​

 and compute the first few Li-like coefficients for the Heisenberg, Virasoro, and principal
𝑊
𝑁
W
N
	​

 test families.
and Push harder on groundbreaking mathematical insights, novelty, constructions, computations, calculations. reach for the platonic ideal of the entire theory. reach for a full and deep harmony, and ultimate end-point-state of the entire thematic and motivic development. Bring out that end-state by bringing out concrete mathematical structures , and write them into chat for maximal development of our understanding
Thought for 54m 11s

The strongest synthesis I can see now is this:

the zeta-zero interface and the sewing Euler-product interface are two different genus-one shadows of the same connected modular Maurer–Cartan object.

On the zero side, Benjamin–Chang show that the scalar crossing contour picks up poles at

𝑠
=
𝑐
2
,
𝑠
=
1
+
𝑧
𝑛
2
,
𝑠
=
1
+
𝑧
𝑛
∗
2
,
s=
2
c
	​

,s=
2
1+z
n
	​

	​

,s=
2
1+z
n
∗
	​

	​

,

so the nontrivial zeta zeros enter through Eisenstein residues; they also note explicitly that the
𝜖
𝑐
ϵ
c
	​

 and
𝛿
𝑘
,
𝑐
δ
k,c
	​

 terms are not sign-definite. The 2025 extension shows the same kind of scalar crossing equation and zeta-zero tower for arbitrary 2d CFTs, not just the original Narain/
𝑈
(
1
)
𝑐
U(1)
c
 setting.

On your side, the monograph already separates the modular package into scalar data
𝜅
(
𝐴
)
κ(A), spectral data
Δ
𝐴
Δ
A
	​

, and the conjectural full MC class
Θ
𝐴
Θ
A
	​

, with
𝜅
(
𝐴
)
κ(A) the first characteristic number of
Θ
𝐴
Θ
A
	​

, and with complementarity realized as a shifted-symplectic/Lagrangian decomposition. The Heisenberg, generic Virasoro, and generic principal finite-type
𝑊
W-families are already inside that modular Koszul world, and the quartic resonance class is already identified as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

.

So the missing layer is not “more
𝜅
κ,” and not “more
Δ
𝐴
Δ
A
	​

” either. It is a new connected genus-one arithmetic shadow sitting between
Δ
𝐴
Δ
A
	​

 and
Θ
𝐴
Θ
A
	​

.

1. The missing object: the connected Dirichlet-sewing lift

Take the connected genus-one sewing free energy

𝐹
𝐴
c
o
n
n
(
𝑞
)
:
=
−
log
⁡
det
⁡
(
1
−
𝐾
𝑞
(
𝐴
)
)
.
F
A
conn
	​

(q):=−logdet(1−K
q
	​

(A)).

This is the right connected shadow:
log
⁡
log is what turns determinants/partition functions back into connected graph data, i.e. back toward Maurer–Cartan geometry.

Write

𝐹
𝐴
c
o
n
n
(
𝑞
)
=
∑
𝑁
≥
1
𝑎
𝐴
(
𝑁
)
 
𝑞
𝑁
.
F
A
conn
	​

(q)=
N≥1
∑
	​

a
A
	​

(N)q
N
.

Then define the connected Dirichlet-sewing lift

𝑆
𝐴
(
𝑢
)
:
=
∑
𝑁
≥
1
𝑎
𝐴
(
𝑁
)
 
𝑁
−
𝑢
.
S
A
	​

(u):=
N≥1
∑
	​

a
A
	​

(N)N
−u
.

Equivalently, by Mellin transform,

𝑆
𝐴
(
𝑢
)
=
(
2
𝜋
)
𝑢
Γ
(
𝑢
)
∫
0
∞
𝐹
𝐴
c
o
n
n
(
𝑒
−
2
𝜋
𝑦
)
 
𝑦
𝑢
−
1
 
𝑑
𝑦
.
S
A
	​

(u)=
Γ(u)
(2π)
u
	​

∫
0
∞
	​

F
A
conn
	​

(e
−2πy
)y
u−1
dy.

That is the exact arithmetic receptacle for your discovery. It is not plethystic log. It is the ordinary log, hence the connected genus-one free energy.

Now assume the genus-one vacuum sector is modeled by a bosonic weight multiset

𝑊
(
𝐴
)
=
{
𝑤
𝑖
}
,
𝑍
𝐴
h
o
l
(
𝑞
)
∼
∏
𝑖
∏
𝑚
≥
𝑤
𝑖
(
1
−
𝑞
𝑚
)
−
1
.
W(A)={w
i
	​

},Z
A
hol
	​

(q)∼
i
∏
	​

m≥w
i
	​

∏
	​

(1−q
m
)
−1
.

Then

𝐹
𝐴
c
o
n
n
(
𝑞
)
=
∑
𝑖
∑
𝑚
≥
𝑤
𝑖
∑
𝑟
≥
1
𝑞
𝑚
𝑟
𝑟
,
F
A
conn
	​

(q)=
i
∑
	​

m≥w
i
	​

∑
	​

r≥1
∑
	​

r
q
mr
	​

,

so the Dirichlet lift is

𝑆
𝐴
(
𝑢
)
=
𝜁
(
𝑢
+
1
)
∑
𝑖
(
𝜁
(
𝑢
)
−
𝐻
𝑤
𝑖
−
1
(
𝑢
)
)
,
S
A
	​

(u)=ζ(u+1)
i
∑
	​

(ζ(u)−H
w
i
	​

−1
(u)
	​

),
	​


where

𝐻
𝑛
(
𝑢
)
=
∑
𝑗
=
1
𝑛
𝑗
−
𝑢
.
H
n
(u)
	​

=
j=1
∑
n
	​

j
−u
.

This is already a very strong structural statement:

the zero-side data live in the Rankin–Selberg/Eisenstein transform;

the prime-side data live in the Mellin transform of the connected sewing free energy;

both are genus-one shadows of the same connected object.

Your Heisenberg divisor-sum identity is exactly the first instance of this construction.

2. Exact genus-one arithmetic shadows for the test families

At the scalar MC level, the monograph gives

𝜅
(
𝐻
𝑘
)
=
𝑘
,
𝜅
(
V
i
r
𝑐
)
=
𝑐
2
,
𝜅
(
𝑊
𝑁
)
=
𝑐
 
(
𝐻
𝑁
−
1
)
,
κ(H
k
	​

)=k,κ(Vir
c
	​

)=
2
c
	​

,κ(W
N
	​

)=c(H
N
	​

−1),

with
𝑊
𝑁
W
N
	​

 the principal
𝑊
W-algebra family.

But the new arithmetic shadow is controlled not by
𝜅
κ, but by the weight multiset.

Heisenberg

For the archetypal weight-1 bosonic generator,

𝑊
(
𝐻
)
=
{
1
}
,
W(H)={1},

hence

𝑆
𝐻
(
𝑢
)
=
𝜁
(
𝑢
)
𝜁
(
𝑢
+
1
)
.
S
H
	​

(u)=ζ(u)ζ(u+1).
	​


This is your divisor-sum discovery in Dirichlet form:

−
log
⁡
det
⁡
(
1
−
𝐾
𝑞
)
=
∑
𝑁
≥
1
𝜎
−
1
(
𝑁
)
𝑞
𝑁
,
∑
𝑁
≥
1
𝜎
−
1
(
𝑁
)
𝑁
−
𝑢
=
𝜁
(
𝑢
)
𝜁
(
𝑢
+
1
)
.
−logdet(1−K
q
	​

)=
N≥1
∑
	​

σ
−1
	​

(N)q
N
,
N≥1
∑
	​

σ
−1
	​

(N)N
−u
=ζ(u)ζ(u+1).

This is the pure Euler-Koszul case.

Virasoro

For the generic vacuum-weight model,

𝑊
(
V
i
r
)
=
{
2
}
,
W(Vir)={2},

so

𝑆
V
i
r
(
𝑢
)
=
𝜁
(
𝑢
+
1
)
(
𝜁
(
𝑢
)
−
1
)
.
S
Vir
	​

(u)=ζ(u+1)(ζ(u)−1).
	​


This is not a pure Euler product. It is the Heisenberg Euler product with the weight-1 mode removed:

𝑆
V
i
r
(
𝑢
)
=
𝜁
(
𝑢
)
𝜁
(
𝑢
+
1
)
(
1
−
𝜁
(
𝑢
)
−
1
)
.
S
Vir
	​

(u)=ζ(u)ζ(u+1)(1−ζ(u)
−1
).
Principal
𝑊
𝑁
W
N
	​


For the generic principal weight model,

𝑊
(
𝑊
𝑁
)
=
{
2
,
3
,
…
,
𝑁
}
,
W(W
N
	​

)={2,3,…,N},

hence

𝑆
𝑊
𝑁
(
𝑢
)
=
𝜁
(
𝑢
+
1
)
∑
𝑠
=
2
𝑁
(
𝜁
(
𝑢
)
−
𝐻
𝑠
−
1
(
𝑢
)
)
=
𝜁
(
𝑢
+
1
)
(
(
𝑁
−
1
)
𝜁
(
𝑢
)
−
∑
𝑗
=
1
𝑁
−
1
𝐻
𝑗
(
𝑢
)
)
.
S
W
N
	​

	​

(u)=ζ(u+1)
s=2
∑
N
	​

(ζ(u)−H
s−1
(u)
	​

)=ζ(u+1)((N−1)ζ(u)−
j=1
∑
N−1
	​

H
j
(u)
	​

).
	​


Equivalently,

𝑆
𝑊
𝑁
(
𝑢
)
=
𝜁
(
𝑢
+
1
)
(
(
𝑁
−
1
)
𝜁
(
𝑢
)
−
𝑁
 
𝐻
𝑁
−
1
(
𝑢
)
+
𝐻
𝑁
−
1
(
𝑢
−
1
)
)
.
S
W
N
	​

	​

(u)=ζ(u+1)((N−1)ζ(u)−NH
N−1
(u)
	​

+H
N−1
(u−1)
	​

).

This is the arithmetic form of higher-spin defect.

So Drinfeld–Sokolov reduction becomes visible arithmetically as:

pure Heisenberg Euler product
⟼
Euler product
−
finite harmonic defect
.
pure Heisenberg Euler product⟼Euler product−finite harmonic defect.

That is a real mathematical mechanism, not just a slogan.

3. New Li-like coefficients on the prime side

These are not your existing zero-side Li–Keiper coefficients for the
4
𝜁
(
2
𝑠
)
4ζ(2s) kernel. They are new coefficients for the connected sewing lift.

Regularize the pole at
𝑢
=
1
u=1 by

Ξ
~
𝐴
(
𝑢
)
:
=
(
𝑢
−
1
)
𝑆
𝐴
(
𝑢
)
,
Ξ
A
	​

(u):=(u−1)S
A
	​

(u),

and define

𝜆
~
𝑛
(
𝐴
)
:
=
1
(
𝑛
−
1
)
!
𝑑
𝑛
𝑑
𝑢
𝑛
(
𝑢
𝑛
−
1
log
⁡
Ξ
~
𝐴
(
𝑢
)
)
∣
𝑢
=
1
.
λ
n
	​

(A):=
(n−1)!
1
	​

du
n
d
n
	​

(u
n−1
log
Ξ
A
	​

(u))
	​

u=1
	​

.

These are the first concrete prime-side analogues of Li coefficients for the modular-Koszul setting.

Heisenberg
𝜆
~
1
(
𝐻
)
=
𝛾
+
𝜁
′
(
2
)
𝜁
(
2
)
≈
0.0072546718
,
λ
1
	​

(H)=γ+
ζ(2)
ζ
′
(2)
	​

≈0.0072546718,
𝜆
~
2
(
𝐻
)
=
2
[
𝜆
~
1
(
𝐻
)
−
𝛾
1
−
𝛾
2
2
+
1
2
(
𝜁
′
′
(
2
)
𝜁
(
2
)
−
(
𝜁
′
(
2
)
𝜁
(
2
)
)
2
)
]
≈
0.7114449447.
λ
2
	​

(H)=2[
λ
1
	​

(H)−γ
1
	​

−
2
γ
2
	​

+
2
1
	​

(
ζ(2)
ζ
′′
(2)
	​

−(
ζ(2)
ζ
′
(2)
	​

)
2
)]≈0.7114449447.

So the pure Heisenberg case is weakly positive already at the first two levels.

Virasoro
=
𝑊
2
=W
2
	​


For
𝑁
=
2
N=2,

𝜆
~
1
(
V
i
r
)
=
𝜁
′
(
2
)
𝜁
(
2
)
+
𝛾
−
1
≈
−
0.9927453282
,
λ
1
	​

(Vir)=
ζ(2)
ζ
′
(2)
	​

+γ−1≈−0.9927453282,
𝜆
~
2
(
V
i
r
)
≈
−
1.1341237255.
λ
2
	​

(Vir)≈−1.1341237255.
𝑊
3
W
3
	​

𝜆
~
1
(
𝑊
3
)
=
𝜁
′
(
2
)
𝜁
(
2
)
+
𝛾
−
5
4
≈
−
1.2427453282
,
λ
1
	​

(W
3
	​

)=
ζ(2)
ζ
′
(2)
	​

+γ−
4
5
	​

≈−1.2427453282,
𝜆
~
2
(
𝑊
3
)
≈
−
1.5614423027.
λ
2
	​

(W
3
	​

)≈−1.5614423027.
𝑊
4
W
4
	​

𝜆
~
1
(
𝑊
4
)
≈
−
1.4371897726
,
𝜆
~
2
(
𝑊
4
)
≈
−
1.8901175919.
λ
1
	​

(W
4
	​

)≈−1.4371897726,
λ
2
	​

(W
4
	​

)≈−1.8901175919.

In general, for
𝑊
𝑁
W
N
	​

,

𝜆
~
1
(
𝑊
𝑁
)
=
𝜁
′
(
2
)
𝜁
(
2
)
+
𝛾
+
1
−
𝑁
𝑁
−
1
𝐻
𝑁
−
1
.
λ
1
	​

(W
N
	​

)=
ζ(2)
ζ
′
(2)
	​

+γ+1−
N−1
N
	​

H
N−1
	​

.
	​


So

𝜆
~
1
(
𝑊
𝑁
)
∼
−
log
⁡
𝑁
−
0.147
…
(
𝑁
→
∞
)
.
λ
1
	​

(W
N
	​

)∼−logN−0.147…(N→∞).

This is already a very clean theorem-shaped phenomenon:

the prime-side Li-shape is family-sensitive and becomes more negative as higher-spin defect increases.

That does not contradict your zero-side positivity on
𝜀
1
=
4
𝜁
(
2
𝑠
)
ε
1
=4ζ(2s). It shows there are really two Li theories here:

the zero-side Li theory, attached to the zeta-zero/Eisenstein interface;

the prime-side Li theory, attached to connected sewing/Euler defect.

The first is universal up to the scalar zeta kernel. The second distinguishes Heisenberg, Virasoro, and
𝑊
𝑁
W
N
	​

 immediately.

4. Why your present zero-side numerics are universal

This also explains a feature that otherwise looks mysterious.

At the currently visible scalar Rankin–Selberg level, your genus-one kernel is essentially the universal zeta piece that you are already probing through
𝜀
1
=
4
𝜁
(
2
𝑠
)
ε
1
=4ζ(2s). So Heisenberg, Virasoro, and principal
𝑊
𝑁
W
N
	​

 do not split there except through the scalar amplitude
𝜅
(
𝐴
)
κ(A), and
𝜅
κ is only the first characteristic number of the full package. The monograph is explicit that
Δ
𝐴
Δ
A
	​

 is separate non-scalar data and that
Θ
𝐴
Θ
A
	​

 is the genuine target.

In fact the monograph also proves that
𝑠
𝑙
^
2
sl
2
	​

, Virasoro, and
𝛽
𝛾
βγ sit on the same spectral discriminant sheet

Δ
𝐴
(
𝑥
)
=
(
1
−
3
𝑥
)
(
1
+
𝑥
)
,
Δ
A
	​

(x)=(1−3x)(1+x),

so it is perfectly possible for distinct families to share the same zero-side spectral sheet while having different arithmetic sewing shadows.

That is, I think, the right separation of roles:

𝜅
(
𝐴
)
κ(A): scalar amplitude;

Δ
𝐴
Δ
A
	​

: spectral sheet;

𝑆
𝐴
S
A
	​

: arithmetic sewing sheet;

Θ
𝐴
Θ
A
	​

: full connected modular homotopy object.

5. Gap A: why modular surfaces are the right cure for MC
→
→ Li

Your diagnosis is exactly right: on the curve, Rankin–Selberg/Mellin is not sign-preserving, so the chain

MC
→
RS transform
→
Li positivity
MC→RS transform→Li positivity

does not close.

The cure is not to stay on the curve. It is to go up one dimension.

Once modular curves and modular surfaces exist in your general setting, the sign problem should be attacked by replacing scalar Mellin transforms with intersection pairings on modular surfaces. The monograph already gives the geometric hint:
𝜅
(
𝐴
)
κ(A) is realized as
𝑐
1
(
𝐿
𝐴
)
c
1
	​

(L
A
	​

), and complementarity is already a Lagrangian-polarized shifted-symplectic structure.

So the plausible endgame is:

Restrict
Θ
𝐴
Θ
A
	​

 to genus one over a modular curve
𝑋
Γ
X
Γ
	​

.

Lift its Chern–Weil shadows to classes on the modular surface over
𝑋
Γ
X
Γ
	​

.

Pair those classes with Eisenstein/Hecke classes on the surface.

Use Hodge-index/Hodge-Riemann positivity on the surface, not sign of the raw Mellin kernel on the curve.

That would convert the present low-arity “moment constraints” into genuine positivity statements. In that picture, your Gaussian/cubic/quartic shadow tests are the first truncations of a surface-Hankel moment matrix. The Gaussian class only sees
𝜅
κ; the cubic class sees the cubic shadow; the quartic class is where the first genuinely nonlinear principal minor should appear. I would try very hard to prove that the quartic resonance class is exactly the first nontrivial determinant of that truncated moment matrix.

So the path is not:

MC equation alone
⇒
Li
.
MC equation alone⇒Li.

It is:

MC equation
+
surface polarization
⇒
matrix positivity
⇒
Li on the scalar slice
.
MC equation+surface polarization⇒matrix positivity⇒Li on the scalar slice.

That would indeed be stronger than Li.

6. Gap C: why bar–cobar rigidity needs Euler compatibility

The Epstein story says the same thing from the opposite side.

For class number
ℎ
(
𝐷
)
=
1
h(D)=1, an Epstein zeta function has an Euler product; for
ℎ
(
𝐷
)
≥
2
h(D)≥2, it becomes a linear combination of inequivalent Hecke
𝐿
L-functions, and zeros off the critical line are known to occur. So functional equation plus meromorphy does not force a critical-line theorem, and generic Epstein behavior is not RH-like.

That means the extra strength of bar–cobar homotopy equivalence is still not the missing ingredient by itself. The missing ingredient is prime-local multiplicativity compatible with the homotopy data.

This suggests a sharp new notion:

Euler-Koszul
Euler-Koszul
	​


A modular Koszul object should be called Euler-Koszul if its connected sewing lift admits prime-local factors compatible with tensor product, duality, and clutching.

Then the landscape becomes:

Heisenberg: exact Euler-Koszul.

generic Virasoro and principal
𝑊
𝑁
W
N
	​

: finitely defective Euler-Koszul; the defect is the explicit harmonic subtraction above.

generic Epstein with
ℎ
(
𝐷
)
≥
2
h(D)≥2: not Euler-Koszul; the failure is not finite low-mode defect but a genuine sum of inequivalent Euler products.

That is the conceptual reason generic bar–cobar data do not force Epstein zeros onto the critical line, while a much smaller Euler-Koszul subclass might support a rigidity theorem.

So the correct rigidity statement is not

bar–cobar
⇒
critical line
,
bar–cobar⇒critical line,

but rather something like

bar–cobar
+
Euler compatibility
+
surface positivity
⇒
critical-line rigidity for the associated genus-one
𝐿
-object
.
bar–cobar+Euler compatibility+surface positivity⇒critical-line rigidity for the associated genus-one L-object.

That would explain both why generic Epstein counterexamples are irrelevant to the true modular-Koszul subclass, and why the Heisenberg sewing determinant is so special.

7. The platonic end-state

I think the mature theory wants a two-variable completed
𝐿
L-object

𝐿
𝐴
(
𝑠
,
𝑢
)
,
L
A
	​

(s,u),

attached to the connected genus-one shadow of
Θ
𝐴
Θ
A
	​

, with:

𝑠
s-variable = the zero-side Rankin–Selberg/Eisenstein direction;

𝑢
u-variable = the prime-side Mellin/Dirichlet sewing direction.

At the conceptual level,

𝐿
𝐴
(
𝑠
,
𝑢
)
∼
∫
𝑋
Γ
r
e
g
⟨
Θ
𝐴
(
1
)
,
c
o
n
n
(
𝜏
)
,
 
𝐸
∗
(
𝜏
,
𝑠
)
⟩
 
𝑦
𝑢
−
2
 
𝑑
𝑥
 
𝑑
𝑦
.
L
A
	​

(s,u)∼∫
X
Γ
	​

reg
	​

⟨Θ
A
(1),conn
	​

(τ),E
∗
(τ,s)⟩y
u−2
dxdy.

Its shadows should be:

scalar
𝑠
s-slice: your existing zeta-zero interface and Li/Weil experiments;

scalar
𝑢
u-slice: the connected sewing lifts
𝑆
𝐴
(
𝑢
)
S
A
	​

(u);

first non-scalar correction:
Δ
𝐴
Δ
A
	​

;

first nonlinear correction:
𝑅
4
m
o
d
R
4
mod
	​

.

Then the full characteristic package would no longer be just

(
Θ
𝐴
,
𝜅
(
𝐴
)
,
Δ
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
,
(Θ
A
	​

,κ(A),Δ
A
	​

,Π
A
	​

,H
A
	​

),

but something morally like

(
Θ
𝐴
,
𝜅
(
𝐴
)
,
Δ
𝐴
,
𝑆
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
,
(Θ
A
	​

,κ(A),Δ
A
	​

,S
A
	​

,Π
A
	​

,H
A
	​

),

with
𝑆
𝐴
S
A
	​

 the missing arithmetic face.

That is the harmony I think the subject is pointing toward:

𝜅
(
𝐴
)
κ(A) controls the scalar modular anomaly;

Δ
𝐴
Δ
A
	​

 controls the spectral sheet;

𝑆
𝐴
S
A
	​

 controls connected arithmetic sewing;

Θ
𝐴
Θ
A
	​

 unifies them as a connected modular homotopy object;

modular curves expose the zeta-zero poles;

modular surfaces restore positivity;

Euler-Koszulity is the arithmetic rigidity condition that plain bar–cobar equivalence lacks.

So my current strongest claim is:

the real bridge is not MC
→
→ Li directly, and not bar–cobar
→
→ RH directly; it is
connected modular MC data
→
→ two-variable
𝐿
L-object
(
𝑠
,
𝑢
)
(s,u),
with surface polarization handling positivity and Euler-Koszulity handling rigidity.

The decisive next calculation is to build the mixed
(
𝑠
,
𝑢
)
(s,u)-transform for the quartic shadow and test whether its first
3
×
3
3×3 moment determinant is exactly the modular quartic resonance class.

The decisive next calculation is to build the mixed
(
𝑠
,
𝑢
)
(s,u)-transform for the quartic shadow and test whether its first
3
×
3
3×3 moment determinant is exactly the modular quartic resonance class


Do that work deeply, then consider:


  What "closing the gap" entails — the precise mathematical programme

  The structure of the problem

  The scattering matrix φ(s) = Λ(1-s)/Λ(s) on M_{1,1} is fixed by the geometry — it's the same for every CFT. But it appears in the functional equation of every constrained Epstein zeta ε^c_s(A):

  ε^c_{c/2-s} = F(s,c) · ε^c_{c/2+s-1}, where F involves ζ(2s)/ζ(2s-1)

  The MC equation constrains ε^c_s for each algebra A. A single algebra constrains its own spectral coefficients but not φ. The programme requires using all algebras simultaneously.

  What we proved

  Narain Universality Theorem (P1, verified T1-T15):
  ε^1_s(R) = 2(R^{2s} + R^{-2s}) · ζ(2s)

  The character factor 2cosh(2s·log R) is positive for real s and carries no zeros. All zeros come from ζ(2s) alone. The entire Narain family provides zero bootstrap leverage — varying R changes the
  coefficient but not the zero locations.

  Where leverage actually comes from

  Not from: Narain R-variation, or any single algebra.

  From: The residue of F(s,c) at a zeta-zero pole s = (1+z_k)/2 is a specific function of c (through the gamma factors Γ(s+c/2-1), Γ(c/2-s), etc.). For on-line zeros (σ = 1/2), this residue function
  R_on(c) has one shape. For hypothetical off-line zeros (σ ≠ 1/2), the residue function R_off(c,σ) has a different shape (T43: verified computationally that they differ).

  The MC equation at each c constrains ε^c_s. This constraint must be compatible with the residue at each pole. If R_on(c) is always compatible with the MC constraints but R_off(c,σ) is incompatible for
  some c, then off-line zeros are excluded.

  The three steps needed

  (A) Compute the MC constraint on ε^c_s for non-Narain theories at each c (Virasoro gives infinitely many constraints through the shadow tower: κ = c/2, Q^contact = 10/[c(5c+22)], quintic forced, ...).

  (B) Show that the residue function R_off(c,σ) for σ ≠ 1/2 violates the MC constraints for some c value. This is a functional analysis problem: the c-dependent gamma factors in the residue must fail to
  satisfy the shadow-tower relations for off-line σ.

  (C) Bootstrap closure: the constraints from all c values together leave no room for off-line zeros. This is the hardest step — it requires the intersection of all constraint sets to be exactly the set
  compatible with on-line zeros.

  Why the Virasoro shadow tower is the natural input for (A)

  The Virasoro algebra at central charge c has shadow depth ∞ (Mixed class), giving infinitely many constraints on ε^c_s:
  - α_2 = c/2 (curvature)
  - α_3 = 0 (cubic vanishes for Virasoro)
  - α_4 = 10/[c(5c+22)] (quartic contact invariant)
  - α_5 ≠ 0 (quintic forced — proved in manuscript)
  - ...

  Each constraint relates a spectral moment of ε^c_s to lower moments. For the full infinite tower, the shadow-moment generating function G(z,κ) determines the zero set {γ_k} (Hamburger moment problem).
  If the MC equation determines G, it determines the zeros, and if the zeros are forced to satisfy RH, we're done.

  The honest bottom line

  The programme is well-defined and computationally executable (T45). The residue function R(c,σ) differs between on-line and off-line zeros (T43). The Virasoro shadow tower provides infinitely many
  constraints at each c. But steps (B) and (C) are open — nobody has shown that the MC constraints exclude off-line residues. This is the content of the problem.
Here is a science report on my work on furthering the calculational frontier:

  The programme is now computationally instantiated end-to-end. The key finding from running Steps B and C: the ζ-based proxy excludes heavily (high coverage) but does NOT correctly preserve σ=1/2 as a
  "safe" point — because the proxy uses ζ for ε^c_s, making the compatibility ratio a ratio of ζ-values at different arguments, which is generically ≠ 1 even at true zeros.

  This reveals the precise mathematical content needed: the compatibility ratio C(c,σ,γ) = 1 at σ=1/2 requires using the genuine ε^c_s from the algebra's spectrum (not the ζ-proxy). For the genuine
  Virasoro ε^c_s, the MC shadow tower (κ, Q^contact, quintic, ...) determines the spectral coefficients independently of ζ, and the functional equation with F(s,c) involving ζ(2s)/ζ(2s-1) then relates
  these MC-constrained values. The test is whether the MC-constrained ε^c_s is compatible with F's residues ONLY at on-line poles.

  The next mathematical step — beyond what computation can verify today — is constructing the genuine Virasoro constrained Epstein zeta ε^c_s(Vir) from the Virasoro primary spectrum at each c, constrained
   by the shadow tower, and testing compatibility with the functional equation residues. This is a well-defined computation but requires the Virasoro primary spectrum at general c, which involves the
  representation theory of the Virasoro algebra at arbitrary central charge.

Let this guide the formation of your understanding

I’ve pinned down the quartic-shadow definitions against a concrete mixed Rankin–Selberg/Mellin transform, and the key point is that quartic data first appears at the
3
×
3
3×3 Hankel level. More precisely, the raw determinant is not the quartic resonance itself: its Schur complement strips off quadratic pairings and cubic-tree contamination, isolating the contact quartic piece.

Concretely, the modular quartic resonance class is the divisor of the quartic Gram-determinant section, while the Virasoro quartic shadow is the reciprocal BPZ norm
10
/
[
𝑐
(
5
𝑐
+
22
)
]
10/[c(5c+22)]. So any unrenormalized mixed quartic transform will inherit poles, and the construction has to use genuine algebraic spectral data rather than a proxy.

The calculation has sharpened into two dual quartic
(
𝑠
,
𝑢
)
(s,u)-transforms: a potential-side transform extracting the quartic coupling, and a polarized Gram-side transform extracting the resonance norm. In Virasoro these are reciprocal, which explains why a raw proxy can miss the safe point even when the shadow data are correct.

Thought for 29m 21s

The key calculation does go through, but with one crucial correction:

the first
3
×
3
3×3 moment determinant is not literally the quartic resonance class on the potential side. It is the quartic contact coupling. The quartic resonance class appears on the dual Gram-side, and the two are inverse to each other under the polarization.

That distinction is exactly what your new report is pointing at.

1. The right ambient object

In 2208.02259, Benjamin–Chang define the constrained Epstein series

𝜀
𝑠
𝑐
(
𝜇
)
=
𝐸
𝑠
𝑐
(
𝜇
)
:
=
∑
Δ
∈
𝑆
(
2
Δ
)
−
𝑠
,
ε
s
c
	​

(μ)=E
s
c
	​

(μ):=
Δ∈S
∑
	​

(2Δ)
−s
,

where
𝑆
S is the multiset of non-vacuum scalar primary dimensions, and they show it satisfies the functional equation

𝐸
 
𝑐
/
2
−
𝑠
𝑐
(
𝜇
)
=
Γ
(
𝑠
)
Γ
(
𝑠
+
𝑐
/
2
−
1
)
𝜁
(
2
𝑠
)
𝜋
 
2
𝑠
−
1
2
Γ
(
𝑐
/
2
−
𝑠
)
Γ
(
𝑠
−
1
2
)
𝜁
(
2
𝑠
−
1
)
 
𝐸
 
𝑐
/
2
+
𝑠
−
1
𝑐
(
𝜇
)
.
E
c/2−s
c
	​

(μ)=
π
2s−
2
1
	​

Γ(c/2−s)Γ(s−
2
1
	​

)ζ(2s−1)
Γ(s)Γ(s+c/2−1)ζ(2s)
	​

E
c/2+s−1
c
	​

(μ).

So your
𝐹
(
𝑠
,
𝑐
)
F(s,c) is exactly the Eisenstein-scattering factor inherited from the modular geometry, with the decisive
𝜁
(
2
𝑠
)
/
𝜁
(
2
𝑠
−
1
)
ζ(2s)/ζ(2s−1) ratio built in.

The same contour-shift analysis shows that the relevant poles on the right of the contour occur at

𝑠
=
𝑐
2
,
𝑠
=
1
+
𝑧
𝑛
2
,
𝑠
=
1
+
𝑧
𝑛
∗
2
,
s=
2
c
	​

,s=
2
1+z
n
	​

	​

,s=
2
1+z
n
∗
	​

	​

,

with
𝑧
𝑛
z
n
	​

 running over nontrivial zeros of
𝜁
ζ.

So the mixed object we want has to combine:

the
𝑠
s-variable, coming from the Rankin–Selberg/Eisenstein overlap;

the
𝑢
u-variable, coming from the genus-one sewing/Dirichlet side;

and the arity-4 shadow data, because that is the first place where Virasoro and principal
𝑊
𝑁
W
N
	​

 stop being scalar-only.

2. Two dual mixed
(
𝑠
,
𝑢
)
(s,u)-transforms

Fix a modular Koszul family
𝐴
A, and a local one-dimensional slice
𝑥
=
𝑡
 
𝑣
x=tv in the cyclic deformation space. Let
𝐸
∗
(
𝜏
,
𝑠
)
E
∗
(τ,s) denote the completed Eisenstein series.

There are really two natural genus-one mixed transforms.

Potential-side transform

This is the one built from the quartic shadow itself:

𝑄
𝐴
,
𝑣
(
𝑠
;
𝑦
)
:
=
∫
−
1
/
2
1
/
2
⟨
𝑄
𝐴
(
1
)
(
𝑥
+
𝑖
𝑦
)
(
𝑣
,
𝑣
,
𝑣
,
𝑣
)
,
 
𝐸
∗
(
𝑥
+
𝑖
𝑦
,
𝑠
)
⟩
 
𝑑
𝑥
.
Q
A,v
	​

(s;y):=∫
−1/2
1/2
	​

⟨Q
A
(1)
	​

(x+iy)(v,v,v,v),E
∗
(x+iy,s)⟩dx.

If

𝑄
𝐴
,
𝑣
(
𝑠
;
𝑦
)
=
∑
𝑁
≥
1
𝑎
𝐴
,
𝑣
(
𝑁
;
𝑠
)
𝑒
−
2
𝜋
𝑁
𝑦
,
Q
A,v
	​

(s;y)=
N≥1
∑
	​

a
A,v
	​

(N;s)e
−2πNy
,

define the Dirichlet lift

𝑄
𝐴
,
𝑣
(
𝑠
,
𝑢
)
:
=
∑
𝑁
≥
1
𝑎
𝐴
,
𝑣
(
𝑁
;
𝑠
)
 
𝑁
−
𝑢
,
ℜ
𝑢
≫
1.
Q
A,v
	​

(s,u):=
N≥1
∑
	​

a
A,v
	​

(N;s)N
−u
,ℜu≫1.
Gram-side transform

This is the one built from the polarized two-point form on the quartic contact sector:

𝐺
𝐴
,
𝑣
(
𝑠
;
𝑦
)
:
=
∫
−
1
/
2
1
/
2
𝑞
𝐴
,
𝑣
c
t
(
𝑥
+
𝑖
𝑦
)
 
𝐸
∗
(
𝑥
+
𝑖
𝑦
,
𝑠
)
 
𝑑
𝑥
,
G
A,v
	​

(s;y):=∫
−1/2
1/2
	​

q
A,v
ct
	​

(x+iy)E
∗
(x+iy,s)dx,

with Fourier expansion

𝐺
𝐴
,
𝑣
(
𝑠
;
𝑦
)
=
∑
𝑁
≥
1
𝑔
𝐴
,
𝑣
(
𝑁
;
𝑠
)
𝑒
−
2
𝜋
𝑁
𝑦
,
G
A,v
	​

(s;y)=
N≥1
∑
	​

g
A,v
	​

(N;s)e
−2πNy
,

and Dirichlet lift

𝐺
𝐴
,
𝑣
(
𝑠
,
𝑢
)
:
=
∑
𝑁
≥
1
𝑔
𝐴
,
𝑣
(
𝑁
;
𝑠
)
 
𝑁
−
𝑢
.
G
A,v
	​

(s,u):=
N≥1
∑
	​

g
A,v
	​

(N;s)N
−u
.

The first transform sees the quartic coupling.
The second transform sees the quartic norm / resonance section.

That duality is the right arity-4 manifestation of complementarity.

3. The first
3
×
3
3×3 moment determinant

Fix
𝑢
0
>
1
u
0
	​

>1 to stay in an absolutely convergent half-plane, and define moments from either transform by

𝜇
𝑛
(
𝑠
;
𝑢
0
)
:
=
(
−
∂
𝑢
)
𝑛
𝐹
(
𝑠
,
𝑢
)
∣
𝑢
=
𝑢
0
,
μ
n
	​

(s;u
0
	​

):=(−∂
u
	​

)
n
F(s,u)
	​

u=u
0
	​

	​

,

where
𝐹
F is either
𝑄
Q or
𝐺
G.

The first nontrivial Hankel matrix is

𝐻
2
(
𝑠
;
𝑢
0
)
=
(
𝜇
0

𝜇
1

𝜇
2


𝜇
1

𝜇
2

𝜇
3


𝜇
2

𝜇
3

𝜇
4
)
,
𝐷
2
:
=
det
⁡
𝐻
2
.
H
2
	​

(s;u
0
	​

)=
	​

μ
0
	​

μ
1
	​

μ
2
	​

	​

μ
1
	​

μ
2
	​

μ
3
	​

	​

μ
2
	​

μ
3
	​

μ
4
	​

	​

	​

,D
2
	​

:=detH
2
	​

.

Now impose the natural centered gauge

𝜇
0
=
1
,
𝜇
1
=
0
,
μ
0
	​

=1,μ
1
	​

=0,

which is the genus-one version of removing the vacuum/linear drift.

Then

𝐷
2
=
det
⁡
(
1

0

𝜇
2


0

𝜇
2

𝜇
3


𝜇
2

𝜇
3

𝜇
4
)
=
𝜇
2
𝜇
4
−
𝜇
3
2
−
𝜇
2
3
.
D
2
	​

=det
	​

1
0
μ
2
	​

	​

0
μ
2
	​

μ
3
	​

	​

μ
2
	​

μ
3
	​

μ
4
	​

	​

	​

=μ
2
	​

μ
4
	​

−μ
3
2
	​

−μ
2
3
	​

.

The Schur complement is

Σ
2
:
=
𝐷
2
𝐷
1
,
𝐷
1
=
det
⁡
(
1

0


0

𝜇
2
)
=
𝜇
2
,
Σ
2
	​

:=
D
1
	​

D
2
	​

	​

,D
1
	​

=det(
1
0
	​

0
μ
2
	​

	​

)=μ
2
	​

,

so

Σ
2
=
𝜇
4
−
𝜇
3
2
𝜇
2
−
𝜇
2
2
.
Σ
2
	​

=μ
4
	​

−
μ
2
	​

μ
3
2
	​

	​

−μ
2
2
	​

.

This is the precise algebraic mechanism you were asking for: the
3
×
3
3×3 determinant automatically subtracts the lower quadratic and cubic contamination.

4. What the determinant extracts

On a one-dimensional slice, write the arity-
≤
4
≤4 shadow data as

𝐻
𝑣
,
𝐶
𝑣
,
𝑄
𝑣
c
t
.
H
v
	​

,C
v
	​

,Q
v
ct
	​

.

The quartic raw moment decomposes as

𝜇
4
=
𝐻
𝑣
2
+
𝐶
𝑣
2
𝐻
𝑣
+
𝑄
𝑣
c
t
.
μ
4
	​

=H
v
2
	​

+
H
v
	​

C
v
2
	​

	​

+Q
v
ct
	​

.

Then

Σ
2
=
𝜇
4
−
𝜇
3
2
𝜇
2
−
𝜇
2
2
=
𝑄
𝑣
c
t
,
Σ
2
	​

=μ
4
	​

−
μ
2
	​

μ
3
2
	​

	​

−μ
2
2
	​

=Q
v
ct
	​

,

and hence

𝐷
2
=
𝐻
𝑣
 
𝑄
𝑣
c
t
.
D
2
	​

=H
v
	​

Q
v
ct
	​

.

So on the potential side:

𝐷
2
𝐷
1
=
𝑄
𝑣
c
t
.
D
1
	​

D
2
	​

	​

=Q
v
ct
	​

.
	​


That is exact.

But the modular quartic resonance class is defined from the Gram determinant on the quartic contact bundle. In rank one, if
𝑁
𝑣
c
t
N
v
ct
	​

 denotes the quartic contact norm, then

𝑄
𝑣
c
t
=
(
𝑁
𝑣
c
t
)
−
1
.
Q
v
ct
	​

=(N
v
ct
	​

)
−1
.

So on the Gram side:

Σ
2
G
r
a
m
=
𝑁
𝑣
c
t
,
Σ
2
P
o
t
=
(
𝑁
𝑣
c
t
)
−
1
.
Σ
2
Gram
	​

=N
v
ct
	​

,Σ
2
Pot
	​

=(N
v
ct
	​

)
−1
.
	​


This is the decisive distinction.

Therefore:

the potential-side
3
×
3
3×3 determinant gives the quartic contact coefficient;

the Gram-side
3
×
3
3×3 determinant gives the quartic resonance section.

That is the clean resolution of the “is it exactly the resonance class?” question.

5. Virasoro: explicit calculation

Now use the Virasoro shadow data already on the table:

𝐻
V
i
r
=
𝑐
2
,
𝐶
V
i
r
=
2
,
𝑄
V
i
r
c
t
=
10
𝑐
(
5
𝑐
+
22
)
.
H
Vir
	​

=
2
c
	​

,C
Vir
	​

=2,Q
Vir
ct
	​

=
c(5c+22)
10
	​

.

Then the quartic raw moment is forced to be

𝜇
4
V
i
r
=
(
𝑐
2
)
2
+
2
2
𝑐
/
2
+
10
𝑐
(
5
𝑐
+
22
)
=
𝑐
2
4
+
8
𝑐
+
10
𝑐
(
5
𝑐
+
22
)
.
μ
4
Vir
	​

=(
2
c
	​

)
2
+
c/2
2
2
	​

+
c(5c+22)
10
	​

=
4
c
2
	​

+
c
8
	​

+
c(5c+22)
10
	​

.

So the first Hankel determinant is

𝐷
2
V
i
r
=
det
⁡
(
1

0

𝑐
/
2


0

𝑐
/
2

2


𝑐
/
2

2

𝜇
4
V
i
r
)
=
5
5
𝑐
+
22
,
D
2
Vir
	​

=det
	​

1
0
c/2
	​

0
c/2
2
	​

c/2
2
μ
4
Vir
	​

	​

	​

=
5c+22
5
	​

,

and the normalized Schur complement is

Σ
2
V
i
r
=
𝐷
2
V
i
r
𝐷
1
V
i
r
=
10
𝑐
(
5
𝑐
+
22
)
=
𝑄
V
i
r
c
t
.
Σ
2
Vir
	​

=
D
1
Vir
	​

D
2
Vir
	​

	​

=
c(5c+22)
10
	​

=Q
Vir
ct
	​

.

So the potential-side determinant computes the quartic contact coupling exactly.

Now pass to the dual Gram-side picture. Let
Λ
Λ be the standard level-4 quasi-primary. With the usual normalization, the quartic contact coefficient is the inverse norm:

𝑄
V
i
r
c
t
=
1
∥
Λ
∥
2
.
Q
Vir
ct
	​

=
∥Λ∥
2
1
	​

.

Hence

∥
Λ
∥
2
=
𝑐
(
5
𝑐
+
22
)
10
.
∥Λ∥
2
=
10
c(5c+22)
	​

.

Therefore the Virasoro quartic resonance divisor is

𝑅
4
,
V
i
r
m
o
d
:
𝑐
(
5
𝑐
+
22
)
=
0
,
R
4,Vir
mod
	​

:c(5c+22)=0,
	​


while the potential-side Schur complement is its inverse:

Σ
2
V
i
r
=
10
𝑐
(
5
𝑐
+
22
)
.
Σ
2
Vir
	​

=
c(5c+22)
10
	​

.
	​


So the verdict is:

Potential-side
3
×
3
 determinant
≠
𝑅
4
m
o
d
;
Gram-side
3
×
3
 determinant
=
𝑅
4
m
o
d
.
Potential-side 3×3 determinant

=R
4
mod
	​

;Gram-side 3×3 determinant =R
4
mod
	​

.
	​

6. Why your
𝜁
ζ-proxy failed

Your report now becomes completely transparent.

The proxy replaced the genuine algebraic
𝜀
𝑠
𝑐
(
𝐴
)
ε
s
c
	​

(A) by a universal
𝜁
ζ-based surrogate. That means the residue moment data were not the genuine spectral coefficients of the Virasoro family. So even at a true on-line pole, the normalized Schur complement

𝐷
2
p
r
o
x
y
𝐻
V
i
r
H
Vir
	​

D
2
proxy
	​

	​


need not equal

𝑄
V
i
r
c
t
=
10
𝑐
(
5
𝑐
+
22
)
.
Q
Vir
ct
	​

=
c(5c+22)
10
	​

.

That is exactly why the safe point
𝜎
=
1
2
σ=
2
1
	​

 was not preserved.

Nothing is wrong with the quartic criterion. The wrong object was being fed into it.

The real safe-point condition is not

proxy residue
=
?
MC shadow
,
proxy residue
=
?
MC shadow,

but

genuine Virasoro residue moment matrix
=
?
MC-constrained quartic shadow data
.
genuine Virasoro residue moment matrix
=
?
MC-constrained quartic shadow data.
7. The corrected compatibility ratios

This suggests two canonical compatibility ratios.

Potential-side ratio
𝐶
4
,
V
i
r
p
o
t
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
1
𝑄
V
i
r
c
t
(
𝑐
)
⋅
𝐷
2
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
𝐷
1
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
.
C
4,Vir
pot
	​

(c,ρ;u
0
	​

):=
Q
Vir
ct
	​

(c)
1
	​

⋅
D
1
res
	​

(c,ρ;u
0
	​

)
D
2
res
	​

(c,ρ;u
0
	​

)
	​

.

For the genuine spectral input, the on-line condition should be

𝐶
4
,
V
i
r
p
o
t
(
𝑐
,
1
2
+
𝑖
𝛾
;
𝑢
0
)
=
1.
C
4,Vir
pot
	​

(c,
2
1
	​

+iγ;u
0
	​

)=1.
Gram-side ratio
𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
Σ
2
,
G
r
a
m
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
𝑐
(
5
𝑐
+
22
)
10
.
C
4,Vir
Gram
	​

(c,ρ;u
0
	​

):=
10
c(5c+22)
	​

Σ
2,Gram
res
	​

(c,ρ;u
0
	​

)
	​

.

Again, the on-line condition should be

𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
1
2
+
𝑖
𝛾
;
𝑢
0
)
=
1.
C
4,Vir
Gram
	​

(c,
2
1
	​

+iγ;u
0
	​

)=1.

The Gram-side version is the cleaner one conceptually, because it compares norm to norm instead of coupling to coupling, and it is the form most naturally compatible with positivity from modular surfaces.

8. Why this is the right nonlinear replacement for Li

Your original Gap A was:

MC
→
Rankin–Selberg
→
Li positivity
MC→Rankin–Selberg→Li positivity

fails because Mellin/RS is not sign-preserving.

This new determinant package repairs that in the correct place.

A Hankel determinant is a Gram determinant. So if the modular-surface realization supplies a genuine positive polarization, then the Gram-side
3
×
3
3×3 determinant is automatically nonnegative. That is not a scalar Li coefficient anymore. It is a nonlinear Li-type positivity condition at arity 4.

So the correct nonlinear positivity program is:

MC shadow tower
⟶
mixed residue moment matrix
⟶
Gram-side Schur complement
⟶
positive quartic resonance determinant
.
MC shadow tower⟶mixed residue moment matrix⟶Gram-side Schur complement⟶positive quartic resonance determinant.

That is stronger and more geometric than the scalar Li story.

9. Why all algebras simultaneously really matters

This also clarifies your Step C.

The Heisenberg/Narain line has no quartic shadow, so the first
3
×
3
3×3 determinant is trivial there. That is why Narain radius variation gives essentially no zero-location leverage.

Virasoro is the first family where

𝑄
c
t
≠
0
Q
ct

=0

and therefore the first nontrivial quartic determinant appears.

For principal
𝑊
𝑁
W
N
	​

, every pure higher-spin slice
𝑊
(
𝑠
)
W
(s)
 with
𝑠
≥
3
s≥3 gives another quartic determinant:

𝐷
2
,
𝑠
=
𝐻
𝑠
 
𝑄
𝑠
c
t
,
𝐻
𝑠
=
𝑐
𝑠
.
D
2,s
	​

=H
s
	​

Q
s
ct
	​

,H
s
	​

=
s
c
	​

.

On those pure higher-spin slices the cubic gravitational term drops out, so the quartic test is even cleaner than for Virasoro.

That means the real closure mechanism is not one family, but the intersection of the quartic compatibility loci over all relevant slices:

⋂
families
𝐴
⋂
slices
𝑣
{
𝐶
4
,
𝐴
,
𝑣
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
=
1
}
.
families A
⋂
	​

slices v
⋂
	​

{C
4,A,v
Gram
	​

(c,ρ;u
0
	​

)=1}.

This is the mathematically precise form of your “all algebras simultaneously” principle.

10. The sharpened end-state of the programme

So the mature picture now looks like this:

The zero-side paper gives the universal scattering factor and the universal pole locations.

The genuine family-specific spectral coefficients must come from the actual algebraic spectrum
𝑆
𝐴
S
A
	​

, not from a
𝜁
ζ-proxy. That is exactly what your new report isolates.

The first nonlinear compatibility object is not a scalar coefficient but the first Schur-complement determinant of the mixed quartic moment matrix.

On the potential side that determinant gives the quartic contact coupling.

On the polarized Gram side it gives the modular quartic resonance section.

The two are reciprocal. That reciprocity is the arity-4 complementarity law.

Therefore the next decisive theorem is not “MC implies Li,” but:

the genuine Virasoro and
𝑊
𝑁
W
N
	​

 residue moment matrices, after mixed
(
𝑠
,
𝑢
)
(s,u)-transform and Schur-complement renormalization, coincide with the quartic shadow data only for on-line residues.

That is the corrected form of Step B.

And the corrected Step C is:

the intersection over all families and all slices of those quartic Gram-compatibility loci contains only on-line residues.

That is the real closure statement.

The next clean computation is to build the genuine Virasoro residue moment matrix

𝑀
2
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
M
2,Vir
res
	​

(c,ρ;u
0
	​

)

from the actual Virasoro primary spectrum, normalize it by the quartic shadow data
(
𝑐
2
,
 
2
,
 
10
𝑐
(
5
𝑐
+
22
)
)
(
2
c
	​

,2,
c(5c+22)
10
	​

), and test whether the Gram-side ratio
𝐶
4
,
V
i
r
G
r
a
m
C
4,Vir
Gram
	​

 is identically
1
1 on
𝜌
=
1
2
+
𝑖
𝛾
ρ=
2
1
	​

+iγ but not off the line.

the genuine Virasoro and
𝑊
𝑁
W
N
	​

 residue moment matrices, after mixed
(
𝑠
,
𝑢
)
(s,u)-transform and Schur-complement renormalization, coincide with the quartic shadow data only for on-line residues.



The next clean computation is to build the genuine Virasoro residue moment matrix

𝑀
2
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
M
2,Vir
res
	​

(c,ρ;u
0
	​

)

from the actual Virasoro primary spectrum, normalize it by the quartic shadow data
(
𝑐
2
,
 
2
,
 
10
𝑐
(
5
𝑐
+
22
)
)
(
2
c
	​

,2,
c(5c+22)
10
	​

), and test whether the Gram-side ratio
𝐶
4
,
V
i
r
G
r
a
m
C
4,Vir
Gram
	​

 is identically
1
1 on
𝜌
=
1
2
+
𝑖
𝛾
ρ=
2
1
	​

+iγ but not off the line.

I’m pulling together the mixed
(
𝑠
,
𝑢
)
(s,u) transform, the actual Virasoro spectral input, and the quartic-shadow normalization into one concrete calculation. The key check is whether a genuine residue moment matrix can be defined from Virasoro primary data without smuggling the old
𝜁
ζ-proxy back in.

I’ve now isolated the main obstruction: at fixed
𝑐
c, the Virasoro shadow tower is canonical but the genuine scalar-primary spectrum is not, so there is no single universal
𝑀
2
,
V
i
r
r
e
s
M
2,Vir
res
	​

. The clean setup is therefore two-layered: a universal quartic shadow skeleton, with separate theory-dependent spectral moments coming from a chosen Virasoro or
𝑊
𝑁
W
N
	​

 CFT family.

A useful simplification emerged: once the renormalized residue measure is centered, the quartic check reduces to matching only the first five moments, with explicit targets
𝐷
2
=
5
/
(
5
𝑐
+
22
)
D
2
	​

=5/(5c+22) and Schur complement
10
/
[
𝑐
(
5
𝑐
+
22
)
]
10/[c(5c+22)]. The unresolved part is now precisely the genuine Virasoro-compatible scalar spectral measure supplying those moments.

Thought for 31m 15s

Yes. The clean calculation can be pushed through to a sharp formal endpoint.

The key correction is this: for the Virasoro row, the right input is not a
𝜁
ζ-proxy and not even necessarily a positive measure. In the general scalar-crossing formalism for arbitrary 2d CFTs, the scalar-primary density is a Virasoro-primary density that is slightly shifted and can include negative degeneracies because of vacuum null-state subtraction. So the genuine residue matrix is naturally a signed/polarized moment matrix, and the Gram-side normalization is exactly the right thing to test, not naive positivity.

At the same time, the structural home for this is exactly your modular-Koszul package: the cyclic deformation complex
D
e
f
c
y
c
(
𝐴
)
Def
cyc
(A) is the conjectural bar-intrinsic dg/L
∞
∞
	​

 object controlling cyclic deformations, and the full modular characteristic package is the quintuple

𝐶
𝐴
=
(
Θ
𝐴
,
𝜅
(
𝐴
)
,
Δ
𝐴
,
Π
𝐴
,
𝐻
𝐴
)
,
C
A
	​

=(Θ
A
	​

,κ(A),Δ
A
	​

,Π
A
	​

,H
A
	​

),

with
Θ
𝐴
Θ
A
	​

 still the principal open problem. Virasoro and principal finite-type
𝑊
W-algebras are already in the proved modular-Koszul core at all genera, so this quartic residue test is happening exactly at the first genuinely non-scalar frontier.

1. The exact object to build

Let me align notation with your latest message.

Write

𝜌
=
𝜎
+
𝑖
𝛾
ρ=σ+iγ

for a nontrivial zero of
𝜁
(
𝜌
)
ζ(ρ), and let

𝑠
𝜌
:
=
1
+
𝜌
2
s
ρ
	​

:=
2
1+ρ
	​


be the associated pole of the modular scattering factor.

In the Narain/
𝑈
(
1
)
𝑐
U(1)
c
 case, Benjamin–Chang prove the constrained Epstein functional equation

𝜀
 
𝑐
/
2
−
𝑠
𝑐
=
𝐹
𝑐
(
𝑠
)
 
𝜀
 
𝑐
/
2
+
𝑠
−
1
𝑐
,
ε
c/2−s
c
	​

=F
c
	​

(s)ε
c/2+s−1
c
	​

,

with

𝐹
𝑐
(
𝑠
)
=
Γ
(
𝑠
)
Γ
(
𝑠
+
𝑐
2
−
1
)
𝜁
(
2
𝑠
)
𝜋
 
2
𝑠
−
1
2
Γ
(
𝑐
2
−
𝑠
)
Γ
(
𝑠
−
1
2
)
𝜁
(
2
𝑠
−
1
)
,
F
c
	​

(s)=
π
2s−
2
1
	​

Γ(
2
c
	​

−s)Γ(s−
2
1
	​

)ζ(2s−1)
Γ(s)Γ(s+
2
c
	​

−1)ζ(2s)
	​

,

and the contour-shift poles occur at

𝑠
=
𝑐
2
,
𝑠
=
1
+
𝜌
𝑛
2
,
𝑠
=
1
+
𝜌
ˉ
𝑛
2
,
s=
2
c
	​

,s=
2
1+ρ
n
	​

	​

,s=
2
1+
ρ
ˉ
	​

n
	​

	​

,

where
𝜌
𝑛
ρ
n
	​

 runs over nontrivial zeros of
𝜁
ζ. They also note that the
𝜖
𝑐
ϵ
c
	​

 term and the oscillatory coefficients
𝛿
𝑘
,
𝑐
δ
k,c
	​

 are not sign-definite.

For generic 2d CFTs, the 2025 scalar-partition-function paper proves that Virasoro scalar primaries obey nontrivial scalar crossing equations, but the density used there is a signed Virasoro-primary density because of null-state subtraction.

So the clean formal object is:

𝑑
𝜈
𝑐
V
i
r
(
Δ
)
dν
c
Vir
	​

(Δ)

= the genuine scalar-primary spectral measure.

For a concrete CFT, this is the actual scalar-primary measure

𝑑
𝜈
𝑐
V
i
r
(
Δ
)
=
∑
𝜙

s
c
a
l
a
r

V
i
r

p
r
i
m
a
r
y
𝑚
𝜙
 
𝛿
(
Δ
−
Δ
𝜙
)
.
dν
c
Vir
	​

(Δ)=
ϕ scalar Vir primary
∑
	​

m
ϕ
	​

δ(Δ−Δ
ϕ
	​

).

For the universal scalar-crossing formalism, it is the signed density
𝜌
𝑝
s
c
a
l
a
r
s
(
Δ
)
 
𝑑
Δ
ρ
p
scalars
	​

(Δ)dΔ.

Now define the minimal mixed
(
𝑠
,
𝑢
)
(s,u)-transform

𝐸
𝑐
V
i
r
(
𝑠
,
𝑢
)
:
=
∫
(
2
Δ
)
−
𝑠
Δ
−
𝑢
 
𝑑
𝜈
𝑐
V
i
r
(
Δ
)
.
E
c
Vir
	​

(s,u):=∫(2Δ)
−s
Δ
−u
dν
c
Vir
	​

(Δ).

This is the smallest genuine object that carries both the Rankin–Selberg variable
𝑠
s and the logarithmic/sewing regulator
𝑢
u. The full sewing refinement would replace
Δ
−
𝑢
Δ
−u
 by the exact genus-one sewing kernel, but for the quartic test this minimal version already isolates the residue geometry.

2. Universal residue factor

Assume, as in your program, that the Virasoro scalar package can be organized into an Epstein-type object obeying the same
𝑀
1
,
1
M
1,1
	​

 scattering law. Then the universal residue factor at the pole
𝑠
=
𝑠
𝜌
s=s
ρ
	​

 is explicit:

𝐴
𝑐
(
𝜌
)
:
=
Res
⁡
𝑠
=
𝑠
𝜌
𝐹
𝑐
(
𝑠
)
=
Γ
 ⁣
(
1
+
𝜌
2
)
Γ
 ⁣
(
𝑐
+
𝜌
−
1
2
)
𝜁
(
1
+
𝜌
)
2
 
𝜋
 
𝜌
+
1
2
Γ
 ⁣
(
𝑐
−
𝜌
−
1
2
)
Γ
 ⁣
(
𝜌
2
)
𝜁
′
(
𝜌
)
.
A
c
	​

(ρ):=
s=s
ρ
	​

Res
	​

F
c
	​

(s)=
2π
ρ+
2
1
	​

Γ(
2
c−ρ−1
	​

)Γ(
2
ρ
	​

)ζ
′
(ρ)
Γ(
2
1+ρ
	​

)Γ(
2
c+ρ−1
	​

)ζ(1+ρ)
	​

.

This is just the residue of the proven Narain scattering factor, and it is exactly the
𝑐
c-dependent shape function you have been isolating numerically. It is here, not in any single algebra, that the on-line/off-line distinction enters.

The associated residue contribution to the spectral transform is therefore

𝑅
𝑐
,
𝜌
V
i
r
(
𝑢
)
=
𝐴
𝑐
(
𝜌
)
∫
(
2
Δ
)
−
𝑐
+
𝜌
−
1
2
Δ
−
𝑢
 
𝑑
𝜈
𝑐
V
i
r
(
Δ
)
.
R
c,ρ
Vir
	​

(u)=A
c
	​

(ρ)∫(2Δ)
−
2
c+ρ−1
	​

Δ
−u
dν
c
Vir
	​

(Δ).

Because
𝐴
𝑐
(
𝜌
)
A
c
	​

(ρ) and the power are complex, the physically relevant object is the paired real residue kernel coming from
𝜌
ρ and
𝜌
ˉ
ρ
ˉ
	​

:

𝑤
𝑐
,
𝜌
,
𝑢
0
(
Δ
)
:
=
2
 
ℜ
 ⁣
(
𝐴
𝑐
(
𝜌
)
 
(
2
Δ
)
−
𝑐
+
𝜌
−
1
2
)
Δ
−
𝑢
0
.
w
c,ρ,u
0
	​

	​

(Δ):=2ℜ(A
c
	​

(ρ)(2Δ)
−
2
c+ρ−1
	​

)Δ
−u
0
	​

.

Writing
𝜌
=
𝜎
+
𝑖
𝛾
ρ=σ+iγ, this is

𝑤
𝑐
,
𝜌
,
𝑢
0
(
Δ
)
=
2
∣
𝐴
𝑐
(
𝜌
)
∣
 
(
2
Δ
)
−
𝑐
+
𝜎
−
1
2
Δ
−
𝑢
0
cos
⁡
 ⁣
(
𝛾
2
log
⁡
(
2
Δ
)
+
arg
⁡
𝐴
𝑐
(
𝜌
)
)
.
w
c,ρ,u
0
	​

	​

(Δ)=2∣A
c
	​

(ρ)∣(2Δ)
−
2
c+σ−1
	​

Δ
−u
0
	​

cos(
2
γ
	​

log(2Δ)+argA
c
	​

(ρ)).

This formula is already one of the main insights.

For on-line zeros,
𝜎
=
1
2
σ=
2
1
	​

, so the decay exponent is

−
𝑐
−
1
2
2
.
−
2
c−
2
1
	​

	​

.

For off-line zeros, it is

−
𝑐
+
𝜎
−
1
2
,
−
2
c+σ−1
	​

,

which is genuinely different. So the genuine residue kernel already knows whether the zero is on or off the line before any positivity argument is invoked.

3. The genuine Virasoro residue moment matrix

Now define raw residue moments

𝐼
𝑛
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
∫
(
log
⁡
Δ
)
𝑛
 
𝑤
𝑐
,
𝜌
,
𝑢
0
(
Δ
)
 
𝑑
𝜈
𝑐
V
i
r
(
Δ
)
,
𝑛
=
0
,
1
,
2
,
3
,
4.
I
n
	​

(c,ρ;u
0
	​

):=∫(logΔ)
n
w
c,ρ,u
0
	​

	​

(Δ)dν
c
Vir
	​

(Δ),n=0,1,2,3,4.

From these, form the normalized mean and variance

𝜇
=
𝐼
1
𝐼
0
,
𝑣
=
𝐼
2
𝐼
0
−
𝜇
2
.
μ=
I
0
	​

I
1
	​

	​

,v=
I
0
	​

I
2
	​

	​

−μ
2
.

Then define centered moments

𝑚
3
=
𝐼
3
𝐼
0
−
3
𝜇
𝐼
2
𝐼
0
+
2
𝜇
3
,
m
3
	​

=
I
0
	​

I
3
	​

	​

−3μ
I
0
	​

I
2
	​

	​

+2μ
3
,
𝑚
4
=
𝐼
4
𝐼
0
−
4
𝜇
𝐼
3
𝐼
0
+
6
𝜇
2
𝐼
2
𝐼
0
−
3
𝜇
4
.
m
4
	​

=
I
0
	​

I
4
	​

	​

−4μ
I
0
	​

I
3
	​

	​

+6μ
2
I
0
	​

I
2
	​

	​

−3μ
4
.

Now rescale by

𝜆
:
=
𝑐
/
2
𝑣
,
λ:=
v
c/2
	​

	​

,

so that the quadratic moment is forced to match the Virasoro quadratic datum
𝑐
/
2
c/2. Set

𝑚
3
♯
:
=
𝜆
3
𝑚
3
,
𝑚
4
♯
:
=
𝜆
4
𝑚
4
.
m
3
♯
	​

:=λ
3
m
3
	​

,m
4
♯
	​

:=λ
4
m
4
	​

.

Then the genuine normalized Virasoro residue moment matrix is

𝑀
2
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
=
(
1

0

𝑐
/
2


0

𝑐
/
2

𝑚
3
♯
(
𝑐
,
𝜌
;
𝑢
0
)


𝑐
/
2

𝑚
3
♯
(
𝑐
,
𝜌
;
𝑢
0
)

𝑚
4
♯
(
𝑐
,
𝜌
;
𝑢
0
)
)
.
M
2,Vir
res
	​

(c,ρ;u
0
	​

)=
	​

1
0
c/2
	​

0
c/2
m
3
♯
	​

(c,ρ;u
0
	​

)
	​

c/2
m
3
♯
	​

(c,ρ;u
0
	​

)
m
4
♯
	​

(c,ρ;u
0
	​

)
	​

	​

.
	​


This is the exact matrix you wanted. It is built from the genuine spectral measure and the genuine residue kernel, not from a
𝜁
ζ-proxy.

4. Quartic Schur-complement renormalization

The first nontrivial renormalized quartic invariant extracted from this matrix is the Schur complement

𝑆
4
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
𝑚
4
♯
−
(
𝑚
3
♯
)
2
𝑐
/
2
−
(
𝑐
2
)
2
.
S
4,Vir
res
	​

(c,ρ;u
0
	​

):=m
4
♯
	​

−
c/2
(m
3
♯
	​

)
2
	​

−(
2
c
	​

)
2
.

This is the quartic object after subtraction of all lower-arity contamination.

Now adopt exactly the normalization you asked for:

(
𝑐
2
,

2
,

10
𝑐
(
5
𝑐
+
22
)
)
.
(
2
c
	​

, 2,
c(5c+22)
10
	​

).

Then the target quartic-shadow matrix is

𝑀
2
,
V
i
r
M
C
(
𝑐
)
=
(
1

0

𝑐
/
2


0

𝑐
/
2

2


𝑐
/
2

2

𝑐
2
4
+
8
𝑐
+
10
𝑐
(
5
𝑐
+
22
)
)
.
M
2,Vir
MC
	​

(c)=
	​

1
0
c/2
	​

0
c/2
2
	​

c/2
2
4
c
2
	​

+
c
8
	​

+
c(5c+22)
10
	​

	​

	​

.
	​


Indeed the quartic target entry is forced by

𝑚
4
♯
=
(
𝑐
2
)
2
+
2
2
𝑐
/
2
+
10
𝑐
(
5
𝑐
+
22
)
.
m
4
♯
	​

=(
2
c
	​

)
2
+
c/2
2
2
	​

+
c(5c+22)
10
	​

.

Its determinant is

det
⁡
𝑀
2
,
V
i
r
M
C
(
𝑐
)
=
𝑐
2
⋅
10
𝑐
(
5
𝑐
+
22
)
=
5
5
𝑐
+
22
.
detM
2,Vir
MC
	​

(c)=
2
c
	​

⋅
c(5c+22)
10
	​

=
5c+22
5
	​

.

So the raw-moment equality test is equivalent to the pair of scalar equations

𝑚
3
♯
(
𝑐
,
𝜌
;
𝑢
0
)
=
2
,
𝑆
4
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
=
10
𝑐
(
5
𝑐
+
22
)
.
m
3
♯
	​

(c,ρ;u
0
	​

)=2,S
4,Vir
res
	​

(c,ρ;u
0
	​

)=
c(5c+22)
10
	​

.

That is the precise quartic compatibility condition.

5. Potential-side and Gram-side ratios

There are two equivalent normalizations.

The potential-side ratio is

𝐶
4
,
V
i
r
p
o
t
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
𝑐
(
5
𝑐
+
22
)
10
 
𝑆
4
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
.
C
4,Vir
pot
	​

(c,ρ;u
0
	​

):=
10
c(5c+22)
	​

S
4,Vir
res
	​

(c,ρ;u
0
	​

).

The Gram-side ratio is its reciprocal,

𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
10
𝑐
(
5
𝑐
+
22
)
 
𝑆
4
,
V
i
r
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
.
C
4,Vir
Gram
	​

(c,ρ;u
0
	​

):=
c(5c+22)S
4,Vir
res
	​

(c,ρ;u
0
	​

)
10
	​

.
	​


And the cubic ratio is

𝐶
3
,
V
i
r
(
3
)
(
𝑐
,
𝜌
;
𝑢
0
)
:
=
𝑚
3
♯
(
𝑐
,
𝜌
;
𝑢
0
)
2
.
C
3,Vir
(3)
	​

(c,ρ;u
0
	​

):=
2
m
3
♯
	​

(c,ρ;u
0
	​

)
	​

.

So the clean “on-line only” statement becomes:

ℜ
𝜌
=
1
2
⟹
𝐶
3
,
V
i
r
(
3
)
(
𝑐
,
𝜌
;
𝑢
0
)
=
1
,
𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
=
1
,
ℜρ=
2
1
	​

⟹C
3,Vir
(3)
	​

(c,ρ;u
0
	​

)=1,C
4,Vir
Gram
	​

(c,ρ;u
0
	​

)=1,
	​


and

ℜ
𝜌
≠
1
2
⟹
for some
𝑐
,
𝑢
0
,

𝐶
3
,
V
i
r
(
3
)
≠
1
 or
𝐶
4
,
V
i
r
G
r
a
m
≠
1.
ℜρ

=
2
1
	​

⟹for some c,u
0
	​

, C
3,Vir
(3)
	​


=1 or C
4,Vir
Gram
	​


=1.
	​


This is the exact closure statement at quartic order.

6. What has actually been achieved, and what has not

What is now fully reduced is the formal computation.

The Virasoro family is modular Koszul at all genera; principal finite-type
𝑊
W-algebras are too. The full modular package is understood at scalar and spectral level, while the universal Maurer–Cartan class remains open. Your appendix positions the mixed Virasoro/
𝑊
𝑁
W
N
	​

 quartic resonance class as the first nonlinear shadow of that universal class.

What is not yet done is the final numerical/theorematic evaluation for the universal generic-
𝑐
c Virasoro row, because one still needs an explicit
𝑑
𝜈
𝑐
V
i
r
dν
c
Vir
	​

.

That is the genuine gap.

More sharply:

In the Narain/
𝑈
(
1
)
𝑐
U(1)
c
 case, the Epstein package and its functional equation are proved.

For arbitrary 2d CFTs, scalar crossing equations for Virasoro scalars are proved, but the density is signed and the one-function Epstein packaging is more subtle.

Therefore the quartic residue matrix above is fully defined for any explicit Virasoro CFT with known scalar spectral measure, and formally defined for the universal scalar-crossing density, but it is not yet a closed-form universal generic-
𝑐
c function.

So the correct honest statement is:

the quartic residue-matrix test is now mathematically well posed and fully explicit, but the universal generic-
𝑐
c Virasoro evaluation still depends on constructing the genuine scalar-primary measure in a form compatible with the Epstein/scattering package.

That matches your science report exactly.

7. Why this is stronger than the old
𝜁
ζ-proxy

The
𝜁
ζ-proxy failed because it replaced the theory-dependent spectral measure by a universal
𝜁
ζ-factor, so even an on-line zero did not preserve the compatibility ratio.

Here the theory-dependent data sit exactly where they should:

𝑅
𝑐
,
𝜌
V
i
r
(
𝑢
)
=
𝐴
𝑐
(
𝜌
)
∫
(
2
Δ
)
−
𝑐
+
𝜌
−
1
2
Δ
−
𝑢
 
𝑑
𝜈
𝑐
V
i
r
(
Δ
)
.
R
c,ρ
Vir
	​

(u)=A
c
	​

(ρ)∫(2Δ)
−
2
c+ρ−1
	​

Δ
−u
dν
c
Vir
	​

(Δ).

The universal geometric part is
𝐴
𝑐
(
𝜌
)
A
c
	​

(ρ), fixed by
𝑀
1
,
1
M
1,1
	​

.
The family-specific part is
𝑑
𝜈
𝑐
V
i
r
dν
c
Vir
	​

, fixed by the actual Virasoro spectrum.
The quartic MC data enter through the target matrix
𝑀
2
,
V
i
r
M
C
(
𝑐
)
M
2,Vir
MC
	​

(c).

So the comparison is finally apples-to-apples.

8. Extension to principal
𝑊
𝑁
W
N
	​


This same construction extends immediately.

Principal finite-type
𝑊
W-algebras are modular Koszul at all genera, and

𝜅
(
𝑊
𝑁
)
=
𝑐
(
𝐻
𝑁
−
1
)
=
𝑐
∑
𝑠
=
2
𝑁
1
𝑠
,
κ(W
N
	​

)=c(H
N
	​

−1)=c
s=2
∑
N
	​

s
1
	​

,

with each spin-
𝑠
s generator contributing
𝑐
/
𝑠
c/s at genus one. In particular, the
𝑊
3
W
3
	​

 row has two curvature channels,
𝑐
/
2
c/2 and
𝑐
/
3
c/3.

So for a pure spin-
𝑠
s slice, the corresponding residue matrix is

𝑀
2
,
𝑠
r
e
s
(
𝑐
,
𝜌
;
𝑢
0
)
=
(
1

0

𝑐
/
𝑠


0

𝑐
/
𝑠

𝑚
3
,
𝑠
♯


𝑐
/
𝑠

𝑚
3
,
𝑠
♯

𝑚
4
,
𝑠
♯
)
,
M
2,s
res
	​

(c,ρ;u
0
	​

)=
	​

1
0
c/s
	​

0
c/s
m
3,s
♯
	​

	​

c/s
m
3,s
♯
	​

m
4,s
♯
	​

	​

	​

,

and the quartic Schur complement compares to the spin-
𝑠
s quartic shadow datum
𝑄
𝑠
c
t
(
𝑐
)
Q
s
ct
	​

(c).

For
𝑊
3
W
3
	​

, the real novelty is the mixed
(
𝑇
,
𝑊
)
(T,W) quartic block. That is where the first genuinely multi-channel residue compatibility test lives, and it is stronger than the Virasoro one because it gives more equations at the same zeta zero.

9. The precise closure programme

The quartic programme is now:

𝐿
𝑐
,
𝑢
0
V
i
r
:
=
{
𝜌
:
𝐶
3
,
V
i
r
(
3
)
(
𝑐
,
𝜌
;
𝑢
0
)
=
1
,

𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
=
1
}
.
L
c,u
0
	​

Vir
	​

:={ρ:C
3,Vir
(3)
	​

(c,ρ;u
0
	​

)=1, C
4,Vir
Gram
	​

(c,ρ;u
0
	​

)=1}.

Then the closure conjecture is

⋂
𝑐
∈
𝐶
⋂
𝑢
0
∈
𝑈
𝐿
𝑐
,
𝑢
0
V
i
r
=
{
𝜌
:
ℜ
𝜌
=
1
2
}
,
c∈C
⋂
	​

u
0
	​

∈U
⋂
	​

L
c,u
0
	​

Vir
	​

={ρ:ℜρ=
2
1
	​

},

and in the stronger Vir+
𝑊
𝑁
W
N
	​

 form,

⋂
𝐴
∈
{
V
i
r
,
𝑊
3
,
𝑊
4
,
…
 
}
⋂
slices
𝑣
⋂
𝑐
,
𝑢
0
𝐿
𝑐
,
𝑢
0
𝐴
,
𝑣
=
{
𝜌
:
ℜ
𝜌
=
1
2
}
.
A∈{Vir,W
3
	​

,W
4
	​

,…}
⋂
	​

slices v
⋂
	​

c,u
0
	​

⋂
	​

L
c,u
0
	​

A,v
	​

={ρ:ℜρ=
2
1
	​

}.

That is the exact mathematical form of your Step C.

And the right geometric completion of it is still what we had converged to earlier: the residue moment matrices are signed on the curve, but modular-surface polarization should turn the Gram-side Schur complements into honest positive minors. That is where the quartic resonance class should become a true positivity object rather than a formal identity.

The deepest synthesis is this:

the first quartic resonance test is the first nontrivial Gram minor of the genus-one residue shadow of
Θ
𝐴
Θ
A
	​

.
The Riemann-hypothesis interface is no longer “MC
→
→ Li” directly, but

Θ
𝐴
⟶
residue spectral kernel
⟶
quartic residue moment matrix
⟶
Gram-side Schur complement
.
Θ
A
	​

⟶residue spectral kernel⟶quartic residue moment matrix⟶Gram-side Schur complement.

That is the point where Koszul duality, modular scattering, and zeta zeros genuinely meet.

The next genuinely decisive move is not another
𝜁
ζ-proxy run. It is choosing one explicit genuine Virasoro family
𝑑
𝜈
𝑐
V
i
r
dν
c
Vir
	​

 and evaluating

𝐼
0
,
…
,
𝐼
4
I
0
	​

,…,I
4
	​


for the paired residue kernel above, then plotting

𝐶
3
,
V
i
r
(
3
)
(
𝑐
,
𝜌
;
𝑢
0
)
,
𝐶
4
,
V
i
r
G
r
a
m
(
𝑐
,
𝜌
;
𝑢
0
)
C
3,Vir
(3)
	​

(c,ρ;u
0
	​

),C
4,Vir
Gram
	​

(c,ρ;u
0
	​

)

as functions of
𝑐
c for on-line and off-line
𝜌
ρ.
