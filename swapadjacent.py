str1="abcde"
l=list(str1)
for i in range(0,len(l)-1,2):
    l[i],l[i+1] = l[i+1],l[i]
    

for j in l:
    print(j,end="")