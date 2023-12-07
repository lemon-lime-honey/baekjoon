from bisect import bisect_left
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for i in range(n)])

for i in range(m):
    target = int(input())
    chk = bisect_left(a, target)
    
    if chk < n and chk > -1 and a[chk] == target:
        print(chk)
    else:
        print(-1)