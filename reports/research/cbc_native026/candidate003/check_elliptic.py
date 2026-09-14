from fractions import Fraction as F
from pathlib import Path
import json,cmath,math
# Exact complex arithmetic over Q(i); lambda here means the Dolbeault eigenvalue divided by pi.
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def inv(a):
 d=a[0]*a[0]+a[1]*a[1];return(a[0]/d,-a[1]/d)
taus=[(F(0),F(1)),(F(3,10),F(6,5)),(F(-2,3),F(7,4))];checks=0
for tr,ti in taus:
 for m in range(-5,6):
  for n in range(-5,6):
   if m==n==0:continue
   lam=((m*tr-n)/ti,F(m));h=inv(lam);assert mul(lam,h)==(1,0);checks+=1
# These are floating illustrations of the proved formulas, not acceptance certificates.
def P(t,z,N=80):
 q=cmath.exp(2j*math.pi*t)
 return math.pi/cmath.tan(math.pi*z)+4*math.pi*sum(q**n/(1-q**n)*cmath.sin(2*math.pi*n*z) for n in range(1,N+1))+2j*math.pi*z.imag/t.imag
t=.3+1.2j;z=.2-.3j
nums={'tau':[t.real,t.imag],'z':[z.real,z.imag],'N':80,'period_1':abs(P(t,z+1)-P(t,z)),'period_tau':abs(P(t,z+t)-P(t,z)),'odd':abs(P(t,-z)+P(t,z)),'S_weight1':abs(P(-1/t,z/t)-t*P(t,z)),'T_weight1':abs(P(t+1,z)-P(t,z)),'error_bounds':'floating roundoff not certified; all general claims proved analytically'}
r={'exact_nonconstant_fourier_modes':checks,'constant_mode_eigenvalue':0,'numerical_illustrations':nums};Path(__file__).with_name('calculation-results.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
