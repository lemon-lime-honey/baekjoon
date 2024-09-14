import sys
input = sys.stdin.readline


def chk(nums, height):
    for idx, num in enumerate(nums):
        if height < num:
            return idx
    return -1


p = int(input())

for i in range(p):
    ipt = list(map(int, input().split()))
    nums = list()
    result = 0

    for height in ipt[1:]:
        if not nums:
            nums.append(height)
        else:
            idx = chk(nums, height)
            if idx == -1:
                nums.append(height)
            else:
                result += len(nums) - idx
                nums.insert(idx, height)

    print(ipt[0], result)
