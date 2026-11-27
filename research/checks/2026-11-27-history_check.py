import sympy as s
print('SymPy', s.__version__)
I=s.eye(4)
X=s.Matrix([[0,1],[1,0]])
XS=s.kronecker_product(X,s.eye(2))
CX=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
U=[XS,CX,XS]
v=[I[:,0]]
for u in U: v.append(u*v[-1])
H=s.zeros(16)
for t,u in enumerate(U):
    a,b=4*t,4*(t+1)
    H[a:a+4,a:a+4]+=I/2
    H[b:b+4,b:b+4]+=I/2
    H[b:b+4,a:a+4]-=u/2
    H[a:a+4,b:b+4]-=u.T/2
psi=s.Matrix.vstack(*v)/2
P=s.kronecker_product(s.eye(4)[::-1,:],I)
print('history basis indices:', [list(x).index(1) for x in v])
print('norm squared:', (psi.T*psi)[0])
print('Hermitian:', H==H.T)
print('stationary:', H*psi==s.zeros(16,1))
print('reversal stationary:', (P*H*P.T)*(P*psi)==s.zeros(16,1))
print('propagator spectrum:', H.eigenvals())
B=s.diag(0,1,1,1)
Bin=s.diag(B,s.zeros(12))
print('boundary-selected kernel dimension:', len((H+Bin).nullspace()))
assert H*psi==s.zeros(16,1) and H==H.T and (psi.T*psi)[0]==1
assert (P*H*P.T)*(P*psi)==s.zeros(16,1)
assert len((H+Bin).nullspace())==1
