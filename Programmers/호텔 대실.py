# 자료구조 heap을 이용해서 투숙시간을 기준으로 가장 빠른 시간을 체크한다.
# 퇴실 이후 10분이 쉬는 시간으로 사용되어야 하기 때문에, 이를 고려한다.

import heapq

def convert(time):
    start = time[0].split(":")
    end = time[1].split(":")
    return int(start[0])*60+int(start[1]), int(end[0])*60+int(end[1])

def solution(book_time):
    heap = []
    hotel = [-10]
    for i in book_time:
        start, end = convert(i)
        heapq.heappush(heap, (start, end))
    
    while heap:
        start, end = heapq.heappop(heap)
        if start >= hotel[0]+10:
            heapq.heappop(hotel)
            heapq.heappush(hotel, end)
        else:
            heapq.heappush(hotel, end)
            
    return len(hotel)
        
