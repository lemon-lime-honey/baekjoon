from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    charge = list()
    for i in range(n):
        charge.append(tuple(map(int, input().split())))
    end = tuple(map(int, input().split()))

    que = deque([start])
    visited = {start}
    result = False

    while que:
        r, c = que.popleft()
        if abs(end[0] - r) + abs(end[1] - c) <= 1000:
            result = True
            break
        for coord in charge:
            if (coord in visited or
                abs(r - coord[0]) + abs(c - coord[1]) > 1000):
                continue
            visited.add(coord)
            que.append(coord)

    print('happy' if result else 'sad')