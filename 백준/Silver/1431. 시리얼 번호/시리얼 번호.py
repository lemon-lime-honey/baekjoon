from functools import cmp_to_key
import sys
input = sys.stdin.readline


def compare(x, y):
    if len(x) < len(y):
        return -1
    elif len(x) > len(y):
        return 1

    numX, numY = 0, 0

    for i in range(len(x)):
        if x[i].isdigit():
            numX += int(x[i])
        if y[i].isdigit():
            numY += int(y[i])
      
    if numX < numY:
        return -1
    elif numX > numY:
        return 1

    if x < y:
        return -1
    elif x > y:
        return 1

    return 0


n = int(input())
lst = list()

for i in range(n):
    lst.append(input().rstrip())

result = sorted(lst, key=cmp_to_key(compare))
print(*result, sep='\n')