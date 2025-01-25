# 2020 카카오 인턴십

def solution(gems):
    answer = []
    target = len(set(gems))
    count = {}
    minv = len(gems)
    start = 0
    
    for i in range(len(gems)):
        if gems[i] not in count:
            count[gems[i]] = 1
        else:
            count[gems[i]] += 1
        
        if len(count) == target:
            while start <= i:
                if count[gems[start]] > 1:
                    count[gems[start]] -= 1
                    start += 1
                elif minv > i-start:
                    minv = i-start
                    answer = [start+1, i+1]
                    break
                else:
                    break

    return answer
