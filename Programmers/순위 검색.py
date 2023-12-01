# 2021 KAKAO BLIND RECRUITMENT
# 데이터가 10만개까지 있으므로 이중 for문을 사용하면 시간초과가 발생한다.
# 따라서 이진 탐색을 사용하고 해당 카테고리에서 발생할 수 있는 모든 경우의 수를 구해서 갯수를 구한다.

def izin(arr, num):
    start, end = 0, len(arr)
    mid = (start+end)//2

    while start < end:
        mid = (start+end)//2
        if arr[mid] < num:
            start = mid+1
        else:
            end = mid

    if arr[mid] < num:
        return len(arr)-mid-1
    else:
        return len(arr)-mid 

def solution(info, query):
    answer = []
    dd = {}
    lan = ["cpp", "java", "python", "-"]
    pos = ["backend", "frontend", "-"]
    year = ["junior", "senior", "-"]
    food = ["chicken", "pizza", "-"]
    
    for i in lan:
        for j in pos:
            for k in year:
                for l in food:
                    res = i+j+k+l
                    if res not in dd:
                        dd[res] = []
    
    for i in info:
        di = i.split(" ")
        l, p, y, f, s = ["-", di[0]], ["-", di[1]], ["-", di[2]], ["-", di[3]], int(di[4])
        for j in l:
            for k in p:
                for l in y:
                    for m in f:
                        res = j+k+l+m
                        dd[res].append(s)
    
    for i in lan:
        for j in pos:
            for k in year:
                for l in food:
                    res = i+j+k+l
                    dd[res].sort()
    
    for i in query:
        di = i.split(" ")
        l, p, y, f, s = di[0], di[2], di[4], di[6], int(di[7])
        res = l+p+y+f
        if dd[res]:
            answer.append(izin(dd[res], s))
        else:
            answer.append(0)
    
    return answer
