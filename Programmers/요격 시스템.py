# 시작점을 기준으로 오름차순 정렬을 하였을 때, 종료점의 대소 관계에 따라서 해당 범위가 겹치는지 알 수가 있다.
# 따라서 이를 판단하는 check 함수를 생성한다.

def check(temp, target):
    if temp[1] > target[0]:
        return [max(temp[0], target[0]), min(temp[1], target[1])]
    else:
        return []

def solution(targets):
    answer = 1
    temp = [-1, 100000001]
    
    targets.sort(key = lambda x:x[0])
    
    for target in targets:
        temp = check(temp, target)

        #temp가 없다면 겹치는 부분이 존재하지 않는 것이기 때문에 answer를 카운트하고 temp를 초기화해준다.
        if not temp:
            answer += 1
            temp = target
            
    return answer
