# 2019 카카오 개발자 겨울 인턴십 

def solution(board, moves):
    answer = 0
    bucket = []
    new_board = []
    
    for j in range(len(board[0])):
        temp = []
        for i in range(len(board)-1, -1, -1):
            if board[i][j]:
                temp.append(board[i][j])
        new_board.append(temp)
    
    for move in moves:
        move -= 1
        if new_board[move]:
            bucket.append(new_board[move].pop())
        else:
            continue
        
        if len(bucket) >= 2:
            if bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()
                answer += 2

    return answer
