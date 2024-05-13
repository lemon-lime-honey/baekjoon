from collections import defaultdict
import sys
input = sys.stdin.readline


def get(c):
    for i in range(row):
        if (i, c) in sharks:
            global result
            result += sharks.pop((i, c))[0]
            return


def move():
    after = defaultdict(list)
    for key, value in sharks.items():
        d = value[2]
        r, c = key[0], key[1]
        length = value[1]

        while length:
            r += direction[d][0]
            c += direction[d][1]
            if 0 <= r < row and 0 <= c < col:
                length -= 1
            else:
                r -= direction[d][0]
                c -= direction[d][1]
                if d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3: d = 4
                elif d == 4: d = 3

        if (r, c) in after and value[0] < after[(r, c)][0]: continue
        after[(r, c)] = [value[0], value[1], d]

    return after


row, col, amount = map(int, input().split())
sharks = defaultdict(list)
direction = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
result = 0

for i in range(amount):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)].extend([z, s, d])

for i in range(col):
    get(i)
    sharks = move()

print(result)
