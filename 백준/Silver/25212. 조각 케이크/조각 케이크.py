def calc(idx, route):
    cake_size = 0

    for c in route:
        cake_size += 1/c

    if 0.99 <= cake_size <= 1.01:
        global result
        result += 1

    for i in range(idx + 1, n):
        calc(i, route + [cake[i]])


n = int(input())
cake = list(map(int, input().split()))
result = 0

calc(-1, list())

print(result)