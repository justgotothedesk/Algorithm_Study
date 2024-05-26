# 선행 스킬을 배워야 후행 스킬을 배울 수 있으므로, 조건이 있는 스킬만을 우선 골라준다.
# 해당 스킬이 첫 번째 스킬이면, 정상이므로 넘어가고 그렇지 않으면 잘못된 스킬이므로 그냥 넘어간다.

def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idx = 0
        flag = True
        for i in range(len(tree)):
            if tree[i] in skill:
                if skill[idx] == tree[i]:
                    idx += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1
    
    return answer
