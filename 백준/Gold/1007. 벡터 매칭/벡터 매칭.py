from itertools import combinations
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    result = 1e9
    n = int(input())
    dots = list()
    x_total = 0
    y_total = 0

    for j in range(n):
        x, y = map(int, input().split())
        x_total += x
        y_total += y
        dots.append((x, y))

    combs = combinations(range(n), n // 2)

    for comb in combs:
        x_one, x_two = 0, x_total
        y_one, y_two = 0, y_total
        for j in comb:
            x_one += dots[j][0]
            y_one += dots[j][1]
            x_two -= dots[j][0]
            y_two -= dots[j][1]
        temp = (y_two - y_one) ** 2 + (x_two - x_one) ** 2
        result = min(result, temp ** 0.5)

    print(result)