import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
maps = [list(input().strip()) for _ in range(r)]
swan = [[False]*c for _ in range(r)]
water = [[False]*c for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
#본 문제의 핵심이다.시간 초과를 방지하기 위해서 bfs 이후에 녹을 얼음과 이동할 백조를 큐에 미리 넣어둔다.
sq, sq_temp = deque(), deque()
wq, wq_temp = deque(), deque()
ex, ey = 0, 0
answer = 0

def melt():
    while wq:
        x, y = wq.popleft()
        maps[x][y] = '.'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not water[nx][ny]:
                if maps[nx][ny] == '.':
                    wq.append([nx, ny])
                #다음에 녹을 얼음을 미리 큐에 넣는다.
                elif maps[nx][ny] == 'X':
                    wq_temp.append([nx, ny])
                water[nx][ny] = True

def move():
    while sq:
        x, y = sq.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not swan[nx][ny]:
                if maps[nx][ny] == '.':
                    sq.append([nx, ny])
                #다음에 이동할 경로를 미리 큐에 넣는다.
                elif maps[nx][ny] == 'X':
                    sq_temp.append([nx, ny])
                swan[nx][ny] = True
    return False

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'L':
            if not sq:
                sq.append([i, j])
                swan[i][j] = True
            else:
                ex, ey = i, j
            maps[i][j] = '.'
        if maps[i][j] == '.':
            wq.append([i, j])
            water[i][j] = True

while True:
    melt()
    if move():
        break
    answer += 1
    sq = sq_temp
    sq_temp = deque()
    wq = wq_temp
    wq_temp = deque()

print(answer)
