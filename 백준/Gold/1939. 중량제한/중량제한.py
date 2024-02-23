from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
weights = [[] for i in range(n + 1)]
max_weight = 0

for i in range(m):
    a, b, c = map(int, input().split())
    weights[a].append((b, c))
    weights[b].append((a, c))
    max_weight = max(max_weight, c)

start, end = map(int, input().split())
lo, hi = 1, max_weight

while lo <= hi:
    mid = lo + (hi - lo) // 2
    chk = [False for i in range(n + 1)]
    que = deque([(max_weight + 1, start)])
    
    while que:
        weight, point = que.popleft()
        for next_point, next_weight in weights[point]:
            if next_weight < mid or chk[next_point]:
                continue
            que.append((min(weight, next_weight), next_point))
            chk[next_point] = True

    if chk[end]:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)