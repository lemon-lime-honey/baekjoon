from math import ceil

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
result = 0

for i in range(n):
    if b >= a[i]: result += 1
    else:
        result += 1 + ceil((a[i] - b) / c)

print(result)