from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
food = [int(input()) for i in range(n)]
pick = defaultdict(int)
start, end = 0, k - 1
types = set()
result = 0

for i in range(start, end + 1):
    pick[food[i]] += 1
    if pick[food[i]] == 1: types.add(food[i])

start += 1
end += 1

if end >= n:
    if c not in types: result = len(types) + 1
    else: result = len(types)
    print(result)
else:
    while True:
        pick[food[start - 1]] -= 1
        pick[food[end]] += 1

        if pick[food[start - 1]] == 0:
            types.remove(food[start - 1])
        if pick[food[end]] == 1:
            types.add(food[end])
        if c not in types:
            result = max(result, len(types) + 1)
        else:
            result = max(result, len(types))

        start += 1
        end += 1

        if end >= n: end = 0
        if start >= n: break

    print(result)