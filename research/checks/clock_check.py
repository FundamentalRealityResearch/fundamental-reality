import sympy as s

h, w, t = s.symbols('hbar omega t', real=True, nonzero=True)
H = -h*w*s.diag(1,-1)/2
full = s.Matrix([s.exp(s.I*w*t/2),s.exp(-s.I*w*t/2)])/s.sqrt(2)
ray = s.Matrix([1,s.exp(-s.I*w*t)])/s.sqrt(2)
wrong = s.Matrix([1,s.exp(s.I*w*t)])/s.sqrt(2)

def residual(psi,H):
    return (s.I*h*psi.diff(t)-H*psi).applyfunc(s.simplify)

print("SymPy",s.__version__)
print("full:", residual(full,H))
print("ray:",residual(ray,H))
print("ray shifted:",residual(ray,H+h*w*s.eye(2)/2))
print("opposite ray projected:",(residual(wrong,H)-wrong*(wrong.conjugate().T*residual(wrong,H))[0]).applyfunc(s.simplify))
