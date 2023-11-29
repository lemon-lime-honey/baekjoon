import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))
lo, hi = max(lectures), sum(lectures)
result = int(1e9)

while lo <= hi:
    mid = (lo + hi) // 2
    cnt, size = 1, 0
    
    for lecture in lectures:
        if size + lecture <= mid:
            size += lecture
        else:
            size = lecture
            cnt += 1

    if cnt <= m:
        hi = mid - 1
    else:
        lo = mid + 1

print(lo)