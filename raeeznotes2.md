According to a document from March 2026, the latest iteration of the manuscript is no longer primarily threatened by the old theorem-killers. The complementarity theorem is now built from a Verdier involution with
±
1
±1-eigenspaces, not from a bad dimension count, and the manuscript now proves a Lagrangian refinement as well. At the same time, the author is now much more honest about what remains unbuilt: the full coderived/contraderived factorization formalism is still missing, and the full factorization-categorical Drinfeld–Kohno statement is still conjectural. So the current state is this: the theorematic spine is stronger, but the book still contains a serious formalism instability and a large amount of theorem/conjecture/status drift that has not yet been propagated backward through the chapters. latest manuscript PDF

main

The single deepest live problem is that the manuscript still uses one notation for at least two mathematically different objects. In Definition 8.17.10, the scalar invariant
𝜅
(
𝐴
)
κ(A) is said to control genus‑1 curvature via

𝑑
2
=
𝜅
(
𝐴
)
 
𝜔
1
⋅
i
d
,
d
2
=κ(A)ω
1
	​

⋅id,

so the higher-genus package is presented as genuinely curved. But Chapter 8.14 then defines a quantum-corrected differential

𝑑
𝑔
=
𝑑
0
+
∑
𝑘
𝑡
𝑘
𝑑
𝑘
d
g
	​

=d
0
	​

+
k
∑
	​

t
k
	​

d
k
	​


and proves
𝑑
𝑔
2
=
0
d
g
2
	​

=0. And Chapter 6 still states that for central anomalies one has
𝑑
b
a
r
2
=
0
d
bar
2
	​

=0 strictly at all genera for the standard examples. These can all be true only if the manuscript is working with distinct differentials — a genus-fixed curved differential, a total corrected differential, and the bar differential in the central-curvature regime — but the notation does not enforce that distinction. As long as the same symbol
𝑑
𝑔
d
g
	​

 or
𝑑
d is allowed to mean all three, the higher-genus formalism is unstable at its foundation.

The second deepest problem is that the source of the higher-genus parameters is still inconsistent inside the body of the book. Chapter 8.14 now explicitly says that for
𝑔
≥
2
g≥2, Harer kills
𝐻
1
(
𝑀
𝑔
,
𝑄
)
H
1
(M
g
	​

,Q), so the parameters
𝑡
𝑖
t
i
	​

 arise from
𝐻
1
(
Σ
𝑔
,
𝐶
)
H
1
(Σ
g
	​

,C), the cohomology of the curve, not the cohomology of moduli. But the same chapter still contains the requirement that “quantum corrections (from
𝐻
1
(
𝑀
𝑔
)
H
1
(M
g
	​

)) preserve acyclicity.” That is not a harmless slip. It changes the deformation problem itself: are the parameters periods of the fiber curve, or classes on the moduli stack? Those are categorically different objects, and they feed into different versions of the Kodaira–Spencer story. This contradiction has to be removed at the level of definitions, not patched by remarks.

The third major issue is rhetorical but mathematically consequential: the manuscript still speaks as if the full “modular characteristic package” were established, when in fact only its scalar shadow is. Definition 8.17.10 now defines the package as
(
𝜅
(
𝐴
)
,
{
𝐹
𝑔
(
𝐴
)
}
,
Δ
𝐴
,
Θ
𝐴
)
(κ(A),{F
g
	​

(A)},Δ
A
	​

,Θ
A
	​

), but it simultaneously says that the first three pieces are established and the fourth, the universal Maurer–Cartan class
Θ
𝐴
Θ
A
	​

, is conjectural in its non-scalar form. Chapter 34 is admirably clear about this: the existence of
Θ
𝐴
Θ
A
	​

 requires constructing
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
	​

(A) as a cyclic
𝐿
∞
L
∞
	​

-algebra and solving the Maurer–Cartan equation in a completed tensor product with tautological classes. So Theorem D should be stated as a theorem about the scalar modular characteristic system, not about the full modular package. At present the introduction overstates what has actually been proved.

With that in view, here is the updated critique chapter by chapter.

Chapters 1–2: the atomic exposition is strong, but the formal picture is not yet stable

