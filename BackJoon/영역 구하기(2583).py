from collections import deque
import sys
input = sys.stdin.readline

x, y, n = map(int, input().split())

graph = [[True]*y for _ in range(x)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

for _ in range(n):
    y1, x1, y2, x2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = False

def bfs(r, c):
    q = deque()
    q.append((r, c))
    dist = 0
    
    while q:
        a, b = q.popleft()
        dist += 1
        
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            
            if 0 <= nx < x and 0 <= ny < y and graph[nx][ny]:
                graph[nx][ny] = False
                q.append((nx, ny))
    
    return dist

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]:
            graph[i][j] = False
            value = bfs(i, j)
            answer.append(value)

answer.sort()
print(len(answer))
print(" ".join(map(str, answer)))
