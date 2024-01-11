from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0]*n
    
    for i, j in edge:
        i, j = i-1, j-1
        graph[i].append(j)
        graph[j].append(i)
    
    q = deque()
    q.append(0)
    
    while q:
        idx = q.popleft()
        for node in graph[idx]:
            if visited[node] == 0:
                visited[node] = visited[idx]+1
                q.append(node)
    maxv = max(visited)
    
    for i in range(len(visited)):
        if i != 0 and visited[i] == maxv:
            answer += 1
            
    return answer
