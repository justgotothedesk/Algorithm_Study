import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    temp = 0
    q = deque()
    visited = set()
    q.append((i, j, 0))
    visited.add((i, j, 0))
    
    while q:
        x, y, dist = q.popleft()
        if dist > temp:
            temp = dist
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] > graph[i][j] and (nx, ny, dist+1) not in visited:
                q.append((nx, ny, dist+1))
                visited.add((nx, ny, dist+1))
                
    return temp

for i in range(len(graph)):
    for j in range(len(graph[i])):
        answer = max(answer, bfs(i, j))
        
print(answer)
