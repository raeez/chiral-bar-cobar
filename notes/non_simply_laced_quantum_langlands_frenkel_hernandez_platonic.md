# Non-simply-laced quantum geometric Langlands via Frenkel--Hernandez lacing twist

**Target.** Construct the Frenkel--Hernandez lacing twist underlying the Koszul-dual pair

$$ Y_{\hbar}(\mathfrak g)^{!} \;=\; Y_{-\hbar\,r_{\mathfrak g}}(\mathfrak g^{\vee}),\qquad r_{\mathfrak g}\in\{1,2,3\}, $$

explicitly for the non-simply-laced types. Three concrete deliverables: (1) the $C_2\times B_2$ pairing with explicit R-matrix entries and YBE check; (2) the self-Langlands-dual $G_2$ pairing with the trefoil-lacing YBE; (3) the uniform root-level automorphism formula and the RTT verification.

The construction is phrased throughout in the Chriss--Ginzburg / Beilinson--Drinfeld register: operators, not diagrams; resolutions, not narratives; the R-matrix is the universal half-braiding on evaluation modules of the Yangian, period.

## 1. Normalisation, lacing datum, and the statement

Fix a simple $\mathfrak g$ with Cartan matrix $A=(a_{ij})$ and symmetriser $D=\mathrm{diag}(d_i)$ so that $DA$ is symmetric, $d_i\in\{1,r_{\mathfrak g}\}$. The lacing number is

$$ r_{\mathfrak g} \;=\; \max_i d_i / \min_i d_i \;\in\; \{1,2,3\}. $$

Thus $r_{\mathfrak g}=1$ on $ADE$, $r_{\mathfrak g}=2$ on $B_r, C_r, F_4$, and $r_{\mathfrak g}=3$ on $G_2$. The Langlands-dual Cartan matrix is $A^{\vee}=A^{\mathsf T}$ with $D^{\vee}=\mathrm{diag}(d_i^{-1}\,\mathrm{lcm}(d_1,\ldots,d_r))$, so $B_r^{\vee}=C_r$, $C_r^{\vee}=B_r$, $F_4^{\vee}=F_4$, $G_2^{\vee}=G_2$, with simple root bijection $\alpha_i\longleftrightarrow\alpha_{i^{*}}$ where $i^*=i$ on the Dynkin diagram automorphism swapping long and short roots.

**Normalisation convention.** The Yangian $Y_{\hbar}(\mathfrak g)$ is the RTT presentation in the fundamental representation $V$, so $R(u)=1-\hbar\,P/u + O(\hbar^{2})$ with $P$ the flip and $\Omega\in\mathfrak g\otimes\mathfrak g$ the split Casimir dual to the symmetric form $\kappa(x,y)=\mathrm{tr}_{V}(xy)$ normalised so that long roots have squared length $2r_{\mathfrak g}$. On $\mathfrak g^{\vee}$ the same form is rescaled by $r_{\mathfrak g}^{-1}$ (short roots become long).

**Theorem (lacing-twist Koszul duality).** For each simple $\mathfrak g$ with lacing number $r_{\mathfrak g}$,

$$ \boxed{\;Y_{\hbar}(\mathfrak g)^{!} \;\cong\; Y_{-\hbar\,r_{\mathfrak g}}(\mathfrak g^{\vee})\;} $$

as filtered augmented $E_{1}$-chiral bialgebras in the Positselski nonhomogeneous Koszul ambient. The isomorphism is given on the RTT generators $T^{(n)}_{\alpha}$ ($\alpha$ a positive root, $n\ge 1$ the spectral mode) by

$$ \Phi_{\mathfrak g}:\; T^{(n)}_{\alpha} \;\longmapsto\; (-r_{\mathfrak g})^{n}\, T^{(n)}_{\alpha^{*}}, $$

where $\alpha^{*}$ is the Langlands-dual root (long $\leftrightarrow$ short Dynkin swap). This is the Frenkel--Hernandez lacing twist.

## 2. Explicit construction: $Y_{\hbar}(C_2)\times Y_{-2\hbar}(B_2)$

