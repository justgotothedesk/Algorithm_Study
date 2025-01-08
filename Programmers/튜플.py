# 2019 카카오 개발자 겨울 인턴십

def solution(s):
    answer = []
    s = s[2:len(s)-2]
    tuples = s.split("},{")
    temp = []
    
    for tuple in tuples:
        tuple = tuple[0:len(tuple)]
        temp2 = []
        for i in tuple.split(','):
            temp2.append(int(i))
        
        temp.append(temp2)
    
    temp.sort(key=lambda x:len(x))
    
    for i in temp:
        for j in i:
            if j not in answer:
                answer.append(j)
    
    return answer
