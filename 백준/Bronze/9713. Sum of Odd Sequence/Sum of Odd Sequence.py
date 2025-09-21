t = int(input())
result = list()

for i in range(t):
    n = int(input())
    result.append(((1 + n) // 2) ** 2)

print(*result, sep="\n")
