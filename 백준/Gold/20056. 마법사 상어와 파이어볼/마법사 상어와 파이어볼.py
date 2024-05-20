from collections import defaultdict
import sys
input = sys.stdin.readline


def run(fire):
    next_fire = defaultdict(list)
    for key, value in fire.items():
        for m, s, d in value:
            nr, nc = (key[0] + mvmt[d][0] * s) % n, (key[1] + mvmt[d][1] * s) % n
            next_fire[(nr, nc)].append((m, s, d))

    add = dict()
    delete = list()

    for key, value in next_fire.items():
        if len(value) > 1:
            odd = 0
            mass = 0
            speed = 0
            even = False
            for m, s, d in value:
                if d % 2: odd += 1
                mass += m
                speed += s
            if odd in (0, len(value)): even = True
            mass //= 5
            speed //= len(value)
            if mass: add[key] = [mass, speed, even]
            delete.append(key)

    for key in delete:
        next_fire.pop(key)

    for key, value in add.items():
        if value[2]:
            for i in (0, 2, 4, 6):
                next_fire[key].append((value[0], value[1], i))
        else:
            for i in (1, 3, 5, 7):
                next_fire[key].append((value[0], value[1], i))

    return next_fire


mvmt = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

n, m, k = map(int, input().split())
fire = defaultdict(list)

for i in range(m):
    r, c, m, s, d = map(int, input().split())
    fire[(r, c)].append((m, s, d))

for i in range(k):
    fire = run(fire)

result = 0

for value in fire.values():
    for v in value:
        result += v[0]

print(result)