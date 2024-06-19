def win(p, q):
    if dp[p][q] >= 0:
        return dp[p][q]

    for i in range(3):
        if b[i] <= p and not win(p - b[i], q):
            dp[p][q] = 1
            return dp[p][q]

    for j in range(3):
        if b[j] <= q and not win(p, q - b[j]):
            dp[p][q] = 1
            return dp[p][q]
          
    dp[p][q] = 0
    return dp[p][q] 

dp = [[-1 for _ in range(501)] for _ in range(501)]
b = list(map(int, input().split()))

for _ in range(5):
    k1, k2 = map(int, input().split())
    if win(k1, k2):
        print("A")
    else:
        print("B")
