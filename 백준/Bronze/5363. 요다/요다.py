n = int(input())

result = list()

for i in range(n):
    ipt = input().split()
    ipt = ipt[2:] + ipt[:2]

    result.append(" ".join(ipt))

print(*result, sep="\n")
