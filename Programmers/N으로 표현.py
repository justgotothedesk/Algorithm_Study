def caculate(one, two):
    result = set()
    for o in one:
        for t in two:
            result.add(o+t)
            result.add(o-t)
            result.add(t-o)
            result.add(o*t)
            if o:
                result.add(t//o)
            if t:
                result.add(o//t)
    return list(result)

def solution(N, number):
    answer = 0
    combi = {}
    
    for i in range(1, 9):
        combi[i] = [int(str(N)*i)]
    
    if N == number:
        return 1
    
    for i in range(2, 9):
        idx = 1
        temp_i = i-1
        
        while temp_i and idx:     
            combi[i].extend(caculate(combi[idx], combi[temp_i]))
            idx += 1
            temp_i -= 1
            
        if number in combi[i]:
            return i
    
    return -1
