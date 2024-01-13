from collections import deque

def bfs(graph, start):
    visited = [False]*len(graph)
    visited[start] = True
    q = deque()
    q.append(start)
    edge = 0
    
    while q:
        now = q.popleft()
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                q.append(node)
                edge += 1
                
    return edge

def solution(n, wires):
    answer = float('inf')
    graph = [[] for _ in range(n)]
    
    for i in range(len(wires)):
        graph = [[] for _ in range(n)]
        temp = []
        for idx, [start, end] in enumerate(wires):
            if i == idx:
                continue
            graph[start-1].append(end-1)
            graph[end-1].append(start-1)
        
        temp.append(bfs(graph, wires[i][0]-1))
        temp.append(bfs(graph, wires[i][1]-1))
        
        if abs(temp[0]-temp[1]) < answer:
            answer = abs(temp[0]-temp[1])       
    
    return answer
