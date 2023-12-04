# 정확성과 효율성을 모두 보는 문제이므로 col마다 이중 for문을 통해 모든 경우를 탐색하면 시간 초과가 발생한다.
# 따라서 bfs 알고리즘을 사용하여 land에서 석유가 매장된 각각의 면적과 최소 col과 최대 col을 구한다.
# 최대로 석유를 얻을 수 있는 col만 구하면 되므로 각 면적의 최소 col과 최대 col을 이용하여 1 row짜리 dp 배열을 만들어 면적을 넣어준다.
# dp 배열의 최댓값을 정답으로 구해준다.

from collections import deque

def solution(land):
    answer = 0
    result = []
    visited = [[False]*len(land[0]) for _ in range(len(land))]
        
    def bfs(graph, x, y):
        dist = 1
        temp = []
        temp.append(y)
        q = deque()
        q.append([x, y])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        temp.append(ny)
                        dist += 1
                        q.append([nx, ny])
        
        temp.sort()
        
        return [temp[0], temp[-1], dist]
        
    for i in range(len(land)):
        for j in range(len(land[i])):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                result.append(bfs(land, i, j))
    
    dp = [0]+[0]*len(land[0])

    for x, y, d in result:
        dp[x] += d
        dp[y+1] -= d
    
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]
    
    answer = max(dp)
    
    return answer
