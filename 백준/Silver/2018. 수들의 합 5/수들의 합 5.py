n = int(input())

cnt = 0
lo, hi = 1, 1

while hi <= n:
    addi = (lo + hi) * (hi - lo + 1) // 2
    if addi == n:
        cnt += 1
        lo += 1
    if addi < n:
        hi += 1
    else:
        lo += 1

print(cnt)