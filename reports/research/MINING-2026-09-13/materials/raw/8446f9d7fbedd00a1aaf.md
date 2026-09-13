The ordered coefficient construction can be recovered substantially. It supports an explicit associative dg algebra whose bar and Koszul dual differential retain collision classes. The general comparison with a native chiral multiplication remains a separate theorem.

`changed_paths: []`. No files, git state, builds, or rendered artifacts were changed. Requested controls were `gpt-6-astra/ultra`; observed runtime metadata was unavailable and remains unverified.

### 1. The actual all-point coefficient algebra

Work over a characteristic-zero field \(k\). For a finite nonempty label set \(I\), put
\[
R_I=k[z_i\mid i\in I],\qquad \mathcal O_I=\operatorname{Ord}(I).
\]
For a nonempty subset \(J\subset\mathcal O_I\), let \(D(J)\) contain the unordered pairs whose relative order varies among the orders in \(J\). Define
\[
R_{I,J}
 =
R_I[(z_i-z_j)^{-1}\mid\{i,j\}\in D(J)].
\]

Take one copy \(U_\sigma=\operatorname{Spec}R_I\) for each \(\sigma\in\mathcal O_I\). Glue \(U_\sigma\) and \(U_\tau\) by the identity on \(\operatorname{Spec}R_{I,\{\sigma,\tau\}}\).

The gluing is valid: for three orders, the pairs varying among them are
\[
D(\{\sigma,\tau,\rho\})
 =
D(\{\sigma,\tau\})\cup D(\{\sigma,\rho\}),
\]
and the same identity holds from either other anchor. Thus the triple intersections agree, and the identity transition maps satisfy the cocycle condition. Denote the resulting scheme by \(X_I^{\mathrm{ord}}\).

Its finite intersections are precisely \(\operatorname{Spec}R_{I,J}\). In particular, this construction specifies every coefficient ring and every restriction map.

Choose an auxiliary ordering of \(\mathcal O_I\). The finite Čech complex is
\[
\check C_I^p
 =
\bigoplus_{\sigma_0<\cdots<\sigma_p}
R_{I,\{\sigma_0,\ldots,\sigma_p\}},
\]
with
\[
(\delta c)_{\sigma_0\ldots\sigma_{p+1}}
 =
\sum_{a=0}^{p+1}(-1)^a
c_{\sigma_0\ldots\widehat{\sigma_a}\ldots\sigma_{p+1}}
\big|_{U_{\sigma_0}\cap\cdots\cap U_{\sigma_{p+1}}}.
\]
The Alexander–Whitney product is
\[
(c\smile d)_{\sigma_0\ldots\sigma_{p+q}}
 =
c_{\sigma_0\ldots\sigma_p}
d_{\sigma_p\ldots\sigma_{p+q}},
\]
after the indicated restrictions. Associativity follows by cutting an index string twice. Expanding \(\delta(c\smile d)\) gives
\[
\delta(c\smile d)=\delta c\smile d+(-1)^p c\smile\delta d.
\]

Every term is a finite sum of flat \(R_I\)-localizations. The cover and all its intersections are affine. The augmented sheaf Čech resolution contracts on a stalk by inserting a chart containing that stalk. Consequently,
\[
\check C_I\simeq R\Gamma(X_I^{\mathrm{ord}},\mathcal O)
\]
as an associative dg algebra model.

For symmetric coefficient maps, retain the commutative Thom–Sullivan model
\[
C_I=
\left\{
(\omega_J)_J:
\omega_J\in R_{I,J}\otimes\Omega_{\mathrm{poly}}^\bullet(\Delta^J),
\quad
\omega_J|_{\Delta^K}=\omega_K|_{R_{I,J}}
\right\},
\]
where
\[
\Omega_{\mathrm{poly}}^\bullet(\Delta^J)
=
k[t_\sigma,dt_\sigma\mid\sigma\in J]/
\left(\sum t_\sigma-1,\sum dt_\sigma\right).
\]
The differential acts on the simplex variables; the \(z_i\) have degree zero and zero differential. Multiplication is the ordinary graded commutative product. Polynomial integration supplies the comparison with the Čech complex in characteristic zero. This comparison is not a claim that ordinary integration preserves the Alexander–Whitney product strictly.

