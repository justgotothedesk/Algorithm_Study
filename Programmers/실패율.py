# 2019 KAKAO BLIND RECRUITMENT
# stages의 column 갯수가 200_000개 이하 이므로, 완전 탐색을 실시하면 시간 초과가 발생한다.
# 따라서, 0단계부터 N단계까지를 한 번씩만 순회한다.
# 각 단계마다 일치하는 인원의 수는 해당 단계를 실패한 인원과 동일하므로, 이를 배열로 저장하여 전체 인원에서 빼주면서 실패율을 구한다.

def solution(N, stages):
    answer = []
    rate = [0]*(N+1)
    fail = []
    
    for i in range(N):
        fail.append([0, i])
    
    for i in range(N+1):
        rate[i] = 0
    for i in stages:
        rate[i-1] += 1
    
    total = len(stages)
    for i in range(N):
        if total == 0:
            fail[i][0] = 0
        else:
            fail[i][0] = rate[i]/total
            total -= rate[i]
    
    fail.sort(key = lambda x:[-x[0], x[1]])
    
    for _, idx in fail:
        answer.append(idx+1)
    
    return answer
