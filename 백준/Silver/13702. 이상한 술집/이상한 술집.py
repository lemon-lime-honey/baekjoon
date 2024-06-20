import sys
input = sys.stdin.readline

n, k = map(int, input().split())
liquid = [int(input()) for i in range(n)]
liquid.sort()

lo, hi = 1, liquid[-1]
result = 1

while lo <= hi:
    mid = lo + (hi - lo) // 2
    cnt = 0
    for l in liquid:
        cnt += l // mid
    if cnt < k:
        hi = mid - 1
    else:
        lo = mid + 1
        result = mid

print(result)
