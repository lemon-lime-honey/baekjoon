import sys

input = sys.stdin.readline

result = list()
idx = 1

while True:
    ipt = input().rstrip()

    if ipt == "Was it a cat I saw?":
        break

    res = list()

    for i in range(0, len(ipt), idx + 1):
        res.append(ipt[i])

    result.append("".join(res))

    idx += 1

print(*result, sep="\n")
