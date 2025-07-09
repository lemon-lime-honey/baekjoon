from collections import defaultdict

n = int(input())

ring = defaultdict(set)
result = list()

for i in range(n):
    p, s = input().split()
    if s == '-':
        continue
    ring[s].add(p)

for val in ring.values():
    if len(val) == 2:
        result.append(val)

print(len(result))

for pair in result:
    print(*pair)
