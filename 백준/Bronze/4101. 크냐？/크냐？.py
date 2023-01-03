import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if (n == 0) * (m == 0):
        break
    if n > m:
        print('Yes')
    else:
        print('No')