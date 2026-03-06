n = int(input())

result = 0

for i in range(n):
    nums = list(map(int, input().split()))
    trick = nums[2:]
    trick.sort()
    result = max(result, max(nums[:2]) + sum(trick[3:]))

print(result)
