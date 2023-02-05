n = int(input())
length = 2 * n - 1

for i in range(1, n + 1):
    print(' ' * ((length - (2 * i - 1)) // 2), end ='')
    for j in range(2 * i - 1):
        if j % 2:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()