#!/usr/bin/env python3
"""Exact square boundaries, translated contractions, and four-input signs."""
from pathlib import Path
from itertools import permutations, combinations
import hashlib
import json
import math
import platform
import sympy as sp

REPORT = Path(__file__).resolve().parent
ROOT = REPORT.parents[3]
u, v, t, s, x, y, z, k = sp.symbols('u v t s x y z k')


def integral2(f):
    return sp.integrate(sp.integrate(f, (u,0,1)), (v,0,1))


def pp(f, variable):
    return sp.Add(*(term for term in sp.Add.make_args(sp.expand(f))
                    if term.as_powers_dict().get(variable,0) < 0))


# These forms are global: each additional unavailable denominator is multiplied
# by q(1-q), while its own differential already vanishes on constant-order faces.
square_count = 0
for a in range(4):
    for b in range(4):
        for p, q in [(0,0),(1,0),(0,2),(2,2)]:
            g = u**a*v**b/t**p/s**q
            h = u**b*v**a/t**p/s**q
            if q:
                g *= v*(1-v)
            if p:
                h *= u*(1-u)
            H = sp.diff(h,u)-sp.diff(g,v)
            du_h = h.subs(u,1)-h.subs(u,0)
            dv_g = g.subs(v,1)-g.subs(v,0)
            identities = [
                integral2(u*v*H+v*h-u*g)
                -sp.integrate(v*h.subs(u,1),(v,0,1))
                +sp.integrate(u*g.subs(v,1),(u,0,1)),
                integral2(-v*H+g)
                -sp.integrate(g.subs(v,1),(u,0,1))
                +sp.integrate(v*du_h,(v,0,1)),
                integral2(-u*H-h)
                +sp.integrate(h.subs(u,1),(v,0,1))
                -sp.integrate(u*dv_g,(u,0,1)),
                integral2(H)-sp.integrate(du_h,(v,0,1))
                +sp.integrate(dv_g,(u,0,1))]
            assert all(sp.simplify(f)==0 for f in identities)
            assert pp(du_h,t)==0 and pp(dv_g,s)==0
            square_count += 1

# Direct five-state bar matrices, independent of the written gauge formulas.
E = [sp.zeros(5) for _ in range(3)]
E[0][1,0]=1; E[0][4,3]=1
E[1][2,0]=1
E[2][3,0]=1; E[2][4,1]=1
for i in range(3):
    for j in range(3):
        assert E[i]*E[j] == E[j]*E[i]
qvars = sp.symbols('q1:4'); tvars = sp.symbols('t1:4')
rvars = [qvars[i]/tvars[i] for i in range(3)]
gauge = sp.eye(5)
for i in range(3):
    gauge = gauge*(sp.eye(5)+rvars[i]*E[i])
expected = sp.Matrix([1,rvars[0],rvars[1],rvars[2],rvars[0]*rvars[2]])
assert gauge[:,0] == expected
for i in range(3):
    assert sp.simplify(gauge.diff(qvars[i])-E[i]*gauge/tvars[i]) == sp.zeros(5)
assert E[0]*E[2] != sp.zeros(5)

# The twenty-four path cubics generate exactly the asserted six-dimensional ideal.
positions = {1:x,2:y,3:z,4:sp.Integer(0)}
paths = []
for order in permutations(range(1,5)):
    paths.append(sp.expand(sp.prod(positions[order[i]]-positions[order[i+1]] for i in range(3))))
monomials = [x**a*y**b*z**(3-a-b) for a in range(4) for b in range(4-a)]
matrix = sp.Matrix([[sp.Poly(f,x,y,z).coeff_monomial(m) for m in monomials] for f in paths])
assert matrix.rank()==6
claimed = [sp.expand(a*b) for a in (x,y,z) for b in (x*(y-z),y*(x-z))]
actual_gb = sp.groebner(paths,x,y,z)
claimed_gb = sp.groebner(claimed,x,y,z)
assert actual_gb == claimed_gb
named_paths={''.join(map(str,order)):f for order,f in zip(permutations(range(1,5)),paths)}
A=x*(y-z); B=y*(x-z)
inverse_identities=[z*B+named_paths['1342'],
 y*B+named_paths['1342']+named_paths['1324'],
 y*A-named_paths['1243']+named_paths['1342']+named_paths['1324'],
 z*A-named_paths['1234']-named_paths['1243']+named_paths['1342'],
 x*A-named_paths['1234']-named_paths['1243']+named_paths['1342']+named_paths['2314'],
 x*B+named_paths['2314']+named_paths['1342']+named_paths['2134']]
assert all(sp.expand(f)==0 for f in inverse_identities)
for point in [(x,0,0),(0,y,0),(0,0,z),(x,x,x)]:
    assert all(sp.expand(f.subs(dict(zip((x,y,z),point)),simultaneous=True))==0 for f in paths)

# Derivatives of the original double pole retain the fixed nonzero level.
z1,z2 = sp.symbols('z1 z2')
contractions = 0
for r in range(7):
    for a in range(7):
        actual = sp.diff(k/(z1-z2)**2,z1,r,z2,a)
        expected = k*(-1)**r*math.factorial(r+a+1)/(z1-z2)**(r+a+2)
        assert sp.simplify(actual-expected)==0
        contractions += 1

