# 한 칸만 이동하는 것이 아니라 한 번에 이동할 수 있는 모든 거리를 미끄러지듯이 이동하는 것이기 때문에 while문을 사용한다.
# 이동 횟수를 나타내는 visited 배열을 사용하여 이동하면 이전 배열에서 +1한 값을 넣어준다.

from collections import deque

def bfs(board, start, end):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    row = len(board)
    col = len(board[0])
    visited = [[0]*col for _ in range(row)]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == start:
                visited[i][j] = 1
                q.append([i, j])
    
    while q:
        x, y = q.popleft()
        if board[x][y] == end:
            return visited[x][y]-1
        
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]

                # 미끄러져 이동했는데 해당 좌표가 이동할 수 없는 곳일 경우
                if 0 <= nx < row and 0 <= ny < col and board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    break

                # 미끄러져 이동했는데 해당 좌표가 좌표의 범위를 넘을 경우
                if nx < 0 or nx >= row or ny < 0 or ny >= col:
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                  
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append([nx, ny])
    
    return -1

def solution(board):
    answer = bfs(board, "R", "G")
  
    return answer
