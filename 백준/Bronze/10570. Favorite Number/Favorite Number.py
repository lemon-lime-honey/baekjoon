from collections import defaultdict

n = int(input())

for i in range(n):
    v = int(input())
    nums = defaultdict(int)

    for j in range(v):
        s = int(input())
        nums[s] += 1

    result = sorted(nums.items(), key=lambda x: (-x[1], x[0]))

    print(result[0][0])
