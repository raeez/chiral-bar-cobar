"""Exact uncropped Clifford and Verma-module actions. Python standard library only."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import json,platform,time
from pathlib import Path

def add(out,vec,scale=1):
 for k,v in vec.items():
  out[k]=out.get(k,0)+scale*v
  if not out[k]:del out[k]
 return out

def creator(op,down=False):
 t,n=op
 if down=='pol':return n<=0 if t=='b' else n<=-1
 return n<=(-1 if down else -2) if t=='b' else n<=(0 if down else 1)

def apply(op,state):
 t,n=op
 if creator(op):
  if op in state:return {}
  k=sum(x<op for x in state)
  return {tuple(sorted(state+(op,))):(-1)**k}
 partner=('c' if t=='b' else 'b',-n)
 if partner not in state:return {}
 k=state.index(partner)
 return {state[:k]+state[k+1:]:(-1)**k}

def product(ops,state,normal=False,down=False):
 sign=1
 if normal:
  sign=(-1)**sum(not creator(x,down) and creator(y,down) for i,x in enumerate(ops) for y in ops[i+1:])
  ops=tuple(x for x in ops if creator(x,down))+tuple(x for x in ops if not creator(x,down))
 out={state:sign}
 for op in reversed(ops):
  nxt={}
  for s,v in out.items():add(nxt,apply(op,s),v)
  out=nxt
 return out

def bind(action,vec):
 out={}
 for s,v in vec.items():add(out,action(s),v)
 return out

def support(s):return max([abs(n) for _,n in s]+[1])

@lru_cache(None)
def R(s,down=False,padding=0):
 bound=2*support(s)+4+padding
 out={}
 for m in range(-bound,bound+1):
  for n in range(-bound,bound+1):
   if m!=n:add(out,product((('c',-m),('c',-n),('b',m+n)),s,True,down),F(n-m,2))
 return out

@lru_cache(None)
def Lg(m,s,down=False):
 bound=support(s)+abs(m)+4
 out={}
 for n in range(-bound,bound+1):
  add(out,product((('b',m-n),('c',n)),s,True,down),m+n)
 return out

@lru_cache(None)
def normalize(word):
 for i in range(len(word)-1):
  a,b=word[i:i+2]
  if a<b:
   out=dict(normalize(word[:i]+(b,a)+word[i+2:]))
   add(out,normalize(word[:i]+(a+b,)+word[i+2:]),b-a)
   return out
 return {word:F(1)}

class Verma:
 def __init__(self,charge,weight):self.charge=charge;self.weight=weight
 @lru_cache(None)
 def L(self,n,word):
  if n<0:return normalize((-n,)+word)
  if n==0:return {word:F(self.weight+sum(word))} if self.weight+sum(word) else {}
  if not word:return {}
  k,rest=word[0],word[1:]
  out={}
  for w,v in self.L(n,rest).items():add(out,normalize((k,)+w),v)
  add(out,self.L(n-k,rest),n+k)
  if n==k:add(out,{rest:F(self.charge*(n**3-n),12)})
  return out
 def Q(self,state,t=0):
  w,s=state;out={}
  bound=max(sum(w),support(s),2)+2
  for n in range(-bound,bound+1):
   gv=apply(('c',-n),s)
   if gv:
    for mw,mv in self.L(n,w).items():
     for gs,gc in gv.items():add(out,{(mw,gs):mv*gc})
  for gs,gc in R(s).items():add(out,{(w,gs):gc})
  for gs,gc in apply(('c',0),s).items():add(out,{(w,gs):t*gc})
  return out
 def anomaly(self,state,t=0):
  w,s=state;out={}
  for n in range(1,support(s)+2):
   a=F((self.charge-26)*(n**3-n),12)-2*t*n
   for gs,gc in product((('c',-n),('c',n)),s).items():add(out,{(w,gs):a*gc})
  return out

start=time.time()
gens=tuple(sorted([('b',-n) for n in range(2,5)]+[('c',-n) for n in range(-1,5)]))
basis=[]
for k in range(len(gens)+1):
 for s in combinations(gens,k):
  if sum(-n for _,n in s)<=3:basis.append(s)
checks=0
for s in basis:
 assert R(s)==R(s,padding=2)
 expected={}
 for n in range(1,support(s)+2):add(expected,product((('c',-n),('c',n)),s),F(-26*(n**3-n),12))
 assert bind(R,R(s))==expected,('ghost_square',s)
 assert add(dict(R(s,True)),R(s),-1)==apply(('c',0),s)
 assert add(dict(R(s,'pol')),R(s),-1)==apply(('c',0),s)
 for m in range(-3,4):
  want=dict(Lg(m,s));add(want,{s:1} if m==0 else {})
  assert Lg(m,s,True)==want
  for n in range(-3,4):
   lhs=bind(lambda z:Lg(m,z),Lg(n,s));add(lhs,bind(lambda z:Lg(n,z),Lg(m,s)),-1)
   rhs={};add(rhs,Lg(m+n,s),m-n)
   if m+n==0:add(rhs,{s:F(-26*(m**3-m),12)})
   assert lhs==rhs,('ghost_central',m,n,s)
   checks+=1
words=[(),(1,),(2,),(1,1)]
parameters=[(0,0,0),(26,-2,0),(27,-2,0),(26,0,1)]
for charge,weight,t in parameters:
 module=Verma(charge,weight)
 for w in words:
  for s in basis:
   state=(w,s)
   actual=bind(lambda z:module.Q(z,t),module.Q(state,t))
   assert actual==module.anomaly(state,t),('full_square',charge,weight,t,state,actual,module.anomaly(state,t))
   checks+=1
low=[]
for n in range(2,7):
 actual=bind(R,R((('b',-n),)))
 assert actual=={(('c',-n),):F(-26*(n**3-n),12)}
 low.append({'mode':n,'coefficient':str(F(-26*(n**3-n),12))})
polgens=(('b',-3),('b',-2),('b',-1),('b',0),('c',-3),('c',-2),('c',-1))
polimages=set()
for k in range(len(polgens)+1):
 for s in combinations(polgens,k):
  v=product(s,(('c',0),('c',1)))
  assert len(v)==1 and abs(next(iter(v.values())))==1
  target=next(iter(v))
  assert sum(1 if t=='c' else -1 for t,n in target)==sum(1 if t=='c' else -1 for t,n in s)+2
  assert sum(-n for t,n in target)==sum(-n for t,n in s)-1
  polimages.add(target)
assert len(polimages)==2**len(polgens)
report={'polarization_basis_images':len(polimages),'python':platform.python_version(),'arithmetic':'fractions.Fraction, exact rational','ghost_basis':len(basis),'ghost_energy_bound':3,'verma_words':[list(w) for w in words],'parameters':parameters,'operator_equalities':checks,'low_mode_square':low,'elapsed_seconds':round(time.time()-start,2),'cropping':'No intermediate state is cropped. Each call recomputes finite mode bounds from its input. Ghost cutoff increase by 2 checked on every initial ghost state.','bounds':'R: 2 max(abs occupied index)+4, with annihilator indices fixed by occupied partners and the total index zero. Lgh_m: max(abs occupied index)+abs(m)+4. Matter: max(PBW level,abs occupied ghost index,2)+2.','limitations':'Exact finite checks only. General equality uses the manuscript proof. No formal proof assistant was run.'}
Path(__file__).with_name('results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
