import sys

n, m = map(int, sys.stdin.readline().split())
basket = [k for k in range(1, n + 1)]

for k in range(m):
    i, j = map(int, sys.stdin.readline().split())
    basket = basket[:i - 1] + list(reversed(basket[i - 1:j])) + basket[j:]

print(*basket)