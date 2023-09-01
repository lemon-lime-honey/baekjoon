from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
nums = defaultdict(int)

for i in range(n):
    nums[int(input())] += 1

print(sorted(nums.items(), key=lambda x:(-x[1], x[0]))[0][0])