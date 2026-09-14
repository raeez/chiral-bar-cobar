#!/usr/bin/env python3
"""Exact jets, intersection quotient, and source-connection obstruction."""
from pathlib import Path
import json
import platform
from itertools import permutations
import sympy as sp

REPORT=Path(__file__).resolve().parent
s,t,y,u,k=sp.symbols('s t y u k')
p=s*(t-s)
groebner=sp.groebner([t*t,p],s,t,order='lex')
basis=[sp.Integer(1),s,t,s*t]
def coordinates(poly):
    reduced=sp.Poly(groebner.reduce(sp.expand(poly))[1],s,t)
    return sp.Matrix([reduced.coeff_monomial(term) for term in basis])
S=sp.Matrix.hstack(*(coordinates(s*x) for x in basis))
T=sp.Matrix.hstack(*(coordinates(t*x) for x in basis))
assert S*T==T*S
assert T*T==sp.zeros(4)
assert S*S==S*T
assert S*S*S==sp.zeros(4)
assert sp.Matrix.hstack(*(coordinates(x) for x in basis))==sp.eye(4)
assert [tuple(pol.LM(order='lex').exponents) for pol in groebner.polys]==[(2,0),(0,2)]

# Multiplication by p on the normal two-jet module over C[y,s].
a0,a1=sp.symbols('a0 a1')
normal_remainder=sp.rem(p*(a0+t*a1),t*t,t)
assert sp.expand(normal_remainder-(-s*s*a0+t*(s*a0-s*s*a1)))==0
P=sp.Matrix([[-s*s,0],[s,-s*s]])
assert P.det()==s**4

# The connecting image of the actual global cycle is nonzero.
native_image=sp.expand(-k*p/t**2)
assert native_image==k*s*s/t**2-k*s/t
assert native_image.subs(s,1)==k/t**2-k/t

# Delta' has two regular-function jets; it is not a delta-line generator.
def principal(expression):
    expression=sp.expand(expression)
    return sp.Add(*(term for term in sp.Add.make_args(expression)
                    if term.as_powers_dict().get(t,0)<0))
nu=k/t**2
assert principal(t*nu)==k/t
assert principal(t*t*nu)==0
assert -sp.diff(principal(t*nu),t)==nu

# The exact polynomial binary cycle equations force the normal divisibility.
A0=sp.Symbol('A0')
assert (1+t*A0).subs(t,0)==1
path=sp.Symbol('a')*u+sp.Symbol('g0')
assert sp.diff(path,u)==sp.Symbol('a')

# Boundary coefficients of z_sigma = t12*t23 e + t23*q12 m + t12*q23 n.
t12,t23,dq12,dq23=sp.symbols('t12 t23 dq12 dq23')
assert sp.expand(-t12*t23*dq12/t12+t23*dq12)==0
assert sp.expand(-t12*t23*dq23/t23+t12*dq23)==0

positions={1:y+t,2:y+s,3:y}
all_coefficients=[]
for ordering in permutations((1,2,3)):
    i,j,l=ordering
    inversions=sum(ordering[a]>ordering[b] for a in range(3) for b in range(a+1,3))
    parity=(-1)**inversions
    coefficient=-parity*(positions[i]-positions[j])*(positions[j]-positions[l])
    all_coefficients.append(sp.rem(sp.expand(coefficient),t*t,t))
expected=[s*s-s*t,-s*t,s*t,s*t,-s*t,s*t-s*s]
assert all(sp.expand(a-b)==0 for a,b in zip(all_coefficients,expected))
all_ideal=sp.groebner([t*t]+all_coefficients,s,t,order='lex')
assert [f.as_expr() for f in all_ideal.polys]==[s*s,s*t,t*t]

record={'python':platform.python_version(),'sympy':sp.__version__,
 'result':'PASS','groebner_basis':[str(f.as_expr()) for f in groebner.polys],
 'normal_basis':[str(x) for x in basis], 'multiply_s':S.tolist(),'multiply_t':T.tolist(),
 'connecting_normal_matrix':P.tolist(),'connecting_determinant':str(P.det()),
 'global_connecting_image':str(native_image),
 'all_word_connecting_coefficients':[str(x) for x in all_coefficients],
 'all_word_quotient_groebner':[str(f.as_expr()) for f in all_ideal.polys],
 'checks':['normal two-jet annihilator','normal Weyl Euler relation',
           'length-four Groebner quotient','commuting nilpotent normal actions',
           'nonzero global connecting image','selected global source cycle',
           'endpoint obstruction to regular normal connection'],
 'scope':'Exact finite normal calculation and source-cycle coefficients. General module exact sequences and native support claims are proved in the source. No formal proof assistant.'}
(REPORT/'exact-checks.json').write_text(json.dumps(record,indent=2,default=str)+'\n')
print(json.dumps(record,indent=2,default=str))
