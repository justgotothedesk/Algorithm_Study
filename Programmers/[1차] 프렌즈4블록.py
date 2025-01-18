# 2018 KAKAO BLIND RECRUITMENT

def fall(board):
    result = set()
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j].isalpha() and board[i][j] == board[i][j-1] == board[i-1][j-1] == board[i-1][j]:
                result.add((i, j))
                result.add((i, j-1))
                result.add((i-1, j-1))
                result.add((i-1, j))
    
    return list(result)

def solution(m, n, board):
    answer = 0
    pop_board = []
    
    for j in range(len(board[0])):
        temp = []
        for i in range(len(board)-1, -1, -1):
            temp.append(board[i][j])
        pop_board.append(temp)
    
    while True:
        result = fall(pop_board)
        
        if not result:
            break
        
        answer += len(result)
        result.sort(key = lambda x:-x[1])
        for i, j in result:
            pop_board[i].pop(j)
            pop_board[i].append("0")
        
    return answer
