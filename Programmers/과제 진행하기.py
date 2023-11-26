# 시작 시간에 따라서 정렬된 것이 아니기 때문에 우선, 시작 시간을 기준으로 오름차순 정렬을 해준다.
# 현재 진행중인 과제를 담는 배열인 temp를 사용해서 시간이 지났을 때, temp 배열이 있다면 다른 일을 먼저 진행해준다.

def convert(time):
    hh, mm = time.split(":")
    return int(hh)*60+int(mm)

def solution(plans):
    answer = []
    temp = []
  
    for i in plans:
        i[1] = convert(i[1])
        i[2] = int(i[2])
    
    plans.sort(key = lambda x:x[1])
    
    for i in plans:
        sub, start, time = i
        
        if not temp:
            temp.append([sub, start, time])
            continue
        
        lsub, lstart, ltime = temp[-1]
        gap = start-lstart
        
        while gap > 0 and temp:
            a, b, c = temp.pop()
            if c <= gap:
                answer.append(a)
                gap -= c
            else:
                temp.append([a, b, c-gap])
                gap = 0
                
        temp.append([sub, start, time])
        
    while temp:
        a, b, c = temp.pop()
        answer.append(a)
        
    return answer
