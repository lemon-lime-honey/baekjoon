n, m = map(int, input().split())

for i in range(n):
    ipt = list(input())
    for j in range(m // 2):
        if ipt[j] != ".":
            ipt[m - j - 1] = ipt[j]
        elif ipt[m - j - 1] != ".":
            ipt[j] = ipt[m - j - 1]
    print(*ipt, sep="")
