import sys

input = sys.stdin.readline
n = int(input())

stair = [int(input()) for _ in range(N)]+[0]
dp = [0]*(n+1)
dp[0] = stair[0]
dp[1] = stair[0]+stair[1]

for i in range(2, n):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])

print(dp[-2])
