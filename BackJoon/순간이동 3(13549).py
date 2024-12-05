import sys
from collections import deque
input = sys.stdin.readline

start, end = map(int, input().split())
max = 100000
visited = [-1]*(max+1)
visited[start] = 0
q = deque()
q.append(start)

while q:
    now = q.popleft()
    if now == end:
        print(visited[now])
        break
    
    two = now*2
    if 0 <= two <= max and visited[two] == -1:
        visited[two] = visited[now]
        q.appendleft(two)
    
    for two in (now-1, now+1):
        if 0 <= two <= max and visited[two] == -1:
            visited[two] = visited[now]+1
            q.append(two)
