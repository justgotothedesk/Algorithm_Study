# 2020 KAKAO INTERNSHIP

from collections import deque

def solution(n, path, order):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False]*n
    step = [0]*n
    after = {}
    q = deque()
    q.append(0)
    
    for v, w in path:
        graph[v].append(w)
        graph[w].append(v)

    # 해당 방을 방문한 후, 방문해야하는 방을 구하기 위해 반대로 넣어준다.
    for a, b in order:
        step[b] = a
        
    while q:
        now = q.popleft()

        # 현재 위치를 방문하기전에 들러야하는 정점이 존재하고 아직 그 정점을 방문하지 않았다면 체크해둔다.
        # step[now] : now를 방문하기 위해 이전에 방문해야하는 정점
        if step[now] and not visited[step[now]]:
            after[step[now]] = now
            continue
        
        visited[now] = True
        answer += 1
        
        for adj in graph[now]:
            if not visited[adj]:
                q.append(adj)
                
        if now in after:
            q.append(after[now])
            
    return answer == n
