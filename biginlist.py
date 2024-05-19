l=int(input()).split()
big=0
for i in range (len(l)):
    if l[i]>=big:
        big=l[i]
    else:
        big=big

print(big)