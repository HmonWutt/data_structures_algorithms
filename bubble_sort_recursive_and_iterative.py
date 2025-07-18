def main(n):
    helper(n,0)

def helper(n,ind):
    if n == 0:
        return
    if n == ind:
        print()
        helper(n-1,0)
    
    else:
        print("*", end="")
        helper(n,ind+1)

def bubble_sort(arr,n,ind):
    if n == 0:
        return arr
    if ind==n-1:
        return bubble_sort(arr,n-1,0)
    else:
        if arr[ind]> arr[ind+1]:
            arr[ind],arr[ind+1] = arr[ind+1],arr[ind]
        return bubble_sort(arr,n,ind+1)
arr = [1,5,2,1,9]
#print(bubble_sort(arr,len(arr),0))

def bubb_sort(arr):
    for i in range(len(arr),-1,-1):

        for j in range(1,i):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]

    return arr
print(bubb_sort(arr))  