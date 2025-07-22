import copy
def combination(string,mod):
    if not string:
        if not mod:
            return []
        return [mod]


    ch = string[0]
    left = combination(string[1:], mod+ch)
    #ascii = combination(string[1:],mod+str(ord(ch)))
    right =combination(string[1:],mod)
    left+=right
    #left+=ascii
    return left

#print(combination("abbc",""))
def comination_iterative(string):
    lst = [[]]
    for i in string:
        for j in range(len(lst)): 
            temp = []
            temp+=lst[j]
            temp.append(i)
            lst.append(temp)
            
        
    return lst[1:]
#print(comination_iterative([1,2,2])) 


def comination_duplicate(string):
    lst = [[]]
    for i,_ in enumerate(string): 
        if (i >0 and string[i] == string[i-1]):
            s = e 
            e = len(lst)
        else:
            s = 0
            e = len(lst) 
        for j in range(s,e): 
            temp = []
            temp+=lst[j]
            temp.append(string[i])
            lst.append(temp)
            
        
    return lst[1:]
print(comination_duplicate([1,2,2])) 