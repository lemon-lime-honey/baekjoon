import sys
from copy import deepcopy

input = sys.stdin.readline

m = int(input())
func = [0] + list(map(int, input().split()))
table = [deepcopy(func) for j in range(21)]

for i in range(1, 21):
    for j in range(1, m + 1):
        table[i][j] = table[i - 1][table[i - 1][j]]

q = int(input())
result = list()

for i in range(q):
    n, x = map(int, input().split())

    for j in range(21):
        if (n >> j) & 1:
            x = table[j][x]

    result.append(x)

print(*result, sep="\n")
