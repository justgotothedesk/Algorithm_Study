import statistics
import math
import random
import timeit

def simulate(n, t):
    def root(i):
        while i != ids[i]:
            i = ids[i]
        return i

    def connected(p, q):
        return root(p) == root(q)

    def union(p, q):
        id1, id2 = root(p), root(q)
        if id1 == id2:
            return
        if size[id1] <= size[id2]:
            ids[id1] = id2
            size[id2] += size[id1]
        else:
            ids[id2] = id1
            size[id1] += size[id2]

    result = []
    first = n*n
    last = n*n+1

    for _ in range(t):
        count = 0
        idx = []
        ids = []
        size = []
        visited = []

        for i in range(n*n):
            idx.append(i)
        random.shuffle(idx)

        for i in range(n*n+2):
            ids.append(i)
            size.append(1)
            visited.append(0)

        while True:
            now = idx.pop()

            if now%n != 0 and visited[now - 1] == 1:
                union(now, now-1)
            if (now+1)%n != 0 and visited[now + 1] == 1:
                union(now, now+1)
            if now-n >= 0 and visited[now-n] == 1:
                union(now, now-n)
            if now+n < n*n and visited[now+n] == 1:
                union(now, now+n)

            visited[now] = 1
            count += 1
            
            if 0 <= now < n:
                union(first, now)
            if n*n-n <= now <n*n:
                union(last, now)

            if connected(first, last):
                result.append(count/(n**2))
                break

    mean = statistics.mean(result)
    stdev = statistics.stdev(result)

    return mean, stdev


'''
Simulate the performance of Quick Union
'''
def simulateQU(n, t):
    def root(i):
        nonlocal ids
        while i != ids[i]: i = ids[i]
        return i

    def connected(p, q):
        return root(p) == root(q)

    def union(p, q):
        nonlocal ids
        id1, id2 = root(p), root(q)
        ids[id1] = id2
    
    for _ in range(t):
        ids = [i for i in range(n*n + 2)]
        for _ in range(math.floor(n*n*2)):
            connected(0, len(ids)-1)
            union(random.randint(0, len(ids)-1), random.randint(0, len(ids)-1))

'''
Simulate the performance of Quick Find
'''
def simulateQF(n, t):
    def connected(p, q):
        nonlocal ids
        return ids[p] == ids[q]

    def minMax(a, b):
        if a < b: return a, b
        else: return b, a

    def union(p, q):
        nonlocal ids
        id1, id2 = minMax(ids[p], ids[q])
        for idx, _ in enumerate(ids):
            if ids[idx] == id2: ids[idx] = id1
    
    for _ in range(t):
        ids = [i for i in range(n*n + 2)]
        for _ in range(math.floor(n*n*2)):
            connected(0, len(ids)-1)
            union(random.randint(0, len(ids)-1), random.randint(0, len(ids)-1))


'''
Unit Test
'''
if __name__ == "__main__":

    print("Correctness test for simulate()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    correct = True
    
    input = 1,100
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if rt_val[0] == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if rt_val[1] == 0: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()    

    input = 2,10000
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if math.floor(rt_val[0]*100) == 66: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if round(rt_val[1]*10) == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()

    input = 200,100
    rt_val = simulate(*input)
    print(f"simulate{input}: {rt_val} ", end="")
    if math.floor(rt_val[0]*100) == 59: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    if round(rt_val[1]*100) == 1: print("Pass ", end="")
    else:
        print("Fail ", end="")
        correct = False
    print()


    print()
    print()
    print("Speed test for simulate()")
    if not correct: print("Fail (since the algorithm is not correct)")
    else:
        repeat = 10
        input = 10,100
        simulateCompare = simulateQF
        tSubmittedCode = timeit.timeit(lambda: simulate(*input), number=repeat) / repeat
        tCodeToCompare = timeit.timeit(lambda: simulateCompare(*input), number=repeat) / repeat
        print(f"Average running time of simulate{input} and {simulateCompare.__name__}{input} : {tSubmittedCode:.10f} and {tCodeToCompare:.10f} ", end="")        
        if tSubmittedCode < tCodeToCompare * 0.2: print("Pass ", end="")
        else:
            print("Fail ", end="")
        print()
        #print(tSubmittedCode / tCodeToCompare)

        repeat = 10
        input = 10,100
        simulateCompare = simulateQU
        tSubmittedCode = timeit.timeit(lambda: simulate(*input), number=repeat) / repeat
        tCodeToCompare = timeit.timeit(lambda: simulateCompare(*input), number=repeat) / repeat
        print(f"Average running time of simulate{input} and {simulateCompare.__name__}{input} : {tSubmittedCode:.10f} and {tCodeToCompare:.10f} ", end="")        
        if tSubmittedCode < tCodeToCompare * 0.3: print("Pass ", end="")
        else:
            print("Fail ", end="")
        print()        
        #print(tSubmittedCode / tCodeToCompare)


        
    
