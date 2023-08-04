from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
que = deque()

for i in range(n):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        que.appendleft(cmd[1])
    elif cmd[0] == 2:
        que.append(cmd[1])
    elif cmd[0] == 3:
        print(que.popleft() if que else -1)
    elif cmd[0] == 4:
        print(que.pop() if que else -1)
    elif cmd[0] == 5:
        print(len(que))
    elif cmd[0] == 6:
        print(0 if que else 1)
    elif cmd[0] == 7:
        print(que[0] if que else -1)
    elif cmd[0] == 8:
        print(que[-1] if que else -1)