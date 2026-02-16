import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())

videos = [0] + list(map(int, input().split()))
sequence = [0] + list(map(int, input().split()))

table = [[0 for i in range(k + 1)] for j in range(31)]
table[0] = sequence

result = list()

for i in range(1, 31):
    for j in range(1, k + 1):
        table[i][j] = table[i - 1][table[i - 1][j]]

for i in range(1, n + 1):
    target = videos[i]

    for j in range(31):
        if ((m - 1) >> j) & 1:
            target = table[j][target]

    result.append(target)

print(*result)
