import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = sorted([int(input()) for i in range(n)])
lo, hi = 1, house[-1] - house[0]

while lo <= hi:
    mid = lo + (hi - lo) // 2

    cnt = 1
    before = house[0]

    for i in range(1, n):
        if house[i] >= before + mid:
            before = house[i]
            cnt += 1

    if cnt >= c:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)