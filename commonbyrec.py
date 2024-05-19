# def check(string1,string2):
#       c=min(len(string1),len(string2))
#       for i in range(c):
        
#         if string1[0]==string2[i]:
#             return 1+check(string1[1:],string2)
#         else:
#             return check(string1[1:],string2)

# string1=str(input())
# string2=str(input())

# print(check(string1,string2))

def check(string1, string2):
    if not string1 or not string2:
        return 0

    if string1[0] in string2:
        return 1 + check(string1[1:], string2)
    else:
        return check(string1[1:], string2)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = check(string1, string2)
print("Number of common characters:", result)

