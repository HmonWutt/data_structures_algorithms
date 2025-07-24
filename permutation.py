def permutation(arr,mod):
    if not arr:
        print(mod)
        return 
    ch = arr[0]
    for i in range(len(mod)+1):
        
        first = mod[0:i]
        second = mod[i:]
        tmp = first+ch+second
        permutation(arr[1:],tmp)           
#print(permutation( "abc",""))

def permutation_lst(arr,mod):
    if not arr:
        #total.append(mod)
        return 1
        #return total,count
    each = arr[0]
    count = 0
    for i in range(len(mod)+1):
        temp = []
        temp+=mod[0:i]
        temp+=[each]
        temp+=mod[i:]

        count+=permutation_lst(arr[1:],temp)
    return count




        

    

print(permutation_lst(["a","b","c","d"],[]))