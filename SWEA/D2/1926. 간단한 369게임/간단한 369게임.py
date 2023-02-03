def chk(n):
    result = 0
    while n > 0:
        if n % 10 in (3, 6, 9):
            result += 1
        n //= 10
    return result

n = int(input())

for i in range(1, n + 1):
    temp = chk(i)
    if temp:
        print('-' * temp, end = ' ')
    else:
        print(i, end = ' ')