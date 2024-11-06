def solution(points, routes):
    answer = 0
    result = [[] for _ in range(len(routes))]
    
    for i in range(len(routes)):
        for j in range(len(routes[i])):
            if j == len(routes[i])-1:
                break
            
            nowx, nowy = points[routes[i][j]-1]
            targetx, targety = points[routes[i][j+1]-1]

            if nowx < targetx:
                while nowx < targetx:
                    result[i].append([nowx, nowy])
                    nowx += 1
            else:
                while nowx > targetx:
                    result[i].append([nowx, nowy])
                    nowx -= 1

            if nowy > targety:
                while nowy > targety:
                    result[i].append([nowx, nowy])
                    nowy -= 1
            else:
                while nowy < targety:
                    result[i].append([nowx, nowy])
                    nowy += 1
            
            if j == len(routes[i])-2:
                result[i].append([targetx, targety])

        # 아래의 코드를 실행할 경우, 시간 초과가 발생함
        # if not result[i]:
        #     result[i].append([nowx, nowy])
            
    maxlen = max(len(route) for route in result)
    
    for i in range(len(result)):
        diff = maxlen-len(result[i])
        if result[i]:
            for _ in range(diff):
                result[i].append([0, 0])
    
    for j in range(len(result[0])):
        graph = [[0]*101 for _ in range(101)]
        for i in range(len(result)):
            graph[result[i][j][0]][result[i][j][1]] += 1
        
        for r in range(len(graph)):
            for c in range(len(graph[r])):
                if r == 0 and c == 0:
                    continue
                if graph[r][c] >= 2:
                    answer += 1

    return answer
