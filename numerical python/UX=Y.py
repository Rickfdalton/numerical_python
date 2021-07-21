U=[[1,-0.49,0,0],[0,1,-0.64,0],[0,0,1,-0.72],[0,0,0,1]]
X=[0,0,0,0]
Y=[20,13.42,10.23,159.87]

n=len(U)

for i in range(n-1,-1,-1):
    b=Y[i]
    for j in range(n):
        if j!=i:
            b-=X[j]*U[i][j]
    X[i]=b/U[i][i]

print(X)
        
