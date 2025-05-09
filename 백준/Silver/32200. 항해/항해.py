n, x, y = map(int, input().split())
length = list(map(int, input().split()))
result = [0, 0]

for l in length:
    if l < x:
        result[1] += l
    else:
        result[0] += l // x
        result[1] += max(l % x - (l // x) * (y - x), 0)

print(*result, sep="\n")
