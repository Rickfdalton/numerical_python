#gauss-seidel
a11,a12,a13,a14,b1=(10,-1,2,0,6)
a21,a22,a23,a24,b2=(-1,11,-1,3,25)
a31,a32,a33,a34,b3=(2,-1,10,-1,-11)
a41,a42,a43,a44,b4=(0,3,-1,8,15)

c=0
n=11
x1,x2,x3,x4=0,0,0,0
while c<n:
    print("iteration",c)
    print()
    print("x1",x1)
    print("x2",x2)
    print("x3",x3)
    print("x4",x4)
    print()
    x1=(b1-a12*x2-a13*x3-a14*x4)/a11
    x2=(b2-a21*x1-a23*x3-a24*x4)/a22
    x3=(b3-a31*x1-a32*x2-a34*x4)/a33
    x4=(b4-a41*x1-a42*x2-a43*x3)/a44
   
    c+=1
