import sys
input = sys.stdin.readline
from collections import deque

r, c, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(r)]
startX, startY = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, cost, last):
    q = deque()
    q.append([a, b, cost, last])
  
    #해당 부분이 핵심이다.
    #시간복잡도를 줄이기 위해서 벽을 부순 수에 해당하는 3차원 배열을 만들어서 방문 여부를 판단한다.
    visited = [[[False]*c for _ in range(r)] for _ in range(k+1)]
    visited[last][a][b] = True

    while q:
        x, y, dist, wall = q.popleft()
        if x == r-1 and y == c-1:
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
          
            #3차원 배열에 벽을 부순 횟수와 좌표에 따라서 조건에 맞다면 큐에 넣어준다.
            if 0 <= nx < r and 0 <= ny < c and not visited[wall][nx][ny]:
                if graph[nx][ny] == 0:
                    visited[wall][nx][ny] = True
                    q.append([nx, ny, dist+1, wall])
                elif graph[nx][ny] == 1 and wall > 0:
                    visited[wall][nx][ny] = True
                    q.append([nx, ny, dist+1, wall-1])

answer = bfs(startX, startY, 1, k)
if answer == None:
    answer = -1
print(answer)
