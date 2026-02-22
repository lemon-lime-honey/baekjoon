import sys

input = sys.stdin.readline

nums = [1, 1, 3]
result = list()

while True:
    try:
        n = int(input())
        if n <= len(nums) - 1:
            result.append(nums[n])
        else:
            for i in range(len(nums) - 1, n + 1):
                nums.append(nums[-1] + 2 * nums[-2])
            result.append(nums[n])
    except Exception:
        break

print(*result, sep="\n")
