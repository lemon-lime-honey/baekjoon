t = int(input())

result = list()

for i in range(t):
    n, m = map(int, input().split())
    if n < 12 or m < 4:
        result.append(-1)
    else:
        result.append(11 * m + 4)

print(*result, sep="\n")
