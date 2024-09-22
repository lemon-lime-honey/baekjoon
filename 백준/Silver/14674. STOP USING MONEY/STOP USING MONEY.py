import sys
from functools import cmp_to_key

input = sys.stdin.readline


def compare(x, y):
    chk1 = x[2] * y[1]
    chk2 = x[1] * y[2]
    if chk1 < chk2: 
        return 1
    elif chk2 < chk1:
        return -1
    elif x[1] < y[1]:
        return -1
    elif x[1] > y[1]:
        return 1
    elif x[0] < y[0]:
        return -1
    return 1

n, k = map(int, input().split())
games = [list(map(int, input().split())) for i in range(n)]

games.sort(key=cmp_to_key(compare))

print(*[x[0] for x in games[:k]], sep="\n")
