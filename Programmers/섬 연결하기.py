# heapq를 사용하여 최적의 경로를 탐색한다.

import heapq

def solution(n, costs):
    answer = 0
    count = 0
    visited = [False]*n
    graph = [[] for _ in range(n)]
    q = [[0, 0]]
    
    for e, v, w in costs:
        graph[e].append([w, v])
        graph[v].append([w, e])
    
    while q:
        if count == n:
            break
        cost, now = heapq.heappop(q)
        
        if not visited[now]:
            visited[now] = True
            count += 1
            answer += cost
            
            for i in graph[now]:
                heapq.heappush(q, i)
        
    return answer
