# 2022 KAKAO BLIND RECRUITMENT
# skill에 따라서 건물의 내구도를 일일이 깎으면 시간초과가 발생하게 된다.
# 그러므로 skill마다 파괴되거나 회복되는 범위의 꼭짓점을 마킹하여 한꺼번에 계산한다.

def solution(board, skill):
    answer = 0
    temp = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for i in skill:
        if i[0] == 1:
            temp[i[1]][i[2]] -= i[5]
            temp[i[1]][i[4]+1] += i[5]
            temp[i[3]+1][i[2]] += i[5]
            temp[i[3]+1][i[4]+1] -= i[5]
        elif i[0] == 2:
            temp[i[1]][i[2]] += i[5]
            temp[i[1]][i[4]+1] -= i[5]
            temp[i[3]+1][i[2]] -= i[5]
            temp[i[3]+1][i[4]+1] += i[5]
    
    for i in range(len(temp)):
        for j in range(1, len(temp[i])):
            temp[i][j] += temp[i][j-1]
    
    for i in range(len(temp[0])):
        for j in range(1, len(temp)):
            temp[j][i] += temp[j-1][i]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] >= 1:
                answer += 1
    
    return answer
