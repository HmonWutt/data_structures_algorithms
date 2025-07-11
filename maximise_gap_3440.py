
class Solution:
    def maxFreeTime(self, eventTime, startTime, endTime):
        top_three_gaps = self.make_top_three(eventTime, startTime, endTime)

        biggest = top_three_gaps[0][0]
        for ind in range(len(startTime[:-1])):
            if ind == 0:
                end = 0
            else:
                end = endTime[ind-1]
            event_length = endTime[ind] - startTime[ind]
            continous_space = startTime[ind+1] - end
            biggest = max(biggest, continous_space - event_length)
            for gap_index in range(3):
                if top_three_gaps[gap_index][1] != ind + 1 \
                    and top_three_gaps[gap_index][1] != ind \
                    and event_length <= top_three_gaps[gap_index][0]:
                    biggest = max(biggest, continous_space)
                    break

        return biggest
    
    def make_top_three(self,eventTime, startTime, endTime):
        top_three_gaps = [(-1, -1), (-1, -1), (-1, -1)]
        startTime.append(eventTime)
        endTime.append(eventTime)
        for i in range(len(startTime)):
            if i == 0:
                gap = startTime[i] - 0
            else:
                gap = startTime[i]-endTime[i-1]
                
            for place in range(2, -1, -1):
                if gap > top_three_gaps[place][0]:
                    top_three_gaps[place] = (gap, i)
                    break
            for place in range(2, 0, -1):
                if top_three_gaps[place-1][0] < top_three_gaps[place][0]:
                    tmp = top_three_gaps[place]
                    top_three_gaps[place] = top_three_gaps[place-1]
                    top_three_gaps[place - 1] = tmp

        return top_three_gaps
                    


sol = Solution()
#sol.maxFreeTime(5,[1,3],[2,5])
#sol.maxFreeTime(10, [0,7,9], [1,8,10])
tmp = sol.maxFreeTime(10,[0,3,7,9], [1,4,8,10])
print(tmp)