import sys

n, s = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

lo, hi = 0, 0
total = number[0]
min_len = n + 1

while hi < n:
    if total >= s:
        min_len = min(min_len, hi - lo + 1)
        total -= number[lo]
        lo += 1
    elif total == s:
        min_len = min(min_len, hi - lo + 1)
        hi += 1
        lo += 1
    else:
        hi += 1
        if hi == n:
            break
        total += number[hi]

if min_len == (n + 1):
    print(0)
else:
    print(min_len)