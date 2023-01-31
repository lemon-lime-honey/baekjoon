import sys
from collections import Counter

n, m, b = map(int, sys.stdin.readline().split())
ground = Counter()

for i in range(n):
    ground.update(list(map(int, sys.stdin.readline().split())))

sorted_level = sorted(ground.items(), key = lambda x: x[0], reverse = True)
min_time = 256 * m * n
ref = sorted_level[0][0]
level = 0

while ref >= 0:
    brick = 0
    time = 0
    for lev in sorted_level:
        if lev[0] < ref:
            brick += (ref - lev[0]) * lev[1]
            time += (ref - lev[0]) * lev[1]
        elif lev[0] > ref:
            brick -= (lev[0] - ref) * lev[1]
            time += 2 * (lev[0] - ref) * lev[1]
    if (brick <= b) * (time < min_time):
        min_time = time
        level = ref
    ref -= 1

print(f'{min_time} {level}')