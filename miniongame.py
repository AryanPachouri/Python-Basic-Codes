s="banana"
stuart=0
kevin=0


def isvowel(k):
    flag=True
    if k in "aeiouAEIOU":
        flag=True
    else:
        flag=False

    return flag


for i in range(len(s)):
    while isvowel(s[i])==True:
        for j in range(len(s)):
            kevin+=(s.count(s[i:i+j]))

for i in range(len(s)):
    while isvowel(s[i])==False:
        for j in range(len(s)):
            stuart+=s.count(s[i:i+j])

maxi=max(stuart,kevin)
if maxi==stuart:
    print(f"Staurt {maxi}")
else:
    print(f"Kevin {maxi}")

            



