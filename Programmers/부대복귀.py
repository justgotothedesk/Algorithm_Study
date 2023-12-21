from collections import deque

def bfs(dest, graph, road):
    q = deque([dest])
    road[dest] = 0
    while q:
        value = q.popleft()
        for i in graph[value]:
            if road[i] == -1:
                q.append(i)
                road[i] = road[value]+1
    return road

def solution(n, roads, sources, destination):
    answer = []
    road = [-1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    
    for e, v in roads:
        graph[e].append(v)
        graph[v].append(e)
    
    bfs(destination, graph, road)
    
    for i in sources:
        answer.append(road[i])
    
    return answer
