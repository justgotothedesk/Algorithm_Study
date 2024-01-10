# 일반적인 좌표를 사용하면 bfs 순회에서 잘못된 경로가 나오기 때문에 좌표를 2배 늘려준다.
# 각 사각형들의 겹치는 부분을 제거하기 위해서 board를 -1로 초기화하고 테두리 부분이 아닌 내부 부분일 경우 0으로 설정해준다.

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[-1]*102 for _ in range(102)]
    visited = [[False]*102 for _ in range(102)]
    characterX, characterY = characterX*2, characterY*2
    itemX, itemY = itemX*2, itemY*2
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for x1, y1, x2, y2 in rectangle:
        x1, y1 = x1*2, y1*2
        x2, y2 = x2*2, y2*2
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                else:
                    if board[i][j] != 0:
                        board[i][j] = 1
    
    q = deque()
    q.append([characterX, characterY, 0])
    visited[characterX][characterY] = True
    
    while q:
        x, y, dist = q.popleft()
        if x == itemX and y == itemY:
            return dist//2
          
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and not visited[nx][ny] and board[nx][ny] == 1:
                q.append([nx, ny, dist+1])
                visited[nx][ny] = True

    return answer
