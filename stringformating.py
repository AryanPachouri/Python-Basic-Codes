number=int(input())

 
width = len(bin(number)[2:])
for i in range(1,number+1):
    bi=str(i).rjust(width)
    o=oct(i)[2:].rjust(width)
    h=hex(i)[2:].upper().rjust(width)
    b=bin(i)[2:].rjust(width)
    print(f"{bi} {o} {h} {b}")