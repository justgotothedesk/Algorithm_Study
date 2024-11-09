def dfs(temp, data, result):
    if not temp:
        result.append(data)
        
        return
    
    for i in range(len(temp)):
        dfs(temp[:i]+temp[i+1:], data+[temp[i]], result)

def solution(n, k):
    answer = []
    temp = []
    result = []
    
    for i in range(1, n+1):
        temp.append(i)
    
    dfs(temp, [], result)
        
    answer = result[k-1]
    
    return answer
