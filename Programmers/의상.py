def solution(clothes):
    answer = 1
    kind = {}
    
    for name, category in clothes:
        if category not in kind.keys():
            kind[category] = name+","
        else:
            kind[category] += name+","
    
    for i in kind.keys():
        result = kind[i].split(",")
        answer *= len(result)
    
    return answer-1
