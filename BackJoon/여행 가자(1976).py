import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n):
    now = i+1
    temp = list(map(int, input().split()))
    
    for j in range(len(temp)):
        if temp[j]:
            graph[now].append(j+1)
            
travel = list(map(int, input().split()))

q = deque()
q.append(travel[0])
visited = set()
visited.add(travel[0])

while q:
    now = q.popleft()
    
    for next in graph[now]:
        if next not in visited:
            q.append(next)
            visited.add(next)

flag = 1            
for t in travel:
    if t not in visited:
        flag = 0
        break

if flag:
    print("YES")
else:
    print("NO")
