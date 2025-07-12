
from heapq import heappush, heappop
class Solution:
    def mostBooked(self,n, meetings) -> int:
        used = [[0,i]for i in range(n)] 
        free = []
        count = [0]*n
        meetings.sort()
        for start, end in meetings:
            while used and used[0][0] <= start:
                _,room_number = heappop(used)
                heappush(free,room_number)
            if not free:
                end_time,room_number = heappop(used)
                meeting_len = end - start
                end  = end_time + meeting_len
                heappush(free,room_number)
            
            room_number = heappop(free)
            count[room_number] +=1
            heappush(used,[end,room_number])
        
        return count.index(max(count))


sol = Solution()
print(sol.mostBooked(3,[[1,20],[2,10],[3,5],[4,9],[6,8]]))


        




