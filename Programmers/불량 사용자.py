# 2019 카카오 개발자 겨울 인턴쉽
# 발생할 수 있는 모든 닉네임의 경우의 수를 구하기 위해서 permutations 라이브러리를 사용한다.

from itertools import permutations

# 해당 닉네임이 일치하는 지 확인하는 함수
def check(user, ban):
    if len(user) != len(ban):
        return False
    for i, j in zip(user, ban):
        if j == '*':
            continue
        if j != i:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    stack = []
    
    for i in permutations(user_id, len(banned_id)):
        cnt = 0
        for a, b in zip(i, banned_id):
            if check(a, b):
                cnt += 1
            # cnt와 banned_id의 길이가 일치하다면 해당 아이디는 제재 대상이다.
            if cnt == len(banned_id):
                if set(i) not in stack:
                    stack.append(set(i))
    answer = len(stack)
    return answer
