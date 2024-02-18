# 2022 KAKAO BLIND RECRUITMENT
# 트리 자료구조를 사용하기 보다, 양방향 그래프를 사용하여 이동이 용이하게 한다.
# 그래프에서 좌, 우로 계속하여 이동할 수 있기 때문에 3차원 배열을 사용하여 방문 여부를 확인한다.
# 방문한 노드를 다시 방문했을 경우에 양이나 늑대가 추가되면 안되기 때문에 다른 값을 넣어준다.
# 그래프의 한 쪽 방향을 모두 탐색했을 경우에는 기존의 값을 다시 넣어주어, 다른 방향으로 탐색이 가능하게 한다.

def dfs(now, sheep, wolf):
    global graph, visited, answer, ginfo
    if visited[now][sheep][wolf]:
        return
    visited[now][sheep][wolf] = True
    
    backs = sheep
    backw = wolf
    backg = ginfo[now]
    
    if ginfo[now] == 0:
        sheep += 1
    elif ginfo[now] == 1:
        wolf += 1
    ginfo[now] = -1
    
    if sheep > wolf:
        answer = max(answer, sheep)
        for next_node in graph[now]:
            dfs(next_node, sheep, wolf)
    
    ginfo[now] = backg
    visited[now][backs][backw] = False

def solution(info, edges):
    global graph, visited, answer, ginfo
    graph = [[] for _ in range(len(info))]
    visited = [[[False]*(len(info)+1) for _ in range(len(info)+1)] for _ in range(len(info)+1)]
    answer = 0
    ginfo = info

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    dfs(0, 0, 0)    

    return answer
