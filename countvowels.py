word=str(input())
vowels=["a","e","i","o","u"]
sum=0
for vowel in vowels:
    for j in range(len(word)):
        if vowel==word[j]:
            sum+=1
        
print(sum)