n = int(input())
result = list()

result.append('*' * n + ' ' * (2 * n - 3) + '*' * n)
blank = 2 * n - 5

for i in range(1, n - 1):
    result.append(
        ' ' * i + '*' + ' ' * (n - 2) + '*' + 
        ' ' * blank + '*' + ' ' * (n - 2) + '*'
    )
    blank -= 2

result.append(' ' * (n - 1) + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')
blank = 1

for i in range(n - 2, 0, -1):
    result.append(
        ' ' * i + '*' + ' ' * (n - 2) + '*' + 
        ' ' * blank + '*' + ' ' * (n - 2) + '*'
    )
    blank += 2

result.append('*' * n + ' ' * (2 * n - 3) + '*' * n)

for line in result:
    print(*line, sep='')