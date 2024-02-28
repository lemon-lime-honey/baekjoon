import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
points = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    x, y = map(int, input().split())
    if y > l: continue
    left = x + y - l
    right = x - y + l
    lo, hi = 0, m - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if points[mid] < left:
            lo = mid + 1
        elif points[mid] > right:
            hi = mid - 1
        else:
            result += 1
            break

print(result)