The primary construction appears in Alfonsi–Kim–Young, §§4.1–4.2. Their §5 gives actual coefficient maps, rather than only a description of the charts. [Primary source](https://arxiv.org/html/2401.11917v1#S4)

### 2. Three labels already require the whole geometry

At a geometric point, partition \(I\) into blocks \(B\) of equal coordinate values. Two orders determine the same point precisely when they restrict to the same order on every \(B\). Hence
\[
X_I^{\mathrm{ord}}\times_{\operatorname{Spec}R_I}\operatorname{Spec}\kappa
\cong
\bigsqcup_{\prod_B|B|!}\operatorname{Spec}\kappa.
\]

This also computes the derived coefficient fibre. Tensor the bounded flat Čech complex with \(\kappa\). An intersection vanishes if one of its inverted differences becomes zero. The surviving orders split into classes having identical restrictions to the equality blocks. Each class contributes the cochain complex of a simplex, which contracts to one copy of \(\kappa\). Its multiplication is coordinatewise.

For three coincident labels the coefficient fibre is therefore \(k^6\). The product of the three binary doubles has fibre \(k^8\). Its extra branches are the two directed cycles.

More generally, let \(P_I\) be the fibre product of all binary doubles over \(\operatorname{Spec}R_I\). Remove the closed loci where a directed triangle has all three coordinates equal. The remaining scheme is \(X_I^{\mathrm{ord}}\): within each equality block, absence of a directed triangle makes the tournament transitive, hence totally ordered.

For \(I=\{1,2,3\}\), remove translation and write the differences as \(x,y,x+y\). Put
\[
M=\frac{k[x^{\pm1},y^{\pm1}]}
        {k[x^{\pm1},y]+k[x,y^{\pm1}]}.
\]
The removed cyclic points give the exact triangle
\[
(M\oplus M)[-2]
\longrightarrow R\Gamma(P_3,\mathcal O)
\longrightarrow C_3
\longrightarrow(M\oplus M)[-1].
\]

Indeed, the supported complex at either point is
\[
[k[x,y]\longrightarrow
 k[x^{\pm1},y]\oplus k[x,y^{\pm1}]
 \longrightarrow k[x^{\pm1},y^{\pm1}]],
\]
whose only cohomology is \(M\) in degree two. Excision gives the triangle.

The derived specialization of \(M\) at \(x=y=0\) is \(k[2]\). To check this, tensor its Koszul resolution with \(M\):
\[
M\xrightarrow{w\mapsto(-yw,xw)}
M^2\xrightarrow{(u,v)\mapsto xu+yv}M.
\]
Both coordinate multiplications are surjective. Their common kernel is \(kx^{-1}y^{-1}\). If \(xu+yv=0\), choose \(w\) with \(xw=v\). Then \(u+yw\in\ker x\). Surjectivity of \(y\) on \(\ker x\) supplies \(a\in\ker x\) with \(ya=u+yw\), and \(w-a\) is the required preimage. Thus the specialized triangle is
\[
k^2\longrightarrow k^8\longrightarrow k^6.
\]

This is the precise three-point correction. Independent binary coefficients omit its support map and degree shift.

### 3. The actual insertion maps

Let \(T\) be a finite rooted tree, with local coordinates \(u_{v,a}\) on the inputs of each vertex \(v\). Assign a scale \(t_v\) to each nonroot internal vertex. Define leaf coordinates recursively:
\[
Z_i^{(v)}=
\begin{cases}
u_{v,a},&a\text{ is leaf }i,\\
u_{v,a}+t_w Z_i^{(w)},&a\text{ enters vertex }w.
\end{cases}
\]
Local total orders induce the global leaf order by concatenation.

For a collection \(L\) of tuples of vertex orders, let \(L_v\) be its projection at \(v\). Put
\[
D_{T,L}
 =
\bigotimes_v
k[u_{v,a}]
[(u_{v,a}-u_{v,b})^{-1}:\{a,b\}\in D(L_v)]
\]
and
\[
E_{T,L}
 =
D_{T,L}[[t_v]][t_v^{-1}].
\]
An element of this last ring has a fixed lower bound in every scale exponent.

If \(v\) is the least common ancestor of \(i,j\), then
\[
Z_i-Z_j=s_v(u_{v,a}-u_{v,b}+r_{ij}),
\]
where \(s_v\) is the product of scales above \(v\), and \(r_{ij}\) belongs to the ideal of scales below \(v\).

Suppose the global order of \(i,j\) varies in \(L\). Their order therefore varies between the corresponding inputs \(a,b\) at \(v\). Thus \(u_{v,a}-u_{v,b}\) is invertible in \(D_{T,L}\). Consequently,
\[
(Z_i-Z_j)^{-1}
 =
s_v^{-1}(u_{v,a}-u_{v,b})^{-1}
\sum_{r\ge0}
\left(
-\frac{r_{ij}}{u_{v,a}-u_{v,b}}
\right)^r
\]
exists in \(E_{T,L}\).

This proves the coefficient map
\[
R_{I,\ell(L)}\longrightarrow E_{T,L},
\qquad z_i\longmapsto Z_i,
\]
including every inverted generator. Uniqueness of inverses proves compatibility with restriction.

For the Thom–Sullivan forms, the atlas map \(\ell\) gives
\[
t_\sigma\longmapsto
\sum_{a:\ell(a)=\sigma}t_a,
\qquad
dt_\sigma\longmapsto
\sum_{a:\ell(a)=\sigma}dt_a.
\]
These formulas preserve the simplex relations, differential, products, and faces. They therefore give an actual dg algebra map
\[
g_T:C_I\longrightarrow\mathcal E_T,
\]
where \(\mathcal E_T\) is the compatible-family expansion model of the product atlas.

For a finite rational input, different refinement orders agree. They give the same polynomial leaf substitution, then the same inverses in the final expansion ring. This proves coherence on the rational-image coefficient system. It does not define refinement on every unrestricted intermediate Laurent series.

For example,
\[
\sum_{n\ge0}t^n u^{-n^2}
\]
belongs to \(k[u,u^{-1}][[t]]\), but \(u=\delta a,\ t=\delta\epsilon\) produces \(\delta^{n-n^2}\), with no fixed lower bound.

### 4. A finite-state algebra that retains the collision coefficient

The following is an explicit additional construction, independently derived from the preceding coefficients.

Define in \(C_I\)
\[
q_{ij}=\sum_{\sigma:i\prec_\sigma j}t_\sigma,
\qquad
\omega_{ij}=\frac{dq_{ij}}{z_i-z_j}.
\]
On a face where the pair order is constant, \(q_{ij}\) is either zero or one, so \(dq_{ij}=0\). Thus the apparent pole satisfies every face condition and \(\omega_{ij}\in C_I^1\). Moreover,
\[
d\omega_{ij}=0,\qquad \omega_{ji}=\omega_{ij}.
\]

This coefficient is not exact. Restrict to two charts differing by one adjacent exchange of \(i,j\). Their union has overlap obtained by inverting only \(z_i-z_j\). The restriction of \(\omega_{ij}\) is \(\pm dt/(z_i-z_j)\), whose integral represents the nonzero principal part \(\pm(z_i-z_j)^{-1}\).

Define a finite free graded \(C_I\)-module
\[
A_I=C_I1
 \oplus\bigoplus_{i\in I}C_Ia_i
 \oplus\bigoplus_{i\ne j}C_Ib_{ij},
\]
with
\[
|a_i|=0,\quad |b_{ij}|=-1,\quad da_i=db_{ij}=0.
\]
The coefficient algebra acts graded centrally. Give \(A_I\) its unit and impose
\[
a_i a_j=\omega_{ij}b_{ij}\quad(i\ne j),\qquad a_i^2=0,
\]
with every product involving \(b_{ij}\) and another augmentation-ideal generator equal to zero.

These formulas define an augmented associative dg algebra over \(C_I\).

*Proof.* Every product of three augmentation-ideal elements vanishes in both parenthesizations. Products involving the unit obey associativity by graded central scalar extension. The only nonzero generator products have closed coefficient \(\omega_{ij}\), so the Leibniz identity holds. The augmentation kills all \(a_i,b_{ij}\). ∎

This example is noncommutative when \(b_{ij}\) and \(b_{ji}\) are retained as distinct generators. Its multiplication uses a nonzero derived collision class.

For every actual coefficient expansion \(g_T:C_I\to\mathcal E_T\), form
\[
A_{I,T}=\mathcal E_T\otimes_{C_I}A_I.
\]
The scalar-extension map is an algebra map, with
\[
a_i a_j=g_T(\omega_{ij})b_{ij}.
\]
Thus the coefficient expansion and multiplication satisfy an exact equation:
\[
g_T^*\mu=\mu_T(g_T^*\otimes g_T^*).
\]

### 5. Its bar differential and Koszul dual are explicit

Use cohomological grading, \(|s|=-1\), and
\[
(f\otimes g)(x\otimes y)=(-1)^{|g||x|}f(x)\otimes g(y).
\]
For the augmentation ideal \(\bar A_I\), define
\[
B_{C_I}A_I=\bigoplus_{r\ge0}(s\bar A_I)^{\otimes_{C_I}r}.
\]
The cogenerator maps are
\[
b_1(sa)=-s(da),\qquad
b_2(sa\otimes sb)=(-1)^{|a|}s(ab).
\]
Consequently,
\[
b_{\mathrm{mult}}[a_1|\cdots|a_r]
 =
\sum_{i=1}^{r-1}
(-1)^{\sum_{j<i}(|a_j|-1)+|a_i|}
[a_1|\cdots|a_i a_{i+1}|\cdots|a_r].
\]

The nontrivial low-length formulas are
\[
b[a_i|a_j]=[\omega_{ij}b_{ij}],
\]
and
\[
b[a_i|a_j|a_k]
 =
[\omega_{ij}b_{ij}|a_k]
 -
[a_i|\omega_{jk}b_{jk}].
\]
The second application of \(b_{\mathrm{mult}}\) gives zero because every product involving a \(b\)-generator vanishes.

For a general associative dg algebra, disjoint contractions cancel by the tensor signs. The remaining three-input component is
\[
b_{\mathrm{mult}}^2[a|b|c]
 =
(-1)^{|b|}s((ab)c-a(bc)).
\]
The internal terms vanish by \(d^2=0\) and the Leibniz identity. This proves \(b^2=0\) in every length.

Because scalar extension preserves the displayed tensor words and their generator formulas, there is a strict isomorphism
\[
\mathcal E_T\otimes_{C_I}B_{C_I}A_I
\cong
B_{\mathcal E_T}A_{I,T}.
\]
It commutes with every adjacent face, the differential, and deconcatenation.

Assign weights
\[
\operatorname{wt}(a_i)=1,\qquad
\operatorname{wt}(b_{ij})=2,\qquad
\operatorname{wt}(C_I)=0.
\]
Every bar weight is a finite free graded \(C_I\)-module. Its augmentation dual is therefore
\[
A_I^!
=
\operatorname{Hom}_{C_I}(B_{C_I}A_I,C_I)
\cong
C_I\langle\!\langle\alpha_i,\beta_{ij}\rangle\!\rangle,
\]
completed by positive weight, with
\[
|\alpha_i|=1,\qquad|\beta_{ij}|=2.
\]
Normalize
\[
\alpha_i(sa_i)=1,\qquad\beta_{ij}(sb_{ij})=1.
\]
Then
\[
\boxed{\quad d\alpha_i=0,\qquad
d\beta_{ij}=-\omega_{ij}\alpha_i\alpha_j.\quad}
\]

The sign is forced. Suspension over a graded coefficient algebra gives
\[
s(\omega_{ij}b_{ij})=-\omega_{ij}sb_{ij}.
\]
Hence \(d\beta_{ij}\) evaluates to \(+\omega_{ij}\) on \(sa_i\otimes sa_j\). Koszul convolution gives
\[
(\alpha_i\alpha_j)(sa_i\otimes sa_j)=-1.
\]

The normalized left bar resolution
\[
A_I\otimes_{C_I}B_{C_I}A_I\longrightarrow C_I
\]
is semifree: filter by word length; its graded generators are finite tensor words in the free state basis. The usual extra degeneracy inserting the unit contracts its augmented underlying \(C_I\)-complex. Applying \(\operatorname{Hom}_{A_I}(-,C_I)\) gives the displayed dual complex. Its deconcatenation cup product agrees with composition through the bar comodule lifts. Therefore
\[
A_I^!\simeq R\operatorname{Hom}_{A_I}(C_I,C_I)
\]
as an associative dg algebra.

This is an explicit geometric coefficient in the Koszul dual differential, not merely a dimension comparison.

### 6. The three-point nested calculation

Take
\[
z_1=Z+\epsilon x_1,\qquad
z_2=Z+\epsilon x_2,\qquad
z_3=W.
\]
The product atlas has the four induced orders
\[
123,\quad213,\quad312,\quad321.
\]
Let \(q_{\mathrm{in}}\) record \(1<2\), and let \(q_{\mathrm{out}}\) record the pair-cluster preceding \(3\). They are the sums of the corresponding barycentric coordinates in this product atlas.

Then
\[
g_T(\omega_{12})
 =
\epsilon^{-1}\frac{dq_{\mathrm{in}}}{x_1-x_2},
\]
while, on the outer overlap where \(Z-W\) is invertible,
\[
g_T(\omega_{13})
 =
dq_{\mathrm{out}}
\sum_{r\ge0}
\frac{(-\epsilon)^r x_1^r}{(Z-W)^{r+1}},
\]
\[
g_T(\omega_{23})
 =
dq_{\mathrm{out}}
\sum_{r\ge0}
\frac{(-\epsilon)^r x_2^r}{(Z-W)^{r+1}}.
\]

The transported bar face is therefore, for example,
\[
[a_1|a_2]\longmapsto
\left[
\epsilon^{-1}
\frac{dq_{\mathrm{in}}}{x_1-x_2}b_{12}
\right].
\]
The transported dual differential is
\[
d\beta_{13}
 =
-
dq_{\mathrm{out}}
\sum_{r\ge0}
\frac{(-\epsilon)^r x_1^r}{(Z-W)^{r+1}}
\alpha_1\alpha_3.
\]
These equations exhibit both punctured scales and completed cross-cluster expansions inside actual bar operations.

Completed scalar extension here means scalar extension in each finite weight truncation followed by inverse limit. It does not mean moving an arbitrary algebraic tensor product through an infinite product.

### 7. The precise reconstruction theorem for this construction

Let \(Q=\widehat B_{C_I}A_I\), completed by the positive weights above. Define the completed cobar weightwise, with \(t=s^{-1}\):
\[
d_\Omega(tc)
 =
-t(dc)+
\sum_{\bar\Delta c=\sum c'\otimes c''}
(-1)^{|c'|+1}(tc')(tc'').
\]
Then the counit
\[
\widehat\Omega_{C_I}Q\longrightarrow A_I
\]
is a quasi-isomorphism in every weight.

*Proof.* Expand a cobar word into its original \(A_I\)-letters. At weight \(w\), there are at most \(w\) such letters. Filter by their number. Multiplication lowers this filtration. On associated graded, each gap between original letters has two statuses: inside a bar block, or between two cobar factors. The coproduct differential changes the former to the latter with coefficient \(\pm1\).

After the suspension signs are included, the gap contribution is the tensor product of copies of
\[
[k\xrightarrow{1}k].
\]
It is contractible when at least one gap exists: contract the leftmost gap with the tensor sign of the preceding factors. The one-letter contribution is \(A_I\), and the counit is its identity. The filtration is finite in every weight, proving the assertion. Taking the product of these weightwise equivalences uses the declared weight completion. ∎

The same proof gives the unit on positive-weight coalgebras with the corresponding finite word bounds and derived tensor models. It does not identify the augmentation dual with a Verdier dual or establish a double-centralizer theorem without its own module hypotheses.

### 8. The genuine curve-Ran bar remains a second construction

For a smooth curve \(X\), take the stable category of right \(D\)-modules on nonempty \(\operatorname{Ran}(X)\), with the actual chiral tensor.

Its \(r\)-fold tensor on a labelled chart \(X^I\) has summands indexed by ordered surjections
\[
\pi:I\twoheadrightarrow[r].
\]
Writing \(I_a=\pi^{-1}(a)\), its summand is
\[
j_{\pi,*}j_\pi^!
\left(A_{I_1}\boxtimes\cdots\boxtimes A_{I_r}\right),
\]
where \(j_\pi\) excludes coincidences between different blocks.

For an associative multiplication in this tensor category, the \(i\)-th bar face merges \(I_i,I_{i+1}\). Let \(\rho\) be the merged partition. The open \(U_\pi\) lies in \(U_\rho\). Factor the extension through this inclusion, apply the multiplication on the two merged blocks, and then extend along \(j_\rho\). This gives the actual map
\[
j_{\pi,*}j_\pi^!(\boxtimes_a A_{I_a})
\longrightarrow
j_{\rho,*}j_\rho^!(\boxtimes_b A_{\rho^{-1}(b)}).
\]
The previous suspension signs apply to these maps.

For two labels, the two length-two ordered summands map to \(A_{12}[1]\). For three labels, six length-three summands map to the six ordered bipartition summands, then to \(A_{123}[1]\). On the \(1|2|3\) summand, the two composites are precisely the two nested products with opposite bar signs.

No word longer than \(|I|\) occurs. The finite gap contraction therefore proves associative bar–cobar reconstruction on every cardinality stage. The contractions commute with the derived restriction maps, so they give compatible equivalences of the stage systems.

The geometric tensor formula is Francis–Gaitsgory, Lemma 2.3.4. Its support-cardinality limit and monoidal truncations are Lemma 5.1.4 and §5.1.5. Their general pro-nilpotent operadic result is Proposition 4.1.2; their Lie–commutative specialization is a different output type. [Primary source](https://arxiv.org/pdf/1103.5803)

This is a curve-Ran theorem. It does not identify the preceding raviolo coefficient algebra with its \(D\)-module carrier.

### 9. The first missing implication

The finite-state algebra above proves that collision coefficients can enter honest bar and Koszul dual differentials. It supplies exact compatibility under coefficient expansion. Its \(b_{ij}\), however, remains a state carrying the pair label. No construction here identifies that state with a state at a collapsed point.

For a native ordered chiral theorem, the next obligation is to construct the state multiplication or supported collision map and prove its comparison with the coefficient expansion system. Specifically:

\[
F_{r-1}\partial_i^{\mathrm{ord}}
 =
\partial_i^{\mathrm{ch}}F_r,
\qquad
dF_r=F_rd,
\]
must hold on the declared common expansion domains, together with compatibility with cuts and refinement. If these equalities hold only up to homotopy, the homotopies must satisfy the higher face equations.

A map \(C_I\to\mathcal E_T\) alone has coefficient variance. It does not supply a state contraction. Nor does it define translation, vacuum insertion, coordinate descent, or a supported \(D\)-module target.

There is also a primary-source boundary: Alfonsi–Kim–Young §5.3, Remark 15, introduces the derived coinvariant tensor product in equation (30) and explicitly leaves extension of Theorem 17 to that derived construction unproved. Their binary coinvariant collision theorem cannot establish a derived geometric bar comparison. [Exact source](https://arxiv.org/html/2401.11917v1#S5.SS3)

### 10. Source correspondence and verification limits

The reconstruction text contains the substantial coefficient construction:

- **C, chapters 12–16:** POSIX lines 2440–3435, including complete gluing, excision, tree expansion, and representation-boundary arguments.
- **C, chapters 9–10:** lines 2015–2265, including the actual chiral tensor and finite-cardinality reconstruction.
- **E, chapter 10:** lines 2135–2330, independently read; it contains the same all-order gluing and three-point excision.
- **Live reconstruction:** `core/part1_foundations.tex`, especially lines 344–365, specifies the intended associative chiral operation. `core/part2_duality.tex` specifies its bar and reconstruction claims.
- **Live integrated source:** `Volume_I_Ordered_Chiral_Geometry.tex:399`–509 contains the internal bar and reconstruction statements.

The live `reconstruction/detailed/` directory is empty. `geometry.tex` references the missing detailed ordered geometry, internal bar, and internal duality sources. The archived detailed construction therefore has no verified complete source-level counterpart there.

The current seven-chapter `manuscript/programme.tex` was read in full. Its input inventory and the theorem/section searches show that it develops relations, products, completions, higher operations, translation/exchange, and Gaussian complexes. It does not yet contain the all-order coefficient diagram or the explicit collision-coefficient bar above. I did not reread and certify all seven chapters.

Verified source hashes:

| Source | SHA-256 |
|---|---|
| C, 747603 bytes | `c78745d9a966c927739a49f3b22192c389065372a24de6990b6e58355e9bc75d` |
| E, 464394 bytes | `ebc8bb469caa65b9042f8361e2d94043a2058141da1a1e1b23e85cbd51c34db0` |
| Live `part1_foundations.tex` | `ba2ca20cd16956470283f0dc4a7ed719ea71eb465b186c802740dbaddf5be84e` |
| Live `part2_duality.tex` | `22774bbb58689013ade7c25bfe5c080abed953b09b9863419f12e679053a1a27` |
| Live `Volume_I_Ordered_Chiral_Geometry.tex` | `a34b132180451df2e29f80794579d001b6672ee62d883338afb3351423cc9c84` |

Live repository commit: `cb6e88263f4bb75ef5c1d9db911f61ca5d3d4d9c`; working tree was clean when inspected.

Complete decisive C reading included byte intervals:

- `[125077,151210)`: bar-category context and two-point coefficients.
- `[151194,156901)`: all-order chart construction.
- `[156901,176693)`: excision and mixed configuration comparison.
- `[176692,213862)`: complete tree and coloured coefficient expansion arguments.

An in-memory Python 3.14.6 calculation checked all 1,000 homogeneous triples of the two-label exterior-coefficient algebra for associativity and the bar-square signs. These are exact finite checks. The general proofs are given above.

The proposed additional finite-state algebra and its Koszul dual have not received independent acceptance review.
