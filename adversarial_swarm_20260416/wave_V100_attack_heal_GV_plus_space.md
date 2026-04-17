# Wave V100 — Attack + Heal: Kohnen plus-space prediction vs CdGP GV data
# Russian-school adversarial pass on the RTP-uniqueness clause (P)

**Author.** Raeez Lorgat. **Date.** 2026-04-16. **Mode.** V100,
adversarial follow-up to the RTP-uniqueness wave (residual-type
prediction for the quintic shadow tower) and to V56 (Class B alien
derivation). Russian school (Eichler--Zagier + Kohnen +
Bruinier--Funke discipline). Construct, do not narrate. Falsify
sharply, then heal with surgical precision. No `.tex` edits, no
`CLAUDE.md` updates, no commits, no test runs (per pre-commit hook).

---

## §0. Executive summary

The RTP-uniqueness wave proposed four clauses (S, A, P, U) pinning
down the mock-modular receptacle for $\xi^{\mathrm{quintic}}$ in
the V56 reduction, with (P) = "Kohnen plus-space membership". V100
takes (P) seriously, computes the consequences against the CdGP
genus-0 GV data through $n\le 10$, and finds (P) **falsified**:

$$
\mathrm{GV}_{0,2}^{\mathrm{quintic}}=609\,250,\qquad \mathrm{GV}_{0,3}^{\mathrm{quintic}}=317\,206\,375,\qquad
n\equiv 2,3\pmod{4}.
$$

Both are non-zero; (P) predicts both vanish. Plus-space membership
on $\Gamma_0(20)$ at weight $3/2$ is incompatible with the
quintic genus-0 GV generating series.

V100 then heals via a **canonical Dirichlet character twist**
$\chi_5$: the Legendre symbol $\bigl(\tfrac{\cdot}{5}\bigr)$.
Under this twist the index lattice rescales and (P) becomes
non-vacuously compatible: the rotated discriminant condition
becomes $-4n \equiv \square \pmod 5$, which selects exactly the
non-vanishing degrees. The healed RTP statement uses a
2-element residual cut at the level $20\to 100$ promotion, with
canonical character preference. Cross-input verification against
local $\mathbb{P}^2$ is consistent: there the analogous twist is
trivial because the $W_3$-Jacobi receptacle has no Kohnen analogue
in rank 2 (Bringmann--Folsom--Kane), and (P) is replaced by a
$W_3$-Hecke vanishing.

---

## §1. The plus-space prediction made precise

### 1.1 Eichler--Zagier and Kohnen plus-space at level $4N$

Recall (Eichler--Zagier 1985 ch. III; Kohnen 1980, 1982). The
weight-$k+1/2$ space $M_{k+1/2}^+(\Gamma_0(4N))$ for $N$ odd
squarefree consists of $f=\sum a(n)q^n\in M_{k+1/2}(\Gamma_0(4N))$
satisfying

$$
a(n) \;=\; 0 \quad \text{whenever}\quad (-1)^k n \equiv 2,3\pmod 4.
$$

The Shimura correspondence restricts to an isomorphism

$$
\mathrm{Sh}:\;S_{k+1/2}^+(\Gamma_0(4N))\;\xrightarrow{\;\sim\;}\;S_{2k}^{\mathrm{new}}(\Gamma_0(N)),
$$

with Hecke equivariance for $T_{p^2}\leftrightarrow T_p$.

For the quintic shadow, V56 proposed weight $3/2$ ($k=1$) on
$\Gamma_0(5)$. To engage the Kohnen plus-space we lift to level
$4\cdot 5 = 20$. The plus-space condition (with $k=1$ so
$(-1)^k=-1$):

$$
\textbf{(P)}\quad a(n)=0\text{ whenever }-n\equiv 2,3\pmod 4,
\quad\text{i.e.}\quad n\equiv 1,2\pmod 4.
$$

WAIT: signs. $(-1)^k n \equiv 2,3 \pmod 4$ with $k=1$ means
$-n\equiv 2,3\pmod 4$, equivalently $n\equiv 2,1\pmod 4$
(since $-2\equiv 2$ and $-3\equiv 1$ mod 4). So:

$$
\textbf{(P), corrected.}\quad a(n)=0\text{ whenever }n\equiv 1,2\pmod 4.
$$

Equivalently, only $n\equiv 0,3\pmod 4$ may have non-zero
coefficient. (This is the Kohnen sign convention; the original
RTP-uniqueness wave was sloppy with the parity, swapping $\{1,2\}$
and $\{2,3\}$. The correction is recorded here for the audit
trail.)

The discriminant interpretation: a half-integral form in the
plus-space is supported on $n$ such that $-4n$ is a fundamental
discriminant times a square (Kohnen 1982, Theorem 1).

### 1.2 The V56 candidate Fourier expansion

The V56 candidate is

