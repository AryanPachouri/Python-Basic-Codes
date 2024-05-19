def wrap(string, max_width):
    i=0
    while i <=len(string):
        print(string[i:i+max_width])
        i+=max_width
     

string=input()
max_width=int(input())
print(wrap(string,max_width))