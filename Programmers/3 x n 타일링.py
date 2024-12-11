def solution(n):
    answer = 0
    
    # n = 1 -> 0
    # n = 2 -> 3
    # n = 3 -> 0
    # n = 4 -> 9+1+1
    
    if n%2:
        return 0
    
    dp = [0]*(n+1)
    dp[2] = 3
    dp[4] = 11
    
    for i in range(6, n+1):
        dp[i] = dp[i-2]*4-dp[i-4]
    
    answer = dp[n]%1000000007
    
    return answer
