import sys

n = int(sys.stdin.readline())
lst = list()

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    lst.append((start, end))

lst = sorted(lst, key = lambda x: (x[1], x[0]))

res, before = 0, 0

for i in range(n):
    if lst[i][0] >= before:
        res += 1
        before = lst[i][1]

print(res)