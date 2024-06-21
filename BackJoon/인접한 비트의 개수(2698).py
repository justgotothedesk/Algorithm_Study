def dfs(depth, cnt, cur):
    if depth == N:
        if cnt == K:
            return 1
        else:
            return 0

    if dp[depth][cnt][cur] != -1:
        return dp[depth][cnt][cur]

    dp[depth][cnt][cur] = 0

    dp[depth][cnt][cur] += dfs(depth + 1, cnt, not cur)
    dp[depth][cnt][cur] += dfs(depth + 1, cnt + (cur * cur), cur)

    return dp[depth][cnt][cur]

N = int(input())
for _ in range(N):
    N, K = map(int, input().split())
    dp = [[[-1, -1] for _ in range(101)] for _ in range(N + 1)]
    print(dfs(0, 0, 0))
