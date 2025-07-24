def combination(string,mod):
    total = []
    if not string:
        return [mod]
    ch = string[0]
    total+=combination(string[1:],mod+ch)
    total+=combination(string[1:],mod)
    return total

    

   

print(combination("abc",""))