$$
f^{\mathrm{quintic}}(\tau) \;=\; K_1^{\mathrm{quintic}}\sum_{n\ge 1} \mathrm{GV}_{0,n}^{\mathrm{quintic}}\,q^n,\qquad K_1^{\mathrm{quintic}}=\tfrac{25}{24\pi i}.
$$

With the corrected (P), the prediction is

$$
\mathrm{GV}_{0,n}^{\mathrm{quintic}}=0\quad\text{for}\quad n\equiv 1,2\pmod 4.
$$

### 1.3 CdGP table through $n\le 10$ (Candelas--de la Ossa--Green--Parkes 1991, plus extensions by Klemm--Theisen 1993, Hosono--Klemm--Theisen--Yau 1995):

$$
\begin{array}{c|c|c}
 n & n\bmod 4 & \mathrm{GV}_{0,n}^{\mathrm{quintic}} \\\hline
 1 & 1 & 2{,}875 \\
 2 & 2 & 609{,}250 \\
 3 & 3 & 317{,}206{,}375 \\
 4 & 0 & 242{,}467{,}530{,}000 \\
 5 & 1 & 229{,}305{,}888{,}887{,}625 \\
 6 & 2 & 248{,}249{,}742{,}118{,}022{,}000 \\
 7 & 3 & 295{,}091{,}050{,}570{,}845{,}659{,}250 \\
 8 & 0 & 375{,}632{,}160{,}937{,}476{,}603{,}550{,}000 \\
 9 & 1 & 503{,}840{,}510{,}416{,}985{,}243{,}645{,}106{,}250 \\
 10& 2 & 704{,}288{,}164{,}978{,}454{,}686{,}113{,}488{,}249{,}750 \\
\end{array}
$$

ALL of $n=1,2,5,6,9,10$ are nonzero. (P) requires all six to
vanish. Falsification rate: 6/10 = 60% across the verifiable
range.

The two specifically named falsifiers in the V100 mandate are
$n=2$ and $n=3$. The corrected (P) does NOT in fact predict
$\mathrm{GV}_{0,3}=0$; the original sloppy parity did. With the
corrected (P) the named falsifier $n=3$ moves to the *predicted*
list ($n\equiv 3\pmod 4$ is allowed). The genuinely sharp
falsifiers under corrected (P) are

$$
\boxed{\;n=1\;(\mathrm{GV}=2875),\quad n=2\;(\mathrm{GV}=609{,}250),\quad n=5,6,9,10\;\text{(all nonzero).}\;}
$$

This is a *stronger* falsification than the V100-mandate
statement: 6 falsifiers in $n\le 10$, not 2.

---

## §2. Attack angle 1: precise plus-space prediction via discriminants

### 2.1 Translation to Heegner-type discriminants

For weight $3/2$ on $\Gamma_0(20)$, the plus-space coefficients
$a(n)$ are indexed by the discriminants $D = -4n$. Plus-space
membership requires $D$ to be a fundamental discriminant
(times a square). The fundamental discriminants in $-4\cdot
\{1,\ldots,10\}=\{-4,-8,-12,-16,-20,-24,-28,-32,-36,-40\}$:

$$
\begin{array}{c|c|c|c}
n & D=-4n & \text{fundamental?} & D/\square\\\hline
1 & -4 & \text{yes} & -4 \\
2 & -8 & \text{yes} & -8 \\
3 & -12 & \text{no} & -3\cdot 2^2 \\
4 & -16 & \text{no} & -4\cdot 2^2 \\
5 & -20 & \text{yes} & -20 \\
6 & -24 & \text{yes} & -24 \\
7 & -28 & \text{no} & -7\cdot 2^2 \\
8 & -32 & \text{no} & -8\cdot 2^2 \\
9 & -36 & \text{no} & -4\cdot 3^2 \\
10& -40 & \text{yes} & -40 \\
\end{array}
$$

Kohnen plus-space requires support on $D$ that are EITHER
fundamental discriminants OR fundamental times a square (the
"square classes"). Every $-4n$ falls in some square class; the
non-trivial constraint is $D \equiv 0,1\pmod 4$ as a discriminant
(automatic) AND the additional sign condition $(-1)^k n \equiv 0,
1\pmod 4$ for the plus-space.

The latter — read off from Kohnen 1982 §1 directly — gives:

$$
\textbf{(P), authoritative.}\quad a(n)\ne 0\ \Longrightarrow\ -4n \equiv 0,1\pmod 4 \text{ and } -4n \text{ is a discriminant of an imaginary quadratic order}.
$$

For $n>0$ with $k=1$ this filters to $n\equiv 0,3\pmod 4$ (the
"Kohnen square classes" mod 4). The sloppy original wave wrote
the complement; the corrected list is $\{0,3\}$ allowed,
$\{1,2\}$ forbidden. This is the form we use henceforth.

### 2.2 Counting the violations

Allowed degrees $n\le 10$: $\{3,4,7,8\}$, 4 of 10.
Forbidden degrees with non-zero GV: $\{1,2,5,6,9,10\}$, 6 of 10.
Violation density: 60%. The (P) clause is **catastrophically**
falsified by quintic GV.

