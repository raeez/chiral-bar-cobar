"""Exact operations for the subregular bar and C2 comparisons."""
from pathlib import Path
from itertools import product, permutations
from math import comb
import json
import sympy as S
import check_modes as M
k=M.k
rows=[]
def check(name,value):
 ok=not value if isinstance(value,dict) else S.simplify(value)==0
 rows.append({'name':name,'pass':bool(ok),'residual':str(value)})
 if not ok:print('FAIL',name,value)

def diff(a,b):return M.add(a,M.scale(-1,b))
assoc=diff(M.normal(M.normal(M.J,M.J),M.U),M.normal(M.J,M.normal(M.J,M.U)))
check('full normal associator',diff(assoc,M.scale(2,M.normal(M.deriv(M.J),M.U))))
assert assoc
check('first product does not descend through C2',M.add(M.mode(M.deriv(M.J),1,M.U),M.U))

def c2(state):return {mon:S.expand(c) for mon,c in state.items() if all(n==-1 for _,n in mon)}
for a,b,target in [(M.J,M.U,M.U),(M.J,M.V,M.scale(-1,M.V)),(M.J,M.P,{}),
 (M.U,M.V,M.add(M.P,M.scale(-S.Rational(9,4),M.normal(M.J,M.J)))),
 (M.P,M.U,M.scale(-S.Rational(3,2),M.normal(M.J,M.U))),
 (M.P,M.V,M.scale(S.Rational(3,2),M.normal(M.J,M.V)))]:
 check('C2 Poisson bracket '+str(len(rows)),c2(diff(M.mode(a,0,b),target)))
for F in [M.J,M.U,M.P,M.V]:check('C2 closed generator '+str(len(rows)),c2(M.mode(M.q,0,F)))
kap=(2*k+3)/3
check('reflected augmentation obstruction',kap+kap.subs(k,-k-6)+2)
check('level zero current vacuum',kap.subs(k,0)-1)
t,c=S.symbols('t c')
check('central charge discriminant',S.discriminant(6*t*t+(c-25)*t+24,t)-(c-1)*(c-49))
check('finite base inverse',S.rem(t*(-(6*t+c-25)/24)-1,6*t*t+(c-25)*t+24,t))

# Polynomial/exterior contraction in the actual transformed C2 coordinates.
# Even a',e,H,X and odd b1,b2,c1,c2 are the eight contracted variables.
def add(*vals):
 out={}
 for v in vals:
  for mon,coef in v.items():out[mon]=out.get(mon,0)+coef
 return {m:S.expand(c) for m,c in out.items() if S.expand(c)!=0}
def scale(a,v):return {m:S.expand(a*c) for m,c in v.items() if a*c!=0}
def mulmon(m,n):
 p,b=m;q,d=n
 if b&d:return None,0
 signs=sum(1 for i in range(4) for j in range(4) if b>>i&1 and d>>j&1 and i>j)
 return (tuple(a+c for a,c in zip(p,q)),b|d),(-1)**signs
def oddmul(i,v):
 out={};u=((0,0,0,0),1<<i)
 for m,c in v.items():n,sgn=mulmon(u,m);out=add(out,{n:c*sgn} if sgn else {})
 return out
def evenmul(i,v):
 out={}
 for (p,b),c in v.items():q=list(p);q[i]+=1;out[(tuple(q),b)]=c
 return out
def ed(i,v):
 out={}
 for (p,b),c in v.items():
  if p[i]:q=list(p);q[i]-=1;out[(tuple(q),b)]=c*p[i]
 return out
def od(i,v):
 return {(p,b^(1<<i)):c*(-1)**((b&((1<<i)-1)).bit_count()) for (p,b),c in v.items() if b>>i&1}
def D(v):return add(evenmul(0,od(0,v)),evenmul(1,od(1,v)),scale(-2,oddmul(2,ed(2,v))),oddmul(3,ed(3,v)))
def h(v):return add(oddmul(0,ed(0,v)),oddmul(1,ed(1,v)),scale(-S.Rational(1,2),evenmul(2,od(2,v))),evenmul(3,od(3,v)))
for p in product(range(5),repeat=4):
 for b in range(16):
  N=sum(p)+b.bit_count()
  if N>4:continue
  mon={(p,b):S.Integer(1)}
  check('C2 D square '+str(p)+','+str(b),D(D(mon)))
  check('C2 Euler contraction '+str(p)+','+str(b),add(D(h(mon)),h(D(mon)),scale(-N,mon)))

# Direct normalized polynomial bar: tuple of exponent vectors is a word.
def bbar(word):
 out={}
 for i in range(len(word)-1):
  merged=tuple(x+y for x,y in zip(word[i],word[i+1]))
  w=word[:i]+(merged,)+word[i+2:]
  out[w]=out.get(w,0)+(-1)**i
 return {w:c for w,c in out.items() if c}
