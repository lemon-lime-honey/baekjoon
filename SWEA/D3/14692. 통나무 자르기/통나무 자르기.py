tc = int(input())

for i in range(tc):
    n = int(input())
    print(f'#{i + 1} ', end = '')
    print('Bob' if n % 2 else 'Alice')