# bfs 알고리즘을 이용한다.
# 먼저 시작점으로부터 레버까지의 최소 거리를 구한다.
# 그리고 레버로부터 도착점까지의 최소 거리를 구하고 더해준다.

from collections import deque

def bfs(start, end, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    row = len(maps)
    col = len(maps[0])
    visited = [[False]*col for _ in range(row)]
    check = False
    q = deque()
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == start:
                check = True
                visited[i][j] = True
                q.append([i, j, 0])
                break
        if check:
            break
    
    while q:
        i, j, cost = q.popleft()
        if maps[i][j] == end:
            return cost
        for c in range(4):
            x = i+dx[c]
            y = j+dy[c]
            
            if 0 <= x < row and 0 <= y < col and maps[x][y] != "X":
                if not visited[x][y]:
                    visited[x][y] = True
                    q.append([x, y, cost+1])
    return -1
                    
def solution(maps):
    answer = 0

    # 시작점에서부터 레버까지
    first = bfs("S", "L", maps)

    # 레버에서부터 도착점까지
    second = bfs("L", "E", maps)
    
    if first != -1 and second != -1:
        answer = first+second
    else:
        answer = -1
        
    return answer