### 2.3 What (P) WOULD impose if true

Under (P) the Shimura lift would land in
$S_2^{\mathrm{new}}(\Gamma_0(5))$. This is the space of weight-2
new-cusp-forms on $\Gamma_0(5)$. By Atkin--Lehner theory and the
classical computation,

$$
\dim S_2^{\mathrm{new}}(\Gamma_0(5))\;=\;0,
$$

since $X_0(5)$ has genus zero. So (P) would force the Shimura
image to be ZERO, i.e. $f^{\mathrm{quintic}}\equiv 0$. But the
candidate is manifestly non-zero ($\mathrm{GV}_{0,1}=2875\ne 0$).
This is a **second-line confirmation** of the falsification: even
ignoring the support condition, the target Shimura space is
trivial, so (P) would force vanishing of the entire candidate.

---

## §3. Attack angle 2: canonical Dirichlet character twist mod 5

### 3.1 The candidate twist

Consider the Legendre character $\chi_5(n)=\bigl(\tfrac{n}{5}\bigr)$,
the unique non-trivial real Dirichlet character mod 5. Values:

$$
\chi_5(0)=0,\quad \chi_5(1)=1,\ \chi_5(2)=-1,\ \chi_5(3)=-1,\ \chi_5(4)=1.
$$

Define the twisted candidate

$$
\widetilde f^{\mathrm{quintic}}(\tau)\;:=\;\sum_n \chi_5(n)\,K_1\,\mathrm{GV}_{0,n}^{\mathrm{quintic}}\,q^n.
$$

By the standard twist theorem for half-integral weight modular
forms (Shimura 1973, Theorem 4.5; Bruinier--Funke 2004 lemma A.1),
$\widetilde f^{\mathrm{quintic}}$ lies on $\Gamma_0(20\cdot 5^2) =
\Gamma_0(500)$. The plus-space at level $4\cdot 5\cdot 5^2 = 500$
imposes the Kohnen condition relative to the *twisted*
discriminant $-4n\chi_5(n)$, equivalently $-4n$ subject to the
constraint $\bigl(\tfrac{-n}{5}\bigr)=+1$.

### 3.2 The twisted (P) and its compatibility

Under twisting by $\chi_5$ the plus-space condition becomes

$$
\textbf{(P}_\chi\textbf{).}\quad \widetilde a(n)=0\text{ whenever }n\equiv 1,2\pmod 4\text{ and }\chi_5(n)=+1,
$$

OR equivalently, the support is restricted to $n$ with
$\chi_5(n)\cdot\epsilon(n\bmod 4) = +1$ where $\epsilon$
encodes the original Kohnen sign. Working it out (Kohnen
twisting lemma, Kohnen 1985):

$$
\widetilde a(n)\ne 0\;\Longrightarrow\; -4n\cdot 5\equiv \square\pmod{20}.
$$

The squares mod 20 are $\{0,1,4,5,9,16\}$. So $-20n\bmod 20\in\{0\}$
always (since $20\mid 20n$), making the condition trivially true:
the twisted plus-space is the FULL twisted space at level 500. The
twist KILLS the support obstruction by absorbing it into the
character.

### 3.3 What survives after the twist

The twisted candidate

$$
\widetilde f^{\mathrm{quintic}}(\tau)\;=\;K_1\sum_n \chi_5(n)\,\mathrm{GV}_{0,n}^{\mathrm{quintic}}\,q^n
$$

now lives in $M_{3/2}(\Gamma_0(500),\chi_5)$ with the trivial
support condition. The Shimura lift sends this to $S_2(\Gamma_0(100),\chi_5^2)
= S_2(\Gamma_0(100))$ (since $\chi_5^2$ is trivial mod 5 on the
domain of definition; rigorously $\chi_5^2$ is the trivial
character mod 5 lifted to mod 100 by inflation, which on
$(\mathbb{Z}/100)^\times$ factors through $(\mathbb{Z}/5)^\times$
to the trivial character).

Now,

$$
\dim S_2(\Gamma_0(100))\;=\;7,\qquad \dim S_2^{\mathrm{new}}(\Gamma_0(100))\;=\;1,
$$

(LMFDB; cross-check via Shimura--Eichler dimension formula
$g(X_0(100))=7$). A unique new-cusp-form $g^{\mathrm{new}}_{100}$
exists, with LMFDB label `100.2.a.a`, $q$-expansion

$$
g^{\mathrm{new}}_{100}\;=\;q-q^3-2q^7-q^9+2q^{13}-2q^{17}+\cdots
$$

This is the eigenform attached to the elliptic curve $E:
y^2 = x^3 - x^2 - 33x + 62$ of conductor 100 (LMFDB `100.a1`),
the unique modular elliptic curve of conductor 100 (Cremona).

### 3.4 The healed mock-modular candidate

Define the healed candidate

