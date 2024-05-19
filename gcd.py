a=int(input())
b=int(input())
c=min(a,b)

for i in range(2,c+1):
    if a%i==0 and b%i==0:
        gcd=i

print(gcd)