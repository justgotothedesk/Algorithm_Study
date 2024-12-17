from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

q = deque()
answer = -1
q.append((start, 0))
visited = set()

while q:
    now, dist = q.popleft()
    visited.add(now)
    if now == end:
        answer = dist
        break
    
    for next in graph[now]:
        if next not in visited:
            q.append((next, dist+1))

print(answer)
