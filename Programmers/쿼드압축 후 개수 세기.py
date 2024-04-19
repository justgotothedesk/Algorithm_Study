# 우선 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순으로 구역을 나눠서 재귀 호출을 한다.
# 해당 구역이 모두 같은 값이면 0이나 1의 값을 +해주고 그러지 않으면 계속 반으로 나누는 재귀 호출을 진행한다.

def check(arr):
    first = arr[0][0]
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != first:
                return False
    
    return True

def solution(arr):
    answer = []
    n = len(arr)
    
    if n == 1 or check(arr):
        if arr[0][0] == 0:
            return 1, 0
        else:
            return 0, 1
    
    z1, o1 = solution([i[:n//2] for i in arr[:n//2]])
    z2, o2 = solution([i[n//2:] for i in arr[:n//2]])
    z3, o3 = solution([i[:n//2] for i in arr[n//2:]])
    z4, o4 = solution([i[n//2:] for i in arr[n//2:]])
    
    answer.append(z1+z2+z3+z4)
    answer.append(o1+o2+o3+o4)
    
    return answer
