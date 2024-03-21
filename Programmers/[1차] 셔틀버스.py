# 2018 KAKAO BLIND RECRUITMENT
# 버스에 반드시 탑승해야하는 것이 목표이기 때문에 버스의 배차 시간에 맞추는 것이 중요함
# 먼저, 버스 운행 갯수(n)과 버스 배차 간격(t)를 통해서 몇 시에 버스가 오는 지 구해준다.
# 대기 인원을 오름차순 정렬하고 버스 시간에 맞다면 m명까지 끊어서 나눠준다.
# 가장 늦게 일어나야하므로, m명 씩 묶은 그룹에서 마지막 그룹의 인원 수를 체크한다.
# 마지막 그룹의 인원 수가 m보다 작으면 해당 버스 시간을 반환한다.
# 그렇지 않다면, 마지막 그룹의 마지막 인원의 시간보다 1분 빠른 시간을 반환한다.

def convert(time):
    hour, minute = time.split(":")
    
    return int(hour)*60+int(minute)

def reconvert(time):
    hour = str(time//60)
    minute = str(time%60)
    
    if len(hour) == 1:
        hour = '0'+hour
    if len(minute) == 1:
        minute = '0'+minute
    
    return hour+':'+minute

def solution(n, t, m, timetable):
    answer = ''
    buses = []
    crews = []
    start = convert("09:00")
    
    for i in range(n):
        buses.append(start)
        start += t
    
    busCrew = [[] for _ in range(len(buses))]
    
    for i in timetable:
        crews.append(convert(i))
    crews.sort(reverse = True)
    
    for idx, bus in enumerate(buses):
        limit = 0
        while crews:
            if limit == m:
                break
            crew = crews.pop()
            if crew <= bus:
                limit += 1
                busCrew[idx].append(crew)
            else:
                crews.append(crew)
                break
    
    if len(busCrew[-1]) == m:
        answer = reconvert(busCrew[-1][-1]-1)
    else:
        answer = reconvert(buses[-1])
        
    return answer
