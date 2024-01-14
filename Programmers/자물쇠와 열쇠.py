# 2020 KAKAO BLIND RECRUITMENT
# 좌물쇠를 열쇠 부분에 맞추기 위해서는 동서남북 4번 돌려야하기 때문에 spin 함수를 만들어준다.
# 그리고 열쇠와 자물쇠가 빈 부분과 겹치는 부분이 없는지 판단하는 correct 함수를 만들어준다.

def spin(new, key, num, i, j):
    n = len(key)
    for r in range(n):
        for c in range(n):
            if num == 0:
                new[r+i][c+j] += key[r][c]
            elif num == 1:
                new[r+i][c+j] += key[n-1-c][r]
            elif num == 2:
                new[r+i][c+j] += key[n-1-r][n-1-c]
            else:
                new[r+i][c+j] += key[c][n-1-r]

def correct(new, init, n):
    for i in range(n):
        for j in range(n):
            if new[init+i][init+j] != 1:
                return False
    return True
                
def solution(key, lock):
    init = len(key)-1
    for i in range(init+len(lock)):
        for j in range(init+len(lock)):
            for num in range(4):
                new = [[0 for _ in range(60)] for _ in range(60)]
                for r in range(len(lock)):
                    for c in range(len(lock)):
                        new[init+r][init+c] = lock[r][c]
                spin(new, key, num, i, j)
                if correct(new, init, len(lock)):
                    return True
    return False
