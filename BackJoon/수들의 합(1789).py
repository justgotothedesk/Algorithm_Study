n = int(input())
now = 0
i = 1
answer = 0

while True:
    now += i
    answer += 1
    if now > n:
        answer -= 1
        break
    elif now == n:
        break
    i += 1

print(answer)
