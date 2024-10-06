from collections import deque
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
dish = [int(input()) for i in range(n)]
types = [0 for i in range(d + 1)]
que = deque()
result = 0
cnt = 0

for i in range(k):
    que.append(dish[i])
    if types[dish[i]] == 0:
        cnt += 1
    types[dish[i]] += 1

result = cnt

for i in range(n):
    target = que.popleft()
    types[target] -= 1
    if types[target] == 0:
        cnt -= 1

    que.append(dish[(i + k) % n])
    if types[dish[(i + k) % n]] == 0:
        cnt += 1
    types[dish[(i + k) % n]] += 1

    if types[c] == 0:
        result = max(result, cnt + 1)
    else:
        result = max(result, cnt)

print(result)
