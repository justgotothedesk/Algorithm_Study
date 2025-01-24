# 2021 KAKAO BLIND RECRUITMENT

def solution(new_id):
    answer = ''
    answer = new_id.lower()
    
    delete = '~!@#$%^&*()=+[{]}:?,<>\'/'
    answer2 = ''
    for a in answer:
        if a not in delete:
            answer2 += a
    
    answer3 = ''
    for a in answer2:
        if len(answer3):
            if a == '.' and answer3[-1] == '.':
                continue
        answer3 += a
    
    answer4 = ''
    for i in range(len(answer3)):
        if i == 0 or i == len(answer3)-1:
            if answer3[i] == '.':
                continue
        answer4 += answer3[i]
        
    if answer4 == '':
        answer4 += 'a'
    
    if len(answer4) >= 16:
        answer4 = answer4[:15]
        if answer4[-1] == '.':
            answer4 = answer4[:14]
    
    target_len = 3-len(answer4)
    if target_len:
        for i in range(target_len):
            answer4 += answer4[-1]
    
    return answer4
