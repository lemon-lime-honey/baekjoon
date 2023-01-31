import sys
from collections import deque

t = int(sys.stdin.readline())
for i in range(t):
    m, n = map(int, sys.stdin.readline().split())
    space = [deque([])for i in range(n)]
    dist = 0

    for j in range(m):
        temp = list(map(int, sys.stdin.readline().split()))
        for k in range(n):
            space[k].appendleft(temp[k])
    
    for j in range(n):
        zero = 0
        one = 0
        last = None
        for k in range(m):
            if (k == 0) * space[j][k]:
                last = 0
                continue
            if space[j][k] == 0:
                zero += 1
            else:
                dist += zero
                if last == None:
                    last = 0
                else:
                    last += 1
                zero = k - last
    print(dist)