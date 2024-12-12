# 2022 KAKAO TECH INTERNSHIP

import heapq
from collections import defaultdict

def solution(n, paths, gates, summits):
    answer = []
    summits.sort()
    graph = defaultdict(list)
    inf = int(1e9)
    ingates = set()
    insummits = set()
    
    for g in gates:
        ingates.add(g)
    for s in summits:
        insummits.add(s)
    
    for start, end, cost in paths:
        if start in ingates or end in insummits:
            graph[start].append((end, cost))
        elif start in insummits or end in ingates:
            graph[end].append((start, cost))
        else:
            graph[start].append((end, cost))
            graph[end].append((start, cost))
    
    def dijkstra():
        q = []
        result = [inf]*(n+1)
        
        for gate in gates:
            result[gate] = 0
            heapq.heappush(q, (0, gate))
        
        while q:
            cost, now = heapq.heappop(q)
            if cost > result[now]:
                continue
            
            for next_node, next_cost in graph[now]:
                if result[next_node] > max(next_cost, result[now]):
                    result[next_node] = max(next_cost, result[now])
                    heapq.heappush(q, (result[next_node], next_node))
    
        return result

    result = dijkstra()
    idx = 0
    maxv = inf
    
    for i in summits:
        if result[i] == inf:
            continue
        if result[i] < maxv:
            idx = i
            maxv = result[i]
    
    answer.append(idx)
    answer.append(maxv)
    
    return answer
