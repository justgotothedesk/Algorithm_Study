# 원 쿠션을 할 때 동, 서, 남, 북으로 총 4가지의 쿠션이 발생한다.
# 각각의 모든 경우에서의 거리를 계산하고 그 중에서 최솟값을 반환한다.
# 당구공의 이동 거리를 계산할 때는 '처음 당구공의 위치와 쿠션과의 거리 + 마지막 당구공의 위치와 쿠션과의 거리'가 아닌
# 처음 혹은 마지막 당구공의 위치를 쿠션으로부터 선대칭 이동하여 '처음 당구공의 위치를 선대칭 이동시킨 위치와 마지막 당구공의 위치'로 계산한다.

maxv = float('inf')

def convert(x, y, sx, sy, m, n):
    one = (sx+x)**2+(y-sy)**2
    if y == sy and sx > x:
        one = maxv
        
    four = (sy-y)**2+(2*m-x-sx)**2
    if y == sy and x > sx:
        four = maxv
        
    two = (sy+y)**2+(sx-x)**2
    if x == sx and y < sy:
        two = maxv
    
    three = (sx-x)**2+(2*n-y-sy)**2
    if x == sx and y > sy:
        three = maxv
      
    return min(one, two, three, four)
    
def solution(m, n, startX, startY, balls):
    answer = []
    
    for i in balls:
        x = i[0]
        y = i[1]
        answer.append(convert(x, y, startX, startY, m, n))
    
    return answer
