# target 블록의 상하좌우가 target 블록과 동일한지 묻는 문제이다.
# 따라서 target 블록을 계속 큐에 넣어줘서 해당 블록을 중심으로 상하좌우 이동하며 같은 지를 판단하면 된다.

from collections import deque

def solution(board, h, w):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(board)
    target = board[h][w]
    q = deque()
    q.append([h, w])
    visited = [[False]*n for _ in range(n)]
    
    for i in range(4):
        nx = h+dx[i]
        ny = w+dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == target:
            q.append([h, w])
            visited[nx][ny] = True
            answer += 1
    
    return answer
