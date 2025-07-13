def sorted(array,ind):
    if ind == len(array):
        return True
    return array[ind]  >array[ind-1] and sorted(array, ind+1) 

print(sorted([3,1,4,5],1))