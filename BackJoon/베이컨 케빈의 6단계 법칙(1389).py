import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
inf = 100
graph = [[inf]*(n) for _ in range(n)]

for i in range(len(graph)):
    graph[i][i] = 0

for v, e in info:
    graph[v-1][e-1] = 1
    graph[e-1][v-1] = 1

#input값이 크지 않으므로 floyd 알고리즘을 사용하였다
for mid in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][end] > graph[start][mid]+graph[mid][end]:
                graph[start][end] = graph[start][mid]+graph[mid][end]

answer = 0
minv = float('inf')

for i in range(len(graph)):
    total = sum(graph[i])
    if minv > total:
        minv = total
        answer = i+1
    elif minv == total:
        answer = min(answer, i+1)        

print(answer)
