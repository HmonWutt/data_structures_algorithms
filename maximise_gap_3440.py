
class Solution:
    def maxFreeTime(self, eventTime, startTime, endTime):
        top_three_gaps = self.make_top_three(eventTime, startTime, endTime)
        
        biggest = -1
        space = 0
        for ind, i in enumerate(startTime[:-1]):
            gap_index = 0
            while gap_index < 3:
                event_length = endTime[ind] - startTime[ind]
                if ind == 0:
                    end = 0
                else:
                    end = endTime[ind-1]
                continous_space = startTime[ind+1] - end
                if top_three_gaps[gap_index][1] != ind + 1 \
                    and top_three_gaps[gap_index][1] != ind \
                    and event_length <= top_three_gaps[gap_index][0]:
                    space = continous_space
                else:
                    space = continous_space - event_length
                if space > biggest:
                    biggest = space
                gap_index+=1
  
        return biggest
    
    def make_top_three(self,eventTime, startTime, endTime):
        top_three_gaps = []
        startTime.append(eventTime)
        endTime.append(eventTime)
        for i in range(len(startTime)):
            if i == 0:
                gap = startTime[i] - 0
            else:
                gap = startTime[i]-endTime[i-1]
                
            top_three_gaps.append([gap,i])
        top_three_gaps = sorted(top_three_gaps, key=lambda x: x[0],reverse=True)
        if len(top_three_gaps)>3:
            top_three_gaps = top_three_gaps[:3]
        return top_three_gaps
                    


sol = Solution()
#sol.maxFreeTime(5,[1,3],[2,5])
#sol.maxFreeTime(10, [0,7,9], [1,8,10])
sol.maxFreeTime(10,[0,3,7,9], [1,4,8,10])