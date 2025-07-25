def phone_num(arr,mod):
    total = []
    if not arr:
        return [mod]
    digit = arr[0]
    if digit ==1:
        total+=phone_num(arr[1:],mod)
    else:
        start = (digit-2) * 3
        end = (digit-1) *3
        if digit >= 7 :
            shift = digit//8
            start += shift
            end+= (digit%2)+shift
    
        for i in range(start,end):
            
            combo = mod+chr(ord('a')+i)
            total+=phone_num(arr[1:],combo)  
    return total

print(phone_num([2,9],""))