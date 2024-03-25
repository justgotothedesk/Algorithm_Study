# 2019 KAKAO 개발자 겨울 인턴쉽
# stones의 배열 길이가 20만개 이하이므로, 이중 for문을 사용하여 탐색하면 시간 초과가 발생한다.
# 따라서, 이진 탐색을 사용해서 이를 해결한다.
# stones를 내림차순 정렬하여 가장 큰 값부터 비교하며, 건널 수 있는 지의 여부를 판단하여 값을 반환한다.
# 연속으로 넘을 수 없는 돌다리의 갯수가 k개 이상면, 건널 수 없기 때문에 다음 값으로 넘어간다.
# answer를 stones[right]가 아닌, stones를 내림차순 정렬한 temp[right]로 한 이유는 가장 큰 수에서부터 여부를 판단하기 때문이다.
# 그리고 left가 아닌 right를 정답으로 반환한 이유는 이분 탐색을 하면서, right가 배열의 최댓값으로 반환하게 하기 때문이다.

def solution(stones, k):
    temp = sorted(stones, reverse = True)
    left = 0
    right = len(temp)-1
    flag = 0
    
    if len(stones) == 1:
        return stones[0]
    
    while left <= right:
        mid = (left+right)//2
        for i in range(len(stones)):
            if stones[i]-temp[mid] <= 0:
                flag += 1
                if flag == k:
                    left = mid+1
                    break                    
            else:
                flag = 0
        
        if flag < k:
            right = mid-1
        flag = 0
            
    answer = temp[right]
    
    return answer
