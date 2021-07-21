A=[[15,-3,-1,3800],
   [-3,18,-6,1200],
   [-4,-1,12,2350]]
n=len(A)



def add_rows(a,b,p):
    for i in range(len(A[0])) :
        A[a][i]=A[a][i]+A[b][i]*p

for k in range(len(A)):
    
    for j in range(k+1,len(A)):
        p=-(A[j][k])/(A[k][k])
        print("R",j+1,"=>","R",j+1,"+",p,"*","R",k+1)
        add_rows(j,k,p)
    for j in A:
        print(j)
    print()
    

    