# Independent oscillator calculation for the first quadratic outer collision.
J = sp.symbols('J0:16')
creation = sum(J[a]*v**a/math.factorial(a) for a in range(16))
oscillator_J2 = creation**2*J[0]**2+4*k*creation*J[0]/v**2+2*k*k/v**4
assert sp.expand(pp(oscillator_J2,v)-(2*k*k/v**4+4*k*J[0]**2/v**2+4*k*J[1]*J[0]/v))==0

# Each even relative-translation generator occurs in a closed two-form defect.
lam,mu = sp.symbols('lam mu')
relative_coefficients = []
for m in range(6):
    r=2*m
    first = 2*k*(-1)**r*math.factorial(r+1)/v**(r+2)*creation*J[0]
    second_creation = sum(J[r+a]*v**a/math.factorial(a) for a in range(16-r))
    second = 2*k/v**2*second_creation*J[0]
    outer_double = sp.expand(first+second).coeff(v,-2)
    assert sp.expand(outer_double-2*k*(r+2)*J[r]*J[0])==0
    relative_coefficients.append(str(2*k*(r+2)/(math.factorial(r)*2**r)))
for degree in range(13):
    basis = [sp.expand((lam+mu)**(degree-2*m)*(lam-mu)**(2*m))
             for m in range(degree//2+1)]
    mat = sp.Matrix([[sp.Poly(f,lam,mu).coeff_monomial(lam**a*mu**(degree-a))
                      for a in range(degree+1)] for f in basis])
    assert mat.rank()==len(basis)

# Coordinate determinants fix the four triple transfers and disjoint-pair density.
coords = sp.symbols('z1:5')
density_signs = {}
for l in range(1,5):
    B=[i for i in range(1,5) if i!=l]
    a,b,c=[coords[i-1] for i in B]; d=coords[l-1]
    staged=sp.Matrix([a-c,b-c,c-d,d])
    determinant=staged.jacobian(coords).det()
    assert determinant==(-1)**(4-l)
    density_signs[''.join(map(str,B))+'|'+str(l)]=int(determinant)
double_coords=sp.Matrix([coords[0]-coords[1],coords[2]-coords[3],coords[1],coords[3]])
assert double_coords.jacobian(coords).det()==-1

# Every permutation has the same three complementary-pair cancellations.
permutation_checks = 0
for order in permutations(range(1,5)):
    sums={}
    for r,a in combinations(range(4),2):
        first=tuple(sorted((order[r],order[a])))
        other=tuple(sorted(i for i in order if i not in first))
        key=tuple(sorted((first,other)))
        first_sign=(-1)**(r+a-1)
        # Keep the word-relative spectator order, then account for the two
        # complementary orders by their common four-label permutation.
        position_complement=tuple(i for i in range(4) if i not in (r,a))
        complementary_first_sign=(-1)**(sum(position_complement)-1)
        assert first_sign==complementary_first_sign
        second_sign=1 if other<first else -1
        sums[key]=sums.get(key,0)+first_sign*second_sign
    assert set(sums.values())=={0}
    permutation_checks += 1

# The proper right ideal tD has a nonzero simple-delta quotient.
assert pp(t*(1/t),t)==0
assert pp(1/t,t)!=0
assert pp(t*k/t**2,t)==k/t
assert pp(t*t*k/t**2,t)==0
assert -sp.diff(pp(t*k/t**2,t),t)-k/t**2==0

old_path=ROOT/'reports/research/bd_diagonal026/nonzero-level004/manifest.json'
assert hashlib.sha256(old_path.read_bytes()).hexdigest()=='9bbb432d69c18a1faa863dddb2b7c19e8554660c0fc984fb2da53d0ef03f31d9'
old=json.loads(old_path.read_text())
for item in old['files']:
    assert hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()==item['sha256'],item['path']

record={'result':'passed','python':platform.python_version(),'sympy':sp.__version__,
        'square_forms':square_count,'square_identities_per_form':4,
        'global_form_scope':'Forms are q-monomials times dq with q(1-q) for each additional denominator; all belong to the actual compatible-family algebra.',
        'bar_curvature':'All three multiplication matrices commute; the disjoint product is nonzero.',
        'path_cubic_rank':6,'path_inverse_identities_checked':6,
        'path_ideal_groebner':[str(f.as_expr()) for f in actual_gb.polys],
        'translated_double_pole_checks':contractions,
        'quadratic_relative_generators_checked':6,'quadratic_generator_coefficients':relative_coefficients,
        'quadratic_basis_total_degree_bound':12,'triple_density_signs':density_signs,
        'double_pair_density_sign':-1,'four_current_permutations_checked':permutation_checks,
        'preserved004_file_count':len(old['files']),
        'limits':'Exact finite checks. General module presentations, cone cohomology, all-coefficient maps, equivariance, and deconcatenation results depend on the written proofs. No proof assistant was used.'}
(REPORT/'exact-checks.json').write_text(json.dumps(record,indent=2)+'\n')
(REPORT/'preservation-check.json').write_text(json.dumps({'result':'passed','manifest_sha256':hashlib.sha256(old_path.read_bytes()).hexdigest(),'files':old['files']},indent=2)+'\n')
print(json.dumps(record,indent=2))
