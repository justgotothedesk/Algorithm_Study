from collections import deque

def solution(tickets):
    answer = []
    q = deque()
    q.append(["ICN", ["ICN"], []])
    
    while q:
        target, history, visited = q.popleft()
        
        if len(history) == len(tickets)+1:
            answer.append(history)
        
        for idx, [start, end] in enumerate(tickets):
            if start == target and idx not in visited:
                q.append([end, history+[end], visited+[idx]])
    
    answer.sort()
    
    return answer[0]

# 이전에 틀렸던 풀이
# def solution(tickets):
#     answer = ["ICN"]
    
#     tickets.sort(key = lambda x:x[1])
    
#     for i, j in tickets:
#         if i == "ICN":
#             answer.append(j)
#             tickets.remove([i, j])
#             target = j
#             break
    
#     while tickets:
#         tickets.sort(key = lambda x:x[1])
#         for i, j in tickets:
#             if i == target:
#                 answer.append(j)
#                 tickets.remove([i, j])
#                 target = j
#                 break
    
#     return answer
