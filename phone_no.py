def num(arr,mod):
    if not arr:
        print (mod)
        return
    digit = arr[0]
    if digit==1:
        num(arr[1:],mod)
    else:
        start  = 3*(digit-2)
        end = 3*(digit-1)
        if digit >=7:
            shift = digit//8
            start = start+shift
            end = end+(digit%2)+shift
        for i in range(start,end):
            ch = chr(ord("a")+i)
            num(arr[1:],mod+ch)

num([2,9],"")