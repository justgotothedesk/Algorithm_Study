from collections import deque
import sys
input = sys.stdin.readline

row, col = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
#대각선도 움직이기 위한 좌표
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]
count = 0

def bfs(r, c):
    q = deque()
    q.append([r, c])
    flag = True

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[r][c] == maps[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny]) 
                elif maps[nx][ny] > maps[r][c]: #해당 조건에 맞지 않으면 count하지 않는다
                    flag = False
                    break
    if flag:
        return True
    
    return False

for i in range(row):
    for j in range(col):
        if not visited[i][j] and bfs(i, j):
            count += 1

print(count)

