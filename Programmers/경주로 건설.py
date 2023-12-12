# 2020 카카오 인턴십

import heapq

def solution(board):
    answer = 0
    r = len(board)
    result = [[[float('inf')]*r for _ in range(r)] for _ in range(4)]
    heap = [[0, 0, 0, 0], [0, 0, 0, 2]]
    
    for i in range(4):
        result[i][0][0] = 0
    
    while heap:
        dist, x, y, dir = heapq.heappop(heap)
        
        for dx, dy, dd in [[1, 0, 0], [-1, 0, 1], [0, 1, 2], [0, -1, 3]]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < r and 0 <= ny < r and board[nx][ny] == 0:
                if dd == dir:
                    newdist = dist+100
                else:
                    newdist = dist+600
                if result[dd][nx][ny] > newdist:
                    result[dd][nx][ny] = newdist
                    heapq.heappush(heap, [newdist, nx, ny, dd])
    
    answer = min(result[0][r-1][r-1], result[1][r-1][r-1], result[2][r-1][r-1], result[3][r-1][r-1])
    
    return answer