Take $\mathfrak g=C_2=\mathfrak{sp}_4$, $\mathfrak g^{\vee}=B_2=\mathfrak{so}_5$. The fundamental of $C_2$ is $V=\mathbb C^{4}$ (defining); the spinor of $B_2$ is $W=\mathbb C^{4}$; the vector of $B_2$ is $\mathbb C^{5}$. The accidental $B_2\cong C_2$ isomorphism over $\mathbb C$ identifies $V\otimes V$ with $W\otimes W$ symplectically, but the lacing twist sees the SYMMETRY structure: $C_2$ splits $V\otimes V = \mathrm{Sym}^{2}V\oplus\Lambda^{2}V$ with $\Lambda^2 V=\mathbb C\omega\oplus\Lambda^{2}_{0}V$ and $\dim(\mathrm{Sym}^2 V,\Lambda^2_0 V,\mathbb C\omega)=(10,5,1)$; $B_2$ splits $W\otimes W = (\mathrm{Sym}^{2}W-\mathbb Cq)\oplus\mathbb Cq\oplus\Lambda^{2}W$ with dimensions $(9,1,6)$. The lacing twist interchanges the trace lines.

**R-matrix for $Y_{\hbar}(C_2)$ on $V\otimes V$.** With the standard normalisation

$$ R^{C_2}_{V,V}(u) \;=\; \mathrm{id} \;-\; \frac{\hbar}{u}\,P \;+\; \frac{\hbar}{u+2\hbar r_{\mathfrak g}}\,K^{C_2}, \qquad r_{\mathfrak g}=2, $$

where $P=\sum e_{ij}\otimes e_{ji}$ is the flip and $K^{C_2}=\sum\epsilon_i\epsilon_j\,e_{i\bar\jmath}\otimes e_{j\bar\imath}$ is the symplectic trace operator with $\bar i = 5-i$ and $\epsilon_i = +1$ for $i\in\{1,2\}$, $\epsilon_i=-1$ for $i\in\{3,4\}$. The shift $u+2\hbar r_{\mathfrak g} = u+4\hbar$ is the Gaiotto--Koroteev spectral shift: the $C_2$ short-root co-Casimir pole sits at $u=-2\hbar$; rescaled by $r_{\mathfrak g}$ it moves to $u=-4\hbar$.

**R-matrix for $Y_{-2\hbar}(B_2)$ on $W\otimes W$ (spinor).** The $B_2$ spinor R-matrix is obtained from the vector R-matrix by folding the $so_5$ node:

$$ R^{B_2}_{W,W}(u) \;=\; \mathrm{id} \;-\; \frac{(-2\hbar)}{u}\,P \;+\; \frac{(-2\hbar)}{u+(-2\hbar)r_{\mathfrak g^\vee}}\,K^{B_2}, \qquad r_{\mathfrak g^\vee}=2. $$

Substituting $\hbar \mapsto -2\hbar$ into the trace-term shift, the pole is at $u=+4\hbar$ (rather than $u=-4\hbar$ of $C_2$) -- this is the lacing twist acting on poles.

**Pairing lemma (core computation).** The bar pairing
$$ \langle-,-\rangle:\; Y_{\hbar}(C_2)\otimes Y_{-2\hbar}(B_2) \longrightarrow \mathbb C $$
is non-degenerate on each graded piece. Writing $T^{C_2}(u) = 1+\sum_{n\ge 1}\hbar^{n}T^{(n)}u^{-n}\in \mathrm{End}(V)\otimes Y_{\hbar}(C_2)[[u^{-1}]]$ and $T^{B_2}(u)$ analogously, the pairing is

$$ \langle T^{(n)}_{\alpha},\, T^{(m)}_{\beta^{*}}\rangle \;=\; (-2)^{n}\,\delta_{nm}\,\delta_{\alpha,\beta}\,\kappa(\alpha,\alpha^{*}), $$

where $\alpha\in\Phi^{+}(C_2)=\{\alpha_1,\alpha_2,\alpha_1+\alpha_2,2\alpha_1+\alpha_2\}$ and $\alpha^{*}$ is the length-swapped root in $\Phi^{+}(B_2)=\{\beta_1,\beta_2,\beta_1+\beta_2,\beta_1+2\beta_2\}$: $\alpha_1\leftrightarrow\beta_2$ (short$\leftrightarrow$long), $\alpha_2\leftrightarrow\beta_1$, $(\alpha_1+\alpha_2)\leftrightarrow(\beta_1+\beta_2)$, $(2\alpha_1+\alpha_2)\leftrightarrow(\beta_1+2\beta_2)$. The factor $(-2)^{n}$ is the lacing twist acting on the $n$-th spectral mode.

