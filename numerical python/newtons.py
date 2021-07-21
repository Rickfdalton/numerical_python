import sympy
import math
input_function =input("enter function ")
err=float(input("enter error"))
p=float(input("initial guess"))

x= sympy.Symbol('x')
diff_fun=sympy.diff(input_function,x)

def f(x):
    return eval(input_function)
def f1(x):
    return eval(str(diff_fun))

def g(k):
    return k-(f(k)/f1(k))

def  printer(step,p,error):
    print(f'{step:<{5}}',f'{p:<{15}}',f'{error:<{15}}')

c=0
print()
printer("step","p","error")
printer(c,p,'-')
while c<10:
    c+=1
    p_new=g(p)
    rel_err=abs((p-p_new)/p_new)
    printer(c,p_new,rel_err)
    if rel_err <err:
        break
    
    
    p=p_new
    
