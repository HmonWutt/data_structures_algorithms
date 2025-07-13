from bisect import bisect_right

class Solution:

    def maxValue(self, events, k ):
        self.sorted_events = sorted(events,key=lambda x:x[0])
        self.starts = [x[0] for x in self.sorted_events]
        self.n = len(self.sorted_events)
        self.dp = [[-1] * self.n for _ in range(k+1)]
        return self.dfs(0,k)

    def dfs(self,index,k):
        if index == self.n or k == 0:
            return 0

        if self.dp[k][index] != -1:
            return self.dp[k][index]
        
        next_index = bisect_right(self.starts, self.sorted_events[index][1])
        take = self.sorted_events[index][2] + self.dfs(next_index,k - 1)
        skip = self.dfs(index+1,k)
        
        self.dp[k][index]= max(take, skip)

        return self.dp[k][index]


sol = Solution()
val = sol.maxValue([[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]], 3)

print(val)
