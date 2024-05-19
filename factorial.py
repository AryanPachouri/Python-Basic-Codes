n=int(input())
if(n==1):
    ans=1
else:
    i=1
    fac=1
    while i<n+1:
        fac*=i
        i+=1
    ans=fac

print(ans)