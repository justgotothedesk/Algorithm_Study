# 정사각형이 만들어진다는 것은 한 지점으로부터 오른쪽, 아래, 오른쪽 대각선 아래 방향으로 이어진다는 것이다.
# 따라서 이를 전환하여, 한 점으로부터 위, 왼쪽, 왼쪽 대각선 위 방향으로 어떤 값이 있는지 확인하여 정사각형 갯수를 찾는다.

def solution(board):
    answer = 0
    
    if len(board) == 1:
        if sum(board[0]):
            return 1
        else:
            return 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1])+1
            answer = max(answer, board[i][j])
    
    return answer**2
  
# 실패 코드
# def solution(board):
#     answer = 0
#     row = []
#     col = []
#     dd = []
#     ff = []
    
#     for i in range(len(board)):
#         row.append(sum(board[i]))
#     for i in range(len(board[0])):
#         temp = 0
#         for j in range(len(board)):
#             temp += board[j][i]
#         col.append(temp)

#     for i in range(0, len(row)-1):
#         now = row[i]
#         count = 1
#         for j in range(i+1, len(row)):
#             if now <= row[j]:
#                 count += 1
#         if count >= now:
#             dd.append(now)
#     if row[-1] == 1:
#         dd.append(1)
          
#     for i in range(0, len(col)-1):
#         now = col[i]
#         count = 1
#         for j in range(i+1, len(col)):
#             if now <= col[j]:
#                 count += 1
#         if count >= now:
#             ff.append(now)
#     if col[-1] == 1:
#         ff.append(1)

#     dd = list(set(dd))
#     ff = list(set(ff))
#     gg = []

#     for element in dd:
#         if element in ff:
#             gg.append(element)
            
#     if gg:
#         gg.sort(reverse = True)
#         return gg[0]**2
#     else:
#         a = max(dd)
#         b = max(ff)
#         fin = min(a, b)
#         return fin**2
