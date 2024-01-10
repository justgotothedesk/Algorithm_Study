# 진짜 너무너무 궁금한 문제. 
# 딱 하나 차이 나는데 정답이 아니고 뭐가 다르고 뭐가 문제인지 모르겠음

# solution 함수에 궁금한 점 적어놨음
from collections import deque

def rotate(board):
    row = len(board)
    col = len(board[0])
    result = [[0]*row for _ in range(col)]
    count = 0
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                count += 1
            result[j][row-i-1] = board[i][j]
    
    return count, result

def compact(board):
    x, y = zip(*board)
    r = max(x)-min(x)+1
    c = max(y)-min(y)+1
    result = [[0]*c for _ in range(r)]
    
    for i, j in board:
        i -= min(x)
        j -= min(y)
        result[i][j] = 1
    
    return result

def bfs(board, value):
    row = len(board)
    col = len(board[0])
    visited = [[False]*col for _ in range(row)]
    q = deque()
    result = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == value and not visited[i][j]:
                temp = [[i, j]]
                visited[i][j] = True
                q.append([i, j])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny] == value:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            temp.append([nx, ny])
                result.append(temp)
                
    return result

def solution(game_board, table):
    answer = 0
    dd = []
    empty_blocks = bfs(game_board, 0)
    puzzles = bfs(table, 1)

    for empty in empty_blocks:
        filled = False
        compact_empty = compact(empty)

        for puzzle_origin in puzzles:
            if filled == True:
                break
            puzzle = compact(puzzle_origin)
            for i in range(4):
                count, puzzle = rotate(puzzle) #count, rotate_puzzle = rotate(puzzle)로 하면 답이 틀림
                if compact_empty == puzzle:
                    answer += count
                    puzzles.remove(puzzle_origin)
                    filled = True
                    break
                    
    return answer
