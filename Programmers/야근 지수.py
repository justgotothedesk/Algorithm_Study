# 가장 많은 피로도를 추출하기 위해서 자료구조 heap을 사용한다.

import heapq

def solution(n, works):
    answer = 0
    heap = []
  
    if sum(works) < n:
        return 0
    
    for i in works:
        heapq.heappush(heap, -i)
    
    for i in range(n):
        value = -heapq.heappop(heap)
        heapq.heappush(heap,-(value-1))
        
    for i in heap:
        answer += (-i)**2
      
    return answer
