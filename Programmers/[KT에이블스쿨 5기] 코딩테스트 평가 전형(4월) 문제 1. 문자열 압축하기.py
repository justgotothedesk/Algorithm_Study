# 문제 내용 : "0"과 "1"로만 구성된 숫자를 통해 똑같은 숫자가 반복되는 갯수만큼 해당 숫자를 특정 알파벳으로 변경한다.
# ex) 111100100011 -> 1DBACB
# ex) 00011011100000 -> 0CBACE

def solution(src):
    answer = ''
    count = 0
    start = -1

    for i in range(len(src)):
        if start == -1:
            count += 1
            answer += src[i]
            start = src[i]
        elif src[i] == start:
            count += 1
        else:
            start = src[i]
            answer += chr(64+count)
            count = 1

    answer += chr(64+count)
    
    return answer
