class Solution:
    def generate(self, numRows: int) :
        lst = []
        if numRows == 0:
            return [1]
        lst.append([1])
        for i in range(1,numRows):
            temp = [1]
            for j in range(1,i):
                previous_row = lst[i-1]
                item_at_previous_index = previous_row[j-1]
                item_at_current_index = previous_row[j]
                current_value = item_at_previous_index +item_at_current_index
                temp.append(current_value)
            temp.append(1)
            lst.append(temp)
            temp=[]
        return lst
sol = Solution()
print(sol.generate(7))