import math
#fixed-point
def g1(x):
    return 2*x-3*x**2

"""def g2(x):
    return x-((x**3-21)/(3*x**2))

def g3(x):
    return x-((x**4-21*x)/(x**2-21))

def g4(x):
    return (21/x)**0.5"""

print('====G1========')
p=0.3
for i in range(10):
    print(p)
    p=g1(p)

"""print('====G2========')
p=1
for i in range(10):
    print(p)
    p=g2(p)

print('====G3========')
p=1
for i in range(10):
    print(p)
    p=g3(p)

print('====G4========')
p=1
for i in range(10):
    print(p)
    p=g4(p)
"""
