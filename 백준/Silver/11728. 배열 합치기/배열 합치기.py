n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = list()
ap = 0
bp = 0

while ap <= n and bp <= m:
    if ap == n:
        result.append(b[bp])
        bp += 1
    elif bp == m:
        result.append(a[ap])
        ap += 1
    else:
        if a[ap] <= b[bp]:
            result.append(a[ap])
            ap += 1
        else:
            result.append(b[bp])
            bp += 1
    if ap >= n and bp >= m:
        break

print(*result)