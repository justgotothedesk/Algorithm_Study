def solution(s):
    answer = ''
    stack = s.split(' ')
    soo = []
  
    for i in stack:
        soo.append(int(i))
      
    maxv = max(soo)
    minv = min(soo)
    answer += str(minv)
    answer += ' '
    answer += str(maxv)
  
    return answer
