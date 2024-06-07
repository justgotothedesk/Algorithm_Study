def solution(s):
    answer = True
    count = 0
    
    for char in s:
        if char == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    
    if count != 0:
        answer = False
    
    return answer
