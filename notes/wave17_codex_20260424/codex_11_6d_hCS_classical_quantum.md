# 6D hCS Classical BV and Quantum Observables
Date: 2026-04-24  
Author: Raeez Lorgat

## 1. Brutal Adversarial Findings

- **Shift law, \(d=5\). VERDICT: WRONG.** Serre duality for the hCS master field \(\Omega^{0,\bullet}(X,\mathfrak g)[1]\) on a complex \(m\)-fold pairs \(p+q=m\), hence gives symplectic degree \(2-m\); for \(m=3\) this is \(-1\) (Costello--Li, arXiv:1905.09269, Sec. 2.1). The table \((2,-2),(3,-1),(4,0),(5,+1)\) is not CPTVV Sec. 3. CPTVV define \(n\)-shifted Poisson structures and identify the nondegenerate ones with \(n\)-shifted symplectic structures (CPTVV, arXiv:1506.03699, Sec. 3). "\(E_5\)-Poisson" is programme shorthand, not a CPTVV term.

- **Bochner--Martinelli coefficient on \(\mathbb C^3\). VERDICT: CORRECT-WITH-CAVEAT.** The primary normalization is \((n-1)!/(2\pi i)^n\); at \(n=3\) this is \(2/(2\pi i)^3\), with sign controlled by the ordering of \(d\bar z\) and \(dz\) factors (Range, *Holomorphic Functions and Integral Representations*, 1986, Ch. IV; Krantz, *Function Theory of Several Complex Variables*, 1992). The wave formula has the right scalar coefficient, but its orientation convention must be fixed before using it in an OPE coefficient.

- **Flat non-abelian 3-dualizability. VERDICT: UNVERIFIED.** Infinite-dimensional \(HH^\bullet_{E_3}\) would obstruct finite Morita dualizability, but the cited Gwilliam--Williams 2021 Prop. 5.3.2 anchor does not verify the displayed \(HH^0=\mathbb C[[\tau_1,\tau_2,\tau_3]]\) claim in the checked primary surface. Compact \(X\) gives finite Dolbeault cohomology, not automatic 3-dualizability.

- **Anomaly vs wave-function. VERDICT: CORRECT-WITH-CAVEAT.** The mechanism split is correct: anomaly is a QME obstruction class; wave-function renormalisation is a counterterm/rescaling in the effective action (Costello--Gwilliam, *Factorization Algebras in QFT*, Vols. 1--2). The wave anomaly formula is wrong: Costello--Li compute the complex-dimension-three open anomaly from the quartic adjoint invariant \(\mathrm{Tr}_{ad}(A F_A^3)\), with Green--Schwarz cancellation governed by quartic trace factorisation, not by a cubic \(d^{abc}\) coefficient (Costello--Li, arXiv:1905.09269, Sec. 3.2).

## 2. Frontier Push

- **6D hCS to 4D \(\mathcal N=2\) \(\Omega\)-background. VERDICT: WRONG AS STATED; CONDITIONAL BRIDGE EXISTS.** Costello--Yagi start from a six-dimensional topological--holomorphic twist of maximally supersymmetric Yang--Mills on \(M\times C\), not bare hCS on \(\mathbb C^3\). The \(\Omega\)-deformation on \(\mathbb R^2\subset M\) produces four-dimensional Chern--Simons theory on \(\Sigma\times C\); string dualities then relate this to standard \(\Omega\)-deformed gauge-theory systems (Costello--Yagi, ATMP 24 (2020), Secs. 2--4). Costello 2013 and Costello--Witten--Yamazaki 2017--18 control Yangian/RTT outputs, not a direct equality \(Obs_{\mathrm{hCS}}(\mathbb C^3)=Z_{\mathrm{Nek}}(\epsilon_1,\epsilon_2,q,m)\).

- **Gwilliam--Williams parameters. VERDICT: UNVERIFIED AS CITED.** If the formal ring \(\mathbb C[[\tau_1,\tau_2,\tau_3]]\) is retained, the \(\tau_i\) must be treated as formal equivariant/Hopf/\(\Omega\)-background parameters, or logarithms of \(q_i\), not moduli of the rigid target \(\mathbb C^3\). The Calabi--Yau volume-preserving slice imposes \(\tau_1+\tau_2+\tau_3=0\).

## 3. Contradictions Flagged in `waves_11_through_16.tex`

- `/Users/raeez/calabi-yau-quantum-groups/notes/platonic_synthesis_waves_11_through_16.tex:89-96`: false CPTVV attribution and false "Poisson not symplectic" inference.
- `.../platonic_synthesis_waves_11_through_16.tex:124-135`: cubic-Casimir anomaly formula contradicts Costello--Li's quartic-adjoint anomaly; the \(E_6\) safe-list statement is false in this form.
- `.../platonic_synthesis_waves_11_through_16.tex:157-160`: \(K3\times E\) formality-vanishing argument fails; \(\mathrm{At}(T_{K3})\neq 0\), and Kunneth gives \(H^3(K3\times E,\Omega^3)\cong\mathbb C\), not zero.
- `.../platonic_synthesis_waves_11_through_16.tex:167-170`: \(H^{0,3}_{\bar\partial,c}(\mathbb C^3)=\mathbb C\) is false without a translation-invariant/local quotient; Serre duality pairs it with entire holomorphic \(3\)-forms, infinite-dimensional.
- `.../platonic_synthesis_waves_11_through_16.tex:176-180`: compact-CY recovery of non-abelian 3-dualizability is unproved.

## 4. Recommended Programme Actions

1. Replace the shift table by the Serre-duality degree \(2-m\) and a separate CPTVV shifted-Poisson sentence.
2. Rewrite the anomaly theorem around the quartic adjoint invariant; keep \(C_2(\mathfrak g)\) only in the counterterm lane.
3. Locate the exact Gwilliam--Williams \(HH^0\) source or downgrade the dualizability theorem.
4. Recompute \(H^{0,3}_{\bar\partial,c}(\mathbb C^3)\) and the \(K3\times E\) Atiyah obstruction before using either in deformation claims.
5. State the Costello--Yagi bridge as: \(6\)D topological--holomorphic SYM plus \(\Omega\)-deformation \(\Rightarrow\) \(4\)D CS \(\Rightarrow\) Yangian/Nekrasov sector after extra brane and duality data.
