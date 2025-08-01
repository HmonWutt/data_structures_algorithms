def binary_search(arr,target,start,end):
    mid = start+((end-start)//2)
    if arr[mid]==target:
        return mid
    if arr[mid]<target:
        return binary_search(arr[mid+1:], target,mid+1,end)
    else:
        return binary_search(arr[start:mid],target,start,mid)

    
arr = [1,4,5,8,9,10]
print(binary_search(arr,4,0,len(arr)-1))


