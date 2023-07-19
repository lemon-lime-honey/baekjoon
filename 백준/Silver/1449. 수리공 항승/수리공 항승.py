from collections import deque
import sys
input = sys.stdin.readline

n, l = map(int, input().split())
points = deque(sorted(list(map(int, input().split()))))
ref = points[0]
points.popleft()
result = 1

while points:
    if points[0] < ref + l:
        points.popleft()
    else:
        ref = points.popleft()
        result += 1

print(result)