Chapter 1 remains the best “seed chapter” in the manuscript. It correctly makes the Heisenberg algebra the atom from which the later structures become visible. But it is now dangerous as a foundation chapter because the whole later ambiguity about curvature versus strict nilpotence is already latent there and never definitively resolved. The introduction then amplifies this by presenting the modular characteristic package and the modular Koszul program as if the full object were already theorematic, even though Chapter 34 plainly says that the full coderived Ran-space formalism and the full universal Maurer–Cartan class remain future work. The fix is not cosmetic: Chapter 1 must introduce two differential notations from the start, and Chapter 2 must explicitly distinguish “proved scalar package” from “conjectural full non-scalar package.”

Chapters 3–5: the algebraic template is solid, but the book still blurs quadratic, curved, filtered, and general regimes

The manuscript already knows that the correct hierarchy is

Quadratic
⊂
Curved
⊂
Filtered
⊂
General
,
Quadratic⊂Curved⊂Filtered⊂General,

and it even says that the general case may have no Koszul dual at all. That is exactly the right taxonomy. The problem is that this taxonomy does not yet govern the theorem statements globally. Too many later claims still sound as though the quadratic/Koszul mechanism proved in full detail automatically extends to curved, filtered, or infinitely generated settings. The fix is structural: every theorem after Chapter 5 should carry a regime tag — quadratic, curved-central, filtered-complete, or programmatic — and examples should only be quoted under the regime in which the stated proof actually lives.

Chapter 6: this is where the live formal contradiction is manufactured

Chapter 6 proves “centrality implies strict nilpotence,” and then goes further: it states that for vertex-operator-algebra examples or theories with central anomalies, one has
𝑑
b
a
r
2
=
0
d
bar
2
	​

=0 strictly at all genera, explicitly including Heisenberg, Kac–Moody, Virasoro,
𝑊
W-algebras, and free-field systems. That is a mathematically meaningful theorem if the differential being discussed is the total corrected differential in a central-curvature setting. But elsewhere in the book,
𝑑
𝑔
2
d
g
2
	​

 is used precisely as the genus-
𝑔
g obstruction class. So Chapter 6 is not wrong in isolation; it is wrong as long as the manuscript fails to separate the curved genus-fixed differential from the strict total differential. The repair is simple in principle and unavoidable in practice:

𝑑
(
𝑔
)
c
u
r
v
,
𝐷
t
o
t
,
𝑚
0
(
𝑔
)
d
(g)
curv
	​

,D
tot
,m
0
(g)
	​


must become permanent notation, and every theorem in Chapters 6, 8, 18, 20, 21, 29, 30, and 34 must be rewritten with one of those three symbols, never “
𝑑
𝑔
d
g
	​

” generically.

Chapters 7–8: the complementarity theorem is repaired, but “standard examples are modular Koszul” is still too broad

This is the chapter pair where the manuscript has improved the most. Theorem 8.13.5 now really is repaired: the Verdier involution
𝜎
σ is defined, its eigenspaces are identified with
𝑄
𝑔
(
𝐴
)
Q
g
	​

(A) and
𝑄
𝑔
(
𝐴
!
)
Q
g
	​

(A!), and the direct sum decomposition follows from eigenspace splitting, not from numerical handwaving. Proposition 8.13.24 then proves that these eigenspaces are Lagrangian for the Verdier pairing. Chapter 34 strengthens the status accounting further by distinguishing the
−
(
3
𝑔
−
3
)
−(3g−3)-shifted symplectic structure on ambient cohomology from the
(
−
1
)
(−1)-shifted structure on formal moduli. All of that is real progress and should now replace all older formulations everywhere in the book.

But the same chapter also still overclaims. Definition 8.17.7 introduces modular Koszul chiral algebras with five axioms, and Proposition 8.17.9 then declares that Heisenberg, free fermion/
𝛽
𝛾
βγ-
𝑏
𝑐
bc, generic affine Kac–Moody, generic Virasoro, and generic
𝑊
𝑁
W
N
	​

 all satisfy them. The proof of MK4 for the generic non-free-field families is not a proof of actual genus-
𝑔
g collapse; it is a proof that the associated graded genus-
𝑔
g PBW page matches genus
0
0, followed by the phrase “hence at generic parameters where the spectral sequence degenerates.” But that degeneration is exactly the missing mathematical statement. So the proposition is currently too strong. The right fix is to split it in two:

a theorem: “if the genus-
𝑔
g PBW spectral sequence degenerates, then MK4 holds,” and

