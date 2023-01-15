import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    command = list(map(str, sys.stdin.readline().split()))
    if len(command) == 2:
        queue.append(command[1])
    else:
        if command[0] == 'pop':
            try:
                print(queue.popleft())
            except:
                print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            try:
                print(queue[0])
            except:
                print(-1)
        elif command[0] == 'back':
            try:
                print(queue[-1])
            except:
                print(-1)