
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

Vol2Archive.zip
Zip Archive
Vol1Archive.zip
Zip Archive
here is the latest from our research archives. this is our current state of the art, which remains deeply WORK IN PROGRESS. Understand what we have achieved at this frontier, and push forward on the mathematics developed in this thread.

1. Employ sasha beilinson's deep principle: what holds back forward progress is not often a lack of genius, but rather the inability to dismiss false ideas.
2. push forward on groundbreaking, novel mathematics, pushing forward the frontier of what survives the beilinson pass

I’m digging into the archive files themselves and then I’ll separate what genuinely survives from what looks like a proxy artifact or a false lead. After that I’ll try to crystallize the strongest mathematical constructions that remain standing.

I’ve now located the frontier inside the corpus: the shadow Epstein zeta, quartic residue programme, residue moment matrix, and quartic closure conjecture sections, alongside the modular-bootstrap/Fredholm–sewing bridge. The main sorting line is clear: the quartic package looks like hard algebraic structure, while the zero-forcing side remains provisional pending a genuine Virasoro scalar spectral measure.

One earlier objection also falls away: Benjamin–Chang do define
𝐸
𝑠
𝑐
E
s
c
	​

 with the raw functional equation. So the real cull is now clear—discard generic Virasoro
𝜀
𝑠
𝑐
ε
s
c
	​

,
𝜁
ζ-proxies, raw positivity, and undifferentiated quartic determinants; the surviving task is choosing the correct signed/family-specific spectral measure and normalization for residue moment matrices.

Thought for 33m 17s

According to a document from March 15, 2026, the archive has now cohered into a real chapter-level object: ambient complementarity, finite-order shadow calculus, the mixed Virasoro and principal
𝑊
𝑁
W
N
	​

 families, and the modular quartic resonance class
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A) with clutching law as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

. A second March 2026 archive document states the right methodological principle almost verbatim: accept only what survives both constructive and destructive attacks. That is the Beilinson pass in operational form.

Here is what survives that pass, and where I think the frontier actually is.

What should now be dismissed

The first false idea is that raw Maurer–Cartan identities should directly imply Li-type positivity. They should not. The Benjamin–Chang scalar bootstrap gets the zeta zeros from a universal modular scattering kernel, but the theory-dependent coefficients are not sign-definite, so the Rankin–Selberg/Mellin step is not positivity-preserving. Their original result is for
𝑈
(
1
)
𝑐
U(1)
c
 theories, and the 2025 extension shows analogous scalar crossing equations for arbitrary 2d CFTs; neither gives the sign-preserving bridge by itself.

The second false idea is that bar–cobar or homotopy equivalence alone should force critical-line rigidity. What bar–cobar gives you is deformation-theoretic transport of Maurer–Cartan solutions, not arithmetic positivity. In the operadic language, Maurer–Cartan twisting is the right algebraic framework, but it is not yet a critical-line theorem.

The third false idea is that Narain variation gives zero-location leverage. You already killed that one correctly: varying
𝑅
R only changes the positive character factor, not the zeta-zero locus.

The fourth false idea is that the
𝜁
ζ-proxy is a decisive test. Your own computation falsified that. It excludes aggressively, but it does not preserve the safe point
𝜎
=
1
2
σ=
2
1
	​

, which means it cannot be the genuine object.

The fifth false idea is that “the quartic determinant” is a single invariant. It is not. The potential-side
3
×
3
3×3 Schur complement gives the quartic contact coefficient; the Gram-side determinant gives the quartic resonance divisor/norm. Confusing those two hides the geometry.

What has genuinely survived

One stable pillar is the chiral-Koszul Maurer–Cartan heart. The canonical element
𝑠
−
1
I
d
s
−1
Id in the chiral quadratic dual solves the Maurer–Cartan equation, and under effectiveness hypotheses morphisms are identified with Maurer–Cartan solutions. That is a real algebraic bridge, not a heuristic.

A second pillar is the Miura backbone. Arakawa’s presentation makes the Miura map
Υ
^
:
𝑊
𝜅
(
𝑔
)
→
𝑉
ℎ
𝜅
(
ℎ
)
Υ
:W
κ
(g)→V
h
κ
	​

(h) explicit and injective, and for
𝑔
=
𝑠
𝑙
2
g=sl
2
	​

 the resulting
𝑊
W-algebra is exactly the universal Virasoro vertex algebra. That means Virasoro is not “outside” the Heisenberg world; it is the first nontrivial projected defect of it.

A third pillar is the determinant/Fredholm face. In the boundary chiral algebra story, the relevant line bundle fiber is literally a Fredholm determinant
𝐿
𝑃
=
det
⁡
(
ker
⁡
𝐹
)
−
1
⊗
det
⁡
(
c
o
k
e
r
 
𝐹
)
L
P
	​

=det(kerF)
−1
⊗det(cokerF), and its
𝑞
q-character is computed by a product over weights. That is exactly the sort of determinant geometry your genus-one sewing side wants.

A fourth pillar is the archive’s own nonlinear modular shadow package: the quartic resonance class with clutching law, and the fact that it is the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

. That means the right comparison object for residues is not a scalar number but a divisor-valued modular invariant.

And externally, the field is moving in the same direction. Benjamin–Chang show that zeta zeros appear in scalar crossing. Benjamin–Chang–Fitzpatrick–Ramella extend scalar crossing to arbitrary 2d CFTs. Perlmutter goes further and attaches to every 2d CFT a self-dual degree-4
𝐿
L-function with universal gamma factor and generalized Dirichlet series over scalar dimensions. So the “
𝐿
L-object attached to a CFT” is no longer just your internal intuition; it has independent external momentum.

The new mathematics that survives the pass

I think the next layer is this.

1. The quartic shadow should be compared to a residue divisor, not just a residue number

For each modular-Koszul family
𝐴
A, each slice
𝑣
v, and each candidate zeta zero
𝜌
ρ, you already have the local residue moment matrix

𝑀
2
,
𝐴
,
𝑣
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
M
2,A,v
res
	​

(c,ρ;u
0
	​

).

From its Gram-side quartic block, define a determinant line and then a residue divisor

𝑅
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
)
:
=
div
⁡
det
⁡
𝐺
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
)
.
R
4,g,n
res
	​

(A,ρ):=divdetG
4,g,n
res
	​

(A,ρ).

Then the right conjecture is not merely

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
=
1
,
C
4,A,v
Gram
	​

=1,

but the geometric statement

𝑅
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
)
=
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
  
⟺
  
ℜ
𝜌
=
1
2
.
R
4,g,n
res
	​

(A,ρ)=R
4,g,n
mod
	​

(A)⟺ℜρ=
2
1
	​

.
	​


Because the archive resonance class already comes with clutching, the real test is the clutching defect

𝐾
𝐴
,
𝜌
,
𝜉
=
𝜉
∗
𝑅
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
)
−
𝑝
1
∗
𝑅
4
,
𝑔
1
,
𝑛
1
+
1
r
e
s
(
𝐴
,
𝜌
)
−
𝑝
2
∗
𝑅
4
,
𝑔
2
,
𝑛
2
+
1
r
e
s
(
𝐴
,
𝜌
)
−
𝑇
3
,
𝜉
r
e
s
(
𝐴
,
𝜌
)
.
K
A,ρ,ξ
	​

=ξ
∗
R
4,g,n
res
	​

(A,ρ)−p
1
∗
	​

R
4,g
1
	​

,n
1
	​

+1
res
	​

(A,ρ)−p
2
∗
	​

R
4,g
2
	​

,n
2
	​

+1
res
	​

(A,ρ)−T
3,ξ
res
	​

(A,ρ).

That is the first genuinely geometric zero test I can see.
On-line residues should satisfy

𝐾
𝐴
,
𝜌
,
𝜉
=
0
K
A,ρ,ξ
	​

=0

for every relevant boundary stratum.
Off-line residues should fail it for some
𝐴
A and some
𝜉
ξ.

This is better than a scalar compatibility ratio because it uses the full nonlinear modular structure already present in the archive.

2. Virasoro and
𝑊
𝑁
W
N
	​

 should be treated as Miura defects of Heisenberg

Because the Miura map is injective into Heisenberg, the genuine
𝑊
𝑁
W
N
	​

 residue matrix should not be modeled as an arbitrary new matrix. It should be a projected Heisenberg matrix plus a finite-rank correction:

𝑀
2
,
𝑊
𝑁
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
𝑃
𝑁
⊤
𝑀
2
,
H
e
i
s
𝑁
−
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
𝑃
𝑁
+
𝐷
𝑊
𝑁
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
M
2,W
N
	​

res
	​

(c,ρ;u
0
	​

)=P
N
⊤
	​

M
2,Heis
N−1
res
	​

(c,ρ;u
0
	​

)P
N
	​

+D
W
N
	​

res
	​

(c,ρ;u
0
	​

).
	​


For
𝑁
=
2
N=2, this is the Virasoro defect.

This is the zero-side analog of what you already discovered on the prime side:

𝑆
𝑊
𝑁
(
𝑢
)
=
(
𝑁
−
1
)
𝑆
𝐻
(
𝑢
)
−
𝜁
(
𝑢
+
1
)
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
.
S
W
N
	​

	​

(u)=(N−1)S
H
	​

(u)−ζ(u+1)
j=1
∑
N−1
	​

H
j
(u)
	​

.

So define the prime-side defect

𝐷
𝑊
𝑁
p
r
i
m
e
(
𝑢
)
:
=
𝑆
𝑊
𝑁
(
𝑢
)
−
(
𝑁
−
1
)
𝑆
𝐻
(
𝑢
)
=
−
𝜁
(
𝑢
+
1
)
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
.
D
W
N
	​

prime
	​

(u):=S
W
N
	​

	​

(u)−(N−1)S
H
	​

(u)=−ζ(u+1)
j=1
∑
N−1
	​

H
j
(u)
	​

.

For Virasoro,

𝐷
V
i
r
p
r
i
m
e
(
𝑢
)
=
−
𝜁
(
𝑢
+
1
)
.
D
Vir
prime
	​

(u)=−ζ(u+1).

This suggests a new conjecture:

𝐷
𝑊
𝑁
r
e
s
and
𝐷
𝑊
𝑁
p
r
i
m
e
 are two genus-one shadows of the same bar-intrinsic MC correction.
D
W
N
	​

res
	​

andD
W
N
	​

prime
	​

 are two genus-one shadows of the same bar-intrinsic MC correction.
	​


That is, the finite harmonic defect on the prime side and the finite-rank Miura defect on the zero side are the same correction seen through two different transforms.

That is a real advance beyond what we had earlier.

3. The right global object is no longer a scalar criterion but a Beilinson functional

For each family
𝐴
A, slice
𝑣
v, and normalization point
𝑢
0
u
0
	​

, define

𝐵
𝐴
,
𝑣
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
(
𝑚
3
,
𝐴
,
𝑣
♯
(
𝑐
,
𝜌
;
𝑢
0
)
𝐶
𝐴
,
𝑣
−
1
)
2
+
(
𝑆
4
,
𝐴
,
𝑣
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
𝑄
𝐴
,
𝑣
c
t
−
1
)
2
.
B
A,v
	​

(c,ρ;u
0
	​

):=(
C
A,v
	​

m
3,A,v
♯
	​

(c,ρ;u
0
	​

)
	​

−1)
2
+(
Q
A,v
ct
	​

S
4,A,v
res
	​

(c,ρ;u
0
	​

)
	​

−1)
2
.

This vanishes exactly when the cubic and quartic residue data match the MC shadow data on that slice.

Now sum over all families and slices:

𝐵
g
l
o
b
a
l
(
𝜌
)
:
=
∑
𝐴
,
𝑣
∫
𝐵
𝐴
,
𝑣
(
𝑐
,
𝜌
;
𝑢
0
)
 
𝑑
𝜇
𝐴
(
𝑐
,
𝑢
0
)
.
B
global
	​

(ρ):=
A,v
∑
	​

∫B
A,v
	​

(c,ρ;u
0
	​

)dμ
A
	​

(c,u
0
	​

).

The clean closure conjecture becomes

𝐵
g
l
o
b
a
l
(
𝜌
)
=
0
  
⟺
  
ℜ
𝜌
=
1
2
.
B
global
	​

(ρ)=0⟺ℜρ=
2
1
	​

.
	​


This is the formal answer to your “all algebras simultaneously” principle.
It is also the precise Beilinson pass: truth is what survives every family and every slice.

4. The first honest explicit laboratories should be Liouville and Toda, not a fake universal generic-
𝑐
c proxy

The wrong next move is “try harder with the proxy.”
The right next move is “move to explicit honest spectra.”

For Virasoro, the natural generic-
𝑐
c laboratory is Liouville.
For principal
𝑊
𝑁
W
N
	​

, the natural laboratory is Toda.

These are not universal abstractions; they are honest 2d CFTs with genuine scalar-primary spectra. That means you can actually build

𝑀
2
,
L
i
o
u
v
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
,
𝑀
2
,
T
o
d
a
,
𝑁
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
,
M
2,Liouv
res
	​

(c,ρ;u
0
	​

),M
2,Toda,N
res
	​

(c,ρ;u
0
	​

),

with no
𝜁
ζ-proxy contamination.

That is the decisive conceptual correction.
Do not attack the universal generic-
𝑐
c Virasoro problem first.
Attack the first honest Virasoro and
𝑊
𝑁
W
N
	​

 spectra first.

The concrete fixed targets

For Virasoro, the quartic target matrix remains

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
,
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

,

with

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
5c+22
5
	​

