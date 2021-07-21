L=[[2.04,0,0,0],
   [-1,1.55,0,0],
   [0,-1,1.39,0],
   [0,0,-1,1.32]]
B=[40.8,0.8,0.8,200.8]
Y=[0,0,0,0]

n=len(L)

for i in range(n):
    b=B[i]
    for j in range(n):
        if j!=i:
            b-=Y[j]*L[i][j]
    Y[i]=b/L[i][i]

print(Y)
        
