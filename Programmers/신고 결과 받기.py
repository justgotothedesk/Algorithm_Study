# 2022 KAKAO RECRUITMENT
# 딕셔너리 자료구조를 이용하여 해당 유저가 이전에 어떤 신고를 받았는지 기록한다.
# 동일한 신고는 의미가 없으니 set 자료구조를 이용하여 중복을 제가한다.

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    count = {}
    who = {}
    res = {}
    r = list(set(report))
    
    for i in id_list:
        if i not in count:
            count[i] = 0
            res[i] = 0
        if i not in who:
            who[i] = ""
            
    for i in r:
        a, b = i.split(" ")
        count[b] += 1
        who[b] += a+" "
    
    for i in id_list:
        if count[i] >= k:
            member = who[i].split(" ")
            member = member[0:-1]
            for m in member:
                res[m] += 1
    
    index = 0
    
    for i in res:
        answer[index] = res[i]
        index += 1
    
    return answer
