n=int(input())

for i in range(1,n*2+1,2):
    print(" "*((n*2-i)//2)+"*"*i) 
for i in range(n*2-3,0,-2):
    print(" "*((n*2-i)//2)+"*"*i) 