def ba(v):
 out={}
 for w,c in v.items():
  for u,d in bbar(w).items():out[u]=out.get(u,0)+c*d
 return {w:c for w,c in out.items() if c}
basis=[tuple(int(i==j) for j in range(4)) for i in range(4)]
for length in range(5):
 for w in product(basis,repeat=length):check('polynomial bar square '+str(w),ba(bbar(w)))
for n in range(5):
 for subset in __import__('itertools').combinations(range(4),n):
  v={}
  for perm in permutations(subset):
   sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
   v[tuple(basis[i] for i in perm)]=sign
  check('exterior cycle '+str(subset),ba(v))

# Independent exact centralizer and Dynkin grading calculations for all sl4 partitions.
def jordan(parts):
 f=S.zeros(4);x=S.zeros(4);offset=0
 for n in parts:
  for i in range(n):x[offset+i,offset+i]=S.Rational(n-1,2)-i
  for i in range(n-1):f[offset+i+1,offset+i]=1
  offset+=n
 return f,x
mats=[]
for i in range(4):
 for j in range(4):
  if i!=j:m=S.zeros(4);m[i,j]=1;mats.append(m)
for i in range(3):m=S.zeros(4);m[i,i]=1;m[3,3]=-1;mats.append(m)
expected={(1,1,1,1):[1]*15,(2,1,1):[1]*4+[S.Rational(3,2)]*4+[2],(2,2):[1]*3+[2]*4,(3,1):[1,2,2,2,3],(4,):[2,3,4]}
for part,weights in expected.items():
 f,x=jordan(part);mat=S.Matrix.hstack(*[S.Matrix(f*m-m*f).reshape(16,1) for m in mats]);ker=mat.nullspace()
 ks=[sum((a*m for a,m in zip(v,mats)),S.zeros(4)) for v in ker]
 base=S.Matrix.hstack(*[m.reshape(16,1) for m in ks])
 ad=S.Matrix.hstack(*[base.gauss_jordan_solve((x*m-m*x).reshape(16,1))[0] for m in ks])
 actual=[]
 for val,mult in ad.eigenvals().items():actual.extend([1-val]*mult)
 check('sl4 centralizer weights '+str(part),0 if sorted(actual)==sorted(weights) else 1)
# Differential module-bar signs on the actual eight-variable contracted factor.
unit=((0,0,0,0),0)
gens=[(tuple(int(i==j) for j in range(4)),0) for i in range(4)]+[((0,0,0,0),1<<i) for i in range(4)]
def deg(mon):
 mask=mon[1]
 return -(mask&3).bit_count()+((mask>>2)&3).bit_count()
def modulebar(state):
 out={}
 def put(key,c):out[key]=out.get(key,0)+c
 for (word,mod),coef in state.items():
  prefix=0
  for j,a in enumerate(word):
   for da,c in D({a:S.Integer(1)}).items():put((word[:j]+(da,)+word[j+1:],mod),coef*(-1)**(prefix+1)*c)
   prefix+=deg(a)-1
  for dm,c in D({mod:S.Integer(1)}).items():put((word,dm),coef*(-1)**prefix*c)
  prefix=0
  for j in range(len(word)-1):
   ab,sgn=mulmon(word[j],word[j+1])
   if sgn:put((word[:j]+(ab,)+word[j+2:],mod),coef*(-1)**(prefix+deg(word[j]))*sgn)
   prefix+=deg(word[j])-1
  if word:
   am,sgn=mulmon(word[-1],mod)
   if sgn:put((word[:-1],am),coef*(-1)**sum(deg(x)-1 for x in word[:-1])*sgn)
 return {key:S.expand(c) for key,c in out.items() if c}
for n in range(3):
 for word in product(gens,repeat=n):
  for mod in [unit]+gens:
   state={(word,mod):S.Integer(1)}
   check('differential module bar square '+str((word,mod)),modulebar(modulebar(state)))
for a,b in product(gens,repeat=2):
 word=(a,b,a);mod=b
 check('module length-three action '+str((a,b)),modulebar(modulebar({(word,mod):S.Integer(1)})))
check('principal Sugawara scalar at zero',((8*k/(k+3))/2).subs(k,0))
check('principal DS scalar at zero',((2-24*(k+2)**2/(k+3))/2).subs(k,0)+15)
check('Virasoro residue factorial',S.Rational(1,2)/S.factorial(3)-S.Rational(1,12))

report={'python':__import__('platform').python_version(),'sympy':S.__version__,'checks':rows,'total':len(rows),'passed':sum(x['pass'] for x in rows),'bar_cohomology_ranks':[comb(4,n) for n in range(5)],'scope':'Exact finite identities and examples; general cohomology is proved in the manuscript.'}
Path(__file__).with_name('bar-checks.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS',report['passed'],'of',report['total'])
raise SystemExit(0 if report['passed']==report['total'] else 1)
