def solution(m, n, puddles):
    answer = 0
    maps = [[0]*m for _ in range(n)]
    for x, y in puddles:
        maps[y-1][x-1] = "X"
        
    for i in range(len(maps[0])):
        if maps[0][i] == "X":
            break
        maps[0][i] = 1
    
    for i in range(len(maps)):
        if maps[i][0] == "X":
            break
        maps[i][0] = 1
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if i == 0 or j == 0 or maps[i][j] == "X":
                continue
            if maps[i-1][j] != "X":
                one = maps[i-1][j]
            else:
                one = 0
            if maps[i][j-1] != "X":
                two = maps[i][j-1]
            else:
                two = 0
            maps[i][j] = (one+two)
                
    answer = maps[-1][-1]%1_000_000_007
  
    return answer
