import sys

input = sys.stdin.readline

n = int(input())
raw_nums = input().split()
nums = list()

for i in range(n):
    target = raw_nums[i]

    while len(target) < 10:
        target += target[len(target) - len(raw_nums[i])]

    nums.append((raw_nums[i], target))

nums.sort(key=lambda x: x[1], reverse=True)

if nums[0][0] == "0":
    print(0)
else:
    result = list()
    for num, temp in nums:
        result.append(num)
    print(int("".join(result)))
