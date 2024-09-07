n, k = map(int, input().split())
weights = sorted(list(map(int, input().split())))
result, lo, hi = 0, 0, n - 1

while lo < hi:
    chk = weights[lo] + weights[hi]
    if chk <= k:
        result += 1
        lo += 1
        hi -= 1
    else:
        hi -= 1

print(min(result, n))
