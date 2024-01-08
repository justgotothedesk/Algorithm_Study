# 실패 .. 정확도 : 30.2

from collections import deque

def solution(maze):
    answer = 0
    startRx, startRy, startBx, startBy = 0, 0, 0, 0
    targetRx, targetRy, targetBx, targetBy = 0, 0, 0, 0
    row = len(maze)
    col = len(maze[0])
    rv = set([(startRx, startRy)])
    bv = set([(startBx, startBy)])

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 3:
                targetRx = i
                targetRy = j
            elif maze[i][j] == 4:
                targetBx = i
                targetBy = j
            elif maze[i][j] == 1:
                startRx = i
                startRy = j
            elif maze[i][j] == 2:
                startBx = i
                startBy = j

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([startRx, startRy, startBx, startBy, 0])

    while q:
        rx, ry, bx, by, dist = q.popleft()
        if (rx == targetRx and ry == targetRy) and (bx == targetBx and by == targetBy):
            return dist
        
        elif rx == targetRx and ry == targetRy:
            for i in range(4):
                nx = bx + dx[i]
                ny = by + dy[i]
                if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] != 5 and nx != rx and ny != ry and (nx, ny) not in bv:
                    bv.add((nx, ny))
                    q.append([rx, ry, nx, ny, dist+1])
                    
        elif bx == targetBx and by == targetBy:
            for i in range(4):
                nx = rx + dx[i]
                ny = ry + dy[i]
                if 0 <= nx < row and 0 <= ny < col and maze[nx][ny] != 5 and nx != bx and ny != by and (nx, ny) not in rv:
                    rv.add((nx, ny))
                    q.append([nx, ny, bx, by, dist+1])

        else:
            for i in range(4):
                for j in range(4):
                    rnx = rx + dx[i]
                    rny = ry + dy[i]
                    bnx = bx + dx[j]
                    bny = by + dy[j]
                    if 0 <= rnx < row and 0 <= bnx < row and 0 <= rny < col and 0 <= bny < col and maze[rnx][rny] != 5 and maze[bnx][bny] != 5 and not (rnx == bx and rny == by) and not (rnx == bnx and rny == bny) and not (bnx == rx and bny == ry) and (rnx, rny) not in rv and (bnx, bny) not in bv:
                        rv.add((rnx, rny))
                        bv.add((bnx, bny))
                        q.append([rnx, rny, bnx, bny, dist+1])

    return answer
