import sys

sys.setrecursionlimit(50000)

N = int(input())
homes = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[1 << 30] * 3 for _ in range(N + 1)]

def recur(row, col):
    if row == N + 1:
        return 0

    if dp[row][col] != 1 << 30:
        return dp[row][col]

    for i in range(3):
        if row >= 1 and i == col:
            continue
        dp[row][col] = min(dp[row][col], recur(row + 1, i) + homes[row][col])

    return dp[row][col]

print(recur(0, 0))
