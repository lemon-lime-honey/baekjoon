import sys

while True:
    m, f = map(int, sys.stdin.readline().split())
    if (m == 0) * (f == 0):
        break
    else:
        print(m + f)