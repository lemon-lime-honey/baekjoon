n = int(input())

result = list()

for i in range(n):
    nums = input().split()
    res = int(nums[0][::-1]) + int(nums[1][::-1])
    result.append(int(str(res)[::-1]))

print(*result, sep="\n")
