import sys
from collections import deque

n = int(sys.stdin.readline())
result = deque()

for i in range(n):
    command = sys.stdin.readline().split()
    try:
        command[1] = int(command[1])
        result.append(command[1])
    except:
        if (command[0] == 'pop'):
            try:
                print(result.popleft())
            except:
                print(-1)
        elif (command[0] == 'size'):
            print(len(result))
        elif (command[0] == 'empty'):
            if (len(result)):
                print(0)
            else:
                print(1)
        elif (command[0] == 'front'):
            try:
                print(result[0])
            except:
                print(-1)
        elif (command[0] == 'back'):
            try:
                print(result[-1])
            except:
                print(-1)