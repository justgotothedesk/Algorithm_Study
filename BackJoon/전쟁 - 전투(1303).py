import sys
from collections import deque

col, row = map(int, input().split())
board = [list(input()) for _ in range(row)]
visited = [[False]*col for _ in range(row)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

B = 0
W = 0
q = deque()

def bfs(i, j):
    q.append([i, j])
    visited[i][j] = True
    answer = 0

    while q:
        x, y = q.popleft()
        answer += 1
        for k in range(4):
            nx = dx[k]+x
            ny = dy[k]+y
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                q.append([nx, ny])

    return answer

for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            temp = bfs(i, j)
            if board[i][j] == 'W':
                W += temp**2
            else:
                B += temp**2

print(W, B)
