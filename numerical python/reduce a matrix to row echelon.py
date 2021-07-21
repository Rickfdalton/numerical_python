import sympy as sym
A=sym.Matrix([[15,-3,-1],
              [-3,18,-6],
              [-4,-1,12]])
print(A.rref(pivots=True))

