# 2019 KAKAO BLIND RECRUITMENT
# 우선 해당 키들을 조합하여 만들 수 있는 모든 경우의 수를 구한다.
# 유일성을 판단하기 위해서 모든 경우의 수를 순회하며 만들 수 있는 결과를 구하고, set 자료구조를 사용하여 중복이 없다면 해당 경우는 유일성을 만족하는 것이다.
# 유일성을 만족하는 경우에 최소성을 판단하기 위해서 이 역시 set 자료구조를 활용하여 그 중에서도 issubset 메서드를 사용해서 포함되지 않으면 최소성을 만족하기에 답안으로 채택한다.

from itertools import combinations

def solution(relation):
    answer = []
    keys = [i for i in range(len(relation[0]))]
    combis = []
    
    for i in range(1, len(relation[0])+1):
        for j in combinations(keys, i):
            combis.append(j)
    
    for combi in combis:
        check = []
        for i in range(len(relation)):
            c = ""
            for j in combi:
                c += relation[i][j]
            check.append(c)
            
        if len(list(set(check))) == len(relation):
            flag = True
            for a in answer:
                if set(a).issubset(set(combi)):
                    flag = False
                    break
            
            if flag:
                answer.append(combi)
            
    return len(answer)
