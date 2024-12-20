import sys
input = sys.stdin.readline

def dfs(node, depth):
    if depth == 5:
        print(1)
        sys.exit()
    
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)
    visited[node] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

for i in range(n):
    dfs(i, 1)
  
print(0)
