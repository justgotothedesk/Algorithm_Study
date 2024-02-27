# 실패 코드. 숫자 1차이로 계속 실패함

def solution(enroll, referral, seller, amount):
    answer = []
    result = {}
    updown = {}
    
    for i in range(len(enroll)):
        updown[enroll[i]] = referral[i]
        result[enroll[i]] = 0

    for i in range(len(seller)):
        money = amount[i]*100
        now = seller[i]

        while updown[now] != '-' and money >= 10:
            result[now] += int(money*0.9)
            now = updown[now]
            money = int(money*0.1)

        if money < 10:
            result[now] += money
        elif updown[now] == '-' and money >= 10:
            result[now] += int(money*0.9)
    
    for i in result.keys():
        answer.append(result[i])
        
    return answer
