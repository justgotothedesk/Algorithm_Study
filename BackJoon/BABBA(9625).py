import sys
input = sys.stdin.readline

k = int(input())

dp = [[1,0], [0,1]]

for i in range(2,k+1):
  a = dp[i-1][1]
  b = dp[i-1][0] + dp[i-1][1]

  dp.append([a,b])

print(*dp[k])
