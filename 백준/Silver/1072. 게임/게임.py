x, y = map(int, input().split())
z = y * 100 // x
result, lo, hi = -1, 0, int(1e9)

while lo <= hi:
    mid = (lo + hi) // 2
    nz = (y + mid) * 100 // (x + mid)

    if nz != z:
        result = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(result)