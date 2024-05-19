x=[]
for i in range(0,10):
    x_i=int(input())
    x.append(x_i)
    

l=[]
for j in x:
    if j not in l:
        l.append(j)