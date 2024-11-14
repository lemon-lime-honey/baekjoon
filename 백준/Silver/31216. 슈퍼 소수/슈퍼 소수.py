import sys

input = sys.stdin.readline

prime = [True for i in range(int(1e6))]
prime[0] = False
prime[1] = False

for i in range(2, int(1e3) + 1):
    if prime[i]:
        for j in range(2 * i, int(1e6), i):
            prime[j] = False

nums = list()

for i in range(2, int(1e6)):
    if prime[i]:
        nums.append(i)

sup = list()

for i in range(len(nums)):
    if prime[i + 1]:
        sup.append(nums[i])

t = int(input())
result = list()

for i in range(t):
    n = int(input())
    result.append(sup[n - 1])

print(*result, sep="\n")
