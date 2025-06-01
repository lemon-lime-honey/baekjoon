t = int(input())

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    result = 0
    for j in range(n - 1):
        for k in range(j + 1, n):
            lo, hi = k + 1, n - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[k] - nums[j] == nums[mid] - nums[k]:
                    result += 1
                    break
                elif nums[k] - nums[j] < nums[mid] - nums[k]:
                    hi = mid - 1
                else:
                    lo = mid + 1
    print(result)
