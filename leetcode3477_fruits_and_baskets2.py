class Solution:
    def numOfUnplacedFruits(self, fruits, baskets) :
        for fruit in fruits:
            num_baskets = len(baskets)
            basket_index = 0
            while basket_index < num_baskets:
                if fruit <= baskets[basket_index]:
                    baskets.pop(basket_index)
                    
                    break
                else:
                    basket_index+=1
        if not baskets:
            return 0
        return len(baskets)
            
                    
fruits = [3,6,1]        
baskets = [6,4,7]

sol = Solution()
print(sol.numOfUnplacedFruits(fruits,baskets))