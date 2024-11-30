import sys
input = sys.stdin.readline

n = int(input())

dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

temp = 1000000001
answer = 0

for i in range(n-1):
    if cost[i] <= temp:
        temp = cost[i]
    answer += temp*dist[i]

print(answer)
