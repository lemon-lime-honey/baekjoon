n, k = map(int, input().split())
g = list(map(int, input().split()))
result = list()

for i in range(k):
    chk = g[i] * 100 // n
    if chk <= 4:
        result.append(1)
    elif chk <= 11:
        result.append(2)
    elif chk <= 23:
            result.append(3)
    elif chk <= 40:
        result.append(4)
    elif chk <= 60:
        result.append(5)
    elif chk <= 77:
        result.append(6)
    elif chk <= 89:
        result.append(7)
    elif chk <= 96:
        result.append(8)
    else:
        result.append(9)

print(*result)