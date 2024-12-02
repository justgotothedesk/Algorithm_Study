import sys
from sys import stdin

from collections import deque
queue=deque()

def push(x) :
    queue.append(x)

def pop():
    if(len(queue) == 0):
        print(-1)   
    else:
        print(queue.popleft()) 

def size():
    print(len(queue))

def empty():
    if(len(queue) == 0):
        print(1)
    else:
        print(0)

def front():
    if(len(queue)==0):
        print(-1)
    else:
        print(queue[0])

def back(): 
    if(len(queue)==0):
        print(-1)
    else:
        print(queue[-1])

N = int(stdin.readline())
for i in range(N):
    k = stdin.readline().split()
    if(k[0] == 'push'):
        push(int(k[1]))
    elif(k[0]=='pop'):
        pop()
    elif(k[0]=='size'):
        size()
    elif(k[0]=='empty'):
        empty()
    elif(k[0]=='front'):
        front()
    elif(k[0]=='back'):
        back()
