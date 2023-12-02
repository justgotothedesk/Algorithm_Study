# 2019 KAKAO BLIND RECRUITMENT
# 사용자가 이름을 변경할 수 있으므로 딕셔너리 자료구조를 활용하여 해당 사용자의 상태를 저장한다.

def solution(record):
    answer = []
    info = {}
    for i in record:
        i = i.split()
        # 사용자가 들어온 경우
        if i[0] == "Enter":
            info[i[1]] = i[2]
            answer.append([i[1], "님이 들어왔습니다."])
          
        # 사용자가 나간 경우
        elif i[0] == "Leave":
            answer.append([i[1], "님이 나갔습니다."])
        
        # 사용자의 닉네임을 변경한 경우
        else:
            info[i[1]] = i[2]
    answer = list(map(lambda x : info[x[0]]+x[1], answer))
    return answer
