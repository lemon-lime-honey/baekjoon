import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for i in range(n)])
lo, hi = 0, 0
result = int(1e12)

while lo <= hi and hi < n:
    if a[hi] - a[lo] >= m:
        result = min(result, a[hi] - a[lo])
        lo += 1
    else:
        hi += 1

print(result)