def solution(n):
    answer = []
    
    def hanoi(src, mid, des, n):
        if n == 1:
            answer.append([src, des])
        else:
            hanoi(src, des, mid, n-1)
            hanoi(src, mid, des, 1)
            hanoi(mid, src, des, n-1)
    
    hanoi(1, 2, 3, n)
    
    return answer
