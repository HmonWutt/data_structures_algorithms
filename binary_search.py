def binary_search(arr,target):
    mid = len(arr)//2
    if mid == 0:
        return -1
    if target == arr[mid]:
        return mid
    if target > arr[mid]:
        return binary_search(arr[mid+1:],target)
    return binary_search(arr[:mid],target)
    

binary_search([1,2,4,6,8,11],13)
    








