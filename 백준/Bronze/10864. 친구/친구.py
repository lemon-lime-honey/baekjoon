n, m = map(int, input().split())

result = [0 for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    result[a] += 1
    result[b] += 1

print(*result[1:], sep="\n")
