# 2024 KAKAO WINTER INTERNSHIP
# 해당 문제는 두 가지를 신경써야한다.
# 첫번째로 임의로 추가한 정점은 inbound가 없는 정점들 중에서 outbound가 가장 큰 정점이다.
# 두번째로 임의로 추가한 정점으로부터 시작되는 정점들이 각 나누어진 그래프들의 종류이다.
# 따라서 각 그래프들을 순회하면서 정점 수와 간선 수를 비교하며 도넛, 막대, 8자 그래프를 구분한다.

from collections import deque

def solution(edges):
    answer = []
    maxv = -float('inf')
    for i, j in edges:
        if i > j:
            if maxv < i:
                maxv = i
        else:
            if maxv < j:
                maxv = j
                
    center = []
    for i in range(maxv):
        center.append([0, 0])
    
    for i, j in edges:
        center[i-1][1] += 1
        center[j-1][0] += 1
    
    node = 0
    nodev = 0
    for i in range(len(center)):
        if center[i][0] != 0:
            continue
        if center[i][1] > nodev:
            nodev = center[i][1]
            node = i
    node += 1
    answer.append(node)
    
    donut = 0
    stick = 0
    eight = 0

    graph = [[] for _ in range(maxv)]
    startv = []
    for start, end in edges:
        if end == node:
            continue
        elif start == node:
            startv.append(end-1)
            continue
        graph[start-1].append(end-1)
        
    def bfs(start_v):
        discovered = set() # set이 아닌 배열로 방문 여부를 판단하면 시간초과가 발생한다.
        node = 0
        edge = 0
        stack = deque([start_v])
        while stack:
            v = stack.popleft()
            if v not in discovered:
                discovered.add(v)
                node += 1
                for w in graph[v]:
                    stack.append(w)
                    edge += 1
        return node, edge
    
    temp = []
    for i in startv:
        temp.append(bfs(i))
        
    for node, edge in temp:
        if node-1 == edge:
            stick += 1
        elif node == edge:
            donut += 1
        else:
            eight += 1
            
    answer.append(donut)
    answer.append(stick)
    answer.append(eight)
    
    return answer
