from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False]*n
    q = deque()
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j]:
                graph[i].append(j)
                
    for i in range(len(graph)):
        if visited[i]:
            continue
        answer += 1
        visited[i] = True
        q.append(i)
        while q:
            v = q.popleft()
            for next in graph[v]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
    
    return answer
