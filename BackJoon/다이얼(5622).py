import sys
input = sys.stdin.readline

phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

d = input()
answer = 0

for i in range(len(d)):
  for p in phone:
    if d[i] in p:
      answer += (phone.index(p)+3)

print(answer)
