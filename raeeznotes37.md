I’m checking the precise passage against the standard bar/cobar–Koszul dictionary, because the apparent contradiction usually comes from two different uses of “dual.”I found the terminology slip: the book is conflating the Koszul dual coalgebra with the Koszul dual algebra, and also blurring the dual object with the bar–cobar resolution.Thought for 20m 20sYes — your instinct is basically right.
The monograph is conflating two different things:


the bar–cobar adjunction, whose counit gives


Ω B(A)≃A\Omega\,B(A)\simeq AΩB(A)≃A
on the Koszul locus (and more generally gives a bar–cobar resolution), and


Koszul duality, where the bar construction of one algebra is identified with the Koszul dual coalgebra of another algebra, and only then can one pass to a dual algebra by an additional duality step. The monograph itself later states this distinction explicitly: bar and cobar are constructions that always exist, while Koszul duality is an extra relationship that only holds for special Koszul pairs. It even summarizes the moral as: “Bar-cobar are tools; Koszul duality is a relationship these tools can detect.”


So the clean way to say it is:


B(A)B(A)B(A) is a coalgebra.


Ω(B(A))\Omega(B(A))Ω(B(A)) is the bar–cobar reconstruction of AAA, not the dual algebra.


If AAA is Koszul, then B(A)B(A)B(A) is quasi-isomorphic to the Koszul dual coalgebra AiA^{\mathrm{i}}Ai (notation varies).


The Koszul dual algebra A!A^!A! is obtained from that dual coalgebra by a further duality/convention-dependent step, not by the plain counit ΩB(A)→A\Omega B(A)\to AΩB(A)→A. This is exactly the way standard references separate the subjects: bar–cobar adjunction is one chapter, quadratic/Koszul duality is another.


That is why, in standard notation, you really want to keep four objects apart:
A,B(A),Ai (dual coalgebra),A! (dual algebra).A,\qquad B(A),\qquad A^{\mathrm{i}} \text{ (dual coalgebra)},\qquad A^! \text{ (dual algebra)}.A,B(A),Ai (dual coalgebra),A! (dual algebra).
For a Koszul algebra,
B(A)≃Ai,Ω(Ai)≃A,B(A)\simeq A^{\mathrm{i}},\qquad \Omega(A^{\mathrm{i}})\simeq A,B(A)≃Ai,Ω(Ai)≃A,
while A!A^!A! is the algebra obtained from AiA^{\mathrm{i}}Ai by dualization/convention. So:
ΩB(A)≃A,\Omega B(A)\simeq A,ΩB(A)≃A,
not A!A^!A!.
In fact, the monograph’s own abstract already gives the right separation in the chiral setting: it says that Verdier duality on Ran exchanges the bar complex of AAA with the bar complex of a second algebra A!A^!A!,
DRan BX(A)≃BX(A!),\mathbb D_{\mathrm{Ran}}\,B_X(A)\simeq B_X(A^!),DRan​BX​(A)≃BX​(A!),
while on the Koszul locus the cobar inverts the bar:
ΩX(BX(A))≃A.\Omega_X(B_X(A))\simeq A.ΩX​(BX​(A))≃A.
So A!A^!A! is coming from a duality on the bar complex, not from the plain cobar counit.
This also explains the Heisenberg confusion. Early on, the book says for HkH_kHk​ that the bar complex is a coLie coalgebra and that applying cobar gives a commutative algebra Hk!≃Symch(V∗)H_k^!\simeq \mathrm{Sym}_{\mathrm{ch}}(V^*)Hk!​≃Symch​(V∗). Immediately after, it says the bar–cobar round trip recovers HkH_kHk​. Those statements can only both be true if one distinguishes:


the quadratic/Koszul dual algebra Hk!H_k^!Hk!​, and


the universal bar–cobar reconstruction ΩB(Hk)≃Hk\Omega B(H_k)\simeq H_kΩB(Hk​)≃Hk​.


Without that distinction, the exposition is misleading. The later chapter 6.5 is effectively the correction.
So the answer to your last question is:
Yes, essentially. If by “Koszul dual chiral algebra” you mean an actual dual algebra, then the bar construction by itself only gets you to the coalgebra side. To obtain the dual algebra, you need an additional duality step — in finite-type algebra this is often linear/operadic duality; in the chiral setting it is more naturally expressed via Verdier duality/factorization duality, not by the raw functor Ω\OmegaΩ.
So the shortest verdict is:


Ω(B(A))≃A\Omega(B(A))\simeq AΩ(B(A))≃A on the Koszul locus.


B(A)B(A)B(A) may model the Koszul dual coalgebra.


The Koszul dual algebra A!A^!A! is not, in general, Ω(B(A))\Omega(B(A))Ω(B(A)).


The problematic sentence in §1.4 should have said “the bar complex models the Koszul dual coalgebra,” not “the cobar of the bar complex produces the Koszul dual algebra” without qualification.
