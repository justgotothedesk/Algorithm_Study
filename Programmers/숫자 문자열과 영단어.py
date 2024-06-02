# 2021 카카오 채용연계형 인턴십

def solution(s):
    answer = ""
    temp = ""
    convert = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
              "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    for i in s:
        if temp in convert.keys():
            answer += convert[temp]
            temp = ""
        if i.isalpha():
            temp += i
        else:
            answer += i
    
    if temp:
        answer += convert[temp]
    
    answer = int(answer)
    
    return answer
