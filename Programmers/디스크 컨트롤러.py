import heapq

def solution(jobs):
    answer = 0
    time = 0
    start = -1
    count = 0
    heap = []
    
    while count < len(jobs):
        for s, t in jobs:
            if start < s <= time:
                heapq.heappush(heap, [t, s])

        if heap:
            wt, ws = heapq.heappop(heap)
            start = time
            time += wt
            answer += time-ws
            count += 1
        else:
            time += 1
    
    return answer//len(jobs)
