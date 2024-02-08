def dfs(n, num, result):
    result = num[n%3]+result
    if n//3 == 0:
        return result
    
    return dfs(n//3-1, num, result)

def solution(n):
    answer = ''
    n -= 1
    num = ['1', '2', '4']
    answer = dfs(n,num, answer)
    
    return answer
