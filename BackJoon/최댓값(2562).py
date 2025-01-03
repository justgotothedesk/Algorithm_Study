import sys
input = sys.stdin.readline

numbers = []

for _ in range(9):
    numbers.append(int(input()))
    
maxv = max(numbers)
maxi = numbers.index(maxv)

print(maxv)
print(maxi+1)
