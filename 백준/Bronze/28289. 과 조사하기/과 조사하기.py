p = int(input())
result = [0, 0, 0, 0]

for i in range(p):
    g, c, n = map(int, input().split())
    if g == 1:
        result[3] += 1
    elif c == 1 or c == 2:
        result[0] += 1
    elif c == 3:
        result[1] += 1
    else:
        result[2] += 1

print(*result, sep="\n")
