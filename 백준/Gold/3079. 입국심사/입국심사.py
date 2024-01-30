import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = sorted([int(input()) for i in range(n)])

lo, hi = t[0], t[-1] * m

while lo <= hi:
    mid = lo + (hi - lo) // 2
    cnt = 0

    for i in range(n):
        cnt += mid // t[i]

    if cnt < m:
        lo = mid + 1
    else:
        hi = mid - 1

print(lo)