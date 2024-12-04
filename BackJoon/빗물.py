n, m = map(int, input().split())
height = list(map(int,input().split()))

left, right = 0, len(height) - 1
left_max, right_max = height[left], height[right]
result = 0

# height가 빈 리스트라면 0을 return
if not height:
    print(0)

# 두 포인터가 만날때 까지 while문 진행
while left < right:
    left_max = max(left_max, height[left])
    right_max = max(right_max, height[right])
    
    if left_max <= right_max:
        result += left_max - height[left]
        left += 1
    else:
        result += right_max - height[right]
        right -= 1
print(result)
