from bisect import bisect_left
import sys
input = sys.stdin.readline

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    arr = [int(input()) for i in range(n)]
    nums = [arr[0]]

    for i in range(1, n):
        if nums[-1] < arr[i]:
            nums.append(arr[i])
        else:
            index = bisect_left(nums, arr[i])
            nums[index] = arr[i]

    result.append(len(nums))

print(*result, sep="\n")
