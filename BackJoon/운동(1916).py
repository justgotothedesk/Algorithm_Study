import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[float('inf')]*(n+1) for _ in range(n+1)]

for _ in range(m):
  start, end, dist = map(int, input().split())
  graph[start][end] = dist

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

answer = float('inf)      
      
for i in range(1, n):
  answer = min(answer, graph[i][i])

if answer == float('inf'):
  print(-1)
else:
  print(answer)
