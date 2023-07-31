def star(n):
    if n == 1:
        return ['*']
    before = star(n - 1)
    result = list()
    result.append((4 * n - 3) * '*')
    result.append('*' + ' ' * (4 * n - 5) + '*')
    for i in range(len(before)):
        result.append('* ' + before[i] + ' *')
    result.append('*' + ' ' * (4 * n - 5) + '*')
    result.append((4 * n - 3) * '*')
    return result


n = int(input())
result = star(n)

for i in range(len(result)):
    print(*result[i], sep='')