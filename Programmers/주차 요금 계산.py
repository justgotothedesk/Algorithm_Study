# 2022 KAKAO BLIND RECRUITMENT
# 차근차근 해결하면 그렇게 어렵지는 않은 문제
# 딕셔너리 두 개를 활용한다.
# 없는 차량이 입차를 한다면, init 딕셔너리에 추가하고 출차를 했다면 init에서 삭제하고 result에 추가한다.
# result를 딕셔너리에서 순차적으로 남아있는 시간을 기준으로 요금을 계산한다.

import math

def convert(time):
    hh,mm=time.split(":")
    return 60*int(hh)+int(mm)

def solution(fees, records):
    init = {}
    result = {}
    for i in records:
        time, num, inout = i.split()
        if num not in result:
            result[num] = 0
        if inout == 'IN':
            init[num] = convert(time)
        else:
            result[num] += convert(time)-init[num]
            del init[num]
    for key,val in init.items():
        result[key] += 23*60+59-val
    
    answer = []
    for key,val in sorted(result.items()):
        if val <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil((val-fees[0])/fees[2])*fees[3])
        
    return answer
