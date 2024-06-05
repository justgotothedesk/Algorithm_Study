def solution(n, m, section):
    answer = 0
    wall = [1 for _ in range(n)]
    rest = []
  
    for i in section:
        wall[i-1] = 0
      
    for i in range(len(wall)-m+1):
        if wall[i] == 0:
            for j in range(m):
                wall[i+j] = 1
            answer += 1
          
    for i in range(len(wall)-m+1, len(wall)):
        rest.append(wall[i])
      
    if 0 in rest:
        answer += 1
      
    return answer
