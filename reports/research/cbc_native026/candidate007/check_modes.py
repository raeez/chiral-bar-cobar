"""Exact affine and Clifford vacuum-mode calculations for subregular sl3."""
from functools import lru_cache
from math import factorial, floor, ceil
from pathlib import Path
import json
import platform
import sympy as s

k = s.Symbol('k')
names = ['a','e','h','j','u','v','A','B','b1','b2','c1','c2']
ix = {n:i for i,n in enumerate(names)}
parity = [0]*8+[1]*4
weight = [s.Integer(1)]*8+[s.Rational(1,2)]*4
zero = s.zeros(3)
def E(i,j):
    m = zero.copy(); m[i-1,j-1]=1; return m
matrices = [E(1,2),E(1,3),s.diag(1,-1,0),s.diag(1,1,-2)/3,
            E(2,3),E(3,2),E(2,1),E(3,1)]

def clean(v):
    return {m:s.expand(c) for m,c in v.items() if s.expand(c)!=0}
def add(*vs):
    z={}
    for v in vs:
        for m,c in v.items(): z[m]=z.get(m,0)+c
    return clean(z)
def scale(c,v): return clean({m:c*a for m,a in v.items()})
one = {():s.Integer(1)}
def gen(n): return {((ix[n],-1),):s.Integer(1)}
def coordinates(m):
    return [m[0,1],m[0,2],(m[0,0]-m[1,1])/2,
            -3*m[2,2]/2,m[1,2],m[2,1],m[1,0],m[2,0]]

@lru_cache(None)
def comm(x,y):
    a,m=x; b,n=y
    if a<8 and b<8:
        cs=coordinates(matrices[a]*matrices[b]-matrices[b]*matrices[a])
        terms=tuple(((i,m+n),c) for i,c in enumerate(cs) if c)
        scalar=k*m*s.trace(matrices[a]*matrices[b]) if m+n==0 else 0
        return terms,scalar
    scalar=int({a,b} in ({8,10},{9,11}) and m+n==-1)
    return (),s.Integer(scalar)

@lru_cache(None)
def act(x,mon):
    """Order a generator mode using its supercommutator."""
    if not mon:
        return {(x,):s.Integer(1)} if x[1]<0 else {}
    y,tail=mon[0],mon[1:]
    if x[1]<0 and (x<y or (x==y and not parity[x[0]])):
        return {(x,)+mon:s.Integer(1)}
    if x==y and parity[x[0]]:
        return {}
    terms,scalar=comm(x,y)
    sign=(-1)**(parity[x[0]]*parity[y[0]])
    moved={}
    for w,c in act(x,tail).items():
        moved=add(moved,scale(sign*c,act(y,w)))
    out=add(moved,scale(scalar,{tail:1}))
    for z,c in terms: out=add(out,scale(c,act(z,tail)))
    return out

def action(x,v):
    out={}
    for mon,c in v.items(): out=add(out,scale(c,act(x,mon)))
    return out
def energy(mon): return sum(weight[a]-n-1 for a,n in mon)
def pmon(mon): return sum(parity[a] for a,n in mon)%2

@lru_cache(None)
def mode_monomial(left,n,right):
    """Reconstruct vertex modes from ordered negative-mode monomials."""
    if not left: return {right:1} if n==-1 else {}
    (a,m),rest=left[0],left[1:]
    d=-m-1
    def derived(j,v):
        return scale((-1)**d*s.binomial(j,d),action((a,j-d),v))
    if not rest: return derived(n,{right:1})
    out={}
    lo=ceil(n-energy(right)-energy(rest))
    for j in range(lo,0):
        z=mode_monomial(rest,n-j-1,right)
        out=add(out,derived(j,z))
    hi=floor(energy(right)+weight[a]+d-1)
    sign=(-1)**(parity[a]*pmon(rest))
    for j in range(0,hi+1):
        z=derived(j,{right:1})
        for mon,c in z.items():
            out=add(out,scale(sign*c,mode_monomial(rest,n-j-1,mon)))
    return out

def mode(left,n,right):
    out={}
    for l,c in left.items():
        for r,d in right.items():
            out=add(out,scale(c*d,mode_monomial(l,n,r)))
    return out
def normal(a,b): return mode(a,-1,b)
def deriv(a,r=1): return scale(factorial(r),mode(a,-r-1,one))

