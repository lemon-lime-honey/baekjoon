n, q = map(int, input().split())
times = [int(input()) for i in range(n)]

table = [0 for i in range(n)]
table[0] = times[0]

result = list()

for i in range(1, n):
    table[i] = table[i - 1] + times[i]

for i in range(q):
    target = int(input())
    for j in range(n):
        if table[j] > target:
            result.append(j + 1)
            break

print(*result, sep="\n")