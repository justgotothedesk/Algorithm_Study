import sys
from itertools import combinations
input = sys.stdin.readline()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

for i in range(combinations(arr, 3)):
  if sum(i) > answer and sum(i) <= m:
    answer = sum(i)

print(answer)
