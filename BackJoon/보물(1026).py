n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
a.sort(reverse = True)
result = 0

for i in range(n):
  result += (a[i]*b[i])

print(result)
