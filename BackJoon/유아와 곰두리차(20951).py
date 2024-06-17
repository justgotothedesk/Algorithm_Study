import sys

def dfs(cur, cnt):
    if cnt > 7:
        return 1

    if dp[cur][cnt] != -1:
        return dp[cur][cnt]

    dp[cur][cnt] = 0
    for nxt in graph[cur]:
        dp[cur][cnt] = (dp[cur][cnt] + dfs(nxt, cnt + 1)) % MOD

    return dp[cur][cnt]
  
ans = 0
MOD = 1e9 + 7
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dp = [[-1] * 8 for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    print(dfs(i, 1))
    ans = (ans + dfs(i, 1)) % MOD

print(f'{ans:.0f}')