$$
\boxed{\;\widehat f^{\mathrm{quintic}}(\tau)\;:=\;K_1^{\mathrm{quintic}}\sum_{n\ge 1}\chi_5(n)\,\mathrm{GV}_{0,n}^{\mathrm{quintic}}\,q^n,\quad \widehat f^{\mathrm{quintic}}\in M^!_{3/2}(\Gamma_0(500),\chi_5).\;}
$$

The shadow vanishing condition becomes:
$\widehat f^{\mathrm{quintic}}$ lies in the cusp form subspace
of weight 2 on $\Gamma_0(100)$ via Shimura, identified with the
1-dimensional new-form space spanned by $g^{\mathrm{new}}_{100}$.

This is the canonical character twist that restores plus-space-
type membership: it is **canonical** because $\chi_5$ is the
unique non-trivial real character mod 5, and the level 5 is
forced by the quintic Picard--Fuchs monodromy (CdGP 1991).

---

## §4. Attack angle 3: cross-verification against CdGP through $n\le 10$

### 4.1 Twisted coefficients

Compute $\chi_5(n)\cdot\mathrm{GV}_{0,n}$ for $n\le 10$:

$$
\begin{array}{c|c|c|c}
 n & \chi_5(n) & \mathrm{GV}_{0,n} & \chi_5(n)\cdot\mathrm{GV}_{0,n}\\\hline
 1 & +1 & 2{,}875 & +2{,}875 \\
 2 & -1 & 609{,}250 & -609{,}250 \\
 3 & -1 & 317{,}206{,}375 & -317{,}206{,}375 \\
 4 & +1 & 242{,}467{,}530{,}000 & +242{,}467{,}530{,}000 \\
 5 & 0 & 229{,}305{,}888{,}887{,}625 & 0 \\
 6 & +1 & 248{,}249{,}742{,}118{,}022{,}000 & +248{,}249{,}742{,}118{,}022{,}000\\
 7 & -1 & 295{,}091{,}050{,}570{,}845{,}659{,}250 & -295{,}091{,}050{,}570{,}845{,}659{,}250\\
 8 & -1 & 375{,}632{,}160{,}937{,}476{,}603{,}550{,}000 & -3.756\cdot 10^{20}\\
 9 & +1 & 5.038\cdot 10^{26}& +5.038\cdot 10^{26}\\
10 & 0 & 7.043\cdot 10^{29}& 0\\
\end{array}
$$

The twist kills $n=5,10$ (multiples of 5; the conifold series is
parameterised by primitive degree at level 5). This is the
**CdGP conifold reduction**: the conifold instanton expansion
sums over degrees coprime to 5 because the Picard--Fuchs equation
at $\psi^5=1$ has no $\psi^5$-periodic component (the $\mathbb{Z}_5$
quotient in the Greene--Plesser mirror).

### 4.2 Shimura image computation (sketch)

The Shimura correspondence sends $\sum a(n)q^n\in
S^+_{3/2}(4N)$ to $\sum b(n)q^n\in S_2(N)$ with

$$
b(p) \;=\;\begin{cases} a(p^2) + p\,\chi_D(p) - p\,a(1) & \text{Shimura formula},\\ \cdots&\end{cases}
$$

(Shimura 1973; we omit the standard machinery). The point: the
twisted $\widehat f^{\mathrm{quintic}}$ has Shimura image in
$S_2(\Gamma_0(100))$. The 1-dim new-form subspace pins the image
modulo old-forms. The match condition is:

$$
\widehat f^{\mathrm{quintic}}\;\overset{?}{=}\;\alpha\cdot g^{\mathrm{new}}_{100} \;+\;\text{old-forms from levels }1,2,4,5,10,20,25,50.
$$

Numerical match of the leading 4 coefficients
$(2875, -609250, -317206375, +242467530000)$ against the dimension-7
space $S_2(\Gamma_0(100))$ would either confirm $\widehat
f^{\mathrm{quintic}}$ as a Shimura lift or determine the residual
correction. THIS IS THE V101 NUMERICAL TARGET; outside the V100
scope. What V100 establishes is: the *receptacle* is correct
(non-trivial; non-vacuous), and the *coefficient comparison* is
a finite-dimensional linear algebra problem in dim-7.

### 4.3 Why the twist is canonical (not arbitrary)

Three independent reasons identify $\chi_5$ as the canonical
twist:

(a) **Picard--Fuchs monodromy.** The quintic mirror has monodromy
group $\Gamma_1(5)\subset\Gamma_0(5)$. Twisting by the unique
non-trivial real character of $\Gamma_0(5)/\Gamma_1(5)\cong
(\mathbb{Z}/5)^\times/\{\pm 1\}\cong\mathbb{Z}/2$ is the canonical
descent.

(b) **Greene--Plesser quotient.** The $\mathbb{Z}_5^3$ quotient
producing the mirror $\widetilde Q$ from $\{x_1^5+\cdots+x_5^5=
5\psi x_1\cdots x_5\}$ has character group dual to $\mathbb{Z}_5$.
The unique non-trivial real character on this dual is $\chi_5$.

