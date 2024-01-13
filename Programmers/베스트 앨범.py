# 딕셔너리를 이용하여 해당 장르의 재생 횟수를 저장한다.
# 재생 횟수를 기준으로 내림차순 정렬을 하여 가장 많이 재생된 장르를 찾는다.
# 이중 for문을 통해, 이미 추가한 장르가 있으면 반복문을 탈출한다.

def solution(genres, plays):
    answer = []
    genre = {}
    
    for i in range(len(plays)):
        if genres[i] not in genre:
            genre[genres[i]] = plays[i]
        else:
            genre[genres[i]] += plays[i]
    
    newgenre = sorted(genre.items(), key = lambda x:-x[1])
    
    newlist = list(enumerate(zip(genres, plays)))
    newlist.sort(key = lambda x:[x[1], -x[0]], reverse = True)

    for value, _ in newgenre:
        count = 0
        for idx, temp in newlist:
            if temp[0] == value:
                answer.append(idx)
                count += 1
            if count == 2:
                break

    return answer
