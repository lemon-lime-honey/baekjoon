import sys

t = int(sys.stdin.readline())

for i in range(t):
    blank = sys.stdin.readline()
    n = int(sys.stdin.readline())
    candy = 0
    for j in range(n):
        candy += int(sys.stdin.readline())
    if candy % n == 0:
        print("YES")
    else:
        print("NO")