a conjecture: “generic Virasoro and generic
𝑊
𝑁
W
N
	​

 satisfy that degeneration.”

Chapter 8.14 specifically: the higher-genus extension chapter is the current pressure point

The manuscript now proves a quantum-corrected differential
𝑑
𝑔
d
g
	​

 with
𝑑
𝑔
2
=
0
d
g
2
	​

=0, and it proves that these quantum corrections preserve Chevalley–Cousin acyclicity. That is mathematically substantial. But the same section still contains both the wrong source for the correction parameters and the old moduli-cohomology language, while the proof of acyclicity relies on a filtration argument whose genus‑1 verification is described in terms of quasi-modular functions and whose general-genus step appeals to Torelli descent with very compressed justification. The repair here is not to delete the chapter — the chapter is important — but to make it explicitly a theorem about the Chevalley–Cousin total differential and to say out loud that this is not the same object as the genus-fixed curved bar differential used in the obstruction package. Without that sentence, the chapter keeps undoing the formal precision gained elsewhere.

Chapters 9–11: the periodicity package is still the weakest mathematical flank

The manuscript has improved here by becoming more honest. It now explicitly says that for general rational chiral algebras, the deduction of bar-cohomology periodicity from
𝑇
𝑁
=
i
d
T
N
=id is not valid:
𝑇
𝑁
=
i
d
T
N
=id is only a phase condition on characters, and one would also need eventual periodicity of fusion multiplicities and compatibility of the bar differential with the
𝑇
T-shift. It says this works for minimal models and is open in general. That is the correct state of affairs. But the chapter still continues to package periodicity as a single scalar invariant
P
e
r
i
o
d
(
𝐴
)
Period(A), and then builds a unified classification and a periodicity-exchange theorem on top of three sources — modular, quantum, and geometric — whose interaction is not canonically scalar at all.

The geometric part has also improved but is still not mature. In the current version, the weak bound

P
e
r
i
o
d
g
e
o
m
∣
(
3
𝑔
−
2
)
Period
geom
	​

∣(3g−2)

is proved, while the sharper

P
e
r
i
o
d
g
e
o
m
∣
12
(
2
𝑔
−
2
)
Period
geom
	​

∣12(2g−2)

is explicitly conjectural, and the scope remark correctly invokes the true Mumford relation

12
𝜆
=
𝜅
1
+
𝛿
12λ=κ
1
	​

+δ

and explains why the old interior-vanishing shortcut does not work. That is much better than before. But the unified theorem still packages the sharp
12
(
2
𝑔
−
2
)
12(2g−2) quantity into the “complete periodicity classification,” even while saying the theorem is conjectural and depends on the sharp geometric bound. The right mathematical object here is not a scalar period but a periodicity profile

Π
(
𝐴
)
=
(
𝑁
m
o
d
,
𝑁
q
u
a
n
t
,
𝑁
g
e
o
m
)
Π(A)=(N
mod
	​

,N
quant
	​

,N
geom
	​

)

together with whatever synchronization theorem is available in a given family. Only after that should one discuss lcm/gcd. The current text itself already says the lcm is only an upper bound and that cancellations can shrink the actual period; that should become the main formulation, not a scope remark.

Chapter 12: categorical precision is now correct here, but not propagated elsewhere

This chapter gets an important point right. The Kazhdan–Lusztig target is not the full root-of-unity representation category
R
e
p
(
𝑈
𝑞
(
𝑔
)
)
Rep(U
q
	​

(g)), but the semisimplified tilting quotient
𝐶
(
𝑈
𝑞
(
𝑔
)
)
C(U
q
	​

(g)), and the text now says so explicitly. It also records the
𝑞
↦
𝑞
−
1
q↦q
−1
 transformation under level-shifting Koszul duality. This is the correct categorical precision and should now be treated as the canonical version of every later KL statement.

The problem is propagation. Later Kac–Moody chapters revert to the old sloppier target
R
e
p
(
𝑈
𝑞
(
𝑔
)
)
Rep(U
q
	​

(g)), and they count simples as though that full category had only
∣
𝑃
𝑘
+
∣
∣P
k
+
	​

