# 2023 KAKAO BLIND RECRUITMENT
# 1. 해당 10진수를 2진수로 변환하고, 해당 노드 갯수로 만들 수 있는 포화 이진트리의 노드 갯수를 로그 값으로 계산하여, 부족한 부분을 '0'으로 채워준다.
# 2. 이진트리가 만족하지 않는 경우는 조상이 0이지만, 자식이 1인 경우이다. 따라서 재귀 함수를 통해서 해당 경우가 있으면 0을 반환한다.

import math

def dfs(now, prev):
    mid = len(now)//2
    if now:
        if now[mid] == '1':
            son = True
        else:
            son = False
    else:
        return True
    
    if son and not prev:
        return False
    
    return dfs(now[mid+1:], son) and dfs(now[:mid], son)

def solution(numbers):
    answer = []
    binary = []
    
    for number in numbers:
        temp = bin(number)[2:]
        length = 2**int(math.log(len(temp), 2)+1)-1
        temp = '0'*(length-len(temp))+temp
        binary.append(temp)
    
    for i in binary:
        if i == '1':
            answer.append(1)
        elif i[len(i)//2] == '1' and dfs(i, True):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer
