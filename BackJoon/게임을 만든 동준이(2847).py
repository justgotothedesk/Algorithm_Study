N = int(input())

arr = [int(input()) for _ in range(N)]

cnt = 0

for i in range(1, N)[::-1]:

    if arr[i - 1] >= arr[i]:
        cnt += (arr[i - 1] - arr[i] + 1)
        arr[i - 1] -= (arr[i - 1] - arr[i] + 1)

print(cnt)
