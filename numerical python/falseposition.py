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

def printer(step,a,b,p,fa,fb,fp,err,w):
    print(f'{step:<{w}}',f'{a:<{w}}',f'{b:<{w}}',f'{p:<{w}}',f'{fa:<{w}}',f'{fb:<{w}}',f'{fp:<{w}}',err)
    
printer("step","a","b","p","f(a)","f(b)","f(p)","Rel-err",15)

c=1
while(c<=10):
    if (c==1):
        p=b-(f(b)*(b-a)/(f(b)-f(a)))
        printer(str(round(c,10)),str(round(a,10)),str(round(b,10)),str(round(p,10)),str(round(f(a),10)),str(round(f(b),10)),str(round(f(p),10)),"-",15)

    else:
        if f(p)==0:
            break
        elif sign(f(p))!=sign(f(a)):
            b=p
            p_new=b-(f(b)*(b-a)/(f(b)-f(a)))
            printer(str(round(c,10)),str(round(a,10)),str(round(b,10)),str(round(p_new,10)),str(round(f(a),10)),str(round(f(b),10)),str(round(f(p_new),10)),str(abs((p_new-p)/p_new)),15)
            if(abs((p_new-p)/p_new)<=err):
                break
            p=p_new
        elif sign(f(p))==sign(f(a)):
            a=p
            p_new=b-(f(b)*(b-a)/(f(b)-f(a)))
            printer(str(round(c,10)),str(round(a,10)),str(round(b,10)),str(round(p_new,10)),str(round(f(a),10)),str(round(f(b),10)),str(round(f(p_new),10)),str(abs((p_new-p)/p_new)),15)
            if(abs((p_new-p)/p_new)<=err):
                break
            p=p_new
    
    c+=1
