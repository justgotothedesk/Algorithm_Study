arr = []
N = int(input())

for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = [1 << 30] * (N + 1) 

for i in range(N):
    for j in range(N):
        mid_x, mid_y = arr[i][0], arr[j][1] 

        distance = []
        for h in range(N):  
            distance.append(abs(mid_x - arr[h][0]) + abs(mid_y - arr[h][1]))
        distance.sort() 
        sum_ = 0 
      
        for dist in range(N):
            sum_ += distance[dist]
            if ans[dist + 1] > sum_: 
                ans[dist + 1] = sum_ 

print(*ans[1:])
