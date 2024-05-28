# 2018 KAKAO BLIND RECRUITMENT

import string

tmp = string.digits+string.ascii_uppercase
def convert(num, base):
    q, R = divmod(num, base)
    if q == 0:
        return tmp[R] 
    else:
        return convert(q, base) + tmp[R]

def solution(n, t, m, p):
    answer = ''
    num = ''
    for i in range(t*m):
        i = convert(i,n)
        num += i
        
    for i in range(t*m):
        while len(answer) < t:
            answer += num[p-1]
            p += m
    
    return answer
