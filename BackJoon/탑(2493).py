# 탑의 갯수가 최대 500_000개이므로, 이중 for문을 사용하면 시간 초과가 난다.
# 따라서 자료구조 stack을 사용하여, 자신보다 큰 숫자를 만날때까지 pop을 해준다.
# pop만 해주는 이유는 만약 다음 탑이 현재 탑보다 작으면 현재 탑이 답이 되는 것이고 그렇지 않다면
# 현재 탑보다 크기 때문에 현재 탑에서 했던 방법을 한 번 더 하지 않아도 되기 때문이다.

import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
stack = []
answer = [0]*n

for i in range(len(list)):
    while stack:
        if stack[-1][0] > list[i]:
            answer[i] = stack[-1][1]+1
            break
        else:
            stack.pop()
    stack.append([list[i], i])

# 원하는 답이 [1, 2, 3]이 아닌, 1 2 3 형태이므로, print(answer)를 해주면 오답이 난다.
print(*answer)
