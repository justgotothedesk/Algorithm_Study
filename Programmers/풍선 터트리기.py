# 가장 왼쪽과 가장 오른쪽으로부터 제거할 수 있는 경우를 각각 계산한다.

def solution(a):
    answer = 0
    minv = 2_000_000_000
    index = 0
    
    if len(a) == 1:
        return 1
    
    for i in range(len(a)):
        if a[i] < minv:
            minv = a[i]
            index = i
            
    left = a[0]
    right = a[-1]
  
    for i in range(len(a)):
        if i == index:
            break
        if i == 0:
            answer += 1
            continue
        if a[i] < left:
            answer += 1
            left = a[i]
    
    for i in range(len(a)-1, -1, -1):
        if i == index:
            break
        if i == len(a)-1:
            answer += 1
            continue
        if a[i] < right:
            answer += 1
            right = a[i]
    
    answer += 1
    
    return answer
