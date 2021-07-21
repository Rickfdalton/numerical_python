A=[[500**4,500**3,500**2,500,1,0.457],
   [250**4,250**3,250**2,250,1,0.675],
   [300**4,300**3,300**2,300,1,0.616],
   [400**4,400**3,400**2,400,1,0.525],
   [200**4,200**3,200**2,200,1,0.746]]

#A=[[0.003,59.14,59.17],[5.291,-6.13,46.78]]
r=-1
n=len(A)

def exchange(r1,r2):
    A[r1],A[r2]=A[r2],A[r1]


def elimination(r1,a,r2):
    if r!=(-1):
        a=sig_round(a,r)
        for i in range(n+1):
            A[r1][i]=sig_round((sig_round(A[r1][i],r)+sig_round(a*sig_round(A[r2][i],r),r)),r)
    else:
        for i in range(n+1):
            A[r1][i]+=a*(A[r2][i])
def max_in(arr):
    maxi=max(arr)

    for e in range(len(arr)):
        if arr[e]==maxi:
            return e

def max_dic(arr2):
    max_val=max(arr2.values())
    for e in arr2.keys():
        if arr2[e]== max_val:
            return e
    
def sig_round(x,y):
    if y==1:
        return float('%s' % float('%.1g' % x))
    elif y==2:
        return float('%s' % float('%.2g' % x))
    elif y==3:
        return float('%s' % float('%.3g' % x))
    elif y==4:
        return float('%s' % float('%.4g' % x))
    elif y==5:
        return float('%s' % float('%.5g' % x))
    elif y==6:
        return float('%s' % float('%.6g' % x))
    elif y==7:
        return float('%s' % float('%.7g' % x))
    elif y==8:
        return float('%s' % float('%.8g' % x))
    elif y==9:
        return float('%s' % float('%.9g' % x))
    
    
step=0
s=[0]*n
for i in range(n):
    arr=[]
    for j in range(n):
        arr.append(abs(A[i][j]))
    s[i]=max(arr)

while step<n:
    arr2={}
    for index in range(step,n):
        arr2[index]=abs(A[index][step]/s[index])
    exchange(step,max_dic(arr2))
    
    print("exchanging row",step+1,max_dic(arr2)+1)
    print(arr2)
    print()

    for j in range(step+1,len(A)):
        p=-(A[j][step]/A[step][step])
        print("R",j+1,"=>","R",j+1,"+",p,"*","R",step+1)
        elimination(j,p,step)
    for j in A:
        print(j)
    print()
    
    step+=1
    
