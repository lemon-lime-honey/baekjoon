n = int(input())
result = 0

for i in range(1, n + 1):
    num, chk = i, 0

    while num:
        chk += num % 10
        num //= 10

    if i % chk == 0:
        result += 1

print(result)
