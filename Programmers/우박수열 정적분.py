def solution(k, ranges):
    answer = []
    su = [k]
    area = []
    newrange = []
    
    while(k>1):
        if k%2 == 0:
            k/=2
        else:
            k = k*3+1
        su.append(k)
        
    for i in range(len(su)-1):
        area.append((su[i]+su[i+1])/2)
        
    for i in ranges:
        newrange.append([i[0], len(su)-1+i[1]])
        
    for i in newrange:
        if i[0] == i[1]:
            answer.append(0.0)
        elif i[0] > i[1]:
            answer.append(-1.0)
        else:
            sum = 0
            for j in range(i[0], i[1]):
                sum += area[j]
            answer.append(sum)
            
    return answer
