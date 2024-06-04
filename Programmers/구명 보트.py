from collections import deque

def solution(people, limit):
    answer = 0
    que = deque(sorted(people))
  
    while que:
        if(len(que) == 1):
            answer += 1
            break
          
        if(que[0]+que[-1]) <= limit:
            que.pop()
            que.popleft()
            answer += 1
        else:
            que.pop()
            answer += 1
          
    return answer
