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
