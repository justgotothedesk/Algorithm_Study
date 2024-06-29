import sys

input = sys.stdin.readline
n = int(input())

ropes = [int(input()) for _ in range(N)]
ropes.sort()

answer = 0

for rope in ropes:
    if answer < rope*n:
        answer = rope*n
    n -= 1

print(answer)
