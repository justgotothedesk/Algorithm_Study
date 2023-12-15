# 2018 KAKAO BLIND RECRUITMENT
# 우선 단어를 정렬해서 가장 짧은 단어부터 빠르게 처리할 수 있도록 해준다.
# 바로 뒤의 단어와 비교하여 겹치는 부분이 얼마나 되는지 구한다.
# 겹치는 수를 기반으로 만들 수 있는 최소한의 차별성이 얼마인지 구한다.

def solution(words):
    answer = 0
    words.sort()
    res = [0]*len(words)
    
    for i in range(len(words)-1):
        pre = words[i]
        now = words[i+1]
        
        for j in range(min(len(pre), len(now))):
            if pre[j] != now[j]:
                j -= 1
                break
        
        res[i] = max(res[i], min(len(pre), j+2))
        res[i+1] = max(res[i+1], min(len(now), j+2))
        
    answer = sum(res)
    
    return answer
