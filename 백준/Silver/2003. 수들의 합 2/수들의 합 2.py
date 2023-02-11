n, m = map(int, input().split())
number = list(map(int, input().split()))
lo, hi = 0, 0
cnt = 0

while hi < len(number):
    total = 0
    for i in range(lo, hi + 1):
        total += number[i]
    
    if total < m:
        hi += 1
    if total == m:
        cnt += 1
        lo += 1
    if total > m:
        lo += 1

print(cnt)