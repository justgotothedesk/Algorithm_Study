# 하나씩 순서대로 골라가며 우선순위에 따라서 실행 여부를 판단하므로 deque 자료구조를 사용한다.
# 해당 프로세스가 내가 원하는 프로세스임을 나타내는 큐와 우선순위 순서인 큐를 하나씩 만들어준다.
# 각 큐를 pop해주면서 우선순위가 제일 높다면 실행시키고 그렇지 않다면 다시 큐에 넣어준다.

from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    my = [0 for _ in range(len(priorities))]
    my[location] = 1
    my = deque(my)
    
    while(my):
        value = que.popleft()
        check = my.popleft()

        # 더 높은 우선순위가 있는 경우
        if len(que) > 1 and max(que) > value:
            que.append(value)
            my.append(check)
        else:
            answer += 1
            if check == 1:
                break
            
    return answer