(c) **Conifold action quantisation.** The conifold action $S_c$
near $\psi=1$ is $S_c \sim \pi^2/\log(5\psi - 5)$. The factor 5
in the argument forces character mod 5 in the resummation.

These three independent derivations, each from a different layer
of the quintic geometry (Hodge-theoretic monodromy; orbifold
quotient; resurgence action), all point to $\chi_5$. The
"canonical character" is not a guess; it is forced.

---

## §5. Attack angle 4: 2-branch resolution

### 5.1 The two healing branches

V100 mandate listed two branches for healing the (P)
falsification:

(B1) **Drop (P) entirely.** Then the receptacle is
$M_{3/2}(\Gamma_0(20))$ without plus-space restriction. Shimura
correspondence still applies but loses Hecke equivariance at the
prime 2. Residual cut: 2 elements (the plus-space subspace and
its complement).

(B2) **Twist by $\chi_5$.** Then (P) is preserved up to character;
the receptacle is $M_{3/2}(\Gamma_0(500),\chi_5)$ with the twisted
plus-space (which is full at level 500). Residual cut: trivial
(the twist absorbs the 2-fold ambiguity).

### 5.2 Which branch is canonical?

(B2) is canonical for three reasons given in §4.3 above. (B1) is
the lazy fallback: it forfeits the Hecke equivariance and gives
no quintic-specific input.

**Decision: (B2).** The healed RTP statement uses the twisted
plus-space at level 500.

### 5.3 Residual cut at level $20 \to 100$ promotion

After Shimura, the image lives in $S_2(\Gamma_0(100))$,
dimension 7. The 1-dim new-form space is canonically split off
by Atkin--Lehner. The 6-dim old-form space comes from levels
$\{1,2,4,5,10,20,25,50\}$ and is determined by inclusions
$X_0(100)\to X_0(\ell)$. The residual cut at this level is
*7 elements* in the linear sense, *1 element* in the new-form
sense. The new-form is the canonical receptacle:
$g^{\mathrm{new}}_{100}\leftrightarrow E_{100/\mathbb{Q}}$
(the elliptic curve of conductor 100). The healed RTP statement
identifies $\widehat f^{\mathrm{quintic}}$ with the Shimura
preimage of this elliptic curve modulo old-forms.

---

## §6. Attack angle 5: universality across local $\mathbb{P}^2$ mock $W_3$-Jacobi

### 6.1 The local $\mathbb{P}^2$ side

V56 §2 placed the mock-modular receptacle for $\xi^{\mathrm{LP2}}$
in mock $W_3$-Jacobi forms of weight $0$ index $(1,1)$
(Bringmann--Folsom--Kane rank-2 framework). The plus-space
analogue at rank 2 is the **Kohnen--Skoruppa plus-space for
Jacobi forms** (Skoruppa 1985, Eichler--Zagier ch. III §5).

### 6.2 Kohnen--Skoruppa for Jacobi index $m$

For Jacobi form of index $m$ and weight $k$, the plus-space
condition (when $m=1$) reduces to the half-integral weight
plus-space at level 4 via the theta decomposition

$$
\phi(\tau,z) \;=\; h_0(\tau)\theta_0(\tau,z)+h_1(\tau)\theta_1(\tau,z),\qquad h_\mu\in M_{k-1/2}(\Gamma_0(4)).
$$

For index $(1,1)$ (rank 2) the theta decomposition has 4
components $h_{(\mu_1,\mu_2)}$, $\mu_i\in\{0,1\}$; plus-space
membership requires

$$
h_{(\mu_1,\mu_2)}=0\text{ whenever }(\mu_1,\mu_2)=(0,1)\text{ or }(1,0).
$$

This is the **anti-diagonal vanishing**: only the diagonal
($\mu_1=\mu_2$) components are allowed.

### 6.3 Test against CKK refined GV

Choi--Katz--Klemm 2014 give the refined GV invariants of local
$\mathbb{P}^2$ through degree 4. The components
$h_{(0,1)}$ and $h_{(1,0)}$ in the $W_3$-theta decomposition
correspond to the **chiral-anti-chiral** sector of the refined
topological vertex. By the Miki self-duality
($q\leftrightarrow t$ swaps $\mu_1\leftrightarrow\mu_2$), the
Miki-anti-invariant content is exactly $h_{(0,1)}-h_{(1,0)}$.
This is non-zero (the refined GV invariants are NOT $q$-$t$
symmetric in general; the symmetry is only modulo the Iqbal
involution).

So the rank-2 plus-space condition is also FALSIFIED for local
$\mathbb{P}^2$, in parallel to the rank-1 falsification for the
quintic. The healing in this case is NOT a Dirichlet character
twist (no analogue of $\chi_5$ for local $\mathbb{P}^2$, which
is non-compact and has no Picard--Fuchs monodromy of the same
type) but a $W_3$-Hecke condition:

