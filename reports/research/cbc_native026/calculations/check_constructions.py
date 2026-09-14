"""Exact finite polynomial and scalar checks; standard-library rational arithmetic."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, platform

# Monomials e^a h^j f^k b^r c^s use this fixed order.
one=(0,0,0,0,0)
def add(*terms):
    out={}
    for poly in terms:
        for mon,c in poly.items():out[mon]=out.get(mon,F(0))+c
    return {mon:c for mon,c in out.items() if c}
def scale(p,c):return {mon:c*x for mon,x in p.items() if c*x}
def mul(p,q):
    out={}
    for a,x in p.items():
        for b,y in q.items():
            if a[3]+b[3]>1 or a[4]+b[4]>1:continue
            mon=tuple(a[i]+b[i] for i in range(5))
            out[mon]=out.get(mon,F(0))+x*y*(-1)**(a[4]*b[3])
    return {mon:c for mon,c in out.items() if c}
gens=[]
for j in range(5):
    a=[0]*5;a[j]=1;gens.append({tuple(a):F(1)})
e,h,f,b,c=gens
def power(x,n):
    r={one:F(1)}
    for _ in range(n):r=mul(r,x)
    return r
dg=[{},scale(mul(e,c),-2),mul(h,c),add(e,{one:F(-1)}),{}]
def differential(poly):
    out={}
    for mon,coef in poly.items():
        factors=[i for i,n in enumerate(mon) for _ in range(n)]
        for j,i in enumerate(factors):
            term={one:coef*(-1)**sum(k>=3 for k in factors[:j])}
            for k in factors[:j]:term=mul(term,gens[k])
            term=mul(term,dg[i])
            for k in factors[j+1:]:term=mul(term,gens[k])
            out=add(out,term)
    return out
K=add(mul(e,f),scale(power(h,2),F(1,4)))
assert differential(K)=={}
count=0
for a,j,k in product(range(5),repeat=3):
    if a+j+k>6:continue
    for r,s in product(range(2),repeat=2):
        mon={(a,j,k,r,s):F(1)}
        assert differential(differential(mon))=={}
        count+=1

# Check the polynomial primitive after the constraint e=1.
def reduce_e(poly):
    out={}
    for mon,x in poly.items():
        n=(0,)+mon[1:];out[n]=out.get(n,F(0))+x
    return {m:x for m,x in out.items() if x}
u=add(f,scale(power(h,2),F(1,4)))
primitive_count=0
for a,j in product(range(9),range(9)):
    target=mul(c,mul(power(h,a),power(u,j)))
    primitive=scale(mul(power(h,a+1),power(u,j)),F(-1,2*a+2))
    assert reduce_e(differential(primitive))==target
    primitive_count+=1

def central(k):return 1-6*(k+1)**2/(k+2)
scalar_rows=[]
for k in [F(-8,3),F(-7,2),F(-4,3),F(-1,2),F(0),F(1),F(4,7)]:
    kp=-k-4;C=central(k);Cp=central(kp)
    assert C+Cp==26
    assert (C+Cp)/2==13
    assert (C==26)==(k in (F(-8,3),F(-7,2)))
    scalar_rows.append({'k':str(k),'reflected_k':str(kp),'c':str(C),'reflected_c':str(Cp)})
for h0,d in [(F(2),3),(F(3),8),(F(4),10)]:
    for k in [F(0),F(1),F(-1),F(4,7)]:
        kp=-k-2*h0
        assert (k+h0)*d/(2*h0)+(kp+h0)*d/(2*h0)==0
        assert k*d/(k+h0)+kp*d/(kp+h0)==2*d

# Exterior torus complex, basis 1,e1,e2,e1e2, lambda=2.
def matmul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
dt=[[0,0,0,0],[1,0,0,0],[0,0,0,0],[0,0,1,0]]
ht=[[0,1,0,0],[0,0,0,0],[0,0,0,1],[0,0,0,0]]
dh=matmul(dt,ht);hd=matmul(ht,dt)
assert [[dh[i][j]+hd[i][j] for j in range(4)] for i in range(4)]==[[int(i==j) for j in range(4)] for i in range(4)]
report={'python':platform.python_version(),'arithmetic':'fractions.Fraction','ds_square_monomials':count,'constrained_polynomial_primitives':primitive_count,'scalar_rows':scalar_rows,'torus_contraction':'dh+hd=I_4, lambda=2','limitations':'Finite identities only. Polynomial cohomology, bar quasi-isomorphism, and general transport use the written proofs. No chiral comparison is computed.'}
Path(__file__).with_name('construction-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
