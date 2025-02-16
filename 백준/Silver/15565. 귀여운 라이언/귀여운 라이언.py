n, k = map(int, input().split())
data = list(map(int, input().split()))

lo, hi = 0, 0
result = int(1e9)
cnt = 0 if data[hi] == 2 else 1

while hi < n:
    if cnt == k:
        result = min(result, hi - lo + 1)
        if data[lo] == 1:
            cnt -= 1
        lo += 1
    else:
        hi += 1
        if hi < n and data[hi] == 1:
            cnt += 1

print(-1 if result == int(1e9) else result)
