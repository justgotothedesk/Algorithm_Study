def solution(diffs, times, limit):
    answer = max(diffs)
    start = min(diffs)
    end = max(diffs)
    
    while start <= end:
        count = 0
        prev = 0
        flag = True
        mid = (start+end)//2
        
        for i in range(len(diffs)):
            if i == 0:
                count += times[i]
                prev = times[i]
            else:
                if mid >= diffs[i]:
                    count += times[i]
                else:
                    gap = diffs[i]-mid
                    count += times[i]+gap*(prev+times[i])
                prev = times[i]
                
            if count > limit:
                flag = False
                break
                 
        if flag:
            answer = mid
            end = mid-1
        else:
            start = mid+1
            
    return answer
