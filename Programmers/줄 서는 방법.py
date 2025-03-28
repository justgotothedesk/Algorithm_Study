# 시간 초과 방법
# def dfs(temp, data, result):
#     if not temp:
#         result.append(data)
        
#         return
    
#     for i in range(len(temp)):
#         dfs(temp[:i]+temp[i+1:], data+[temp[i]], result)

# def solution(n, k):
#     answer = []
#     temp = []
#     result = []
    
#     for i in range(1, n+1):
#         temp.append(i)
    
#     dfs(temp, [], result)
        
#     answer = result[k-1]
    
#     return answer

import math

def solution(n, k):
    answer = []
    number = []
    
    for i in range(1, n+1):
        number.append(i)
    
    while number:
        perm = math.factorial(n-1)
        idx = (k-1)//perm
        answer.append(number.pop(idx))
        k %= perm
        n -= 1

    return answer
