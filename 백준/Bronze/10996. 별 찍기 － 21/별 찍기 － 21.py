n = int(input())

if n == 1:
    print('*')
else:
    down = n // 2
    up = n - down
    result = '* ' * (up - 1) + '*\n' + ' *' * down
    for i in range(n):
        print(*result, sep='')