from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    
q = deque()
q.append(1)

answer = [0]*(n+1)

while q:
    now = q.popleft()
    
    for next in graph[now]:
        if answer[next] == 0:
            answer[next] = now
            q.append(next)

for i in range(2, len(answer)):
    print(answer[i])
