import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1):
    for j in range(len(triangle[i])+1): 
        if j == 0 : triangle[i+1][j] += triangle[i][j]

        elif (j == (len(triangle[i+1]))-1):
            triangle[i+1][j] += triangle[i][j-1]
        else:
            triangle[i+1][j] += max(triangle[i][j], triangle[i][j-1])

print(max(triangle[-1]))
