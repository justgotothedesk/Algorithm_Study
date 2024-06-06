def solution(word):
    global answer
    answer = -1
    big = ["A", "E", "I", "O", "U"]
    
    def dfs(string):
        global answer
        answer += 1
        if string == word:
            return True
        if len(string) == 5:
            return False
        
        for b in big:
            if dfs(string+b) == True:
                return True
    
    dfs("")
    
    return answer
