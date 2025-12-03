u = list(map(int, input().split()))
d = list(map(int, input().split()))
p = list(map(int, input().split()))

h = int(input())

result = 0

while True:
    if result % u[0] == 0:
        h -= u[1]
    if result % d[0] == 0:
        h -= d[1]
    if result % p[0] == 0:
        h -= p[1]

    if h <= 0:
        break

    result += 1

print(result)
