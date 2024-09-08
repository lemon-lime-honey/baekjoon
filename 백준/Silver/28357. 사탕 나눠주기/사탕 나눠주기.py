import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
lo, hi = 0, max(nums)

while lo < hi:
    mid = (lo + hi) // 2
    candy = 0

    for num in nums:
        if mid < num:
            candy += num - mid

    if candy > k:
        lo = mid + 1
    else:
        hi = mid

print(lo)
