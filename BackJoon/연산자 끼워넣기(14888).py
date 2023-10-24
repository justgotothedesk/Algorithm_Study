import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxv = -float('inf')
minv = float('inf')

#dfs 재귀호출을 통해서 모든 경우의 연산에서의 최솟값과 최댓값을 구한다.
def dfs(i, now):
    global maxv, minv, add, sub, mul, div

    if i == n:
        maxv = max(maxv, now)
        minv = min(minv, now)
    
    if add > 0:
        add -= 1
        dfs(i+1, now+data[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i+1, now-data[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i+1, now*data[i])
        mul += 1
    if div > 0:
        div -= 1
        dfs(i+1, int(now/data[i]))
        div += 1

dfs(1, data[0])
print(maxv)
print(minv)
