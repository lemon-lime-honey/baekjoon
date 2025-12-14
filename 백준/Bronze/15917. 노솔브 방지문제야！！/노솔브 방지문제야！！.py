q = int(input())
result = list()

for i in range(q):
    a = int(input())
    result.append(1 if a & (-a) == a else 0)

print(*result, sep="\n")