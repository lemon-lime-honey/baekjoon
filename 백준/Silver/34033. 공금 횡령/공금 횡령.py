n, m = map(int, input().split())
cost = dict()

result = 0

for i in range(n):
    a, b = input().split()
    cost[a] = int(b)

for i in range(m):
    c, d = input().split()
    if int(d) > cost[c] * 1.05:
        result += 1

print(result)
