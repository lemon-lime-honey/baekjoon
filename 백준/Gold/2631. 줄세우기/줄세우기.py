from bisect import bisect_left

n = int(input())
nums = [int(input()) for i in range(n)]
result = [nums[0]]

for num in nums[1:]:
    if result[-1] < num:
        result.append(num)
    else:
        result[bisect_left(result, num)] = num

print(n - len(result))
