a=str(input())
b=str(input())

flag=1
for i in range (len(a)):
    if b[0]==a[i]:
        x=i
        break

for j in range (x,len(b)):
    for k in range (len(b)):
        if a[j]!=b[k]:
            flag=0

if flag==0:
    print("false")

elif flag==1:
    print("true")




