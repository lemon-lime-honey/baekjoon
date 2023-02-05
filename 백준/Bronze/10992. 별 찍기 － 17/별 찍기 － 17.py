n = int(input())
length = 2 * n - 1

for i in range(1, n):
    print(' ' * ((length - (2 * i - 1)) // 2), end ='')
    print('*', end = '')
    if i > 1:
        print(' '* (2 * i - 3), end = '')
        print('*')
    else:
        print()

print('*' * length)