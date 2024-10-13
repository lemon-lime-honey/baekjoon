from collections import deque
import sys

input = sys.stdin.readline


def get_distance(p, q):
    distance = [int(1e9) for i in range(n + 1)]
    distance[p] = 0
    que = deque([(p, 0)])

    while que:
        point, dist = que.popleft()

        if distance[point] < dist:
            continue

        for next_point, next_dist in tree[point]:
            if distance[next_point] <= dist + next_dist:
                continue
            distance[next_point] = dist + next_dist
            que.append((next_point, dist + next_dist))

    return distance[q]


n, m = map(int, input().split())
tree = [[] for i in range(n + 1)]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

for i in range(m):
    a, b = map(int, input().split())
    print(get_distance(a, b))
