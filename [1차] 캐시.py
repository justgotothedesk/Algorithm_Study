# 2018 KAKAO BLIND RECRUITMENT
# 캐시는 LRU(Least Recently Used) 알고리즘을 사용하기 때문에 가장 나중의 데이터는 제거하기 위해서 deque 자료구조를 사용한다.
# 캐시에 있는 정보라면 +1을 하고 그렇지 않다면 +5를 한다.
# 이때, 해당 도시 정보를 최신에 읽은 도시로 표시하기 위해서 캐시에 담아준다. 캐시에 이미 존재한다면 제거하고 담아주고 캐시 용량이 제한치보다 넘어선다면 가장 오래된 도시를 제거하고 담아준다.

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    buffer = deque()
    
    if(cacheSize == 0):
        return 5*len(cities)
    else:
        for i in cities:
            i = i.lower()
            if(i in buffer):
                answer += 1
            else:
                answer += 5
                
            if(i in buffer):
                buffer.remove(i)
            else:
                if(len(buffer) >= cacheSize):
                    buffer.popleft()
                    
            buffer.append(i)
          
    return answer
