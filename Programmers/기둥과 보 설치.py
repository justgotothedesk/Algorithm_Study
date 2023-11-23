# 2020 KAKAO BLIND RECRUITMENT
# 해당 문제 풀이의 핵심은 임의의 좌표를 선정하여 대입하는 것이 아니라, 주어진 조건에 맞는 기록이 있다면 설치하거나 제거하는 방식을 사용한다.

# 보나 기둥을 삭제하거나 설치할 때, 조건에 맞는 기록이 있는지 확인하는 함수
def check(x, y, kind, res):
    # 해당 조건에 맞으면 삭제해도 문제가 없다는 것이다.
    if kind == 0:
        if y == 0 or [x, y-1, 0] in res or [x, y, 1] in res or [x-1, y, 1] in res:
            return True

    # 해당 조건에 맞으면 설치해도 문제가 없다는 것이다.
    else:
        if [x+1, y-1, 0] in res or [x, y-1, 0] in res or ([x-1, y, 1] in res and [x+1, y, 1] in res):
            return True
    
    return False

def solution(n, build_frame):
    res = []
    
    for x, y, kind, job in build_frame:
        if job == 1:
            if check(x, y, kind, res):
                res.append([x, y, kind])
        else:
            res.remove([x, y, kind])
            for nx, ny, nkind in res:
                if not check(nx, ny, nkind, res):
                    res.append([x, y, kind])
                    break
    
    answer = sorted(res)
    
    return answer
