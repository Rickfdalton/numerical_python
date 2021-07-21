import math

fun = input("Enter Function")
a=float(input("Enter a"))
b=float(input("Enter b"))
err=float(input("Enter accuracy"))

def f(x):
    return eval(fun)
    
def sign(x):
    if x>0: return "+"
    elif x<0: return "-"
    else: return 0
    
print(f'{"steps":<{10}}',f'{"a":<{10}}',f'{"b":<{10}}',f'{"p":<{10}}',f'{"f(a)":<{10}}',f'{"f(b)":<{10}}',f'{"f(p)":<{10}}',"REl-Err")
n= math.ceil(math.log(((b-a)/err),2))
c=1
while(c<=n):
    if (c==1):
        p=float(a+b)/float(2)
        print(f'{str(c):<{10}}',f'{str(a):<{10}}',f'{str(b):<{10}}',f'{str(p):<{10}}',f'{str(sign(f(a))):<{10}}',f'{str(sign(f(b))):<{10}}',f'{str(sign(f(p))):<{10}}',"-")
    else:
        if f(p)==0:
            break
        elif sign(f(p))!=sign(f(a)):
            b=p
            p_new=(a+b)/2.0
            print(f'{str(c):<{10}}',f'{str(a):<{10}}',f'{str(b):<{10}}',f'{str(p_new):<{10}}',f'{str(sign(f(a))):<{10}}',f'{str(sign(f(b))):<{10}}',f'{str(sign(f(p_new))):<{10}}',abs((p_new-p)/p_new))
            p=p_new
        elif sign(f(p))==sign(f(a)):
            a=p
            p_new=(a+b)/2.0
            print(f'{str(c):<{10}}',f'{str(a):<{10}}',f'{str(b):<{10}}',f'{str(p_new):<{10}}',f'{str(sign(f(a))):<{10}}',f'{str(sign(f(b))):<{10}}',f'{str(sign(f(p_new))):<{10}}',abs((p_new-p)/p_new))
            p=p_new
    
    c+=1
