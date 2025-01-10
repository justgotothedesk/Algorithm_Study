# 2022 KAKAO BLIND RECRUITMENT
# 차근차근 해결하면 그렇게 어렵지는 않은 문제
# 딕셔너리 두 개를 활용한다.
# 없는 차량이 입차를 한다면, parking 딕셔너리에 추가하고 출차를 했다면 parking에서 삭제하고 result에 추가한다.
# result를 딕셔너리에서 순차적으로 남아있는 시간을 기준으로 요금을 계산한다.

import math

def convert(time):
    hh,mm=time.split(":")
    
    return 60*int(hh)+int(mm)

def calculate(fees, total_time):
    dtime, dfee, ptime, pfee = fees[0], fees[1], fees[2], fees[3]
    
    if total_time <= dtime:
        return dfee
    return dfee+math.ceil((total_time-dtime)/ptime)*pfee

def solution(fees, records):
    answer = []
    temp = []
    parking = {}
    result = {}
    
    for record in records:
        time, number, do = record.split(" ")
        time = convert(time)
        
        if do == "IN":
            parking[number] = time
        elif do == "OUT":
            total_time = time-parking[number]
            del parking[number]
            
            if number not in result.keys():
                result[number] = total_time
            else:
                result[number] += total_time
            
    for number in parking.keys():
        if number not in result.keys():
            result[number] = convert("23:59")-parking[number]
        else:
            result[number] += convert("23:59")-parking[number]
            
    for number in result.keys():
        temp.append([number, calculate(fees, result[number])])
    
    temp.sort(key = lambda x:x[0])
    
    for _, value in temp:
        answer.append(value)
        
    return answer
