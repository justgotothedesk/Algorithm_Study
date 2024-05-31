def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    box = []
    temp = []
    cnt = 0
  
    for i in score:
        temp.append(i)
        cnt += 1
        if cnt%m == 0:
            box.append(temp)
            cnt = 0
            temp = []
    for i in box:
        answer += min(i)*m
      
    return answer
