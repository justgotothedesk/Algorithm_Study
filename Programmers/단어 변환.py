from collections import deque

def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    visited = [False]*len(words)
    
    while q:
        now, dist = q.popleft()
        if now == target:
            return dist
        for i in range(len(words)):
            same = 0
            for j in range(len(words[i])):
                if words[i][j] == now[j]:
                    same += 1
            if same == len(words[i])-1 and not visited[i]:
                visited[i] = True
                q.append([words[i], dist+1])
                
    return 0
