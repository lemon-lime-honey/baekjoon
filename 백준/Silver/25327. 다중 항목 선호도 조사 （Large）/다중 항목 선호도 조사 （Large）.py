from collections import defaultdict
import sys

input = sys.stdin.readline

result = list()

n, m = map(int, input().split())

data = defaultdict(int)

for i in range(n):
    data[tuple(input().split())] += 1

for i in range(m):
    elem = input().split()
    cnt = 0

    for key, value in data.items():
        if elem[0] == "-":
            if elem[1] == "-":
                if elem[2] == "-":
                    cnt += value
                elif elem[2] == key[2]:
                    cnt += value
            else:
                if elem[2] == "-":
                    if elem[1] == key[1]:
                        cnt += value
                elif elem[1] == key[1] and elem[2] == key[2]:
                    cnt += value
        else:
            if elem[1] == "-":
                if elem[2] == "-":
                    if elem[0] == key[0]:
                        cnt += value
                elif elem[0] == key[0] and elem[2] == key[2]:
                    cnt += value
            else:
                if elem[2] == "-":
                    if elem[0] == key[0] and elem[1] == key[1]:
                        cnt += value
                elif elem[0] == key[0] and elem[1] == key[1] and elem[2] == key[2]:
                    cnt += value

    result.append(cnt)

print(*result, sep="\n")
