def quick_sort(nums, low, high):
    if high <= low:
        return 
    pivot = low +(high-low)//2
    s=low
    e = high
    while s < e:
        while nums[s] < nums[pivot]:
            s+=1
        while nums[e] > nums[pivot]:
            e-=1
        if e >= s:
            nums[s],nums[e] = nums[e],nums[s]
            e-=1
            s+=1
    quick_sort(nums,low,e)
    quick_sort(nums,s,high)
    


def partition(nums, low, high):
    pass


nums = [5,3,4,2,1]
quick_sort(nums,0,len(nums)-1)
print(nums)
