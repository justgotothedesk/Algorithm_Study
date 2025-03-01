import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*max(2, n)
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1]+dp[i-2])%10007

print(dp[n-1])
