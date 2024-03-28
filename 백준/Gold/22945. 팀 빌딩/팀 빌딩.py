n = int(input())
nums = list(map(int, input().split()))

lo, hi, result = 0, n - 1, 0

while lo < hi:
    result = max(result, (hi - lo - 1) * min(nums[lo], nums[hi]))
    if nums[lo] <= nums[hi]:
        lo += 1
    else:
        hi -= 1

print(result)