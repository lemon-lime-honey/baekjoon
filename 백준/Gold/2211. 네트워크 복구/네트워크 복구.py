from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
connection = [i for i in range(n + 1)]
lines = [[] for i in range(n + 1)]
times = [int(1e9) for i in range(n + 1)]
times[1] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    lines[a].append((b, c))
    lines[b].append((a, c))

que = deque([(1, 0)])

while que:
    point, time = que.popleft()
    if times[point] < time:
        continue
    for next_point, next_time in lines[point]:
        if time + next_time < times[next_point]:
            connection[next_point] = point
            times[next_point] = time + next_time
            que.append((next_point, time + next_time))

result = 0
rev = list()

for i in range(1, n + 1):
    if connection[i] != i:
        result += 1
        rev.append((i, connection[i]))

print(result)

for r in rev:
    print(*r)