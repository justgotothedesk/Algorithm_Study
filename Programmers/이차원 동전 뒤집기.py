def solution(beginning, target):
    answer = 10000000000000000000
    graph = [[0]*len(target[0]) for _ in range(len(target))]
    graph2 = [[0]*len(target[0]) for _ in range(len(target))]
    
    for i in range(len(target)):
        for j in range(len(target[0])):
            if target[i][j] == beginning[i][j]:
                graph[i][j] = 1
                graph2[i][j] = 1
            else:
                graph[i][j] = 0
                graph2[i][j] = 0
                
    temp1 = 0
    temp2 = 0
    
    for j in range(len(graph[0])):
        for i in range(len(graph)):
            if not graph[i][j]:
                for col in range(len(graph)):
                    if graph[col][j]:
                        graph[col][j] = 0
                    else:
                        graph[col][j] = 1
                    temp1 += 1
                break
                
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if not graph[i][j]:
                for row in range(len(graph[0])):
                    if graph[i][row]:
                        graph[i][row] = 0
                    else:
                        graph[i][row] = 1
                    temp1 += 1
                break
    
    one = True
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if not graph[i][j]:
                one = False
                break
        if not one:
            break
    
    if one:
        answer = min(answer, temp1)
    
    for i in range(len(graph2)):
        for j in range(len(graph2[i])):
            if not graph2[i][j]:
                for row in range(len(graph2[0])):
                    if graph2[i][row]:
                        graph2[i][row] = 0
                    else:
                        graph2[i][row] = 1
                    temp2 += 1
                break
                
    for j in range(len(graph2[0])):
        for i in range(len(graph2)):
            if not graph2[i][j]:
                for col in range(len(graph2)):
                    if graph2[col][j]:
                        graph2[col][j] = 0
                    else:
                        graph2[col][j] = 1
                    temp2 += 1
                break
                
    two = True
    for i in range(len(graph2)):
        for j in range(len(graph2[0])):
            if not graph2[i][j]:
                two = False
                break
        if not two:
            break
    
    if two:
        answer = min(answer, temp2)
    
    if not one and not two:
        return -1

    return answer
