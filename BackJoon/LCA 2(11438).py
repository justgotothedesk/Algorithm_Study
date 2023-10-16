import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

maxv = 21
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
depth = [0]*(n+1)
#바로 위의 부모 노드를 표시하기 위한 배열
parent = [[0]*maxv for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for child in graph[node]:
        if not visited[child]:
            parent[child][0] = node
            dfs(child, d+1)

#해당 부분이 문제 해결의 핵심이라고 생각한다. 바로 위의 부모노드는 얼마인지 표시한다.
def setparent():
    dfs(1, 0)
    for i in range(1, maxv):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

#이전에 작성한 parent 배열을 통해 공통 조상이 같아질 때까지 반복문을 수행한다.
def lca(a, b):
    #b를 깊이가 더 깊은 노드로 선정한다.
    if depth[a] > depth[b]:
        a, b = b, a
    
    for i in range(maxv-1, -1 ,-1):
        if depth[b]-depth[a] >= 2**i:
            b = parent[b][i]
    
    if a == b:
        return b
    
    for i in range(maxv-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[b][0]

setparent()

for _ in range(int(input())):
    u, v = map(int, input().split())
    print(lca(u, v))
