# 하나씩 순서대로 골라가며 우선순위에 따라서 실행 여부를 판단하므로 deque 자료구조를 사용한다.
# 해당 프로세스가 내가 원하는 프로세스임을 나타내는 큐와 우선순위 순서인 큐를 하나씩 만들어준다.
# 각 큐를 pop해주면서 우선순위가 제일 높다면 실행시키고 그렇지 않다면 다시 큐에 넣어준다.

from collections import deque

def solution(priorities, location):
    answer = 1
    q = deque(priorities)
    temp = [0]*len(priorities)
    temp[location] = 1
    idxq = deque(temp)
    
    while q:
        now = q.popleft()
        idx = idxq.popleft()
        
        if not q:
            return answer
        
        if max(q) <= now:
            if now == priorities[location] and idx:
                return answer
            answer += 1
        else:
            q.append(now)
            idxq.append(idx)
    
    return answer
