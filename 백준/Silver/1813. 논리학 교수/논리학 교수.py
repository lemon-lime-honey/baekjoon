from collections import Counter

n = int(input())
nums = Counter(map(int, input().split()))
result = -1

for i in range(n, -1, -1):
    if nums.get(i, 0) == i:
        result = i
        break

print(result)
