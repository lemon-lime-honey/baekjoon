import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = list()
lo, hi = 0, 0
result = 0

for i in range(n):
    money.append(int(input()))
    hi += money[-1]

while lo < hi:
    mid = lo + (hi - lo) // 2
    total = mid
    flag = True
    cnt = 1
    for cash in money:
        if mid < cash:
            flag = False
            break
        if total < cash:
            total = mid
            cnt += 1
        total -= cash
    if not flag or cnt > m:
        lo = mid + 1
    else:
        hi = mid

print(lo)
