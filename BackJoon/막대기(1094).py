import sys
input = sys.stdin.realine()

n = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
answer = 0

for i in range(len(stick)):
  if n == 0:
    break
  if stick[i] <= n:
    n -= stick[i]
    answer += 1

print(answer)
