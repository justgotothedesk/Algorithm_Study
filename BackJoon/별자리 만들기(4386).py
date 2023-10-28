import sys
input = sys.stdin.readline
import heapq

n = int(input())
star = []
for _ in range(n):
    x, y = map(float, input().split())
    star.append([x, y])
graph = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        graph[i][j] = ((star[i][0]-star[j][0])**2+(star[i][1]-star[j][1])**2)**(1/2)

q = []
heapq.heappush(q, [0, 0])
visited = set()
answer = 0

#시간초과를 막기 위해, 자료구조 heap을 사용한다.
while len(visited) < n:
    cost, now = heapq.heappop(q)
    if now in visited:
        continue
    answer += cost
    visited.add(now)
    for next in range(n):
        if now != next and next not in visited:
            heapq.heappush(q, [graph[now][next], next])

print(round(answer, 2))
