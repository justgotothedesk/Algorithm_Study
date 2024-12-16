# 2021 KAKAO BLIND RECRUITMENT

def reconvert(time):
    hh = time//3600
    time = time-hh*3600
    mm = time//60
    ss = time-mm*60
    hh, mm, ss = str(hh), str(mm), str(ss)
    
    if len(hh) == 1:
        hh = "0"+hh
    if len(mm) == 1:
        mm = "0"+mm
    if len(ss) == 1:
        ss = "0"+ss
    
    return hh+":"+mm+":"+ss

def convert(time):
    hh, mm, ss = time.split(":")
    
    return int(ss)+int(mm)*60+int(hh)*3600

def solution(play_time, adv_time, logs):
    answer = ''
    idx = 0
    maxv = 0
    time = [0]*(convert(play_time)+2)
    
    for log in logs:
        start, end = log.split("-")
        start = convert(start)
        end = convert(end)
        
        time[start] += 1
        time[end] -= 1
    
    for i in range(1, len(time)):
        time[i] += time[i-1]
    
    for i in range(1, len(time)):
        time[i] += time[i-1]
    
    for i in range(convert(adv_time), len(time)):
        if i == convert(adv_time):
            if time[i] > maxv:
                idx = i-convert(adv_time)
                maxv = time[i]
        else:
            if time[i]-time[i-convert(adv_time)] > maxv:
                idx = i-convert(adv_time)+1
                maxv = time[i]-time[i-convert(adv_time)]
    
    answer = reconvert(idx)

    return answer
