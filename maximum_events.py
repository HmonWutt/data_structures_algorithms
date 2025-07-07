from heapq import heappush,heapify,heappop

def max_events(events):
    attending = 0
    events.sort()
    position = 0
    time = 1
    last_position = len(events)
    outstanding = []
    heapify(outstanding)
    heappush(outstanding,0)
    while (position < last_position or outstanding):
        if not outstanding:
            time = max(time,events[position][0])
        while position < last_position and time == events[position][0]:
            heappush(outstanding, events[position][1])
            position+=1
        
        while outstanding and outstanding[0] < time:    
            heappop(outstanding)
        
        if outstanding:
            attending +=1
            heappop(outstanding)

        
        time+=1
    return attending

alt_list = [[1,2],[2,3],[3,4]]
print(max_events([[1,2],[1,2],[3,3],[1,5],[1,5]]))