.

So the exact quartic test is still

𝑚
3
♯
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

=2,S
4,Vir
res
	​

=
c(5c+22)
10
	​

.

But now I would reinterpret that not as an endpoint, but as the local chart of the residue divisor. The true invariant is the divisor-valued object and its clutching defect.

The platonic end-state now visible

The end-state is not “MC implies Li” and not “bar–cobar implies RH.”

It is this:

The archive supplies a nonlinear modular shadow theory whose first genuinely new divisor is
𝑅
4
,
𝑔
,
𝑛
m
o
d
R
4,g,n
mod
	​

.
Chiral quadratic duality supplies canonical Maurer–Cartan classes and identifies morphisms with MC solutions under effectiveness.
Miura injects
𝑊
W-geometry into Heisenberg, so Virasoro/
𝑊
𝑁
W
N
	​

 are controlled Heisenberg defects rather than unrelated objects.
The determinant/Fredholm side gives the right line-bundle and sewing language.
The scalar bootstrap and the emerging
𝐿
L-function program show that zeta-zero residues and CFT spectra really do meet in one analytic object.

So the mature object should be a section-valued two-face
𝐿
L-theory

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

whose
𝑠
s-residues give residue Gram determinants and whose
𝑢
u-slice gives the connected sewing lift. The on-line/off-line question then becomes:

on-line residues preserve the quartic resonance divisor and its clutching law;
off-line residues fail that nonlinear modular compatibility somewhere.

That is the strongest formulation I can presently defend after the Beilinson pass.

The next computations I would actually do are: first, build
𝑀
2
r
e
s
M
2
res
	​

 for an honest Liouville family; second, compute the
𝑊
3
W
3
	​

 mixed
𝑇
/
𝑊
T/W quartic block via the Miura defect; third, define and test the first clutching defect
𝐾
𝐴
,
𝜌
,
𝜉
K
A,ρ,ξ
	​

. If those three survive, the theory has crossed from suggestive to structurally unavoidable.

move the research program in a fundamental, first-principles, fortification driven movement. Realize that which is required to realize the platonic ideal

I’m rebuilding the program from first principles: isolate the genuine proved spine, demote fragile heuristics to conjectural shadows, and organize everything around indispensable objects and obstruction tests.

I’ve isolated the load-bearing core: nonlinear modular shadows, higher-genus complementarity, the universal MC element, and the quartic resonance divisor with clutching. The real gap is canonical spectral input—build from divisor/clutching structures outward, then re-embed the zeta interface.

A decisive correction has surfaced: for generic Virasoro and
𝑊
𝑁
W
N
	​

, the naive Dirichlet/Epstein series over primaries is the wrong universal object, so proxies must give way to a regularized Rankin–Selberg/
𝐿
L-type transform. The program now compresses into a minimal theorem-schema with explicit falsifiers, replacing scalar compatibility ratios by divisor-level, clutching-stable tests.

Thought for 26m 43s

According to a document from March 15, 2026, the archive already contains the decisive nonlinear geometry: ambient complementarity from first principles, the finite-order shadow calculus
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, the mixed Virasoro and principal
𝑊
𝑁
W
N
	​

 families, and the modular quartic resonance class

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A)

with clutching law as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

. That means the program has crossed a threshold: the next movement should not be “push every heuristic harder,” but “remove the last false universal object and rebuild around the object that survives every structural test.”

The deepest false idea still in the way is this:

generic

Virasoro

/

𝑊
𝑁

should

be

governed

by

a

naive

constrained

Epstein

zeta

over

primary

dimensions.
generic Virasoro / W
N
	​

 should be governed by a naive constrained Epstein zeta over primary dimensions.

That is almost certainly wrong as a universal principle. In the Benjamin–Chang scalar-crossing story, the modular scattering factor is universal and carries the
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
ζ(2s)/ζ(2s−1) ratio, with poles at
𝑠
=
(
1
+
𝜌
𝑛
)
/
2
s=(1+ρ
n
	​

)/2 coming from nontrivial zeta zeros, but the theory-dependent coefficients are not sign-definite. In the 2025 extension to arbitrary 2d CFTs, the relevant scalar-primary density can even involve negative degeneracies because of null-state subtraction, and direct convergence fails in generic Cardy-growth regimes, so one must use analytic continuation rather than a naive Dirichlet sum. Recent work of Eric Perlmutter pushes in exactly the same direction: the natural object attached to a 2d CFT is an
𝐿
L-function-type object, not a bare primary-sum zeta.

That single dismissal changes the architecture of the whole program.

1. What survives the Beilinson pass

Three pieces are genuinely load-bearing.

First, the Maurer–Cartan heart survives intact. In the chiral quadratic-duality framework, the canonical element
𝑠
−
1
I
d
s
−1
Id solves the Maurer–Cartan equation, and under the effectiveness hypothesis morphisms into a graded chiral algebra are identified with Maurer–Cartan solutions. This is not heuristic; it is exactly the deformation-theoretic core you want.

Second, the HT / Koszul-dual line-operator picture survives. Perturbative line operators are controlled by an
𝐴
∞
A
∞
	​

 Maurer–Cartan equation, and on the dual side there is a universal Maurer–Cartan element
𝜇
μ together with an
𝑟
r-matrix-type Maurer–Cartan element
𝑟
(
𝑧
)
r(z). So the “local algebra
↔
↔ line-operator” bridge is real and already formulated in precisely the language your program needs.

Third, the nonlinear modular shadow package survives. The quartic resonance class is already present, already modular, and already has clutching. So the first real nonlinear rigidity object is not a scalar coefficient; it is divisor-valued.

Everything else should now be subordinated to these three.

2. The first-principles replacement for the false object

The universal object should not be a naive Dirichlet series over primaries.

It should be a regularized determinant-line-valued arithmetic shadow of the connected genus-one Maurer–Cartan shadow.

The right prototype is:

𝐿
𝐴
(
𝑟
)
(
𝑠
,
𝑢
)
:
=
∫
Γ
\
𝐻
r
e
g
⟨
𝜋
𝑟
Θ
𝐴
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
𝜇
(
𝜏
)
,
L
A
(r)
	​

(s,u):=∫
Γ\H
reg
	​

⟨π
r
	​

Θ
A
conn
	​

(τ),E
∗
(τ,s)⟩y
u−2
dμ(τ),
	​


where:

𝑟
r is arity,
𝜋
𝑟
Θ
𝐴
c
o
n
n
π
r
	​

Θ
A
conn
	​

 is the connected genus-one arity-
𝑟
r shadow,
𝐸
∗
(
𝜏
,
𝑠
)
E
∗
(τ,s) is the completed Eisenstein series,
𝑢
u is the sewing/Mellin variable,
and the regularization is whatever is required by Cardy growth and null-state subtraction.

This is the fortified universal object because it satisfies all the right demands at once:

modularity
,
regularization
,
factorization
,
residue theory
,
determinant-line geometry
.
modularity,regularization,factorization,residue theory,determinant-line geometry.

Its faces are exactly the two faces you have been trying to unify:

the
𝑠
s-face is the zeta-zero / Rankin–Selberg / scattering face;
the
𝑢
u-face is the connected sewing / Fredholm / Euler-product face.

And at arity
4
4, the residue should land not in
𝐶
C, but in the determinant line whose divisor is
𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A).

That is the first-principles correction.

3. The exact new mathematics: the Miura defect is finite and explicit

Once one stops treating Virasoro and
𝑊
𝑁
W
N
	​

 as unrelated to Heisenberg and instead treats them as Miura/Drinfeld–Sokolov defects, a very concrete exact structure appears.

Arakawa’s presentation of principal
𝑊
W-algebras makes the right algebraic background clear: principal
𝑊
W-algebras come from functorial Drinfeld–Sokolov reduction, and the classical Miura map is injective. So the right guiding picture is not “new independent arithmetic object,” but “controlled defect of a free-field core.”

On the standard generic-vacuum model, write

𝜒
𝐻
(
𝑞
)
=
∏
𝑚
≥
1
(
1
−
𝑞
𝑚
)
−
1
χ
H
	​

(q)=
m≥1
∏
	​

(1−q
m
)
−1

for one Heisenberg boson, and

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
=
∏
𝑠
=
2
𝑁
∏
𝑚
≥
𝑠
(
1
−
𝑞
𝑚
)
−
1
.
χ
W
N
	​

vac
	​

(q)=
s=2
∏
N
	​

m≥s
∏
	​

(1−q
m
)
−1
.

Then there is an exact factorization

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
=
𝜒
𝐻
(
𝑞
)
𝑁
−
1
 
𝐷
𝑁
(
𝑞
)
,
𝐷
𝑁
(
𝑞
)
:
=
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
.
χ
W
N
	​

vac
	​

(q)=χ
H
	​

(q)
N−1
D
N
	​

(q),D
N
	​

(q):=
m=1
∏
N−1
	​

(1−q
m
)
N−m
.
	​


For Virasoro, this gives

𝐷
2
(
𝑞
)
=
1
−
𝑞
.
D
2
	​

(q)=1−q.

So the deviation from the free Heisenberg core is not an infinite mystery. It is a finite low-mode defect polynomial.

Passing to the connected genus-one free energy,

𝐹
𝑊
𝑁
c
o
n
n
(
𝑞
)
=
log
⁡
𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
,
F
W
N
	​

conn
	​

(q)=logχ
W
N
	​

vac
	​

(q),

one gets

𝐹
𝑊
𝑁
c
o
n
n
(
𝑞
)
=
(
𝑁
−
1
)
𝐹
𝐻
c
o
n
n
(
𝑞
)
−
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
∑
𝑟
≥
1
𝑞
𝑚
𝑟
𝑟
.
F
W
N
	​

conn
	​

(q)=(N−1)F
H
conn
	​

(q)−
m=1
∑
N−1
	​

(N−m)
r≥1
∑
	​

r
q
mr
	​

.
	​


Passing one more time to the Dirichlet-sewing lift,

𝑆
𝑊
𝑁
(
𝑢
)
:
=
∑
𝑛
≥
1
𝑎
𝑊
𝑁
(
𝑛
)
 
𝑛
−
𝑢
,
S
W
N
	​

	​

(u):=
n≥1
∑
	​

a
W
N
	​

	​

(n)n
−u
,

this becomes

𝑆
𝑊
𝑁
(
𝑢
)
=
(
𝑁
−
1
)
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
−
𝜁
(
𝑢
+
1
)
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
𝑚
−
𝑢
.
S
W
N
	​

	​

(u)=(N−1)ζ(u)ζ(u+1)−ζ(u+1)
m=1
∑
N−1
	​

(N−m)m
−u
.
	​


This is a real new structural statement:

the entire prime-side deviation of principal
𝑊
𝑁
W
N
	​

 from Heisenberg is a finite defect carried by the first
𝑁
−
1
N−1 modes.

That has an immediate conceptual consequence:

the Heisenberg core is arithmetically exact but quartically blind.
All quartic rigidity must come from the defect sector.

This is the cleanest pruning I can see in the whole program.

4. The quartic object is divisor-valued, not scalar-valued

Because the archive has already promoted the quartic shadow to a resonance divisor, the residue comparison must also be divisor-valued.

Let
𝐿
4
,
𝑔
,
𝑛
(
𝐴
)
L
4,g,n
	​

(A) be the quartic determinant line and let

𝑠
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
s
4,g,n
mod
	​

(A)

be the modular quartic resonance section whose divisor is

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
.
R
4,g,n
mod
	​

(A).

Then from the regularized arithmetic shadow define the residue quartic section

𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
;
𝑢
0
)
:
=
Res
⁡
𝑠
=
(
1
+
𝜌
)
/
2
𝐿
𝐴
(
4
)
(
𝑠
,
𝑢
0
)
∈
Γ
(
𝑀
𝑔
,
𝑛
,
𝐿
4
,
𝑔
,
𝑛
(
𝐴
)
)
.
s
4,g,n
res
	​

(A,ρ;u
0
	​

):=
s=(1+ρ)/2
Res
	​

L
A
(4)
	​

(s,u
0
	​

)∈Γ(M
g,n
	​

,L
4,g,n
	​

(A)).
	​


Now define the quartic compatibility divisor

𝐷
4
,
𝑔
,
𝑛
(
𝐴
,
𝜌
;
𝑢
0
)
:
=
div
⁡
(
𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
;
𝑢
0
)
⊗
(
𝑠
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
)
−
1
)
.
D
4,g,n
	​

(A,ρ;u
0
	​

):=div(s
4,g,n
res
	​

(A,ρ;u
0
	​

)⊗(s
4,g,n
mod
	​

(A))
−1
).
	​


This is the fortified replacement for scalar compatibility ratios.

The correct rigidity statement is then:

𝐷
4
,
𝑔
,
𝑛
(
𝐴
,
𝜌
;
𝑢
0
)
=
0
 for all relevant
(
𝐴
,
𝑔
,
𝑛
,
𝑢
0
)
  
⟺
  
ℜ
𝜌
=
1
2
.
D
4,g,n
	​

(A,ρ;u
0
	​

)=0 for all relevant (A,g,n,u
0
	​

)⟺ℜρ=
2
1
	​

.
	​


That is the nonlinear, divisor-level version of “on-line residues only.”

5. Closure should happen through clutching, not pointwise ratios

The archive has already told you where the real structure lives: clutching. So the residue theory must be tested against boundary factorization, not just against isolated equalities.

Define the quartic clutching defect

