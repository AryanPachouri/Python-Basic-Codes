def swap_case(s):
    a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b="abcdefghijklmnopqrstuvwxyz"
    string=""
    for i in s:
        if i in a:
            j=i.lower()
            string+=j
        else:
            j=i.upper()
            string+=j
    
    return string

c=swap_case("pYTHONliST")
print(c)