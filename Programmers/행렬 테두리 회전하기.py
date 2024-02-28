# 시계 방향으로 한 칸 회전할 때, 회전하는 방향을 기준으로 상하좌우 각각 4개의 배열로 나누어준다.
# 상하좌우 배열의 순서대로 한 칸씩 이동시키면 기존에 있던 값이 사라지게 되므로 각각의 값들도 따로 저장해준다.
# 헷갈리지 않게 순차적으로 계산한 뒤, 최소값을 구한다.

def solution(rows, columns, queries):
    answer = []
    graph = [[0]*columns for _ in range(rows)]
    start = 1
    
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = start
            start += 1

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        right, rightv = [], []
        down, downv = [], []
        left, leftv = [], []
        up, upv = [], []

        for y in range(y1, y2):
            right.append([x1, y])
            rightv.append(graph[x1][y])
        for x in range(x1, x2):
            down.append([x, y2])
            downv.append(graph[x][y2])
        for y in range(y2, y1, -1):
            left.append([x2, y])
            leftv.append(graph[x2][y])
        for x in range(x2, x1, -1):
            up.append([x, y1])
            upv.append(graph[x][y1])
        
        for i in range(len(right)):
            graph[right[i][0]][right[i][1]+1] = rightv[i]
        for i in range(len(down)):
            graph[down[i][0]+1][down[i][1]] = downv[i]
        for i in range(len(left)):
            graph[left[i][0]][left[i][1]-1] = leftv[i]
        for i in range(len(up)):
            graph[up[i][0]-1][up[i][1]] = upv[i]
        
        answer.append(min(min(rightv), min(downv), min(leftv), min(upv)))
        
    return answer
