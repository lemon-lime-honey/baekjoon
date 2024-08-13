n = int(input())
a = list(map(int, input().split()))
res = sorted([(i, j) for i, j in enumerate(a)], key=lambda x: x[1])
result = [0 for i in range(n)]

for i in range(n):
    result[res[i][0]] = i

print(*result)
