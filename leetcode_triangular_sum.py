def triangularSum(nums): 
        if len(nums)==1:
            return nums
        end = len(nums)
        rows = []
        rows.append(nums)
        print(rows)
        for row in range(1,end):
            cols = end - row
            temp = []
            for col in range(cols):

                num = rows[row-1][col]+rows[row-1][col+1]
                temp.append(num%10)
            rows.append(temp)
            temp =[]
        return rows[-1][0]
print(triangularSum([1,2,3,4,5]))