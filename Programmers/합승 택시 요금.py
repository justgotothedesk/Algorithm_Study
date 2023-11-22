# 2021 KAKAO BLIND RECRUITMENT
# 모든 경우의 순회 경로 비용을 dist 배열에 저장한다.
# 지점의 갯수(n)가 최대 200개이므로, floyd 알고리즘을 사용하여 각 지점의 최단 거리를 구한다.
# 문제에서 제시된 거리의 최솟값을 구한다.

INF=200*100000

def minimum(dist, n):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if dist[start][mid]+dist[mid][end]<dist[start][end]:
                    dist[start][end]=dist[start][mid]+dist[mid][end]

def solution(n, s, a, b, fares):
    answer = INF
    dist=[[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i]=0
    for edge in fares:
        dist[edge[0]-1][edge[1]-1]=edge[2]
        dist[edge[1]-1][edge[0]-1]=edge[2]
    minimum(dist,n)
    for i in range(n):
        answer=min(answer,dist[s-1][i]+dist[i][a-1]+dist[i][b-1])
    return answer
