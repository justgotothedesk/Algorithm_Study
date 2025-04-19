def solution(m, n, puddles):
    answer = 0
    graph = [[0]*m for _ in range(n)]
    
    for puddle in puddles:
        c, r = puddle
        graph[r-1][c-1] = "X"
        
    for i in range(len(graph)):
        if graph[i][0] != "X":
            graph[i][0] = 1
        else:
            break
    
    for i in range(len(graph[0])):
        if graph[0][i] != "X":
            graph[0][i] = 1
        else:
            break
    
    for i in range(1, len(graph)):
        for j in range(1, len(graph[i])):
            if graph[i][j] == "X":
                continue
            one = graph[i-1][j]
            two = graph[i][j-1]
            if one == "X":
                one = 0
            if two == "X":
                two = 0
            graph[i][j] = one+two
    
    return graph[-1][-1]%1000000007
