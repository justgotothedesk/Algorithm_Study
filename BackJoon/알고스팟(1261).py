from collections import deque

c, r = map(int, input().split())

graph = []

for i in range(r):
    graph.append(list(map(int, input())))

dist = [[-1] * c for _ in range(r)]
dx = [1, 0, -1, 0] 
dy = [0, 1, 0, -1]

queue = deque()
queue.append([0, 0])
dist[0][0] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if dist[nx][ny] == -1:
            if graph[nx][ny] == 0:
                dist[nx][ny] = dist[x][y]
                queue.appendleft([nx, ny]) 
            else:
                dist[nx][ny] = dist[x][y]+1 
                queue.append([nx, ny])

print(dist[r-1][c-1])
