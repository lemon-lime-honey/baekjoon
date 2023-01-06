import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if lst[0] == 0:
        break
    result = 0
    for i in range(1, len(lst)):
        if i == 1:
            result += lst[i]
        elif i % 2 == 0:
            result -= lst[i]
        else:
            result *= lst[i]
    print(result)