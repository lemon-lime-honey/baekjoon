n, m = map(int, input().split())
result = list()

for i in range(n):
    ipt = list(map(int, input().split()))
    temp = list()
    for j in range(0, 3 * m, 3):
        value = 2126 * ipt[j] + 7152 * ipt[j + 1] + 722 * ipt[j + 2]
        if value < 510000:
            temp.append("#")
        elif value < 1020000:
            temp.append("o")
        elif value < 1530000:
            temp.append("+")
        elif value < 2040000:
            temp.append("-")
        else:
            temp.append(".")
    result.append("".join(temp))

print(*result, sep="\n")