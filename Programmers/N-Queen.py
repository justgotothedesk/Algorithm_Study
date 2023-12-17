answer = 0
def solution(n):
    global answer
    visited = [False]*n
    board = [0]*n
    
    def check(x):
        for i in range(x):
            if abs(board[x]-board[i]) == x-i:
                return False
        return True
    
    def dfs(x):
        global answer
        if x == n:
            answer += 1
            return
        for y in range(n):
            if visited[y]:
                continue
            board[x] = y
            if check(x):
                visited[y] = True
                dfs(x+1)
                visited[y] = False
    
    dfs(0)
    
    return answer
