import sys
input = sys.stdin.readline()

num = int(input())
now = 1
answer = 1

while num > now:
  now += 6*now
  answer += 1

print(answer)
