def merge_sort(arr,start,end):

    if end - start == 1:
        return 
    mid = start + (end-start)//2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid,end)
    sort(arr,start,mid,end)



def sort(arr,start,mid,end):
    i = start
    j = mid
    new_arr = []
    while i < mid and j < end:
        if arr[i] > arr[j]:
            new_arr.append(arr[j])
            j+=1
        else:
            new_arr.append(arr[i])
            i+=1
    while i < mid:
        new_arr.append(arr[i])
        i+=1
    while j <end:
        new_arr.append(arr[j])
        j+=1
    arr[start:end] = new_arr

arr = [2,7,1,3,10,6]

merge_sort(arr,0,len(arr))
print(arr)