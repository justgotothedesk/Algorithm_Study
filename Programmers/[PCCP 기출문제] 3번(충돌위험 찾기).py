from collections import defaultdict

def solution(points, routes):
    answer = 0
    paths = []

    # 각 로봇의 경로를 사전 계산하여 좌표별로 저장
    for route in routes:
        path = []
        for j in range(len(route) - 1):
            nowx, nowy = points[route[j] - 1]
            targetx, targety = points[route[j + 1] - 1]
            
            # x축 이동
            if nowx < targetx:
                while nowx < targetx:
                    path.append((nowx, nowy))
                    nowx += 1
            elif nowx > targetx:
                while nowx > targetx:
                    path.append((nowx, nowy))
                    nowx -= 1
            
            # y축 이동
            if nowy < targety:
                while nowy < targety:
                    path.append((nowx, nowy))
                    nowy += 1
            elif nowy > targety:
                while nowy > targety:
                    path.append((nowx, nowy))
                    nowy -= 1
            
            # 마지막 목적지 좌표 추가
            path.append((targetx, targety))
        
        paths.append(path)

    # 시간별 좌표에 대한 충돌 여부를 추적
    time_position_count = defaultdict(int)
    max_steps = max(len(path) for path in paths)

    for time in range(max_steps):
        # 현재 시간의 각 로봇 위치를 갱신
        current_positions = set()
        for i, path in enumerate(paths):
            if time < len(path):  # 현재 경로의 위치가 유효할 때
                pos = path[time]
                if pos in current_positions:
                    answer += 1
                else:
                    current_positions.add(pos)
                time_position_count[(time, pos)] += 1

    return answer
