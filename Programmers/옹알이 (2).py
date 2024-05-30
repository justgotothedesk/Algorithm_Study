def solution(babbling):
    answer = 0
  
    for i in babbling:
        i = i.replace("aya", "1")
        i = i.replace("ye", "2")
        i = i.replace("woo", "3")
        i = i.replace("ma", "4")
        if i.isdigit() and not "11" in i and not "22" in i and not "33" in i and not "44" in i:
            answer += 1
          
    return answer
