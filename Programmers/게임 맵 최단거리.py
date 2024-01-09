from collections import deque

def solution(maps):
    answer = 0
    row = len(maps)
    col = len(maps[0])
    visited = [[False]*col for _ in range(row)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append([0, 0, 1])
    visited[0][0] = True
    
    while q:
        x, y, dist = q.popleft()
        if x == row-1 and y == col-1:
            return dist
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]\
            and maps[nx][ny]:
                visited[nx][ny] = True
                q.append([nx, ny, dist+1])
    
    return -1