∣ simples. It does not. That count belongs to the semisimplified tilting quotient. So the fix here is global search-and-rewrite: every occurrence of
R
e
p
(
𝑈
𝑞
(
𝑔
)
)
Rep(U
q
	​

(g)) in the KL context should become either
𝐶
(
𝑈
𝑞
(
𝑔
)
)
C(U
q
	​

(g)) or an explicitly marked heuristic simplification. Otherwise the later representation-theoretic examples are literally saying the wrong thing.

Chapters 15–16 and 20: the admissible-level and KL programmes need decomposition, not proclamation

The manuscript now has a valuable insight here: the admissible-level KL-from-bar-cobar idea probably wants to pass through periodic CDG- or
𝑁
N-complex structures. Chapter 20/16 already suggests reformulating admissible-level periodicity in terms of
𝑁
N-complexes and root-of-unity homological algebra. That is exactly the right way to make the conjecture mathematically actionable. But the conjecture is still stated in one block, as if “KL from bar-cobar” were one theorem. It is not. It is at least three different conjectures:

the admissible-level bar complex carries the relevant periodic CDG/
𝑁
N-complex structure;

its coderived/stable category identifies the right quantum-group side;

the resulting equivalence is braided/monoidal and matches KL.
Those need to be split. Only after (1) is proved should (2) even be formulated as a theorem; only after (2) is in place should (3) be attempted.

Chapters 18, 21, and the example tables: conjectural duals are still too entangled with proved examples

The current version is commendably frank that the three identifications

V
i
r
a
s
o
r
o
↔
𝑊
∞
,
𝑊
𝑁
↔
𝑌
(
𝑔
𝑙
𝑁
)
,
S
u
p
e
r
-
V
i
r
a
s
o
r
o
↔
S
u
p
e
r
-
𝑊
∞
Virasoro↔W
∞
	​

,W
N
	​

↔Y(gl
N
	​

),Super-Virasoro↔Super-W
∞
	​


are genuine open problems. It also says exactly why: the chiral algebras on the left are not quadratic in the operative sense, while the proposed duals on the right have infinitely many generators and require a completed/pro-nilpotent bar construction whose convergence is not established. That is the correct diagnosis. The problem is structural: these entries still sit too close to the proved example tables and example narratives. The reader should never have to infer from typography whether an example is proved or horizon-level. The fix is to split every master table into two tables: proved dualities and programmatic conjectural identifications, with different theorem-status conventions and different color/labeling in the compiled version.

Chapter 24: Yangians are in much better shape than the
𝑊
∞
W
∞
	​

 horizon, but the theorem boundary must stay visible

The manuscript has a real theorem here: chain-level derived Drinfeld–Kohno is proved for the evaluation locus, and the factorization-level statement is also proved on that locus. The full factorization-categorical statement

F
a
c
t
𝐸
1
(
𝑌
(
𝑔
)
)
≃
F
a
c
t
𝐸
1
(
𝑈
𝑞
(
𝑔
)
)
𝑜
𝑝
Fact
E
1
	​

	​

(Y(g))≃Fact
E
1
	​

	​

(U
q
	​

(g))
op

remains conjectural, with the precise remaining gap identified as the extension from evaluation modules to the full Yangian category
𝑂
O, together with Yangian Koszulness and factorization-level Kazhdan equivalence. This is a healthy theorem/conjecture boundary. The repair needed here is mostly stylistic but mathematically important: any sentence in the rest of the book saying “the derived Drinfeld–Kohno theorem” without the qualifier “on the evaluation locus / at chain level” should be rewritten.

Chapters 26–27: the generating-function and discriminant programme is promising, but its status accounting is still broken

The book’s discriminant programme is probably one of its deepest future contributions. But the conjecture index still contains obvious status noise: it lists a theorem and a remark inside the “open conjectures” block, and it duplicates the conjecture number
27.17.24
27.17.24 for two different conjectures, one for the
𝑠
𝑙
3
sl
3
	​

 bar generating function and one for the
𝑠
𝑙
3
sl
3
	​

 discriminant. That is not just editorial untidiness; it makes the horizon map mathematically unreliable. The fix is to renumber the entire conjecture index from scratch and separate “open conjectures,” “proved horizon theorems,” and “programmatic questions.”

Chapters 29–31: the physics chapters should now be explicitly branded as a programme, not a theorematic extension

