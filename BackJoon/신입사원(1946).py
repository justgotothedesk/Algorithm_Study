import sys

input = sys.stdin.readline
T = int(input())

for tc in range(T):
    N = int(input())
    freshman = [list(map(int, input().split())) + [i + 1] for i in range(N)]

    freshman.sort(key=lambda x: x[0])

    rank = freshman[0][1]
    cnt = 1

    for i in range(1, N):
        if rank > freshman[i][1]:
            rank = freshman[i][1]
            cnt += 1
          
    print(cnt)
