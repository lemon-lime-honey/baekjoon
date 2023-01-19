n = int(input())

for i in range(n):
    x = int(input())
    print(f'{x} is ', end = '')
    if x % 2 == 0:
        print('even')
    else:
        print('odd')