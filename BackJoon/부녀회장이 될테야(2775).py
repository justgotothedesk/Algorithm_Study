def summer(k, n):
    sum = 0
    if k == 0:
        sum += n
    elif k == 1:
        for i in range(1, n+1):
            sum += i
    else:
        for i in range(1, n+1):
            sum += i * summer(k-2, n-i+1)
    return sum
 
tc = int(input())
 
for i in range(tc):
    k = int(input())
    n = int(input())
    print(summer(k,n))
