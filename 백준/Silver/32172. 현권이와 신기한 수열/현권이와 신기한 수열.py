n = int(input())

nums = {0}
num = 0

for i in range(1, n + 1):
    target = num - i

    if target < 0 or target in nums:
        target = num + i

    nums.add(target)
    num = target

print(num)
