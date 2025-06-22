a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

for num in (p, m, n):
    print(1 * (0 < num % (a + b) <= a) + 1 * (0 < num % (c + d) <= c))
