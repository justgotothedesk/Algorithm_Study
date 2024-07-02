n = int(input())
word = input()
W_acc = [0]*n
E_acc = [0]*n

W_acc[0] = int(word[0] == 'W')
E_acc[-1] = int(word[-1] == 'E')

idx = n-2
for i in range(1, n):
    W_acc[i] = W_acc[i-1] + int(word[i] == 'W')
    E_acc[idx] = E_acc[idx+1] + int(word[idx] == 'E')
    idx -= 1

answer = 0
for i in range(n):
    if word[i] == 'H':
        answer += (W_acc[i]*(pow(2, E_acc[i], 1000000007)-E_acc[i]-1))

print(answer % 1000000007)
