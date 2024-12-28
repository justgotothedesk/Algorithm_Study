def solution(diffs, times, limit):
    answer = max(diffs)
    
    while True:
        count = 0
        prev = 0
        
        for i in range(len(diffs)):
            if i == 0:
                count += times[i]
                prev = times[i]
            else:
                if answer >= diffs[i]:
                    count += times[i]
                else:
                    gap = diffs[i]-answer
                    count += times[i]+gap*(prev+times[i])
                prev = times[i]
                
            if count > limit:
                return answer+1
            
        answer -= 1
            
    return answer
