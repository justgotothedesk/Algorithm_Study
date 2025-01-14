# 2018 KAKAO BLIND RECRUITMENT

def convert(file):
    idx = 0
    for i in range(len(file)):
        if file[i].isdecimal():
            idx = i
            break
    
    head = file[:idx]
    
    idx2 = len(file)
    for i in range(idx, len(file)):
        if not file[i].isdecimal():
            idx2 = i
            break
    
    number = file[idx:idx2]
    tail = file[idx2:]
    
    return head, int(number), tail

def solution(files):
    answer = []
    temp = []
    idx = 0
    
    for file in files:
        head, number, tail = convert(file)
        temp.append([head.lower(), number, tail, idx])
        idx += 1
    
    temp.sort(key = lambda x:[x[0], x[1]])
    
    for _, _, _, i in temp:
        answer.append(files[i])
    
    return answer
