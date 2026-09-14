from fractions import Fraction as F
from pathlib import Path
import json,cmath
c=lambda t:F(13)-6*(t+1/t)
t=F(-2,3);assert (c(t),c(-t),c(1/t))==(26,0,26)
rho=(F(3,2),F(1,2));rhoc=(F(2),F(1));pair=sum(a*b for a,b in zip(rho,rhoc));assert 4+48*pair==172 and 4+4*3*10==124
f1=F(26,2)*F(1,2)*F(1,6)*F(1,2);assert f1==F(13,24)
def eta(tau,N=24):
 q=cmath.exp(2j*cmath.pi*tau);v=cmath.exp(cmath.pi*1j*tau/12)
 for n in range(1,N+1):v*=1-q**n
 return v
tau=.3+1.2j;N=24
rows={'exact':{'reflected_charges':[str(c(t)),str(c(-t))],'reciprocal_charge':str(c(1/t)),'B2_rho_pair':str(pair),'B2_sum':172,'incorrect_specialization':124,'F1_c26':str(f1),'vacuum_exponent_c26':str(-F(26,24))},'numerical_illustration_only':{'tau':[tau.real,tau.imag],'N':N,'eta_T_residual':abs(eta(tau+1)-cmath.exp(cmath.pi*1j/12)*eta(tau)),'eta_S_residual':abs(eta(-1/tau)-cmath.sqrt(-1j*tau)*eta(tau)),'floating_error':'not certified; proof uses exact eta identity, not numerical result'},'kernel_residue_at_S_i':{'correct':'i','old_weight_two':'-1'}}
Path(__file__).with_name('calculation-results.json').write_text(json.dumps(rows,indent=2)+'\n');print(json.dumps(rows))
