# 2024 KAKAO WINTER INTERNSHIP
# 누가 주고 받았는지에 대한 정보는 문자열로 되어 있기 때문에 이를 정수로 변환하여 딕셔너리가 아닌 배열 자료구조를 사용할 수 있도록 한다.
# graph 배열에 row에는 준 사람, col에는 받은 사람의 갯수를 저장한다.
# score 배열에 선물 지수에 대한 정보를 저장한다.
# graph 배열을 하나하나 탐색하며, 해당 값이 0이 아닐 때 반대 상황의 값을 통해 누가 더 큰 지를 비교하고, 만약 값이 동일하다면 score 배열을 통해 판단한다.

def solution(friends, gifts):
    idx = 0
    convert = {}
    for friend in friends:
        convert[friend] = idx
        idx += 1
    
    answer = 0
    score = [0]*len(friends)
    graph = [[0]*len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        give, receive = gift.split()
        graph[convert[give]][convert[receive]] += 1
        score[convert[give]] += 1
        score[convert[receive]] -= 1
    
    for i in range(len(graph)):
        temp = 0
        for j in range(len(graph[i])):
            if i == j:
                continue
            if graph[i][j] and graph[i][j] > graph[j][i]:
                temp += 1
            elif graph[i][j] == graph[j][i]:
                if score[i] > score[j]:
                    temp += 1
        answer = max(answer, temp)               
    
    return answer
