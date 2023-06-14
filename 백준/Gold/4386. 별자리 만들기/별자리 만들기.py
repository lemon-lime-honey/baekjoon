from math import sqrt
import sys
input = sys.stdin.readline


def find(s):
    if s != const[s]:
        const[s] = find(const[s])
    return const[s]


def union(s1, s2):
    s1, s2 = find(s1), find(s2)
    if s1 == s2: return True
    if s1 < s2: const[s2] = s1
    else: const[s1] = s2
    return False


n = int(input())
stars = [list(map(float, input().split())) for i in range(n)]
const = [i for i in range(n)]
paths = list()
result = 0

for i in range(n):
    for j in range(i + 1, n):
        distance = sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)
        paths.append((distance, i, j))

paths.sort()

for dist, start, end in paths:
    chk = union(start, end)
    if not chk:
        result += dist

print(f'{result:.2f}')