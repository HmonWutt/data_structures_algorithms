def selection_sort(arr):
    for i,_ in enumerate(arr):
        smallest = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]< smallest:
                smallest = arr[j]
            arr[i]=smallest
    return arr
#arr = [10,3,1,3,10,9]
arr=[9,3,2]
#print(selection_sort(arr))
def selection_Rsort(arr,i,o,smallest,ind):

    if o == len(arr)-1:
        return arr
    if i == len(arr):
        arr [o],arr[ind] = arr[ind],arr[o]
        smallest = arr[o]
        o+=1
        return selection_Rsort(arr,o,o+1,smallest,ind)
    else:
        if arr[i]< smallest:
            smallest = arr[i]
            ind =i
        return selection_Rsort(arr,i+1,o,smallest,ind)
i = 1
o = 0
print(selection_Rsort(arr,o+1,o,arr[o],-1))