import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snack = list(map(int, input().split()))
lo, hi = 1, max(snack)
result = 0

while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0
    for s in snack:
        cnt += s // mid
    if cnt < m:
        hi = mid - 1
    else:
        result = mid
        lo = mid + 1

print(result)
