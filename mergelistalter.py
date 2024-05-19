l1=[10, 20, 30]
l2=[40, 50, 60]
n=len(l1)
m=len(l2)
l=[]

for i in range(len(l1)):
    for j in l1,l2:
        l.append(j[i])

print(l)