input_function=input("enter function ")
err=float(input("enter error "))
p_0=float(input())
p_1=float(input())

def f(x):
    return eval(input_function)
def g(p1,p2):
    return p2-f(p2)/((f(p2)-f(p1))/(p2-p1))

print("p_0",p_0)
print("p_1",p_1)
c=1
while c<=10:
    p_2=g(p_0,p_1)
    re=abs((p_2-p_1)/p_2)
    print(p_2,re)
    if re<err:
        break
    p_0=p_1
    p_1=p_2
    
    c=c-1
