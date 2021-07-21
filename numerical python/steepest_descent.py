import sympy
h=sympy.symbols('h')

def f(x,y):
    return x**2+y**2+x

def df_dy(a,b):
    return 2*b

def df_dx(a,b):
    return 2*a+1

x0=2
y0=3

c=0
n=2
while c<n:
    x1=x0-h*df_dx(x0,y0)
    y1=y0-h*df_dy(x0,y0)
    print("x0:",x0)
    print("y0:",y0)
    print("x1:",x1)
    print("y1:",y1)
    print("g(h0):",f(x1,y1))
    print("g'(h0):",sympy.diff(f(x1,y1),h))
    try:
        h0=sympy.solvers.solve(sympy.diff(f(x1,y1),h),h)[0]
    except IndexError:
        print("found above")
        break
    print("h0:",h0)
    x1=x0-h0*df_dx(x0,y0)
    y1=y0-h0*df_dy(x0,y0)
    print("x1:",x1)
    print("y1:",y1)
    x0=x1
    y0=y1
    print()
    c+=1
