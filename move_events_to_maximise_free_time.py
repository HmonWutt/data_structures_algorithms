def free_up_time(eventTime, k,startTime,endTime,):
    count = len(startTime)
    gaps = []
    maxFree = 0
    

    for i in range(0,count):
        if i == 0:
            window_start = 0
        else:
            window_start = endTime[i-1]

        if i == count -1:
            window_end = eventTime
        else:
            try:
                window_end = startTime[i+1] 
            
            except IndexError:
                window_end = eventTime
        
        if window_start == startTime[i] or window_end == endTime[i]:
            moved = 0
        else:
            moved = 1
        event_length = endTime[i] - startTime[i]
        gap = window_end - window_start - event_length
        gaps.append([gap,moved])
    total = 0
    print("len: ",len(gaps),gaps)
    for i in range(len(gaps)-1):
        for j in range(i,i+k):
            print(j)
        
            total  += (gaps[j][0] *gaps[j][1])
        maxFree = max(maxFree,total)
        total = 0
        
    return maxFree

    



print(free_up_time(34,2,[0,17],[14,19]))

    