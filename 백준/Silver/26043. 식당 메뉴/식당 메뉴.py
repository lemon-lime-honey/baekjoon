from collections import deque
import sys

input = sys.stdin.readline

student = deque()
a, b, c = set(), set(), set()

n = int(input())

for i in range(n):
    ipt = list(map(int, input().split()))
    if ipt[0] == 1:
        student.append((ipt[1], ipt[2]))
    else:
        if student[0][1] == ipt[1]:
            a.add(student[0][0])
        else:
            b.add(student[0][0])
        student.popleft()

while student:
    c.add(student[0][0])
    student.popleft()

if a:
    print(*sorted(a))
else:
    print("None")

if b:
    print(*sorted(b))
else:
    print("None")

if c:
    print(*sorted(c))
else:
    print("None")
