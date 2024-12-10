from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

def bfs(x, y):
    visited = [[False]*c for _ in range(r)]
    q = deque([(x, y, 0)])
    visited[x][y] = True
    maxd = 0
    
    while q:
        x, y, dist = q.popleft()
        maxd = max(maxd, dist)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, dist+1))
              
    return maxd
        
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'L':
            answer = max(answer, bfs(i, j))
    
print(answer)
