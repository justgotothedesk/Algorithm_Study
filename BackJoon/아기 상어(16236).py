import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 9:
            startx, starty = i, j
size = 2

def bfs(x, y, size):
    q = deque()
    q.append([x, y])
    eat = []
    visited = [[False]*n for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    visited[x][y] = True

    while q:
        r, c = q.popleft()

        for i in range(4):
            nx = r+dx[i]
            ny = c+dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    dist[nx][ny] = dist[r][c]+1
                    if graph[nx][ny] < size and graph[nx][ny] != 0:
                        eat.append([nx, ny, dist[nx][ny]])
    
    return sorted(eat, key = lambda x:[-x[2], -x[0], -x[1]])

count = 0
answer = 0

while True:
    new = bfs(startx, starty, size)

    if len(new) == 0:
        break
    
    nx, ny, time = new.pop()
    answer += time
    graph[nx][ny] = 0
    graph[startx][starty] = 0
    startx, starty = nx, ny
    count += 1

    if count == size:
        count = 0
        size += 1

print(answer)
