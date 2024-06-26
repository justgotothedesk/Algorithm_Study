import sys

input = sys.stdin.readline
N = int(input())
sum_ = 0
max_ = 0

for _ in range(N):
    num = int(input())
    sum_ += num
    if num > max_:
        max_ = num

if sum_ - max_ <= max_:
    print(max_ - (sum_ - max_))
else:
    if sum_ % 2:
        print(1)
    else:
        print(0)
