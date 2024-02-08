def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    one = [0 for _ in range(len(sticker))]
    two = [0 for _ in range(len(sticker))]
    
    one[0] = sticker[0]
    one[1] = one[0]
    
    for i in range(2, len(sticker)-1):
        one[i] = max(one[i-2]+sticker[i], one[i-1])
    
    for i in range(1, len(sticker)):
        two[i] = max(two[i-2]+sticker[i], two[i-1])

    return max(one[-2], two[-1])
