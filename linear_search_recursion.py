def search(arr, target, ind):
    if ind == len(arr):
        return -1
    elif arr[ind]==target:
        return ind
    return search(arr,target,ind+1)
     
print(search([1,4,2,18],0,0))