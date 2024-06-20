import sys

sys.setrecursionlimit(10000)
N = int(input())
arr = list(map(int, input().split())) + [0]

dp = [[-1] * (N + 1) for _ in range(N + 1)]

def recur(cur, pre):
    if cur >= N:
        return 0

    if dp[cur][pre] != -1:
        return dp[cur][pre]

    if arr[cur] > arr[pre]:
        dp[cur][pre] = max(recur(cur + 1, cur) + arr[cur], recur(cur + 1, pre))
    else:
        dp[cur][pre] = recur(cur + 1, pre)

    return dp[cur][pre]

print(recur(0, -1))
