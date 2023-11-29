# 귤을 크기 순서대로 오름차순 정렬을 한다.
# 연속적으로 크기가 같지 않은 경우에 new 배열에 담아준다.
# 반면 연속적으로 크기가 같으면 cnt를 카운트해주고 배열에 담지 않는다.
# cnt를 기준으로 내림차순 정렬을 하여 가장 많이 연속적으로 같은 크기의 귤을 선정한다.

def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    new = []
    cnt = 1
    
    for i in range(len(tangerine)):
        if i == len(tangerine)-1:
            new.append([tangerine[i],cnt])
        elif tangerine[i] == tangerine[i+1]:
            cnt += 1
        else:
            new.append([tangerine[i],cnt])
            cnt = 1
    new.sort(key=lambda x:-x[1])
    
    total = 0
    for i in new:
        total += i[1]
        answer += 1
        
        if total >= k:
            return answer
        
    return answer