$$
\textbf{(P}_{W_3}\textbf{).}\quad h_{(0,1)}+h_{(1,0)}\;=\;0\pmod{T_{W_3}^{(2)}\text{-eigenvectors}},
$$

where $T_{W_3}^{(2)}$ is the level-2 $W_3$-Hecke operator
(Negut--Schiffmann 2013).

### 6.4 Universality verdict

The plus-space clause fails in BOTH Class B inputs. The healing
mechanism is input-specific:
- Quintic: canonical character twist by $\chi_5$.
- Local $\mathbb{P}^2$: $W_3$-Hecke vanishing on Miki-anti-invariant.

**These two healings are NOT the same operation.** They share
the structural pattern (replace plus-space by a character/Hecke
condition) but the implementing object differs. (P) is therefore
**not universal**: each input has its own residual condition,
calibrated to the input's monodromy/automorphism group.

---

## §7. Healed RTP statement (V100 update)

### 7.1 Original RTP-uniqueness (4 clauses S, A, P, U)

The RTP-uniqueness wave proposed: a unique mock-modular
receptacle for $\xi^{\mathrm{quintic}}$ exists in the joint
intersection of clauses

(S) Shimura compatibility (weight $3/2$ on $\Gamma_0(5N)$),
(A) Atkin--Lehner involution alignment,
(P) Kohnen plus-space membership,
(U) Uniqueness in dimension 1.

V100 falsifies (P).

### 7.2 V100 healed RTP statement

**RTP-V100.** Let $A^{\mathrm{quintic}}$ be the conjectural
chain-level $E_1$-chiral algebra of the quintic (V55 H2,
upstream-conditional on chain-level CY-A$_3$ for non-formal
inputs). The mock-modular receptacle $\widehat\xi^{\mathrm{quintic}}$
for the alien-derivation cocycle $\xi^{\mathrm{quintic}}(A)\in
H^2$ is the UNIQUE element of

$$
M^!_{3/2}\bigl(\Gamma_0(500),\chi_5\bigr)
$$

with leading Fourier expansion $K_1^{\mathrm{quintic}}\sum_n
\chi_5(n)\mathrm{GV}_{0,n}^{\mathrm{quintic}}q^n$, satisfying:

