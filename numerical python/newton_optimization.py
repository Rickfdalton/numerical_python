import math
def f(x):
    return (2*math.sin(x)-(x**2/10))
def g(x):
    return x-(2*math.cos(x)-x/5)/(-2*math.sin(x)-0.2)

n=20
c=1
x=2.5
err=0.001
while c<n:
    print(g(x))
    rel_err=abs(g(x)-x)/g(x)
    print('err',rel_err)
    print()
    x=g(x)
    if rel_err<err:
        print(f(x))
        break
    c+=1
    
