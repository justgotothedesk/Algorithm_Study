from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    de = deque()
    de.append([0,0])
    ch[0][0] = 0
    dq = [deque() for i in range(26)] # 알파벳이 26개이므로, 26개의 큐를 만들어준다.
    r = 0 # 획득할 수 있는 $의 갯수

    while de:
        x,y = de.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h+2 and 0 <= ny < w+2: # 좌표의 범위에서 벗어나지 않는 경우만
                
                if a[nx][ny] == '*':
                    continue
            
                if ch[nx][ny] == -1:
                    ch[nx][ny] = 0

                    if a[nx][ny] == '$':
                        r += 1
                    elif 'A' <= a[nx][ny] <= 'Z': # 문인 경우
                        d = ord(a[nx][ny])-ord('A')
                        if alp[d] is False:
                            dq[d].append([nx,ny])
                            continue
                    elif 'a' <= a[nx][ny] <= 'z': # 열쇠인 경우
                        k = ord(a[nx][ny])-ord('a')
                        alp[k] = True
                        while dq[k]: # 해당 열쇠에 해당하는 좌표를 가져온다.
                            kx,ky=dq[k].popleft()
                            de.append([kx,ky])
                    
                    de.append([nx,ny])
    return r
                
            
for _ in range(int(input())):
    h, w = map(int,input().split()) 
    a = [list('.'*(w+2))]
    for i in range(h):
        a.append(list('.'+input()+'.'))
    a.append(list('.'*(w+2)))
    k = input()
    
    ch = [[-1]*(w+2) for i in range(h+2)]
    alp = [False]*26
    
    if k != '0':
        for i in k:
            alp[ord(i)-ord('a')] = True

    print(bfs())
