# 문제 설명 : n개의 구멍을 가진 원형큐가 존재할 때, 연속적인 n개의 구멍만을 선택하여 두더지를 잡으려고 한다.
# 구멍마다 점수가 다르고 동시에 두더지가 나올 경우에는 하나만 잡을 수 있을 때, 최대 득점을 구하여라.

# 1. 같은 시간의 구멍에서는 하나만 선택할 수 있기에 시간 순으로 오름차순을 할 때, 값이 같다면 점수를 기준으로 내림차순을 해준다.
# 2. 같은 시간에 존재하는 두더지를 한꺼번에 모으기 위해서 new_moles라는 배열을 만들어서 두더지를 완전탐색할 때, 이전 두더지와 시간이 다르다면 구분하여 2차원 배열의 형태를 만들어준다.
# 3. 원형큐에서 큐의 시작과 끝을 같이 선택할 수 있기에 배열의 크기를 두 배로 늘려서 고를 수 있는 구멍의 모든 경우의 수를 구해준다.
# 4. 모든 경우의 수를 비교하며 같은 시간의 큐를 통해서 해당 값이 내가 보고 있는 구멍이라면 score 값을 더하고 넘어간다. 같은 시간의 큐는 점수를 기준으로 내림차순이기 때문에 해당 점수 외에는 최고점을 얻을 수 없다.

def solution(n, m, moles):
    answer = 0

    # 1
    moles.sort(key = lambda x:[x[0], -x[2]])
    new_moles = []

    # 2
    same_time = 0
    all = []
    for time, idx, score in moles:
        if same_time == 0:
            same_time = time
            all.append([idx, score])
        else:
            if same_time == time:
                all.append([idx, score])
            else:
                new_moles.append(all)
                same_time = time
                all = []
                all.append([idx, score])
    if all:
        new_moles.append(all)

    # 3
    temp = []
    for i in range(1, n+1):
        temp.append(i)
    temp *= 2
    combis = []
    for i in range(n):
        combis.append(temp[i:i+m])

    # 4
    for combi in combis:
        count = 0
        now = set()
        for c in combi: # 현재 바라보고 있는 구멍의 번호를 set 자료구조를 이용하여 시간 복잡도를 줄였다.
            now.add(c)
        
        for mole in new_moles:
            for idx, score in mole:
                if idx in now:
                    count += score
                    break

        answer = max(answer, count)
        
    return answer
