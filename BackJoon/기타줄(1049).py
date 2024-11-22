import sys
input = sys.stdin.readline

n, m = map(int, input().split())
price6 = []
price1 = []

for i in range(m):
  a,b = map(int, input().split())
  price6.append(a)
  price1.append(b)

sum = 0
while True:
  if n <= 6:
    sum += min(min(price6), min(price1)*n)
    break
  else:
    sum += min(min(price6), min(price1)*6)
    n -= 6

print(sum)
