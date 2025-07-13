from collections import deque 
def free_up_time(eventTime, k,startTime,endTime,):
    count = len(startTime)
    ind = 0
    dq = deque([])
    while ind < count:
        if ind == 0:
            window_start = 0
        else:
            window_start = endTime[ind-1]

        if ind == count -1:
            window_end = eventTime
        else:
            window_end = startTime[ind+1] 
        event_length = endTime[ind] - startTime[ind]
        ind+=1
        gap_1 = window_start - startTime[ind]
        gap_ = window_end - window_start - event_length
        if dq:
            to_add = dq[-1]
        else:
            to_add = 0
        dq.append(gap+to_add) 
        if len(dq) > k :
            to_remove = dq.popleft()
            dq[-1] -= to_remove
      
    print(dq)
    return  max(dq)
        
    
#print(free_up_time(64,2,[29,49],[37,54]))
#print(free_up_time(10,1,[0,2,9],[1,4,10]))
#print(free_up_time(21,1,[7,10,16],[10,14,18]))
#print(free_up_time(30,2,[1,15,17],[14,17,29]))
#print(free_up_time(5,1,[1,3],[2,5]))
print(free_up_time(21,1,[7,10,16],[10,14,18]))