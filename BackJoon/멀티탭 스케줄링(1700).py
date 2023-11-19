import sys
input = sys.stdin.readline

n, k = map(int, input().split())
info = list(map(int, input().split()))
plug = [0]*n
answer = 0

for i in range(len(info)):
    if info[i] in plug:
        continue

    if 0 in plug:
        plug[plug.index(0)] = info[i]
        continue
      
    q = []
    qq = []
    check = False
  
    for j in range(len(plug)):
        if plug[j] not in info[i:]:
            plug[j] = info[i]
            check = True
            answer += 1
            break
          
        for k in range(i, len(info)):
            if plug[j] == info[k] and plug[j] not in q:
                q.append(plug[j])
                qq.append([k, plug[j]])
    
    if not check:
        qq.sort(key = lambda x:-x[0])
        value = qq[0][1]
        plug[plug.index(value)] = info[i]
        answer += 1

print(answer)
