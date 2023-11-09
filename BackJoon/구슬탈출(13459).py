import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'R':
            redx, redy = i, j
        elif graph[i][j] == 'B':
            bluex, bluey = i, j
        elif graph[i][j] == 'O':
            targetx, targety = i, j

# 벽에 닿거나 출구에 다다르기 전까지 이동시키는 함수이다.
def move_ball(x, y, dx, dy):
    move = 0
    while graph[x+dx][y+dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        move += 1
    
    return x, y, move

# 빨간 공과 파란 공이 바로 붙어있는 경우에는 이동하는 방향으로부터 조금 더 가까운 색깔의 공이 벽이나 출구까지 이동하고 나머지 공은 한 칸 덜 이동한다.
# 이를 고려한 bfs 코드이다.
def bfs():
    q = deque()
    q.append([redx, redy, bluex, bluey, 1])
    visited = set((redx, redy, bluex, bluey))

    while q:
        rx, ry, bx, by, dist = q.popleft()
        if dist > 10:
            break

        for i in range(4):
            nrx, nry, r_move = move_ball(rx, ry, dx[i], dy[i])
            nbx, nby, b_move = move_ball(bx, by, dx[i], dy[i])

            if graph[nbx][nby] != 'O':
                if graph[nrx][nry] == 'O':
                    return dist

                # 서로 다른 색깔의 공이 바로 붙어있는 경우이다.
                if (nrx, nry) == (nbx, nby):
                    if r_move > b_move:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                
                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append([nrx, nry, nbx, nby, dist+1])
    
    return -1

answer = bfs()
if answer != -1:
    print(1)
else:
    print(0)

                
