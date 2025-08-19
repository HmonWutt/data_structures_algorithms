def selection_sort(nums):
    for current in range(len(nums)):
        smallest = current
        for j in range(current,len(nums)):
            if nums[smallest] > nums[j]:
                smallest = j
        nums[current],nums[smallest] = nums[smallest],nums[current]
nums = [4,5,2,1,3]
selection_sort(nums)
print(nums)