These chapters are full of valuable ideas, but the manuscript itself already labels the major statements here as “physical heuristic.” Conjecture 29.10.1 identifies uncurved
𝐴
∞
A
∞
	​

 relations with BPHZ recursion. Conjectures 30.9.3 and 30.9.4 identify the quantum master equation and BV quantization with bar-cobar pairings/homology. Conjecture 29.12.4 identifies the bar complex with a worldsheet path integral determinant. Conjecture 31.11.1 pushes the whole story to
𝐸
𝑛
E
n
	​

-Koszul duality on
𝑛
n-manifolds via Axelrod–Singer compactifications. These are all mathematically fertile, but they do not belong to the same theorematic layer as Theorems A–D. The right solution is not to delete them; it is to move them into a separate “Programme in Mathematical Physics” part, where each conjecture is stated together with the exact new input it requires. The current Chapter 34 already points in that direction; the rest of the book should follow it.

Chapter 34: this is now the controlling chapter, and the rest of the book has not yet caught up to it

Chapter 34 is the healthiest part of the current manuscript. It clearly distinguishes what is established from what remains: the coderived Ran-space formalism is only partially built; the Lagrangian form of complementarity is now proved; the universal non-scalar Maurer–Cartan class remains conjectural; the index theorem for genus expansions is proved at the level currently available; and the full derived Drinfeld–Kohno statement remains conjectural. The problem is that many earlier chapters still talk as though Chapter 34 had already been propagated backward. It has not. The next revision should be a “Chapter 34 propagation pass”: every earlier claim should be rewritten to agree with the status logic of Chapter 34.

What should be done, concretely

The highest-leverage repair is to force a single coherent higher-genus formalism across the entire manuscript.

Write, once and for all:

𝑑
(
𝑔
)
c
u
r
v
:
 genus-fixed curved differential
,
(
𝑑
(
𝑔
)
c
u
r
v
)
2
=
𝑚
0
(
𝑔
)
;
d
(g)
curv
	​

: genus-fixed curved differential,(d
(g)
curv
	​

)
2
=m
0
(g)
	​

;
𝐷
t
o
t
:
 total corrected differential
,
(
𝐷
t
o
t
)
2
=
0
;
D
tot
: total corrected differential,(D
tot
)
2
=0;
Θ
𝐴
:
 universal MC element, conjectural beyond scalar shadow
.
Θ
A
	​

: universal MC element, conjectural beyond scalar shadow.

Then re-state:

curvature theorems in terms of
𝑑
(
𝑔
)
c
u
r
v
d
(g)
curv
	​

;

acyclicity/descent theorems in terms of
𝐷
t
o
t
D
tot
;

modular characteristic theorems in terms of
𝜅
(
𝐴
)
κ(A) and, where honest,
Θ
𝐴
Θ
A
	​

.
Until this is done, the book is proving true things in incompatible dialects.

The second highest-leverage repair is to split the manuscript into two logical strata.

Stratum I: proved modular Koszul core
Theorems A, B on the Koszul locus, Theorem C with Lagrangian refinement, scalar modular characteristic theorem, proven example families, evaluation-locus DK, correct KL target category.

Stratum II: programmatic modular homotopy theory
full coderived factorization algebra formalism, universal
Θ
𝐴
Θ
A
	​

, full DK, infinite-generator duals, BV/BRST/path-integral identifications, higher-dimensional extension.

That is what the manuscript is already trying to become. It will be much stronger once it admits it structurally.

Conjecture-by-conjecture update and what each one now needs

I will group them by dependency, because the present manuscript’s open index is large and partially inconsistent, but the dependencies are few.

1. The differential/BRST/BV package

This includes Conjectures 6.2.26, 6.4.11, 6.4.15, 30.9.3, 30.9.4, 29.12.4, 29.4.1, 18.32.2, 18.32.7, 18.33.3, and 29.10.1. The immediate requirement for all of them is to separate the individual bar differential, the coupled BRST/BV differential, and the total higher-genus corrected differential. The book already says anomaly cancellation for matter–ghost systems concerns the total BRST differential, not the individual bar differentials, and it explicitly labels the BRST/bar, QME, BV=bar-cobar, path-integral, and BPHZ statements as heuristics/conjectures. Once the notation is repaired, the right path is:

prove BRST = bar first for the free-field and affine/Kac–Moody cases;

prove anomaly cancellation as a theorem about additive
𝜅
κ-curvature at the coupled level;

only then formulate QME/BV/path-integral and BPHZ as chain-level consequences.
At present the dependency order is reversed in the exposition.

