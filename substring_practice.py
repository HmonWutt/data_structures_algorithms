def combination(arr,mod):
    ans = []
    if not arr:
        return ans+[mod]
    ch = arr[0]
    
    ans+=combination(arr[1:],mod+ch)
    ans+=combination(arr[1:],mod)
    return ans

print(combination("abc",""))

def combination_with_repetition(arr,ind,mod):
    ans=[]
    if ind == len(arr) :
        return ans+[mod]
    ch = arr[ind]
    j = ind+1
    while j < len(arr) and ch==arr[j]:
        j+=1

    ans += combination_with_repetition(arr,j,mod) 
    ans += combination_with_repetition(arr,ind+1,mod+ch)   
    return ans
print(combination_with_repetition("abbc",0,""))