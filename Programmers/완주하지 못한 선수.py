def solution(participant, completion):
    answer = ''
    person = {}
    
    for i in participant:
        if i not in person.keys():
            person[i] = 1
        else:
            person[i] += 1
    
    for i in completion:
        person[i] -= 1
        
    for i in person.keys():
        if person[i]:
            return i
