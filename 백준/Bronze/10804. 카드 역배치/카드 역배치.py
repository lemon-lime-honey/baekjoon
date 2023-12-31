nums = [i for i in range(21)]

for i in range(10):
    a, b = map(int, input().split())
    nums[a:b + 1] = nums[a:b + 1][::-1]

print(*nums[1:])