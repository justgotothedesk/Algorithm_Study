# 1. Floyd 알고리즘
def minimum(dist, n):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][mid]+dist[mid][end] < dist[start][end]:
                    dist[start][end] = dist[start][mid]+dist[mid][end]

def solution(n, road, K):
    answer = 0
    INF = 10000*10000
    dist=[[INF for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        dist[i][i] = 0
        
    for edge in road:
        dist[edge[0]-1][edge[1]-1] = min(edge[2], dist[edge[0]-1][edge[1]-1])
        dist[edge[1]-1][edge[0]-1] = min(edge[2], dist[edge[1]-1][edge[0]-1])
        
    minimum(dist, n)
    
    for i in range(len(dist[0])):
        if dist[0][i] <= K:
            answer += 1
    
    return answer

# 2. Dijkstra 알고리즘
import heapq

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]
    distance = [float('inf')]*N
    distance[0] = 0
    
    for start, end, cost in road:
        graph[start-1].append([cost, end-1])
        graph[end-1].append([cost, start-1])
        
    q = []
    heapq.heappush(q, [0, 0])
    
    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue
        else:
            for newcost, node in graph[now]:
                if distance[node] > newcost+cost:
                    distance[node] = newcost+cost
                    heapq.heappush(q, [newcost+cost, node])
    
    for i in distance:
        if i <= K:
            answer += 1

    return answer
