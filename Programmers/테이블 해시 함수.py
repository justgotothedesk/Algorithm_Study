def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x:(x[col-1], -x[0]))
    
    s1 = 0
    for j in range(row_begin-1, row_end):
        for i in range(len(data[0])):
            s1 += data[j][i]%(j+1)
        answer ^= s1
        s1 = 0
        
    return answer
