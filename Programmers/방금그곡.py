# 2018 KAKAO BLIND RECRUITMENT
# '#'음계를 따로 변환해주는 sharp 함수와 음악의 시작과 끝의 길이가 얼마인지를 나타내는 transfer 함수를 만들어준다.
# 조건에 맞다면 res 리스트에 담아 정렬해주고 그렇지 않다면 '(None)'을 반환한다.

def sharp(string):
    string = string.replace('C#', 'c')
    string = string.replace('D#', 'd')
    string = string.replace('F#', 'f')
    string = string.replace('G#', 'g')
    string = string.replace('A#', 'a')
    
    return string

def transfer(first, second):
    firsth = int(first.split(':')[0])
    firstm = int(first.split(':')[1])
    secondh = int(second.split(':')[0])
    secondm = int(second.split(':')[1])
    
    return (secondh*60+secondm)-(firsth*60+firstm)
    
def solution(m, musicinfos):
    answer = ''
    res = []
    m = sharp(m)
    for i in range(len(musicinfos)):
        first, second, title, code = musicinfos[i].split(',')
        time = transfer(first, second)
        code = sharp(code)
        
        if len(code) < time:
            code *= time//len(code)
            code += code[0:time-len(code)]
        else:
            code = code[0:time]
          
        if m in code:
            temp = []
            temp.append(time)
            temp.append(title)
            res.append(temp)
          
    if not res:
        return "(None)"
    
    res.sort(key = lambda x:-x[0])
    answer += res[0][1]
    
    return answer