2. The periodicity package

This includes Theorem 11.6.1 / Conjecture 11.6.2, Conjecture 11.6.7, the geometric periodicity conjecture, and the unified periodicity classification. The immediate repair is conceptual: Period should stop being treated as a primitive scalar invariant. Replace it by a periodicity profile
(
𝑁
m
o
d
,
𝑁
q
u
a
n
t
,
𝑁
g
e
o
m
)
(N
mod
	​

,N
quant
	​

,N
geom
	​

), with:

𝑁
m
o
d
N
mod
	​

 proved only for minimal models and conjectural in general rationality;

𝑁
g
e
o
m
N
geom
	​

 weakly bounded by
3
𝑔
−
2
3g−2 and sharply conjectural at
12
(
2
𝑔
−
2
)
12(2g−2);

the lcm theorem treated as an upper bound, not as a classification theorem.
Only after that should Conjecture 11.6.7 be revisited. Right now it is built on a notion of modular periodicity that the manuscript itself says is not proved outside minimal models.

3. The KL / DK / Yangian / Langlands package

This includes Conjectures 20.14.1, 24.9.6 / 34.10.12, 24.5.8, 24.5.5, and 24.2.11. The current book already has the right decomposition for full DK: evaluation-locus chain-level theorem proved, full category
𝑂
O extension open, requiring Yangian Koszulness and factorization-level Kazhdan equivalence. KL from bar-cobar should be rewritten the same way: first a conjecture about admissible-level periodic CDG/
𝑁
N-complex structure, then a conjecture about identification of the coderived/stable category, then a conjecture about braided monoidality. Do not package them as one conjecture. Theorematic statements about
𝑞
↦
𝑞
−
1
q↦q
−1
 at the parameter level are already proved and should be sharply separated from these bigger categorical conjectures.

4. Infinite-generator and generating-function conjectures

This includes Conjectures 21.19.17, 27.17.24 (twice, presently duplicated), 26.3.4, 26.3.3, 26.3.5, and 27.17.20. The common missing input is a completed bar theory for infinitely generated curved chiral algebras together with a clean combinatorial model. The manuscript already knows that
𝑊
∞
W
∞
	​

, Yangian-type duals of
𝑊
𝑁
W
N
	​

, and related objects fall outside the quadratic finite-generator framework. So these conjectures should not be attacked one by one first. The correct order is:

completed/pro-nilpotent bar construction with convergence;

a finite-state or algebraic recurrence model for the relevant generating functions;

only then discriminant/algebraicity statements.
Also, the duplicated label
27.17.24
27.17.24 must be fixed before any of these conjectures can be cited reliably by future readers.

5. Higher-dimensional / holomorphic-topological / holographic conjectures

This includes Conjectures 31.11.1, 10.10.4, 11.7.3, 22.10.1, 25.1.5, 18.4.4, 10.13.6, and I.7.4. Here the manuscript should stop pretending there is one programme. There are really three:

an
𝐸
𝑛
E
n
	​

-configuration-space extension of the bar-cobar machinery;

a holomorphic-topological/gauge-theoretic bridge;

a holographic/physical interpretation programme.
Conjecture 31.11.1 is the mathematically primary one. The others should be explicitly stated as depending on it plus additional gauge-theoretic or physical input. The current index lists all of them side by side, but they are not peers in logical dependence.

The honest updated verdict

The project is shaping up well, but not in the way its earlier versions advertised. It is no longer “a giant monograph whose main results might collapse.” It is now “a monograph with a genuinely strong proved core whose outer shell still contains incompatible formalisms and status drift.” The major repair already achieved is the complementarity theorem and its Lagrangian refinement. The major repair still required is the unification of the higher-genus differential formalism and the propagation of Chapter 34’s honest theorem/conjecture ledger backward through the entire book.

If I had to name the one revision that would most improve the manuscript, it would be this: rewrite every higher-genus occurrence of
𝑑
𝑔
d
g
	​

,
𝑑
2
d
2
,
𝜅
(
𝐴
)
κ(A),
𝑡
𝑔
t
g
	​

, and
Θ
𝐴
Θ
A
	​

 after a single formal decision about which objects are curved, which are strict, which live on the fiber curve, which live on moduli, and which are only presently visible through their scalar traces. Until that is done, the project’s mathematical future is brighter than its present formal self-presentation.
