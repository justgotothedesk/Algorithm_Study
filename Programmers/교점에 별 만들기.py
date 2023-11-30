# 우선 두 직선으로부터 겹치는 점들을 계산하는 함수 caculate를 만든다.
# 여러 직선들로부터 어느 것이 겹치는 지 알기 위해서 combinations 라이브러리를 사용하여 겹치는 모든 점을 구한다.
# 우선 '.'으로 answer 좌표를 모두 채우고 저장한 겹치는 점들을 바탕으로 '*'을 채워준다.

from itertools import combinations

def caculate(one, two):
    a1, b1, c1 = one
    a2, b2, c2 = two
    
    if a1*b2 == a2*b1:
        return
    x = (b1*c2-c1*b2)/(a1*b2-b1*a2)
    y = (c1*a2-a1*c2)/(a1*b2-b1*a2)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def solution(line):
    res = []
    row = []
    col = []
    #ax+by+c = 0
    for i in combinations(line, 2):
        one = i[0]
        two = i[1]
        dd = caculate(one, two)
        if dd and dd not in res:
            res.append(dd)
    
    for i in res:
        x, y = i
        col.append(x)
        row.append(y)
    
    maxr = max(row)
    minr = min(row)
    maxc = max(col)
    minc = min(col)
    
    answer = [["."]*(maxc-minc+1) for _ in range(maxr-minr+1)]
    
    for x, y in res:
        answer[y-minr][x-minc] = "*"
        
    answer.reverse()
    
    dd = []
    for i in range(len(answer)):
        temp = ""
        for j in range(len(answer[i])):
            temp += answer[i][j]
        dd.append(temp)
        
    return dd 
