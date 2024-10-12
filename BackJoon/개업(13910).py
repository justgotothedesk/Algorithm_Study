import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
w_size = list(map(int, input().split()))

dp = [1 << 30] * (N + 1)

def recur(total):
    if total < 0:
        return 10000000
    elif total == 0:
        return 0

    if dp[total] != 1 << 30:
        return dp[total]

    for i in range(M):
        dp[total] = min(dp[total], recur(total - w_size[i]) + 1)
        for j in range(i + 1, M):
            dp[total] = min(dp[total], recur(total - w_size[i] - w_size[j]) + 1)

    return dp[total]


ans = recur(N)
if ans >= 10000000:
    print(-1)
else:
    print(ans)
