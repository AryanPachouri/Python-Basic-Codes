string=str(input())
 
for i in range(0,len(string)):
    flag=0
    for j in range(0,len(string)):
        #checking if two characters are equal
        if(string[i]==string[j] and i!=j):
            flag=1
            break
    if(flag==0):
        print(string[i],end="")