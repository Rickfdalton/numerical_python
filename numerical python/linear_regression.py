x=[0,0.693,1.098,1.386,1.609]
y=[-0.693,0.53,1.22,1.74,2.13]

n=len(x)
E_x=sum(x)
E_y=sum(y)
E_xy=0
E_x2=0
E_y2=0

for i in range(n):
    E_x2+=x[i]**2
    E_y2+=y[i]**2
    E_xy+=x[i]*y[i]

print("e=y-(a1x+x0)")
print("E_x:",E_x)
print("E_y:",E_y)
print("E_xy:",E_xy)
print("E_x2:",E_x2)
print("E_y2:",E_y2)
print("a1:",(n*E_xy-E_x*E_y)/(n*E_x2-(E_x)**2))
print("a0:",(E_y*E_x2-E_x*E_xy)/(n*E_x2-(E_x)**2))
