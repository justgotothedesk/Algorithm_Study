# 2021 카카오 채용연계형 인턴십
# 해당 좌표가 'P'일 때만 거리두기가 올바른지 확인하면 된다.
# 우선 좌표의 거리를 벗어나는 지를 확인하는 limit함수를 만든다.
# 점 'P'로부터 상하좌우를 살펴보면서 'P'가 있는 경우 바로 False를 반환한다.

def limit(x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return False
    return True

def check(x, y, k):
    yes = []
    if limit(x+1,y):
        if k[x+1][y] == 'X':
            yes.append('X')
        elif k[x+1][y] == 'P':
            return False
        else:
            if (x+2 <= 4 and k[x+2][y] == 'P') or (y-1 >= 0 and k[x+1][y-1] == 'P') or (y+1 <= 4 and k[x+1][y+1] == 'P'):
                return False
                
    if limit(x-1,y):
        if k[x-1][y] == 'X':
            yes.append('X')
        elif k[x-1][y] == 'P':
            return False
        else:
            if (x-2 >= 0 and k[x-2][y] == 'P') or (y-1 >= 0 and k[x-1][y-1] == 'P') or (y+1 <= 4 and k[x-1][y+1] == 'P'):
                return False
                
    if limit(x, y+1):
        if k[x][y+1] == 'X':
            yes.append('X')
        elif k[x][y+1] == 'P':
            return False
        else:
            if (y+2 <= 4 and k[x][y+2] == 'P') or (x-1 >= 0 and k[x-1][y+1] == 'P') or (x+1 <= 4 and k[x+1][y+1] == 'P'):
                return False
                
    if limit(x, y-1):
        if k[x][y-1] == 'X':
            yes.append('X')
        elif k[x][y-1] == 'P':
            return False
        else:
            if (y-2 >= 0 and k[x][y-2] == 'P') or (x-1 >= 0 and k[x-1][y-1] == 'P') or (x+1 <= 4 and k[x+1][y-1] == 'P'):
                return False
            
    return True
    
def solution(places):
    answer = []
    for k in places:
        fast = True
        for i in range(len(k)):
            for j in range(len(k[i])):
                if k[i][j] == 'P':
                    if check(i, j, k) == False:
                        fast = False
                        break
            if fast == False:
                answer.append(0)
                break
        if fast:
            answer.append(1)
                    
    return answer
