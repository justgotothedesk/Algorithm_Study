# 루트 노드(center)까지 거슬러 올라가기 위해서 딕셔너리 자료구조를 사용한다.
# 우선 모든 이익을 판매자에게 더해주고 추천인이 있다면 해당 금액을 삭감하는 식으로 반복문을 진행한다.
# 마지막으로 추천인이 '-'라면 한 번 더 10%를 빼줘서 마무리를 해준다.

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
        result[now] += money

        while updown[now] != '-':
            if money == 0:
                break
            money = int(money*0.1)
            result[now] -= money
            now = updown[now]
            result[now] += money

        if updown[now] == '-':
            result[now] -= int(money*0.1)
    
    for i in result.keys():
        answer.append(result[i])
        
    return answer

# 실패 코드 : 단위가 1원보다 작을 때를 고려하지 않아서 실패함
# def solution(enroll, referral, seller, amount):
#     answer = []
#     result = {}
#     updown = {}
    
#     for i in range(len(enroll)):
#         updown[enroll[i]] = referral[i]
#         result[enroll[i]] = 0

#     for i in range(len(seller)):
#         money = amount[i]*100
#         now = seller[i]

#         while updown[now] != '-' and money >= 10:
#             result[now] += int(money*0.9)
#             now = updown[now]
#             money = int(money*0.1)

#         if money < 10:
#             result[now] += money
#         elif updown[now] == '-' and money >= 10:
#             result[now] += int(money*0.9)
    
#     for i in result.keys():
#         answer.append(result[i])
        
#     return answer
