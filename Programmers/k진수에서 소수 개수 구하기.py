# 2022 KAKAO BLIND RECRUITMENT

import math

def convert(n, k):
    result = ""
    while n:
        result += str(n%k)
        n //= k
    result = result[::-1]
    
    return result

def isPrime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if not n%i:
            return False
    return True

def solution(n, k):
    answer = 0
    temp = convert(n, k)
    numbers = list(temp.split("0"))

    for number in numbers:
        if len(number) and isPrime(int(number)):
            answer += 1
    
    return answer
