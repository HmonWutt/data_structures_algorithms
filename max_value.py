
from heapq import heappush,heapify,heappop

def max_events(events,k):   
    events = sorted(events, key=lambda x: x[2])
    position = 0
    time = 1
    last_position = len(events)
    end_days = []
    heapify(end_days)
    max_events = 0
    values = []
    heapify(values)
    biggest_value = 0
    heappush(end_days,(0,0))
    while end_days or position < last_position :
        if not end_days:
            time = max(time,events[position][0])
        
        while position <last_position and time == events[position][0]:
            heappush(end_days,(events[position][1],events[position][2]))
            position +=1

        while end_days[0][0]<time:
            heappop(end_days)

        if end_days:
            _,value = heappop(end_days)
            heappush(values,(-value))

    while max_events < k and values:
        biggest_value+= (-heappop(values))
        max_events+=1
    return biggest_value

max_events([[1,2,4],[3,4,3],[2,3,1]],2)