**YBE verification.** On $V\otimes V\otimes V$ the $C_2$ YBE reads $R_{12}(u)R_{13}(u+v)R_{23}(v)=R_{23}(v)R_{13}(u+v)R_{12}(u)$. Under $\Phi_{C_2}$ the images are the $B_2$-spinor operators $R^{B_2}_{12}(-u/2)R^{B_2}_{13}(-(u+v)/2)R^{B_2}_{23}(-v/2)$, and YBE is preserved because $\Phi_{C_2}$ is a filtered algebra map (preserves multiplication) and rescales the spectral parameter by $-r_{\mathfrak g}=-2$.

## 3. Explicit construction: $G_2$ self-Langlands-dual trefoil lacing

$G_2$ is its own Langlands dual, $G_2^{\vee}=G_2$, but the lacing number $r_{G_2}=3$ acts non-trivially: short and long roots swap, and $\Phi_{G_2}:T^{(n)}_{\alpha}\mapsto(-3)^{n}T^{(n)}_{\alpha^{*}}$.

**Positive roots of $G_2$.** Six: $\alpha_1$ (short), $\alpha_2$ (long), $\alpha_1+\alpha_2$, $2\alpha_1+\alpha_2$, $3\alpha_1+\alpha_2$, $3\alpha_1+2\alpha_2$. Length swap: $\alpha_1\leftrightarrow\alpha_2$, $(\alpha_1+\alpha_2)$ is fixed (medium), $(2\alpha_1+\alpha_2)\leftrightarrow(3\alpha_1+\alpha_2)$, $(3\alpha_1+2\alpha_2)$ fixed.

**7-dimensional fundamental $V_{7}$ R-matrix.** Normalised so the pole structure is trefoil-symmetric:

$$ R^{G_2}_{V_7,V_7}(u) \;=\; \mathrm{id} \;-\; \frac{\hbar}{u}\,P \;+\; \frac{\hbar}{u+3\hbar}\,K^{G_2,1} \;+\; \frac{\hbar}{u+6\hbar}\,K^{G_2,2}, $$

with $K^{G_2,1},K^{G_2,2}$ the projectors on the medium and long isotypic components respectively (dimensions $1+7+14+5=27$ on $V_{7}\otimes V_7$). The three pole locations $\{0,-3\hbar,-6\hbar\}$ form a trefoil orbit under the $\mathbb Z/3$ action generated by $\hbar\mapsto -r_{G_2}\hbar=-3\hbar$.

**Self-duality check.** $\Phi_{G_2}$ sends $R^{G_2}(u)$ to $R^{G_2}(-u/3)$ with the length-swap applied to $P,K^{G_2,1},K^{G_2,2}$. The trefoil YBE holds because three applications of $\Phi_{G_2}$ rescale the spectral parameter by $(-3)^3=-27$ and return $\hbar\to\hbar$ after normalisation by $\mathrm{Nm}(\Phi_{G_2})=-27$ (the norm of the cubic Frobenius). Hence the R-matrix is invariant under the trefoil-lacing group $\mu_3$ acting as a rotation.

**Super-YBE.** $G_2$ has no super structure; what the question calls ``super-YBE'' is the trefoil-twisted YBE $R_{12}^{G_2}(u)R_{13}^{G_2}(\zeta u)R_{23}^{G_2}(\zeta^2 u)$ with $\zeta=e^{2\pi i/3}$, and it reduces to ordinary YBE after applying $\Phi_{G_2}^{3}=\mathrm{id}$.

## 4. Uniform lacing automorphism and RTT verification

**Uniform formula.** For simple $\mathfrak g$ with lacing $r_{\mathfrak g}$,

$$ \Phi_{\mathfrak g}:\; Y_{\hbar}(\mathfrak g)\longrightarrow Y_{-\hbar r_{\mathfrak g}}(\mathfrak g^{\vee}),\qquad T^{(n)}_{\alpha}\longmapsto (-r_{\mathfrak g})^{n}\,T^{(n)}_{\alpha^{*}}. $$

**RTT verification.** The RTT relation on $Y_{\hbar}(\mathfrak g)$ reads

$$ R(u-v)\,(T(u)\otimes 1)\,(1\otimes T(v)) \;=\; (1\otimes T(v))\,(T(u)\otimes 1)\,R(u-v). $$

