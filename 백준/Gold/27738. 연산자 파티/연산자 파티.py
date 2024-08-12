import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = 0

for i in range(nums[5] * (n // nums[5]) + 1, n + 1):
    targets = list()
    if i % nums[0] == 0:
        x += i
    if i % nums[1] == 0:
        x %= i
    if i % nums[2] == 0:
        x &= i
    if i % nums[3] == 0:
        x ^= i
    if i % nums[4] == 0:
        x |= i

print(x)
