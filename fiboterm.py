a=int(input())
def fibo(n):
    if n==1:
        return 1 
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(1,a):
    if fibo(i)==a:
        print("yes")
        break  

