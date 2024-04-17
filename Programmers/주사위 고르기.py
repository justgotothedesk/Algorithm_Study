# 2024 KAKAO WINTER INTERNSHIP
# 주사위를 분배할 수 있는 모든 경우로 나눈다.
# 해당 주사위에서 발생할 수 있는 모든 경우의 합을 구한다.
# A와 B를 모두 비교하며, 승리하는 경우의 수를 측정한다면 시간 초과가 발생한다.
# 따라서, B의 배열을 정렬하고 이진 탐색을 응용한 bisect_left 함수를 사용한다.
# bisect_left는 target으로부터 비교하려는 배열에서 바로 다음으로 큰 수를 반환하기 때문에 이는 해당 경우로 승리할 수 있는 횟수를 의미한다.
# 아래는 bisect_left 라이브러리를 사용한 것과 직접 구현한 두 가지 코드이다.

# 1. bisect_left 라이브러리 사용
from itertools import combinations, product
from bisect import bisect_left

def solution(dice):
    answer = []
    maxv = -1
    
    for A_dice in combinations(range(len(dice)), len(dice)//2):
        count = 0
        B_dice = []
        for i in range(len(dice)):
            if i not in A_dice:
                B_dice.append(i)

        A, B = [], []        
        for i in product(range(6), repeat=len(dice)//2):
            countA, countB = 0, 0
            for j in range(len(i)):
                countA += dice[A_dice[j]][i[j]]
                countB += dice[B_dice[j]][i[j]]
            A.append(countA)
            B.append(countB)
        
        B.sort()
        
        for a in A:
            count += bisect_left(B, a)
        
        if count > maxv:
            maxv = count
            answer = list(A_dice)

    for i in range(len(answer)):
        answer[i] += 1
            
    return answer

# 2. bisect_left 함수 직접 구현
from itertools import combinations, product

def bisect_left(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left

def solution(dice):
    answer = []
    maxv = -1
    
    for A_dice in combinations(range(len(dice)), len(dice)//2):
        count = 0
        B_dice = []
        for i in range(len(dice)):
            if i not in A_dice:
                B_dice.append(i)

        A, B = [], []        
        for i in product(range(6), repeat=len(dice)//2):
            countA, countB = 0, 0
            for j in range(len(i)):
                countA += dice[A_dice[j]][i[j]]
                countB += dice[B_dice[j]][i[j]]
            A.append(countA)
            B.append(countB)
        
        B.sort()
        
        for a in A:
            count += bisect_left(B, a)
        
        if count > maxv:
            maxv = count
            answer = list(A_dice)

    for i in range(len(answer)):
        answer[i] += 1
            
    return answer

