N = int(input())
trees = list(zip(map(int, input().split()), map(int, input().split())))

trees.sort(key = lambda x: (x[1], x[0]))

answer = 0
for i in range(N):
    answer += (trees[i][0] + (i*trees[i][1]))

print(answer)
