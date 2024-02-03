# 시소의 좌석이 중심으로부터 2, 3, 4미터 간격에 있다.
# 따라서 몸무게가 동일하거나 2배 차이나거나, 3/2배 혹은 4/3배가 차이는 경우가 짝꿍이라고 할 수 있다.

from collections import Counter

def solution(weights):
    answer = 0
    temp = Counter(weights) # Counter를 사용하여 각 몸무게에 해당하는 인원의 수를 구한다.

    for i in range(100, 1001): # 몸무게가 100~1000이므로 해당 몸무게에 2배, 3/2배, 4/3배에 해당하는 인원을 구해준다.
        answer += temp[i]*(temp[i]-1)//2 # 몸무게가 동일한 경우, 짝지을 수 있는 경우의 수가 nC2로 구해준다.
        answer += temp[i]*temp[i*3/2]
        answer += temp[i]*temp[i*2]
        answer += temp[i]*temp[i*4/3]
    return answer
