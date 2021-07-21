import math

def f(x):
    return 2*math.sin(x)-(x**2)/10

n=30
c=0
x_l=0
x_u=4
error=0.0001
while c<n:
    print(c)
    d=((5**0.5-1)/2)*(x_u-x_l)
    x_1=x_l+d
    x_2=x_u-d
    print("x_l:",round(x_l,4))
    print("x_u:",round(x_u,4))
    print("d:",round(d,4))
    print("x_1:",round(x_1,4))
    print("x_2:",round(x_2,4))
    print("f(x1):",round(f(x_1),4))
    print("f(x2):",round(f(x_2),4))
    
    if f(x_1)>f(x_2):
        x_opt=x_1
        
    else:
        x_opt=x_2
    print("x_opt:",x_opt)
    max_err=(1-((5**0.5-1)/2))*abs((x_u-x_l)/x_opt)  
    print("max_err:",max_err)
    if(max_err<error):
        break
    if f(x_1)>f(x_2):
        
        x_l=x_2
    else:
        
        x_u=x_1
    print()
    
    c+=1
