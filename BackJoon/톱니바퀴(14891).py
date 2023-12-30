# deque의 rotate 함수를 써도 되지만 톱니바퀴의 숫자가 네 개이기 때문에 많지 않아서 하드 코딩하였다.
# 좌우 톱니바퀴의 회전 여부 역시, 갯수가 많지 않아서 하드 코딩하였다.

import sys
input = sys.stdin.readline

cycle = list(input().strip() for _ in range(4))
n = int(input())
orders = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def spin(temp, dir):
    if dir == 1:
        return temp[-1]+temp[:-1]
    elif dir == 0:
        return temp
    else:
        return temp[1:]+temp[0]

for i, dir in orders:
    i -= 1
    one = 0
    two = 0
    thr = 0
    four = 0
  
    # 첫 번째 톱니바퀴가 회전할 때
    if i == 0:
        one = dir
        if cycle[0][2] != cycle[1][6]:
            two = -one
        if two != 0 and cycle[1][2] != cycle[2][6]:
            thr = -two
        if thr != 0 and cycle[2][2] != cycle[3][6]:
            four = -thr
          
    # 두 번째 톱니바퀴가 회전할 때
    elif i == 1:
        two = dir
        if cycle[1][2] != cycle[2][6]:
            thr = -two
        if cycle[0][2] != cycle[1][6]:
            one = -two
        if thr != 0 and cycle[2][2] != cycle[3][6]:
            four = -thr
    # 세 번째 톱니바퀴가 회전할 때
    elif i == 2:
        thr = dir
        if cycle[2][2] != cycle[3][6]:
            four = -thr
        if cycle[2][6] != cycle[1][2]:
            two = -thr
        if two != 0 and cycle[1][6] != cycle[0][2]:
            one = -two
          
    # 네 번째 톱니바퀴가 회전할 때
    else:
        four = dir
        if cycle[3][6] != cycle[2][2]:
            thr = -four
        if thr != 0 and cycle[2][6] != cycle[1][2]:
            two = -thr
        if two != 0 and cycle[1][6] != cycle[0][2]:
            one = -two
    
    cycle[0] = spin(cycle[0], one)
    cycle[1] = spin(cycle[1], two)
    cycle[2] = spin(cycle[2], thr)
    cycle[3] = spin(cycle[3], four)

for i in range(4):
    if cycle[i][0] == '1':
        answer += 2**i

print(answer)
