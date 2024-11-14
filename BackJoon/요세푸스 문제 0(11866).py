from sys import stdin

n, k = map(int,stdin.readline().split())
index = 0
array = list(range(1,N+1))
result = []

while len(array) != 0:
    index += (k-1)
    index %= len(array)
    result.append(array.pop(index))

print("<",end="")
for i in range(n-1):
    print(result[i],end = ", ")
print(result[n-1], end = "")
print(">", end = "")