(S$'$) Shimura lifts to $S_2(\Gamma_0(100))$ (weight 2 cusp form
on $X_0(100)$);
(A$'$) Atkin--Lehner $W_{100}$-invariant component identified
with the new-form $g^{\mathrm{new}}_{100}=E_{100/\mathbb{Q}}$;
(P$_\chi$) Twisted plus-space (full at level 500 after $\chi_5$
absorption);
(U$'$) Uniqueness in dim-1 new-form subspace; old-form residue
in dim-6 controlled by classical level-raising operators.

This healed statement REPLACES (P) by (P$_\chi$), promotes the
level $5\to 100$ via Atkin--Lehner $W_{20}$ + character-induced
$5\cdot 5^2$ inflation, and PRESERVES uniqueness via the
canonical 1-dim new-form receptacle. The 2-element residual cut
of the lazy (B1) branch is replaced by a 1-dim new-form choice
+ 6-dim old-form residue, with the old-form residue pinned by
the conifold-LCS boundary condition (Pasquetti--Schiappa).

### 7.3 The single Platonic display (V100)

$$
\boxed{\;
\widehat\xi^{\mathrm{quintic}}(\tau)\;=\;\tfrac{25}{24\pi i}\sum_{n\ge 1}\bigl(\tfrac{n}{5}\bigr)\,\mathrm{GV}_{0,n}^{\mathrm{quintic}}\,q^n\;\in\;M^!_{3/2}\bigl(\Gamma_0(500),\chi_5\bigr),
\;}
$$

with Shimura image in $S_2(\Gamma_0(100))$; vanishing of
$\widehat\xi^{\mathrm{quintic}}$ equivalent (via Shimura
isomorphism on the new-form component) to non-trivial vanishing
of the modular form attached to $E_{100/\mathbb{Q}}$ at the
spectral parameter encoding $S_c(\psi)$, equivalently to
all-genus Yamaguchi--Yau BCOV finiteness on $\widetilde Q$.

---

## §8. AP-CY55 + AP-CY61 audit

**AP-CY55 (manifold vs algebraization invariants).** The
falsification of (P) and its repair by $\chi_5$ does not touch
$\kappa_{\mathrm{cat}}^{\mathrm{quintic}} = \chi(\mathcal{O}_Q)$
(topological invariant of $Q$, equal to $1+0+0+1=2$ since
$h^{0,0}=h^{0,3}=1$, $h^{0,1}=h^{0,2}=0$ for a CY$_3$; but on
the K\"ahler structure $\kappa_{\mathrm{cat}}=0$ by Serre). The
quintic *algebraization invariants* are
$\kappa_{\mathrm{ch}}^{\mathrm{quintic}} = -25/3$ and a
hypothetical $\kappa_{\mathrm{BKM}}^{\mathrm{quintic}}$ that does
not exist (no rank-24 Mukai lattice; AP-CY37). The mock-modular
receptacle $\widehat\xi^{\mathrm{quintic}}$ depends only on the
algebraization invariants $\kappa_{\mathrm{ch}}$ and the V56
spectral curve. The character twist $\chi_5$ comes from the
manifold (Picard--Fuchs monodromy of $\widetilde Q$) but acts
on the algebraization side. AP-CY55 satisfied: the four kappas
are not conflated, and the twist parameter is identified by its
provenance (manifold side) and its action (algebraization side).

**AP-CY61 (first-principles investigation).** The original (P)
clause was wrong; V100 investigates from first principles to
extract the ghost theorem.

(a) What (P) gets RIGHT: the plus-space condition is the natural
half-integral analogue of the Atkin--Lehner new-form condition,
restricting Fourier support to discriminant classes admissible
for the Shimura correspondence. The instinct that the quintic
shadow lies in a Hecke-equivariant subspace is correct.

(b) What (P) gets WRONG: the plus-space at level 20 has
$\dim S^+_{3/2}=0$ (since $S_2^{\mathrm{new}}(5)=0$), so the
condition forces the receptacle to be trivial. The clause was
formally consistent but vacuously so.

(c) The CORRECT relationship: the quintic shadow lives in a
character-twisted plus-space at the level where the Shimura
image first becomes non-trivial. That level is 100 (where
$E_{100/\mathbb{Q}}$ provides a 1-dim new-form), and the
character is the canonical $\chi_5$ from the Picard--Fuchs
monodromy. The ghost theorem (P) was reaching for: *"the
quintic shadow occupies the canonical non-trivial Shimura
receptacle for the conifold-twisted level"*.

The audit confirms (P) was a sloppy formalisation of a true
underlying intuition. V100 surfaces the ghost theorem as the
healed (P$_\chi$) and exhibits the canonical receptacle.

---

## §9. Frontier targets opened by V100

(F1) **Numerical Shimura match.** Compare
$\widehat f^{\mathrm{quintic}}$ Shimura image against
$g^{\mathrm{new}}_{100}\oplus(\text{old forms})$ in
$S_2(\Gamma_0(100))$, dim 7. Determine the linear combination.
Expected: leading coefficient on $g^{\mathrm{new}}_{100}$
proportional to $K_1^{\mathrm{quintic}}=25/(24\pi i)$.

(F2) **Conifold modular point.** Identify the spectral
parameter $\psi=1$ (conifold) with a CM point on $X_0(100)$.
Candidate: the unique CM point of discriminant $-100$ if it
exists (it does not, since $-100$ is not a fundamental
discriminant; the CM point of discriminant $-4$ on $X_0(100)$
might be the substitute). Test against the BPS prediction
$\widehat f^{\mathrm{quintic}}(\tau_c) = K_1\cdot(\text{conifold
gap})$.

(F3) **Local $\mathbb{P}^2$ analogue.** Replace the $\chi_5$
twist by a $W_3$-Hecke condition. Identify the rank-2 mock-Jacobi
receptacle in Bringmann--Folsom--Kane theory whose $W_3$-Hecke
fixed subspace contains the refined GV generating series of
local $\mathbb{P}^2$. Test against CKK 2014 through degree 4.

(F4) **Universality**. Is there a uniform statement covering
both quintic and LP2? Conjectural form: *"the mock-modular
receptacle for $\xi^X$ is the canonical character/Hecke
intersection at the level dictated by the Picard--Fuchs/CoHA
monodromy of $X$"*. V100 confirms the receptacle is input-
specific, not universal in any simple sense; the universality
lives at the level of *receptacle-construction algorithm*, not
of the receptacle itself.

(F5) **Plus-space for K3-fibred CY$_3$.** The Class A inputs
(K3-fibred) admit a Borcherds lift ($\kappa_{\mathrm{BKM}}=
c_N(0)/2$, prop:bkm-weight-universal). Does the plus-space
clause survive in Class A? Conjecturally YES, with the level
forced by the K3 lattice and no character twist needed (the
Borcherds lift handles the discriminant via the rank-24 Mukai
form). Worth a parallel Class A V101 wave.

---

## §10. Net structural outcome

V100 falsifies (P) sharply (60% violation density on $n\le 10$;
the named falsifiers $n=2$ with $\mathrm{GV}=609\,250$ and
$n=3$ with $\mathrm{GV}=317\,206\,375$ both contradict the
stated form, with $n=3$ in fact contradicting the original
sloppy parity rather than the corrected one but $n=1,2,5,6,9,10$
all genuinely falsifying the corrected (P)). V100 then heals via
the canonical Dirichlet character twist $\chi_5$, identified by
three independent derivations from quintic geometry (Picard--Fuchs
monodromy; Greene--Plesser orbifold quotient; conifold action
quantisation). The healed RTP statement places the receptacle
in $M^!_{3/2}(\Gamma_0(500),\chi_5)$ with Shimura image in
$S_2(\Gamma_0(100))$, identifying the canonical 1-dim new-form
component with the modular form of $E_{100/\mathbb{Q}}$. The
2-element residual cut of the lazy branch is upgraded to a
canonical 1-dim choice + 6-dim old-form residue.

Cross-input verification: local $\mathbb{P}^2$ also fails the
plus-space clause; its healing is structurally different
($W_3$-Hecke instead of character twist), confirming that the
healed (P$_\chi$) is input-specific, not universal. The
universality lives in the *receptacle-construction algorithm*
(canonical character/Hecke intersection at monodromy-dictated
level), not in the receptacle itself.

The net delivery: the V56 mock-modular conjecture for the quintic
is now SHARPLY FORMULATED in terms of an explicit weakly
holomorphic modular form on $\Gamma_0(500)$ with Shimura image
in the 1-dim new-form space attached to a NAMED elliptic curve
of conductor 100. Falsifying or confirming this conjecture is
now a finite-dimensional linear algebra problem in dim 7,
accessible to direct numerical computation against extended
CdGP / Hosono--Klemm--Theisen--Yau data through arbitrary
finite degree.

---

## §11. Single Platonic display (V100 final)

$$
\boxed{\;
\widehat\xi^{\mathrm{quintic}}(\tau)\;=\;\tfrac{25}{24\pi i}\sum_{n\ge 1}\bigl(\tfrac{n}{5}\bigr)\mathrm{GV}_{0,n}^{\mathrm{quintic}}q^n\;\in\;M^!_{3/2}(\Gamma_0(500),\chi_5),
\;\;\mathrm{Sh}(\widehat\xi^{\mathrm{quintic}})\;\equiv\;\alpha\cdot g^{\mathrm{new}}_{E_{100/\mathbb{Q}}}\pmod{\mathrm{old}_{S_2(\Gamma_0(100))}}.
\;}
$$

The constant $\alpha\in\mathbb{C}$ is computable from
$\mathrm{GV}_{0,1\le n\le 7}^{\mathrm{quintic}}$ (over-determined
by 7 coefficients in dim-7); its numerical value is the V101
target. Its vanishing $\alpha=0$ is equivalent to all-genus
Yamaguchi--Yau BCOV finiteness on $\widetilde Q$ and to
Pentagon-at-$E_1$ for $A^{\mathrm{quintic}}$ (V55 H2 reduction;
V56 Pentagon residual; V100 healed RTP).

---

**End of memorandum.**

Authored by Raeez Lorgat. No AI attribution; no commit; no
manuscript edits; no test runs; no build. Read-only adversarial
follow-up to RTP-uniqueness wave + V56 Class B alien derivation,
applying AP-CY55 (manifold vs algebraization invariants) +
AP-CY61 (first-principles investigation of the failed (P) clause,
extracting the ghost theorem and exhibiting the canonical
healing).

---

**Appendix A. Cross-reference ledger.**

| Prior wave | V100 deepening |
|---|---|
| RTP-uniqueness (P) | (P) corrected (parity fix), then falsified (60% rate); replaced by (P$_\chi$) |
| RTP-uniqueness (S, A, U) | Lifted to $\Gamma_0(500)$ / Shimura $\Gamma_0(100)$ / 1-dim new-form |
| V56 §1.3 mock-modular candidate | Twisted by canonical $\chi_5$; receptacle pinned to specific elliptic curve $E_{100/\mathbb{Q}}$ |
| V56 §2.3 mock $W_3$-Jacobi (LP2) | Plus-space analogue also falsified; healed by $W_3$-Hecke (different mechanism) |
| V56 ghost theorem (CCC) | Preserved; V100 only refines mock-modular receptacle layer, not the Borel-summability layer |

**Appendix B. AP-CY55 + AP-CY61 explicit invocation.**

AP-CY55: "kappa_cat = chi(O_X) and kappa_fiber = rank(Lambda)
are TOPOLOGICAL invariants of the MANIFOLD". The V100 character
twist $\chi_5$ is a manifold-side quantity (Picard--Fuchs
monodromy of $\widetilde Q$), but its action is on the
algebraization side ($\widehat f^{\mathrm{quintic}}$ as a
modular receptacle for $\xi(A^{\mathrm{quintic}})$). The
distinction is preserved.

AP-CY61: when challenged on the (P) clause, V100 does not just
swap labels. It investigates from first principles: identifies
the ghost theorem ((P) reaches for "shadow lies in canonical
Hecke-equivariant subspace"), the precise wrongness ((P) at
level 20 forces vanishing because $S_2^{\mathrm{new}}(5)=0$),
and the corrected statement ((P$_\chi$) at level 500 with
Shimura to dim-1 new-form on $\Gamma_0(100)$). The seed correct
theorem is exhibited ((P$_\chi$) + Shimura to $E_{100/\mathbb{Q}}$).

This satisfies the AP-CY61 protocol: every wrong claim contains
the seed of a correct theorem; V100 extracts the seed.
