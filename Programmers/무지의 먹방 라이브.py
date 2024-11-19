# 2019 KAKAO BLIND RECRUITMENT

import heapq

def solution(food_times, k):
    answer = 0
    q = []
    
    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        heapq.heappush(q, [food_times[i], i+1])

    pre = 0
    length = len(food_times)

    while q:
        left = (q[0][0]-pre)*length
        if left <= k:
            pre, idx = heapq.heappop(q)
            k -= left
            length -= 1
        else:
            idx = k%length
            q.sort(key=lambda x: x[1])
            answer = q[idx][1]
            
            break

    return answer