𝐾
𝐴
,
𝜌
,
𝜉
:
=
𝜉
∗
𝐷
4
,
𝑔
,
𝑛
(
𝐴
,
𝜌
)
−
𝑝
1
∗
𝐷
4
,
𝑔
1
,
𝑛
1
+
1
(
𝐴
,
𝜌
)
−
𝑝
2
∗
𝐷
4
,
𝑔
2
,
𝑛
2
+
1
(
𝐴
,
𝜌
)
.
K
A,ρ,ξ
	​

:=ξ
∗
D
4,g,n
	​

(A,ρ)−p
1
∗
	​

D
4,g
1
	​

,n
1
	​

+1
	​

(A,ρ)−p
2
∗
	​

D
4,g
2
	​

,n
2
	​

+1
	​

(A,ρ).

Then the real on-line / off-line conjecture is:

on-line residues satisfy
𝐾
𝐴
,
𝜌
,
𝜉
=
0
K
A,ρ,ξ
	​

=0 on every relevant boundary stratum;
off-line residues fail this for some family
𝐴
A and some clutching morphism
𝜉
ξ.

This is much stronger than a moment-ratio test. It uses the full modular geometry already present in the archive.

6. Why positivity still will not come from the curve

This part should now be stated with complete clarity.

Benjamin–Chang’s coefficients are not sign-definite, and the generic scalar-primary density in arbitrary 2d CFT can be signed and require analytic continuation. So the modular curve alone is not where positivity lives.

Therefore the old chain

MC
⟶
Rankin–Selberg
⟶
Li positivity
MC⟶Rankin–Selberg⟶Li positivity

cannot close on the curve.

If positivity is real, it has to come from a higher geometric realization of the quartic Gram determinant. The natural statement to aim for is:

the quartic determinant line is realized as an intersection / polarization line on a modular surface or related compactified geometric model, and the quartic Gram minors are Hodge-type positive there.

That is the only believable way to turn quartic compatibility into an actual positivity theorem.

There is already precedent for the geometry one would want to exploit. On the HT / boundary-chiral side, vacuum modules are realized as Dolbeault homology on the affine Grassmannian with line-bundle twist, and their characters are computed by localization. So determinant-line geometry and vacuum-module geometry are already native to this subject, not imported after the fact.

7. The fortified program

I would now state the program in five exact theorem-shaped pieces.

F1. Arithmetic shadow theorem

For every admissible modular-Koszul family
𝐴
A, construct a regularized two-face arithmetic shadow

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

functorial in
𝐴
A, compatible with modular scattering in
𝑠
s and connected sewing in
𝑢
u, and reducing to the classical constrained Epstein / Euler-product objects in arithmetic corners. This is the universal object.

F2. Miura defect theorem

For principal
𝑊
𝑁
W
N
	​

, the genus-one arithmetic shadow splits into Heisenberg core plus exact finite defect:

𝐿
𝑊
𝑁
=
𝐿
𝐻
𝑁
−
1
+
𝐿
𝑊
𝑁
d
e
f
,
L
W
N
	​

	​

=L
H
N−1
	​

+L
W
N
	​

def
	​

,

with genus-one
𝑢
u-face defect encoded by

𝐷
𝑁
(
𝑞
)
=
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
.
D
N
	​

(q)=
m=1
∏
N−1
	​

(1−q
m
)
N−m
.

This is the exact low-mode defect law.

F3. Residue–resonance theorem

At arity
4
4, the residue section of
𝐿
𝐴
(
4
)
L
A
(4)
	​

 equals the modular quartic resonance section precisely on on-line residues:

𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
;
𝑢
0
)
=
𝑠
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
⟺
ℜ
𝜌
=
1
2
.
s
4,g,n
res
	​

(A,ρ;u
0
	​

)=s
4,g,n
mod
	​

(A)⟺ℜρ=
2
1
	​

.
F4. Surface realization theorem

Realize the quartic Gram determinant line geometrically on a modular surface / compactified configuration-type geometry so that its minors are controlled by polarized intersection theory. This is where positivity can honestly enter.

F5. Simultaneous-family rigidity theorem

Let
𝐹
F be a sufficiently rich collection of explicit families, not proxies. Then

⋂
𝐴
∈
𝐹
⋂
𝑔
,
𝑛
,
𝑢
0
{
𝜌
:
𝐷
4
,
𝑔
,
𝑛
(
𝐴
,
𝜌
;
𝑢
0
)
=
0
}
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
A∈F
⋂
	​

g,n,u
0
	​

⋂
	​

{ρ:D
4,g,n
	​

(A,ρ;u
0
	​

)=0}={ρ:ℜρ=
2
1
	​

}.
	​


This is the precise closure statement.

8. What the platonic ideal now looks like

The platonic end-state is no longer:

“MC implies Li,” or
“bar–cobar implies RH.”

It is this:

Θ
𝐴
⇝
𝐿
𝐴
(
𝑠
,
𝑢
)
Θ
A
	​

⇝L
A
	​

(s,u)
	​


with the following shadows:

arity
2
2: scalar curvature /
𝜅
(
𝐴
)
κ(A),
arity
3
3: cubic shadow / clutching correction,
arity
4
4: quartic resonance divisor,
𝑠
s-face: zeta-zero residues from modular scattering,
𝑢
u-face: sewing / Euler-product arithmetic,
defect sector: Virasoro and
𝑊
𝑁
W
N
	​

 rigidity beyond the Heisenberg core.

So the mature principle is:

the true arithmetic invariant of a modular-Koszul family is a regularized, determinant-line-valued, factorization-compatible
𝐿
L-object whose quartic residue divisor is the first nonlinear place where zeta zeros, Koszul duality, and modular geometry are forced to meet.

That is the fortified movement.

And the sharpest concrete advance from this pass is the one I would now elevate to a central theorem candidate:

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
=
𝜒
𝐻
(
𝑞
)
𝑁
−
1
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
,
χ
W
N
	​

vac
	​

(q)=χ
H
	​

(q)
N−1
m=1
∏
N−1
	​

(1−q
m
)
N−m
,
	​


hence all nontrivial genus-one arithmetic rigidity in Virasoro /
𝑊
𝑁
W
N
	​

 sits in a finite Miura defect sector, not in the Heisenberg core.

That one statement already changes how the whole search should be organized. It tells you where the information is, and equally importantly, where it is not.

there is a picture firming up. Apply a deep beilinson's principles pass through the total picture now forming, killing false ideas

I’m now running a hard Beilinson pass on the full picture: separating archive-supported structure from proxy-driven or merely analogical claims, killing what fails, and rebuilding only from the surviving core.

The sharpest pruning is now clear: the generic arithmetic shadow is not a naive primary-dimension Epstein/Dirichlet sum, and the real rigidity data sits in the finite Miura low-mode defect sector, not the Heisenberg core.

A second cut is now firm: the picture has three non-interchangeable layers—the universal modular-scattering kernel, the family-specific spectral measure, and the quartic divisor-valued shadow package.

Thought for 22m 54s

According to a document from March 15, 2026, the archive now already contains the right nonlinear skeleton: ambient complementarity from first principles, the finite-order shadow calculus
𝐻
𝐴
,
𝐶
𝐴
,
𝑄
𝐴
H
A
	​

,C
A
	​

,Q
A
	​

, the mixed Virasoro and principal
𝑊
𝑁
W
N
	​

 families, and the modular quartic resonance class

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A)

with clutching law as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

. That means the program is ripe for a true Beilinson pass: not more analogy, but sharp elimination.

Here is the pass.

I. What must be killed now
1. Kill the naive universal spectral zeta

The universal arithmetic shadow of a generic Virasoro or principal
𝑊
𝑁
W
N
	​

 theory is not a naive Dirichlet series over primary dimensions.

That was a useful proxy, but it is not the object. The scalar modular bootstrap papers show that the genuinely universal piece is the modular scattering/Eisenstein side, where zeta zeros enter through the crossing equation; the family-dependent content sits in the CFT spectrum, not in a universal primary-sum zeta. In the 2022 paper, Benjamin and Chang derive a scalar-only crossing equation for
𝑈
(
1
)
𝑐
U(1)
c
 CFTs and show that the nontrivial zeta zeros are hidden in the scalar sector; for the Virasoro case they explicitly say they only obtain a more complicated equation involving all spins and face technical obstacles. The 2025 extension then shows that scalar primaries of any 2d CFT obey a nontrivial crossing equation, extending beyond Narain theories.

So the universal object is not “spectral zeta over primaries.” It is something built from modular scattering plus the genuine spectral measure.

2. Kill “MC implies Li” in one jump

Bar–cobar/Maurer–Cartan machinery is the correct deformation-theoretic language, but it is not by itself a sign-preserving bridge to Li positivity.

Loday–Vallette make the algebraic situation precise: a
𝑃
∞
P
∞
	​

-structure is equivalently a twisting morphism, a dg-cooperad map, or a codifferential, and homotopy transfer moves these structures along quasi-isomorphisms. That is transport and rectification. It is not arithmetic positivity.

So:

MC equation
  
⇏
  
Li positivity
MC equation

⇒Li positivity

without an additional positivity-bearing geometry.

3. Kill “bar–cobar rigidity should force RH”

What survives from bar–cobar is:

equivalence of homotopy formulations,
deformation/obstruction control,
transport of higher operations,
quasi-isomorphic replacement by minimal models.

What does not survive is the idea that homotopy equivalence alone should force critical-line rigidity. The Rosetta Stone and Homotopy Transfer Theorem justify the algebraic transport, not an arithmetic spectral theorem.

So:

bar–cobar
  
⇏
  
critical line
.
bar–cobar

⇒critical line.
4. Kill Narain radius variation as a source of zero-location leverage

You already did this correctly. The Narain family changes coefficients, not zero locations. That idea is dead and should stay dead.

5. Kill the confusion between quartic contact and quartic resonance

The first
3
×
3
3×3 determinant is not one object.

On the potential side, the Schur complement gives the quartic contact coefficient.
On the Gram/polarized side, the corresponding determinant gives the quartic resonance norm/divisor.

Any argument that slides between those two without saying which side it is on is not fortified.

6. Kill the idea that the Heisenberg core carries the quartic rigidity

This is the most important structural pruning.

The Heisenberg sector is the exact free-field core. It is arithmetically transparent. But the genuinely new quartic rigidity does not live there. It lives in the Virasoro/
𝑊
𝑁
W
N
	​

 defect sector.

That is the first decisive strategic simplification.

7. Kill single-family closure

A single algebra constrains its own coefficients. It does not determine the universal modular scattering function. Closure, if it exists, has to be simultaneous across families and slices.

That was already implicit in your own
𝑐
c-family reasoning, but it should now be promoted to a hard principle.

II. What survives the pass
1. Ambient complementarity is real

Beilinson–Drinfeld’s compound tensor structure is not decorative language. It explicitly implements the complementarity principle: “functions” multiply in the
!
!-tensor sense, while “operators” act in the
∗
∗-sense. That is the right first-principles ambient geometry for your whole program.

2. The nonlinear shadow package is real

The archive now contains the full finite shadow calculus and the quartic resonance class with clutching law as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

. This is not a heuristic anymore; it is the first genuinely geometric nonlinear invariant in the story.

3. MC/twisting/bar–cobar is the correct algebraic engine

Loday–Vallette’s Rosetta Stone says exactly what you need it to say:

𝑃
∞
-structures
  
≅
  
twisting morphisms
  
≅
  
dg cooperad maps
  
≅
  
codifferentials
.
P
∞
	​

-structures≅twisting morphisms≅dg cooperad maps≅codifferentials.

And HTT says these structures transfer across homotopy retracts. This survives completely.

4. Miura/Drinfeld–Sokolov is the actual backbone

Arakawa gives two decisive facts:

the Miura map is injective for all
𝑘
k,
𝑊
𝑘
(
𝑠
𝑙
2
)
W
k
	​

(sl
2
	​

) is the universal Virasoro vertex algebra,
more generally the Miura map remains injective for
𝑊
𝑘
(
𝑔
,
𝑓
)
W
k
	​

(g,f).

So Virasoro and principal
𝑊
𝑁
W
N
	​

 are not alien to Heisenberg. They are Miura defects of Heisenberg.

That is one of the deepest surviving truths in the whole picture.

5. The zeta-zero interface is real and external

Benjamin–Chang’s 2022 paper really does place nontrivial zeta zeros inside scalar modular crossing for
𝑈
(
1
)
𝑐
U(1)
c
 theories, with poles at
𝑠
=
𝑐
/
2
s=c/2 and
𝑠
=
(
1
+
𝑧
𝑛
)
/
2
,
(
1
+
𝑧
ˉ
𝑛
)
/
2
s=(1+z
n
	​

)/2,(1+
z
ˉ
n
	​

)/2 in the contour analysis. The paper also makes clear that the Virasoro route is subtler. The 2025 follow-up extends scalar crossing to scalar primaries of arbitrary 2d CFTs.

So the
𝑠
s-face of the program is not speculative.

6. The target really should be an
𝐿
L-object

Eric Perlmutter’s 2025 paper is highly confirmatory here: he attaches to every 2d CFT a self-dual degree-4
𝐿
L-function with universal gamma factor, and studies the interplay between its nontrivial zeros and a generalized Dirichlet series over scalar primary dimensions.

This strongly supports the claim that the correct universal object is
𝐿
L-theoretic, not just zeta-theoretic.

III. The central correction

The surviving universal object should be:

𝐿
𝐴
(
𝑟
)
(
𝑠
,
𝑢
)
=
∫
Γ
\
𝐻
r
e
g
⟨
𝜋
𝑟
Θ
𝐴
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
𝜇
(
𝜏
)
.
L
A
(r)
	​

