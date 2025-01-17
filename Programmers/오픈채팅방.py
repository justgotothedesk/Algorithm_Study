# 2019 KAKAO BLIND RECRUITMENT
# 사용자가 이름을 변경할 수 있으므로 딕셔너리 자료구조를 활용하여 해당 사용자의 상태를 저장한다.

def solution(record):
    answer = []
    temp = []
    history = {}
    
    for r in record:
        r = r.split(" ")
        
        if len(r) == 3:
            do, uid, name = r[0], r[1], r[2]
            if uid not in history.keys() or do == "Change":
                history[uid] = name
            elif do == "Enter" and uid in history.keys():
                history[uid] = name
            temp.append([do, uid, name])
        elif len(r) == 2:
            do, uid = r[0], r[1]
            temp.append([do, uid])
    
    for t in temp:
        if len(t) == 2:
            answer.append(history[t[1]]+"님이 나갔습니다.")
        else:
            if t[0] == "Enter":
                answer.append(history[t[1]]+"님이 들어왔습니다.")
    
    return answer
