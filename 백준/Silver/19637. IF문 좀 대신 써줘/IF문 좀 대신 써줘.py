import sys
input = sys.stdin.readline

n, m = map(int, input().split())
title = [input().split() for i in range(n)]

for i in range(m):
    power = int(input())
    lo, hi = 0, n - 1

    while lo < hi:
        mid = (lo + hi) // 2
        if power <= int(title[mid][1]):
            hi = mid
        else:
            lo = mid + 1

    print(title[lo][0])