# 현재 로봇의 위치를 좌표의 한 가운데인 (5, 5)로 설정
# 좌표 범위를 넘어가면 건너뛰기
# 로봇이 이동한 길은 취급하지 않기 위해서 이동 전과 이동 후의 좌표를 저장함
# 자료 구조 set을 이용해서 중복된 값을 제가
# 이동 전과 이동 후의 좌표를 한 번에 저장했기 때문에 2로 나누어 정답을 도출

def solution(dirs):
    answer = 0
    move = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    x = 5
    y = 5
    record = []
  
    for i in dirs:
        dx, dy = move[i]
        if not (x+dx <= 10 and x+dx >= 0 and y+dy <= 10 and y+dy >= 0):
            continue
          
        record.append((x,y,x+dx,y+dy))
        record.append((x+dx,y+dy,x,y))
        x += dx
        y += dy
      
    recordset = set(record)
    answer = len(recordset)//2
  
    return answer
