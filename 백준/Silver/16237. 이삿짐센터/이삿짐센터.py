a, b, c, d, e = map(int, input().split())
result = e + d
a -= d

while c > 0:
    result += 1
    if b > 0:
        b -= 1
        c -= 1
    elif a > 0:
        a -= 2
        c -= 1
    else:
        c -= 1

while b > 0:
    result += 1
    if b > 1 and a > 0:
        b -= 2
        a -= 1
    elif b > 0 and a > 0:
        b -= 1
        a -= 3
    else:
        b -= 2

while a > 0:
    result += 1
    a -= 5

print(result)
