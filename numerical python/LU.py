A=[[2,-1,0,0],
   [-1,2,-1,0],
   [0,-1,2,-1],
   [0,0,-1,2]]

B=[1,0,0,1]

L=[[1,0,0,0],
   [0,1,0,0],
   [0,0,1,0],
   [0,0,0,1]
   ]
n=len(A)

def elimination(R1,a,R2):
    for i in range(n):
        A[R1][i]+=A[R2][i]*a
        

step=1
while step<n:
    for j in range(step,n):
        a=-A[j][step-1]/A[step-1][step-1]
        elimination(j,a,step-1)
        L[j][step-1]=-a
    step+=1

print('U',A)
print('L',L)

Y=[0,0,0,0]

n=len(L)

for i in range(n):
    b=B[i]
    for j in range(n):
        if j!=i:
            b-=Y[j]*L[i][j]
    Y[i]=b/L[i][i]

print('y=',Y)

X=[0,0,0,0]
U=A
n=len(U)

for i in range(n-1,-1,-1):
    b=Y[i]
    for j in range(n):
        if j!=i:
            b-=X[j]*U[i][j]
    X[i]=b/U[i][i]

print('x=',X)
        

