import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

maxv = 21
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dist = [0]*(n+1)
depth = [0]*(n+1)
depth[0] = -1
parent = [[0]*maxv for _ in range(n+1)]

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

# lca를 통해 각 노드까지의 거리를 저장한다.
def make_depth(node, post, value):
    depth[node] = depth[post]+1
    visited[node] = True
    if node != 1:
        dist[node] += dist[post]+value
    
    for child, next_value in graph[node]:
        if not visited[child]:
            parent[child][0] = node
            make_depth(child, node, next_value)

def set_parent():
    make_depth(1, 0, 0)
    for i in range(1, maxv):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    if depth[a] > depth[b]:
        a, b = b, a
    
    for i in range(maxv-1, -1, -1):
        if depth[b]-depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return a

    for i in range(maxv-1, -1, -1):
        if parent[b][i] != parent[a][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[b][0]

set_parent()
for _ in range(int(input())):
    u, v = map(int, input().split())
    # lca를 사용하여 root부터 공통 조상까지와 공통 조상으로부터 각 node까지의 거리를 통해 두 정점과의 거리를 구한다.
    answer = dist[u]+dist[v]-2*dist[lca(u, v)]
    print(answer)
