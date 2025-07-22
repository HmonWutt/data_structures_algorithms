def qs(arr,s,e):
    if s >= e:
        return arr
    l= s
    r= e
    p = s+(e-s)//2
    while l < r:
        while arr[l]<arr[p]:
            l+=1

        while arr[r]> arr[p]:
            r-=1

        if l< r:
            arr[r],arr[l] = arr[l],arr[r]
            l+=1
            r-=1
    qs(arr,s,p)
    qs(arr,p+1,e)


#arr = [1,10,9,4,3,2]
#arr = [5,4,3,2,1]
arr = [3,2]
print(qs(arr,0,len(arr)-1)  )
print(arr)