from collections import Counter
class Solution:
    def totalFruit(self, fruits) :
        items = Counter(fruits)
        if len(items) <=2:
             return sum(items.values())
        current_fruit = -1
        counts = []

        for ind,fruit in enumerate(fruits):
            if fruit !=current_fruit:
                current_fruit = fruit
                counts.append(self.takeFruit(fruits[ind:]))
        return max(counts)
            
    def takeFruit(self,fruits):
        num_of_fruits = {}
        
        for fruit in fruits:
            if fruit in num_of_fruits:
                num_of_fruits[fruit]+=1
            
            elif len(num_of_fruits) <=1:
                    num_of_fruits[fruit]=1
            else:
                    break
                   
        return self.count(num_of_fruits)

    def count(self,basket):
        count = 0
        for _,value in basket.items():
                count+=value
        return count
        

lst = [3,3,3,1,2,1,1,2,3,3,4]
sol  = Solution()
print(sol.totalFruit(lst))

