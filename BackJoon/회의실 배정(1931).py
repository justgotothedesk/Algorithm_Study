import sys

input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
obj = arr[0][1]
for i in range(1, N):

    if obj <= arr[i][0]:
        obj = arr[i][1]
        cnt += 1

print(cnt)