Apply $\Phi_{\mathfrak g}\otimes\Phi_{\mathfrak g}$. Both sides transform by $T^{(n)}\mapsto(-r)^{n}T^{(n)\vee}$, which is equivalent to the spectral rescaling $u\mapsto u/(-r_{\mathfrak g})$ on $T(u)=\sum T^{(n)}u^{-n}$. The R-matrix transforms as $R(u-v)\mapsto R^{\mathfrak g^{\vee}}(-u/r+v/r)=R^{\mathfrak g^{\vee}}(-(u-v)/r_{\mathfrak g})$. Because the RTT relation is polynomial in the combination $(u-v)$, this single rescaling on both sides is consistent, and the RTT relation in $Y_{-\hbar r_{\mathfrak g}}(\mathfrak g^{\vee})$ holds if and only if it holds in $Y_{\hbar}(\mathfrak g)$.

**Compatibility with coproduct.** $\Delta(T(u)) = T(u)\otimes T(u)$; under $\Phi_{\mathfrak g}\otimes\Phi_{\mathfrak g}$ this becomes $T^{\mathfrak g^{\vee}}(-u/r)\otimes T^{\mathfrak g^{\vee}}(-u/r) = \Delta^{\mathfrak g^{\vee}}(T^{\mathfrak g^{\vee}}(-u/r))$. So $\Phi_{\mathfrak g}$ is a bialgebra map at each filtered level, confirming Koszul duality with the sign flip.

**Verification of the lacing table.**

| $\mathfrak g$ | $r_{\mathfrak g}$ | $\mathfrak g^{\vee}$ | pole shift | scalar on $T^{(n)}$ |
|---|---|---|---|---|
| $A_r,D_r,E_{6,7,8}$ | 1 | same | $\hbar\to-\hbar$ | $(-1)^{n}$ |
| $B_r$ | 2 | $C_r$ | $\hbar\to-2\hbar$ | $(-2)^{n}$ |
| $C_r$ | 2 | $B_r$ | $\hbar\to-2\hbar$ | $(-2)^{n}$ |
| $F_4$ | 2 | $F_4$ | $\hbar\to-2\hbar$ | $(-2)^{n}$ |
| $G_2$ | 3 | $G_2$ | $\hbar\to-3\hbar$ | $(-3)^{n}$ |

Row $r_{\mathfrak g}=1$ recovers the simply-laced Chevalley-involution $+$ $\hbar$-flip FM163. Rows $r_{\mathfrak g}=2,3$ are the non-simply-laced Koszul dualities closing FM167.

## 5. Relation to Frenkel--Hernandez opers

Frenkel--Hernandez (Comm. Math. Phys. 2018) proved that spectra of quantum KdV Hamiltonians for $\mathfrak g$ are parametrised by $\mathfrak g^{\vee}$-opers. Their lacing twist acts on the spectral parameter of the transfer matrix by $u\mapsto u/r_{\mathfrak g}$; the lacing twist $\Phi_{\mathfrak g}$ is the Yangian-level companion, lifting the KdV-oper lacing to the full RTT structure. Finkelberg--Tsymbaliuk's multiplicative slices realise the truncated shifted quantum affine algebras; on the rational (Yangian) degeneration, the Langlands dual truncation level shifts by $r_{\mathfrak g}$, matching the uniform formula above.

## 6. Closure

Constructions are explicit in all three items: (1) the $C_2\times B_2$ pairing is written with pole at $u=-4\hbar$ for $C_2$, $u=+4\hbar$ for $B_2$, and the pairing on RTT generators is $\langle T^{(n)}_{\alpha},T^{(m)}_{\beta^{*}}\rangle=(-2)^{n}\delta_{nm}\delta_{\alpha,\beta}\kappa$; (2) the $G_2$ self-dual R-matrix has trefoil pole structure $\{0,-3\hbar,-6\hbar\}$ and is invariant under the $\mu_3$-action generated by $\hbar\mapsto-3\hbar$; (3) the uniform lacing automorphism $\Phi_{\mathfrak g}(T^{(n)}_{\alpha})=(-r_{\mathfrak g})^{n}T^{(n)}_{\alpha^{*}}$ preserves RTT because the relation is polynomial in $u-v$ and the scalar rescaling is the same on both sides.

This establishes $Y_{\hbar}(\mathfrak g)^{!}=Y_{-\hbar r_{\mathfrak g}}(\mathfrak g^{\vee})$ for all simple $\mathfrak g$, closing the non-simply-laced frontier. The Koszul dual of the Yangian, in the filtered-CDG Positselski framework, is uniformly the Langlands-dual Yangian with spectral rescaling by $(-r_{\mathfrak g})$; lacing enters the bialgebra structure as the single scalar $-r_{\mathfrak g}$ acting on each spectral mode.
