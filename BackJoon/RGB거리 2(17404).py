import sys

sys.setrecursionlimit(5000)

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

dp = [[[1 << 30] * 3 for _ in range(3)] for _ in range(N)]

def recur(row, col, first_col):
    if row == N:
        return 0

    if dp[row][col][first_col] != 1 << 30:
        return dp[row][col][first_col]

    for j in range(3):
        if j == col:
            continue
        elif row == N - 2 and j == first_col:
            continue
        dp[row][col][first_col] = min(dp[row][col][first_col], recur(row + 1, j, first_col) + house[row][col])

    return dp[row][col][first_col]

answer = 1 << 30
for i in range(3):
    answer = min(answer, recur(0, i, i))

print(answer)
