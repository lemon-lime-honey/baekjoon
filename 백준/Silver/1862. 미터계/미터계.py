num = int(input())
result = 0
exp = 0

while num:
    n = num % 10
    num //= 10

    if n > 4:
        result += (n - 1) * (9**exp)
    else:
        result += n * (9**exp)

    exp += 1

print(result)
