# 2019 카카오 개발자 겨울 인턴쉽

from itertools import permutations

def check(combi, banned_id):
    for i in range(len(combi)):
        if len(combi[i]) != len(banned_id[i]):
            return False
    
    for i in range(len(combi)):
        for j in range(len(combi[i])):
            if banned_id[i][j] == '*':
                continue
            if combi[i][j] != banned_id[i][j]:
                return False
    
    return combi

def solution(user_id, banned_id):
    answer = []
    
    for combi in permutations(user_id, len(banned_id)):
        temp = check(combi, banned_id)
        
        if temp:
            temp2 = list(temp)
            temp2.sort()
            if temp2 not in answer:
                answer.append(temp2)
    
    return len(answer)