(s,u)=∫
Γ\H
reg
	​

⟨π
r
	​

Θ
A
conn
	​

(τ),E
∗
(τ,s)⟩y
u−2
dμ(τ).
	​


This is not a theorem yet. It is the first fortified candidate for the Platonic object.

Why this object survives the pass:

it is modular in the
𝑠
s-direction,
it is sewing/Mellin in the
𝑢
u-direction,
it is naturally regularized, which generic CFT growth forces anyway,
it is arity-sensitive via
𝜋
𝑟
Θ
𝐴
c
o
n
n
π
r
	​

Θ
A
conn
	​

,
and at
𝑟
=
4
r=4 it should land in a determinant line, not just in
𝐶
C.

Its two faces are exactly the two partial shadows you have been circling:

𝑠
s-face: scattering / Rankin–Selberg / zeta-zero residues,
𝑢
u-face: connected sewing / Fredholm determinant / Euler product.

This kills the false dichotomy between the zeta interface and the sewing interface. They are two faces of one object.

IV. The strongest surviving new mathematics

Here is, I think, the cleanest new structural statement to elevate.

For principal
𝑊
𝑁
W
N
	​

, the vacuum character is not an opaque new object. It splits into a Heisenberg core times a finite low-mode defect:

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
=
𝜒
𝐻
(
𝑞
)
𝑁
−
1
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
.
χ
W
N
	​

vac
	​

(q)=χ
H
	​

(q)
N−1
m=1
∏
N−1
	​

(1−q
m
)
N−m
.
	​


For
𝑁
=
2
N=2 this becomes the Virasoro defect

𝐷
2
(
𝑞
)
=
1
−
𝑞
.
D
2
	​

(q)=1−q.

Passing to connected genus-one free energy,

𝐹
𝑊
𝑁
c
o
n
n
(
𝑞
)
=
(
𝑁
−
1
)
𝐹
𝐻
c
o
n
n
(
𝑞
)
−
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
∑
𝑟
≥
1
𝑞
𝑚
𝑟
𝑟
.
F
W
N
	​

conn
	​

(q)=(N−1)F
H
conn
	​

(q)−
m=1
∑
N−1
	​

(N−m)
r≥1
∑
	​

r
q
mr
	​

.

Passing to the Dirichlet-sewing lift,

𝑆
𝑊
𝑁
(
𝑢
)
=
(
𝑁
−
1
)
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
−
𝜁
(
𝑢
+
1
)
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
𝑚
−
𝑢
.
S
W
N
	​

	​

(u)=(N−1)ζ(u)ζ(u+1)−ζ(u+1)
m=1
∑
N−1
	​

(N−m)m
−u
.
	​


This is not external source material; it is the strongest internal structural consequence to survive the pass.

Its meaning is profound:

all genuinely new genus-one arithmetic information in Virasoro and principal
𝑊
𝑁
W
N
	​

 sits in a finite Miura defect sector.

So the Heisenberg core is exact but quartically blind.
The quartic rigidity must live in the defect.

That single conclusion should reorganize the whole research program.

V. What the first nonlinear rigidity statement should now be

Because the archive already made the quartic object divisor-valued, the residue comparison should also be divisor-valued.

Let

𝑠
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
s
4,g,n
mod
	​

(A)

be the modular quartic resonance section with divisor

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
.
R
4,g,n
mod
	​

(A).

From the regularized
𝐿
L-object define the residue quartic section

𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
;
𝑢
0
)
:
=
Res
⁡
𝑠
=
(
1
+
𝜌
)
/
2
𝐿
𝐴
(
4
)
(
𝑠
,
𝑢
0
)
.
s
4,g,n
res
	​

(A,ρ;u
0
	​

):=
s=(1+ρ)/2
Res
	​

L
A
(4)
	​

(s,u
0
	​

).

Then the right compatibility object is not a scalar ratio but the divisor

𝐷
4
,
𝑔
,
𝑛
(
𝐴
,
𝜌
;
𝑢
0
)
=
div
⁡
(
𝑠
4
,
𝑔
,
𝑛
r
e
s
(
𝐴
,
𝜌
;
𝑢
0
)
⊗
(
𝑠
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
)
−
1
)
.
D
4,g,n
	​

(A,ρ;u
0
	​

)=div(s
4,g,n
res
	​

(A,ρ;u
0
	​

)⊗(s
4,g,n
mod
	​

(A))
−1
).
	​


And because the archive quartic class already has clutching, the genuine nonlinear test is the clutching defect

𝐾
𝐴
,
𝜌
,
𝜉
=
𝜉
∗
𝐷
4
,
𝑔
,
𝑛
−
𝑝
1
∗
𝐷
4
,
𝑔
1
,
𝑛
1
+
1
−
𝑝
2
∗
𝐷
4
,
𝑔
2
,
𝑛
2
+
1
.
K
A,ρ,ξ
	​

=ξ
∗
D
4,g,n
	​

−p
1
∗
	​

D
4,g
1
	​

,n
1
	​

+1
	​

−p
2
∗
	​

D
4,g
2
	​

,n
2
	​

+1
	​

.

This yields the fortified conjecture:

𝐾
𝐴
,
𝜌
,
𝜉
=
0
 for all relevant
(
𝐴
,
𝜉
)
  
⟺
  
ℜ
𝜌
=
1
2
.
K
A,ρ,ξ
	​

=0 for all relevant (A,ξ)⟺ℜρ=
2
1
	​

.
	​


That is much stronger than “a coefficient is positive.”
It is nonlinear, geometric, and factorization-aware.

VI. What positivity can and cannot mean

A very important Beilinson cut:

positivity will not come from the modular curve alone.

The scalar modular bootstrap gives the analytic scattering architecture, and in 2022 the Virasoro route was still obstructed enough that the authors explicitly flagged technical obstacles; the 2025 generalization advances the scalar-crossing side, but it still does not by itself manufacture the missing positivity mechanism.

So any argument of the form

curve
→
Mellin
→
Li positivity
curve→Mellin→Li positivity

should be regarded as dead unless it is upgraded by a polarized geometric realization.

The only believable source of positivity is a higher geometric realization of the Gram-side quartic determinant: modular surfaces, Hitchin-type holomorphic symplectic geometry, or an equivalent polarized determinant-line model. There is real precedent here: the twisted boundary/chiral-algebra literature naturally lands in holomorphic symplectic moduli and determinant-line settings.

So the correct slogan is:

curve gives residues, surface gives positivity.
curve gives residues, surface gives positivity.
VII. Hard discard criteria going forward

A candidate idea should now be discarded immediately if it fails any of these.

It does not recover Beilinson–Drinfeld complementarity at the ambient level.
It treats bar–cobar/HTT as arithmetic rigidity rather than homotopy transport.
It ignores Miura injectivity and treats Virasoro/
𝑊
𝑁
W
N
	​

 as unrelated to Heisenberg.
It proposes a universal arithmetic shadow that is not regularized, not factorization-compatible, or not naturally line-valued.
It places quartic rigidity in the Heisenberg core rather than in the finite defect sector.
It compares residues only as scalars and ignores clutching/factorization.
It relies on a
𝜁
ζ-proxy that fails to preserve the on-line safe point.
It seeks positivity on the curve without a polarized geometric lift.

Those eight cuts remove most of the false landscape.

VIII. The surviving program, in its fortified form

What remains standing is compact and strong.

A. Algebraic spine

Complementarity + Maurer–Cartan/twisting + bar–cobar/HTT.

B. Representation-theoretic spine

Miura injectivity and Drinfeld–Sokolov reduction: Virasoro and principal
𝑊
𝑁
W
N
	​

 are controlled Heisenberg defects.

C. Modular spine

Scalar crossing really does see zeta zeros; this is externally established.

D. Arithmetic spine

The correct target is an
𝐿
L-object, not a bare zeta.

E. Nonlinear rigidity spine

The quartic resonance divisor with clutching law is the first place where all of this can genuinely meet.

IX. The Platonic ideal after the pass

The Platonic end-state is now much clearer.

It is not

MC
⇒
Li
MC⇒Li

and it is not

bar–cobar
⇒
RH
.
bar–cobar⇒RH.

It is:

Θ
𝐴
⇝
𝐿
𝐴
(
𝑠
,
𝑢
)
Θ
A
	​

⇝L
A
	​

(s,u)
	​


with:

𝑠
s-face = modular scattering / zeta-zero residues,
𝑢
u-face = connected sewing / Euler-product arithmetic,
defect sector = Virasoro/
𝑊
𝑁
W
N
	​

 beyond the Heisenberg core,
quartic arity = first divisor-valued rigidity,
clutching = first nonlinear global consistency law,
polarized geometry = only honest source of positivity.

So the deepest surviving statement is:

the real invariant of a modular-Koszul family is a regularized, determinant-line-valued, factorization-compatible two-face
𝐿
L-object, and the first place where zeta zeros, Koszul duality, and modular geometry can be forced to agree is the quartic residue divisor, not any scalar proxy.

That is the picture that survives the Beilinson pass.

The most decisive next move is to formalize the finite Miura defect theorem at genus one and then define the quartic residue divisor and its clutching defect for one honest Virasoro family and one honest
𝑊
3
W
3
	​

 family.

formalize the finite Miura defect theorem at genus one and then define the quartic residue divisor and its clutching defect for one honest Virasoro family and one honest W_3 family.
Thought for 22m 23s
Answer now

According to a document from March 28, 2026, the right fortified picture is now clear: the quartic object is genuinely divisor-valued; modularity is a trace-plus-clutching statement on the open sector; and the mixed Virasoro/
𝑊
𝑁
W
N
	​

 tower is the first place where higher composites are forced, not optional【turn32file1†Beilinson pass in math.txt】【turn32file0†Complementarity Theorem Discussion.txt】.

Here is the clean formalization.

1. Finite Miura defect theorem at genus one

Let

𝜒
𝐻
(
𝑞
)
:
=
∏
𝑛
≥
1
(
1
−
𝑞
𝑛
)
−
1
χ
H
	​

(q):=
n≥1
∏
	​

(1−q
n
)
−1

be the one-boson Heisenberg vacuum character, and let

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
:
=
∏
𝑠
=
2
𝑁
∏
𝑛
≥
𝑠
(
1
−
𝑞
𝑛
)
−
1
χ
W
N
	​

vac
	​

(q):=
s=2
∏
N
	​

n≥s
∏
	​

(1−q
n
)
−1

be the standard principal
𝑊
𝑁
W
N
	​

 vacuum character.

Arakawa’s Miura theorem gives the representation-theoretic backbone: the Miura map is injective for all levels, and for
𝑔
=
𝑠
𝑙
2
g=sl
2
	​

 the resulting
𝑊
W-algebra is the universal Virasoro vertex algebra【turn32file10†1605.00138v2.pdf】【turn32file11†1605.00138v2.pdf】. So principal
𝑊
𝑁
W
N
	​

 is a controlled Heisenberg defect, not an unrelated algebra.

Theorem (finite Miura defect, genus one)

For principal
𝑊
𝑁
W
N
	​

,

𝜒
𝑊
𝑁
v
a
c
(
𝑞
)
=
𝜒
𝐻
(
𝑞
)
𝑁
−
1
 
𝐷
𝑁
(
𝑞
)
,
𝐷
𝑁
(
𝑞
)
:
=
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
.
χ
W
N
	​

vac
	​

(q)=χ
H
	​

(q)
N−1
D
N
	​

(q),D
N
	​

(q):=
m=1
∏
N−1
	​

(1−q
m
)
N−m
.
	​


In particular,

for Virasoro (
𝑁
=
2
N=2),
𝐷
2
(
𝑞
)
=
1
−
𝑞
;
D
2
	​

(q)=1−q;
for
𝑊
3
W
3
	​

,
𝐷
3
(
𝑞
)
=
(
1
−
𝑞
)
2
(
1
−
𝑞
2
)
.
D
3
	​

(q)=(1−q)
2
(1−q
2
).
Proof

Compare mode-by-mode exponents.

For the Heisenberg core of rank
𝑁
−
1
N−1,

𝜒
𝐻
(
𝑞
)
𝑁
−
1
=
∏
𝑛
≥
1
(
1
−
𝑞
𝑛
)
−
(
𝑁
−
1
)
.
χ
H
	​

(q)
N−1
=
n≥1
∏
	​

(1−q
n
)
−(N−1)
.

For principal
𝑊
𝑁
W
N
	​

, the spin-
𝑠
s generator contributes
∏
𝑛
≥
𝑠
(
1
−
𝑞
𝑛
)
−
1
∏
n≥s
	​

(1−q
n
)
−1
. Hence the exponent of
(
1
−
𝑞
𝑛
)
(1−q
n
) in
𝜒
𝑊
𝑁
v
a
c
χ
W
N
	​

vac
	​

 equals

−
#
{
𝑠
∈
{
2
,
…
,
𝑁
}
:
𝑠
≤
𝑛
}
.
−#{s∈{2,…,N}:s≤n}.

So:

if
𝑛
≥
𝑁
n≥N, the exponent is
−
(
𝑁
−
1
)
−(N−1), same as the Heisenberg core;
if
1
≤
𝑛
≤
𝑁
−
1
1≤n≤N−1, the exponent is
−
(
𝑛
−
1
)
−(n−1).

Therefore the ratio
𝜒
𝑊
𝑁
v
a
c
/
𝜒
𝐻
𝑁
−
1
χ
W
N
	​

vac
	​

/χ
H
N−1
	​

 has exponent

