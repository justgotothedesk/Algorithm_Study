# 2018 KAKAO BLIND RECRUITMENT
# 해당 글자가 추가된 글자라면 길수록 압축이 잘된 것이기 때문에 긴 단어를 우선적으로 탐색한다.
# 포함된 글자라면 그 글자로부터 한 글자 더 추가된 글자를 다시 추가해준다.

def solution(msg):
    answer = []
    alpha = []
    
    for i in range(65, 91):
        alpha.append(chr(i))
        
    start = 0
    end = len(msg)
    
    while start < end:
        if msg[start:end] in alpha:
            answer.append(alpha.index(msg[start:end])+1)
            alpha.append(msg[start:end+1])
            start = end
            end = len(msg)
        else:
            end -= 1
        
    return answer
