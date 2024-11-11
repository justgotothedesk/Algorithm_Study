def solution(n):
    answer = 0
    dp = [0]*16
    
    dp[0] = 1
    dp[1] = 1
    
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j]*dp[i-j-1]
    
    return dp[n]
