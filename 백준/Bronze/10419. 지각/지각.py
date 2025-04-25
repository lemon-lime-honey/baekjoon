t = int(input())
result = list()

for i in range(t):
    d = int(input())

    for j in range(int(d ** 0.5) + 1):
        if j + j ** 2 > d:
            result.append(j - 1)
            break
    else:
        result.append(int(d ** 0.5))

print(*result, sep="\n")
