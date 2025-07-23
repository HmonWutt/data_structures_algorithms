def quick_sort(arr,s,e):
    left = s
    right = e
    pivot = s+(e-s)//2
    if s == e:
        return arr
    while left<=right:
        while arr[left]<arr[pivot]:
            left +=1
        while arr[right]>arr[pivot]:
            right-=1

        if left <=right:
            arr[left],arr[right] =arr[right],arr[left]
            left+=1
    quick_sort(arr,s,pivot)
    quick_sort(arr,pivot+1,e)
arr = [8,3,8,9,2,4,6,7,1,2]
print(quick_sort(arr,0,len(arr)-1))
print(arr)