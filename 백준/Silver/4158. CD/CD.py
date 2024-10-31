import sys

input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    result = 0
    cd = set()

    for i in range(n):
        cd.add(int(input()))

    for i in range(m):
        if int(input()) in cd:
            result += 1

    print(result)
