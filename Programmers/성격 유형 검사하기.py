# 2022 KAKAO TECH INTERNSHIP

def solution(survey, choices):
    answer = ''
    mbti = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = {}
    temp = [3, 2, 1, 0, 1, 2, 3]
    
    for m in mbti:
        score[m] = 0
    
    for i in range(len(survey)):
        c = choices[i]
        front = survey[i][0]
        rear = survey[i][1]
        
        if c < 4:
            score[front] += temp[c-1]
        elif c > 4:
            score[rear] += temp[c-1]
    
    keys = list(score.keys())
    for i in range(0, len(keys), 2):
        if score[keys[i]] >= score[keys[i+1]]:
            answer += keys[i]
        else:
            answer += keys[i+1]

    return answer
