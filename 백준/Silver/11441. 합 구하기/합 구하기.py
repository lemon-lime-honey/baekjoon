import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

sums = [0 for i in range(n)]
sums[0] = nums[0]

for i in range(1, n):
    sums[i] = sums[i - 1] + nums[i]

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(sums[b - 1] - sums[a - 1] + nums[a - 1])