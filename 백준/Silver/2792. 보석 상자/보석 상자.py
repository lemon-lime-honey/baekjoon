import sys
input = sys.stdin.readline

n, m = map(int, input().split())
jewels = sorted([int(input()) for i in range(m)])
lo, hi = 1, jewels[-1]
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    total = 0

    for jewel in jewels:
        total += jewel // mid
        if jewel % mid:
            total += 1

    if total > n:
        lo = mid + 1
    else:
        hi = mid - 1
        result = mid

print(result)