# BFS를 사용하여 풀 수 있는 간단한 문제이다.
# maps 값이 str 형으로 되어 있기 때문에 문자형으로 이루어진 숫자가 있을 경우에는 int로 변환한 후에 더해주어야 오류가 발생하지 않는다.

from collections import deque

def solution(maps):
    answer = []
    row = len(maps)
    col = len(maps[0])
    visited = [[False]*col for _ in range(row)]
    q = deque()
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                q.append([i, j, maps[i][j]])
                now = 0
                while q:
                    x, y, cost = q.popleft()
                    now += int(cost)
                    
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < row and 0 <= ny < col:
                            if maps[nx][ny] != 'X' and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([nx, ny, maps[nx][ny]])
                if now:
                    answer.append(now)
    
    if not answer:
        return [-1]
    else:
        answer.sort()
    
    return answer