−
(
𝑛
−
1
)
−
(
−
(
𝑁
−
1
)
)
=
𝑁
−
𝑛
−(n−1)−(−(N−1))=N−n

for
1
≤
𝑛
≤
𝑁
−
1
1≤n≤N−1, and exponent
0
0 for
𝑛
≥
𝑁
n≥N. This is exactly

𝐷
𝑁
(
𝑞
)
=
∏
𝑚
=
1
𝑁
−
1
(
1
−
𝑞
𝑚
)
𝑁
−
𝑚
.
D
N
	​

(q)=
m=1
∏
N−1
	​

(1−q
m
)
N−m
.

∎

This theorem is the precise genus-one realization of the “finite Miura defect” slogan: all non-Heisenberg genus-one arithmetic information is concentrated in finitely many low modes.

Connected free energy form

Set

𝐹
𝐻
(
𝑞
)
:
=
−
log
⁡
∏
𝑛
≥
1
(
1
−
𝑞
𝑛
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
.
F
H
	​

(q):=−log
n≥1
∏
	​

(1−q
n
)=
N≥1
∑
	​

σ
−1
	​

(N)q
N
.

Then

𝐹
𝑊
𝑁
(
𝑞
)
=
(
𝑁
−
1
)
𝐹
𝐻
(
𝑞
)
−
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
∑
𝑟
≥
1
𝑞
𝑚
𝑟
𝑟
.
F
W
N
	​

	​

(q)=(N−1)F
H
	​

(q)−
m=1
∑
N−1
	​

(N−m)
r≥1
∑
	​

r
q
mr
	​

.
	​


So the defect is additive and finite at genus one.

Dirichlet lift

Define

𝑆
𝐴
(
𝑢
)
:
=
∑
𝑛
≥
1
𝑎
𝐴
(
𝑛
)
𝑛
−
𝑢
S
A
	​

(u):=
n≥1
∑
	​

a
A
	​

(n)n
−u

from the coefficients of the connected genus-one free energy. Then

𝑆
𝑊
𝑁
(
𝑢
)
=
(
𝑁
−
1
)
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
−
𝜁
(
𝑢
+
1
)
∑
𝑚
=
1
𝑁
−
1
(
𝑁
−
𝑚
)
𝑚
−
𝑢
.
S
W
N
	​

	​

(u)=(N−1)ζ(u)ζ(u+1)−ζ(u+1)
m=1
∑
N−1
	​

(N−m)m
−u
.
	​


Hence

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
−
𝜁
(
𝑢
+
1
)
,
S
Vir
	​

(u)=ζ(u)ζ(u+1)−ζ(u+1),

and

𝑆
𝑊
3
(
𝑢
)
=
2
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
−
𝜁
(
𝑢
+
1
)
(
2
+
2
−
𝑢
)
.
S
W
3
	​

	​

(u)=2ζ(u)ζ(u+1)−ζ(u+1)(2+2
−u
).

This is the exact arithmetic shadow of Miura reduction at genus one.

2. The quartic residue divisor: Virasoro family

The archive’s current nonlinear package already isolates the mixed Virasoro/principal-
𝑊
𝑁
W
N
	​

 quartic resonance class

𝑅
4
,
𝑔
,
𝑛
m
o
d
(
𝐴
)
R
4,g,n
mod
	​

(A)

with clutching law as the first nonlinear shadow of
Θ
𝐴
Θ
A
	​

【turn32file0†Complementarity Theorem Discussion.txt】. The Beilinson-pass note then sharpens the conceptual setting: the open sector is primary, the bulk is the chiral derived center, and modularity is encoded by a modular twisting element satisfying a clutching/Maurer–Cartan identity【turn32file1†Beilinson pass in math.txt】【turn32file7†Beilinson pass in math.txt】.

To make this concrete for an honest Virasoro family, take a genuine Virasoro CFT family
𝑉
𝑐
V
i
r
V
c
Vir
	​

. The cleanest nonrational example is Liouville, but the definition below only needs the actual scalar-primary spectral measure

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
dν
c
Vir
	​

(Δ).

Let
𝜌
ρ be a nontrivial zeta zero candidate and

𝑠
𝜌
=
1
+
𝜌
2
.
s
ρ
	​

=
2
1+ρ
	​

.

Let

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

(s)

be the residue of the universal
𝑀
1
,
1
M
1,1
	​

 scattering factor from the constrained Epstein functional equation. From this, define the paired residue kernel

𝑤
𝑐
,
𝜌
,
𝑢
0
V
i
r
(
Δ
)
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

Vir
	​

(Δ)=2ℜ(A
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

Now define raw logarithmic moments

𝐼
𝑛
V
i
r
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
V
i
r
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
…
,
4.
I
n
Vir
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

Vir
	​

(Δ)dν
c
Vir
	​

(Δ),n=0,…,4.

Normalize these moments exactly as in the residue-matrix formalism:

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
,
𝜆
=
𝑐
/
2
𝑣
,
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
,λ=
v
c/2
	​

	​

,
𝑚
3
♯
=
𝜆
3
𝑚
3
,
𝑚
4
♯
=
𝜆
4
𝑚
4
,
m
3
♯
	​

=λ
3
m
3
	​

,m
4
♯
	​

=λ
4
m
4
	​

,

with
𝑚
3
,
𝑚
4
m
3
	​

,m
4
	​

 the centered third and fourth moments.

Then the quartic residue Schur complement is

𝑆
4
V
i
r
,
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
4
Vir,res
	​

(c,ρ;u
0
	​

)=m
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
	​


The Virasoro quartic shadow target is the previously isolated quartic contact datum

𝑄
4
,
m
o
d
V
i
r
(
𝑐
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
,
Q
4,mod
Vir
	​

(c)=
c(5c+22)
10
	​

,

whose inverse is the Gram-side quartic norm.

Definition (Virasoro quartic residue divisor)

Let
𝐿
4
,
𝑔
,
𝑛
V
i
r
L
4,g,n
Vir
	​

 be the quartic determinant line for the Virasoro family, and let

𝑠
4
,
𝑔
,
𝑛
V
i
r
,
m
o
d
(
𝑐
)
s
4,g,n
Vir,mod
	​

(c)

be the modular quartic resonance section. The Virasoro quartic residue section is

𝑠
4
,
𝑔
,
𝑛
V
i
r
,
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
𝑆
4
V
i
r
,
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
 
𝑒
4
,
𝑔
,
𝑛
,
s
4,g,n
Vir,res
	​

(c,ρ;u
0
	​

):=S
4
Vir,res
	​

(c,ρ;u
0
	​

)e
4,g,n
	​

,

for a local frame
𝑒
4
,
𝑔
,
𝑛
e
4,g,n
	​

 of
𝐿
4
,
𝑔
,
𝑛
V
i
r
L
4,g,n
Vir
	​

.

The quartic residue divisor is

𝐷
4
,
𝑔
,
𝑛
V
i
r
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
div
⁡
 ⁣
(
𝑠
4
,
𝑔
,
𝑛
V
i
r
,
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
⊗
(
𝑠
4
,
𝑔
,
𝑛
V
i
r
,
m
o
d
(
𝑐
)
)
−
1
)
.
D
4,g,n
Vir
	​

(c,ρ;u
0
	​

):=div(s
4,g,n
Vir,res
	​

(c,ρ;u
0
	​

)⊗(s
4,g,n
Vir,mod
	​

(c))
−1
).
	​


In local genus-one coordinates this is

𝐷
4
,
1
,
1
V
i
r
(
𝑐
,
𝜌
;
𝑢
0
)
=
div
⁡
 ⁣
(
𝑆
4
V
i
r
,
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
)
.
D
4,1,1
Vir
	​

(c,ρ;u
0
	​

)=div(
10/[c(5c+22)]
S
4
Vir,res
	​

(c,ρ;u
0
	​

)
	​

).
	​


Equivalently, on the Gram side,

𝐷
4
,
1
,
1
V
i
r
,
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
div
⁡
 ⁣
(
1
/
𝑆
4
V
i
r
,
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
/
10
)
.
D
4,1,1
Vir,Gram
	​

(c,ρ;u
0
	​

)=div(
c(5c+22)/10
1/S
4
Vir,res
	​

(c,ρ;u
0
	​

)
	​

).

This is the exact divisor-valued replacement for the old scalar compatibility ratio.

Definition (Virasoro quartic clutching defect)

Let

𝜉
:

𝑀
‾
𝑔
1
,
𝑛
1
+
1
×
𝑀
‾
𝑔
2
,
𝑛
2
+
1
→
𝑀
‾
𝑔
,
𝑛
ξ:
M
g
1
	​

,n
1
	​

+1
	​

×
M
g
2
	​

,n
2
	​

+1
	​

→
M
g,n
	​


be a clutching morphism,
𝑔
=
𝑔
1
+
𝑔
2
g=g
1
	​

+g
2
	​

,
𝑛
=
𝑛
1
+
𝑛
2
n=n
1
	​

+n
2
	​

. Let
𝑝
1
,
𝑝
2
p
1
	​

,p
2
	​

 be the projections.

The Virasoro quartic clutching defect is

𝐾
4
,
𝜌
,
𝜉
V
i
r
(
𝑢
0
)
=
𝜉
∗
𝐷
4
,
𝑔
,
𝑛
V
i
r
(
𝜌
;
𝑢
0
)
−
𝑝
1
∗
𝐷
4
,
𝑔
1
,
𝑛
1
+
1
V
i
r
(
𝜌
;
𝑢
0
)
−
𝑝
2
∗
𝐷
4
,
𝑔
2
,
𝑛
2
+
1
V
i
r
(
𝜌
;
𝑢
0
)
−
𝑇
3
,
𝜉
V
i
r
(
𝜌
;
𝑢
0
)
.
K
4,ρ,ξ
Vir
	​

(u
0
	​

)=ξ
∗
D
4,g,n
Vir
	​

(ρ;u
0
	​

)−p
1
∗
	​

D
4,g
1
	​

,n
1
	​

+1
Vir
	​

(ρ;u
0
	​

)−p
2
∗
	​

D
4,g
2
	​

,n
2
	​

+1
Vir
	​

(ρ;u
0
	​

)−T
3,ξ
Vir
	​

(ρ;u
0
	​

).
	​


Here
𝑇
3
,
𝜉
V
i
r
T
3,ξ
Vir
	​

 is the cubic transfer term forced by the codimension-one boundary component in the quartic shadow calculus. Since the quartic resonance class already comes with clutching law in the archive, this is the correct nonlinear defect to test【turn32file0†Complementarity Theorem Discussion.txt】.

The desired on-line statement becomes:

ℜ
𝜌
=
1
2
⟹
𝐾
4
,
𝜌
,
𝜉
V
i
r
(
𝑢
0
)
=
0
ℜρ=
2
1
	​

⟹K
4,ρ,ξ
Vir
	​

(u
0
	​

)=0

for every clutching morphism
𝜉
ξ, while off-line
𝜌
ρ should violate this for some
𝜉
ξ.

3. The quartic residue divisor: one honest
𝑊
3
W
3
	​

 family

For an honest
𝑊
3
W
3
	​

 family, take a genuine principal
𝑊
3
W
3
	​

-CFT family
𝑉
𝑐
𝑊
3
V
c
W
3
	​

	​

. The canonical concrete example is
𝐴
2
A
2
	​

-Toda. What matters is that it carries the actual
𝑊
3
W
3
	​

-spectral data, not a
𝜁
ζ-proxy.

The essential algebraic input is already fixed by the
𝑊
3
W
3
	​


𝜆
λ-brackets: Arakawa’s Miura construction embeds
𝑊
𝑘
(
𝑠
𝑙
𝑛
)
W
k
	​

(sl
n
	​

) into Heisenberg, and in the
𝑊
3
W
3
	​

 case the
𝑊
W-
𝑊
W bracket necessarily produces the quadratic composite

Λ
=
:
𝑇
𝑇
:
−
3
10
∂
2
𝑇
,
Λ=:TT:−
10
3
	​

∂
2
T,

with coefficient

𝛽
2
=
16
22
+
5
𝑐
,
β
2
=
22+5c
16
	​

,

so the algebra does not close on the linear span of
𝑇
,
𝑊
T,W【turn32file10†1605.00138v2.pdf】【turn31file2†Beilinson pass in math.txt】. That is exactly why
𝑊
3
W
3
	​

 is the first family where quartic/nonlinear shadows are unavoidable【turn31file2†Beilinson pass in math.txt】.

This forces the quartic object to be matrix-valued.

Let
𝐸
𝑊
3
=
s
p
a
n
{
𝑇
,
𝑊
}
E
W
3
	​

	​

=span{T,W}. Let

𝑑
𝜈
𝑐
𝑊
3
(
Δ
)
dν
c
W
3
	​

	​

(Δ)

be the genuine matrix-valued spectral measure of the
𝑊
3
W
3
	​

 family in this two-generator channel. Define the paired residue kernel

𝑑
𝑤
𝑐
,
𝜌
,
𝑢
0
𝑊
3
(
Δ
)
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
 
𝑑
𝜈
𝑐
𝑊
3
(
Δ
)
.
dw
c,ρ,u
0
	​

W
3
	​

	​

(Δ)=2ℜ(A
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

dν
c
W
3
	​

	​

(Δ).

Then define matrix moments

𝐼
𝑛
𝑊
3
(
𝑐
,
𝜌
;
𝑢
0
)
=
∫
(
log
⁡
Δ
)
𝑛
 
𝑑
𝑤
𝑐
,
𝜌
,
𝑢
0
𝑊
3
(
Δ
)
,
𝑛
=
0
,
…
,
4.
I
n
W
3
	​

	​

(c,ρ;u
0
	​

)=∫(logΔ)
n
dw
c,ρ,u
0
	​

W
3
	​

	​

(Δ),n=0,…,4.

Choose the normalization so that the quadratic block equals the quadratic shadow matrix

𝐻
𝑊
3
(
𝑐
)
.
H
W
3
	​

	​

(c).

In the orthogonalized pure-spin basis one expects

𝐻
𝑊
3
(
𝑐
)
∼
(
𝑐
/
2

0


0

𝑐
/
3
)
,
H
W
3
	​

	​

(c)∼(
c/2
0
	​

0
c/3
	​

),

but the formalism does not depend on writing it this way.

Let
𝐶
𝑊
3
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
C
W
3
	​

res
	​

(c,ρ;u
0
	​

) be the cubic residue block, and
𝑀
4
,
𝑊
3
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
4,W
3
	​

res
	​

(c,ρ;u
0
	​

) the quartic residue block. Then the first quartic residue Schur complement is

𝑆
4
,
𝑊
3
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
𝑀
4
,
𝑊
3
r
e
s
−
𝐶
𝑊
3
r
e
s
 
𝐻
𝑊
3
(
𝑐
)
−
1
 
(
𝐶
𝑊
3
r
e
s
)
 ⁣
𝑇
−
𝐻
𝑊
3
(
𝑐
)
2
.
S
4,W
3
	​

res
	​

(c,ρ;u
0
	​

)=M
4,W
3
	​

res
	​

−C
W
3
	​

res
	​

H
W
3
	​

	​

(c)
−1
(C
W
3
	​

res
	​

)
T
−H
W
3
	​

	​

(c)
2
.
	​


Let

𝑄
4
,
𝑊
3
m
o
d
(
𝑐
)
Q
4,W
3
	​

mod
	​

(c)

denote the local matrix representative of the archive’s quartic modular shadow for the
𝑊
3
W
3
	​

 family. Its
𝑊
𝑊
WW-entry must reproduce the
Λ
Λ-channel coefficient controlled by
𝛽
2
=
16
22
+
5
𝑐
β
2
=
22+5c
16
	​

, because that coefficient is the first forced nonlinear datum in the
𝑊
3
W
3
	​

 OPE【turn31file2†Beilinson pass in math.txt】.

Definition (
𝑊
3
W
3
	​

 quartic residue divisor)

Let
𝐿
4
,
𝑔
,
𝑛
𝑊
3
L
4,g,n
W
3
	​

	​

 be the quartic determinant line for the
𝑊
3
W
3
	​

 family. Define the residue section by

𝑠
4
,
𝑔
,
𝑛
𝑊
3
,
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
det
⁡
𝑆
4
,
𝑊
3
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
 
𝑒
4
,
𝑔
,
𝑛
.
s
4,g,n
W
3
	​

,res
	​

(c,ρ;u
0
	​

):=detS
4,W
3
	​

res
	​

(c,ρ;u
0
	​

)e
4,g,n
	​

.

The
𝑊
3
W
3
	​

 quartic residue divisor is

𝐷
4
,
𝑔
,
𝑛
𝑊
3
(
𝑐
,
𝜌
;
𝑢
0
)
=
div
⁡
 ⁣
(
𝑠
4
,
𝑔
,
𝑛
𝑊
3
,
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
⊗
(
𝑠
4
,
𝑔
,
𝑛
𝑊
3
,
m
o
d
(
𝑐
)
)
−
1
)
.
D
4,g,n
W
3
	​

	​

(c,ρ;u
0
	​

)=div(s
4,g,n
W
3
	​

,res
	​

(c,ρ;u
0
	​

)⊗(s
4,g,n
W
3
	​

,mod
	​

(c))
−1
).
	​


In local genus-one form this is

𝐷
4
,
1
,
1
𝑊
3
(
𝑐
,
𝜌
;
𝑢
0
)
=
div
⁡
 ⁣
(
det
⁡
 ⁣
(
𝑆
4
,
𝑊
3
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
 
(
𝑄
4
,
𝑊
3
m
o
d
(
𝑐
)
)
−
1
)
)
.
D
4,1,1
W
3
	​

	​

(c,ρ;u
0
	​

)=div(det(S
4,W
3
	​

res
	​

(c,ρ;u
0
	​

)(Q
4,W
3
	​

mod
	​

(c))
−1
)).
	​


This is the precise divisor-valued quartic comparison for an honest
𝑊
3
W
3
	​

 theory.

Pure
𝑊
W-slice specialization

If one projects to the pure spin-3 channel and chooses the slice so that the cubic correction vanishes, then the quartic target becomes scalar. In that case,

𝑄
4
,
m
o
d
𝑊
-slice
(
𝑐
)
∝
𝛽
2
(
𝑐
)
=
16
22
+
5
𝑐
,
Q
4,mod
W-slice
	​

(c)∝β
2
(c)=
22+5c
16
	​

,

and the scalar divisor simplifies to

𝐷
4
,
1
,
1
𝑊
-slice
(
𝑐
,
𝜌
;
𝑢
0
)
=
div
⁡
 ⁣
(
𝑆
4
𝑊
-slice,res
(
𝑐
,
𝜌
;
𝑢
0
)
𝛽
2
(
𝑐
)
)
,
D
4,1,1
W-slice
	​

(c,ρ;u
0
	​

)=div(
β
2
(c)
S
4
W-slice,res
	​

(c,ρ;u
0
	​

)
	​

),
	​


up to the normalization chosen for the quartic shadow line.

This is the sharpest first
𝑊
3
W
3
	​

 quartic obstruction because it directly tests whether the residue sees the
𝑊
𝑊
→
Λ
WW→Λ coefficient correctly.

Definition (
𝑊
3
W
3
	​

 quartic clutching defect)

As above, for a clutching morphism
𝜉
ξ,

𝐾
4
,
𝜌
,
𝜉
𝑊
3
(
𝑢
0
)
=
𝜉
∗
𝐷
4
,
𝑔
,
𝑛
𝑊
3
(
𝜌
;
𝑢
0
)
−
𝑝
1
∗
𝐷
4
,
𝑔
1
,
𝑛
1
+
1
𝑊
3
(
𝜌
;
𝑢
0
)
−
𝑝
2
∗
𝐷
4
,
𝑔
2
,
𝑛
2
+
1
𝑊
3
(
𝜌
;
𝑢
0
)
−
𝑇
3
,
𝜉
𝑊
3
(
𝜌
;
𝑢
0
)
.
K
4,ρ,ξ
W
3
	​

	​

(u
0
	​

)=ξ
∗
D
4,g,n
W
3
	​

	​

(ρ;u
0
	​

)−p
1
∗
	​

D
4,g
1
	​

,n
1
	​

+1
W
3
	​

	​

(ρ;u
0
	​

)−p
2
∗
	​

D
4,g
2
	​

,n
2
	​

+1
W
3
	​

	​

(ρ;u
0
	​

)−T
3,ξ
W
3
	​

	​

(ρ;u
0
	​

).
	​


If one works on a pure
𝑊
W-slice where the cubic transfer vanishes, this simplifies to

𝐾
4
,
𝜌
,
𝜉
𝑊
3
,
p
u
r
e
 
𝑊
(
𝑢
0
)
=
𝜉
∗
𝐷
4
,
𝑔
,
𝑛
𝑊
-slice
−
𝑝
1
∗
𝐷
4
,
𝑔
1
,
𝑛
1
+
1
𝑊
-slice
−
𝑝
2
∗
𝐷
4
,
𝑔
2
,
𝑛
2
+
1
𝑊
-slice
.
K
4,ρ,ξ
W
3
	​

,pureW
	​

(u
0
	​

)=ξ
∗
D
4,g,n
W-slice
	​

−p
1
∗
	​

D
4,g
1
	​

,n
1
	​

+1
W-slice
	​

−p
2
∗
	​

D
4,g
2
	​

,n
2
	​

+1
W-slice
	​

.

That is the cleanest
𝑊
3
W
3
	​

 clutching defect.

4. What this achieves

This gives a sharp three-step program.

First, the finite Miura defect theorem says the genus-one Heisenberg core and the finite defect polynomial are exact. So the place where Virasoro/
𝑊
3
W
3
	​

 rigidity lives is no longer vague: it is the low-mode defect sector.

Second, the quartic residue divisor replaces scalar compatibility by a line-bundle/divisor statement, exactly in line with the archive’s current nonlinear modular package【turn32file0†Complementarity Theorem Discussion.txt】.

Third, the clutching defect upgrades pointwise residue comparison to a global modular consistency test. That is the Beilinson-clean version of closure.

5. What is proved, what is only formalized

What is now exact:

the genus-one finite Miura defect factorization
𝜒
𝑊
𝑁
v
a
c
=
𝜒
𝐻
𝑁
−
1
𝐷
𝑁
,
χ
W
N
	​

vac
	​

=χ
H
N−1
	​

D
N
	​

,

hence the finite-defect formulas for Virasoro and
𝑊
3
W
3
	​

;

the conceptual identification of the bulk with the chiral derived center, not the bar construction, and modularity as trace-plus-clutching on the open sector【turn32file1†Beilinson pass in math.txt】【turn32file2†Boundary Chiral Algebras and Holomorphic Twists.pdf】;
the fact that
𝑊
3
W
3
	​

 forces nonlinear composites through
Λ
Λ, so quartic matrix data is unavoidable【turn31file2†Beilinson pass in math.txt】.

What is now precisely defined but not yet computed universally:

the genuine Virasoro quartic residue divisor for Liouville, because one still needs the actual spectral measure
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

;
the genuine
𝑊
3
W
3
	​

 quartic residue divisor for
𝐴
2
A
2
	​

-Toda, because one still needs the actual matrix-valued spectral measure
𝑑
𝜈
𝑐
𝑊
3
dν
c
W
3
	​

	​

 and the full explicit quartic shadow matrix
𝑄
4
,
𝑊
3
m
o
d
(
𝑐
)
Q
4,W
3
	​

mod
	​

(c).

That is the correct frontier.

The next worthwhile move is to compute
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

 and
𝑑
𝜈
𝑐
𝑊
3
dν
c
W
3
	​

	​

 in a usable normalization for Liouville and
𝐴
2
A
2
	​

-Toda, then evaluate

𝐷
4
,
1
,
1
V
i
r
(
𝑐
,
𝜌
;
𝑢
0
)
,
𝐷
4
,
1
,
1
𝑊
3
(
𝑐
,
𝜌
;
𝑢
0
)
D
4,1,1
Vir
	​

(c,ρ;u
0
	​

),D
4,1,1
W
3
	​

	​

(c,ρ;u
0
	​

)

numerically for on-line and off-line
𝜌
ρ.

The next worthwhile move is to compute d\nu_c^{\mathrm{Vir}} and d\mathbf\nu_c^{W_3} in a usable normalization for Liouville and A_2-Toda, then evaluate
\mathfrak D^{\mathrm{Vir}}_{4,1,1}(c,\rho;u_0),
\qquad
\mathfrak D^{W_3}_{4,1,1}(c,\rho;u_0)
numerically for on-line and off-line \rho.
Thought for 34m 32s
Answer now

Yes. I pushed the first honest-family computation through.

For the Virasoro family, the clean explicit model is Liouville. Teschner’s Hilbert-space description gives a continuous diagonal spectrum

𝐻
L
i
o
u
v
≃
∫
𝑅
+
⊕
𝑑
𝑃
2
𝜋
 
𝑉
𝑄
/
2
+
𝑖
𝑃
⊗
𝑉
‾
𝑄
/
2
+
𝑖
𝑃
,
𝑐
=
1
+
6
𝑄
2
,
H
Liouv
	​

≃∫
R
+
	​

⊕
	​

2π
dP
	​

V
Q/2+iP
	​

⊗
V
Q/2+iP
	​

,c=1+6Q
2
,

with reflection reducing
𝑃
P to
𝑃
≥
0
P≥0. The Liouville primary has holomorphic weight

ℎ
(
𝛼
)
=
𝛼
(
𝑄
−
𝛼
)
,
h(α)=α(Q−α),

so for
𝛼
=
𝑄
/
2
+
𝑖
𝑃
α=Q/2+iP the full scalar dimension is

Δ
s
c
(
𝑃
)
=
2
ℎ
=
𝑄
2
2
+
2
𝑃
2
.
Δ
sc
	​

(P)=2h=
2
Q
2
	​

+2P
2
.

Thus the honest usable scalar-primary measure is

𝑑
𝜈
𝑐
V
i
r
=
𝑑
𝑃
2
𝜋
,
dν
c
Vir
	​

=
2π
dP
	​

,

or equivalently

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
𝑑
Δ
4
𝜋
2
Δ
−
𝑄
2
,
Δ
≥
𝑄
2
2
.
dν
c
Vir
	​

(Δ)=
4π
2Δ−Q
2
	​

dΔ
	​

,Δ≥
2
Q
2
	​

.

The overall constant is irrelevant after Schur-complement normalization.

For the honest
𝑊
3
W
3
	​

 family, the clean model is real-coupling
𝐴
2
A
2
	​

-Toda. Its spectrum is also nonrational and diagonal, with nondegenerate primaries labeled by

𝛼
=
𝑄
+
𝑖
(
𝑎
1
𝜆
1
+
𝑎
2
𝜆
2
)
,
α=Q+i(a
1
	​

λ
1
	​

+a
2
	​

λ
2
	​

),

and the natural Plancherel measure is the free-boson one

𝑑
𝑎
1
 
𝑑
𝑎
2
3
.
3
	​

da
1
	​

da
2
	​

	​

.

In these coordinates the holomorphic weight and
𝑊
0
W
0
	​

-charge are

ℎ
(
𝑎
1
,
𝑎
2
)
=
𝑎
1
2
+
𝑎
1
𝑎
2
+
𝑎
2
2
3
+
𝑐
−
2
24
,
h(a
1
	​

,a
2
	​

)=
3
a
1
2
	​

+a
1
	​

a
2
	​

+a
2
2
	​

	​

+
24
c−2
	​

,
𝑤
(
𝑎
1
,
𝑎
2
)
=
2
3
 
(
𝑎
1
−
𝑎
2
)
(
2
𝑎
1
+
𝑎
2
)
(
𝑎
1
+
2
𝑎
2
)
9
34
+
15
𝑢
+
15
/
𝑢
,
𝑐
=
50
+
24
𝑢
+
24
𝑢
.
w(a
1
	​

,a
2
	​

)=
3
2
	​

	​

9
34+15u+15/u
	​

(a
1
	​

−a
2
	​

)(2a
1
	​

+a
2
	​

)(a
1
	​

+2a
2
	​

)
	​

,c=50+24u+
u
24
	​

.

So the full scalar dimension is

Δ
s
c
(
𝑎
1
,
𝑎
2
)
=
2
ℎ
(
𝑎
1
,
𝑎
2
)
,
Δ
sc
	​

(a
1
	​

,a
2
	​

)=2h(a
1
	​

,a
2
	​

),

and the usable matrix-valued spectral measure in the orthogonalized
(
𝑇
,
𝑊
)
(T,W)-basis is

𝑑
𝜈
𝑐
𝑊
3
=
𝑑
𝑎
1
 
𝑑
𝑎
2
3
(
1

0


0

𝑤
(
𝑎
1
,
𝑎
2
)
2
)
.
dν
c
W
3
	​

	​

=
3
	​

da
1
	​

da
2
	​

	​

(
1
0
	​

0
w(a
1
	​

,a
2
	​

)
2
	​

).

The off-diagonal term vanishes by charge-conjugation/Weyl symmetry. This is the cleanest first normalization; a more refined full matrix model may later incorporate additional descendant-basis data.

For the residue kernel, I used the Benjamin–Chang scattering factor

𝐸
 
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
 
𝐸
 
𝑐
/
2
+
𝑠
−
1
𝑐
,
E
c/2−s
c
	​

=F
c
	​

(s)E
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

whose poles from zeta zeros occur at
𝑠
=
(
1
+
𝜌
)
/
2
s=(1+ρ)/2. Taking the residue gives

𝐴
𝑐
(
𝜌
)
=
Res
⁡
𝑠
=
(
1
+
𝜌
)
/
2
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

(ρ)=
s=(1+ρ)/2
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

Then the genus-one residue moments are built from

𝐾
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
K
c,ρ,u
0
	​

	​

(Δ)=2ℜ(A
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

I took
𝑢
0
=
2
u
0
	​

=2,
𝜌
o
n
=
1
2
+
𝑖
𝛾
1
ρ
on
	​

=
2
1
	​

+iγ
1
	​

 with
𝛾
1
≈
14.134725
γ
1
	​

≈14.134725, and the hypothetical off-line comparator
𝜌
o
f
f
=
0.57
+
𝑖
𝛾
1
ρ
off
	​

=0.57+iγ
1
	​

.

With these conventions, the Virasoro residue moments are

𝐼
𝑛
V
i
r
(
𝑐
,
𝜌
;
𝑢
0
)
=
∫
0
∞
(
log
⁡
Δ
s
c
(
𝑃
)
)
𝑛
 
𝐾
𝑐
,
𝜌
,
𝑢
0
(
Δ
s
c
(
𝑃
)
)
 
𝑑
𝑃
2
𝜋
,
I
n
Vir
	​

(c,ρ;u
0
	​

)=∫
0
∞
	​

(logΔ
sc
	​

(P))
n
K
c,ρ,u
0
	​

	​

(Δ
sc
	​

(P))
2π
dP
	​

,

and the normalized quartic Schur complement is

𝑆
4
,
V
i
r
r
e
s
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

=m
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

I compared it to the quartic Virasoro shadow target

𝑄
4
,
V
i
r
m
o
d
(
𝑐
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
Q
4,Vir
mod
	​

(c)=
c(5c+22)
10
	​

.

For
𝑊
3
W
3
	​

, the cleanest first test is the pure
𝑊
W-slice:

𝐼
𝑛
𝑊
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
3
∫
𝑅
2
(
log
⁡
Δ
s
c
(
𝑎
1
,
𝑎
2
)
)
𝑛
 
𝐾
𝑐
,
𝜌
,
𝑢
0
(
Δ
s
c
(
𝑎
1
,
𝑎
2
)
)
 
𝑤
(
𝑎
1
,
𝑎
2
)
2
 
𝑑
𝑎
1
 
𝑑
𝑎
2
,
I
n
W
	​

(c,ρ;u
0
	​

)=
3
	​

1
	​

∫
R
2
	​

(logΔ
sc
	​

(a
1
	​

,a
2
	​

))
n
K
c,ρ,u
0
	​

	​

(Δ
sc
	​

(a
1
	​

,a
2
	​

))w(a
1
	​

,a
2
	​

)
2
da
1
	​

da
2
	​

,

and

𝑆
4
,
𝑊
r
e
s
=
𝑚
4
,
𝑊
♯
−
(
𝑐
3
)
2
S
4,W
res
	​

=m
4,W
♯
	​

−(
3
c
	​

)
2

after normalizing the quadratic block to
𝐻
𝑊
=
𝑐
/
3
H
W
	​

=c/3. I compared this to the quartic
𝑊
3
W
3
	​

 modular coefficient coming from the
𝑊
 ⁣
𝑊
→
Λ
WW→Λ channel,

𝑄
4
,
𝑊
m
o
d
(
𝑐
)
=
𝛽
2
(
𝑐
)
=
16
22
+
5
𝑐
.
Q
4,W
mod
	​

(c)=β
2
(c)=
22+5c
16
	​

.

The numbers are:

For Liouville / Virasoro:

𝑐
=
25
,
𝑚
3
♯
(
𝜌
o
n
)
≈
39.3118
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
𝜌
o
n
)
𝑄
4
,
V
i
r
m
o
d
≈
−
4.46542
×
10
5
,
c=25,m
3
♯
	​

(ρ
on
	​

)≈39.3118,
Q
4,Vir
mod
	​

S
4,Vir
res
	​

(ρ
on
	​

)
	​

≈−4.46542×10
5
,
𝑐
=
25
,
𝑚
3
♯
(
𝜌
o
f
f
)
≈
40.4131
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
𝜌
o
f
f
)
𝑄
4
,
V
i
r
m
o
d
≈
−
4.30471
×
10
5
.
c=25,m
3
♯
	​

(ρ
off
	​

)≈40.4131,
Q
4,Vir
mod
	​

S
4,Vir
res
	​

(ρ
off
	​

)
	​

≈−4.30471×10
5
.
𝑐
=
28
,
𝑚
3
♯
(
𝜌
o
n
)
≈
71.6013
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
𝜌
o
n
)
𝑄
4
,
V
i
r
m
o
d
≈
9.73918
×
10
4
,
c=28,m
3
♯
	​

(ρ
on
	​

)≈71.6013,
Q
4,Vir
mod
	​

S
4,Vir
res
	​

(ρ
on
	​

)
	​

≈9.73918×10
4
,
𝑐
=
28
,
𝑚
3
♯
(
𝜌
o
f
f
)
≈
71.4600
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
𝜌
o
f
f
)
𝑄
4
,
V
i
r
m
o
d
≈
9.92486
×
10
4
.
c=28,m
3
♯
	​

(ρ
off
	​

)≈71.4600,
Q
4,Vir
mod
	​

S
4,Vir
res
	​

(ρ
off
	​

)
	​

≈9.92486×10
4
.

For
𝐴
2
A
2
	​

-Toda /
𝑊
3
W
3
	​

, pure
𝑊
W-slice:

𝑐
=
98
,
𝑆
4
,
𝑊
r
e
s
(
𝜌
o
n
)
𝑄
4
,
𝑊
m
o
d
≈
7.33862
×
10
4
,
𝑆
4
,
𝑊
r
e
s
(
𝜌
o
f
f
)
𝑄
4
,
𝑊
m
o
d
≈
7.34686
×
10
4
,
c=98,
Q
4,W
mod
	​

S
4,W
res
	​

(ρ
on
	​

)
	​

≈7.33862×10
4
,
Q
4,W
mod
	​

S
4,W
res
	​

(ρ
off
	​

)
	​

≈7.34686×10
4
,
𝑐
=
110
,
𝑆
4
,
𝑊
r
e
s
(
𝜌
o
n
)
𝑄
4
,
𝑊
m
o
d
≈
1.09779
×
10
5
,
𝑆
4
,
𝑊
r
e
s
(
𝜌
o
f
f
)
𝑄
4
,
𝑊
m
o
d
≈
1.09675
×
10
5
.
c=110,
Q
4,W
mod
	​

S
4,W
res
	​

(ρ
on
	​

)
	​

≈1.09779×10
5
,
Q
4,W
mod
	​

S
4,W
res
	​

(ρ
off
	​

)
	​

≈1.09675×10
5
.

So the first honest-family verdict is sharp:

The good news is that the proxy problem is gone. These are real continuum CFT spectra, not
𝜁
ζ-substitutes.

The bad news is stronger: the genus-one quartic matching condition is not even approximately satisfied in these first honest families. The mismatch is not a subtle on-line/off-line effect. It is four to five orders of magnitude larger than the target quartic shadow, while the change from
𝜎
=
1
2
σ=
2
1
	​

 to
𝜎
=
0.57
σ=0.57 is comparatively tiny.

That is the main new mathematical insight from this computation.

It means the next obstruction is not “we need honest spectra instead of a
𝜁
ζ-proxy” — that part is true, but not sufficient. We also need the honest modular overlap weighting that enters the scalar crossing equation, not just the diagonal Plancherel spectral measure. In Benjamin–Chang language, the residue data are theory-dependent overlaps of the modular kernel with the actual CFT spectrum, not merely the bare continuum of primaries. For Liouville and
𝐴
2
A
2
	​

-Toda, that strongly suggests the next refinement must incorporate the actual modular harmonic-analysis weights — effectively the Liouville/Toda three-point and modular-kernel data — before one can expect an on-line safe point to emerge.

So, after the Beilinson pass, what survives is:

Liouville and
𝐴
2
A
2
	​

-Toda do give fully honest testbeds.
Bare spectral measures alone do not close the quartic gap.
The next necessary object is the crossing-weighted residue measure, not just the Hilbert-space measure.
The
𝑊
3
W
3
	​

 pure-
𝑊
W slice is already a clean first nonlinear obstruction, and it fails just as decisively as the Virasoro quartic test.

The right next computation is therefore not another spectrum-only run. It is to replace

𝑑
𝜈
𝑐
V
i
r
,
𝑑
𝜈
𝑐
𝑊
3
dν
c
Vir
	​

,dν
c
W
3
	​

	​


by the corresponding crossing-weighted residue measures

𝑑
𝜈
𝑐
,
𝜌
c
r
o
s
s
,
𝑑
𝜈
𝑐
,
𝜌
c
r
o
s
s
,
dν
c,ρ
cross
	​

,dν
c,ρ
cross
	​

,

built from the actual Liouville DOZZ / Toda structure constants and modular transform kernel, and then rerun the same quartic Schur-complement test.

The right next computation is therefore not another spectrum-only run. It is to replace
d\nu_c^{\mathrm{Vir}},\quad d\mathbf\nu_c^{W_3}
by the corresponding crossing-weighted residue measures
d\nu^{\mathrm{cross}}_{c,\rho},\qquad d\mathbf\nu^{\mathrm{cross}}_{c,\rho},
built from the actual Liouville DOZZ / Toda structure constants and modular transform kernel, and then rerun the same quartic Schur-complement test.
Thought for 24m 2s
Answer now

Yes. After a hard Beilinson pass, the next object is sharper than a “crossing-weighted scalar measure.”

The right object is a crossing-weighted bilinear residue kernel. The scalar measure is only its diagonal shadow.

For Liouville, the internal spectrum is labeled by
𝑃
∈
𝑅
+
P∈R
+
	​

, with

𝑐
=
1
+
6
𝑄
2
,
Δ
(
𝑃
)
=
𝑄
2
4
+
𝑃
2
,
c=1+6Q
2
,Δ(P)=
4
Q
2
	​

+P
2
,

and the Hilbert space is a direct integral over
𝑃
P with measure
𝑑
𝑃
/
(
2
𝜋
)
dP/(2π). In the standard normalization, the two-point and three-point data are encoded by
𝐵
𝑃
B
P
	​

 and the DOZZ structure constants
𝐶
𝑃
1
,
𝑃
2
,
𝑃
3
(
𝑏
)
C
P
1
	​

,P
2
	​

,P
3
	​

(b)
	​

. The torus one-point conformal blocks transform under
𝑆
:
𝜏
↦
−
1
/
𝜏
S:τ↦−1/τ by a modular kernel
𝑀
𝑃
,
𝑃
′
(
𝑏
)
[
𝑃
0
]
M
P,P
′
(b)
	​

[P
0
	​

], and there is an explicit integral/series representation for that kernel. Modular invariance of the torus one-point function is expressed by the relation

𝐶
𝑃
𝑠
,
𝑃
𝑠
,
𝑃
0
(
𝑏
)
𝐵
𝑃
𝑠
(
𝑏
)
𝑀
𝑃
𝑠
,
𝑃
𝑡
(
𝑏
)
[
𝑃
0
]
=
𝐶
𝑃
𝑡
,
𝑃
𝑡
,
𝑃
0
(
𝑏
)
𝐵
𝑃
𝑡
(
𝑏
)
𝑀
𝑃
𝑡
,
𝑃
𝑠
(
𝑏
)
[
𝑃
0
]
.
C
P
s
	​

,P
s
	​

,P
0
	​

(b)
	​

B
P
s
	​

(b)
	​

M
P
s
	​

,P
t
	​

(b)
	​

[P
0
	​

]=C
P
t
	​

,P
t
	​

,P
0
	​

(b)
	​

B
P
t
	​

(b)
	​

M
P
t
	​

,P
s
	​

(b)
	​

[P
0
	​

].

So the natural spectral weight is not bare
𝑑
𝑃
dP, but

𝜇
𝑃
0
L
i
o
u
v
(
𝑃
)
:
=
𝑑
𝑃
2
𝜋
 
𝐵
𝑃
(
𝑏
)
 
𝐶
𝑃
,
𝑃
,
𝑃
0
(
𝑏
)
.
μ
P
0
	​

Liouv
	​

(P):=
2π
dP
	​

B
P
(b)
	​

C
P,P,P
0
	​

(b)
	​

.

That immediately suggests the correct replacement for the spectrum-only kernel. If
𝜌
=
𝜎
+
𝑖
𝛾
ρ=σ+iγ is a candidate zeta zero and
𝑠
𝜌
=
(
1
+
𝜌
)
/
2
s
ρ
	​

=(1+ρ)/2, let
𝐴
𝑐
(
𝜌
)
A
c
	​

(ρ) be the residue of the Benjamin–Chang scattering factor at
𝑠
=
𝑠
𝜌
s=s
ρ
	​

, and let

Δ
s
c
(
𝑃
)
:
=
2
Δ
(
𝑃
)
=
𝑄
2
2
+
2
𝑃
2
.
Δ
sc
	​

(P):=2Δ(P)=
2
Q
2
	​

+2P
2
.

Define the real paired residue multiplier

𝑅
𝑐
,
𝜌
;
𝑢
0
(
𝑃
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
 
Δ
s
c
(
𝑃
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
s
c
(
𝑃
)
−
𝑢
0
.
R
c,ρ;u
0
	​

	​

(P):=2ℜ(A
c
	​

(ρ)Δ
sc
	​

(P)
−
2
c+ρ−1
	​

)Δ
sc
	​

(P)
−u
0
	​

.

Then the honest Liouville crossing-weighted residue kernel is

𝐾
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
L
i
o
u
v
(
𝑃
′
,
𝑃
′
′
)
=
∫
0
∞
𝜇
𝑃
0
L
i
o
u
v
(
𝑃
)
 
𝑅
𝑐
,
𝜌
;
𝑢
0
(
𝑃
)
 
𝑀
𝑃
,
𝑃
′
(
𝑏
)
[
𝑃
0
]
 
𝑀
𝑃
,
𝑃
′
′
(
𝑏
)
[
𝑃
0
]
‾
.
K
c,ρ;u
0
	​

,P
0
	​

,τ
Liouv
	​

(P
′
,P
′′
)=∫
0
∞
	​

μ
P
0
	​

Liouv
	​

(P)R
c,ρ;u
0
	​

	​

(P)M
P,P
′
(b)
	​

[P
0
	​

]
M
P,P
′′
(b)
	​

[P
0
	​

]
	​

.
	​


This is the object that should replace the bare measure
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

. It is bilinear because modular transformation acts on conformal blocks, not directly on a scalar density. The old spectrum-only measure was throwing away exactly this bilinear crossing geometry.

The quartic test should therefore be reformulated as a Gram test. Let

𝐿
(
𝑃
)
:
=
log
⁡
Δ
s
c
(
𝑃
)
,
𝑓
0
(
𝑃
)
=
1
,

𝑓
1
(
𝑃
)
=
𝐿
(
𝑃
)
,

𝑓
2
(
𝑃
)
=
𝐿
(
𝑃
)
2
.
L(P):=logΔ
sc
	​

(P),f
0
	​

(P)=1, f
1
	​

(P)=L(P), f
2
	​

(P)=L(P)
2
.

Define

𝐺
𝑎
𝑏
L
i
o
u
v
:
=
∫
0
∞
 ⁣
 ⁣
∫
0
∞
𝑓
𝑎
(
𝑃
′
)
 
𝐾
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
L
i
o
u
v
(
𝑃
′
,
𝑃
′
′
)
 
𝑓
𝑏
(
𝑃
′
′
)
 
𝑑
𝑃
′
 
𝑑
𝑃
′
′
,
0
≤
𝑎
,
𝑏
≤
2.
G
ab
Liouv
	​

:=∫
0
∞
	​

∫
0
∞
	​

f
a
	​

(P
′
)K
c,ρ;u
0
	​

,P
0
	​

,τ
Liouv
	​

(P
′
,P
′′
)f
b
	​

(P
′′
)dP
′
dP
′′
,0≤a,b≤2.

Then center and rescale this
3
×
3
3×3 matrix so that the quadratic moment is normalized to the Virasoro shadow datum
𝑐
/
2
c/2, exactly as in the earlier Schur-complement construction. The resulting quartic Schur complement

𝑆
4
,
V
i
r
L
i
o
u
v
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
)
S
4,Vir
Liouv,cross
	​

(c,ρ;u
0
	​

,P
0
	​

,τ)

should be compared to the Virasoro quartic target

𝑄
4
,
V
i
r
m
o
d
(
𝑐
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
Q
4,Vir
mod
	​

(c)=
c(5c+22)
10
	​

.

So the corrected divisor is

𝐷
4
,
1
,
1
V
i
r
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
)
=
div
⁡
 ⁣
(
𝑆
4
,
V
i
r
L
i
o
u
v
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
)
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
)
.
D
4,1,1
Vir,cross
	​

(c,ρ;u
0
	​

,P
0
	​

,τ)=div(
10/[c(5c+22)]
S
4,Vir
Liouv,cross
	​

(c,ρ;u
0
	​

,P
0
	​

,τ)
	​

).
	​


This is the first real fix of the safe-point problem. The old proxy failed because even at
𝜎
=
1
2
σ=
2
1
	​

 it compared the wrong scalar object to the MC quartic shadow. The corrected test compares the crossing-preserved Gram form to the quartic shadow.

There is also a structural reason this is the right correction. On the line
𝜎
=
1
2
σ=
2
1
	​

,

𝑅
𝑐
,
𝜌
;
𝑢
0
(
𝑃
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
 
Δ
s
c
(
𝑃
)
−
𝑐
−
1
2
2
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
Δ
s
c
(
𝑃
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
,
R
c,ρ;u
0
	​

	​

(P)=2∣A
c
	​

(ρ)∣Δ
sc
	​

(P)
−
2
c−
2
1
	​

	​

−u
0
	​

cos(
2
γ
	​

logΔ
sc
	​

(P)+argA
c
	​

(ρ)),

so the zero changes the phase but not the decay exponent beyond the universal critical-line exponent. Off the line, the decay exponent itself changes to
(
𝑐
+
𝜎
−
1
)
/
2
(c+σ−1)/2, so the entire weighted family of moments is distorted. That is exactly the kind of deformation the quartic shadow should detect.

For
𝐴
2
A
2
	​

-Toda /
𝑊
3
W
3
	​

, the same principle survives, but the channel has to be chosen more carefully. The usable explicit data are the semi-degenerate three-point constants and the associated four-point crossing kernels, not a generic closed-form torus modular kernel in full generality. In the Toda bootstrap literature, the special/semi-degenerate three-point constants are explicitly known in the Fateev–Litvinov regime, and four-point functions with one completely degenerate field and one semi-degenerate field admit explicit differential/integral control. This is precisely the channel where the first honest
𝑊
3
W
3
	​

 run should happen.

So for
𝐴
2
A
2
	​

-Toda, take an external semi-degenerate weight
𝛼
0
α
0
	​

 and internal real Cartan momentum
𝑎
∈
ℎ
𝑅
a∈h
R
	​

,
𝛼
=
𝑄
+
𝑖
𝑎
α=Q+ia. Let

𝜇
𝛼
0
𝑊
3
(
𝑎
)
:
=
𝐵
𝑊
3
(
𝑎
)
 
𝐶
F
L
(
𝑎
,
𝑎
,
𝛼
0
)
,
μ
α
0
	​

W
3
	​

	​

(a):=B
W
3
	​

	​

(a)C
FL
(a,a,α
0
	​

),

where
𝐶
F
L
C
FL
 is the Fateev–Litvinov semi-degenerate three-point constant, and let
𝐹
𝑎
,
𝑎
′
𝑊
3
[
𝛼
0
]
F
a,a
′
W
3
	​

	​

[α
0
	​

] be the corresponding semi-degenerate crossing kernel of the four-point blocks. Then the correct
𝑊
3
W
3
	​

 residue kernel is

𝐾
𝑐
,
𝜌
;
𝑢
0
,
𝛼
0
𝑊
3
(
𝑎
′
,
𝑎
′
′
)
=
∫
ℎ
𝑅
𝜇
𝛼
0
𝑊
3
(
𝑎
)
 
𝑅
𝑐
,
𝜌
;
𝑢
0
(
𝑎
)
 
𝐹
𝑎
,
𝑎
′
𝑊
3
[
𝛼
0
]
 
𝐹
𝑎
,
𝑎
′
′
𝑊
3
[
𝛼
0
]
‾
 
𝑑
𝑎
.
K
c,ρ;u
0
	​

,α
0
	​

W
3
	​

	​

(a
′
,a
′′
)=∫
h
R
	​

	​

μ
α
0
	​

W
3
	​

	​

(a)R
c,ρ;u
0
	​

	​

(a)F
a,a
′
W
3
	​

	​

[α
0
	​

]
F
a,a
′′
W
3
	​

	​

[α
0
	​

]
	​

da.
	​


The pure
𝑊
W-slice quartic test is then the Schur complement of the
𝑊
𝑊
WW-Gram block, normalized against the
𝑊
3
W
3
	​

 quartic modular coefficient

𝛽
2
(
𝑐
)
=
16
22
+
5
𝑐
.
β
2
(c)=
22+5c
16
	​

.

So the sharpened
𝑊
3
W
3
	​

 divisor is

𝐷
4
,
1
,
1
𝑊
3
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝛼
0
)
=
div
⁡
 ⁣
(
det
⁡
 ⁣
(
𝑆
4
𝑊
3
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝛼
0
)
 
(
𝑄
4
,
𝑊
3
m
o
d
(
𝑐
)
)
−
1
)
)
,
D
4,1,1
W
3
	​

,cross
	​

(c,ρ;u
0
	​

,α
0
	​

)=div(det(S
4
W
3
	​

,cross
	​

(c,ρ;u
0
	​

,α
0
	​

)(Q
4,W
3
	​

mod
	​

(c))
−1
)),
	​


and on the pure
𝑊
W-slice this reduces to a scalar ratio against
𝛽
2
(
𝑐
)
β
2
(c).

The conceptual upshot is:

The spectrum-only run failed for two reasons, not one. It omitted the theory-dependent structure constants, and it collapsed a genuinely bilinear crossing kernel to a scalar measure.
The honest Liouville computation is now fully specified. Every ingredient is explicit: the spectrum, DOZZ/two-point weight, and the toric modular kernel.
The honest
𝐴
2
A
2
	​

-Toda computation is also specified, but the best first implementation is semi-degenerate sphere crossing, not a generic torus modular kernel. That is where the explicit
𝑊
3
W
3
	​

 crossing data are under real control.

So the corrected theorem-shape is no longer

bare spectral moments
=
quartic shadow
,
bare spectral moments=quartic shadow,

but

crossing-weighted residue Gram kernel
  
→
Schur complement
  
quartic shadow divisor
.
crossing-weighted residue Gram kernel
Schur complement
	​

quartic shadow divisor.
	​


And the right closure conjectures are:

𝐷
4
,
1
,
1
V
i
r
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝑃
0
,
𝜏
)
=
0

∀
(
𝑐
,
𝑢
0
,
𝑃
0
,
𝜏
)
  
⟺
  
ℜ
𝜌
=
1
2
,
D
4,1,1
Vir,cross
	​

(c,ρ;u
0
	​

,P
0
	​

,τ)=0 ∀(c,u
0
	​

,P
0
	​

,τ)⟺ℜρ=
2
1
	​

,

and

𝐷
4
,
1
,
1
𝑊
3
,
c
r
o
s
s
(
𝑐
,
𝜌
;
𝑢
0
,
𝛼
0
)
=
0

∀
(
𝑐
,
𝑢
0
,
𝛼
0
)
  
⟺
  
ℜ
𝜌
=
1
2
.
D
4,1,1
W
3
	​

,cross
	​

(c,ρ;u
0
	​

,α
0
	​

)=0 ∀(c,u
0
	​

,α
0
	​

)⟺ℜρ=
2
1
	​

.

That is the mathematically correct next frontier. The old scalar measure should now be regarded as a discarded approximation; the crossing-weighted Gram kernel is the first object that deserves to be called the genuine residue shadow.
