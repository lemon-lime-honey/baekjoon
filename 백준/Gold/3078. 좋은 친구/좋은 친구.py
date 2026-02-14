import sys

input = sys.stdin.readline

n, k = map(int, input().split())
cnt = [0 for i in range(21)]
length = list()
result = 0

for i in range(n):
    name = input().strip()
    length.append(len(name))

for i in range(n):
    if i > k:
        cnt[length[i - k - 1]] -= 1
    result += cnt[length[i]]
    cnt[length[i]] += 1

print(result)
