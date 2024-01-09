def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(index, total, target, numbers):
        global answer
        if total == target and index == len(numbers):
            answer += 1
            return
        if index == len(numbers):
            return
        dfs(index+1, total+numbers[index], target, numbers)
        dfs(index+1, total-numbers[index], target, numbers)
        
    dfs(0, 0, target, numbers)
    
    return answer
