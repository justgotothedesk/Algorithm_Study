# 2023 KAKAO BLIND RECRUITMENT
# 우선 반환점을 기준으로 연속적으로 0인 집들은 가지 않아도 되기 때문에 이들 먼저 제거한다.
# 픽업을 할 때, 현재 들고 있는 것과 들 수 있는 제한량을 비교하며 픽업하고 해당 집으로부터 더 이상 픽업할 것이 없다면 pickups 큐에서 제거하고 그렇지 않다면 다시 추가한다.
# 배달을 할 때도 이와 동일하다.
# 이동거리는 배달과 픽업 중 더 큰 값을 왕복 이동하는 것과 같으므로 max를 사용하여 더 큰 값을 구한다.

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        if deliveries[-1] == 0 and pickups[-1] == 0:
            deliveries.pop()
            pickups.pop()
        else:
            break
            
    while deliveries or pickups:
        now = 0
        answer += max(len(deliveries), len(pickups))*2
        while deliveries:
            d = deliveries.pop()
            if now+d > cap:
                d -= cap-now
                now = 0
                deliveries.append(d)
                break
            else:
                now += d
        now = 0
        while pickups:
            p = pickups.pop()
            if p+now > cap:
                p -= cap-now
                now = 0
                pickups.append(p)
                break
            else:
                now += p
                
    return answer
