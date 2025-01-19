# 2022 KAKAO TECH INTERNSHIP

from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = len(queue1)*3
    q1 = deque(queue1)
    q2 = deque(queue2)
    one = sum(q1)
    two = sum(q2)
    
    while True:
        if one > two:
            value = q1.popleft()
            q2.append(value)
            one -= value
            two += value
            answer += 1
        elif one < two:
            value = q2.popleft()
            q1.append(value)
            one += value
            two -= value
            answer += 1
        elif one == two:
            return answer
        if answer > limit:
            return -1
    
    return answer
