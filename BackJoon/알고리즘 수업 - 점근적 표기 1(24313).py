import sys
input = sys.stdin.readline()

def g(n: int) -> int:
    return n

def f(a0: int, a1: int, n: int) -> int:
    return (a1 * n) + a0

a, b = map(int, input().split())
c = int(input())
n = int(input())

if c >= a:
  # compare two functions' initial outcomes
    if c * g(n) >= f(b, a, n):
        print(1)
    else:
        print(0)
else:
    print(0)
