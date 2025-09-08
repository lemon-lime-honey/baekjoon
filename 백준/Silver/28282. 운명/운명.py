from collections import Counter

x, k = map(int, input().split())
socks = list(map(int, input().split()))

left = Counter(socks[:x])
right = Counter(socks[x:])

result = 0

for key, val in left.items():
    result += val * (x - right[key])

print(result)
