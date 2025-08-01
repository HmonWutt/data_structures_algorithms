def selection_sort(arr):
    for ind,i in enumerate(arr):
        smallest_ind = find_smallest(arr,ind)
        arr[ind],arr[smallest_ind]= arr[smallest_ind],arr[ind]
    return arr

def find_smallest(arr,start):
    smallest = (-1,float('inf'))
    for i in range(start,len(arr)):
        if arr[i]<smallest[1]:
            smallest = (i,arr[i])
    return smallest[0]

arr = [8,3,9,1,4]
#selection_sort(arr)

def recursive_find_smallest(arr,current,smallest,smallest_ind):
    if current == len(arr)-1:
        return smallest_ind
    if arr[current] < smallest:
        return recursive_find_smallest(arr,current+1,arr[current],current)
    return recursive_find_smallest(arr, current+1,smallest,smallest_ind)


def recursive_selection_sort(ind,arr):
    if ind == len(arr)-1:
        return arr
    smallest_ind = recursive_find_smallest(arr,ind,float('inf'),-1)
    arr[ind],arr[smallest_ind]= arr[smallest_ind],arr[ind]
    return recursive_selection_sort(ind+1,arr)

recursive_selection_sort(0,arr)
print(arr)