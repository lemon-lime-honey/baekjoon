n = int(input())
b = list(map(int, input().split()))
result = 0

while True:
    for i in range(n):
        if b[i] % 2:
            result += 1
            b[i] -= 1

    if b.count(0) == n:
        print(result)
        break

    result += 1

    for i in range(n):
        b[i] //= 2