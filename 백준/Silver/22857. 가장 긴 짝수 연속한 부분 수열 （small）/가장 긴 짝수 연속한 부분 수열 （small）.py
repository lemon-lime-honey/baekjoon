import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
lo, cnt, result = 0, 0, 0

for i in range(n):
    if nums[i] % 2:
        if cnt >= k:
            while nums[lo] % 2 == 0:
                lo += 1
            while nums[lo] % 2 == 1 and cnt >= k:
                lo += 1
                cnt -= 1
        cnt += 1
        result = max(result, i - lo - cnt)
    else:
        result = max(result, i - lo + 1 - cnt)

print(result)
