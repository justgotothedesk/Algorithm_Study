# bfs 알고리즘을 사용하여 start에서 n을 더한 값, 2를 곱한 값, 3을 곱한 값으로 세 가지의 경우를 생각한다.
# 이전에 방문한 경우를 판단하여야 한다. 하지만 이전에 방문한 경우보다 횟수가 작은 경우도 있기 때문에 딕셔너리를 사용하여 더 작은 경우를 기록한다.

from collections import deque

def bfs(start, target, n):
    dd = [n, 2, 3]
    q = deque()
    q.append([start, 0])
    visited = {}
    visited[str(start)] = 0
    
    while q:
        now, dist = q.popleft()
        if now == target:
            return dist
        
        elif now > target:
            continue
        
        for i in range(3):
            if i == 0:
                if str(now+n) in visited.keys():
                    if visited[str(now+n)] > dist+1:
                        visited[str(now+n)] = dist+1
                        q.append([now+n, dist+1])
                else:
                    q.append([now+n, dist+1])
                    visited[str(now+n)] = dist+1
            elif i == 1:
                if str(now*2) in visited.keys():
                    if visited[str(now*2)] > dist+1:
                        visited[str(now*2)] = dist+1
                        q.append([now*2, dist+1])
                else:
                    q.append([now*2, dist+1])
                    visited[str(now*2)] = dist+1
            else:
                if str(now*3) in visited.keys():
                    if visited[str(now*3)] > dist+1:
                        visited[str(now*3)] = dist+1
                        q.append([now*3, dist+1])
                else:
                    q.append([now*3, dist+1])
                    visited[str(now*3)] = dist+1
                
    return -1

def solution(x, y, n):
    answer = 0
    start = x
    target = y
    
    answer = bfs(start, target, n)
    
    return answer
