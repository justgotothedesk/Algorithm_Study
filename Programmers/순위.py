# 1이 3을 이기고 3이 4를 이겼다면, 1은 4를 이긴다.
# 그래프에서 경유할 수 있는 지점을 구하듯이 이는 floyd 알고리즘을 사용하여 누가 누구를 경유해서 이길 수 있는지 구할 수 있다.
# 선수마다 매칭할 수 있는 경우의 수로 2차원 배열을 만들고 이길 수 있다면 1, 진다면 -1, 모른다면 -2로 채운다.
# 해당 행에 -2가 없다면 해당 선수가 누구와 붙었을 때, 이기는 지 지는 지를 알기 때문에 순위를 구할 수 있다.
# 따라서 각 행에 -2가 없는 선수의 수가 답이 된다.

def solution(n, results):
    answer = 0
    graph = [[-2]*n for _ in range(n)]
    
    for i in range(n):
        graph[i][i] = 0
    
    for win, lose in results:
        graph[win-1][lose-1] = 1
        graph[lose-1][win-1] = -1
    
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if graph[start][mid] == 1 and graph[mid][end] == 1:
                    graph[start][end] = 1
                    graph[end][start] = -1
                    
    for i in range(len(graph)):
        flag = True
        for j in range(len(graph[i])):
            if graph[i][j] == -2:
                flag = False
                break
        if flag:
            answer += 1
          
    return answer
