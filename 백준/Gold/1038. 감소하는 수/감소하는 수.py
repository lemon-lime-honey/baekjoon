from itertools import combinations

n = int(input())
nums = list()

for i in range(1, 11):
    for j in combinations(range(10), i):
        nums.append(int(''.join(list(map(str, reversed(list(j)))))))

nums.sort()

if len(nums) <= n: print(-1)
else: print(nums[n])