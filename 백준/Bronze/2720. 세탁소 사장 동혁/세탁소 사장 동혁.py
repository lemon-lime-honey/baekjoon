import sys

t = int(sys.stdin.readline())

for i in range(t):
    q = 0
    d = 0
    n = 0
    p = 0
    c = int(sys.stdin.readline())
    if c >= 25:
        q = c // 25
        c %= 25
    if c >= 10:
        d = c // 10
        c %= 10
    if c >= 5:
        n = c // 5
        c %= 5
    if c > 0:
        p = c
    print(f'{q} {d} {n} {p}')