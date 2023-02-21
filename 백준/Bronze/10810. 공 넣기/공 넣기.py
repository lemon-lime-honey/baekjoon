import sys

n, m = map(int, sys.stdin.readline().split())
basket = [0] * n

for l in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for m in range(i - 1, j):
        basket[m] = k

print(*basket)