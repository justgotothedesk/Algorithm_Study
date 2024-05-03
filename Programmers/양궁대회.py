# 2022 KAKAO BLIND RECRUITMENT
# 데이터의 종류가 많지 않으므로 활을 쏠 수 있는 모든 경우의 수를 함수로 구해준다.
# 모든 경우의 수를 하나씩 탐색하면서 차이값이 최대가 나면 해당 경우를 후보에 넣어준다.
# 이 때, 모든 탐색 이후에도 차이값이 0이라면 이는 라이언과 무지가 모든 점수에서 비긴 경우이므로 라이언이 이길 수 없으므로 -1을 예외적으로 반환한다.
# 후보가 여러 가지일 경우에 낮은 득점을 많이 한 것을 골라야 하므로 0점부터 맞춘 갯수가 0이 아닌 점수를 반환한다.
# 해당 점수를 기준으로 내림차순하여 가장 앞의 값을 정답으로 도출한다.

def distribute_gifts(total_gifts, num_people, gifts_per_person=None, idx=0):
    if gifts_per_person is None:
        gifts_per_person = [0] * num_people

    if total_gifts == 0:
        return [tuple(gifts_per_person)]

    distributions = []

    for i in range(idx, num_people):
        if total_gifts > 0:
            gifts_per_person[i] += 1
            next_distributions = distribute_gifts(total_gifts - 1, num_people, gifts_per_person, i)
            distributions.extend(next_distributions)
            gifts_per_person[i] -= 1

    return distributions    

def solution(n, info):
    answer = []
    maxv = 0
    real = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    all_distributions = distribute_gifts(n, 11)
    
    for temp in all_distributions:
        ryan = 0
        muzi = 0
        for i in range(len(temp)):
            if temp[i] or info[i]:
                if temp[i] > info[i]:
                    ryan += real[i]
                else:
                    muzi += real[i]
        
        gap = ryan - muzi
        
        if gap > maxv:
            answer = []
            answer.append(temp)
            maxv = gap
        elif gap < maxv:
            continue
        else:
            answer.append(temp)
    
    if not answer:
        return [-1]
    elif maxv == 0:
        return [-1]
    
    idx = -1
    for i in range(len(answer[0])-1, -1, -1):
        maxv = -float('inf')
        for a in answer:
            if a[i] == 0:
                continue
            if maxv < a[i]:
                maxv = a[i]
        if maxv > 0:
            idx = i
            break
    
    answer.sort(key = lambda x:-x[idx]) 

    return answer[0]
