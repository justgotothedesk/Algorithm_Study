from itertools import permutations
import math

def check(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i == 0:
                return False

        return True
    return False

def solution(numbers):
    answer = 0
    visited = set()
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            temp = "".join(j)
            if int(temp) not in visited and check(int(temp)):
                visited.add(int(temp))
                answer += 1
    
    return answer
