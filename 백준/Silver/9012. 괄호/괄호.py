import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range(t):
    flag = 0
    ps = deque()
    inp = sys.stdin.readline().strip()
    for item in inp:
        if (item == '('):
            ps.append('(')
        else:
            try:
                ps.pop()
            except:
                flag = 1
                break
    if (len(ps) == 0 and (flag == 0)):
        print("YES")
    else:
        print("NO")
