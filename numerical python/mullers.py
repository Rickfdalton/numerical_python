input_function=input('enter function ')
p_0=float(input('enter p_0 '))
p_1=float(input('enter p_1 '))
p_2=float(input('enter p_2 '))

def f(x):
    return eval(input_function)
def sign(x):
    if abs(x)>=0:
        return 1
    else:
        return -1
    
def g(x,a,b,c):
    return x-(2*c/(b+sign(b)*(b**2-4*a*c)**0.5))

def printer(count,p_0,p_1,p_2,h_0,h_1,s_0,s_1,a,b,c,p_3):
    print("=====================================")
    print("step:",count)
    print("p0:",p_0)
    print("p1:",p_1)
    print("p2:",p_2)
    print("h0:",h_0)
    print("h1:",h_1)
    print("s0:",s_0)
    print("s1:",s_1)
    print("a:",a)
    print("b",b)
    print("c",c)
    print()
    print("p_3",p_3)
    print("relative error",abs((p_3-p_2)/p_3))

count=0
while count<6:
    h_0=p_1-p_0
    h_1=p_2-p_1
    s_1=(f(p_2)-f(p_1))/(p_2-p_1)
    s_0=(f(p_1)-f(p_0))/(p_1-p_0)
    a=(s_1-s_0)/(h_1+h_0)
    b=(a*h_1+s_1)
    c=f(p_2)
    p_3=g(p_2,a,b,c)
    printer(count,p_0,p_1,p_2,h_0,h_1,s_0,s_1,a,b,c,p_3)

    p_0=p_1
    p_1=p_2
    p_2=p_3
    count+=1
    
