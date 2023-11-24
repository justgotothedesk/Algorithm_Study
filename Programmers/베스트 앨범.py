# 딕셔너리를 이용하여 해당 장르의 재생 횟수를 저장한다.
# 재생 횟수를 기준으로 내림차순 정렬을 하여 가장 많이 재생된 장르를 찾는다.
# 이중 for문을 통해, 이미 추가한 장르가 있으면 반복문을 탈출한다.

def solution(genres, plays):
    answer = []
    total = {}
    for i in range(len(genres)):
        if genres[i] not in total:
            total[genres[i]] = plays[i]
        else:
            total[genres[i]] += plays[i]
          
    total = sorted(total.items(), key = lambda x:-x[1])
    
    new_genres = list(enumerate(list(zip(genres,plays))))
    new_genres.sort(key = lambda x:-x[1])
    
    for i in total:
        cnt = 0
        for j in new_genres:
            if j[1][0] == i[0]:
                answer.append(j[0])
                cnt += 1
                if cnt == 2:
                    break
    
    return answer