g={n:gen(n) for n in names}
N1=normal(g['b1'],g['c1']); N2=normal(g['b2'],g['c2'])
H=add(g['h'],scale(2,N1),N2)
J=add(g['j'],N2)
U=add(g['u'],scale(-1,normal(g['b2'],g['c1'])))
X=add(g['v'],scale(-1,normal(g['b1'],g['c2'])))
P=add(g['A'],scale(s.Rational(1,4),normal(H,H)),normal(U,X),
      scale((k+2)/2,deriv(H)))
V=add(g['B'],scale(-s.Rational(1,2),normal(H,X)),
      scale(-s.Rational(3,2),normal(J,X)),scale(-k-2,deriv(X)))
q=add(normal(add(g['a'],scale(-1,one)),g['c1']),normal(g['e'],g['c2']))
Tnum=add(P,scale(s.Rational(3,4),normal(J,J)),scale(-s.Rational(3,2),deriv(J)))
T=scale(1/(k+3),Tnum)

checks=[]
def check(name,actual,expected):
    delta=add(actual,scale(-1,expected))
    delta={str(m):str(s.factor(c)) for m,c in delta.items() if s.factor(c)!=0}
    checks.append({'name':name,'pass':not delta,'difference':delta})
    print(name, 'PASS' if not delta else 'FAIL '+str(delta),flush=True)

if __name__=='__main__':
    for a in names:
        check('vacuum '+a,mode(g[a],-1,one),g[a])
    for a in names:
        for b in names:
            for n in [0,1]:
                terms,scalar=comm((ix[a],n),(ix[b],-1))
                expected=scale(scalar,one)
                for z,c in terms: expected=add(expected,scale(c,act(z,())))
                check('generator '+a+' '+b+' '+str(n),mode(g[a],n,g[b]),expected)
    check('q square',mode(q,0,q),{})
    for n,F in [('J',J),('U',U),('P',P),('V',V)]:
        check('D '+n,mode(q,0,F),{})
    check('D H',mode(q,0,H),scale(-2,g['c1']))
    check('D X',mode(q,0,X),g['c2'])
    for n in range(3):
        check('J J '+str(n),mode(J,n,J),scale((2*k+3)/3,one) if n==1 else {})
        check('J U '+str(n),mode(J,n,U),U if n==0 else {})
        check('J V '+str(n),mode(J,n,V),scale(-1,V) if n==0 else {})
        check('U U '+str(n),mode(U,n,U),{})
        check('V V '+str(n),mode(V,n,V),{})
    cc=-(2*k+3)*(3*k+1)/(k+3)
    for n in range(5):
        check('T T '+str(n),mode(T,n,T),{0:deriv(T),1:scale(2,T),3:scale(cc/2,one)}.get(n,{}))
        for name,F,w in [('J',J,1),('U',U,s.Rational(3,2)),('V',V,s.Rational(3,2))]:
            check('T '+name+' '+str(n),mode(T,n,F),{0:deriv(F),1:scale(w,F)}.get(n,{}))
    uv={2:scale((k+1)*(2*k+3),one),1:scale(3*(k+1),J),
        0:add(scale(3,normal(J,J)),scale(3*(k+1)/2,deriv(J)),scale(-k-3,T))}
    for n in range(4): check('U Gminus '+str(n),mode(U,n,scale(-1,V)),uv.get(n,{}))
    Snum=add(scale(s.Rational(1,4),normal(g['h'],g['h'])),
             scale(s.Rational(3,4),normal(g['j'],g['j'])))
    for a,b in [('a','A'),('e','B'),('u','v')]:
        Snum=add(Snum,scale(s.Rational(1,2),
                 add(normal(g[a],g[b]),normal(g[b],g[a]))))
    Lnum=add(Snum,scale((k+3)/2,deriv(add(g['h'],g['j']))),
             scale(k+3,add(normal(deriv(g['b1']),g['c1']),
                           normal(deriv(g['b2']),g['c2']))))
    Lrep=add(P,scale(s.Rational(3,4),normal(J,J)),scale(k/2,deriv(J)))
    primitive=add(normal(g['b1'],g['A']),normal(g['b2'],g['B']))
    check('exact stress homotopy',add(Lnum,scale(-1,Lrep)),mode(q,0,primitive))
    report={'python':platform.python_version(),'sympy':s.__version__,'checks':checks,
            'passed':sum(x['pass'] for x in checks),'total':len(checks)}
    Path(__file__).with_name('mode-checks.json').write_text(json.dumps(report,indent=2)+'\n')
    raise SystemExit(0 if report['passed']==report['total'] else 1)
