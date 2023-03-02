from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    ipt = deque(sys.stdin.readline().rstrip())
    que1 = deque()
    que2 = deque()
    
    for element in ipt:
        if element == '<':
            if que1:
                que2.appendleft(que1.pop())
        elif element == '>':
            if que2:
                que1.append(que2.popleft())
        elif element == '-':
            if que1:
                que1.pop()
        else:
            que1.append(element)
    
    print(*que1, *que2, sep = '')