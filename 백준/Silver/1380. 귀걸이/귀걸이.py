import sys

input = sys.stdin.readline

result = list()
cnt = 1

while True:
    n = int(input())

    if n == 0:
        break

    names = [input().rstrip() for i in range(n)]
    seen = set()

    for i in range(2 * n - 1):
        ipt = input().split()
        if ipt[0] not in seen:
            seen.add(ipt[0])
        else:
            seen.discard(ipt[0])

    result.append(f"{cnt} {names[int(seen.pop()) - 1]}")
    cnt += 1

print(*result, sep="\n")
