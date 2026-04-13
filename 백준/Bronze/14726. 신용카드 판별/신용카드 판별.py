t = int(input())

result = list()

for i in range(t):
    num = input()
    nums = list()

    for j in range(16):
        if j % 2 == 0:
            target = 2 * int(num[j])
            target = target % 10 + target // 10
        else:
            target = int(num[j])
        nums.append(target)

    if sum(nums) % 10:
        result.append("F")
    else:
        result.append("T")

print(*result, sep="\n")
