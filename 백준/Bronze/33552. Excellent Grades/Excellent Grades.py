from decimal import Decimal

u = int(input())
n = int(input())

result = 0
num = 0
flag = True

for i in range(n):
    g, w = input().split()

    if not flag:
        continue

    g = int(Decimal(g) * 10)
    w = int(w)

    if g < 58:
        flag = False

    result += w * g
    num += w

result = 80 * (num + u) - result

if result <= 100 * u and flag:
    result = max(result, 58 * u)
    result = (result + u - 1) // u
    print(f"{result // 10}.{result % 10}")
else:
    print("IMPOSSIBLE")
